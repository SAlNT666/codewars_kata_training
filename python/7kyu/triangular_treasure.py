# https://www.codewars.com/kata/525e5a1cb735154b320002c8

def triangular(n):
    return n > 0 and n * (n + 1) // 2


print(triangular(2), 3)
print(triangular(4), 10)
print(triangular(45), 1035)
print(triangular(-9), 0)
