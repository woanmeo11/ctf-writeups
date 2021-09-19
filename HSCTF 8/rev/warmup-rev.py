# HSCTF 8
# rev: warmup-rev
# woanmeo11

def rev_cold(s):
    return s[17:] + s[:17]

def rev_cool(s):
    t = ''
    for i in range(len(s)):
        if i & 1:
            t += s[i]
        else:
            t += chr(ord(s[i]) - 3*(i >> 1))
    return t

def rev_warm(s):
    k = s[:-1].rindex('l')
    a = s[k + 1:]
    possible = []

    for i in range(1, k + 1):
        c = s[:i]
        b = s[i:k + 1]
        possible.append(a + b + c)
    
    return possible

def rev_hot(s):
    adj = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]
    t = ''
    for i in range(len(s)):
        t += chr(ord(s[i]) - adj[i])
    return t

s = '4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy'
x = rev_warm(rev_hot(s))
for i in range(len(x)):
    print(rev_cold(rev_cool(x[i])))


