import base64
from Crypto.Cipher import AES
import random
import string
import os

def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    key = open('key.txt', 'r').read().strip()
    if len(key) != 16:
        open('key.txt', 'w').write(generate_random_string())
    break

FLAG = os.getenv('FLAG') or "####REDACTED####"
assert len(FLAG) == 16

word = str(input("Enter the message : "))
message = f'{key}{word}{FLAG}'

if len(message) % 16 != 0:
    message = message + '0' * (16 - len(message) % 16)
message = bytes(message,'utf-8')

aes = AES.new( key.encode(), AES.MODE_ECB )
cipher = aes.encrypt(message)
cipher = base64.b64encode(cipher)
print(cipher.decode('ascii'))

