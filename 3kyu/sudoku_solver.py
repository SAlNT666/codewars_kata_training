def check_puzzle(v, point):
    p_i, p_j = point
    p_v = v
    if [puzzle[p_i][j] for j in range(9)].count(p_v) > 1 or [puzzle[i][p_j] for i in range(9)].count(p_v) > 1:
        return False

    # проверка на наличие такой цифры в квадрате кандидата
    if [puzzle[p[0]][p[1]] for p in
        [(i, j) for i in range(9) for j in range(9) if
         (p_i // 3) * 3 <= j < (p_i // 3) * 3 + 3 and (p_j // 3) * 3 <= i < (p_j // 3) * 3 + 3]].count(p_v) > 1:
        return False

    return True


def sudoku(puzzle):
    new_positions = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]
    new_values = [1] * len(new_positions)
    counter = 0
    while True:
        for v in range(new_values[counter], 10):
            puzzle[new_positions[counter][0]][new_positions[counter][1]] = v
            if check_puzzle(v, (new_positions[counter][0], new_positions[counter][1])):
                new_values[counter] = v
                counter += 1
                break
            else:
                puzzle[new_positions[counter][0]][new_positions[counter][1]] = 0
        else:
            for i in range(counter, len(new_values)):
                new_values[i] = 1
                puzzle[new_positions[i][0]][new_positions[i][1]] = 0
            counter -= 1
            new_values[counter] += 1

        if counter == len(new_positions) - 1:
            puzzle[new_positions[counter][0]][new_positions[counter][1]] = list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(puzzle[new_positions[-1][0]]))[0]

            return puzzle


def solve(puzzle):
    def guessAt():
        _, x, y = min((len(s), x, y) for x, row in enumerate(grid) for y, s in enumerate(row) if s)
        return x, y, grid[x][y].pop()

    def isValid():
        return all(bool(s) ^ bool(ans[x][y]) for x, row in enumerate(grid) for y, s in enumerate(row))

    def filterGridSets(i, j, v):
        nonlocal counts
        counts += 1
        ans[i][j] = v
        xS, yS = i // 3 * 3, j // 3 * 3
        for z in range(9):
            for a, b in ((i, z), (z, j), (xS + z // 3, yS + z % 3)):
                grid[a][b].discard(v)

    grid = [[{puzzle[x][y]} if puzzle[x][y] else {1, 2, 3, 4, 5, 6, 7, 8, 9} for y in range(9)] for x in range(9)]
    stk, counts, ans = [], 0, [[0] * 9 for _ in range(9)]

    while counts != 81:

        change = True
        while change:
            change = False
            for x in range(9):
                for y in range(9):
                    if len(grid[x][y]) == 1:
                        change = True
                        filterGridSets(x, y, grid[x][y].pop())

        if counts == 81: break

        if isValid():
            x, y, guess = guessAt()
            stk.append(([[set(s) for s in r] for r in grid], [r[:] for r in ans], x, y, guess, counts))
            grid[x][y].clear()
            filterGridSets(x, y, guess)
        else:
            grid, ans, x, y, guess, counts = stk.pop()
            grid[x][y].discard(guess)

    return ans


if __name__ == '__main__':

    # puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    #           [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #           [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #           [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #           [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #           [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #           [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #           [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #           [0, 0, 0, 0, 8, 0, 0, 7, 9]]
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
    # for i in range(100):
    #     # puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],[6, 0, 0, 1, 9, 5, 0, 0, 0],[0, 9, 8, 0, 0, 0, 0, 6, 0],[8, 0, 0, 0, 6, 0, 0, 0, 3],[4, 0, 0, 8, 0, 3, 0, 0, 1],[7, 0, 0, 0, 2, 0, 0, 0, 6],[0, 6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5],[0, 0, 0, 0, 8, 0, 0, 7, 9]]
    #     solve(puzzle)
    # print(datetime.now() - start)

    # import timeit
    # print(timeit.timeit("sudoku()", setup="from __main__ import sudoku, check_puzzle"))
