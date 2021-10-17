#import woanmeo11
from pwn import *
import qrtools
import os
import pyscreenshot as ps

r = remote('125.235.240.166', 20123)

def qr_recive():
    qr = b''
    while not b'ID Number:' in qr:
        qr += r.recv()
    print(qr.decode('utf8'))

def qr_decode():
    # invert color
    os.system('convert qr.png -channel RGB -negate qr.png')

    qr = qrtools.QR()
    qr.decode('qr.png')
    return qr.data.split('|')

def screenshot():
    im = ps.grab() # grab whole screen
    im.save('qr.png')

for i in range(100):
    qr_recive()
    screenshot()
    
    data = qr_decode()
    
    r.sendline(data[0].encode())
    print(r.recv())

    r.sendline(data[1].encode())
    print(r.recv())
    
    r.sendline(data[2].encode())
    print(r.recvline())

    print('\n' * 20) # clear previous QR

print(r.recv())

# ASCIS{c0r0n4_v1rus_1s_g0n3}
