import httpx
import random
import string

BASE_URL = "http://challenges.ctf.compfest.id:9010/"
c = httpx.Client(base_url=BASE_URL)

def get_icb_256_hash(msg: bytes) -> bytes:
    """Get icb_256 hash of a message by sending it to the /sign endpoint."""
    response = c.get("/sign", params={"message": msg.hex()})
    if response.status_code == 403:
        # Forbidden, meaning icb_256(message) == icb_256(magic_string)
        return None
    elif response.status_code == 200:
        return response.json().get("signature")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def find_valid_message():
    """Try to find a valid message that does not match icb_256(magic_string)."""
    # Attempt to sign random messages until we find a valid one
    for _ in range(10000):  # Adjust the range as needed
        message = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        message_bytes = message.encode()
        if get_icb_256_hash(message_bytes) is not None:
            print(f"Found valid message: {message}")
            return message
    print("No valid message found.")
    return None

if __name__ == "__main__":
    valid_message = find_valid_message()
    if valid_message:
        print(f"Valid message found: {valid_message}")
    else:
        print("Failed to find a valid message.")
