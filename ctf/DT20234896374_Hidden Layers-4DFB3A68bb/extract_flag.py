from PIL import Image
import numpy as np

# Load the image
img = Image.open("image_4DFB3A68bb.png")
pixels = np.array(img)

# Extract LSB from each channel
bits = []
for row in pixels:
    for pixel in row:
        for channel in pixel:
            bits.append(channel & 1)

# Convert bits to bytes
message = []
for i in range(0, len(bits) - 7, 8):
    byte = 0
    for j in range(8):
        byte = (byte << 1) | bits[i + j]
    if byte == 0:
        break
    if 32 <= byte < 127:
        message.append(chr(byte))

result = ''.join(message)

# Extract just the flag
if "HQX{" in result:
    start = result.index("HQX{")
    end = result.index("}", start) + 1
    flag = result[start:end]
    print(f"Flag: {flag}")
else:
    print("Flag not found")
