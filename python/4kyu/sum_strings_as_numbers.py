# https://www.codewars.com/kata/5324945e2ece5e1f32000370
from itertools import zip_longest


def sum_strings(x, y):
    result = list()
    e = 0
    for i, j in zip_longest(reversed(x), reversed(y), fillvalue='0'):
        s = int(i) + int(j) + e
        result.append(str(s % 10))
        e = (0, 1)[s > 9]
    return (str(e) * e + ''.join(result)[::-1].lstrip('0')) or '0'


print(''.join(sum_strings('125', '456')), 581)
