# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
