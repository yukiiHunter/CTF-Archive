import httpx
from hashlib import sha256, sha512, sha3_256, sha3_512, blake2b, blake2s
import itertools

# URL ke server
BASE_URL = "http://challenges.ctf.compfest.id:9010/"
c = httpx.Client(base_url=BASE_URL)

# Magic string asli
magic_string = b"SkibidiSigmaRizzleDizzleMyNizzleOffTheHizzleShizzleKaiCenat"

# Fungsi untuk mendapatkan signature
def sign(msg: str):
    r = c.get("/sign", params={"message": msg})
    return r.text

# Fungsi hashing menggunakan algoritma yang sama
def icb_256(bytes_to_hash):
    if len(bytes_to_hash) < 64:
        bytes_to_hash = sha512(bytes_to_hash).digest()

    algo_round = [sha256, sha3_256, sha3_512, blake2b, blake2s]
    result = b""
    for i in range(0, len(bytes_to_hash), 4):
        current = bytes_to_hash[i:i+4]
        current = algo_round[i % len(algo_round)](current).digest()[:2]
        result += current

    temp = result
    result = b""
    for i in range(0, len(temp), 32):
        result = bytes([x ^ y for x, y in zip(result, temp[i:i+32])])

    return result

# Variasi pesan
def generate_variations(magic_string):
    variations = []
    for i in range(1, 4):
        for positions in itertools.combinations(range(len(magic_string)), i):
            for replacements in itertools.product(b'abcdefghijklmnopqrstuvwxyz', repeat=i):
                modified_string = bytearray(magic_string)
                for pos, rep in zip(positions, replacements):
                    modified_string[pos] = rep
                variations.append(bytes(modified_string))
    return variations

if __name__ == "__main__":
    variations = generate_variations(magic_string)
    for var in variations:
        hashed_msg = icb_256(var).hex()
        response = sign(hashed_msg)
        if "signature" in response:
            print(f"Success: {var.hex()}")
            break
        else:
            print(f"Failed: {var.hex()}") 
