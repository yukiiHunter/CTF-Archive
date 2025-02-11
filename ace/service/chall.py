#!/usr/bin/python3
import os, sys, string
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = os.urandom(16)
safe_command = string.ascii_letters + string.digits + '/.*'


def encrypt():
    user = input("\nenc(ls -al <input>): ")
    if any(c not in safe_command for c in user):
        print("dont do nasty!")
        return
    
    cmd = 'ls -al ' + user
    iv = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC, iv)
    ct = aes.encrypt(pad(cmd.encode(), 16))
    print(f"encrypted ls command: {(iv+ct).hex()}")

def execute():
    cmd = bytes.fromhex(input("\nexec(dec(<hex>)): "))
    iv, ct = cmd[:16], cmd[16:] 
    aes = AES.new(key, AES.MODE_CBC, iv)
    cmd = unpad(aes.decrypt(ct), 16).decode()
    subprocess.run(
        cmd,
        shell=True,
    )

def main():
    while 1:
        try:
            print("\n1. encrypt ls command")
            print("2. execute encrypted ls")
            print("3. exit")
            choice = int(input("> "))
            match choice:
                case 1:
                    encrypt()
                case 2:
                    execute()
                case 3:
                    exit()
                case _:
                    print("invalid choice")
                    
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()
