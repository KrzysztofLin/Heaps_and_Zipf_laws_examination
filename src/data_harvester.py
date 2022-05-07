from collections import Counter
from typing import List, Tuple

import pandas as pd

from data_preprocesser import preprocess_data


def harvest_data(
    files_names, files_content: List[str]
) -> Tuple[pd.DataFrame, List[int], List[int]]:
    """ Function used to preprocessed loaded data.
    Create terms, tokens and vector matrix for tests with Heaps and Zipf law."""

    file_dict = {}
    token_number_list = []
    terms_number_list = []

    for file_name, raw_text in zip(files_names, files_content):
        preprocessed_tokens = preprocess_data(raw_text)
        counted_tokens = Counter(preprocessed_tokens)

        file_dict[file_name] = counted_tokens
        if token_number_list:
            terms_number_list.append(len(counted_tokens))
            token_number_list.append(len(preprocessed_tokens))

        data_frame = pd.DataFrame(data=file_dict).T.fillna(0)
        terms_number_list.append(len(data_frame.columns))
        token_number_list.append(data_frame.values.sum())
    return data_frame, sorted(terms_number_list), sorted(token_number_list)
