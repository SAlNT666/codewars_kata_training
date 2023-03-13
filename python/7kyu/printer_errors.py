# https://www.codewars.com/kata/56541980fa08ab47a0000040

def printer_error(s):
    return f'{len([l for l in s if l not in "abcdefghijklm"])}/{len(s)}'


print(printer_error('aaabbbbhaijjjm'), '0/14')
