# HSCTF 8
# algo: extended-fibonacci-sequence
# woanmeo11

from pwn import *
from math import log10

f = [0, 1]
s = [0, 1]
t = [0, 1]
p10 = [1]

def length(x):
    return int(log10(x)) + 1

def init():
    for i in range(1, 12):
        p10.append(10 * p10[-1])

    for i in range(2, 1001):
        f.append(f[-1] + f[-2])
        if length(f[-1]) < 11:
            s.append(s[-1]*p10[length(f[-1])] + f[-1])
        else:
            s.append(f[-1])
        t.append((t[-1] + s[-1]) % p10[11])

init()

r = remote('extended-fibonacci-sequence.hsc.tf', 1337)
r.recv()

while True:
    msg = r.recv()
    print(msg)
    
    if b'flag' in msg:
        break

    while msg[-1] != 32:
        msg += r.recv()

    n = int(msg[:-3])
    print(t[n])

    r.sendline(str(t[n]))
