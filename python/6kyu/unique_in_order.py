# https://www.codewars.com/kata/54e6533c92449cc251001667
from itertools import groupby


def unique_in_order(sequence):
    return [a[0] for a in groupby(sequence)]



print(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'], sep='\n', end='\n\n')
print(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'], sep='\n', end='\n\n')
print(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3], sep='\n', end='\n\n')


from time import monotonic


start = monotonic()

for i in range(1_000_000):
    unique_in_order('AAAABBBCCDAABBBHDFKHFSDHFGAJFAFAFAFSSSSSSAAAABBBCCDAABBBHDFKHFSDHFGAJFAFAFAFSSSSSSAAAABBBCCDAABBBHDFKHFSDHFGAJFAFAFAFSSSSSS')

print(monotonic() - start)


def unique_in_order(sequence):
    res = [None]
    for s in sequence:
        if res[-1] != s:
            res.append(s)
    return res[1:]


start = monotonic()

for i in range(1_000_000):
    unique_in_order('AAAABBBCCDAABBBHDFKHFSDHFGAJFAFAFAFSSSSSSAAAABBBCCDAABBBHDFKHFSDHFGAJFAFAFAFSSSSSSAAAABBBCCDAABBBHDFKHFSDHFGAJFAFAFAFSSSSSS')

print(monotonic() - start)
