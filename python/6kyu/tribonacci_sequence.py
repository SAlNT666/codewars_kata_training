# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    a, b, c = signature
    for _ in range(n - 3):
        a, b, c = b, c, a + b + c
        signature.append(c)
    return [] if n == 0 else signature[:n]


print(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105], sep='\n', end='\n\n')
print(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44], sep='\n', end='\n\n')
