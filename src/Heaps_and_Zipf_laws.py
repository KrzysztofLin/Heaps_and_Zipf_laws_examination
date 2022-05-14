from math import log
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean


class HeapsLaw:
    """Class with functions created to check Heaps' law"""

    def __init__(self, terms: List[int], tokens: List[int]):
        self.terms = terms
        self.tokens = tokens

    def heaps_parameters_calculation(self):
        """to check Heaps law it is nessesary to get empirical parameters:
        b - values should be in interval 0.4 - 0.6,
        k - values should be in interval 30 - 100.
        Parameters will be used to check dependency between tokens and terms.
        """
        b: float = 0
        count: int = 0
        for i in range(len(self.terms) - 1, 1, -1):
            try:
                pot_b = log(self.terms[i] / self.terms[i - 1], 10) / log(
                    self.tokens[i] / self.tokens[i - 1], 10
                )
                if pot_b < 1.5:
                    b += pot_b
                    count += 1
            except ZeroDivisionError:
                pass

        b = b / count
        log_k = log(mean(self.terms), 10) - log(mean(self.tokens), 10) * b
        return b, pow(10, log_k)

    def heaps_graph(self):
        """'Heaps' graph visualizing data collected from documents"""
        plt.xlabel("number of tokens")
        plt.ylabel("number of terms")
        plt.title("Empirical heaps graph")
        plt.plot(self.tokens, self.terms, label="empirical heaps graph")
        plt.show()
        # plt.savefig("Empirical heaps graph.png")

    def check_theoretical_dependency(self, b: float, k: float):
        """graph visualising differences between theoretical (created based on b and k) and collected values"""
        log_M = []
        log_T = []
        log_M_emp = []
        log_T_emp = []

        for i in range(1000, 1000000, 1000):
            log_T.append(log(i))
            log_M.append(log(i) * b + log(k))

        for element in range(len(self.terms)):
            log_M_emp.append(log(self.terms[element]))
            log_T_emp.append(log(self.tokens[element]))
        plt.xlabel("log T")
        plt.ylabel("log M")
        plt.title("Heaps empirical vs theoretical dependency")
        plt.scatter(log_M, log_T, label="theoretical heaps graph")
        plt.scatter(log_M_emp, log_T_emp, label="empirical heaps graph")
        plt.show()
        # plt.savefig("Heaps empirical vs theoretical dependency.png")


class ZipfLaw:
    def __init__(self, data_frame: pd.DataFrame):
        self.frequency_dict = _zipf_df_transform_to_frequency_dict(data_frame)
        self.log_index = []
        self.log_frequency = []
        self.c = 0

    def zipf_C_calculator(self) -> float:
        """function used to calculate c, based on frequency and rank"""

        for index, frequency in enumerate(self.frequency_dict.values()):
            self.c += frequency * (index + 1)
            self.log_index.append(log(index + 1))
            self.log_frequency.append(log(frequency))
        self.c = self.c / len(self.frequency_dict.values())
        return self.c

    def zipf_graph(self):
        """graph visualising differences between theoretical (created based on c) and collected values"""
        log_cf = []
        log_rank = []
        for i in range(1, 10000):  # round(self.log_frequency[-1])):
            log_rank.append(log(i))
            log_cf.append(log(self.c) - log(i))

        plt.xlabel("log10 rank")
        plt.ylabel("log10 cf")
        plt.title("Zipf empirical vs theoretical dependency")
        plt.plot(log_rank, log_cf, label="theoretical zipf graph")
        plt.plot(self.log_frequency, self.log_index, label="theoretical zipf graph")
        plt.show()
        # plt.savefig("Zipf empirical vs theoretical dependency.png")


def _zipf_df_transform_to_frequency_dict(df: pd.DataFrame) -> Dict[str, int]:
    frequency_dict = df.sum(axis=0)
    frequency_dict = dict(
        sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
    )
    return frequency_dict
