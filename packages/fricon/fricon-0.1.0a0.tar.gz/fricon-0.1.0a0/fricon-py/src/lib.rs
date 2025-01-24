#![allow(
    clippy::missing_errors_doc,
    clippy::missing_panics_doc,
    clippy::must_use_candidate,
    clippy::significant_drop_tightening
)]

use std::{
    collections::HashMap,
    path::PathBuf,
    sync::{Arc, LazyLock},
};

use anyhow::{bail, ensure, Context, Result};
use arrow::{
    array::{
        downcast_array, make_array, Array, ArrayData, ArrayRef, BooleanArray, Float64Array,
        Int64Array, ListArray, RecordBatch, StringArray, StringBuilder, StructArray,
    },
    buffer::OffsetBuffer,
    datatypes::{DataType, Field, Fields, Schema},
    pyarrow::PyArrowType,
};
use chrono::{DateTime, Utc};
use clap::Parser;
use fricon::{
    cli::Cli,
    client::{self, Client, DatasetRecord, Info, DATASET_NAME},
    paths::WorkDirectory,
};
use itertools::Itertools;
use num::complex::Complex64;
use numpy::{AllowTypeChange, PyArrayLike1, PyArrayMethods};
use pyo3::{
    prelude::*,
    sync::GILOnceCell,
    types::{PyBool, PyComplex, PyDict, PyFloat, PyInt, PyList, PySequence, PyString},
};
use pyo3_async_runtimes::tokio::get_runtime;

#[pymodule]
pub mod _core {
    #[pymodule_export]
    pub use super::{
        complex128, main, trace_, Dataset, DatasetManager, DatasetWriter, Trace, Workspace,
    };
}

/// A client of fricon workspace server.
#[pyclass(module = "fricon._core")]
#[derive(Clone)]
pub struct Workspace {
    root: WorkDirectory,
    client: Client,
}

#[pymethods]
impl Workspace {
    /// Connect to a fricon server.
    ///
    /// Parameters:
    ///     path: The path to the workspace.
    ///
    /// Returns:
    ///     A workspace client.
    #[staticmethod]
    #[expect(clippy::needless_pass_by_value)]
    pub fn connect(path: PathBuf) -> Result<Self> {
        let root = WorkDirectory::new(&path)?;
        let ipc_file = root.ipc_file();
        let client = get_runtime().block_on(Client::connect(ipc_file))?;
        Ok(Self { root, client })
    }

    /// A dataset manager for this workspace.
    #[getter]
    pub fn dataset_manager(&self) -> DatasetManager {
        DatasetManager {
            workspace: self.clone(),
        }
    }
}

/// Manager of datasets in workspace.
#[pyclass(module = "fricon._core")]
#[derive(Clone)]
pub struct DatasetManager {
    workspace: Workspace,
}

#[pymethods]
impl DatasetManager {
    /// Create a new dataset.
    ///
    /// Parameters:
    ///     name: Name of the dataset.
    ///     description: Description of the dataset.
    ///     tags: Tags of the dataset. Duplicate tags will be add only once.
    ///     schema: Schema of the underlying arrow table. Can be only a subset of all columns,
    ///         other fields will be inferred from first row.
    ///     index: Names of index columns.
    ///
    /// Returns:
    ///     A writer of the newly created dataset.
    #[pyo3(signature = (name, *, description=None, tags=None, schema=None, index=None))]
    pub fn create(
        &self,
        name: String,
        description: Option<String>,
        tags: Option<Vec<String>>,
        schema: Option<PyArrowType<Schema>>,
        index: Option<Vec<String>>,
    ) -> Result<DatasetWriter> {
        let description = description.unwrap_or_default();
        let tags = tags.unwrap_or_default();
        let schema = schema.map_or_else(Schema::empty, |s| s.0);
        let index = index.unwrap_or_default();
        let writer = get_runtime().block_on(self.workspace.client.create_dataset(
            name,
            description,
            tags,
            index,
        ))?;
        Ok(DatasetWriter::new(writer, Arc::new(schema)))
    }

