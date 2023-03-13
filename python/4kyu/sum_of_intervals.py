# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    x, res = intervals[0][0], 0
    for s, e in intervals:
        if e >= x:
            res += e - (x, s)[s > x]
            x = e
    return res


print(sum_of_intervals([(1, 4), (7, 10), (4, 5)]), 7)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)

from time import monotonic


start = monotonic()

for i in range(1_000_000):
    sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40), (1, 4), (7, 10), (4, 5)])

print(monotonic() - start)

def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s


start = monotonic()

for i in range(1_000_000):
    sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40), (1, 4), (7, 10), (4, 5)])

print(monotonic() - start)
