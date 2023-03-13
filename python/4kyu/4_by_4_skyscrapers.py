# https://www.codewars.com/kata/5671d975d81d6c1c87000022
from itertools import permutations


def solve_puzzle(clues):
    size = len(clues) // 4
    filter_p = lambda p, n: n == 0 or n == sum(max(p[:i]) < p[i] for i in range(1, size)) + 1
    clues = [clues[size * i:size * i + size] for i in range(4)]

    possible_rows = [[p for p in permutations(range(1, size + 1))
                      if filter_p(p, clues[3][::-1][i]) and filter_p(p[::-1], clues[1][i])] for i in range(size)]

    possible_cols = [[p for p in permutations(range(1, size + 1))
                      if filter_p(p, clues[0][i]) and filter_p(p[::-1], clues[2][::-1][i])] for i in range(size)]

    while any(len(row) > 1 for row in possible_rows):
        for i in range(size):
            for j in range(size):
                row_set = set(r[j] for r in possible_rows[i])
                col_set = set(c[i] for c in possible_cols[j])

                possible_scrapes = row_set & col_set
                possible_rows[i] = [row for row in possible_rows[i] if row[j] in possible_scrapes]
                possible_cols[j] = [col for col in possible_cols[j] if col[i] in possible_scrapes]

    return tuple(*zip(*possible_rows))
