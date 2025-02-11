from hashlib import md5

# Example hex strings
alice_hex = "d131dd02c5e6eec4693d9a0698aff95c"
bob_hex = "d131dd02c5e6eec4693d9a0698aff95d"

# Convert hex to bytes
alice = bytes.fromhex(alice_hex)
bob = bytes.fromhex(bob_hex)

# Compute MD5 hashes
md5alice = md5(alice).hexdigest()
md5bob = md5(bob).hexdigest()

# Output the results
print(f"MD5 of Alice's ticket: {md5alice}")
print(f"MD5 of Bob's ticket: {md5bob}")
