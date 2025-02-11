from Crypto.Cipher import AES
import base64
import random
import string

class AESCipher:
    def __init__(self, key):
        self.bs = 32
        self.key = key

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def decrypt_with_key(encrypted, key):
    try:
        aes = AESCipher(key)
        return aes.decrypt(encrypted)
    except:
        return None

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
     except:
	return None

def brute_force_challenge(encrypted):
    plaintext = 'Welcome crypto challenge ACE CTF2024!'
    for seed in range(0, 0xffff + 1):
        random.seed(seed)
        characters = string.ascii_letters + string.digits
        key = (''.join(random.choice(characters) for _ in range(32))).encode()
        decrypted = decrypt_with_key(encrypted, key)
        if decrypted == plaintext:
            print(f"Key found: {key.decode()}")
            print(f"Decrypted message: {decrypted}")
            return
    print("Failed to find the key.")

if __name__ == '__main__':
    encrypted_message = input('Enter the encrypted message: ')
    brute_force_challenge(encrypted_message)
