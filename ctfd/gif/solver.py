def shift_bytes(input_file, output_file):
    # Baca konten file input sebagai bytes
    with open(input_file, 'rb') as f:
        data = bytearray(f.read())

    # Inisialisasi variabel untuk mengontrol proses shifting
    shift = -3  # Perubahan byte sebanyak -3
    chunk_size = 3  # Ukuran chunk yang akan di-shift

    # Loop untuk memproses data sesuai pola
    for i in range(0, len(data), chunk_size * 2):
        # Shift 3 bytes pertama di setiap pola
        for j in range(chunk_size):
            if i + j < len(data):
                data[i + j] = (data[i + j] + shift) % 256  # Menghindari overflow

        # 3 bytes berikutnya dibiarkan tanpa perubahan, jadi lompat ke posisi berikutnya

    # Simpan hasil shifting ke file output
    with open(output_file, 'wb') as f:
        f.write(data)

# Contoh penggunaan
input_file = 'chall.gif'
output_file = 'shifted.gif'
shift_bytes(input_file, output_file)
