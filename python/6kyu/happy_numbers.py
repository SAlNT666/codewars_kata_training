# https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e

def is_happy(n):
    while n > 4:
        r = 0
        while n:
            r, n = r + (n % 10) ** 2, n // 10
        n = r
    return n == 1


print(is_happy(1), True)
print(is_happy(7), True)
print(is_happy(901), True)
