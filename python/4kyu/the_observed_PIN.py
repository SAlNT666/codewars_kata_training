# https://www.codewars.com/kata/5263c6999e0f40dee200059d

dict_keypad = {'1': ['2', '4'], '2': ['1', '3', '5'], '3': ['2', '6'],
               '4': ['1', '5', '7'], '5': ['2', '4', '6', '8'], '6': ['3', '5', '9'],
               '7': ['4', '8'], '8': ['5', '7', '9', '0'], '9': ['6', '8'],
               '0': ['8']}


def get_pins(observed):
    if len(observed) == 1:
        return dict_keypad[observed] + [observed]
    else:
        return [a + b for a in (dict_keypad[observed[0]] + [observed[0]]) for b in get_pins(observed[1:])]


expectations = [('8', ['5', '7', '8', '9', '0']),
                ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"])]

for tup in expectations:
    print(sorted(get_pins(tup[0])), sorted(tup[1]), sep='\n', end='\n\n')
