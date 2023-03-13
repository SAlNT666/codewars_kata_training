# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    count = 0
    while n > 9:
        count += 1
        x = 1
        n_copy = n
        while n_copy:
            n_copy, x = n_copy // 10, n_copy % 10 * x
        n = x
    return count


print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
