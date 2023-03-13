# https://www.codewars.com/kata/58c5577d61aefcf3ff000081

def encrypt(n, size):
    r = 2 * (n - 1)
    return sorted((i % r if i % r < n else r - i % r, i) for i in range(size))


def encode_rail_fence_cipher(string, n):
    return ''.join(string[i] for _, i in encrypt(n, len(string)))


def decode_rail_fence_cipher(string, n):
    indexed_string = zip(encrypt(n, len(string)), string)
    return ''.join(s for _, s in sorted(indexed_string, key=lambda x: x[0][1]))


print(encode_rail_fence_cipher('WEAREDISCOVEREDFLEEATONCE', 3), 'WECRLTEERDSOEEFEAOCAIVDEN')
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE")
