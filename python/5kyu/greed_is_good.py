# https://www.codewars.com/kata/5270d0d18625160ada0000e4

def score(dice):
    return dice.count(1) // 3 * 1000 + dice.count(1) % 3 * 100 + \
           dice.count(2) // 3 * 200 + \
           dice.count(3) // 3 * 300 + \
           dice.count(4) // 3 * 400 + \
           dice.count(5) // 3 * 500 + dice.count(5) % 3 * 50 + \
           dice.count(6) // 3 * 600


print(score([5, 5, 1, 1, 2]))
print(score([3, 3, 3, 3, 1]))
print(score([2, 4, 4, 5, 4]))
