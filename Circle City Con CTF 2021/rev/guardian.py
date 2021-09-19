# Circle City Con CTF 2021
# rev: [Baby] Guardian
# woanmeo11

from pwn import *
from string import ascii_lowercase, digits

correct = b'\xe2\x9c\x85'
charset = ascii_lowercase + digits + '_!?}'
flag = 'CCC{'

found = False
while not found:
    found = True
    for c in charset:
        while True:
            r = remote('35.224.135.84', 2000)
            r.recvuntil('?\n> ')

            print(flag + c)
            r.send(flag + c)
            
            respone = r.recv()
            print(respone)
            r.close()

            if b'incorrect' in respone or b'best' in respone:
                if b'best' in respone:
                    flag += c
                    print(flag)
                    exit(0)
                break
        
        if respone.count(correct) == len(flag) + 1:
            flag += c
            found = False
            print(flag)
            break
