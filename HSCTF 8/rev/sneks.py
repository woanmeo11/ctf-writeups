# HSCTF 8
# rev: sneks
# woanmeo11

from string import printable

def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x = f(n >> 1)
    y = f(n // 2 + 1)
    return g(x, y, not n & 1)


def e(b, j):
    return 5 * f(b) - 7 ** j


def d(v):
    return v << 1


def g(x, y, l):
    if l:
        return h(x, y)
    return x ** 2 + y ** 2


def h(x, y):
    return x * j(x, y)


def j(x, y):
    return 2 * y - x


def encrypt(plain):
    inp = bytes(plain, 'utf-8')
    a = []
    enc = []
    for i, c in enumerate(inp):
        a.append(e(c, i))
    else:
        for c in a:
            enc.append(d(c))
    return enc[-1]

t = []
with open('output.txt', 'r') as w:
    t = w.read().split(' ')
t.pop()

flag = ''
finish = False

for i in range(len(t)):
    for c in printable:
        if encrypt(flag + c) == int(t[i]):
            flag += c
            break
    print(flag)