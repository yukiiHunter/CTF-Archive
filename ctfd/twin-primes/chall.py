from Crypto.Util.number import bytes_to_long, getPrime

flag = open("flag.txt","rb").read()

p = q = getPrime(2048)
n = p*q

e = 0x10001

m = bytes_to_long(flag)
c = pow(m,e,n)

with open("flag.txt","w") as f:
    f.write(f'n = {n}\nc = {c}\n')
    f.close()
