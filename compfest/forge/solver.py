import httpx

BASE_URL = "http://challenges.ctf.compfest.id:9010/"
c = httpx.Client(base_url=BASE_URL)

def sign(msg: str):
    r = c.get("/sign", params={"message": msg})
    print(f"[RESULT] {r.text}")

def pubkey():
    r = c.get("/pubkey")
    print(f"[RESULT] {r.text}")

def get_flag(sig: str):
    r = c.get("/get_flag", params={"signature": sig})
    print(f"[RESULT] {r.text}")

if __name__ == "__main__":
    while 1:
        print("Choose opts:")
        print("1. Sign")
        print("2. Pubkey")
        print("3. Get Flag")
        opt = int(input(">>> "))

        if opt == 1:
            msg = input("Message (hex): ")
            sign(msg)
        elif opt == 2:
            pubkey()
        elif opt == 3:
            sig = input("Signature (hex): ")
            get_flag(sig)
        else:
            print("Invalid option")
