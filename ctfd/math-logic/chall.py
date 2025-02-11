#!/usr/bin/env python3
from Crypto.Util.number import getRandomRange, isPrime
# from secret import FLAG, z
z = 39034347554788886188862828900368120155828678821750756988259309575481111063637738059399123616138932815543173268897792
FLAG = b'LKS{**************************************}'


def nextPrime(a):
    b = a | 1
    while not isPrime(b) or a == b:
        b += 2
    return b


def getPrime(z):
    while True:
        a = nextPrime(getRandomRange(z // 2, z - 1))
        b = nextPrime(getRandomRange(z // 2, z - 1))
        p = a * pow(z, 2) + b
        if isPrime(p):
            return p


m = int.from_bytes(FLAG, "big")
e = 65537
n = getPrime(z) * getPrime(z)
c = pow(m, e, n)

print(f"{z = }")
print(f"{e = }")
print(f"{n = }")
print(f"{c = }")
