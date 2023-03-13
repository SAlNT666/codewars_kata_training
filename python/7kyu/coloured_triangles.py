# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111

COLORS = set('RGB')


def triangle(row):
    while len(row) > 1:
        row = [c if c == row[i + 1] else (COLORS - {c, row[i + 1]}).pop() for i, c in enumerate(row[:-1])]
    return row[0]


print(triangle('GB'), 'R')
print(triangle('RRR'), 'R')
print(triangle('RGBG'), 'B')
print(triangle('RBRGBRB'), 'G')
