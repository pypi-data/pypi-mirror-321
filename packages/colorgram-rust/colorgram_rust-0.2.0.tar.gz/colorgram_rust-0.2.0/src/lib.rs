use dominant_color::get_colors;
use reqwest::blocking::get as get_response;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::{PyBytes, PyString};

#[pyclass(module = "colorgram_rust")]
pub struct Response {
    pub color: String,
    pub bytes: Option<Py<PyBytes>>, // Use Py<PyBytes> for thread safety

}

#[pymethods]
impl Response {
    #[getter]
    pub fn color(&self) -> String {
        return self.color.clone();
    }

    #[getter]
    pub fn bytes(&self) -> Option<Py<PyBytes>> {
        return self.bytes.clone();
    }

    #[new]
    pub fn new(color: String, bytes: Option<Py<PyBytes>>) -> Self {
        Response { color, bytes }
    }
}

#[pyfunction]
fn get_dominant_color(py: Python, input: PyObject, with_data: Option<bool>) -> PyResult<Response> {
    let with_data = with_data.unwrap_or(false);
    let mut bytes: Vec<u8> = vec![];

    // If input is a `PyBytes`, use it as image data
    if let Ok(data) = input.extract::<&PyBytes>(py) {
        bytes = data.as_bytes().to_vec();
    } else if let Ok(py_str) = input.extract::<&PyString>(py) {
        let value: String = py_str.to_str()?.to_string();
        println!("Received URL: {}", value);
        
        let response = get_response(&value).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("Failed to fetch image: {}", e))
        })?;

        bytes = response.bytes().map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("Failed to read image data: {}", e))
        })?.to_vec();
    } else {
        return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>("Input must be either bytes or a URL string"));
    }

    // Decode the image data
    let img = image::load_from_memory(&bytes).map_err(|e| {
        PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("Error decoding image: {}", e))
    })?;

    // Convert image to RGB
    let img_rgb = img.to_rgb8();
    let (width, height) = img_rgb.dimensions();
    let mut pixels: Vec<u8> = Vec::with_capacity((width * height * 3) as usize);
    for y in 0..height {
        for x in 0..width {
            let pixel = img_rgb.get_pixel(x, y);
            pixels.push(pixel[0]);
            pixels.push(pixel[1]);
            pixels.push(pixel[2]);
        }
    }

    let colors = get_colors(&pixels, false); // Assuming no alpha channel

    if let Some(dominant_color) = colors.first() {
        // Assuming dominant_color is a tuple of (u8, u8, u8)
        let hex_color = format!("#{:02X}{:02X}{:02X}", *dominant_color, *dominant_color, *dominant_color);
        
        let response_bytes = if with_data {
            Some(PyBytes::new(py, &bytes).into()) // Create PyBytes directly from bytes
        } else {
            None
        };
        
        return Ok(Response::new(hex_color, response_bytes));
    } else {
        Err(PyErr::new::<pyo3::exceptions::PyValueError, _>("Failed to find dominant color"))
    }
}

#[pymodule]
fn colorgram_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_dominant_color, m)?)?;
    Ok(())
}

