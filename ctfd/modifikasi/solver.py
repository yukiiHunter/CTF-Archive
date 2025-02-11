from hashlib import md5
from pwn import remote

# Establish connection
address = ("ctf-chall.stembascc.com", 5362)
conn = remote(address[0], address[1])

# Script logic
print("Anda sedang menjual tiket konser Taylor Swift")
print("Terdapat 2 pembeli yang ingin membeli tiket, Alice dan Bob. Sayangnya tiket hanya tersisa 1")
print("Tiket tersebut diverifikasi menggunakan md5")
print("Dapatkah anda membuat tiket palsu untuk dijual ke Bob?")

# Precomputed collision hex strings
alice_hex = "4ca00ff4c898d61e1edbf1800618fb28"  # Hex string for Alice
bob_hex = "4ca00ff4c898d61e1edbf1800618fb29"    # Hex string for Bob (colliding MD5)

# Convert hex to bytes
alice = bytes.fromhex(alice_hex)
bob = bytes.fromhex(bob_hex)

# MD5 hashes for Alice and Bob
md5alice = md5(alice).digest()
md5bob = md5(bob).digest()

# Print the MD5 hashes
print("MD5 dari tiket Alice:", md5alice.hex())
print("MD5 dari tiket Bob:", md5bob.hex())

# Check if the MD5 hashes collide
if md5bob == md5alice and alice != bob:
    print("Bob: Terima kasih! Ini bayarannya")
    print(open("flag.txt").read())
else:
    print("Bob: Hey apa apaan ini, ini bukan tiket asli!")

# Close the connection
conn.close()
