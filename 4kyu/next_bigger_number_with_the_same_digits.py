# import itertools

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
    n = list(str(n))[::-1]
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            new_min = min(filter(lambda x: x > n[i], n[:i]))
            n[n.index(new_min)], n[i] = n[i], new_min
            n[:i] = sorted(n[:i], reverse=True)
            result = int(''.join(str(d) for d in n[::-1]))
            return result
    return -1


print(next_bigger(2017))
