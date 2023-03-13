# https://www.codewars.com/kata/5a00a8b5ffe75f8888000080

def replace_zero(arr):
    total = 0
    left = i_zero = right = 0
    for i, v in enumerate(arr + [0]):
        if v:
            right += 1
        else:
            if left + right >= total:
                max_i_zero, total = i_zero, left + right
            left, i_zero, right = right, i, 0
    return max_i_zero


print(replace_zero([1, 1, 1, 0, 1, 1, 0, 1, 1, 1]), 6)
print(replace_zero([0, 1, 1, 1]), 0)
print(replace_zero([1, 1, 1, 0]), 3)
print(replace_zero([0, 1, 0, 0, 0, 0]), 2)
