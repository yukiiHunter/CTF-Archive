from pwn import xor

data = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
    # Convert integer to single byte
    single_byte = i.to_bytes(1, byteorder='big')
    
    # XOR the data with the single byte
    result = xor(data, single_byte)
    
    # Print the result in both hex and ASCII (if printable)
    try:
        print(f"Byte: {i:02x} -> Result: {result.hex()} -> ASCII: {result.decode('utf-8', errors='ignore')}")
    except UnicodeDecodeError:
        # Skip non-decodable results
        continue
