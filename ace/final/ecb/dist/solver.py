# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# import base64

# def decrypt_aes(encrypted_message: str, key: str) -> str:
#     # Convert key and encrypted message to bytes
#     key_bytes = key.encode('utf-8')
#     encrypted_message_bytes = base64.b64decode(encrypted_message)

#     # Assuming the encrypted message uses AES CBC mode
#     # Extract the IV (initialization vector), first 16 bytes
#     iv = encrypted_message_bytes[:16]
#     cipher_text = encrypted_message_bytes[16:]

#     # Initialize AES cipher for decryption in CBC mode
#     cipher = AES.new(key_bytes, AES.MODE_CBC, iv)

#     # Decrypt and unpad the message
#     decrypted_bytes = cipher.decrypt(cipher_text)
#     try:
#         decrypted_message = unpad(decrypted_bytes, AES.block_size)
#         return decrypted_message.decode('utf-8')
#     except (ValueError, KeyError):
#         return "Invalid decryption. Could not unpad message."

# if __name__ == "__main__":
#     # Contoh pesan terenkripsi dan kunci
#     encrypted_message = "KdXeAf8Z8YcZ5Eh+B+v8hXj5UZbqa6GBTQ8A1VAhwCYp1EY75umrX1vxlNOQ2JJW"  # ganti dengan encrypted message Anda (base64)
#     key = "qtB4tZZfQ3fqM4Hg"  # ganti dengan key Anda (16, 24, atau 32 byte untuk AES)

#     decrypted_message = decrypt_aes(encrypted_message, key)
#     print(f"Decrypted Message: {decrypted_message}")


from base64 import b64decode
from pwn import *
from Crypto.Cipher import AES


address = ("challenges.acectf.site", 9090)

conn = remote(address[0], address[1])

ciphertexts = []

def sendAndRecieve(line):
    prompt = conn.recvuntil(b":").decode()  # Menerima prompt dari server
    conn.sendline(line)
    response = conn.recvline()
    print(f"Response from server: {response}")
    return conn.recvline().decode().strip()

for i in range(15, 0, -1):
	pad = b"\x00" * i
	ct = b64decode(sendAndRecieve(pad))[-32:-16]
	ciphertexts.append(ct)
	print(f"Pad {15 - i}: {pad.hex()} -> Ciphertext: {ct.hex()}")

ct = b64decode(sendAndRecieve(b""))[-32:-16]
ciphertexts.append(ct)

key = b"qtB4tZZfQ3fqM4Hg"
for i in range(len(key), len(ciphertexts)):
	pad = b"\x00" * (15 - i) + key
	ciphertext = ciphertexts[i]
	# print(f"Pad {15 - i}: {pad.hex()} -> Ciphertext: {ciphertext.hex()}")
	for j in range(32, 127):
		if chr(j) != chr(j).strip(): continue
		ct = b64decode(sendAndRecieve(pad + bytes([j])))[-32:-16]
		# print(f"\tTrying pad: {(pad + bytes([j])).hex()} -> Ciphertext: {ct.hex()}")
		if ct == ciphertext:
			key += bytes([j])
			print(key)
			break


encrypted = "yRhF4zE6mVuZmr79VrwZda7kDz+FDgmIrn6YBwRDud3HkZIUTTt73Ax4jzuN+8/k"
encrypted = b64decode(encrypted)
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(encrypted))