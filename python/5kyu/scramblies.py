# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

def scramble(s1, s2):
    return all(s1.count(i) >= s2.count(i) for i in set(s2))


print(scramble('rkqodlw', 'world'), True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptingjava', 'javascript'), True)
