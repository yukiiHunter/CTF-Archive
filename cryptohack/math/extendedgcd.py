#import math

#p = 26513
#q = 32321

#print(math.gcd(p, q))

# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0
#     gcd, u1, v1 = extended_gcd(b, a % b)
#     u = v1
#     v = u1 - (a // b) * v1
#     return gcd, u, v

# # Contoh penggunaan
# a = 26513
# b = 32321
# gcd, u, v = extended_gcd(a, b)
# print(f"GCD({a}, {b}) = {gcd}")
# print(f"u = {u}, v = {v}")

# def egcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = egcd(b % a, a)
#         return gcd, y - (b // a) * x, x


# print(egcd(26513, 32321))

from egcd import egcd

p = 26513
q = 32321

egcd(p, q)