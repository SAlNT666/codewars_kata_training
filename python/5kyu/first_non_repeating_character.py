# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, s in enumerate(string_lower):
        if string_lower.count(s) == 1:
            return string[i]
    return ''


print(first_non_repeating_letter('stress'), 't')
print(first_non_repeating_letter('moonmen'), 'e')
print(first_non_repeating_letter('~><#~><'), '#')
