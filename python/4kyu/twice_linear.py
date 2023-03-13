# https://www.codewars.com/kata/5672682212c8ecf83e000050

def dbl_linear(n):
    get_b = lambda x: 2 * x + 1
    get_c = lambda x: 3 * x + 1

    seq = [1]
    i, j = 0, 0
    c = get_c(seq[j])
    while len(seq) <= n:
        while c > (b := get_b(seq[i])):
            seq.append(b)
            i += 1

        while b > (c := get_c(seq[j])):
            seq.append(c)
            j += 1

        if b == c:
            seq.append(b)
            i += 1
            j += 1
    return seq[n]


print(dbl_linear(3), 4)
print(dbl_linear(5), 9)
print(dbl_linear(20), 57)
print(dbl_linear(100), 447)
print(dbl_linear(2439), 26247)
