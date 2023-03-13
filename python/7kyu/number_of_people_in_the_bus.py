# https://www.codewars.com/kata/5648b12ce68d9daa6b000099

def number(bus_stops):
    return sum(x - y for x, y in bus_stops)


print(number([[10, 0], [3, 5], [5, 8]]), 5)
