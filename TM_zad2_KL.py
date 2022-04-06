import os
from typing import List, Dict
from preproces_data import preproces_data
from collections import Counter
import pandas as pd
from Heaps import Heaps_Laws, Zipf_law

PATH = "C:\\Users\\Krzychiu\\Documents\\Analiza_danych_studia\\2 semestr\\Text Mining\\Text_Minning"


def get_files(PATH: str) -> tuple[List[str], List[str]]:
    files_names = []
    files_content = []
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            files_names.append(file_name)
            file_path = f"{PATH}\{file_name}"
            files_content.append(read_text_file(file_path))
    return files_names, files_content


def read_text_file(file_path: str) -> str:
    with open(file_path, mode='r', encoding="utf8") as f:
        readed_file = f.read()
    return readed_file


def data_harvester(files_names, files_content: List[str]) -> tuple[pd.DataFrame, List[int], List[int]]:
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


def main(PATH: str):

    files_names, files_content = get_files(PATH)
    df, terms_number_list, token_number_list = data_harvester(files_names, files_content)
    df.to_csv('genrated_data.csv', header=True, index=True, mode='w') #you can look through document
    #df = pd.read_csv(f"{PATH}\genrated_data.csv")

    #Heaps law
    heaps_law = Heaps_Laws(terms_number_list, token_number_list)
    #Heaps graph, visualizing data
    heaps_law.heaps_graph()
    b, k = heaps_law.heaps_parameters_calculation()
    print(f"B value {b}, k value {k}")
    heaps_law.check_teoretical_dependency(b, k)

    zipf_law = Zipf_law(df)
    print(f'Wartość c dla dokumentów wyniosła {zipf_law.zipf_C_calculator()}')
    zipf_law.zipf_graph()


if __name__ == "__main__":
    main(PATH)
