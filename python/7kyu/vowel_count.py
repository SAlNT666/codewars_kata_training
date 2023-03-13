# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = ('n', 'e', 'i', 'o', 'u')
    return sum(sentence.count(v) for v in vowels)
