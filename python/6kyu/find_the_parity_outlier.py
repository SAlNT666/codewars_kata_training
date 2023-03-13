# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
