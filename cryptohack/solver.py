from pwn import xor

# Original flag and key
flag = "STEMBACTF{Th1s_A1_been_tr41ned_f0r_1337_t1mes}".encode('utf-8')
key = "adminganteng12345".encode('utf-8')

# Repeat the key to match the length of the flag
repeated_key = (key * (len(flag) // len(key) + 1))[:len(flag)]

# Perform XOR operation
result = xor(flag, repeated_key)

# Convert result to a readable string (if possible)
result_string = result.decode('utf-8', errors='ignore')

# Print the results
print("Flag (bytes):", flag)
print("Key (bytes):", repeated_key)
print("XOR Result (bytes):", result)
print("XOR Result (string):", result_string)

# Detailed XOR analysis (optional)
print("\nDetailed XOR analysis:")
for i in range(len(flag)):
    flag_char = chr(flag[i]) if 32 <= flag[i] <= 126 else f"\\x{flag[i]:02x}"
    key_char = chr(repeated_key[i]) if 32 <= repeated_key[i] <= 126 else f"\\x{repeated_key[i]:02x}"
    result_char = chr(result[i]) if 32 <= result[i] <= 126 else f"\\x{result[i]:02x}"
    print(f"{flag_char} ({flag[i]:02x}) XOR {key_char} ({repeated_key[i]:02x}) = {result_char} ({result[i]:02x})")
