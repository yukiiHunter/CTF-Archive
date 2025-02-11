import httpx

BASE_URL = "http://challenges.ctf.compfest.id:9010/"
c = httpx.Client(base_url=BASE_URL)

def sign(msg: str):
    """Send a message to the /sign endpoint and print the result."""
    r = c.get("/sign", params={"message": msg})
    print(f"[RESULT] {r.text}")
    return r

def find_similar_message(base_message: str, variations: int):
    """Generate messages similar to the base_message and try to find a valid one."""
    for i in range(variations):
        # Create a new message by modifying the base_message slightly
        message = base_message + chr(65 + (i % 26))  # Example: appending letters A-Z
        message_bytes = message.encode()
        message_hex = message_bytes.hex()
        response = sign(message_hex)

        if response.status_code == 200:
            print(f"Valid message found: {message}")
            return message, response.json().get("signature")
        elif response.status_code == 403:
            print(f"Message '{message}' is restricted. Trying another message.")
        else:
            print(f"Unexpected response: {response.status_code} - {response.text}")

    print("Failed to find a valid message.")
    return None

if __name__ == "__main__":
    base_message = "SkibidiSigmaRizzleDizzleMyNizzleOffTheHizzleShizzleKaiCenat"
    valid_message, signature = find_similar_message(base_message, 100)
    if valid_message:
        print(f"Found valid message: {valid_message}, Signature: {signature}")
    else:
        print("No valid message found.")
