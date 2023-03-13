# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

def spiralize(size):
    i = 1
    j = 0
    a = [[0] * (size + 3) for _ in range(size + 3)]
    x = 1
    flag = True

    while flag:
        flag = False
        while a[i][j+1] == 0 and a[i][j+2] != 1 and j < size:
            if a[i+1][j+1] != 1:
                flag = True
                a[i][j+1] = x
                j += 1
            else:
                break

        while a[i+1][j] == 0 and a[i+2][j] != 1 and i < size:
            if a[i + 1][j - 1] != 1:
                flag = True
                a[i+1][j] = x
                i += 1
            else:
                break

        while a[i][j-1] == 0 and a[i][j-2] != 1 and j > 1:
            if a[i - 1][j - 1] != 1:
                flag = True
                a[i][j-1] = x
                j -= 1
            else:
                break

        while a[i-1][j] == 0 and a[i-2][j] != 1 and a[i - 1][j + 1] != 1 and i > 1:
            if a[i - 1][j + 1] != 1:
                flag = True
                a[i-1][j] = x
                i -= 1
            else:
                break

    return [[a[i][j] for j in range(1, size+1)] for i in range(1, size+1)]


for row in spiralize(5):
    print(*row)
