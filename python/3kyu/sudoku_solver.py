# https://www.codewars.com/kata/5296bc77afba8baa690002d7

def sudoku(puzzle):
    def filter_grid_sets(i, j, v):
        nonlocal counts
        counts += 1
        ans[i][j] = v
        x_square, y_square = i // 3 * 3, j // 3 * 3
        for z in range(9):
            for a, b in ((i, z), (z, j), (x_square + z // 3, y_square + z % 3)):
                grid[a][b].discard(v)

    grid = [[{puzzle[i][j]} if puzzle[i][j] else {1, 2, 3, 4, 5, 6, 7, 8, 9} for j in range(9)] for i in range(9)]
    counts, ans = 0, [[0] * 9 for _ in range(9)]

    while counts != 81:

        change = True
        while change:
            change = False
            for i in range(9):
                for j in range(9):
                    if len(grid[i][j]) == 1:
                        change = True
                        filter_grid_sets(i, j, grid[i][j].pop())

    return ans


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

for row in sudoku(puzzle):
    print(*row)
