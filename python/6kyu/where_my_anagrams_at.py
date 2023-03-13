# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    word = sorted(list(word))
    return list(filter(lambda x: sorted(list(x)) == word, words))


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'], sep='\n', end='\n\n')
