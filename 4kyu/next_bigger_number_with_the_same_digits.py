import itertools


# САМЫЙ ТУПОЙ ПОДХОД EVER
# def next_bigger(n):
#     difference = 9999999999
#     result = -1
#     for num in (int(''.join(str(d) for d in i)) for i in itertools.permutations([int(i) for i in str(n)], len(str(n)))):
#         new_difference = abs(num - n)
#         if num > n and new_difference < difference:
#             result = num
#             difference = new_difference
#     return result

def next_bigger(n):
    n = [int(d) for d in str(n)][::-1]

    result = -1
    for i in range(len(n)):
        new_min = None

        try:
            new_min = min(filter(lambda x: x > n[i], n[:i]))
        except ValueError:
            pass

        if new_min:

            print('n:', n)
            print('i:', i, 'i2:', -n[::-1].index(new_min) - 1)
            print('v:', n[i], 'v2:', n[-n[::-1].index(new_min) - 1])

            print('n:', n)
            print(n[i], n[-n[::-1].index(new_min) - 1])

            n[-n[::-1].index(new_min) - 1], n[i] = n[i], n[-n[::-1].index(new_min) - 1]

            print('n:', n)

            result = int(''.join(str(d) for d in n[::-1]))
            break
    return result


print(next_bigger(414))
