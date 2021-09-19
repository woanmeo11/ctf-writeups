# HSCTF 8
# crypto: aptenodytes-forsteri
# woanmeo11

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = "IOWJLQMAGH"
for c in encoded:
    print(letters[(letters.index(c) - 18)%26], end='')
