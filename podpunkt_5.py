import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from typing import Dict
from Heaps_and_Zipf_laws import HeapsLaw, ZipfLaw
from random import choice
from collections import Counter
from typing import List


# simple generator
def abcdef_generator() -> str:
    text = ''
    for i in range(1000):
        text += choice('ab cdef ')
    return text


# simple data preprocessing, getting rid of blank signs
def preprocess_data(text: List[str]) -> List[str]:
    final_text = []
    for word in text:
        if word.isalnum():
           final_text.append(word)
    return final_text

# analogical function to the presented in main_HZ
def generate_multiple_functions_tokens_terms()-> tuple[pd.DataFrame, List[int], List[int]]:
    text_dict = {}
    token_number_list = []
    terms_number_list = []
    for element in range(1, 100):
        text = abcdef_generator()
        text = list(text.split(' '))
        tokens = preprocess_data(text)
        counted_tokens = Counter(tokens)
        text_dict[element] = counted_tokens
        if token_number_list != []:
            terms_number_list.append(len(counted_tokens))
            token_number_list.append(len(tokens))
        df = pd.DataFrame(data=text_dict).T.fillna(0)
        terms_number_list.append(len(df.columns))
        token_number_list.append(df.values.sum())
    return df, sorted(terms_number_list), sorted(token_number_list)


def main() -> None:
    df, terms_number_list, token_number_list = generate_multiple_functions_tokens_terms()
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


if __name__ == "__main__":
    main()