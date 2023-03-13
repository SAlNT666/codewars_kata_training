# https://www.codewars.com/kata/530e15517bc88ac656000716

import string


def rot13(message):
    alphabet = string.ascii_lowercase + string.ascii_lowercase
    result = []
    for l in message:
        if l.isalpha():
            result.append(alphabet[alphabet.index(l) + 13] if l.islower()
                          else alphabet[alphabet.index(l.lower()) + 13].upper())
        else: result.append(l)
    return ''.join(result)


print(rot13('test'), 'grfg', sep='\n', end='\n\n')
