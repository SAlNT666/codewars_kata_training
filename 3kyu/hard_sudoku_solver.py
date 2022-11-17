def solve(puzzle):

    def guess_at():
        i, j = min([(i, j) for i, row in enumerate(grid) for j, s in enumerate(row) if s],
                   key=lambda x: min(len(grid[x[0]][x[1]]), x[0], x[1]))
        return i, j, grid[i][j].pop()

    def is_valid():
        return all(bool(s) ^ bool(ans[i][j]) for i, row in enumerate(grid) for j, s in enumerate(row))

    def filter_grid_sets(i, j, v):
        nonlocal counts
        counts += 1
        ans[i][j] = v
        x_square, y_square = i // 3 * 3, j // 3 * 3
        for z in range(9):
            for a, b in ((i, z), (z, j), (x_square + z // 3, y_square + z % 3)):
                grid[a][b].discard(v)

    grid = [[{puzzle[i][j]} if puzzle[i][j] else {1, 2, 3, 4, 5, 6, 7, 8, 9} for j in range(9)] for i in range(9)]
    stk, counts, ans = [], 0, [[0] * 9 for _ in range(9)]

    while counts != 81:

        change = True
        while change:
            change = False
            for i in range(9):
                for j in range(9):
                    if len(grid[i][j]) == 1:
                        change = True
                        filter_grid_sets(i, j, grid[i][j].pop())

        if counts == 81: break

        if is_valid():
            i, j, guess = guess_at()
            stk.append(([[set(s) for s in row] for row in grid], [row[:] for row in ans], i, j, guess, counts))
            grid[i][j].clear()
            filter_grid_sets(i, j, guess)
        else:
            grid, ans, i, j, guess, counts = stk.pop()
            grid[i][j].discard(guess)

    return ans


if __name__ == '__main__':
    puzzle = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
              [0, 0, 0, 4, 0, 6, 0, 0, 0],
              [0, 0, 5, 0, 7, 0, 3, 0, 0],
              [0, 6, 0, 0, 0, 0, 0, 4, 0],
              [4, 0, 1, 0, 6, 0, 5, 0, 8],
              [0, 9, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 7, 0, 3, 0, 2, 0, 0],
              [0, 0, 0, 7, 0, 5, 0, 0, 0],
              [1, 0, 0, 0, 4, 0, 0, 0, 7]]

    for row in solve(puzzle):
        print(*row)

    # from datetime import datetime
    # start = datetime.now()
    # for i in range(1000):
    #     solve(puzzle)
    # print(datetime.now() - start)

    # import timeit
    # print(timeit.timeit("solve(puzzle)", setup="from __main__ import solve, puzzle"))