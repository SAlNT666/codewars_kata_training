# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, b + a
    return [a, b, a * b == prod]


print(productFib(4895), [55, 89, True])
print(productFib(5895), [89, 144, False])
print(productFib(0), [0, 1, True])
