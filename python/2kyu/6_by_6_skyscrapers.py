# https://www.codewars.com/kata/5679d5a3f2272011d700000d
from itertools import permutations


def solve_puzzle(clues):
    size = len(clues) // 4
    check = lambda p, n: n == 0 or n == sum(max(p[:i]) < p[i] for i in range(1, size)) + 1
    clues = [clues[size * i:size * i + size] for i in range(4)]

    possible_rows = [[p for p in permutations(range(1, size + 1))
                      if check(p, clues[3][::-1][i]) and check(p[::-1], clues[1][i])] for i in range(size)]

    possible_cols = [[p for p in permutations(range(1, size + 1))
                      if check(p, clues[0][i]) and check(p[::-1], clues[2][::-1][i])] for i in range(size)]

    while any(len(row) > 1 for row in possible_rows):
        for i in range(size):
            for j in range(size):
                row_set = set(r[j] for r in possible_rows[i])
                col_set = set(c[i] for c in possible_cols[j])

                possible_scrapes = row_set & col_set
                possible_rows[i] = [row for row in possible_rows[i] if row[j] in possible_scrapes]
                possible_cols[j] = [col for col in possible_cols[j] if col[i] in possible_scrapes]

    return tuple(tuple(*r) for r in possible_rows)


clues = (3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4)

#   3 2 2 3 2 1
# 4 • • • • • • 1
# 2 • • • • • • 2
# 2 • • • • • • 3
# 1 • • • • • • 3
# 2 • • • • • • 2
# 3 • • • • • • 2
#   3 4 2 2 1 5

expected = (
    (2, 1, 4, 3, 5, 6),
    (1, 6, 3, 2, 4, 5),
    (4, 3, 6, 5, 1, 2),
    (6, 5, 2, 1, 3, 4),
    (5, 4, 1, 6, 2, 3),
    (3, 2, 5, 4, 6, 1)
)

print(solve_puzzle(clues), expected, sep='\n', end='\n\n')


clues = (0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 3, 0, 0, 4, 0, 0, 0, 0, 4, 4, 0, 3, 0, 0)

expected = (
    (5, 6, 1, 4, 3, 2),
    (4, 1, 3, 2, 6, 5),
    (2, 3, 6, 1, 5, 4),
    (6, 5, 4, 3, 2, 1),
    (1, 2, 5, 6, 4, 3),
    (3, 4, 2, 5, 1, 6)
)
print(solve_puzzle(clues), expected, sep='\n', end='\n\n')
