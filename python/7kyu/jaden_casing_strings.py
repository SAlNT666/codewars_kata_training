# https://www.codewars.com/kata/5390bac347d09b7da40006f6

def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())


print(toJadenCase("How can mirrors be real if eyes aren't real"), "How Can Mirrors Be Real If Eyes Aren't Real", sep='\n')
