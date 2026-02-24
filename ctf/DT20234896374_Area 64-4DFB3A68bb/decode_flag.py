"""
Area 64 CTF Challenge - Flag Decoder
=====================================
This script decodes the hidden flag from the Base64 encoded string
found in the 4DFB3A68bb.txt file.
"""

import base64

def decode_flag():
    # The encoded string found in the challenge file
    encoded_string = "WW91J3JlIGluc2lkZSBBcmVhIDY0LiBIZXJlJ3MgeW91ciBrZXkgOiBIUVh7NzBjNWQ1MjVjYTBlMjc4MDY1NTNiNGE0OWJmNGNjZjh9"
    
    # Decode from Base64
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_message = decoded_bytes.decode('utf-8')
    
    return decoded_message

def extract_flag(message):
    # Extract the flag from the decoded message
    # Flag format: HQX{...}
    import re
    flag_pattern = r'HQX\{[a-fA-F0-9]+\}'
    match = re.search(flag_pattern, message)
    
    if match:
        return match.group()
    return None

def main():
    print("=" * 60)
    print("        AREA 64 CTF CHALLENGE - FLAG DECODER")
    print("=" * 60)
    print()
    
    # Step 1: Read and display the encoded string
    encoded = "WW91J3JlIGluc2lkZSBBcmVhIDY0LiBIZXJlJ3MgeW91ciBrZXkgOiBIUVh7NzBjNWQ1MjVjYTBlMjc4MDY1NTNiNGE0OWJmNGNjZjh9"
    print("[*] Encoded String Found:")
    print(f"    {encoded}")
    print()
    
    # Step 2: Decode the Base64 string
    decoded_message = decode_flag()
    print("[*] Decoded Message:")
    print(f"    {decoded_message}")
    print()
    
    # Step 3: Extract and display the flag
    flag = extract_flag(decoded_message)
    print("[+] FLAG CAPTURED:")
    print(f"    {flag}")
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
