def get_count(sentence):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return sum(sentence.count(v) for v in vowels)
