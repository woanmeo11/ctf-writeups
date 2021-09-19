# HSCTF 8
# algo: extended-fibonacci-sequence-2
# woanmeo11

from pwn import *

f = [4, 5]
s = [4, 9]
t = [4, 13]
mod = 10**10

def init():
    for _ in range(2, 1001):
        f.append((f[-1] + f[-2]) % mod)
        s.append((s[-1] + f[-1]) % mod)
        t.append((t[-1] + s[-1]) % mod)

init()

r = remote('extended-fibonacci-sequence-2.hsc.tf', 1337)

while True:
    msg = r.recvuntil('!\n')
    print(msg)

    msg = r.recv()
    print(msg)
    
    if b'flag' in msg:
        break

    while msg[-1] != 10:
        msg += r.recv()

    n = int(msg[:-1])
    print(t[n])

    r.sendline(str(t[n]))

    print(r.recv())
