def max_sum(a, ranges):
    return max(sum(a[i] for i in range(r[0], r[1]+1)) for r in ranges)


print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3)]))
