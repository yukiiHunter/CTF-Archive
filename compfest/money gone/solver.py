import hashlib
import random

methods = ['md5', 'sha256', 'sha3_256', 'sha3_512', 'sha3_384', 'sha1', 'sha384', 'sha3_224', 'sha512', 'sha224']

def random_encrypt(x):
    # Fungsi yang sama seperti di script enkripsi
    method = random.choice(methods)
    hash_obj = hashlib.new(method)
    hash_obj.update(x.encode())
    return hash_obj.hexdigest()

def generate_hash_dictionary():
    # Buat kamus hash untuk semua nilai dari 0 hingga 129
    hash_dict = {}
    for i in range(130):
        num_str = str(i)
        sha512_hash = hashlib.sha512(num_str.encode()).hexdigest()
        for method in methods:
            encrypted = hashlib.new(method)
            encrypted.update(sha512_hash.encode())
            hash_dict[random_encrypt(sha512_hash)] = i
    return hash_dict

def decrypt_message(encrypted_list, hash_dict):
    decrypted_message = []
    for enc in encrypted_list:
        if enc in hash_dict:
            num = hash_dict[enc]
            char = chr((num - 20) % 130)
            decrypted_message.append(char)
        else:
            decrypted_message.append('?')  # Jika hash tidak ditemukan, gunakan karakter placeholder
    return ''.join(decrypted_message)

def main():
    # Baca data terenkripsi dari file
    with open('encrypted_memory.txt', 'r') as f:
        encrypted_list = eval(f.read())  # Menggunakan eval untuk mengonversi string menjadi list

    # Buat kamus hash
    hash_dict = generate_hash_dictionary()

    # Dekripsi pesan
    decrypted_message = decrypt_message(encrypted_list, hash_dict)

    # Simpan pesan yang didekripsi
    with open('decrypted_memory.txt', 'w') as f:
        f.write(decrypted_message)

if __name__ == "__main__":
    main()
