#! /usr/bin/python3
from random import randint


def encrypt(s):
    key = list(str(randint(101, 999)))
    key = [int(i) for i in key]
    s = list(str(s))
    cipher = []
    k = 0

    for i in s:
        k = 0 if k >= 3 else k
        if "A" <= i <= "Z":
            if chr(ord(i) + key[k]) > "Z":
                cipher.append(chr(ord(i) + key[k] - 26))
            else:
                cipher.append(chr(ord(i) + key[k]))
        elif "a" <= i <= "z":
            if chr(ord(i) + key[k]) > "z":
                cipher.append(chr(ord(i) + key[k] - 26))
            else:
                cipher.append(chr(ord(i) + key[k]))
        elif "0" <= i <= "9":
            if chr(ord(i) + key[k]) > "9":
                cipher.append(chr(ord(i) + key[k] - 10))
            else:
                cipher.append(chr(ord(i) + key[k]))
        else:
            cipher.append(i)
        k += 1
    sym = [60, 62, 123, 125, 63, 33, 38, 37, 64, 35]
    return scramble(chr(sym[randint(0, 9)]) + str_sum(cipher) + str_sum(key) + chr(sym[randint(0, 9)]))


def decrypt(s):
    s = unscramble(s)[1:-1]
    key = s[-3:]
    key = [int(i) for i in key]
    s = list(str(s[0:-3]))
    plain = []
    k = 0

    for i in s:
        k = 0 if k >= 3 else k
        if "A" <= i <= "Z":
            if chr(ord(i) - key[k]) < "A":
                plain.append(chr(ord(i) - key[k] + 26))
            else:
                plain.append(chr(ord(i) - key[k]))
        elif "a" <= i <= "z":
            if chr(ord(i) - key[k]) < "a":
                plain.append(chr(ord(i) - key[k] + 26))
            else:
                plain.append(chr(ord(i) - key[k]))
        elif "0" <= i <= "9":
            if chr(ord(i) - key[k]) < "0":
                plain.append(chr(ord(i) - key[k] + 10))
            else:
                plain.append(chr(ord(i) - key[k]))
        else:
            plain.append(i)
        k += 1

    return str_sum(plain)


def scramble(s):
    pos, scr_text, s = [], [], list(str(s))

    for i in s:
        x = randint(0, len(s) - 1)
        while x in pos:
            x = randint(0, len(s) - 1)
        pos.append(x)
        scr_text.append(s[x])

    return str_sum(scr_text) + str_sum([chr(i + 103) for i in pos])


def unscramble(s):
    pos, unscr_text, s = s[-int(len(s)/2):], [], s[:-int(len(s)/2)]

    for i in range(len(pos)):
        unscr_text.append(s[pos.index(chr(i + 103))])
    return str_sum(unscr_text)


def str_sum(l):
    sum = ""
    for i in l:
        sum += str(i)
    return sum


if __name__ == "__main__":
    print(encrypt("Man"))
    print(decrypt(encrypt("Man")))