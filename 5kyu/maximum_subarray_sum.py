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

# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
# print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
# print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)


from time import monotonic
from random import randint

arr = [randint(-100, 100) for _ in range(20_000)]


start = monotonic()

for _ in range(1_000):
    max_sequence(arr)

print(monotonic() - start)


def max_sequence(arr):
    max_sum = 0
    temp_sum = 0
    for e in arr:
        temp_sum += e
        if max_sum < temp_sum:
            max_sum = temp_sum
        elif temp_sum < 0:
            temp_sum = 0
    return max_sum


start = monotonic()

for _ in range(1_000):
    max_sequence(arr)

print(monotonic() - start)
