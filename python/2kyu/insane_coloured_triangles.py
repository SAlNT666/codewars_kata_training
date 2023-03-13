# https://www.codewars.com/kata/5a331ea7ee1aae8f24000175

from math import log

rules = {'RR': 'R', 'GG': 'G', 'BB': 'B',
         'BG': 'R', 'RB': 'G', 'RG': 'B',
         'GB': 'R', 'BR': 'G', 'GR': 'B'}


def triangle(row):
    n = len(row)
    if n == 1:
        return row
    else:
        d = n - 3 ** int(log(n - 1, 3))
        return rules[triangle(row[:d]) + triangle(row[-d:])]


print(triangle('GB'), 'R')
print(triangle('RRR'), 'R')
print(triangle('RGBGBR'), 'B')
print(triangle('RBRGBRB'), 'G')
