from pwn import xor
from Crypto.Util.number import *

flag = "U1RFTUJBQ1RGe1RoMXNfQTFfYmVlbl90cjQxbmVkX2Ywcl8xMzM3X3QxbWVzfQ==".encode('utf-8')
key = "adminganteng12345".encode('utf-8')

rep = (key * (len(flag) // len(key) + 1))[:len(flag)]

print(xor(flag, rep))
