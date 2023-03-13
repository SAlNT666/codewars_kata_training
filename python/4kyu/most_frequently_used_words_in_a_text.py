# https://www.codewars.com/kata/51e056fe544cf36c410000fb
from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w, _ in c.most_common(3)]


print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"], sep='\n', end='\n\n')
