# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
from itertools import groupby


def solution(args):
    result = []
    for _, g in groupby(enumerate(args), lambda i_x: i_x[0] - i_x[1]):
        temp_range = [x for _, x in g]
        if len(temp_range) > 2:
            result.append(f'{temp_range[0]}-{temp_range[-1]}')
        elif len(temp_range) == 2:
            result.append(f'{temp_range[0]},{temp_range[1]}')
        else:
            result.append(str(temp_range[0]))
    return ','.join(result)


print(solution([-6, -3, -2, -1, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
