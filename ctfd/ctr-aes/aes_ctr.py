from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util import Counter
from base64 import *
import os

key = os.urandom(AES.key_size[0])
iv = os.urandom(AES.block_size)
secret = f'LKS{{{bytes_to_long(os.urandom(16))}}}'

def encrypt(pt):
    bytes_pt = pt.encode()
    cipher = AES.new(key, AES.MODE_CTR,counter=Counter.new(128))
    padded_pt = pad(bytes_pt, AES.block_size)
    return b64encode(cipher.encrypt(padded_pt))

print(encrypt(secret))
print('this text as test that my encryption work mwehe')
print(encrypt('this text as test that my encryption work mwehe'))
print(secret)
