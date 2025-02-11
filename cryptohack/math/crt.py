from sympy import factorint, mod_inverse
from sympy.ntheory.modular import crt

N = 935
ints = [5, 11, 17]
a = [2, 3, 5]

f, _ = crt(ints, a)
print(f'{f} ini flagnya king')

# def qr(a, p) :
#     if pow(a, (p - 1) // 2, p) != 1 :
#         return None
#     return pow(a, (p + 1) // 4, p)

# factors = factorint(N)
# print(factors)
# # {5: 1, 11: 1, 17: 1}

# p1, p2, p3 = 5, 11, 17
# N = p1 * p2 * p3

# a1, a2, a3 = 2, 3, 5

# x1 = qr(a1, p1)
# x2 = qr(a2, p2)
# x3 = qr(a3, p3)

# if x1 is not None and x2 is not None and x3 is not None :
#     solution = []

#     for r1 in [x1, p1 - x1] :
#         for r2 in [x2, p2 - x2] :
#             for r3 in [x3, p3 - x3] :
#                 result = crt([p1, p2, p3], [r1, r2, r3])[0]
#                 solution.append(result)
#     print(f'{a1, a2, a3} mod {N} = {solution}')
# else :
#     print("Nope")