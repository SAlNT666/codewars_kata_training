# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

def even_or_odd(number):
    return ('Even', 'Odd')[number % 2]


print(even_or_odd(2))
