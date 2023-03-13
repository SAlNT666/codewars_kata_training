# https://www.codewars.com/kata/5629db57620258aa9d000014
from collections import Counter


def mix(s1, s2):
    letter_counter = lambda s: Counter([l for l in s if l.islower() and s.count(l) > 1])
    s1 = letter_counter(s1)
    s2 = letter_counter(s2)

    return '/'.join(('=', '1', '2')[(s1[l] > s2[l]) + (s1[l] < s2[l]) * 2] + ':' + l * max(s1[l], s2[l])
                    for l in sorted(s1 | s2, key=lambda l: (-max(s1[l], s2[l]), -(s1[l] != s2[l]), s1[l] < s2[l], l)))


print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr", sep='\n', end='\n\n')

print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"), "2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz", sep='\n', end='\n\n')

