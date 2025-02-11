n = 29
ints = [14, 6, 11]

def qr(n, x) :
    for a in range(n) :
        if (a * a) % n == x :
            return a
    return None

for x in ints :
    root = qr(n, x) 

    if root is not None:
        print(f"\n{x} Bruhh noob. This is what you got : {root}")
    else:
        print(f"\n{x} Yattaaaa you got pranked!!")