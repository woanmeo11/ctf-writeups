encoded = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"


def rev_right(x, d):
    n = len(x)
    x = x[n - d:] + x[:n - d]
    return x

def rev_left(x, d):
    x = x[::-1]
    return rev_right(x, len(x) - d)

def rev_down(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x

def rev_up(x):
    res = ''
    for i in range(0, len(x), 8):
        res += chr(int(x[i:i+8], 2) >> 1)
    return res

def decode(plain):
    d = 24
    x = rev_left(plain, d)
    x = rev_down(x)
    x = rev_right(x, d)
    x = rev_up(x)
    return x


print(decode(encoded))
