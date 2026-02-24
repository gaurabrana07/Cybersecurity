#!/usr/bin/env python3
"""
Know Meh Better - CTF Challenge Solution
"""

import base64

# Step 1: Encoded hex from output file
encoded_hex = "0123322c1714694427216d173a393b543f5a221179133d1f22346a033467374b2e0523412c033f543c6a131d2e31115e4625"

# Step 2: Hex decode
encoded_bytes = bytes.fromhex(encoded_hex)

# Step 3: XOR key (len.__doc__ from decompiled code)
xor_key = "Return the number of items in a container."

# Step 4: XOR decrypt
xor_result = ''.join([chr(encoded_bytes[i] ^ ord(xor_key[i % len(xor_key)])) for i in range(len(encoded_bytes))])

# Step 5: Base64 decode
flag = base64.b64decode(xor_result + "==").decode('utf-8')

print(f"\n🚩 FLAG: {flag}\n")
