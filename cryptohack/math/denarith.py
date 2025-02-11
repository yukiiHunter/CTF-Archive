num = 273246787654
p = 65537
q = p - 1
#print((num ^ (p-1)) % p)

print((num ^ q) % p)
print((num ^ p) % p)

print(pow(num, p-1, p))
