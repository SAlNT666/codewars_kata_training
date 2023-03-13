# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    max_sum = 0
    temp_sum = 0
    for i in arr:
        temp_sum = temp_sum + i
        if max_sum < temp_sum:
            max_sum = temp_sum
        elif temp_sum < 0:
            temp_sum = 0
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)
