# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    return n % 9 or n and 9


print(digital_root(16), 7)
