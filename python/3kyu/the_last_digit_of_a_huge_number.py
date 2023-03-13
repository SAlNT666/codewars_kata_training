# https://www.codewars.com/kata/5518a860a73e708c0a000027

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = pow(x, (n, n % 4 + 4)[n > 1])
    return n % 10


test_data = [
    ([], 1),
    ([1], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([2, 0, 1], 1),
    ([2, 2, 101, 2], 6),
    ([4, 0], 1),
    ([2, 2, 2, 0], 4),
    ([12, 30, 21], 6),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([937640, 767456, 981242], 0),
    ([499942, 898102, 846073], 6)
]
for test_input, test_output in test_data:
    print(str(test_input).ljust(24), last_digit(test_input), test_output)
