# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints, s):
    seen = set()
    for n in ints:
        diff = s - n
        if diff in seen:
            return [diff, n]
        seen.add(n)


print(sum_pairs([11, 3, 7, 5], 10), [3, 7])