    /// Open a dataset by id.
    ///
    /// Parameters:
    ///     dataset_id: An integer `id` or UUID `uid`
    ///
    /// Returns:
    ///     The requested dataset.
    ///
    /// Raises:
    ///     RuntimeError: Dataset not found.
    pub fn open(&self, dataset_id: &Bound<'_, PyAny>) -> Result<Dataset> {
        if let Ok(id) = dataset_id.extract::<i64>() {
            let record = get_runtime().block_on(self.workspace.client.get_dataset_by_id(id))?;
            Ok(Dataset {
                workspace: Some(self.workspace.clone()),
                record,
            })
        } else if let Ok(uid) = dataset_id.extract::<String>() {
            let record = get_runtime().block_on(self.workspace.client.get_dataset_by_uid(uid))?;
            Ok(Dataset {
                workspace: Some(self.workspace.clone()),
                record,
            })
        } else {
            bail!("Invalid dataset id.")
        }
    }

    /// List all datasets in the workspace.
    ///
    /// Returns:
    ///     A pandas dataframe containing information of all datasets.
    pub fn list_all(&self, py: Python<'_>) -> PyResult<PyObject> {
        static FROM_RECORDS: GILOnceCell<PyObject> = GILOnceCell::new();

        let records = get_runtime().block_on(self.workspace.client.list_all_datasets())?;
        let py_records = records.into_iter().map(
            |DatasetRecord {
                 id,
                 info:
                     Info {
                         uid,
                         name,
                         description,
                         favorite,
                         index_columns,
                         created_at,
                         tags,
                         ..
                     },
             }| {
                let uid = uid.simple().to_string();
                (
                    id,
                    uid,
                    name,
                    description,
                    favorite,
                    index_columns,
                    created_at,
                    tags,
                )
            },
        );
        let py_records = PyList::new(py, py_records)?;
        let kwargs = PyDict::new(py);
        kwargs.set_item("index", "id")?;
        kwargs.set_item(
            "columns",
            [
                "id",
                "uid",
                "name",
                "description",
                "favorite",
                "index",
                "created_at",
                "tags",
            ],
        )?;
        FROM_RECORDS
            .get_or_try_init(py, || {
                Ok::<_, PyErr>(
                    py.import("pandas")?
                        .getattr("DataFrame")?
                        .getattr("from_records")?
                        .unbind(),
                )
            })?
            .call(py, (py_records,), Some(&kwargs))
    }
}

fn extract_float_array(values: &Bound<'_, PyAny>) -> Result<Float64Array> {
    if let Ok(PyArrowType(data)) = values.extract() {
        let arr = make_array(data);
        if *arr.data_type() == DataType::Float64 {
            return Ok(downcast_array(&arr));
        }
        bail!("The data type of the given arrow array is not float64.");
    }
    if let Ok(arr) = values.extract::<PyArrayLike1<'_, f64, AllowTypeChange>>() {
        let arr = arr.readonly();
        let arr = arr.as_array().into_iter().copied();
        let arr = Float64Array::from_iter_values(arr);
        return Ok(arr);
    }
    let py_type = values.get_type();
    bail!("Cannot convert values with type {py_type} to float64 array.");
}

fn extract_scalar_array(values: &Bound<'_, PyAny>) -> Result<ArrayRef> {
    if let Ok(PyArrowType(data)) = values.extract() {
        let arr = make_array(data);
        return match arr.data_type() {
            DataType::Boolean | DataType::Int64 | DataType::Float64 | DataType::Utf8 => Ok(arr),
            t @ DataType::Struct(_) if *t == get_complex_type() => Ok(arr),
            _ => bail!("The data type of the given arrow array is not float64."),
        };
    }
    if let Ok(sequence) = values.downcast::<PySequence>() {
        let data_type =
            infer_sequence_item_type(sequence).context("Inferring sequence item data type.")?;
        return build_array_from_sequence(&data_type, sequence);
    }
    let py_type = values.get_type();
    bail!("Cannot convert {py_type} to scalar array.");
}

