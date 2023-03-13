# https://www.codewars.com/kata/583d171f28a0c04b7c00009c
from itertools import accumulate


def max_sum(a, ranges):
    acc = list(accumulate(a, initial=0))
    return max(acc[j + 1] - acc[i] for i, j in ranges)


print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3), (0, 4), (6, 8)]), 6)
