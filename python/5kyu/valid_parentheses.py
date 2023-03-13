# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    c = 0
    for i in string:
        if i == '(': c += 1
        elif i == ')': c -= 1
        if c < 0: return False
    return (False, True)[c == 0]


print(valid_parentheses(")test"), False)
print(valid_parentheses("hi(hi)()"), True)
