
terms = [2135, 2558, 3134, 3180, 3421, 3980, 3987, 4196, 4335, 4417, 4795, 5035, 5207, 5707, 5750, 7006, 7050, 7954,
         8371, 10022, 11382, 11619, 15346, 16006, 16500, 16951, 17482, 17948, 19272, 20035, 21454, 22305, 22710]
tokens = [6042, 10927, 12670, 17062, 17843, 19494, 22478, 23606, 24609, 25364, 34126, 35148.0, 35270, 36873, 40845,
          52210.0, 56642, 58252.0, 85822, 99097.0, 116940.0, 154977, 271917.0, 306043.0, 331407.0, 356016.0, 379622.0,
          416495.0, 473137.0, 508407.0, 594229.0, 605156.0, 624650.0]

from math import log
import matplotlib.pyplot as plt
from typing import Dict


class HeapsZipfLaws:
    def __init__(self, data_points):
        self.data_points = data_points


    def heaps_parameters_calculation(terms, tokens):
        b = 0
        count = 0
        for i in range(len(terms) - 1, 1, -2):
            pot_b = log(terms[i] / terms[i - 1], 10) / log(tokens[i] / tokens[i - 1], 10)
            if pot_b < 1.5:
                b += pot_b
                count += 1
        b = b / count
        log_k = (log(terms[-1], 10) - log(tokens[-1], 10) * (b))
        return (b, pow(10, log_k))


    def heaps_graph(tokens, terms):
        plt.plot(tokens, terms, label='wykres_heapsa_empiryczny')
        plt.show()


    def check_teoretical_dependency(b, k, terms, tokens):
        log_M = []
        log_T = []
        log_M_emp = []
        log_T_emp = []

        for i in range(1000, 1000000, 1000):
            log_T.append(log(i))
            log_M.append(log(i) * b + log(k))

        for element in range(len(terms)):
            log_M_emp.append(log(terms[element]))
            log_T_emp.append(log(tokens[element]))
        plt.xlabel('log T')
        # naming the y axis
        plt.ylabel('log M')
        # giving a title to my graph
        plt.title('Zalezność teoretyczna z praktyczna')
        plt.scatter(log_M, log_T, label='wykres_heapsa_teoretyczny')
        plt.scatter(log_M_emp, log_T_emp, label='wykres_heapsa_empiryczny')
        plt.show()


    def zipf_tranform_to_frequency_dict():
        x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        frequency_dict = dict(sorted(x.items(), key=lambda item: item[1]))
        return frequency_dict


    # function used to calculate c, based on frequency and rank
    def zipf_parameters_calculation(frequency_dict: Dict[int, int]) -> float:
        # cf - frequency
        # c = cf/i
        c = 0
        log_frequency = []
        log_index = []
        for index, frequency in enumerate(frequency_dict):
            c += frequency / (index + 1)
            log_index.append(log(index + 1))
            log_frequency.append(log(frequency))
        return c, log_index, log_frequency


    def zipf_graph(c, log_index, log_frequency):
        log_cf = []
        log_rank = []
        for i in range(1, 100):
            log_rank.append(log(i))
            log_cf.append(log(c) - log(i))

        plt.xlabel('log10 rank')
        # naming the y axis
        plt.ylabel('log10 cf')
        # giving a title to my graph
        plt.title('Zalezność teoretyczna z praktyczna')
        plt.plot(log_rank, log_cf, label='wykres_zipfa_teoretyczny')
        plt.plot(log_frequency, log_index, label='wykres_zipfa_empiryczny')
        plt.show()