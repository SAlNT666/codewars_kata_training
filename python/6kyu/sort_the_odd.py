# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d


def sort_array(source_array):
    odds = sorted((x for x in source_array if x % 2), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
