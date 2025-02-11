import base64
from pwn import xor

flag = b'4U?/:2+,%T< T\x03a[x9*\x0b8:!\x077\x193\x02\x05]\x0b\x03W_0\x1c\x0f\x048\x0c9\\-\x12\r\x0b\tJ~NxR<^8\x16\x0568\x0e\x03?Z\x0c'
key = "adminganteng12345".encode('utf-8')
rep = (key * (len(flag) // len(key) + 1))[:len(flag)]

decrypted_bytes = xor(flag, rep)

decrypted_text = base64.b64decode(decrypted_bytes).decode('utf-8')
print(f"Decrypted Text: {decrypted_text}")