fn wrap_as_list_array(array: ArrayRef) -> ListArray {
    ListArray::new(
        Arc::new(Field::new_list_field(array.data_type().clone(), false)),
        OffsetBuffer::from_lengths([array.len()]),
        array,
        None,
    )
}

/// 1-D list of values with optional x-axis values.
#[pyclass(module = "fricon._core")]
pub struct Trace {
    array: StructArray,
}

#[pymethods]
impl Trace {
    /// Create a new trace with variable x steps.
    ///
    /// Parameters:
    ///     xs: List of x-axis values.
    ///     ys: List of y-axis values.
    ///
    /// Returns:
    ///     A variable-step trace.
    #[staticmethod]
    pub fn variable_step(xs: &Bound<'_, PyAny>, ys: &Bound<'_, PyAny>) -> Result<Self> {
        let xs = extract_float_array(xs)?;
        let ys = extract_scalar_array(ys)?;
        ensure!(
            xs.len() == ys.len(),
            "Length of `xs` and `ys` should be equal."
        );
        let xs_list = wrap_as_list_array(Arc::new(xs));
        let ys_list = wrap_as_list_array(ys);
        let fields = vec![
            Field::new("xs", xs_list.data_type().clone(), false),
            Field::new("ys", ys_list.data_type().clone(), false),
        ];
        let array = StructArray::new(
            fields.into(),
            vec![Arc::new(xs_list), Arc::new(ys_list)],
            None,
        );
        Ok(Self { array })
    }

    /// Create a new trace with fixed x steps.
    ///
    /// Parameters:
    ///     x0: Starting x-axis value.
    ///     dx: Step size of x-axis values.
    ///     ys: List of y-axis values.
    ///
    /// Returns:
    ///     A fixed-step trace.
    #[staticmethod]
    pub fn fixed_step(x0: f64, dx: f64, ys: &Bound<'_, PyAny>) -> Result<Self> {
        let x0 = Float64Array::new_scalar(x0).into_inner();
        let dx = Float64Array::new_scalar(dx).into_inner();
        let ys = extract_scalar_array(ys)?;
        let ys_list = wrap_as_list_array(ys);
        let fields = vec![
            Field::new("x0", DataType::Float64, false),
            Field::new("dx", DataType::Float64, false),
            Field::new("ys", ys_list.data_type().clone(), false),
        ];
        let array = StructArray::new(
            fields.into(),
            vec![Arc::new(x0), Arc::new(dx), Arc::new(ys_list)],
            None,
        );
        Ok(Self { array })
    }

    /// Arrow data type of the trace.
    #[getter]
    pub fn data_type(&self) -> PyArrowType<DataType> {
        PyArrowType(self.array.data_type().clone())
    }

    /// Convert to an arrow array.
    ///
    /// Returns:
    ///     Arrow array.
    pub fn to_arrow_array(&self) -> PyArrowType<ArrayData> {
        PyArrowType(self.array.to_data())
    }
}

/// A dataset.
///
/// Datasets can be created and opened using the [`DatasetManager`][fricon.DatasetManager].
#[pyclass(module = "fricon._core")]
pub struct Dataset {
    workspace: Option<Workspace>,
    record: DatasetRecord,
}

impl Dataset {
    fn client(&self) -> Result<&Client> {
        self.workspace
            .as_ref()
            .context("No workspace.")
            .map(|w| &w.client)
    }
}

fn helper_module(py: Python<'_>) -> PyResult<&PyObject> {
    static IO_MODULE: GILOnceCell<PyObject> = GILOnceCell::new();
    IO_MODULE.get_or_try_init(py, || py.import("fricon._helper").map(Into::into))
}

#[pymethods]
impl Dataset {
    /// Name of the dataset.
    #[getter]
    pub fn name(&self) -> &str {
        &self.record.info.name
    }

