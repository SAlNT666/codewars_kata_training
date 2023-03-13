# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    return int(''.join(str(int(d) ** 2) for d in str(num)))


print(square_digits(3212), 9414)
print(square_digits(0), 0)
