# https://www.codewars.com/kata/55983863da40caa2c900004e

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
