#!/usr/bin/env python3

from Crypto.Util.number import *

f = "LKSSMK2023{Fek_Fleg_cuyyyyyyyy}"
p = getPrime(12)
q = getPrime(1024)
n = p * q
e = 0x10001
m = bytes_to_long(f.encode())
c = pow(m, e, n)

print(f"c = {c}")
print(f"e = {e}")
print(f"n = {n}")
