import matplotlib.pyplot as plt
import math

class HeapsZipfLaws:
    def __init__(self, data_points):
        self.data_points = data_points

    def heaps_data_graph(self, data_points):
        tokens = data_points[1]
        terms = data_points[0]
        for i in range(len(terms) - 1, 1, -2):
            b = math.log(terms[i] - terms[i - 1]) / math.log(tokens[i] / tokens[i - 1])
            print(b)


import math
import matplotlib.pyplot as plt

terms = [2135, 2558, 3134, 3180, 3421, 3980, 3987, 4196, 4335, 4417, 4795, 5035, 5207, 5707, 5750, 7006, 7050, 7954,
         8371, 10022, 11382, 11619, 15346, 16006, 16500, 16951, 17482, 17948, 19272, 20035, 21454, 22305, 22710]
tokens = [6042, 10927, 12670, 17062, 17843, 19494, 22478, 23606, 24609, 25364, 34126, 35148.0, 35270, 36873, 40845,
          52210.0, 56642, 58252.0, 85822, 99097.0, 116940.0, 154977, 271917.0, 306043.0, 331407.0, 356016.0, 379622.0,
          416495.0, 473137.0, 508407.0, 594229.0, 605156.0, 624650.0]

b = 0
count = 0
for i in range(len(terms) - 1, 1, -2):
    count += 1
    pot_b = math.log(terms[i] / terms[i - 1]) / math.log(tokens[i] / tokens[i - 1])
    if pot_b < 1.5:
        b += pot_b

print(b / count)
plt.plot(tokens, terms)
plt.show()