use std::{
    fs::{read_to_string, File},
    io::BufReader,
    path::Path,
};

const INPUT_FILE_DIRECTORY: &str = "./src/challenges/inputs";

pub(crate) fn read_input_file(function_number: usize, input_file: String) -> String {
    let input_file_path_string = construct_input_file_path_as_string(function_number, input_file);
    let input_file_path = Path::new(&input_file_path_string);
    match read_to_string(input_file_path) {
        Ok(file_contents) => file_contents,
        Err(error) => panic!("{}", error),
    }
}

pub(crate) fn read_input_file_as_buffer(function_number: usize, input_file: String) -> BufReader<File> {
    let input_file_path_string = construct_input_file_path_as_string(function_number, input_file);
    let input_file = File::open(input_file_path_string).unwrap();
    BufReader::new(input_file)
}

fn construct_input_file_path_as_string(function_number: usize, input_file: String) -> String {
    format!("{}/{:02}/{}", INPUT_FILE_DIRECTORY, function_number, input_file)
}

pub fn test_fn() {
    println!("TEST");
}
