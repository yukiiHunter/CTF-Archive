#!/usr/bin/env python3

from Crypto.Util.number import getStrongPrime, inverse, GCD
from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Util.number import bytes_to_long as btl
from secret import flag
from random import randint
while True:
    p = getStrongPrime(512)
    q = getStrongPrime(512)
    n = p * q
    e = 1337
    phi = (p-1)*(q-1)
    d = inverse(e,phi)
    if GCD(phi, e) == 1:
        break

gen = lambda : randint(0,255).to_bytes(1, 'big') * randint(20,50)
P = gen()
pad = lambda m : btl(m) + btl(P)
upd = lambda m : m - btl(P)
enc = lambda m : pow(pad(m.encode()),e,n)
dec = lambda c : 0 if b'LKS' in ltb(upd(pow(c,d,n))) else ltb(upd(pow(c,d,n)))+P
menu = ['----- RSA as a Service -----','Program enkripsi pesan yang aman!','[0] Generate padding baru' ,'[1] Enkripsi pesan','[2] Dekrip Pesan', '[3] Dapatkan flag terenkripsi','[4] Keluar']

if __name__ == '__main__':
    while 1:
        for i in menu:
            print(i)
        pilih = int(input('Masukkan pilihan: '))

        if pilih == 0:
            print("Generate padding baru")
            P = gen()
        elif pilih == 1:
            plaintext = str(input("Masukkan pesan yang mau dienkripsi: "))
            ciphertext = enc(plaintext)
            print("n:",n)
            print("e:",e)
            print("c:",ciphertext)
        elif pilih == 2:
            ciphertext = int(input("Masukkan pesan yang mau didekripsi: "))
            plaintext = dec(ciphertext)
            if plaintext:
                print("p:",plaintext)
                continue
            print("Lu pikir caranya bisa segampang itu??")
        elif pilih == 3:
            print("Flag terenkripsi:",enc(flag))
        elif pilih == 4:
            print("Bye!")
            break
        else:
            print("Pilihan salah!")
