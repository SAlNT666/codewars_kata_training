# https://www.codewars.com/kata/55aa075506463dac6600010d

CACHE = {}


def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum(x * x for x in divisors)
        return CACHE[number]

    return CACHE[number]


def list_squared(m, n):
    res = list()

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            res.append([number, divisors_sum])

    return res


print(list_squared(1, 250))
