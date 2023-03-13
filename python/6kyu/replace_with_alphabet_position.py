# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    return ' '.join(str(ord(l) - 96) for l in text.lower() if l.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))
print('20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11')
