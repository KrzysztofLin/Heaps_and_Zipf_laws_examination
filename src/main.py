from data_harvester import harvest_data
from data_load import get_files
from Heaps_and_Zipf_laws import HeapsLaw, ZipfLaw


def main():
    files_names, files_content = get_files()
    data_frame, list_with_terms_numbers, list_with_token_numbers = harvest_data(
        files_names, files_content
    )
    heaps_law = HeapsLaw(list_with_terms_numbers, list_with_token_numbers)

    heaps_law.heaps_graph()
    b, k = heaps_law.heaps_parameters_calculation()
    print(f"B value {b}, k value {k}")
    heaps_law.check_theoretical_dependency(b, k)

    zipf_law = ZipfLaw(data_frame)
    print(f"For documents calculated c value was equal: {zipf_law.zipf_C_calculator()}")
    zipf_law.zipf_graph()

    # To analyze additional data, you can save file
    # data_frame.to_csv('generated_data.csv', header=True, index=True, mode='w')


if __name__ == "__main__":
    main()
