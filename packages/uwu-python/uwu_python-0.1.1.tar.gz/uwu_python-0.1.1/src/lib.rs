use uwuifier::uwuify_str_sse;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use unidecode::unidecode;
use rand::Rng;

#[pyfunction]
fn uwu(text: &str) -> PyResult<String> {
    let mut decoded = unidecode(text);
    let choices = [
    " ",
    " UWU",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " MEOW",
    " woof woof arf grr >_<",
    " RAWR",
    ];
    let mut rng = rand::thread_rng();
    let choice = choices[rng.gen_range(0..choices.len())];
    let mut value = uwuify_str_sse(&decoded);
    value.push_str(choice);
    Ok(value)
}

#[pymodule]
fn uwu_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(uwu, m)?)?;
    Ok(())
}   



