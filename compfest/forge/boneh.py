from sympy import Matrix, mod_inverse
from Crypto.Util.number import long_to_bytes, bytes_to_long
import requests

def LLL_reduction(M):
    return Matrix(M).LLL()

def boneh_durfee_attack(e, n, delta=0.292):
    m = int(7 / (delta**2))
    t = int((1 / delta) - 1)
    X = 2 * pow(n, delta)

    PR = Matrix([
        [(X**i) * (e**j) for j in range(t + 1)]
        for i in range(m + 1)
    ])
    
    PR = PR.applyfunc(lambda x: x % n)
    L = LLL_reduction(PR)
    
    for i in range(L.rows):
        d_candidate = (X - L[i, 0]) % n
        if d_candidate > 0:
            k = (d_candidate * e - 1) // n
            if k * n == d_candidate * e - 1:
                return d_candidate
    return None

def forge_signature(magic_string, d, n):
    response = requests.get(f'http://localhost:8080/sign?message={magic_string.hex()}')
    icb_hash = response.json()['signature']
    
    signature = pow(bytes_to_long(bytes.fromhex(icb_hash)), d, n)
    
    return long_to_bytes(signature).hex()

def get_flag(signature):
    response = requests.get(f'http://localhost:8080/get_flag?signature={signature}')
    return response.json()

def main():
    response = requests.get('http://localhost:8080/pubkey')
    pubkey_info = response.json()
    n = int(pubkey_info['n'])
    e = int(pubkey_info['e'])

    d = boneh_durfee_attack(e, n)

    if d:
        print(f"Berhasil menemukan d: {d}")

        magic_string = b"SkibidiSigmaRizzleDizzleMyNizzleOffTheHizzleShizzleKaiCenat"
        forged_signature = forge_signature(magic_string, d, n)

        flag_response = get_flag(forged_signature)
        print(flag_response)
    else:
        print("Gagal menemukan eksponen privat d.")

if __name__ == "__main__":
    main()
