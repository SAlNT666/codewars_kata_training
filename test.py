# def to_camel_case(text):
#     if text:
#         result = list(text)
#         result[0] = result[0].upper()
#         for i in range(len(text)-1):
#             if text[i] == '-' or text[i] == '_':
#                 result[i+1] = result[i+1].upper()
#         return ''.join(result).replace('-', '').replace('_', '')
#     else:
#         return ''
#
# print(to_camel_case('my_code-wars'))
#
#
#
# def to_jaden_case(string):
#     return ' '.join(w.capitalize() for w in string.split())
#
# print(to_jaden_case('How can mirrors be real if our eyes aren\'t real'))
#
#
#
# def printer_error(s):
#     return arg'{len([x for x in s if x not in "abcdefghijklm"])}/{len(s)}'
#
# print(printer_error('aaabbbcdgnjmmwyqz'))
#
#
#
# def digital_root(n):
#     result = 0
#
#     for d in [int(i) for i in str(n)]:
#         result += d
#
#     if result < 10:
#         return result
#     else:
#         return digital_root(result)
#
# print(digital_root(132189))
#
#
#
# def find_outlier(integers):
#     pre = sum([integers[i] % 2 for i in range(3)])
#     if pre < 2:
#         if pre == 0:
#             for n in integers[3:]:
#                 if n % 2:
#                     return n
#         else:
#             for n in integers[:3]:
#                 if n % 2:
#                     return n
#     else:
#         if pre == 3:
#             for n in integers[3:]:
#                 if n % 2 == 0:
#                     return n
#         else:
#             for n in integers[:3]:
#                 if n % 2 == 0:
#                     return n
#
# print(find_outlier([2, 0, 4, 10, 24, -3, 16, 100]))
#
#
#
# def number(bus_stops):
#     return sum(x - y for x, y in bus_stops)
#
# print(number([[10,0],[3,5],[5,8]]))
#
#
#
# def odd_or_even(arr):
#     return 'odd' if sum(arr) % 2 else 'even'
#
# print(odd_or_even([0, 1, 3]))
#
#
#
# def zero(arg=None): return 0 if not arg else arg(0)
# def one(arg=None): return 1 if not arg else arg(1)
# def two(arg=None): return 2 if not arg else arg(2)
# def three(arg=None): return 3 if not arg else arg(3)
# def four(arg=None): return 4 if not arg else arg(4)
# def five(arg=None): return 5 if not arg else arg(5)
# def six(arg=None): return 6 if not arg else arg(6)
# def seven(arg=None): return 7 if not arg else arg(7)
# def eight(arg=None): return 8 if not arg else arg(8)
# def nine(arg=None): return 9 if not arg else arg(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda x: x*y
# def divided_by(y): return lambda x: int(x/y)
#
# print(six(divided_by(two())))
#
#
#
# def make_readable(seconds):
#     return f'{seconds // 3600}:'.rjust(3, '0') +\
#            f'{seconds // 60 % 60}:'.rjust(3, '0') +\
#            f'{seconds % 60}'.rjust(2, '0')
#
# print(make_readable(86399))
#
#
#
# import string
# def rot13(message):
#     alphabet = string.ascii_lowercase + string.ascii_lowercase
#     result = []
#     for l in message:
#         if l.isalpha():
#             result.append(alphabet[alphabet.index(l) + 13] if l.islower() else alphabet[alphabet.index(l.lower()) + 13].upper())
#         else: result.append(l)
#     return ''.join(result)
#
# print(rot13("Test"))
#
#
#
# def delete_nth(order,max_e):
#     result = []
#     order_dict = {}
#     for n in order:
#         if n not in order_dict:
#             order_dict[n] = 1
#             result.append(n)
#         else:
#             if order_dict[n] < max_e:
#                 print(order_dict[n])
#                 order_dict[n] += 1
#                 result.append(n)
#     return result
#
# print(delete_nth([20,37,20,21], 1))
#
#
#
# def eureka(num):
#     return num == sum([int(d) ** (i+1) for i, d in enumerate(str(num))])
#
# def sum_dig_pow(a, b):
#     return list(filter(eureka, range(a, b+1)))
#
# print(sum_dig_pow(1, 100))
#
#
#
# import re
# def pig_it(text):
#     text_list = text.split()
#     for i, word in enumerate(re.findall('\w+', text)):
#         text_list[i] = text_list[i].replace(word, word[1:]+word[0]+'ay')
#     return ' '.join(text_list)
#
# print(pig_it('O tempora o mores!'))
#
#
#
# dict_keypad = {'1': ['2', '4'], '2': ['1', '3', '5'], '3': ['2', '6'],
#                '4': ['1', '5', '7'], '5': ['2', '4', '6', '8'], '6': ['3', '5', '9'],
#                '7': ['4', '8'], '8': ['5', '7', '9', '0'], '9': ['6', '8'],
#                '0': ['8']}
#
# from itertools import product
# def enumeration(possible_variants):
#     print(possible_variants)
#     result = list(product(*possible_variants))
#     return [''.join(l) for l in result]
#
# def get_pins(observed):
#     possible_variants = [[i] + dict_keypad[i] for i in observed]
#     return enumeration(possible_variants)
#
# print(get_pins('601'))
#
# def get_pins(observed):
#     if len(observed) == 1:
#         return [observed] + dict_keypad[observed]
#     else:
#         return [a + b for a in ([observed[0]] + dict_keypad[observed[0]]) for b in get_pins(observed[1:])]
#
# print(get_pins('130'))
#
#
#
# import math
# import re
#
# def zeros(n):
#     temp_num = str(math.factorial(n))[::-1]
#     result = re.search('0+', temp_num)
#     return len(result[0]) if result else 0
#
# def zeros(n):
#     n //= 5
#     return n + zeros(n) if n else 0
#
# print(zeros(6))
#
#
# def sum_pairs(ints, s):
#     seen = set()
#     for num in ints:
#         diff = s - num
#         if diff in seen:
#             return [diff, num]
#         seen.add(num)
#
# print(sum_pairs([-3, 5, 9, 13], 10))
#
#
#
# from itertools import combinations
#
# def choose_best_sum(t, k, ls):
#     return max(filter(lambda x: x <= t, [sum(dists) for dists in combinations(ls, k)]), default=None)
#
#
# print(choose_best_sum(230, 4, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]))
#
# import re
#
# def top_3_words(text):
#     res_dict = {}
#     for l in re.findall('[a-zA-Z\']+', text.lower()):
#         if re.search('\w', l):
#             if res_dict.get(l):
#                 res_dict[l] += 1
#             else:
#                 res_dict[l] = 1
#
#     return sorted(res_dict, key=res_dict.get, reverse=True)[:3]
#
#
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))



