import httpx
import binascii

BASE_URL = "http://challenges.ctf.compfest.id:9010/"
client = httpx.Client(base_url=BASE_URL)

def sign_message(msg: bytes) -> str:
    """Attempt to sign a message and return the response."""
    msg_hex = binascii.hexlify(msg).decode()
    response = client.get("/sign", params={"message": msg_hex})
    return response.text

def brute_force_signature(base_message: bytes):
    """Brute force slight variations of the base message to find a valid signature."""
    for i in range(256):
        # Modify the message slightly, e.g., change the last byte
        modified_message = base_message[:-1] + bytes([base_message[-1] ^ i])
        response = sign_message(modified_message)
        if "signature" in response:
            print(f"Found valid message: {modified_message}")
            print(f"Signature: {response}")
            return modified_message, response
        else:
            print(f"Tried {modified_message.hex()}, not valid.")

    print("Could not find a valid message.")
    return None

if __name__ == "__main__":
    base_message = b"SkibidiSigmaRizzleDizzleMyNizzleOffTheHizzleShizzleKaiCenat"
    brute_force_signature(base_message)
