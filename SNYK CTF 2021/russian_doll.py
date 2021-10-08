import xxtea
from string import digits
from base64 import b64decode

enc = "SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg"
enc = b64decode(enc)

CHARSET = digits

# 1347

for a in CHARSET:
    for b in CHARSET:
        for c in CHARSET:
            for d in CHARSET:
                key = a + b + c + d
                print('key:', key)
                decrypt_data = xxtea.decrypt_utf8(enc, key)
                print(decrypt_data)
                if 'SNYK' in decrypt_data:
                    exit(0)

# SNYK{6f86993db5d45adea7931dafb2d91e2a13ca326f4bc33ef0ee1a428fa005ada5}
