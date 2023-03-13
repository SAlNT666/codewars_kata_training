# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

def zeros(n):
    n //= 5
    return n + zeros(n) if n else 0


print(zeros(6), 1)