    #[setter]
    pub fn set_name(&mut self, name: String) -> Result<()> {
        get_runtime().block_on(self.client()?.update_dataset_name(self.id(), name))
    }

    /// Description of the dataset.
    #[getter]
    pub fn description(&self) -> &str {
        &self.record.info.description
    }

    #[setter]
    pub fn set_description(&mut self, description: String) -> Result<()> {
        get_runtime().block_on(self.client()?.update_dataset_name(self.id(), description))
    }

    /// Tags of the dataset.
    #[getter]
    pub fn tags(&self) -> &[String] {
        &self.record.info.tags
    }

    #[setter]
    pub fn set_tags(&mut self, tags: Vec<String>) -> Result<()> {
        get_runtime().block_on(self.client()?.replace_dataset_tags(self.id(), tags))
    }

    /// Favorite status of the dataset.
    #[getter]
    pub const fn favorite(&self) -> bool {
        self.record.info.favorite
    }

    #[setter]
    pub fn set_favorite(&mut self, favorite: bool) -> Result<()> {
        get_runtime().block_on(self.client()?.update_dataset_favorite(self.id(), favorite))
    }

    /// Load the dataset as a polars DataFrame.
    ///
    /// Returns:
    ///     A polars DataFrame.
    pub fn to_polars(&self, py: Python<'_>) -> PyResult<PyObject> {
        helper_module(py)?.call_method1(py, "read_polars", (self.path()?.join(DATASET_NAME),))
    }

    /// Load the dataset as an Arrow Table.
    ///
    /// Returns:
    ///     An Arrow Table.
    pub fn to_arrow(&self, py: Python<'_>) -> PyResult<PyObject> {
        helper_module(py)?.call_method1(py, "read_arrow", (self.path()?.join(DATASET_NAME),))
    }

    /// Id of the dataset.
    #[getter]
    pub const fn id(&self) -> i64 {
        self.record.id
    }

    /// UUID of the dataset.
    #[getter]
    pub fn uid(&self) -> String {
        self.record.info.uid.simple().to_string()
    }

    /// Path of the dataset.
    #[getter]
    pub fn path(&self) -> Result<PathBuf> {
        // TODO: Non-workspace dataset
        Ok(self
            .workspace
            .as_ref()
            .context("No workspace.")?
            .root
            .data_dir()
            .join(&self.record.info.path))
    }

    /// Creation date of the dataset.
    #[getter]
    pub const fn created_at(&self) -> DateTime<Utc> {
        self.record.info.created_at
    }

    /// Index columns of the dataset.
    #[getter]
    pub fn index(&self) -> &[String] {
        &self.record.info.index_columns
    }
}

/// Writer for newly created dataset.
///
/// Writers are constructed by calling [`DatasetManager.create`][fricon.DatasetManager.create].
#[pyclass(module = "fricon._core")]
pub struct DatasetWriter {
    writer: Option<client::DatasetWriter>,
    id: Option<i64>,
    first_row: bool,
    schema: Arc<Schema>,
}

impl DatasetWriter {
    const fn new(writer: client::DatasetWriter, schema: Arc<Schema>) -> Self {
        Self {
            writer: Some(writer),
            id: None,
            first_row: true,
            schema,
        }
    }
}

fn infer_scalar_type(value: &Bound<'_, PyAny>) -> Result<DataType> {
    // Check bool first because bool is a subclass of int.
    if value.is_instance_of::<PyBool>() {
        Ok(DataType::Boolean)
    } else if value.is_instance_of::<PyInt>() {
        Ok(DataType::Int64)
    } else if value.is_instance_of::<PyFloat>() {
        Ok(DataType::Float64)
    } else if value.is_instance_of::<PyComplex>() {
        Ok(get_complex_type())
    } else if value.is_instance_of::<PyString>() {
        Ok(DataType::Utf8)
    } else {
        let py_type = value.get_type();
        bail!("Cannot infer scalar arrow data type for python type '{py_type}'.");
    }
}

