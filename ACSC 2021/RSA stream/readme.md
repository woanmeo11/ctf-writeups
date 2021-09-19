# RSA stream (crypto-100)

## Summary

```python
import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long, getStrongPrime, inverse
from Crypto.Util.Padding import pad

from flag import m
#m = b"ACSC{<REDACTED>}" # flag!

f = open("chal.py","rb").read() # I'll encrypt myself!
print("len:",len(f))
p = getStrongPrime(1024)
q = getStrongPrime(1024)

n = p * q
e = 0x10001
print("n =",n)
print("e =",e)
print("# flag length:",len(m))
m = pad(m, 255)
m = bytes_to_long(m)

assert m < n
stream = pow(m,e,n)
cipher = b""

for a in range(0,len(f),256):
  q = f[a:a+256]
  if len(q) < 256:q = pad(q, 256)
  q = bytes_to_long(q)
  c = stream ^ q
  cipher += long_to_bytes(c,256)
  e = gmpy2.next_prime(e)
  stream = pow(m,e,n)

open("chal.enc","wb").write(cipher)
```

Flag is encrypted to `stream` with RSA 2048bit and then XORed gradually with each 256 bytes block of file `chal.py`. With each block is XORed,`stream` is recalculated with public exponent `e` provided by `gmpy2.next_prime()` function.

## Solution

### Getting our RSA back
At first, getting our `stream` back by XORing `chal.py` with `chal.enc` for each 256 bytes.

```python
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
```

Focus on `gmpy2.next_prime()` function, I realize that it's not a randomize function so I feed `e` into it and recover two more `e` which is used in previous XORed stage.

```python
e = [65537, 65539, 65543]
```

Now we have with 3 `stream` and 3 public exponent `e`, just crack it and capture the flag, ez :>

### Cracking RSA

Here comes the real problem. The public modulus `n` isn't change so that we have a common modulus but different public exponent RSA system.

```
c1 = m ^ e1 (mod n)
c2 = m ^ e2 (mod n)
c3 = m ^ e3 (mod n)
```

> It can't be solved by using Chinese Remainder Theorem as usual. Feeling bad? 

Okay, here is an idea:

Because in this case `gcd(e1, e2) = 1`, we can find integers `x` and `y` such that:

```
x*e1 + y*e2 = 1
```
By using the Extended Euclidean algorithm we can easily find `x` and `y` sastified above equation. After have `x` and `y`, the plaintext can be recovered by doing some simple math below:

```
c1^x * c2^y = (m ^ e1)^x * (m ^ e2)^y (mod n)
= m^(e1 * x) * m^(e2 * y) (mod n)
= m ^ (e1*x + e2*y) (mod n)
= m ^ 1 (mod n)
= m (mod n)
```

> We only need two pair `(c1, c2)` and `(e1, e2)`, easy huh? However, `x` or `y` can be negative so that we have to do some Modular Multiplicative Inverse.

In this case, I don't have to worry about it, just let python does all the work:

```python
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long, long_to_bytes

def egcd(a, b):
	if a == 0:
		return (0, 1)
	else:
		y, x = egcd(b % a, a)
		return (x - (b // a) * y, y)

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

x, y = egcd(e[0], e[1])
m = long_to_bytes(pow(stream[0], x, n) * pow(stream[1], y, n) % n)

print(m)
```

Flag:
```
ACSC{changing_e_is_too_bad_idea_1119332842ed9c60c9917165c57dbd7072b016d5b683b67aba6a648456db189c}
```
