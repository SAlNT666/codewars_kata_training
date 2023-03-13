# https://www.codewars.com/kata/517abf86da9663f1d2000003/python


def to_camel_case(text):
    result = list(text)
    for i in range(len(text)-1):
        if text[i] in ('-', '_'):
            result[i], result[i+1] = '', result[i+1].upper()
    return ''.join(result)


print(to_camel_case(''), '', sep='\n', end='\n\n')
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior", sep='\n', end='\n\n')
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", sep='\n', end='\n\n')
