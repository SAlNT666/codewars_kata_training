def triangle(row):
    while len(row) > 1:
        row = [c if c == row[i + 1] else ({'R', 'G', 'B'} - {c, row[i + 1]}).pop() for i, c in enumerate(row[:-1])]
    return row[0]


print(triangle('GB'), 'R')
print(triangle('RRR'), 'R')
print(triangle('RGBG'), 'B')
print(triangle('RBRGBRB'), 'G')
