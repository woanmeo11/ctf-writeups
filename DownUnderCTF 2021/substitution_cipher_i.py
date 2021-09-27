from sympy import *

with open('output.txt', 'r') as f:
    cipher = f.read()

for c in cipher:
    c = ord(c)
    var('x')
    print(chr(solve(13*x**2 + 3*x + 7 - c, x)[1]), end='')
