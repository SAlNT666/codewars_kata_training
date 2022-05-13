import random
import copy

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def check_puzzle(puzzle, point):
    global counter
    p_i, p_j = point
    p_v = puzzle[p_i][p_j]

    if [puzzle[p_i][j] for j in range(9)].count(p_v) > 1 or [puzzle[i][p_j] for i in range(9)].count(p_v) > 1:
        return False

    p_square = []
    l_border = (p_i // 3) * 3
    r_border = l_border + 3
    u_border = (p_j // 3) * 3
    d_border = u_border + 3
    for i in range(9):
        for j in range(9):
            if l_border <= j < r_border and u_border <= i < d_border:
                p_square.append((i, j))
    if [puzzle[p[0]][p[1]] for p in p_square].count(p_v) > 1:
        return False

    return True


def get_zeros(puzzle):
    result = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                result.append((i, j))
    return result


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def solve_sudoku(puzzle, new_positions, new_values, counter):
    for v in range(new_values[counter], 10):
        puzzle[new_positions[counter][0]][new_positions[counter][1]] = v
        if check_puzzle(puzzle, (new_positions[counter][0], new_positions[counter][1])):
            new_values[counter] = v
            counter += 1
            break
        else:
            puzzle[new_positions[counter][0]][new_positions[counter][1]] = 0
    else:
        for i in range(counter, len(new_values)):
            new_values[i] = 0
        for p in range(counter, len(new_positions)):
            puzzle[new_positions[p][0]][new_positions[p][1]] = 0
        counter -= 1
        new_values[counter] += 1

    if counter == len(new_positions) - 1:
        puzzle[new_positions[counter][0]][new_positions[counter][1]] = list(digits - set(puzzle[8]))[0]
        return True, puzzle, new_positions, new_values, counter
    else:
        return False, puzzle, new_positions, new_values, counter


def sudoku(puzzle):
    new_positions = get_zeros(puzzle)
    new_values = [0] * len(new_positions)
    counter = 0
    while True:
        res, puzzle, new_positions, new_values, counter = solve_sudoku(puzzle, new_positions, new_values, counter)
        if res:
            return puzzle


for row in sudoku(puzzle):
    print(*row)
