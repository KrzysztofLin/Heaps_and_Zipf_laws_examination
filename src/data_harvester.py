from typing import List
from data_preproceser import preprocess_data
from collections import Counter
import pandas as pd


def harvest_data(files_names, files_content: List[str]) -> tuple[pd.DataFrame, List[int], List[int]]:
    ''' Function used to preprocessed loaded data.
     Create terms, tokens and vector matrix for tests with Heaps and Zipf law. '''
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
