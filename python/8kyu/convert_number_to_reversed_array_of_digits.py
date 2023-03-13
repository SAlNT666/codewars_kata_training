# https://www.codewars.com/kata/5583090cbe83f4fd8c000051

def digitize(n):
    return list(reversed([int(i) for i in str(n)]))


print(digitize(12345))
