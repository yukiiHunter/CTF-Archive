import hashlib
import random

methods = ['md5', 'sha256', 'sha3_256', 'sha3_512', 'sha3_384', 'sha1', 'sha384', 'sha3_224', 'sha512', 'sha224']

def bf(x, expected_hash):
    for method in methods:
        hash_obj = hashlib.new(method)
        hash_obj.update(x.encode())
        if hash_obj.hexdigest() == expected_hash:
            return True
    return False

def dekirp(enc_array):
    message = []

    for hashed_value in enc_array:
        for i in range(130):
            x = (i + 20) % 130
            sha512_hash = hashlib.sha512(str(x).encode()).hexdigest()

            if bf(sha512_hash, hashed_value):
                message.append(chr(i))
                break

    return ''.join(message)

with open("encrypted_memory.txt", "r") as f:
    encrypted_memory = eval(f.read())

decrypted_message = dekirp(encrypted_memory)
print(decrypted_message)
