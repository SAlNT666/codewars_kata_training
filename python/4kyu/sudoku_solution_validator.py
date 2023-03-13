# https://www.codewars.com/kata/529bf0e9bdf7657179000008

def valid_solution(board):
    nums = set(range(1, 10))
    right_rows = (set(r) == nums for r in board)
    right_columns = (set(c) == nums for c in zip(*board))
    right_squares = (nums == set(board[i][j] for i in range(3 + 3 * o) for j in range(3 + 3 * o)) for o in range(3))
    return all((*right_rows, *right_columns, *right_squares))


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True)

print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]), False)
