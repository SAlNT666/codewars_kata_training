# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    res = [i for i in lst if i != 0]
    return res + [0] * (len(lst) - len(res))


# сортировка помедленнее будет
# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0)


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
