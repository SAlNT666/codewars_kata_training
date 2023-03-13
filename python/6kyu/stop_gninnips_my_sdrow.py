# https://www.codewars.com/kata/5264d2b162488dc400000001
import re


def spin_words(sentence):
    return re.sub(r'\w{5,}', lambda x: x[0][::-1], sentence)


print(spin_words('Hey fellow warriors'))
