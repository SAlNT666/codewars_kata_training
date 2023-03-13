# https://www.codewars.com/kata/54d512e62a5e54c96200019e
from math import sqrt


def prime_factors(n):
    divs = list()
    for d in range(2, int(sqrt(n))):
        while not n % d:
            divs.append(d)
            n //= d
    if n != 1: divs.append(n)
    return ''.join('(' + str(d) + ('**' + str(c := divs.count(d))) * (c > 1) + ')' for d in sorted(set(divs)))


print(prime_factors(315))
