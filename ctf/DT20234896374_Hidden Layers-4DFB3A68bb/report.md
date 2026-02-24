# Hidden Layers CTF Challenge - Report

## Challenge Overview
- **Challenge Name:** Hidden Layers - 100
- **Category:** Steganography
- **File:** image_4DFB3A68bb.png (384x256 RGB PNG)

## Hint Analysis
> "The flag isn't hiding in plain sight, it's tucked away in the quietest corners of the image, where only the most observant eyes dare to look."

Keywords like **"quietest corners"** and **"whisper"** pointed to **LSB (Least Significant Bit) steganography** - a technique that hides data in the least significant bits of pixel values.

## Technique Used: LSB Steganography

LSB steganography works by:
1. Taking each pixel's RGB color channels (values 0-255)
2. Extracting the least significant bit (the "quietest" bit that causes minimal visual change)
3. Combining these bits to form hidden bytes/characters

## Solution Steps

1. **Loaded the image** using PIL and converted to numpy array
2. **Extracted LSB** from each color channel (R, G, B) of every pixel
3. **Grouped bits into bytes** (8 bits = 1 character)
4. **Converted bytes to ASCII** characters to reveal the hidden message

## Flag Captured

```
HQX{24c0ce09e0eb65a4944c33439d1d48f0}
```

## Tools Used
- Python 3
- PIL (Pillow) - Image processing
- NumPy - Array manipulation
