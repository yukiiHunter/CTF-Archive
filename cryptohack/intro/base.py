import base64

def hex_to_base64(hex_string):
    # Decode the hex string to bytes
    byte_data = bytes.fromhex(hex_string)
    
    # Encode the byte data to Base64
    base64_data = base64.b64encode(byte_data)
    
    # Convert the Base64 bytes to a string
    return base64_data.decode('utf-8')

# Example usage
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"  # Replace with your hex string
base64_encoded = hex_to_base64(hex_string)
print("Base64 Encoded:", base64_encoded)
