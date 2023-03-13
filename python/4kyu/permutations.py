# https://www.codewars.com/kata/5254ca2719453dcc0b00027d
import itertools


def permutations(s):
    return [''.join(p) for p in set(itertools.permutations(s))]


print(sorted(permutations('n')), ['n'])
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
