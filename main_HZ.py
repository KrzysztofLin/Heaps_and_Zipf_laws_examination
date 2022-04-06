import os
from typing import List
from data_preprocessing import preprocess_data
from collections import Counter
import pandas as pd
from Heaps_and_Zipf_laws import HeapsLaw, ZipfLaw

# to use the program set your path to the folder from which files will be loaded
PATH = "C:\\Users\\Krzychiu\\Documents\\Analiza_danych_studia\\2 semestr\\Text Mining\\Text_Minning"


# function to get filenames, and their content
def get_files(PATH: str) -> tuple[List[str], List[str]]:
    files_names = []
    files_content = []
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            files_names.append(file_name)
            file_path = f"{PATH}\{file_name}"
            files_content.append(read_text_file(file_path))
    return files_names, files_content


# file reader, used to read files
def read_text_file(file_path: str) -> str:
    with open(file_path, mode='r', encoding="utf8") as f:
        readed_file = f.read()
    return readed_file


# most important program's function, data is collected, preprocessed, divided and prepared for testing with Heaps, Zipf laws
def data_harvester(files_names, files_content: List[str]) -> tuple[pd.DataFrame, List[int], List[int]]:
    file_dict = {}
    token_number_list = []
    terms_number_list = []
    for file_name, raw_text in zip(files_names, files_content):
        preprocessed_tokens = preprocess_data(raw_text)
        counted_tokens = Counter(preprocessed_tokens)
        file_dict[file_name] = counted_tokens
        if token_number_list != []:
            terms_number_list.append(len(counted_tokens))
            token_number_list.append(len(preprocessed_tokens))
        df = pd.DataFrame(data=file_dict).T.fillna(0)
        terms_number_list.append(len(df.columns))
        token_number_list.append(df.values.sum())
    return df, sorted(terms_number_list), sorted(token_number_list)


def main(PATH: str) -> None:
    # data loader, set your path
    files_names, files_content = get_files(PATH)

    # collecting and preprocessing data from documents, those variables will be used to check Heaps and Zipf laws
    df, terms_number_list, token_number_list = data_harvester(files_names, files_content)

    # Class with functions to check Heaps law
    heaps_law = HeapsLaw(terms_number_list, token_number_list)
    # 'Heaps' graph visualizing data collected from documents
    heaps_law.heaps_graph()
    # b and k parameters of the collected data from documents
    b, k = heaps_law.heaps_parameters_calculation()
    print(f"B value {b}, k value {k}")

    # graph visualising differences between theoretical (created based on b and k) and collected values
    heaps_law.check_teoretical_dependency(b, k)

    # Class with functions to check Heaps law
    zipf_law = ZipfLaw(df)
    print(f'For documents calculated c value was equal: {zipf_law.zipf_C_calculator()}')
    # graph visualising differences between theoretical (created based on c) and collected values
    zipf_law.zipf_graph()

    # To analyze additional data, you can save file
    # df.to_csv('generated_data.csv', header=True, index=True, mode='w')
    # df = pd.read_csv(f"{PATH}\genrated_data.csv")


if __name__ == "__main__":
    main(PATH)
