import os
from settings import PATH
from typing import List


# function to get filenames, and their content
def get_files(PATH: str) -> tuple[List[str], List[str]]:
    files_names = []
    files_content = []
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            files_names.append(file_name)
            file_path = f"{PATH}/{file_name}"
            files_content.append(read_text_file(file_path))
    return files_names, files_content


# file reader, used to read files
def read_text_file(file_path: str) -> str:
    with open(file_path, mode='r', encoding="utf8") as file_reader:
        text_file = file_reader.read()
    return text_file
