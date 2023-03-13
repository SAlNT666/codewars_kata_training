# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    return str(max(n := [int(i) for i in numbers.split()])) + ' ' + str(min(n))


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
