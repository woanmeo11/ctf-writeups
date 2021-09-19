# HSCTF 8
# algo: hopscotch
# woanmeo11

from pwn import *

f = [0, 1, 2]

for i in range(1000):
    f.append((f[-1] + f[-2]) % 10000)

r = remote('hopscotch.hsc.tf', 1337)
print(r.recv())

while True:
    msg = r.recv()
    print(msg)
    
    if b'flag' in msg:
        break

    while msg[-1] != 32:
        msg += r.recv()

    n = int(msg[:-3])
    print(n)
    
    r.sendline(str(f[n]))
