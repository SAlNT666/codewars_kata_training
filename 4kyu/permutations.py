import itertools


def permutations(s):
    return [''.join(p) for p in set(itertools.permutations(s))]


print(sorted(permutations('a')), ['a'])
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
