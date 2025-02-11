import multiprocessing
import itertools
import string
from hashlib import sha256, sha512, sha3_256, sha3_512, blake2b, blake2s
from Crypto.Util.number import bytes_to_long

# Algoritma hashing dari kode yang disediakan
def xor_256(a, b):
    if len(a) < len(b):
        a = a + b"\x00" * (len(b) - len(a))
    elif len(b) < len(a):
        b = b + b"\x00" * (len(a) - len(b))
    return bytes([x ^ y for x, y in zip(a, b)])

def sigma_round(bytes_to_hash, algo_round):
    result = b""
    for i in range(0, len(bytes_to_hash), 4):
        current = bytes_to_hash[i:i+4]
        current = algo_round[i % len(algo_round)](current).digest()[:2]
        result += current
    return result

def icb_256(bytes_to_hash, algo_round):
    if len(bytes_to_hash) < 64:
        bytes_to_hash = sha512(bytes_to_hash).digest()

    temp = sigma_round(bytes_to_hash, algo_round)
    result = b""
    for i in range(0, len(temp), 32):
        result = xor_256(result, temp[i:i+32])

    return result

# Magic string dari kode yang diberikan
magic_string = b"SkibidiSigmaRizzleDizzleMyNizzleOffTheHizzleShizzleKaiCenat"

# Daftar algoritma hash yang digunakan
algo_round = [sha256, sha3_256, sha3_512, blake2b, blake2s]

# Fungsi brute-force untuk mencari string dengan hash yang sama
def find_collision(target_hash, algo_round):
    charset = string.ascii_letters + string.digits + string.punctuation
    max_len = 8  # Sesuaikan panjang maksimal yang ingin Anda coba

    def worker(target_hash, algo_round, charset, length, queue):
        for attempt in itertools.product(charset, repeat=length):
            candidate = ''.join(attempt).encode()
            candidate_hash = icb_256(candidate, algo_round)
            if candidate_hash == target_hash:
                queue.put(candidate)

    num_processes = multiprocessing.cpu_count()
    processes = []
    queue = multiprocessing.Queue()

    for i in range(num_processes):
        p = multiprocessing.Process(target=worker, args=(target_hash, algo_round, charset, max_len, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    result = queue.get()
    return result

if __name__ == "__main__":
    target_hash = icb_256(magic_string, algo_round)
    collision = find_collision(target_hash, algo_round)
    print(f"Found collision: {collision.decode()}") if collision else print("No collision found within the given length")
