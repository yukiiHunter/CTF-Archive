from pwn import *

address = ("challenges.acectf.site", 13337)

def encrypt_command(command):
    conn = remote(address[0], address[1])
    
    # Pilih opsi 'encrypt' dan kirim command
    conn.sendline(b'1')  # Pilih opsi 'encrypt'
    conn.recvuntil(b'plaintext: ')
    conn.sendline(command)  # Kirim perintah dalam bentuk bytes
    
    # Terima respons dan ambil ciphertext dan tag
    response = conn.recvuntil(b'1. encrypt')  # Sampai ke menu berikutnya
    response_lines = response.decode().strip().split('\n')
    
    # Ambil ciphertext dan tag dari respons
    for line in response_lines:
        if "ciphertext:" in line:
            ciphertext = line.split(": ")[1].strip()
        elif "tag:" in line:
            tag = line.split(": ")[1].strip()
    
    conn.close()
    return ciphertext, tag

def try_nonce_with_seed(ciphertext, tag, seed_range=60000):
    for seed in range(seed_range):
        conn = remote(address[0], address[1])
        
        # Buka nonce
        nonce = seed.to_bytes(16, byteorder='big')  # 16 byte dari seed
        
        # Kirim nonce ke server
        conn.sendline(b'3')  # Pilih opsi 'execute'
        conn.recvuntil(b'nonce: ')
        conn.sendline(nonce.hex().encode())  # Kirim nonce
        
        # Kirim ciphertext dan tag
        conn.recvuntil(b'ciphertext: ')
        conn.sendline(ciphertext.encode())  # Kirim ciphertext
        conn.recvuntil(b'tage: ')
        conn.sendline(tag.encode())  # Kirim tag
        
        # Terima respons dari server
        response = conn.recvline().decode().strip()
        print(f"Nonce {nonce.hex()} mencoba... Response: {response}")
        
        # Cek apakah respons berisi "ACECTF{"
        if "ACECTF{" in response:
            print(f"Nonce ditemukan: {nonce.hex()}")
            print(f"Response: {response}")
            return nonce

        conn.close()
    
    print("Nonce tidak ditemukan dalam rentang seed yang diberikan.")
    return None

# Fungsi execute yang telah disesuaikan
def execute(nonce, ciphertext, tag):
    conn = remote(address[0], address[1])
    conn.sendline(b'3')  # Pilih opsi 'execute'
    conn.recvuntil(b'nonce: ')
    conn.sendline(nonce.hex().encode())  # Kirim nonce
    
    conn.recvuntil(b'ciphertext: ')
    conn.sendline(ciphertext.encode())  # Kirim ciphertext
    conn.recvuntil(b'tage: ')
    conn.sendline(tag.encode())  # Kirim tag
    
    # Terima respons dan proses
    response = conn.recvall().decode().strip()
    print(f"Response: {response}")
    
    if "ACECTF{" in response:
        print("Flag ditemukan!")
    else:
        print("No Flag :(")

    conn.close()

# Perintah modifikasi untuk enkripsi
command = b"6563686f2022666c616722207c20636174"  # cat flag modif dalam hex

# Lakukan enkripsi dan ambil ciphertext dan tag
ciphertext, tag = encrypt_command(command)

# Jalankan fungsi untuk mencoba nilai nonce dengan ciphertext dan tag yang diperoleh
nonce_found = try_nonce_with_seed(ciphertext, tag)

if nonce_found:
    # Jika nonce ditemukan, jalankan fungsi execute
    execute(nonce_found, ciphertext, tag)
