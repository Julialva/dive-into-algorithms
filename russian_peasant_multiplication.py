import math

import pandas as pd


def RPM(x, y):
    halving = [min(x, y)]
    doubling = [max(x, y)]
    while min(halving) > 1:
        halving.append(math.floor(min(halving) / 2))
    while len(doubling) < len(halving):
        doubling.append(max(doubling) * 2)
    halfing_doubles = pd.DataFrame(zip(halving, doubling))
    halfing_doubles = halfing_doubles.loc[halfing_doubles[0] % 2 == 1, :]
    return sum(halfing_doubles.loc[:, 1])
