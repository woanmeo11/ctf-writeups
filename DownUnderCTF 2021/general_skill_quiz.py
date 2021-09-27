from pwn import *
from re import findall
from urllib.parse import unquote
from base64 import b64decode, b64encode
import codecs

r = remote('pwn-2021.duc.tf', 31905)

print(r.recv())
r.sendline()

for i in range(100):
    msg = r.recv()
    print(msg)

    try:
        x = findall(': (.*)\n', msg.decode())[0]
    except:
        r.sendline('DUCTF')
        print(r.recv().decode())
        break

    if i == 0:
        ans = '2'
    elif i == 1:
        ans = str(int(x, 16))
    elif i == 2:
        ans = chr(int(x, 16))
    elif i == 3:
        ans = unquote(x)
    elif i == 4:
        ans = b64decode(x).decode()
    elif i == 5:
        ans = b64encode(x.encode()).decode()
    elif i == 6 or i == 7:
        ans = codecs.encode(x, 'rot_13')
    elif i == 8:
        ans = str(int(x, 2))
    else:
        ans = bin(int(x))
         
    print(x, ans)
    r.sendline(ans.encode())

