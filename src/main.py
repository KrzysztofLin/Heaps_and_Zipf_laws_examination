import os
from typing import List
from data_preproceser import preprocess_data
from collections import Counter
from Heaps_and_Zipf_laws import HeapsLaw, ZipfLaw
import thmc

from data_load import get_files
from data_harvester import harvest_data


def main():
    # data loader, set your path
    files_names, files_content = get_files()

    # collecting and preprocessing data from documents, those variables will be used to check Heaps and Zipf laws
    data_frame, list_with_terms_numbers, list_with_token_numbers = harvest_data(files_names, files_content)

    # Class with functions to check Heaps law
    heaps_law = HeapsLaw(list_with_terms_numbers, list_with_token_numbers)

    # 'Heaps' graph visualizing data collected from documents
    heaps_law.heaps_graph()
    # b and k parameters of the collected data from documents
    b, k = heaps_law.heaps_parameters_calculation()
    print(f"B value {b}, k value {k}")

    # graph visualising differences between theoretical (created based on b and k) and collected values
    heaps_law.check_teoretical_dependency(b, k)

    # Class with functions to check Heaps law
    zipf_law = ZipfLaw(data_frame)
    print(f'For documents calculated c value was equal: {zipf_law.zipf_C_calculator()}')
    # graph visualising differences between theoretical (created based on c) and collected values
    zipf_law.zipf_graph()

    # To analyze additional data, you can save file
    # data_frame.to_csv('generated_data.csv', header=True, index=True, mode='w')


if __name__ == "__main__":
    main()
