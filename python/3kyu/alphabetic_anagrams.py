# https://www.codewars.com/kata/53e57dada0cb0400ba000688
import math
from collections import Counter


def listPosition(word):
    if len(word) == 1:
        return 1
    else:
        return sorted(word).index(word[0]) * calculate_permutations(word) // len(word) + listPosition(word[1:])


def calculate_permutations(word):
    return math.factorial(len(word)) // math.prod(math.factorial(c) for c in Counter(word).values())


print(listPosition('ABAB'))
print('-' * 50)
print(listPosition('AA'))
print('-' * 50)
print(listPosition('BAAA'))
print('-' * 50)
