# https://www.codewars.com/kata/5917a2205ffc30ec3a0000a8
from itertools import permutations, product
from copy import deepcopy


def solve_puzzle(clues):
    size = len(clues) // 4
    check = lambda p, n: n == 0 or n == sum(max(p[:i]) < p[i] for i in range(1, size)) + 1
    clues = [clues[size * i:size * i + size] for i in range(4)]

    possible_rows = [[p for p in permutations(range(1, size + 1))
                      if check(p, clues[3][::-1][i]) and check(p[::-1], clues[1][i])] for i in range(size)]

    possible_cols = [[p for p in permutations(range(1, size + 1))
                      if check(p, clues[0][i]) and check(p[::-1], clues[2][::-1][i])] for i in range(size)]

    while any(len(row) > 1 for row in possible_rows):
        possible_rows_copy = deepcopy(possible_rows)
        for i in range(size):
            for j in range(size):
                row_set = set(r[j] for r in possible_rows[i])
                col_set = set(c[i] for c in possible_cols[j])

                possible_scrapes = row_set & col_set

                possible_rows[i] = [row for row in possible_rows[i] if row[j] in possible_scrapes]
                possible_cols[j] = [col for col in possible_cols[j] if col[i] in possible_scrapes]

        if possible_rows_copy == possible_rows:
            for matrix in product(*possible_rows):
                if all(check(r, clues[0][i]) and check(r[::-1], clues[2][::-1][i]) for i, r in enumerate(zip(*matrix))):
                    return [list(r) for r in matrix]

    return [list(*r) for r in possible_rows]


clues = [7, 0, 0, 0, 2, 2, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 4]

#   3 2 2 3 2 1
# 4 • • • • • • 1
# 2 • • • • • • 2
# 2 • • • • • • 3
# 1 • • • • • • 3
# 2 • • • • • • 2
# 3 • • • • • • 2
#   3 4 2 2 1 5

expected = [[1, 5, 6, 7, 4, 3, 2],
            [2, 7, 4, 5, 3, 1, 6],
            [3, 4, 5, 6, 7, 2, 1],
            [4, 6, 3, 1, 2, 7, 5],
            [5, 3, 1, 2, 6, 4, 7],
            [6, 2, 7, 3, 1, 5, 4],
            [7, 1, 2, 4, 5, 6, 3]]

print(solve_puzzle(clues), expected, sep='\n', end='\n\n')


clues = [3, 3, 2, 1, 2, 2, 3, 4, 3, 2, 4, 1, 4, 2, 2, 4, 1, 4, 5, 3, 2, 3, 1, 4, 2, 5, 2, 3]

print(solve_puzzle(clues), sep='\n', end='\n\n')
