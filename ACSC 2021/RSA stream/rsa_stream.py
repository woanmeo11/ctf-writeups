from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes

with open('chal.enc', 'rb') as r:
    cipher = r.read()
with open('chal.py', 'rb') as r:
    f = r.read()

stream = []
for i in range(0, len(cipher), 256):
    c = bytes_to_long(cipher[i:i + 256])

    q = f[i:i + 256]
    if len(q) < 256:
        q = pad(q, 256)

    q = bytes_to_long(q)
    
    stream.append(c ^ q)

n = 0xedad9a316b218bb93169944b8f1995adfb40653cb89aee0eeb95166a85125fcf403a834bfda896f56bfd553ce6ea48b1480434bb324dd0ffabdfd0f26365261c056295c1064b688b3dd91c469b8d902070b6c68f48935690f6c126beb6c9917d24f02aab1558355e4e3ac9e1cbf1ae74469370d3f87303784e8b23bd11c7826d4a3e8a4247b2dac71153762d578af909b2f38182e89e82836f4b80f807b6b0823524219d0f1e885f2cd4f42849eafb1cd6344cd806ec8216892f209209ed4eb5d13b03354cf0c57aff4aa166a47f1a361a405dfbad3535fbbe046ce8259c4f3c3c9d20aeb7a5a82078089cece53abe04fae95414cde0419175f926ec2309668d 

e = [65537, 65539, 65543]

print(long_to_bytes(pow(stream[0], 32769, n) * pow(inverse(stream[1], n), 32768, n) % n))
