# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    def get_weight(n):
        w, int_n = 0, int(n)
        while int_n:
            w, int_n = w + int_n % 10, int_n // 10
        return w, n
    return ' '.join(sorted(strng.split(), key=get_weight))


print(order_weight('2000 11 11 10003'), '|', '11 11 2000 10003')
