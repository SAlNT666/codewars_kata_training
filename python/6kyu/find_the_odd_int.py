# https://www.codewars.com/kata/54da5a58ea159efa38000836
import operator
from functools import reduce


def find_it(seq):
    return reduce(operator.xor, seq)


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
