# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    result = []

    length = len(snail_map)
    width = len(snail_map[0])
    if length == 0 or width == 0:
        return result

    i_zero = 1
    j_zero = 0
    i = 0
    j = 0

    flag = True

    while flag:
        flag = False

        while j < width - 1:
            flag = True
            result.append(snail_map[i][j])
            j += 1

        while i < length - 1:
            flag = True
            result.append(snail_map[i][j])
            i += 1

        while j > j_zero:
            flag = True
            result.append(snail_map[i][j])
            j -= 1

        width -= 1
        j_zero += 1

        while i > i_zero:
            flag = True
            result.append(snail_map[i][j])
            i -= 1

        length -= 1
        i_zero += 1

    result.append(snail_map[i][j])

    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(snail(array))