fn infer_sequence_item_type(sequence: &Bound<'_, PySequence>) -> Result<DataType> {
    ensure!(
        sequence.len()? > 0,
        "Cannot infer data type for empty sequence."
    );
    let first_item = sequence.get_item(0)?;
    infer_scalar_type(&first_item)
}

fn infer_sequence_type(sequence: &Bound<'_, PySequence>) -> Result<DataType> {
    let item_type = infer_sequence_item_type(sequence)?;
    let data_type = DataType::new_list(item_type, false);
    Ok(data_type)
}

/// Infer [`arrow::datatypes::DataType`] from value in row.
///
/// Currently supports:
///
/// 1. Scalar types: bool, int, float, complex, str
/// 2. [`Trace`]
/// 3. [`arrow::array::Array`]
/// 4. Python Sequence protocol
///
/// TODO: support numpy array
fn infer_data_type(value: &Bound<'_, PyAny>) -> Result<DataType> {
    if let Ok(data_type) = infer_scalar_type(value) {
        Ok(data_type)
    } else if let Ok(trace) = value.downcast_exact::<Trace>() {
        Ok(trace.borrow().data_type().0)
    } else if let Ok(PyArrowType(data)) = value.extract() {
        let arr = make_array(data);
        Ok(arr.data_type().clone())
    } else if let Ok(sequence) = value.downcast::<PySequence>() {
        infer_sequence_type(sequence)
    } else {
        let py_type = value.get_type();
        bail!("Cannot infer arrow data type for python type '{py_type}'.");
    }
}

fn infer_schema(
    py: Python<'_>,
    initial_schema: &Schema,
    values: &HashMap<String, PyObject>,
) -> Result<Schema> {
    let new_fields: Vec<Field> = values
        .iter()
        .filter(|(name, _)| initial_schema.field_with_name(name).is_err())
        .map(|(name, value)| {
            let datatype = infer_data_type(value.bind(py))
                .with_context(|| format!("Inferring data type for column '{name}'."))?;
            anyhow::Ok(Field::new(name, datatype, false))
        })
        .try_collect()?;
    Schema::try_merge([initial_schema.clone(), Schema::new(new_fields)])
        .context("Failed to merge initial schema with inferred schema.")
}

fn build_array_from_sequence(
    data_type: &DataType,
    sequence: &Bound<'_, PySequence>,
) -> Result<ArrayRef> {
    match data_type {
        DataType::Boolean => {
            let mut builder = BooleanArray::builder(sequence.len()?);
            for v in sequence.try_iter()? {
                let v = v?.extract()?;
                builder.append_value(v);
            }
            Ok(Arc::new(builder.finish()))
        }
        DataType::Int64 => {
            let mut builder = Int64Array::builder(sequence.len()?);
            for v in sequence.try_iter()? {
                let v = v?.extract()?;
                builder.append_value(v);
            }
            Ok(Arc::new(builder.finish()))
        }
        DataType::Float64 => {
            let mut builder = Float64Array::builder(sequence.len()?);
            for v in sequence.try_iter()? {
                let v = v?.extract()?;
                builder.append_value(v);
            }
            Ok(Arc::new(builder.finish()))
        }
        DataType::Utf8 => {
            let mut builder = StringBuilder::new();
            for v in sequence.try_iter()? {
                let v = v?.extract::<String>()?;
                builder.append_value(v);
            }
            Ok(Arc::new(builder.finish()))
        }
        _ => bail!("Unsupported data type."),
    }
}

fn build_list(field: Arc<Field>, sequence: &Bound<'_, PySequence>) -> Result<ListArray> {
    let values = build_array_from_sequence(field.data_type(), sequence)?;
    let offsets = OffsetBuffer::from_lengths([values.len()]);
    Ok(ListArray::try_new(field, offsets, values, None)?)
}

