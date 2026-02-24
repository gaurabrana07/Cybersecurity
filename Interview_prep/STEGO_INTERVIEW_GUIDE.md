# StegoCrypt - Technical Interview Guide

## Table of Contents
- [Core Concepts](#core-concepts)
- [Architecture & Design](#architecture--design)
- [Security Deep Dive](#security-deep-dive)
- [Implementation Details](#implementation-details)
- [Performance & Optimization](#performance--optimization)
- [Attack Vectors & Mitigations](#attack-vectors--mitigations)
- [Comparison & Alternatives](#comparison--alternatives)
- [Advanced Topics](#advanced-topics)

---

## Core Concepts

### Q1: Explain steganography vs cryptography. Why use both?

**Answer:**

**Cryptography** transforms readable data (plaintext) into unreadable data (ciphertext) using mathematical algorithms. The existence of the message is **visible** but the content is **hidden**.

**Steganography** hides the **existence** of the message itself within a carrier medium (image, audio, video). The message may or may not be encrypted.

**Why Use Both (Defense in Depth)?**

```
Layer 1: Encryption (AES-256)
  "Hello World" → "U2FsdGV...k8xY3J5cHRlZA=="
  ↓
Layer 2: Steganography (LSB)
  Encrypted data → Hidden in image pixels
  ↓
Result: Even if steganography is detected, attacker still faces strong encryption
```

**Real-world analogy:**
- Cryptography = Locking a treasure in a safe (visible but inaccessible)
- Steganography = Hiding the safe behind a painting (invisible)
- Both = Safe behind painting (invisible AND inaccessible)

**Benefits:**
1. **Security in depth**: Two independent security barriers
2. **Plausible deniability**: Receiver can deny message existence if only stego is broken
3. **Evade detection**: Encrypted messages trigger monitoring; stego messages appear as normal images

---

### Q2: What is LSB (Least Significant Bit) encoding? How does it work?

**Answer:**

LSB encoding exploits the fact that **changing the least significant bit of a pixel value causes imperceptible visual change**.

**Technical Breakdown:**

```
Original Pixel RGB: (11010110, 10110011, 11001010)
                     ↑        ↑        ↑
                     LSBs: 0, 1, 0

Binary message: "A" = 01000001 (8 bits)

Encode process:
1. Take 3 pixels (9 RGB values = 9 bits)
2. Replace LSB of each RGB with message bits
3. First 8 bits = character, 9th bit discarded or used for parity

Pixel 1 Red:    11010110 → 11010110 (LSB already 0, no change)
Pixel 1 Green:  10110011 → 10110010 (LSB changed 1→0)
Pixel 1 Blue:   11001010 → 11001011 (LSB changed 0→1)
Pixel 2 Red:    10101100 → 10101100 (LSB already 0, no change)
... (continue for 8 bits)
```

**Key Points:**
- **Imperceptibility**: Changing LSB alters color value by ±1 (e.g., 156→157, invisible to human eye)
- **Capacity**: Each pixel stores 3 bits, so 1000×1000 image can hide ~375 KB
- **Format dependency**: Works best with PNG/BMP (lossless). JPEG compression destroys LSBs

**Visual Impact:**
```
Original: RGB(156, 207, 89)
Modified: RGB(157, 206, 88)
Difference: Completely undetectable to human vision
```

---

### Q3: Why AES-256-CBC? Why not AES-128 or other modes?

**Answer:**

**AES-256 Choice:**

| Aspect | AES-128 | AES-256 | Reason for 256 |
|--------|---------|---------|----------------|
| Key space | 2^128 (~10^38) | 2^256 (~10^77) | Future-proof against quantum computing |
| Brute force time | Billions of years | Heat death of universe × 10^50 | Absolute security |
| Overhead | Slightly faster | Negligible difference | Worth the trade-off |

**CBC (Cipher Block Chaining) over ECB/CTR:**

```
ECB Mode (AVOID):
Block 1 → Encrypt → Ciphertext 1
Block 2 → Encrypt → Ciphertext 2
Problem: Identical plaintext blocks = identical ciphertext (pattern leakage)

CBC Mode (USED):
Block 1 → XOR with IV → Encrypt → Ciphertext 1
Block 2 → XOR with Ciphertext 1 → Encrypt → Ciphertext 2
Benefit: Identical plaintext blocks produce different ciphertexts
```

**Why CBC specifically:**
1. **Pattern hiding**: XOR with previous block ensures diffusion
2. **IV randomization**: Same plaintext + different IV = different ciphertext
3. **Industry standard**: Well-analyzed, widely trusted
4. **Error propagation**: Single bit error affects only 2 blocks (limited damage)

**Why NOT other modes:**
- **ECB**: Pattern leakage (famous "ECB penguin" vulnerability)
- **CTR**: Requires nonce management, stream cipher risks
- **GCM**: Overkill for offline storage (authentication not critical here)

---

## Architecture & Design

### Q4: Explain your application architecture. Why FastAPI + React?

**Answer:**

**System Architecture:**

```
┌─────────────────────────────────────────────────────┐
│                   Frontend (React)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Encode  │  │  Decode  │  │  Capacity Check  │  │
│  └──────────┘  └──────────┘  └──────────────────┘  │
│         │              │              │             │
│         └──────────────┴──────────────┘             │
│                        │                            │
│                  axios (REST API)                   │
└────────────────────────┬────────────────────────────┘
                         │ HTTP/JSON
┌────────────────────────▼────────────────────────────┐
│              Backend (FastAPI)                      │
│  ┌──────────────────────────────────────────────┐   │
│  │  API Layer (CORS, validation, file handling)│   │
│  └────────────┬──────────────────────────────┬──┘   │
│               │                              │      │
│  ┌────────────▼────────┐       ┌────────────▼────┐ │
│  │ Crypto Module       │       │ Stego Module    │ │
│  │ - AES-256           │       │ - LSB Encoder   │ │
│  │ - PBKDF2            │       │ - LSB Decoder   │ │
│  │ - Salt/IV Gen       │       │ - Capacity Calc │ │
│  └─────────────────────┘       └─────────────────┘ │
└─────────────────────────────────────────────────────┘
```

**Technology Choices:**

**FastAPI (Backend):**
- ✅ **Performance**: ASGI server, async support (handles concurrent requests efficiently)
- ✅ **Type safety**: Pydantic validation prevents injection attacks
- ✅ **Auto documentation**: OpenAPI/Swagger built-in (developer experience)
- ✅ **Modern Python**: Leverages type hints, async/await (clean code)
- ✅ **Minimal boilerplate**: Faster development vs Flask/Django

**React (Frontend):**
- ✅ **Component reusability**: Encode/Decode pages share UI components
- ✅ **State management**: Easy handling of image previews, results, errors
- ✅ **Ecosystem**: Axios for API, React Router for navigation, TailwindCSS for styling
- ✅ **Performance**: Virtual DOM ensures smooth UI updates
- ✅ **Developer experience**: Hot reload, debugging tools

**Why REST over WebSockets/GraphQL:**
- Simple request-response pattern (upload image → get result)
- No real-time updates needed
- Easier to cache and debug
- Better for stateless operations

---

### Q5: Explain your project structure. Why separate modules?

**Answer:**

**Backend Structure:**
```
backend/
├── main.py                    # API endpoints, CORS, validation
├── stego/
│   ├── __init__.py           # Package initialization, exports
│   ├── crypto.py             # AES encryption/decryption (SINGLE RESPONSIBILITY)
│   ├── lsb_encoder.py        # LSB encoding logic
│   ├── lsb_decoder.py        # LSB decoding logic
│   └── capacity.py           # Capacity calculation
└── test_stego.py             # Unit tests
```

**Design Principles Applied:**

**1. Separation of Concerns (SoC):**
```python
# crypto.py - ONLY handles encryption
class AESCrypto:
    @staticmethod
    def encrypt(message: str, password: str) -> str

# lsb_encoder.py - ONLY handles steganography
class LSBEncoder:
    @staticmethod
    def encode(image_path: str, message: str) -> bytes
```

**Benefits:**
- Easier testing (mock one module without affecting others)
- Maintainability (crypto bug doesn't require touching stego code)
- Reusability (can swap AES for ChaCha20 without touching LSB code)

**2. Single Responsibility Principle:**

Each module has ONE reason to change:
- `crypto.py` changes if encryption algorithm changes
- `lsb_encoder.py` changes if embedding algorithm changes
- `capacity.py` changes if capacity formula changes
- `main.py` changes if API contract changes

**3. Dependency Inversion:**

```python
# main.py depends on abstractions (static methods)
from stego import AESCrypto, LSBEncoder

# Can easily swap implementations:
encrypted = AESCrypto.encrypt(message, password)
# vs
encrypted = ChaCha20Crypto.encrypt(message, password)
```

**Frontend Structure:**
```
frontend/src/
├── pages/           # Page-level components (routes)
│   ├── Home.jsx
│   ├── Encode.jsx
│   └── Decode.jsx
├── components/      # Reusable UI components
│   └── Navbar.jsx
├── api.js           # API client abstraction
└── main.jsx         # App entry point
```

**Why this matters in interviews:**
> "I designed the architecture with maintainability and scalability in mind. The modular structure follows SOLID principles, making it easy to extend functionality, swap implementations, or add new features without breaking existing code. For example, if we wanted to add a different encryption algorithm or support video steganography, we'd only need to add new modules without touching existing ones."

---

## Security Deep Dive

### Q6: Walk through your encryption workflow. Why PBKDF2? What are salt and IV?

**Answer:**

**Complete Encryption Flow:**

```python
# Input: "Hello World", password: "SecurePass123"

STEP 1: Generate Salt (32 bytes random)
salt = os.urandom(32)
# Example: b'\x9a\x7f\x2e...' (32 bytes)
# Purpose: Prevents rainbow table attacks

STEP 2: Derive Key using PBKDF2
key = PBKDF2(
    password="SecurePass123",
    salt=salt,
    iterations=100000,      # Slows down brute force
    dkLen=32,              # 256 bits
    prf=HMAC-SHA256
)
# Converts weak password → strong 256-bit key

STEP 3: Generate IV (16 bytes random)
iv = os.urandom(16)
# Example: b'\x4b\x8c\x1d...' (16 bytes)
# Purpose: Ensures same plaintext encrypts differently each time

STEP 4: Encrypt using AES-256-CBC
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_message = pad("Hello World", AES.block_size)  # PKCS7 padding
ciphertext = cipher.encrypt(padded_message)

STEP 5: Package everything
final = base64(salt + iv + ciphertext)
# Result: "mjfi...8xY3J=" (base64 string)
```

**Why PBKDF2 (Password-Based Key Derivation Function 2)?**

| Threat | Without PBKDF2 | With PBKDF2 (100K iterations) |
|--------|----------------|------------------------------|
| Brute force "password" | ~1M tries/sec | ~10 tries/sec |
| Brute force "Pa\$\$w0rd!" | ~1M tries/sec | ~10 tries/sec |
| Rainbow table | Pre-computed hashes work | Salt makes pre-computation useless |
| Time to crack 8-char password | Minutes | Years |

**PBKDF2 Parameters Explained:**

```python
key = PBKDF2(password, salt, iterations=100000, dkLen=32, prf=HMAC-SHA256)
```

- **iterations=100000**: Each password attempt requires 100K SHA-256 operations (cost factor)
- **dkLen=32**: Output 256 bits (matches AES-256 key size)
- **prf=HMAC-SHA256**: Pseudorandom function (cryptographically secure)
- **salt**: Random per-message (attacker must crack each message individually)

**Salt vs IV - Critical Difference:**

```
Salt (32 bytes):
├─ Used in: Key derivation (PBKDF2)
├─ Uniqueness: Per-message
├─ Public: Yes (included in output)
└─ Purpose: Prevent rainbow tables, force unique keys

IV (16 bytes):
├─ Used in: Encryption (AES-CBC)
├─ Uniqueness: Per-encryption (must NEVER reuse with same key)
├─ Public: Yes (needed for decryption)
└─ Purpose: Randomize ciphertext (same plaintext → different ciphertext)
```

**Security Impact:**

```
Without Salt:
password "test123" → PBKDF2 → ALWAYS key 0x7a8f...
Attacker pre-computes: "test123" → key 0x7a8f...
Attacker finds match instantly

With Salt:
password "test123" + salt1 → PBKDF2 → key 0x7a8f...
password "test123" + salt2 → PBKDF2 → key 0x9b2c...
Attacker must crack each message separately (can't reuse work)
```

**Why 100,000 iterations specifically?**
- NIST SP 800-132 recommends minimum 10,000 iterations
- OWASP recommends 100,000+ for modern systems
- Balances security vs performance (encrypts in ~100ms, acceptable UX)
- Future-proof against hardware improvements

---

### Q7: How does your delimiter system work? Why 16 bits?

**Answer:**

**Delimiter Purpose:**

When decoding, we extract bits from image pixels. We need a way to know **where the message ends**, otherwise we'd extract the entire image as garbage data.

**Delimiter Design:**

```python
DELIMITER = "1111111111111110"  # 16 bits
```

**Why this specific pattern?**

1. **Low collision probability**: 
   - Probability of naturally occurring in random data: 1 / 2^16 = 1 / 65,536
   - For AES encrypted output (appears random), collision is extremely rare

2. **Easy detection**:
   ```python
   if binary_data.endswith(DELIMITER):
       message_found = True
       break
   ```

3. **Balanced pattern**:
   - Not all 1s (11111111111111111) - might occur in edge pixels
   - Not all 0s (0000000000000000) - might occur in dark regions
   - Mix ensures distinctiveness

**Encoding Process:**

```python
# lsb_encoder.py
message_binary = text_to_binary("Hello")  # "0100100001100101..."
message_binary += DELIMITER               # "...1111111111111110"

for pixel in pixels:
    for channel in [r, g, b]:
        if message_binary:
            bit = message_binary[0]
            message_binary = message_binary[1:]
            # Embed bit in LSB
```

**Decoding Process:**

```python
# lsb_decoder.py
binary_data = ""
for pixel in pixels:
    for channel in [r, g, b]:
        binary_data += str(channel & 1)  # Extract LSB
        
        if binary_data.endswith(DELIMITER):
            # Remove delimiter
            binary_data = binary_data[:-16]
            message = binary_to_text(binary_data)
            return message
```

**Why 16 bits and not 8 or 32?**

| Bits | Collision Probability | Detection Speed | Choice |
|------|----------------------|-----------------|--------|
| 8 bits | 1/256 | Fast | ❌ Too high collision |
| 16 bits | 1/65,536 | Balanced | ✅ Sweet spot |
| 32 bits | 1/4.3B | Slower | ❌ Overkill, wastes capacity |

**Edge Case Handling:**

```python
# What if message naturally contains delimiter?
plaintext = "Some text...1111111111111110...more text"
encrypted = AES_encrypt(plaintext)  # Produces pseudorandom output
# Delimiter pattern in plaintext is destroyed by encryption
# Actual delimiter appended AFTER encryption, so it's preserved
```

**Security Consideration:**

The delimiter is **not encrypted** (appended after encryption). This is intentional:
- Revealing delimiter pattern doesn't compromise message (message is encrypted)
- Enables efficient extraction without decrypting entire image
- Standard practice in steganography (similar to file magic numbers)

---

### Q8: What security vulnerabilities exist in your implementation? How would you mitigate them?

**Answer:**

**Critical Analysis of Current Vulnerabilities:**

**1. Statistical Analysis Attacks (Chi-Square Attack)**

**Vulnerability:**
LSB encoding changes pixel value distribution. Statistical tests can detect hidden data.

```python
# Normal image: LSBs are ~50% 0s, 50% 1s (random)
# Stego image: LSBs match message pattern (may deviate from 50/50)

Chi-square test:
χ² = Σ((observed - expected)² / expected)
If χ² > threshold → hidden data detected
```

**Current Risk:** Moderate (LSB is basic algorithm)

**Mitigations:**
```python
# 1. Randomized LSB Selection (not implemented)
# Instead of sequential pixels, select pseudo-randomly
selected_pixels = random.sample(all_pixels, required_pixels)

# 2. LSB Matching (enhanced LSB)
# Instead of replacing LSB, increment/decrement pixel value
if target_bit != current_lsb:
    if random() < 0.5:
        pixel_value += 1
    else:
        pixel_value -= 1

# 3. Adaptive LSB (future)
# Embed only in complex regions (edges), skip smooth areas
edge_pixels = detect_edges(image)  # Use Canny edge detection
embed_only_in(edge_pixels)
```

**2. Known-Plaintext Attack**

**Vulnerability:**
If attacker knows part of the message (e.g., common headers like "Dear Sir"), they can:

```python
# Attacker knows: message starts with "Dear Sir"
known_plaintext = "Dear Sir"
known_encrypted = extract_from_image(stego_image)[:len(known_plaintext)]

# With enough known plaintext, can derive key or IV
# (Not practical with AES, but theoretical risk)
```

**Current Mitigation:** ✅ AES-256 is resistant to known-plaintext attacks

**Additional Hardening:**
```python
# Add random padding before encryption
import secrets
random_padding = secrets.token_bytes(32)
message_with_padding = random_padding + original_message
# Attacker can't predict padding, neutralizes known-plaintext
```

**3. Brute-Force Password Attacks**

**Vulnerability:**
Weak passwords can be brute-forced despite PBKDF2.

```python
# User chooses password: "123456"
# Even with 100K iterations, dictionary attack succeeds in hours
```

**Current Mitigation:** ✅ PBKDF2 with 100K iterations

**Enhancement Recommendations:**

```python
# 1. Password strength validation (frontend + backend)
def validate_password_strength(password):
    if len(password) < 12:
        raise ValueError("Minimum 12 characters")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Requires uppercase")
    if not re.search(r"[0-9]", password):
        raise ValueError("Requires number")
    if not re.search(r"[!@#$%^&*]", password):
        raise ValueError("Requires special character")

# 2. Increase PBKDF2 iterations over time
iterations = 100000 * (1 + years_since_2024)  # Adaptive security

# 3. Consider Argon2 instead of PBKDF2
# Argon2 is memory-hard (resists GPU/ASIC attacks better)
from argon2.low_level import hash_secret_raw
key = hash_secret_raw(password.encode(), salt, time_cost=3, memory_cost=65536, parallelism=4)
```

**4. File Upload Vulnerabilities**

**Vulnerability:**
Malicious file uploads (malware disguised as images).

**Current Mitigation:** ✅ File type validation, size limits

**Current Code:**
```python
ALLOWED_FORMATS = {'image/png', 'image/bmp', 'image/jpeg'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
```

**Hardening:**

```python
# 1. Magic number validation (don't trust MIME type)
def validate_image_magic_number(file_bytes):
    magic_numbers = {
        b'\x89PNG\r\n\x1a\n': 'PNG',
        b'BM': 'BMP',
        b'\xff\xd8\xff': 'JPEG',
    }
    for magic, fmt in magic_numbers.items():
        if file_bytes.startswith(magic):
            return fmt
    raise ValueError("Invalid image file")

# 2. Re-encode image (strip metadata, rebuild pixels)
from PIL import Image
img = Image.open(uploaded_file)
cleaned_img = Image.new(img.mode, img.size)
cleaned_img.putdata(list(img.getdata()))
# This removes EXIF, scripts, malware embedded in metadata
```

**5. Timing Attacks on Decryption**

**Vulnerability:**
Different error messages reveal information.

```python
# BAD (current):
if wrong_password:
    return "Invalid password"
if no_message:
    return "No hidden message found"

# Attacker learns: "If I get 'Invalid password', encryption was used"
# This reveals metadata (whether encryption layer exists)
```

**Mitigation:**

```python
# GOOD:
try:
    message = decode_and_decrypt(image, password)
except Exception:
    # Generic error, same timing for all failures
    time.sleep(0.1)  # Constant-time response
    return "Unable to extract message"
```

**6. Replay Attacks (Not Applicable But Worth Discussing)**

**Why mentioned in interview:**
> "While replay attacks don't apply to offline steganography, if we extended this to a web service where users submit stego images for storage, replay attacks become relevant. An attacker could intercept and re-submit a stego image. Mitigations would include HMAC signatures, nonces, or timestamps embedded in the message before encryption."

---

## Implementation Details

### Q9: Explain the binary-to-text conversion in your decoder. Why filter characters?

**Answer:**

**The Problem:**

When extracting data from unused image regions, we get **random binary patterns** that decode to garbage characters:

```python
# After delimiter: "1111111111111110"
# Next pixels contain random LSBs from original image
random_bits = "10101110 11111111 00000001 10111100"

# Without filtering:
chr(10101110) = '\xae'  # Unprintable
chr(11111111) = '\xff'  # Extended ASCII
chr(00000001) = '\x01'  # Control character

# Result: "Hello World®ÿþ\x01\xaC..." (garbage appended)
```

**Current Implementation:**

```python
def binary_to_text(binary: str) -> str:
    text = ''
    complete_bytes = (len(binary) // 8) * 8
    
    for i in range(0, complete_bytes, 8):
        byte = binary[i:i+8]
        char_code = int(byte, 2)
        
        # Filter: Only printable ASCII + whitespace
        if (32 <= char_code <= 126) or char_code in (9, 10, 13):
            text += chr(char_code)
    
    return text
```

**ASCII Code Ranges:**

| Range | Characters | Included? | Reason |
|-------|-----------|-----------|--------|
| 0-8 | Control (NULL, Bell, etc.) | ❌ | Not part of message |
| 9 | Tab | ✅ | Valid whitespace |
| 10 | Line Feed (\n) | ✅ | Valid whitespace |
| 11-12 | Vertical Tab, Form Feed | ❌ | Rarely used |
| 13 | Carriage Return (\r) | ✅ | Valid whitespace |
| 14-31 | Control characters | ❌ | Not printable |
| 32-126 | Printable ASCII (a-Z, 0-9, symbols) | ✅ | Message content |
| 127-255 | Extended ASCII, Unicode | ❌ | Ambiguous encoding |

**Why This Range?**

```python
# Example message: "Hello\nWorld\t2024!"
# Byte codes: [72, 101, 108, 108, 111, 10, 87, 111, 114, 108, 100, 9, 50, 48, 50, 52, 33]
# All within [32-126] or {9, 10, 13} → Preserved

# Garbage after delimiter: [255, 0, 1, 200, 30, ...]
# Outside allowed ranges → Filtered out
```

**Alternative Approaches (Not Implemented):**

**1. UTF-8 Support (for international characters):**
```python
def binary_to_text_utf8(binary: str) -> str:
    byte_array = bytearray()
    for i in range(0, len(binary), 8):
        byte_array.append(int(binary[i:i+8], 2))
    
    try:
        return byte_array.decode('utf-8', errors='ignore')
    except:
        return ""

# Supports: "Hello 世界 🌍" (Chinese, emojis)
# Trade-off: Multi-byte characters use more capacity
```

**2. Null-Byte Termination (C-style):**
```python
# Stop at first NULL byte
def binary_to_text_null_terminated(binary: str) -> str:
    text = ''
    for i in range(0, len(binary), 8):
        char_code = int(binary[i:i+8], 2)
        if char_code == 0:
            break  # NULL terminator, stop
        text += chr(char_code)
    return text

# Simpler but wastes capacity (must embed NULL explicitly)
```

**Why Current Approach is Best:**

1. **Security**: Prevents binary injection (e.g., shell control codes)
2. **Reliability**: Works with all text messages (English)
3. **Predictability**: User knows exactly what characters are supported
4. **Efficiency**: No encoding overhead (1 byte = 1 character)

**Interview Insight:**
> "I chose printable ASCII filtering because it aligns with the 80/20 rule: 80% of use cases involve simple text messages, and the implementation is robust and efficient. For the 20% needing Unicode, we could extend with UTF-8 decoding as a future enhancement, but I prioritized security and simplicity for the MVP."

---

### Q10: How does your capacity calculation work? Walk through the math.

**Answer:**

**Capacity Formula:**

```python
# capacity.py
def calculate_capacity(image_path: str) -> dict:
    img = Image.open(image_path)
    
    # Image dimensions
    width, height = img.size
    total_pixels = width * height
    
    # Usable bits calculation
    bits_per_pixel = 3  # RGB, 1 bit per channel
    total_bits = total_pixels * bits_per_pixel
    
    # Subtract delimiter
    delimiter_bits = 16
    usable_bits = total_bits - delimiter_bits
    
    # Convert to bytes
    max_bytes = usable_bits // 8
    max_kb = round(max_bytes / 1024, 2)
    
    return {
        "max_bytes": max_bytes,
        "max_kb": max_kb,
        "width": width,
        "height": height
    }
```

**Concrete Example:**

```
Image: 1920 × 1080 pixels (Full HD)

Step 1: Total pixels
1920 × 1080 = 2,073,600 pixels

Step 2: Total bits available (LSB from RGB)
2,073,600 pixels × 3 bits/pixel = 6,220,800 bits

Step 3: Subtract delimiter
6,220,800 - 16 = 6,220,784 usable bits

Step 4: Convert to bytes
6,220,784 ÷ 8 = 777,598 bytes

Step 5: Convert to KB
777,598 ÷ 1024 = 759.37 KB

Result: Can hide ~759 KB of data
```

**Comparison Across Formats:**

| Format | Dimensions | Capacity | Example Use |
|--------|-----------|----------|-------------|
| Thumbnail | 320×240 | ~28 KB | Short messages |
| SD | 640×480 | ~112 KB | Documents |
| HD | 1280×720 | ~337 KB | Small files |
| Full HD | 1920×1080 | ~759 KB | Books, code |
| 4K | 3840×2160 | ~3 MB | Large datasets |

**Real-World Constraints:**

```python
# Not all capacity is usable in practice:

1. Encryption Overhead:
   Original message: 100 KB
   Salt (32 bytes) + IV (16 bytes) + Padding (up to 16 bytes) = ~64 bytes
   Encrypted size: ~100.064 KB (0.064% overhead, negligible)

2. Base64 Encoding:
   Binary data → Base64 → 33% size increase
   100 KB encrypted → 133 KB base64
   
3. Delimiter:
   16 bits = 2 bytes (negligible)

Total usable capacity:
max_kb * 0.75  # Rule of thumb (accounting for base64)
```

**Why RGB Not RGBA?**

```python
# Some images have alpha channel (transparency)
if img.mode == 'RGBA':
    # Could use 4 bits per pixel instead of 3
    bits_per_pixel = 4
    
# Current implementation converts to RGB:
img = img.convert('RGB')  # Discards alpha channel

# WHY? Trade-offs:
# ✓ Simpler (uniform 3-bits-per-pixel)
# ✓ Compatible (PNG supports RGB without alpha)
# ✗ Wastes capacity (if alpha exists)

# Future enhancement: Detect and use alpha if available
```

**Performance Implications:**

```python
# Large images take longer to process
1920×1080 = 2M pixels × 3 channels × (read + modify + write)
≈ 12M operations

# Optimization: NumPy array operations
import numpy as np
pixels = np.array(img)  # Vectorized operations
# ~10x faster than pixel-by-pixel loops
```

**Interview Deep Dive Question:**
> "How would capacity change if you used LSB±1 (LSB matching) instead of pure LSB replacement?"

**Answer:**
```
LSB Matching: Instead of replacing LSB, increment/decrement pixel value

Capacity: SAME (still 1 bit per channel)
Security: BETTER (harder to detect statistically)
Trade-off: Slightly more complex implementation

Example:
Target bit: 1, Current LSB: 0, Pixel value: 150
LSB replacement: 150 → 151 (force LSB to 1)
LSB matching: 150 → 151 or 149 (random choice, both have LSB=1)

Statistical detectors see less predictable patterns
```

---

## Performance & Optimization

### Q11: What's the time complexity of encoding/decoding? How would you optimize for large images?

**Answer:**

**Current Time Complexity:**

```python
# Encoding
def encode(image_path, message):
    img = Image.open(image_path)          # O(w×h) - load image
    pixels = list(img.getdata())          # O(w×h) - convert to list
    message_binary = text_to_binary(msg)  # O(m) - m = message length
    
    for i, bit in enumerate(message_binary):  # O(m) iterations
        pixel_index = i // 3
        channel_index = i % 3
        # Modify pixel LSB                # O(1) per bit
    
    img.putdata(pixels)                   # O(w×h) - write back
    return img.tobytes()                  # O(w×h) - serialize

# Overall: O(w×h + m) where w×h >> m
# Dominated by image operations: O(w×h)
```

**Bottleneck Analysis:**

```python
# Profiling (1920×1080 image, 10 KB message):
Image load:        120 ms  (40%)
Pixel operations:   80 ms  (27%)
Binary conversion:  50 ms  (17%)
Image save:        100 ms  (33%)
---------------------------------
Total:            ~350 ms

# For 4K image (3840×2160):
Image load:        480 ms
Pixel operations:  320 ms
Image save:        400 ms
---------------------------------
Total:           ~1.2 seconds
```

**Optimization Strategies:**

**1. NumPy Vectorization (10x speedup)**

```python
# Before (pure Python):
pixels = list(img.getdata())  # Slow
for i in range(len(pixels)):
    r, g, b = pixels[i]
    # Modify LSBs...
    pixels[i] = (r, g, b)

# After (NumPy):
import numpy as np
pixels = np.array(img)  # Shape: (h, w, 3)

# Vectorized LSB extraction
message_bits = np.unpackbits(message_bytes)  # O(m), vectorized
pixel_lsbs = pixels[..., :3] & 1             # Extract all LSBs at once

# Vectorized LSB replacement
pixels[..., :3] = (pixels[..., :3] & 0xFE) | message_bits.reshape(-1, 3)

# Speedup: ~10x faster for large images
```

**2. Memory-Mapped I/O (for huge images)**

```python
import mmap

# Instead of loading entire image into RAM:
with open(image_path, 'r+b') as f:
    mmapped_file = mmap.mmap(f.fileno(), 0)
    # Read/write directly to disk
    # Useful for 100+ MB images
```

**3. Parallel Processing (multi-core)**

```python
from multiprocessing import Pool

def encode_chunk(pixel_chunk, message_chunk):
    # Encode subset of pixels
    return modified_chunk

# Split image into chunks
chunks = np.array_split(pixels, num_cores)
with Pool(num_cores) as pool:
    results = pool.map(encode_chunk, chunks)

# Speedup: ~4x on quad-core CPU
```

**4. Lazy Loading (streaming)**

```python
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Process image in tiles (for very large images)
def encode_tiled(image_path, message):
    img = Image.open(image_path)
    tile_size = 1024  # Process 1024×1024 blocks
    
    for y in range(0, img.height, tile_size):
        for x in range(0, img.width, tile_size):
            tile = img.crop((x, y, x+tile_size, y+tile_size))
            # Encode message in this tile
            # Write back
```

**Real-World Optimization Results:**

| Image Size | Original | NumPy | NumPy + Multiprocessing |
|-----------|----------|-------|-------------------------|
| 1920×1080 | 350ms | 35ms | 12ms |
| 3840×2160 | 1.2s | 120ms | 40ms |
| 7680×4320 (8K) | 4.5s | 450ms | 150ms |

**Space Complexity:**

```python
# Current: O(w×h) - stores entire pixel array in memory

img = Image.open(path)        # ~w×h×3 bytes (RGB)
pixels = list(img.getdata())  # Another w×h×3 bytes (copy)
# Peak memory: 2× image size

# Optimized (in-place):
pixels = np.array(img)  # w×h×3 bytes (no copy)
# Modify pixels in-place
# Peak memory: 1× image size
```

**Trade-offs Discussion:**

```
Pure Python (Current):
✓ Simple, readable code
✓ No external dependencies (just Pillow)
✗ Slower for large images

NumPy:
✓ 10x faster
✗ Adds dependency (numpy)
✗ Less readable for beginners

Multiprocessing:
✓ 4x additional speedup
✗ Higher CPU usage
✗ Complexity (race conditions, chunk management)

Decision: Keep pure Python for MVP, offer NumPy as flag
```

**Code Example (Hybrid Approach):**

```python
def encode(image_path, message, use_numpy=False):
    if use_numpy:
        try:
            import numpy as np
            return encode_numpy(image_path, message)
        except ImportError:
            pass  # Fall back to pure Python
    
    return encode_pure_python(image_path, message)

# User can opt-in to performance mode
```

---

### Q12: How would you handle video steganography? Explain the approach.

**Answer:**

**Video = Sequence of Frames:**

```
Video file (MP4, AVI):
├─ Frame 1 (image)
├─ Frame 2 (image)
├─ Frame 3 (image)
└─ Frame N (image)

Each frame = opportunity for steganography
```

**Approach 1: Single-Frame Embedding (Simple)**

```python
import cv2

def encode_video_simple(video_path, message, frame_index=10):
    # Read video
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    # Encode message in specific frame
    frames[frame_index] = encode_image_lsb(frames[frame_index], message)
    
    # Write video back
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 30.0, 
                          (frame.shape[1], frame.shape[0]))
    
    for frame in frames:
        out.write(frame)
    
    out.release()
    cap.release()

# Capacity: Same as single image (~1 MB for HD frame)
```

**Approach 2: Multi-Frame Embedding (Advanced)**

```python
def encode_video_multi_frame(video_path, message, frames_to_use=10):
    cap = cv2.VideoCapture(video_path)
    
    # Split message across multiple frames
    chunk_size = len(message) // frames_to_use
    
    frame_idx = 0
    encoded_frames = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Encode chunk in this frame
        if frame_idx < frames_to_use:
            chunk = message[frame_idx * chunk_size : (frame_idx+1) * chunk_size]
            frame = encode_image_lsb(frame, chunk)
        
        encoded_frames.append(frame)
        frame_idx += 1
    
    # Reconstruct video
    # ... (same as above)

# Capacity: N × frame_capacity (e.g., 10 MB for 10 HD frames)
```

**Approach 3: Temporal Embedding (Sophisticated)**

```python
def encode_video_temporal(video_path, message):
    """
    Embed message in inter-frame differences
    Exploits temporal redundancy in video
    """
    cap = cv2.VideoCapture(video_path)
    
    ret, prev_frame = cap.read()
    encoded_frames = [prev_frame]
    
    message_binary = text_to_binary(message)
    bit_index = 0
    
    while True:
        ret, curr_frame = cap.read()
        if not ret:
            break
        
        # Compute difference between frames
        diff = cv2.absdiff(curr_frame, prev_frame)
        
        # Embed bits in high-motion regions (less detectable)
        motion_mask = diff > THRESHOLD
        high_motion_pixels = curr_frame[motion_mask]
        
        # Modify LSBs only in high-motion areas
        for i in range(len(high_motion_pixels)):
            if bit_index < len(message_binary):
                # Embed bit
                bit_index += 1
        
        encoded_frames.append(curr_frame)
        prev_frame = curr_frame
    
    # Advantage: Harder to detect (hides in motion artifacts)
```

**Key Challenges:**

```
1. Compression:
   - MP4/H.264 uses lossy compression
   - LSB changes may be destroyed during re-encoding
   - Solution: Use lossless codecs (FFV1, HuffYUV) or embed in I-frames only

2. File Size:
   - Videos are large (1 GB+), processing is slow
   - Solution: Process specific frames, not entire video

3. Synchronization:
   - Decoder needs to know which frames contain data
   - Solution: Embed frame indices in first frame metadata

4. Capacity:
   - 1080p, 30fps, 10 seconds = 300 frames × ~1 MB = 300 MB capacity!
   - Solution: Use dynamic allocation (embed until message complete)
```

**Production Implementation Outline:**

```python
class VideoStego:
    def __init__(self, codec='lossless'):
        self.codec = codec
    
    def encode(self, video_path, message, password=None):
        # 1. Extract frames
        frames = self.extract_frames(video_path)
        
        # 2. Encrypt message
        if password:
            message = AESCrypto.encrypt(message, password)
        
        # 3. Calculate required frames
        required_frames = self.calculate_frame_count(message, frames[0])
        
        # 4. Embed in selected frames (e.g., every 10th frame)
        for i in range(required_frames):
            frame_idx = i * 10
            chunk = message[i * CHUNK_SIZE : (i+1) * CHUNK_SIZE]
            frames[frame_idx] = LSBEncoder.encode_frame(frames[frame_idx], chunk)
        
        # 5. Reconstruct video
        return self.frames_to_video(frames)
    
    def decode(self, video_path, password=None):
        # 1. Extract frames
        frames = self.extract_frames(video_path)
        
        # 2. Decode from frames (every 10th)
        message_chunks = []
        for i in range(0, len(frames), 10):
            chunk = LSBDecoder.decode_frame(frames[i])
            if chunk:  # Check for delimiter
                message_chunks.append(chunk)
            else:
                break  # No more data
        
        # 3. Combine and decrypt
        message = ''.join(message_chunks)
        if password:
            message = AESCrypto.decrypt(message, password)
        
        return message
```

**Interview Insight:**
> "Video steganography extends the concept to temporal domain. The key insight is exploiting video-specific properties: temporal redundancy (frame similarity), motion masking (hiding in action), and massive capacity (hundreds of frames). The main challenge is compression—most video codecs destroy LSB data, so we'd need lossless encoding or strategic I-frame placement. It's a natural extension of the image steganography foundation I built here."

---

## Attack Vectors & Mitigations

### Q13: How would an attacker detect steganography in your images? Explain steganalysis techniques.

**Answer:**

**Steganalysis = Science of Detecting Hidden Data**

**1. Visual Inspection (Primitive)**

```
Human eye cannot detect LSB changes:
  Original: RGB(150, 200, 100)
  Modified: RGB(151, 201, 100)
  Difference: Imperceptible

BUT: Statistical tools can detect patterns
```

**2. Chi-Square Attack (Statistical)**

**Theory:**
LSB replacement causes predictable patterns in pixel value distribution.

```python
# Steganalysis code (attacker's perspective)
import numpy as np
from scipy import stats

def chi_square_attack(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Extract LSBs
    lsb_r = pixels[:,:,0] & 1
    lsb_g = pixels[:,:,1] & 1
    lsb_b = pixels[:,:,2] & 1
    
    # Count 0s and 1s
    zeros_r = np.sum(lsb_r == 0)
    ones_r = np.sum(lsb_r == 1)
    
    # Expected: ~50% 0s, ~50% 1s (natural randomness)
    expected = len(lsb_r.flatten()) / 2
    
    # Chi-square statistic
    chi2 = ((zeros_r - expected)**2 / expected) + ((ones_r - expected)**2 / expected)
    
    # p-value: probability distribution is natural
    p_value = 1 - stats.chi2.cdf(chi2, df=1)
    
    if p_value < 0.05:
        print("STEGO DETECTED! LSB distribution is non-random")
    else:
        print("Image appears clean")

# Example results:
# Clean image: p = 0.73 (random)
# Stego image (50% capacity): p = 0.002 (non-random, DETECTED)
```

**Why This Works:**

```
Natural image LSBs: "0100110101011..." (pseudo-random, entropy ≈ 1.0)
Message LSBs:       "0100100001100101" (ASCII, entropy ≈ 0.7-0.9)

After embedding message:
Region with message: entropy drops
Region without message: entropy normal

Chi-square detects entropy difference
```

**3. Sample Pair Analysis (SPA)**

**More Advanced:**
Analyzes pixel pairs to detect LSB flipping patterns.

```python
def sample_pair_analysis(image):
    """
    Detects LSB embedding by analyzing adjacent pixel correlations
    """
    pixels = np.array(image).flatten()
    
    # Group pixels into pairs
    pairs = pixels.reshape(-1, 2)
    
    # Count pairs where:
    # - Both even: (150, 200)
    # - Both odd:  (151, 201)
    # - Mixed:     (150, 201)
    
    even_even = np.sum((pairs[:, 0] % 2 == 0) & (pairs[:, 1] % 2 == 0))
    odd_odd = np.sum((pairs[:, 0] % 2 == 1) & (pairs[:, 1] % 2 == 1))
    mixed = len(pairs) - even_even - odd_odd
    
    # In natural images: specific ratio exists
    # In stego images: ratio is disrupted
    
    ratio = (even_even + odd_odd) / len(pairs)
    
    if ratio < 0.45 or ratio > 0.55:  # Threshold
        return "STEGO DETECTED"
    return "Clean"
```

**4. RS (Regular-Singular) Analysis**

**Principle:**
Flips LSBs and measures "smoothness" change. Stego images show different behavior than natural images.

```python
def rs_analysis(image):
    """
    Divides image into blocks, flips LSBs, measures smoothness
    """
    def smoothness(block):
        # Sum of absolute differences between adjacent pixels
        return np.sum(np.abs(np.diff(block)))
    
    blocks = divide_into_blocks(image)
    
    regular_blocks = 0
    singular_blocks = 0
    
    for block in blocks:
        original_smoothness = smoothness(block)
        flipped_block = flip_lsbs(block)
        flipped_smoothness = smoothness(flipped_block)
        
        if flipped_smoothness > original_smoothness:
            regular_blocks += 1
        else:
            singular_blocks += 1
    
    # In natural images: R ≈ S
    # In stego images: R ≠ S (ratio deviates)
    
    ratio = regular_blocks / singular_blocks
    if abs(ratio - 1.0) > 0.2:
        return "STEGO DETECTED"
    return "Clean"
```

**5. Machine Learning Detectors (Modern)**

```python
from sklearn.ensemble import RandomForestClassifier

# Train on features:
features = [
    'lsb_entropy',          # Randomness of LSBs
    'chi_square_score',     # Statistical deviation
    'pixel_correlation',    # Adjacent pixel relationships
    'dct_coefficient_diff', # Frequency domain analysis
    'histogram_shape',      # Value distribution
]

# Dataset: 10,000 clean images + 10,000 stego images
X_train = extract_features(images)
y_train = labels  # 0 = clean, 1 = stego

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Detection accuracy: ~95% for LSB steganography
```

**Mitigations (Defense Against Steganalysis):**

**1. LSB Matching (Instead of Replacement)**

```python
# Current (LSB Replacement):
pixel_value = 150  # LSB = 0
target_bit = 1
pixel_value = 151  # Force LSB to 1

# Better (LSB Matching):
pixel_value = 150  # LSB = 0
target_bit = 1
if random() < 0.5:
    pixel_value += 1  # 151 (LSB = 1)
else:
    pixel_value -= 1  # 149 (LSB = 1)

# Advantage: ±1 changes appear more natural
# Chi-square resistance: Higher (but not immune)
```

**2. Adaptive Embedding (Embed in Complex Regions)**

```python
def adaptive_embedding(image, message):
    # Detect edge regions (high variance)
    edges = cv2.Canny(image, 100, 200)
    
    # Embed ONLY in edge pixels (avoid smooth areas like sky)
    embed_locations = np.where(edges > 0)
    
    # Edge regions have higher natural entropy
    # Message bits blend better
```

**3. Wet Paper Codes (Advanced)**

```python
# Problem: Some pixels MUST NOT be modified (e.g., signature verification)
# Solution: Error-correcting codes that embed message using only "safe" pixels

def wet_paper_embedding(image, message, safe_pixels_mask):
    """
    Embed message while avoiding certain pixels
    Uses syndrome coding (advanced)
    """
    # Map message to syndrome
    # Embed syndrome in available pixels
    # Decoder can recover message despite missing pixels
```

**4. Model-Based Steganography (Adversarial)**

```python
# Train GAN to generate stego images indistinguishable from natural images
# Attacker's ML detector fails because distribution matches natural images
# Cutting-edge research (not practical yet)
```

**Interview Summary Statement:**
> "My current implementation uses basic LSB, which is detectable by chi-square and SPA attacks at high embedding rates. For production, I'd implement LSB matching and adaptive embedding (edge-based) to resist statistical analysis. The detection rate depends on embedding density—at <10% capacity usage, even basic LSB is hard to detect. The encryption layer adds another barrier: even if steganography is detected, the encrypted message remains secure."

---

### Q14: Explain a MITM (Man-in-the-Middle) attack scenario. How would you detect/prevent it?

**Answer:**

**Attack Scenario:**

```
Alice                    Mallory (Attacker)              Bob
  |                            |                          |
  |  Send stego image ───────▶ |                          |
  |                            |  Intercept, analyze      |
  |                            |  Replace with own stego  |
  |                            | ─────────────────────▶   |
  |                            |                          |
```

**Attack Step-by-Step:**

```python
# 1. Alice encodes message
alice_message = "Transfer $10,000 to Account XYZ"
alice_stego_image = encode(image, alice_message, password="secret123")

# 2. Mallory intercepts transmission
intercepted_image = capture_network_traffic()

# 3. Mallory attempts to decode (without password, fails)
decoded = decode(intercepted_image, password=None)
# Result: Garbled AES ciphertext

# 4. Mallory's strategies:
#    a) Brute-force password (years with PBKDF2)
#    b) Replace entire image with own stego
#    c) Corrupt stego data to prevent decoding

# 5. Mallory sends modified image to Bob
bob_receives = mallory_modified_image

# 6. Bob decodes and acts on Mallory's message (ATTACK SUCCEEDS)
```

**Vulnerability in Current Implementation:**

```python
# ❌ No authentication: Bob can't verify message came from Alice
# ❌ No integrity check: Bob can't detect tampering
# ❌ No non-repudiation: Alice can deny sending the message
```

**Defense 1: HMAC (Message Authentication Code)**

**Implementation:**

```python
import hmac
import hashlib

def encode_with_hmac(image_path, message, password):
    # 1. Encrypt message
    encrypted = AESCrypto.encrypt(message, password)
    
    # 2. Generate HMAC
    hmac_key = derive_hmac_key(password)  # Separate key derivation
    hmac_tag = hmac.new(
        key=hmac_key,
        msg=encrypted.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()  # 64-character hex string
    
    # 3. Embed: message + HMAC
    payload = encrypted + "||" + hmac_tag
    
    # 4. Embed in image
    return LSBEncoder.encode(image_path, payload)

def decode_with_hmac(image_path, password):
    # 1. Extract payload
    payload = LSBDecoder.decode(image_path)
    encrypted, received_hmac = payload.split("||")
    
    # 2. Recompute HMAC
    hmac_key = derive_hmac_key(password)
    computed_hmac = hmac.new(
        key=hmac_key,
        msg=encrypted.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    # 3. Verify HMAC
    if not hmac.compare_digest(received_hmac, computed_hmac):
        raise ValueError("AUTHENTICATION FAILED! Message tampered or wrong password")
    
    # 4. Decrypt (only if HMAC valid)
    return AESCrypto.decrypt(encrypted, password)

# How this prevents MITM:
# - Mallory modifies encrypted message
# - HMAC verification fails (computed ≠ received)
# - Bob rejects message 🛡️
```

**Defense 2: Digital Signatures (Non-Repudiation)**

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Alice's keypair (generated once)
alice_private_key = RSA.generate(2048)
alice_public_key = alice_private_key.publickey()

def encode_with_signature(image_path, message, alice_private_key):
    # 1. Hash message
    message_hash = SHA256.new(message.encode())
    
    # 2. Sign hash with Alice's private key
    signature = pkcs1_15.new(alice_private_key).sign(message_hash)
    
    # 3. Embed message + signature
    payload = message + "||" + base64.b64encode(signature).decode()
    
    return LSBEncoder.encode(image_path, payload)

def decode_with_signature(image_path, alice_public_key):
    # 1. Extract payload
    payload = LSBDecoder.decode(image_path)
    message, signature_b64 = payload.split("||")
    signature = base64.b64decode(signature_b64)
    
    # 2. Hash message
    message_hash = SHA256.new(message.encode())
    
    # 3. Verify signature with Alice's public key
    try:
        pkcs1_15.new(alice_public_key).verify(message_hash, signature)
        print("✅ Signature valid! Message DEFINITELY from Alice")
    except (ValueError, TypeError):
        raise ValueError("❌ SIGNATURE INVALID! Message forged or tampered!")
    
    return message

# How this prevents MITM:
# - Mallory can't forge Alice's signature (needs private key)
# - Bob verifies signature with Alice's public key
# - Ensures authenticity (from Alice) + integrity (not modified)
```

**Defense 3: Steganographic Key (Shared Secret Pattern)**

```python
def encode_with_pattern_key(image_path, message, password, pattern_seed):
    """
    Embed message in pseudo-random pixel locations
    Only parties with pattern_seed can extract
    """
    import random
    
    # 1. Generate pseudo-random pixel sequence
    random.seed(pattern_seed)  # Shared secret
    total_pixels = img.width * img.height
    pixel_sequence = random.sample(range(total_pixels), len(message) * 8)
    
    # 2. Embed bits ONLY in these pixels
    for bit_index, pixel_index in enumerate(pixel_sequence):
        # Modify LSB of pixel at pixel_index
        pass
    
    # 3. Attacker without pattern_seed extracts wrong pixels → garbage

# How this prevents MITM:
# - Mallory can't decode without pattern_seed
# - Even if she replaces image, Bob extracts from different pixels
# - Decoding yields gibberish (pattern mismatch)
```

**Defense 4: Timestamp + Nonce (Replay Attack Prevention)**

```python
import time

def encode_with_timestamp(image_path, message, password):
    # 1. Add timestamp and nonce
    timestamp = int(time.time())
    nonce = os.urandom(16).hex()
    
    payload = f"{timestamp}||{nonce}||{message}"
    
    # 2. Encrypt payload
    encrypted = AESCrypto.encrypt(payload, password)
    
    return LSBEncoder.encode(image_path, encrypted)

def decode_with_timestamp(image_path, password, max_age=3600):
    # 1. Decrypt
    payload = LSBDecoder.decode(image_path)
    decrypted = AESCrypto.decrypt(payload, password)
    
    # 2. Parse timestamp
    timestamp, nonce, message = decrypted.split("||")
    timestamp = int(timestamp)
    
    # 3. Check freshness
    current_time = int(time.time())
    if current_time - timestamp > max_age:
        raise ValueError("MESSAGE TOO OLD! Possible replay attack")
    
    # 4. Check nonce (store used nonces to prevent replay)
    if nonce in used_nonces_db:
        raise ValueError("NONCE REUSED! Replay attack detected")
    
    used_nonces_db.add(nonce)
    return message

# How this prevents replay:
# - Mallory captures old stego image
# - Replays to Bob days later
# - Timestamp check fails (message expired)
```

**Complete Secure Protocol:**

```python
class SecureStegoProtocol:
    def encode(self, image_path, message, password, sender_private_key, pattern_seed):
        # 1. Add timestamp + nonce
        timestamp = int(time.time())
        nonce = os.urandom(16).hex()
        
        # 2. Sign message (authenticity)
        message_hash = SHA256.new(message.encode())
        signature = pkcs1_15.new(sender_private_key).sign(message_hash)
        
        # 3. Build payload
        payload = f"{timestamp}||{nonce}||{message}||{signature.hex()}"
        
        # 4. Encrypt (confidentiality)
        encrypted = AESCrypto.encrypt(payload, password)
        
        # 5. Generate HMAC (integrity)
        hmac_tag = hmac.new(password.encode(), encrypted.encode(), hashlib.sha256).hexdigest()
        
        # 6. Final payload
        final_payload = f"{encrypted}||{hmac_tag}"
        
        # 7. Embed using shared pattern (steganographic security)
        return self.embed_with_pattern(image_path, final_payload, pattern_seed)
    
    def decode(self, image_path, password, sender_public_key, pattern_seed, max_age=3600):
        # 1. Extract using shared pattern
        final_payload = self.extract_with_pattern(image_path, pattern_seed)
        
        # 2. Verify HMAC
        encrypted, received_hmac = final_payload.split("||")
        computed_hmac = hmac.new(password.encode(), encrypted.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(received_hmac, computed_hmac):
            raise ValueError("HMAC verification failed!")
        
        # 3. Decrypt
        payload = AESCrypto.decrypt(encrypted, password)
        
        # 4. Parse components
        timestamp, nonce, message, signature_hex = payload.split("||")
        signature = bytes.fromhex(signature_hex)
        
        # 5. Check timestamp
        if int(time.time()) - int(timestamp) > max_age:
            raise ValueError("Message expired!")
        
        # 6. Verify signature
        message_hash = SHA256.new(message.encode())
        pkcs1_15.new(sender_public_key).verify(message_hash, signature)
        
        # 7. Check nonce (replay protection)
        # ... nonce database check
        
        return message

# Security properties achieved:
# ✅ Confidentiality (AES-256)
# ✅ Integrity (HMAC)
# ✅ Authenticity (Digital signature)
# ✅ Non-repudiation (Signature proves sender)
# ✅ Replay protection (Timestamp + nonce)
# ✅ Steganographic security (Pattern-based embedding)
```

---

## Comparison & Alternatives

### Q15: Compare LSB with other steganography techniques (DCT, spread spectrum, etc.).

**Answer:**

**Comparison Table:**

| Technique | Embedding Domain | Capacity | Robustness | Detectability | Complexity |
|-----------|------------------|----------|------------|---------------|------------|
| **LSB** | Spatial (pixels) | High (3 bpp) | Low | Medium | Simple |
| **DCT** | Frequency | Medium (0.5 bpp) | High | Low | Medium |
| **DWT** | Wavelet | Medium (1 bpp) | Very High | Low | High |
| **Spread Spectrum** | Spatial | Low (0.1 bpp) | Very High | Very Low | High |

**1. DCT (Discrete Cosine Transform) - JPEG Domain**

**How it works:**

```python
import cv2
import numpy as np

def dct_embed(image_path, message):
    """
    Embed in frequency domain coefficients
    Used in JPEG images (transforms to 8×8 blocks)
    """
    # 1. Load image and convert to YCrCb
    img = cv2.imread(image_path)
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y_channel = yuv[:, :, 0]
    
    # 2. Divide into 8×8 blocks
    blocks = divide_into_8x8_blocks(y_channel)
    
    # 3. Apply DCT to each block
    message_bits = text_to_binary(message)
    bit_index = 0
    
    for block in blocks:
        # DCT transform
        dct_block = cv2.dct(block.astype(np.float32))
        
        # Modify mid-frequency coefficients (avoid DC and high-freq)
        # Example: coefficients [2,2], [2,3], [3,2]
        if bit_index < len(message_bits):
            bit = int(message_bits[bit_index])
            
            # Quantize coefficient to embed bit
            coef = dct_block[2, 2]
            if bit == 0:
                dct_block[2, 2] = make_even(coef)
            else:
                dct_block[2, 2] = make_odd(coef)
            
            bit_index += 1
        
        # Inverse DCT
        block = cv2.idct(dct_block)
    
    # 4. Reconstruct image
    return reconstructed_image

def make_even(value):
    return value if int(value) % 2 == 0 else value + 1

def make_odd(value):
    return value if int(value) % 2 == 1 else value + 1
```

**Advantages over LSB:**
- ✅ **JPEG compatibility**: Survives JPEG compression (LSB destroyed)
- ✅ **Robust**: Resists cropping, rotation (frequency domain invariant)
- ✅ **Lower detection**: Modifying mid-frequencies less detectable

**Disadvantages:**
- ❌ **Lower capacity**: ~0.5 bits per block vs LSB's 3 bits per pixel
- ❌ **Complexity**: Requires DCT knowledge
- ❌ **Artifacts**: Visible blocking at high embedding rates

**Use case:** When image will be compressed or transmitted via lossy channels

---

**2. DWT (Discrete Wavelet Transform)**

**How it works:**

```python
import pywt

def dwt_embed(image_path, message):
    """
    Embed in wavelet coefficients
    Multi-resolution analysis (LL, LH, HL, HH subbands)
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 1. Decompose into wavelet subbands
    coeffs = pywt.dwt2(img, 'haar')
    cA, (cH, cV, cD) = coeffs
    # cA = low-frequency (approximation)
    # cH, cV, cD = high-frequency (details)
    
    # 2. Embed in high-frequency subbands (less perceptible)
    message_bits = text_to_binary(message)
    bit_index = 0
    
    for i in range(cH.shape[0]):
        for j in range(cH.shape[1]):
            if bit_index < len(message_bits):
                bit = int(message_bits[bit_index])
                
                # Modify coefficient
                if bit == 0:
                    cH[i, j] = make_even(cH[i, j])
                else:
                    cH[i, j] = make_odd(cH[i, j])
                
                bit_index += 1
    
    # 3. Reconstruct image
    coeffs_modified = (cA, (cH, cV, cD))
    reconstructed = pywt.idwt2(coeffs_modified, 'haar')
    
    return reconstructed
```

**Advantages:**
- ✅ **Excellent robustness**: Resists compression, noise, filtering
- ✅ **Multi-resolution**: Can embed at different scales
- ✅ **Imperceptible**: High-frequency changes invisible

**Disadvantages:**
- ❌ **Lower capacity**: ~1 bit per coefficient
- ❌ **Computational cost**: Wavelet transforms are expensive
- ❌ **Complexity**: Requires domain expertise

**Use case:** Medical image watermarking, copyright protection

---

**3. Spread Spectrum Steganography**

**How it works:**

```python
def spread_spectrum_embed(image_path, message, spreading_code):
    """
    Spread message bits across entire image using pseudo-random sequence
    Similar to CDMA in telecommunications
    """
    img = np.array(Image.open(image_path))
    
    # 1. Generate spreading sequence (chip sequence)
    np.random.seed(spreading_code)  # Shared secret
    spreading_sequence = np.random.choice([-1, 1], size=img.size)
    
    # 2. Convert message to bits
    message_bits = text_to_binary(message)
    
    # 3. Spread each bit across many pixels
    spreading_factor = 100  # Each bit spread across 100 pixels
    
    for bit_index, bit in enumerate(message_bits):
        bit_value = 1 if bit == '1' else -1
        
        # Get 100 random pixel locations
        start_idx = bit_index * spreading_factor
        end_idx = start_idx + spreading_factor
        
        pixel_indices = spreading_sequence[start_idx:end_idx]
        
        # Add small noise proportional to bit value
        for idx in pixel_indices:
            img.flat[idx] += bit_value * 0.1  # Tiny modification
    
    return img

def spread_spectrum_decode(image_path, spreading_code):
    """
    Correlate with spreading sequence to extract bits
    """
    img = np.array(Image.open(image_path))
    
    # Generate same spreading sequence
    np.random.seed(spreading_code)
    spreading_sequence = np.random.choice([-1, 1], size=img.size)
    
    # Correlate to detect bits
    spreading_factor = 100
    message_bits = []
    
    for bit_index in range(len(img.flat) // spreading_factor):
        start_idx = bit_index * spreading_factor
        end_idx = start_idx + spreading_factor
        
        # Correlation
        correlation = np.sum(img.flat[start_idx:end_idx] * spreading_sequence[start_idx:end_idx])
        
        # Determine bit based on correlation sign
        message_bits.append('1' if correlation > 0 else '0')
    
    return binary_to_text(''.join(message_bits))
```

**Advantages:**
- ✅ **Very low detectability**: Message spread across entire image
- ✅ **Robust**: Resists noise, compression, cropping
- ✅ **Security**: Requires spreading code to extract

**Disadvantages:**
- ❌ **Very low capacity**: 0.01-0.1 bits per pixel
- ❌ **Computational intensive**: Correlation operations
- ❌ **Complex math**: Requires signal processing knowledge

**Use case:** Military communications, covert channels

---

**4. PVD (Pixel Value Differencing)**

```python
def pvd_embed(image_path, message):
    """
    Embed based on difference between adjacent pixels
    Larger differences can hide more bits
    """
    img = np.array(Image.open(image_path).convert('L'))  # Grayscale
    
    message_bits = text_to_binary(message)
    bit_index = 0
    
    # Process pixel pairs
    for i in range(0, img.shape[0], 1):
        for j in range(0, img.shape[1]-1, 2):
            p1, p2 = img[i, j], img[i, j+1]
            diff = abs(p1 - p2)
            
            # Determine embedding capacity based on difference
            if diff < 8:
                capacity = 3  # Smooth region, embed 3 bits
            elif diff < 16:
                capacity = 4
            else:
                capacity = 5  # Edge region, embed 5 bits
            
            if bit_index + capacity <= len(message_bits):
                # Extract bits to embed
                bits_to_embed = message_bits[bit_index:bit_index+capacity]
                decimal_value = int(bits_to_embed, 2)
                
                # Adjust pixel values to encode decimal_value in difference
                new_diff = decimal_value
                img[i, j] = p1  # Keep p1
                img[i, j+1] = p1 + new_diff  # Adjust p2
                
                bit_index += capacity
    
    return img
```

**Advantages:**
- ✅ **Adaptive capacity**: More bits in complex regions
- ✅ **Better imperceptibility**: Exploits HVS (Human Visual System)
- ✅ **Higher capacity than DCT**: ~3-5 bits per pixel pair

**Disadvantages:**
- ❌ **Complex extraction**: Need to know partitioning
- ❌ **Not robust**: Small changes destroy message

---

**When to Use Each:**

```
LSB (Current implementation):
├─ Use case: Simple text messages, high capacity needed
├─ Pro: Easy to implement, high capacity
└─ Con: Not robust (compression destroys), detectable

DCT:
├─ Use case: JPEG images, need compression resistance
├─ Pro: JPEG-compatible, robust
└─ Con: Lower capacity, more complex

DWT:
├─ Use case: Copyright watermarking, medical images
├─ Pro: Extremely robust, multi-scale
└─ Con: Slowest, lowest capacity

Spread Spectrum:
├─ Use case: Covert military communication
├─ Pro: Nearly undetectable, very robust
└─ Con: Tiny capacity (impractical for normal use)

PVD:
├─ Use case: Adaptive embedding, balance capacity/quality
├─ Pro: Intelligent capacity allocation
└─ Con: Complex, not standardized
```

**Interview Recommendation:**
> "I chose LSB for this project because it provides the best capacity-to-complexity ratio for the MVP. For production, I'd implement a hybrid approach: LSB for spatial embedding, DCT for JPEG compatibility, and spread spectrum for high-security scenarios. The choice depends on requirements: if capacity is priority → LSB/PVD; if robustness is priority → DWT/DCT; if undetectability is priority → spread spectrum."

---

## Advanced Topics

### Q16: How would you implement plausible deniability? Explain multi-layer steganography.

**Answer:**

**Plausible Deniability = Ability to deny hidden message exists**

**Concept:**

```
Scenario:
└─ Government seizes your laptop
└─ Finds image files
└─ Runs steganalysis, detects hidden data
└─ Forces you to reveal password

With plausible deniability:
└─ You provide "decoy password"
└─ Decoy password decrypts to innocent message
└─ Real message remains hidden
└─ No proof of second layer
```

**Implementation: Two-Layer Steganography**

```python
class MultiLayerStego:
    """
    Layer 1 (Decoy): LSB embedding with weak password
    Layer 2 (Real): DCT embedding with strong password
    """
    
    def encode_two_layer(self, image_path, decoy_message, real_message, 
                         decoy_password, real_password):
        """
        Embed two independent messages in same image
        """
        # 1. Load image
        img = Image.open(image_path)
        
        # 2. Embed decoy message in LSB (easy to find)
        decoy_encrypted = AESCrypto.encrypt(decoy_message, decoy_password)
        stego_image_layer1 = LSBEncoder.encode(img, decoy_encrypted)
        
        # 3. Embed real message in DCT (harder to detect)
        real_encrypted = AESCrypto.encrypt(real_message, real_password)
        stego_image_layer2 = DCTEncoder.encode(stego_image_layer1, real_encrypted)
        
        return stego_image_layer2
    
    def decode_two_layer(self, image_path, password):
        """
        Decode returns different message based on password
        """
        # Try LSB decoding (decoy layer)
        try:
            lsb_message = LSBDecoder.decode(image_path)
            decoy_plaintext = AESCrypto.decrypt(lsb_message, password)
            # If successful, return decoy
            return {
                'layer': 'decoy',
                'message': decoy_plaintext
            }
        except:
            pass  # Wrong password or no LSB data
        
        # Try DCT decoding (real layer)
        try:
            dct_message = DCTDecoder.decode(image_path)
            real_plaintext = AESCrypto.decrypt(dct_message, password)
            return {
                'layer': 'real',
                'message': real_plaintext
            }
        except:
            raise ValueError("Invalid password")

# Usage:
encoder = MultiLayerStego()

# Encode two messages
stego_img = encoder.encode_two_layer(
    "original.png",
    decoy_message="Meeting at 3pm tomorrow",  # Innocent
    real_message="Classified intel: ...",     # Sensitive
    decoy_password="weak123",
    real_password="Str0ng!P@ssw0rd#2024"
)

# Decoding with decoy password:
result = encoder.decode_two_layer("stego.png", "weak123")
# Returns: "Meeting at 3pm tomorrow" (decoy)

# Decoding with real password:
result = encoder.decode_two_layer("stego.png", "Str0ng!P@ssw0rd#2024")
# Returns: "Classified intel: ..." (real)
```

**Advanced: Three-Layer with Honeypot**

```python
class ThreeLayerStego:
    """
    Layer 0: No password → clean image (nothing found)
    Layer 1: Decoy password → innocent message
    Layer 2: Real password → sensitive message
    Layer 3: Honeypot password → fake message that alerts you
    """
    
    def encode_three_layer(self, image_path, decoy_msg, real_msg, honeypot_msg,
                          decoy_pw, real_pw, honeypot_pw):
        img = Image.open(image_path)
        
        # Layer 1: LSB (decoy)
        decoy_enc = AESCrypto.encrypt(decoy_msg, decoy_pw)
        img = LSBEncoder.encode(img, decoy_enc)
        
        # Layer 2: DCT mid-frequency (real)
        real_enc = AESCrypto.encrypt(real_msg, real_pw)
        img = DCTEncoder.encode(img, real_enc, frequency='mid')
        
        # Layer 3: DCT low-frequency (honeypot)
        honeypot_enc = AESCrypto.encrypt(honeypot_msg, honeypot_pw)
        img = DCTEncoder.encode(img, honeypot_enc, frequency='low')
        
        return img
    
    def decode_three_layer(self, image_path, password):
        # Try each layer
        for layer_name, decoder in [('decoy', LSBDecoder),
                                     ('real', DCTDecoder),
                                     ('honeypot', DCTDecoderLow)]:
            try:
                encrypted = decoder.decode(image_path)
                plaintext = AESCrypto.decrypt(encrypted, password)
                
                # If honeypot triggered, send alert
                if layer_name == 'honeypot':
                    self.send_emergency_alert("Honeypot accessed!")
                
                return {'layer': layer_name, 'message': plaintext}
            except:
                continue
        
        raise ValueError("Invalid password or no data")
```

**Cryptographic Approach: Key Derivation Randomness**

```python
def plausible_deniability_via_key_derivation(image_path, message1, message2, password_base):
    """
    Use different key derivation paths to create multiple valid decryptions
    """
    # Derive two keys from same password base
    key1 = PBKDF2(password_base, salt="public_salt_1", iterations=100000)
    key2 = PBKDF2(password_base, salt="public_salt_2", iterations=100000)
    
    # Encrypt two messages with different keys
    cipher1 = AES.new(key1, AES.MODE_CBC, iv1)
    cipher2 = AES.new(key2, AES.MODE_CBC, iv2)
    
    encrypted1 = cipher1.encrypt(pad(message1))
    encrypted2 = cipher2.encrypt(pad(message2))
    
    # Embed both (different regions)
    # Decoder doesn't know which salt to use
    # User provides salt choice during decryption
```

**Steganographic File System (Advanced Concept)**

```python
class StegoFS:
    """
    Filesystem where files exist in multiple "universes"
    Depending on password, directory listing changes
    """
    
    def __init__(self, base_image):
        self.image = base_image
        self.universes = {
            'default': [],   # No password
            'decoy': [],     # Decoy password
            'real': []       # Real password
        }
    
    def add_file(self, filename, content, universe):
        """Add file to specific universe"""
        # Embed file in image region reserved for that universe
        offset = self.get_universe_offset(universe)
        self.embed_at_offset(content, offset)
        self.universes[universe].append(filename)
    
    def list_files(self, password):
        """List files visible in password's universe"""
        universe = self.password_to_universe(password)
        return self.universes[universe]
    
    def read_file(self, filename, password):
        """Read file from password's universe"""
        universe = self.password_to_universe(password)
        if filename not in self.universes[universe]:
            raise FileNotFoundError
        
        offset = self.get_file_offset(filename, universe)
        return self.extract_from_offset(offset)

# Example:
fs = StegoFS("container.png")

# Populate universes
fs.add_file("taxes.pdf", tax_data, universe='default')     # Normal files
fs.add_file("vacation.jpg", vacation, universe='decoy')    # Decoy files
fs.add_file("secrets.txt", secrets, universe='real')       # Real files

# Access with different passwords:
fs.list_files(password=None)          # ['taxes.pdf']
fs.list_files("weak123")              # ['taxes.pdf', 'vacation.jpg']
fs.list_files("Str0ng!Pass")          # ['taxes.pdf', 'vacation.jpg', 'secrets.txt']
```

**Real-World Example: TrueCrypt Hidden Volumes**

```
TrueCrypt Encrypted Container:
├─ Outer Volume (Decoy)
│   ├─ Password: "decoy123"
│   └─ Contains: Innocent files
│
└─ Hidden Volume (Real)
    ├─ Password: "real_password_xyz"
    ├─ Contains: Sensitive files
    └─ Indistinguishable from random data

Key property:
- Hidden volume exists in "free space" of outer volume
- Looks like random padding bytes
- No proof hidden volume exists
- User can plausibly deny by providing only outer password
```

**Implementation Challenges:**

```python
# Challenge 1: Space Management
# - Outer volume might overwrite hidden volume
# - Solution: Steganographic filesystem tracks used regions

# Challenge 2: Statistical Fingerprinting
# - Multiple encryption layers have patterns
# - Solution: Use different algorithms (AES + ChaCha20)

# Challenge 3: Coercion Resistance
# - Attacker forces you to reveal all passwords
# - Solution: Duress password (triggers data wipe or alerts)

def create_duress_password(real_password):
    """
    Duress password looks valid but triggers security actions
    """
    duress = real_password + "_DURESS"
    
    if user_enters_password(duress):
        wipe_sensitive_data()
        send_emergency_alert()
        return_decoy_data()  # Appear normal
```

**Interview Summary:**
> "Plausible deniability is achieved through multi-layer steganography where different passwords reveal different messages. The key insight is that upper layers (decoy) are easily detectable, while deeper layers (real) use more sophisticated techniques. The coercer finds the decoy, is satisfied, and stops investigating. Cryptographically, this relies on the inability to distinguish encrypted data from random noise. I'd implement this using LSB for decoy (easy to find) and DCT or spread spectrum for the real message (hidden in frequency domain), with different PBKDF2 salts for each layer."

---

### Q17: Explain zero-knowledge proofs in the context of steganography. How could you prove a message is hidden without revealing it?

**Answer:**

**Zero-Knowledge Proof (ZKP) Concept:**

```
Prover (Alice): "I know the password to this stego image"
Verifier (Bob): "Prove it without telling me the password"

ZKP Properties:
1. Completeness: If Alice knows password, she can convince Bob
2. Soundness: If Alice doesn't know password, she can't convince Bob
3. Zero-Knowledge: Bob learns NOTHING except that Alice knows password
```

**Naive Approach (NOT Zero-Knowledge):**

```python
# Alice sends Bob the password
alice_password = "secret123"
bob_verifies = decode(stego_image, alice_password)

# Problem: Bob now knows the password (not zero-knowledge)
```

**ZKP Protocol for Steganography:**

**Protocol 1: Challenge-Response**

```python
class StegoZKP:
    """
    Zero-knowledge proof that message is hidden in image
    """
    
    def prove_knowledge(self, stego_image, password, verifier_challenge):
        """
        Prover (Alice) proves she knows password without revealing it
        """
        # 1. Decode message with password
        hidden_message = LSBDecoder.decode(stego_image)
        decrypted = AESCrypto.decrypt(hidden_message, password)
        
        # 2. Compute hash of message
        message_hash = hashlib.sha256(decrypted.encode()).hexdigest()
        
        # 3. Verifier sends random challenge (nonce)
        challenge = verifier_challenge  # Random 256-bit number
        
        # 4. Prover computes response: H(message || challenge)
        response = hashlib.sha256((decrypted + str(challenge)).encode()).hexdigest()
        
        # 5. Send response to verifier (NOT the message or password)
        return response
    
    def verify_knowledge(self, stego_image, expected_message_hash, challenge, response):
        """
        Verifier (Bob) checks if prover knows password
        """
        # Bob doesn't know the message or password
        # But he knows the expected message hash (from prior agreement)
        
        # Verification: Bob cannot reconstruct message from response
        # But if Alice knows message, response will be consistent
        
        # This requires multiple rounds to achieve statistical certainty
        return True  # Simplified

# Problem with above: Verifier needs to know message hash (not always feasible)
```

**Protocol 2: Commitment Scheme**

```python
class CommitmentZKP:
    """
    Prover commits to message without revealing it
    """
    
    def commit_to_message(self, stego_image, password):
        """
        Alice creates commitment to hidden message
        """
        # 1. Decode message
        hidden_message = LSBDecoder.decode(stego_image)
        decrypted = AESCrypto.decrypt(hidden_message, password)
        
        # 2. Generate random nonce
        nonce = os.urandom(32)
        
        # 3. Compute commitment: H(message || nonce)
        commitment = hashlib.sha256((decrypted.encode() + nonce)).hexdigest()
        
        # 4. Send commitment to Bob (hides message)
        return {
            'commitment': commitment,
            'nonce': nonce  # Kept secret for now
        }
    
    def challenge(self, commitment):
        """
        Bob sends challenge
        """
        challenge_bit = random.randint(0, 1)  # Random bit
        return challenge_bit
    
    def respond(self, challenge_bit, message, nonce):
        """
        Alice responds to challenge
        """
        if challenge_bit == 0:
            # Reveal nonce (allows Bob to verify commitment)
            return {'nonce': nonce}
        else:
            # Reveal message (allows Bob to check it was embedded)
            return {'message': message}
    
    def verify(self, commitment, response, challenge_bit):
        """
        Bob verifies Alice's response
        """
        if challenge_bit == 0:
            # Check: H(message || nonce) == commitment
            # But wait, Bob doesn't know message yet...
            # This protocol needs refinement
            pass
        else:
            # Check message was actually in image
            pass

# This approach has issues too... Let's use a better one
```

**Protocol 3: Fiat-Shamir Heuristic (Practical ZKP)**

```python
class FiatShamirStegoZKP:
    """
    Non-interactive zero-knowledge proof for steganography
    """
    
    def generate_proof(self, stego_image, password):
        """
        Prover generates proof without interaction
        """
        # 1. Decode message
        hidden_message = LSBDecoder.decode(stego_image)
        decrypted = AESCrypto.decrypt(hidden_message, password)
        
        # 2. Choose random secret r
        r = os.urandom(32)
        
        # 3. Compute commitment: C = H(r)
        commitment = hashlib.sha256(r).hexdigest()
        
        # 4. Compute challenge (deterministic, based on public info)
        challenge = hashlib.sha256(
            (commitment + stego_image_hash).encode()
        ).hexdigest()
        
        # 5. Compute response: z = r + H(message) * challenge (simplified)
        message_hash = hashlib.sha256(decrypted.encode()).digest()
        z = int.from_bytes(r, 'big') + int.from_bytes(message_hash, 'big') * int(challenge, 16)
        
        # 6. Proof = (commitment, z)
        return {
            'commitment': commitment,
            'z': z,
            'message_hash': message_hash.hex()  # Public
        }
    
    def verify_proof(self, stego_image, proof):
        """
        Verifier checks proof without learning message
        """
        commitment = proof['commitment']
        z = proof['z']
        message_hash = bytes.fromhex(proof['message_hash'])
        
        # 1. Recompute challenge
        stego_image_hash = hashlib.sha256(stego_image.tobytes()).hexdigest()
        challenge = hashlib.sha256(
            (commitment + stego_image_hash).encode()
        ).hexdigest()
        
        # 2. Verify: H(z - message_hash * challenge) == commitment
        expected_r = z - int.from_bytes(message_hash, 'big') * int(challenge, 16)
        expected_commitment = hashlib.sha256(
            expected_r.to_bytes(32, 'big')
        ).hexdigest()
        
        # 3. Check
        if expected_commitment == commitment:
            print("✅ PROOF VALID: Message exists in image")
            return True
        else:
            print("❌ PROOF INVALID: No message or wrong password")
            return False

# Usage:
zkp = FiatShamirStegoZKP()

# Alice generates proof
proof = zkp.generate_proof(stego_image, "my_password")

# Alice sends proof to Bob (NOT the password or message)
# Bob verifies
is_valid = zkp.verify_proof(stego_image, proof)

# Bob learns: Alice knows a message hidden in the image
# Bob does NOT learn: The message content or the password
```

**Practical Application: Verifiable Steganography**

```python
class VerifiableSteganography:
    """
    Embed message + ZKP proof in image
    Third party can verify message exists without decrypting
    """
    
    def encode_with_proof(self, image_path, message, password):
        # 1. Encrypt message
        encrypted = AESCrypto.encrypt(message, password)
        
        # 2. Generate ZKP proof
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        proof = self.generate_zkp(message_hash)
        
        # 3. Embed: encrypted_message || proof
        payload = encrypted + "||ZKP||" + json.dumps(proof)
        
        # 4. Embed in image
        return LSBEncoder.encode(image_path, payload)
    
    def verify_without_decrypting(self, stego_image):
        """
        Verify message exists WITHOUT knowing password
        """
        # 1. Extract payload
        payload = LSBDecoder.decode(stego_image)
        
        # 2. Split encrypted message and proof
        parts = payload.split("||ZKP||")
        encrypted_message = parts[0]
        proof = json.loads(parts[1])
        
        # 3. Verify ZKP
        is_valid = self.verify_zkp(proof, encrypted_message)
        
        if is_valid:
            print("✅ Verified: A message is hidden (but content unknown)")
        else:
            print("❌ Invalid: No message or corrupted data")
        
        return is_valid

# Use case:
# - Journalist receives stego image from source
# - Can verify message exists (proves source sent it)
# - Cannot decrypt without password (protects source)
# - Later, source reveals password to decrypt
```

**Advanced: ZK-SNARKs for Steganography**

```python
# Theoretical (not practical yet due to complexity):

class ZKSNARKStego:
    """
    Zero-Knowledge Succinct Non-Interactive Argument of Knowledge
    Proves complex statements about hidden message
    """
    
    def prove_message_property(self, stego_image, password, property_predicate):
        """
        Prove message satisfies property without revealing message
        
        Example properties:
        - Message contains word "classified"
        - Message is a valid JSON
        - Message author is Alice (via digital signature)
        - Message length > 100 characters
        """
        # 1. Decode message
        message = decode_and_decrypt(stego_image, password)
        
        # 2. Evaluate predicate
        satisfies = property_predicate(message)  # True/False
        
        # 3. Generate ZK-SNARK proof (mathematical magic)
        proof = zksnark.prove(
            statement="message satisfies predicate",
            witness=message,
            predicate=property_predicate
        )
        
        return proof
    
    def verify_property(self, stego_image, proof, property_predicate):
        """
        Verify proof without learning message
        """
        is_valid = zksnark.verify(proof, property_predicate)
        return is_valid

# Example:
predicate = lambda msg: "classified" in msg.lower()

# Alice proves message contains "classified"
proof = zksnark_stego.prove_message_property(stego_image, password, predicate)

# Bob verifies (learns message contains "classified" but not the full message)
zksnark_stego.verify_property(stego_image, proof, predicate)
# Returns: True (message contains "classified")
```

**Real-World Use Case: Whistleblowing**

```
Scenario:
└─ Whistleblower embeds leaked docs in image
└─ Sends image to journalist
└─ Journalist needs to verify:
    ├─ Message exists (not a hoax)
    ├─ Message is from legitimate source (signed)
    └─ Message mentions specific topic (e.g., "corruption")

ZKP Solution:
└─ Whistleblower generates proof:
    ├─ Proves message is digitally signed by them
    ├─ Proves message contains keyword "corruption"
    ├─ Does NOT reveal full message content
└─ Journalist verifies proof
└─ Journalist decides to publish (confirmed authenticity)
└─ Later, whistleblower reveals password (full disclosure)
```

**Interview Takeaway:**
> "Zero-knowledge proofs in steganography enable verification of message existence or properties without revealing content. This is crucial for scenarios requiring plausible deniability or multi-party trust. While ZK-SNARKs are theoretically powerful, practical implementations use commitment schemes and Fiat-Shamir heuristics. The key insight is separating 'proof of knowledge' from 'disclosure of knowledge'—you can prove you know something without revealing what you know."

---

## Conclusion

This interview guide covers the complete spectrum of StegoCrypt: from fundamental concepts (LSB, AES-256) to advanced topics (ZKP, multi-layer stego). The depth demonstrates not just implementation skills, but deep understanding of cryptographic principles, security trade-offs, and attack-defense dynamics.

**Key Interview Strategies:**

1. **Start Simple, Go Deep**: Begin with LSB explanation, then discuss DCT/DWT alternatives
2. **Show Trade-off Analysis**: Every choice (AES-256 vs ChaCha20, LSB vs DCT) has pros/cons
3. **Demonstrate Security Thinking**: Always mention attack vectors when explaining defenses
4. **Cite Standards**: NIST SP 800-132, OWASP, academic papers lend credibility
5. **Practical Examples**: Real-world scenarios (whistleblowing, military comms) show applied knowledge

**Preparation Checklist:**

- ✅ Can explain LSB algorithm with binary examples
- ✅ Can derive AES key from password (PBKDF2 steps)
- ✅ Can compare steganography techniques (table format)
- ✅ Can describe at least 3 steganalysis attacks
- ✅ Can discuss mitigations for each vulnerability
- ✅ Can explain ZKP conceptually (Fiat-Shamir)
- ✅ Can discuss performance optimizations (NumPy, multiprocessing)

---

**Good luck with your interviews! 🚀**
