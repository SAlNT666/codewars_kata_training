def rgb(r, g, b):
    return '%02X%02X%02X' % tuple(max(0, min(x, 255)) for x in (r, g, b))


print(rgb(1, 2, 3), "010203")
print(rgb(-20, 275, 125), "00FF7D")