fn build_array(value: &Bound<'_, PyAny>, data_type: &DataType) -> Result<ArrayRef> {
    if let Ok(PyArrowType(data)) = value.extract::<PyArrowType<ArrayData>>() {
        ensure!(
            data.data_type() == data_type,
            "Different data type: schema: {data_type}, value: {}",
            data.data_type()
        );
        return Ok(make_array(data));
    }
    match data_type {
        DataType::Boolean => {
            let Ok(value) = value.extract::<bool>() else {
                bail!("Not a boolean value.")
            };
            let array = BooleanArray::new_scalar(value).into_inner();
            Ok(Arc::new(array))
        }
        DataType::Int64 => {
            let Ok(value) = value.extract::<i64>() else {
                bail!("Failed to extract int64 value.")
            };
            let array = Int64Array::new_scalar(value).into_inner();
            Ok(Arc::new(array))
        }
        DataType::Float64 => {
            let Ok(value) = value.extract::<f64>() else {
                bail!("Failed to extract float64 value.")
            };
            let array = Float64Array::new_scalar(value).into_inner();
            Ok(Arc::new(array))
        }
        DataType::Utf8 => {
            let Ok(value) = value.extract::<String>() else {
                bail!("Failed to extract float64 value.")
            };
            let array = StringArray::new_scalar(value).into_inner();
            Ok(Arc::new(array))
        }
        // complex scalar
        t @ DataType::Struct(fields) if *t == get_complex_type() => {
            let Ok(value) = value.extract::<Complex64>() else {
                bail!("Failed to extract complex value.")
            };
            let real = Float64Array::new_scalar(value.re).into_inner();
            let imag = Float64Array::new_scalar(value.im).into_inner();
            let array =
                StructArray::new(fields.clone(), vec![Arc::new(real), Arc::new(imag)], None);
            Ok(Arc::new(array))
        }
        // Trace
        t @ DataType::Struct(_fields) => {
            let Ok(value) = value.downcast_exact::<Trace>() else {
                bail!("Failed to extract `Trace` value.")
            };
            let value = value.borrow();
            if *t != value.data_type().0 {
                bail!("Incompatible data type.")
            }
            let array = value.to_arrow_array().0;
            Ok(make_array(array))
        }
        // Sequence
        DataType::List(field) => {
            let Ok(value) = value.downcast() else {
                bail!("Value is not a python `Sequence`");
            };
            let list = build_list(field.clone(), value)?;
            Ok(Arc::new(list))
        }
        _ => {
            bail!("Unsupported data type {data_type}, please manually construct a `pyarrow.Array`.")
        }
    }
}

fn build_record_batch(
    py: Python<'_>,
    schema: Arc<Schema>,
    values: &HashMap<String, PyObject>,
) -> Result<RecordBatch> {
    ensure!(
        schema.fields().len() == values.len(),
        "Values not compatible with schema."
    );
    let columns = schema
        .fields()
        .into_iter()
        .map(|field| {
            let name = field.name();
            let value = values
                .get(name)
                .with_context(|| format!("Missing value {name}"))?
                .bind(py);
            build_array(value, field.data_type())
                .with_context(|| format!("Building array for column {name}"))
        })
        .try_collect()?;
    Ok(RecordBatch::try_new(schema, columns)?)
}

#[pymethods]
impl DatasetWriter {
    /// Write a row of values to the dataset.
    ///
    /// Parameters:
    ///     kwargs: Names and values in the row.
    #[pyo3(signature = (**kwargs))]
    pub fn write(
        &mut self,
        py: Python<'_>,
        kwargs: Option<HashMap<String, PyObject>>,
    ) -> Result<()> {
        let Some(values) = kwargs else {
            bail!("No data to write.")
        };
        self.write_dict(py, values)
    }

    /// Write a row of values to the dataset.
    ///
    /// Parameters:
    ///     values: A dictionary of names and values in the row.
    #[expect(clippy::needless_pass_by_value)]
    pub fn write_dict(&mut self, py: Python<'_>, values: HashMap<String, PyObject>) -> Result<()> {
        if values.is_empty() {
            bail!("No data to write.")
        }
        let Some(writer) = &mut self.writer else {
            bail!("Writer closed.");
        };
        if self.first_row {
            self.schema = Arc::new(infer_schema(py, &self.schema, &values)?);
            self.first_row = false;
        }
        let batch = build_record_batch(py, self.schema.clone(), &values)?;
        get_runtime().block_on(writer.write(batch))?;
        Ok(())
    }