# def anagrams(word, words):
#     word = sorted(list(word))
#     return list(filter(lambda x: sorted(list(x)) == word, words))
#
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))



# def dirReduc(arr):
#     dir1 = " ".join(arr)
#     dir2 = dir1.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
#     dir3 = dir2.split()
#     return dirReduc(dir3) if len(dir3) < len(arr) else dir3
#
# print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))


# import math
#
# def get_all_divisors_brute(n):
#     result = set()
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             result.add(i ** 2)
#             result.add(int(n / i) ** 2)
#     return result
#
# def list_squared(m, n):
#     result = []
#     for i in range(m, n + 1):
#         sum_sq_i_divisors = sum(get_all_divisors_brute(i))
#         sqrt_sum_of_squares_of_i_divisors = math.sqrt(sum_sq_i_divisors)
#         if sqrt_sum_of_squares_of_i_divisors == math.floor(sqrt_sum_of_squares_of_i_divisors):
#             result.append([i, sum_sq_i_divisors])
#     return result
#
# print(list_squared(1, 250))


# def solution(number):
#     return sum(set(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number))))
#
# print(solution(15))


# battleField = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
#                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
#                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]
#
#
# def validate_battlefield(battleField):
#
#     ships_dict = {1: [], 2: [], 3: [], 4: []}
#     units = set()
#
#     for i, row in enumerate(battleField):
#         for j, elem in enumerate(row):
#             if elem:
#                 units.add((i, j))
#
#     for unit in units:
#         if (unit[0] + 1, unit[1]) in units:
#
#             if (unit[0] + 2, unit[1]) in units:
#
#                 if (unit[0] + 3, unit[1]) in units:
#                     ships_dict[4].append(((unit[0], unit[1]), (unit[0] + 1, unit[1]),
#                                           (unit[0] + 2, unit[1]), (unit[0] + 3, unit[1])))
#                     continue
#
#                 if not {(unit[0] - 1, unit[1]),
#                         (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
#                     ships_dict[3].append(((unit[0], unit[1]), (unit[0] + 1, unit[1]), (unit[0] + 2, unit[1])))
#                 continue
#
#             if not {(unit[0] - 1, unit[1]),
#                     (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
#                 ships_dict[2].append(((unit[0], unit[1]), (unit[0] + 1, unit[1])))
#
#             continue
#
#         if (unit[0], unit[1] + 1) in units:
#
#             if (unit[0], unit[1] + 2) in units:
#
#                 if (unit[0], unit[1] + 3) in units:
#
#                     ships_dict[4].append(((unit[0], unit[1]), (unit[0], unit[1] + 1),
#                                           (unit[0], unit[1] + 2), (unit[0], unit[1] + 3)))
#                     continue
#
#                 if not {(unit[0] - 1, unit[1]), (unit[0], unit[1] - 1),
#                         (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
#                     ships_dict[3].append(((unit[0], unit[1]), (unit[0], unit[1] + 1), (unit[0], unit[1] + 2)))
#                 continue
#
#             if not {(unit[0], unit[1] - 1),
#                     (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
#                 ships_dict[2].append(((unit[0], unit[1]), (unit[0], unit[1] + 1)))
#                 continue
#
#         if not {(unit[0] - 1, unit[1]), (unit[0], unit[1] - 1), (unit[0] + 1, unit[1]), (unit[0], unit[1] + 1),
#                 (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
#             ships_dict[1].append((unit[0], unit[1]))
#             continue
#
#     if [len(ships_dict[i]) for i in range(1, 5)] == [4, 3, 2, 1]:
#         return True
#     else:
#         return False
#
#
# print(validate_battlefield(battleField))



for x in range(3):
    print(x)
    if x == 2:
        break
else:
    print('hello')
