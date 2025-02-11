import struct
import zlib

with open("chall-rep.png", "rb") as f:
    data = bytearray(f.read())

# IHDR biasanya mulai dari byte 12
ihdr_index = data.find(b'IHDR') - 4
ihdr_length = struct.unpack(">I", data[ihdr_index:ihdr_index+4])[0]

# Hitung ulang CRC untuk IHDR
crc_start = ihdr_index + 4  # Dari "IHDR" ke depan
crc_end = crc_start + ihdr_length + 4  # Sampai akhir data IHDR
new_crc = zlib.crc32(data[crc_start:crc_end]) & 0xFFFFFFFF

# Tulis ulang CRC
data[crc_end:crc_end+4] = struct.pack(">I", new_crc)

with open("fixed.png", "wb") as f:
    f.write(data)

print("CRC IHDR diperbaiki!")
