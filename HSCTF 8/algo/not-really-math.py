# HSCTF 8
# algo: not-really-math
# woanmeo11

from pwn import *

stack = []
buf = ''

def push():
    global buf
    if buf:
        stack.append(int(buf))
        buf = ''

def calc(expression):
    global buf, stack

    stack = []
    buf = prev_cmd = ''
    expression += 'm'

    for c in expression:
        if c.isdigit():
            buf += c
        else:
            push()
            if prev_cmd == 'a':
                stack[-2] += stack[-1]
                stack.pop()
            prev_cmd = c

    mod = 2**32 - 1
    p = 1
    for x in stack:
        p = p * x % mod

    return p

r = remote('not-really-math.hsc.tf', 1337)
r.recv()

while True:
    msg = r.recv()
    if b'flag' in msg:
        print(msg)
        exit(0)

    while msg[-1] != 32:
        msg += r.recv()
    print(msg)

    ans = calc(msg[:-3].decode())
    print(ans)

    r.sendline(str(ans))