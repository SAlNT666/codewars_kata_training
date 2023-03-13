# https://www.codewars.com/kata/520b9d2ad5c005041100000f
import re


def pig_it(text):
    text_list = text.split()
    for i, word in enumerate(re.findall(r'\w+', text)):
        text_list[i] = text_list[i].replace(word, word[1:]+word[0]+'ay')
    return ' '.join(text_list)


print(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay', sep='\n', end='\n\n')
