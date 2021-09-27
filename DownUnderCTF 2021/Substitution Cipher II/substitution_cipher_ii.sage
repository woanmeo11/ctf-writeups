from string import ascii_lowercase, digits
CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

P.<x> = PolynomialRing(GF(n))
f = 41*x^6 + 15*x^5 + 40*x^4 + 9*x^3 + 28*x^2 + 27*x + 1 

with open('output.txt', 'r') as g:
    ct = g.read().strip()

flag = ''

for c in ct:
    c = CHARSET.index(c)
    
    for k in CHARSET:
        if c == f.substitute(CHARSET.index(k)):
            flag += k
            break

print(flag)
