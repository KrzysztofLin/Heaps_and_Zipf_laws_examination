from math import log
from numpy import mean
import matplotlib.pyplot as plt
from typing import List, Dict
import pandas as pd


class HeapsLaw:
    def __init__(self, terms: List[int], tokens: List[int]): # initial function, list of numbers of terms and tokens has been used
        self.terms = terms
        self.tokens = tokens

    def heaps_parameters_calculation(self): # calculation of b and k
        b: float = 0
        count: int = 0
        for i in range(len(self.terms) - 1, 1, -1):
            try:
                pot_b = log(self.terms[i] / self.terms[i - 1], 10) / log(self.tokens[i] / self.tokens[i - 1], 10) # formula applied from scriptbook
                if pot_b < 1.5:
                    b += pot_b
                    count += 1
            except ZeroDivisionError:
                pot_b = 0

        b = b / count
        log_k = (log(mean(self.terms), 10) - log(mean(self.tokens), 10) * b)
        return b, pow(10, log_k)

    # heaps graph generator
    def heaps_graph(self):
        plt.xlabel('liczba tokenów')
        plt.ylabel('liczba termów')
        plt.title('wykres_heapsa_empiryczny')
        plt.plot(self.tokens, self.terms, label='wykres_heapsa_empiryczny')
        plt.show()

    # heaps graph generator to compare values
    def check_theoretical_dependency(self, b: float, k: float):
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
        plt.xlabel('log T')
        plt.ylabel('log M')
        plt.title('Heaps Zalezność teoretyczna z praktyczna')
        plt.scatter(log_M, log_T, label='wykres_heapsa_teoretyczny')
        plt.scatter(log_M_emp, log_T_emp, label='wykres_heapsa_empiryczny')
        plt.show()


def zipf_df_tranform_to_frequency_dict(df: pd.DataFrame) -> Dict[str, int]:
    frequency_dict = df.sum(axis=0)
    frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))
    return frequency_dict


class ZipfLaw:
    def __init__(self, df: pd.DataFrame):
        self.frequency_dict = zipf_df_tranform_to_frequency_dict(df)
        self.log_index = []
        self.log_frequency = []
        self.c = 0

    #function used to calculate c, based on frequency and rank
    def zipf_C_calculator(self) -> float:
        for index, frequency in enumerate(self.frequency_dict.values()):
            self.c += frequency * (index + 1)           # formulas applied from book
            self.log_index.append(log(index + 1))
            self.log_frequency.append(log(frequency))
        self.c = self.c/len(self.frequency_dict.values())
        return self.c

    # zipf graph generator to compare values
    def zipf_graph(self):
        log_cf = []
        log_rank = []
        for i in range(1, 10000):#round(self.log_frequency[-1])):
            log_rank.append(log(i))
            log_cf.append(log(self.c) - log(i))

        plt.xlabel('log10 rank')
        plt.ylabel('log10 cf')
        plt.title('Zipf Zalezność teoretyczna z praktyczna')
        plt.plot(log_rank, log_cf, label='wykres_zipfa_teoretyczny')
        plt.plot(self.log_frequency, self.log_index, label='wykres_zipfa_empiryczny')
        plt.show()