    /// Id of the dataset.
    ///
    /// Raises:
    ///     RuntimeError: Writer is not closed yet.
    #[getter]
    pub fn id(&self) -> Result<i64> {
        self.id.context("Writer is not closed yet.")
    }

    /// Finish writing to dataset.
    pub fn close(&mut self) -> Result<()> {
        let writer = self.writer.take();
        if let Some(writer) = writer {
            let id = get_runtime().block_on(writer.finish())?;
            self.id = Some(id);
        }
        Ok(())
    }

    /// Enter context manager.
    pub const fn __enter__(slf: Py<Self>) -> Py<Self> {
        slf
    }

    /// Exit context manager and close the writer.
    ///
    /// Will call [`close`][fricon.DatasetWriter.close] method.
    pub fn __exit__(
        &mut self,
        _exc_type: PyObject,
        _exc_value: PyObject,
        _traceback: PyObject,
    ) -> Result<()> {
        self.close()
    }
}

fn get_complex_type() -> DataType {
    static COMPLEX: LazyLock<DataType> = LazyLock::new(|| {
        let fields = vec![
            Field::new("real", DataType::Float64, false),
            Field::new("imag", DataType::Float64, false),
        ];
        DataType::Struct(Fields::from(fields))
    });
    COMPLEX.clone()
}

fn get_trace_type(item: DataType, fixed_step: bool) -> DataType {
    let y_field = Field::new("ys", DataType::new_list(item, false), false);
    if fixed_step {
        let fields = vec![
            Field::new("x0", DataType::Float64, false),
            Field::new("dx", DataType::Float64, false),
            y_field,
        ];
        DataType::Struct(Fields::from(fields))
    } else {
        let x_field = Field::new("xs", DataType::new_list(DataType::Float64, false), false);
        let fields = vec![x_field, y_field];
        DataType::Struct(Fields::from(fields))
    }
}

/// Get a pyarrow data type representing 128 bit compelex number.
///
/// Returns:
///     A pyarrow data type.
#[pyfunction]
pub fn complex128() -> PyArrowType<DataType> {
    PyArrowType(get_complex_type())
}

/// Get a pyarrow data type representing [`Trace`][fricon.Trace].
///
/// Parameters:
///     item: Data type of the y values.
///     fixed_step: Whether the trace has fixed x steps.
///
/// Returns:
///     A pyarrow data type.
#[pyfunction]
pub fn trace_(item: PyArrowType<DataType>, fixed_step: bool) -> PyArrowType<DataType> {
    PyArrowType(get_trace_type(item.0, fixed_step))
}

#[pyfunction]
#[must_use]
pub fn main(py: Python<'_>) -> i32 {
    fn inner(cli: Cli) -> Result<()> {
        tokio::runtime::Builder::new_multi_thread()
            .enable_all()
            .build()?
            .block_on(async { fricon::main(cli).await })
    }
    fn ignore_python_sigint(py: Python<'_>) -> PyResult<()> {
        let signal = py.import("signal")?;
        let sigint = signal.getattr("SIGINT")?;
        let default_handler = signal.getattr("SIG_DFL")?;
        _ = signal.call_method1("signal", (sigint, default_handler))?;
        Ok(())
    }

    if ignore_python_sigint(py).is_err() {
        eprintln!("Failed to reset python SIGINT handler.");
        return 1;
    }

    // Skip python executable
    let argv = std::env::args_os().skip(1);
    let cli = match Cli::try_parse_from(argv) {
        Ok(cli) => cli,
        Err(e) => {
            let _ = e.print();
            return e.exit_code();
        }
    };
    match inner(cli) {
        Ok(()) => 0,
        Err(e) => {
            eprintln!("Error: {e:?}");
            1
        }
    }
}
