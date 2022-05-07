import os
from typing import List, Tuple

from settings import PATH


def get_files() -> Tuple[List[str], List[str]]:
    """Function get names of files and their content"""
    files_names = []
    files_content = []
    for file_name in os.listdir(PATH):
        if file_name.endswith(".txt"):
            files_names.append(file_name)
            file_path = f"{PATH}/{file_name}"
            files_content.append(read_text_file(file_path))
    return files_names, files_content


def read_text_file(file_path: str) -> str:
    """Function used to read files from given directory"""

    with open(file_path, mode="r", encoding="utf8") as file_reader:
        text_file = file_reader.read()
    return text_file
