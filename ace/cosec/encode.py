from sympy import csc
import sympy as sp

# Encode string ke integer
string_value = 'ACECTF{halobang}'
integer_value = int.from_bytes(string_value.encode(), 'big')

# Hitung csc dari integer
csc_value = csc(integer_value)

# Print hasil dengan presisi tinggi
print(csc_value)
