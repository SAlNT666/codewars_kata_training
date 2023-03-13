# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    return sum(set(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number))))


print(solution(10), 23)
