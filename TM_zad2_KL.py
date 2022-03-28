import os
from typing import List, Dict
from preproces_data import preproces_data
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from math import log
from Heaps import HeapsZipfLaws

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


def data_harvester(files_names, files_content: List[str]) -> List[int]:
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

    terms_token_number_list = [sorted(terms_number_list), sorted(token_number_list)]
    return df, terms_token_number_list


def Heaps_calculation(terms_token_list: List[int]) -> int:
    terms_tokens_number = [[6042, 17843, 23885.0, 24609, 25364, 34126, 58011.0, 83375.0, 107984.0],
                           [2135, 2558, 3697, 3980, 4196, 5207, 6848, 8211, 9256]]
    #for M, T in zip(terms_tokens_number[1], terms_token_number[0]):
    #log(M) = b * log(T) + logk


    #log(M) - log(M2) = b * (logT - logT2)


def main(path: str):

    files_names, files_content = get_files(path)
    df, terms_token_number_list = data_harvester(files_names, files_content)
    print(terms_token_number_list)
    HeapsZipfLaws.heaps_data_graph(terms_token_number_list)
    plt.plot(terms_token_number_list[1], terms_token_number_list[0])
    plt.show()
    df.to_csv('genrated_data.csv', header=True, index=True,mode='w')





if __name__ == "__main__":
    path = "C:\\Users\\Krzychiu\\Documents\\Analiza_danych_studia\\2 semestr\\Text Mining\\Zad_dom_2"
    main(path)
