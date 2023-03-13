# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order, max_e):
    res = []
    for o in order:
        if res.count(o) < max_e: res.append(o)
    return res


print(delete_nth([20, 37, 20, 21], 1), [20,37,21])
