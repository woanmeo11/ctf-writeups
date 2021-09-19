# Circle City Con CTF 2021
# crypto: [Baby] Meadows
# woanmeo11

import random; random.seed(0x1337)
from ast import literal_eval
from Crypto.Util.number import inverse as inv

def decrypt(g, p, n, enc):
    z = []
    for _ in range(n):
        z.append(pow(g, random.randrange(2, p - 1), p))

    enc.pop(0)

    flag = []
    for i in range(n):
        flag.append(enc[i] * inv(z[i], p) % p)

    print(''.join(map(chr, flag)))


with open('out.txt', 'r') as f:
    enc = literal_eval(f.read())
    g, p = enc[0]
    len_flag = len(enc) - 1
    decrypt(g, p, len_flag, enc)
