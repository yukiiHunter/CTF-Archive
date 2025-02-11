from Crypto.Cipher import AES
import base64
import string
import itertools

# Constants
ENCRYPTED_TEXT = 'jpXW5Z7BZ/s+gOAIKLgnYuLCHg3f4ZwdkQBOTn3uxoYTruywmQu4Lo5HjwL2qhTMDJu6Ult3e/VTVov8dJTyslCcxkevn9tmOmHNYzcNa04='
KNOWN_PLAINTEXT = 'Welcome crypto challenge ACE CTF2024!'
BLOCK_SIZE = 16  # Coba dengan panjang kunci yang lebih pendek

def decrypt_aes(ciphertext, key):
    try:
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext[AES.block_size:])
        return _unpad(decrypted).decode('utf-8')
    except Exception as e:
        print(f"Decryption failed for key: {key.decode()}. Error: {e}")
        return None

def _unpad(s):
    padding_len = s[-1]
    return s[:-padding_len]

def brute_force_key():
    characters = string.ascii_letters + string.digits
    attempt = 0
    for key_tuple in itertools.product(characters, repeat=BLOCK_SIZE):
        key = ''.join(key_tuple).encode()
        attempt += 1
        if attempt % 100000 == 0:
            print(f"Attempt {attempt}...")
        try:
            decoded_ciphertext = base64.b64decode(ENCRYPTED_TEXT)
            decrypted_text = decrypt_aes(decoded_ciphertext, key)
            if decrypted_text == KNOWN_PLAINTEXT:
                print(f'Success! Key found: {key.decode()}')
                break
        except Exception as e:
            print(f"Exception occurred: {e}")
            continue

if __name__ == '__main__':
    brute_force_key()
