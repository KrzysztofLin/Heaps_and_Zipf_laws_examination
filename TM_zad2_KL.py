import os
from typing import List, Dict
from preproces_data import preproces_data
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from math import log

def get_files(path: str) -> List[str]:
    files_names = []
    files_content = []
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            files_names.append(file_name)
            file_path = f"{path}\{file_name}"
            files_content.append(read_text_file(file_path))
    return files_names, files_content


def read_text_file(file_path: str) -> str:
    with open(file_path, mode='r', encoding="utf8") as f:
        readed_file = f.read()
    return readed_file


def data_harvester(files_names, files_content: List[str]) -> tuple[List[int], List[int]]:
    file_dict = {}
    token_number_list = []
    terms_number_list = []
    for file_name, raw_text in zip(files_names, files_content):
        preprocesed_tokens = preproces_data(raw_text)
        counted_tokens = Counter(preprocesed_tokens)
        file_dict[file_name] = counted_tokens

        if token_number_list != []:
            terms_number_list.append(len(counted_tokens))
            token_number_list.append(len(preprocesed_tokens))
        df = pd.DataFrame(data=file_dict).T.fillna(0)
        terms_number_list.append(len(df.columns))
        token_number_list.append(df.values.sum())

    return df, sorted(terms_number_list), sorted(token_number_list)


def main(path: str):
    files_names, files_content = get_files(path)
    df, terms_number_list, token_number_list = data_harvester(files_names, files_content)

    df.to_csv('genrated_data.csv', header=True, index=True,mode='w')


if __name__ == "__main__":
    path = "C:\\Users\\Krzychiu\\Documents\\Analiza_danych_studia\\2 semestr\\Text Mining\\Zad_dom_2"
    main(path)
