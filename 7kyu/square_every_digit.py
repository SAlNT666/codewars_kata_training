def square_digits(num):
    return int(''.join(str(int(i) ** 2) for i in str(num)))


# print(square_digits(3212), 9414)
print(square_digits(0), 2542549640)
