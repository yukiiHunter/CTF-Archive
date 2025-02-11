from pwn import xor

data1 = b'label'
data2 = 13

convert = data2.to_bytes(1, byteorder='big')

result = xor(data1, convert)
print(result)
