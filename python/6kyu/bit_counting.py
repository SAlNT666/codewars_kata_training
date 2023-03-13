# https://www.codewars.com/kata/526571aae218b8ee490006f4

def count_bits(n):
    return bin(n).count('1')


print(count_bits(1234), 5)
