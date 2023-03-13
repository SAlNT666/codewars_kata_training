# https://www.codewars.com/kata/5626b561280a42ecc50000d1

def eureka(num):
    return num == sum([int(d) ** i for i, d in enumerate(str(num), start=1)])


def sum_dig_pow(a, b):
    return [x for x in range(a, b + 1) if eureka(x)]


print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89], sep='\n', end='\n\n')
