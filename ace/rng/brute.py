import random
import string
import base64

class AESCipher:
    # Assuming you have your AESCipher implementation here
    def __init__(self, key):
        self.key = key
    
    def decrypt(self, enc):
        # Your decryption method here
        return enc  # Replace with the actual decryption logic

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

for i in range(0, 0xffff):
    try:
        random.seed(i)
        characters = string.ascii_letters + string.digits
        key = (''.join(random.choice(characters) for _ in range(32))).encode()
        aes = AESCipher(key)

        enc = "VMxYf7xQmEEuckXB79yM6Z8PFfrHegQ3cDjyQWy2A28ZYs1BKX2CnFCgw3SNmZ7UKqsKtspSOfmPxmcspVqNiT7pFaixT5EQ/MtbpPU3Gkg="
        pt = 'Welcome crypto challenge ACE CTF2024!'

        dec = aes.decrypt(enc)

        if dec == pt:
            print('oke')
            print(base64.b64encode(xor(key, pt.encode()[:len(key)])))
            break  # If found, exit the loop
    except Exception as e:
        print(f"An error occurred: {e}")
