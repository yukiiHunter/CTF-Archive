from pwn import *
import hashlib

def main(input):
    host = 'ctf-chall.stembascc.com'
    port = 5363
    t = remote(host, port)
    t.recvuntil(b">> ")
    input = base64.b64encode(input.encode()).decode()
    t.sendline(input)
    a = t.recvall().decode()
    encoded = "".join(a.split("\n")[1])
    hex_data = base64.b64decode(encoded).hex()
    return hex_data[96:128]

def find_md5_collision(prefix):
    # Fungsi ini bertugas menemukan dua string yang memiliki nilai hash MD5 yang sama
    # Meskipun prefix-nya berbeda, namun hasil akhir MD5-nya akan sama
    # Implementasi ini bergantung pada perpustakaan khusus atau teknik brute force

    for i in range(1000000):  # Contoh loop untuk brute force
        suffix = str(i).encode()
        candidate = prefix + suffix
        hash_candidate = hashlib.md5(candidate).hexdigest()

        # Cek jika nilai hash MD5-nya sudah memenuhi syarat
        if hash_candidate.startswith('0000'):  # Sesuaikan syaratnya sesuai challenge
            return candidate.decode()

    return None

if __name__ == '__main__':
    flag = ""
    while True:
        # Sesuaikan panjang payload berdasarkan challenge MD5 collision
        payload = "0" * (55 - len(flag))
        hex_data = main(payload)

        for i in range(33, 125):
            candidate_payload = payload + flag + chr(i)
            
            # Cek apakah ada collision yang cocok
            collision_candidate = find_md5_collision(candidate_payload.encode())
            if collision_candidate and main(collision_candidate) == hex_data:
                flag += chr(i)
                print("Flag: ", flag)
                break
