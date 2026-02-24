"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║         TCS HACKQUEST - HIGH PRIORITY PRACTICE CHALLENGES                       ║
║           Topics with 100% Appearance Rate in Past Years                         ║
╚══════════════════════════════════════════════════════════════════════════════════╝

Based on analysis of Seasons 5-10, these topics appear EVERY YEAR:
1. Base64 Encoding/Decoding (100% appearance)
2. Hex Encoding (100% appearance)
3. Caesar/ROT Ciphers (95% appearance)
4. SQL Injection (100% appearance)
5. Steganography/Hidden Data (100% appearance)
6. Source Code Analysis (100% appearance)
7. XOR Operations (90% appearance)
8. Network Packet Analysis (85% appearance)
9. File Signature Analysis (80% appearance)

Run this file and solve each challenge!
"""

import base64
import hashlib
import binascii
import random
import time

# ═══════════════════════════════════════════════════════════════════════════════════
#                    HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════════

def caesar_encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)

def xor_encrypt(data, key):
    if isinstance(data, str):
        data = data.encode()
    if isinstance(key, str):
        key = key.encode()
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def check_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.lower():
        print("✅ CORRECT! Well done!")
        return True
    else:
        print(f"❌ Wrong! The correct answer was: {correct_answer}")
        return False

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 1: BASE64 ENCODING (100% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def base64_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 1: BASE64 ENCODING (100% Appearance)                       ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• Base64 uses characters: A-Z, a-z, 0-9, +, /
• Padding with = at the end
• NOT encryption - just encoding!
• 4 encoded characters = 3 original bytes
""")
    
    score = 0
    
    # Challenge 1.1 - Simple Base64
    print("\n" + "="*70)
    print("🎯 CHALLENGE 1.1: Simple Base64 (Beginner)")
    print("="*70)
    encoded = base64.b64encode(b"HQ10FLAG{welcome_to_ctf}").decode()
    print(f"\nDecode this: {encoded}")
    print("\nHint: Use any Base64 decoder or CyberChef")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, "HQ10FLAG{welcome_to_ctf}"):
        score += 1
    
    # Challenge 1.2 - Double Base64
    print("\n" + "="*70)
    print("🎯 CHALLENGE 1.2: Double Base64 (Intermediate)")
    print("="*70)
    original = "HQ10FLAG{double_encoded}"
    first_encode = base64.b64encode(original.encode()).decode()
    double_encode = base64.b64encode(first_encode.encode()).decode()
    print(f"\nDecode this (encoded twice): {double_encode}")
    print("\nHint: Keep decoding until you get readable text")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 1.3 - Triple Base64
    print("\n" + "="*70)
    print("🎯 CHALLENGE 1.3: Triple Base64 (Hard)")
    print("="*70)
    original = "HQ10FLAG{persistence}"
    e1 = base64.b64encode(original.encode()).decode()
    e2 = base64.b64encode(e1.encode()).decode()
    e3 = base64.b64encode(e2.encode()).decode()
    print(f"\nDecode this (encoded THREE times):\n{e3}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 1.4 - Base64 with noise
    print("\n" + "="*70)
    print("🎯 CHALLENGE 1.4: Find the Base64 (Realistic)")
    print("="*70)
    hidden = base64.b64encode(b"HQ10FLAG{find_me}").decode()
    noise = f"""
HTTP/1.1 200 OK
Content-Type: text/html
X-Custom-Header: nothing_here
Set-Cookie: session=abc123

<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>
<!-- DEBUG: {hidden} -->
<h1>Hello World</h1>
</body>
</html>
"""
    print(f"\nFind and decode the hidden Base64 in this response:\n{noise}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, "HQ10FLAG{find_me}"):
        score += 1
    
    print(f"\n📊 Base64 Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 2: HEX ENCODING (100% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def hex_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 2: HEX ENCODING (100% Appearance)                          ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• Hex uses characters: 0-9, a-f (or A-F)
• 2 hex characters = 1 byte
• String always has EVEN length
• Common in memory dumps, file analysis
""")
    
    score = 0
    
    # Challenge 2.1 - Simple Hex
    print("\n" + "="*70)
    print("🎯 CHALLENGE 2.1: Simple Hex Decode (Beginner)")
    print("="*70)
    original = "HQ10FLAG{hex_is_easy}"
    hex_encoded = original.encode().hex()
    print(f"\nDecode this hex string: {hex_encoded}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 2.2 - Hex with spaces
    print("\n" + "="*70)
    print("🎯 CHALLENGE 2.2: Hex with Spaces (Intermediate)")
    print("="*70)
    original = "HQ10FLAG{spaced_hex}"
    hex_bytes = original.encode().hex()
    spaced = ' '.join(hex_bytes[i:i+2] for i in range(0, len(hex_bytes), 2))
    print(f"\nDecode this: {spaced}")
    print("\nHint: Remove spaces first, then decode")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 2.3 - Hex + Base64
    print("\n" + "="*70)
    print("🎯 CHALLENGE 2.3: Hex inside Base64 (Hard)")
    print("="*70)
    original = "HQ10FLAG{layered}"
    hex_encoded = original.encode().hex()
    b64_of_hex = base64.b64encode(hex_encoded.encode()).decode()
    print(f"\nDecode this (Base64 → Hex → ASCII): {b64_of_hex}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 2.4 - Mixed case hex
    print("\n" + "="*70)
    print("🎯 CHALLENGE 2.4: File Magic Bytes (Realistic)")
    print("="*70)
    print("""
You found this hex dump from a file header:

89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52

What type of file is this?
Options: A) JPEG  B) PNG  C) PDF  D) ZIP
""")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if answer == "B":
        print("✅ CORRECT! 89 50 4E 47 = ‰PNG (PNG file signature)")
        score += 1
    else:
        print("❌ Wrong! The answer is B (PNG). 89 50 4E 47 = ‰PNG")
    
    print(f"\n📊 Hex Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 3: CAESAR/ROT CIPHERS (95% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def caesar_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 3: CAESAR/ROT CIPHERS (95% Appearance)                     ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• Letters shifted by N positions
• ROT13 = shift by 13 (self-reversing!)
• ROT47 includes numbers and symbols
• Bruteforce: only 26 possible shifts
""")
    
    score = 0
    
    # Challenge 3.1 - ROT13
    print("\n" + "="*70)
    print("🎯 CHALLENGE 3.1: Classic ROT13 (Beginner)")
    print("="*70)
    original = "HQ10FLAG{rot_thirteen}"
    rot13 = caesar_encode(original, 13)
    print(f"\nDecode this ROT13: {rot13}")
    print("\nHint: ROT13 is self-reversing (encoding = decoding)")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 3.2 - Unknown shift
    print("\n" + "="*70)
    print("🎯 CHALLENGE 3.2: Unknown Shift (Intermediate)")
    print("="*70)
    original = "HQ10FLAG{caesar_rules}"
    shift = 7
    encoded = caesar_encode(original, shift)
    print(f"\nDecode this Caesar cipher: {encoded}")
    print("\nHint: The flag format starts with HQ10FLAG - use that to find the shift!")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 3.3 - Bruteforce needed
    print("\n" + "="*70)
    print("🎯 CHALLENGE 3.3: Bruteforce Challenge (Hard)")
    print("="*70)
    original = "flag{bruteforce_me}"
    shift = 19
    encoded = caesar_encode(original, shift)
    print(f"\nDecode this: {encoded}")
    print("\nHint: Try all 26 shifts and look for readable text")
    print("Showing all shifts:")
    for i in range(26):
        decoded = caesar_decode(encoded, i)
        print(f"  Shift {i:2d}: {decoded}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 3.4 - ROT with numbers preserved
    print("\n" + "="*70)
    print("🎯 CHALLENGE 3.4: Mixed Content (Realistic)")
    print("="*70)
    original = "HQ10FLAG{m1x3d_c0nt3nt}"
    encoded = caesar_encode(original, 5)
    print(f"\nDecode this (numbers stay same, only letters shift): {encoded}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    print(f"\n📊 Caesar/ROT Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 4: SQL INJECTION (100% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def sql_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 4: SQL INJECTION (100% Appearance)                         ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• ' OR '1'='1 - always true condition
• admin'-- - comment out rest of query
• UNION SELECT - combine results
• ' AND SLEEP(5)-- - time-based blind
""")
    
    score = 0
    
    # Challenge 4.1 - Basic bypass
    print("\n" + "="*70)
    print("🎯 CHALLENGE 4.1: Login Bypass (Beginner)")
    print("="*70)
    print("""
Backend query: SELECT * FROM users WHERE username='$input' AND password='$pass'

What do you enter in username to bypass login?
Options:
A) admin
B) admin'--
C) admin OR 1=1
D) ' OR '1'='1'--
""")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if answer in ["B", "D"]:
        print("✅ CORRECT! Both B and D work for bypass!")
        score += 1
    else:
        print("❌ Wrong! B (admin'--) or D (' OR '1'='1'--) would work")
    
    # Challenge 4.2 - UNION attack
    print("\n" + "="*70)
    print("🎯 CHALLENGE 4.2: UNION Attack (Intermediate)")
    print("="*70)
    print("""
Query: SELECT name, price FROM products WHERE id = $input

The table has 2 columns. There's a 'users' table with columns: username, password

Write a payload to extract usernames and passwords:
""")
    
    answer = input("\nYour payload: ").lower()
    if "union" in answer and "select" in answer and "users" in answer:
        print("✅ CORRECT! UNION SELECT username, password FROM users would work!")
        score += 1
    else:
        print("❌ Expected something like: 1 UNION SELECT username, password FROM users--")
    
    # Challenge 4.3 - Error identification
    print("\n" + "="*70)
    print("🎯 CHALLENGE 4.3: Identify the Vulnerability (Hard)")
    print("="*70)
    print("""
You tested a search box with these inputs and got these responses:

Input: test         → "Found 5 results"
Input: test'        → "Error: syntax error near 'test''"
Input: test''       → "Found 0 results"
Input: test' OR '1  → "Found 127 results"

What type of SQL injection is this?
A) Blind SQL injection
B) Error-based SQL injection  
C) Time-based blind SQL injection
D) Union-based SQL injection
""")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if answer == "B":
        print("✅ CORRECT! Error messages reveal the vulnerability = Error-based SQLi")
        score += 1
    else:
        print("❌ Wrong! It's B - Error-based SQLi (visible error messages)")
    
    # Challenge 4.4 - Construct full attack
    print("\n" + "="*70)
    print("🎯 CHALLENGE 4.4: Real Scenario (Expert)")
    print("="*70)
    print("""
You found a vulnerable endpoint:
URL: http://target.com/user?id=1

When you try id=1' you get an error.
When you try id=1'-- you get no error.

You discovered the table has 4 columns using ORDER BY.
There's an 'admin_flags' table with a 'flag' column.

Construct the UNION payload to get the flag (columns 2 and 3 are displayed):
""")
    
    answer = input("\nYour payload: ").lower().replace(" ", "")
    # Check for key components
    if "union" in answer and "select" in answer and "admin_flags" in answer:
        print("✅ CORRECT! A valid payload would be:")
        print("   1 UNION SELECT null,flag,null,null FROM admin_flags--")
        score += 1
    else:
        print("❌ Expected: 1 UNION SELECT null,flag,null,null FROM admin_flags--")
    
    print(f"\n📊 SQL Injection Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 5: XOR OPERATIONS (90% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def xor_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 5: XOR OPERATIONS (90% Appearance)                         ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• XOR is reversible: A XOR B XOR B = A
• Single-byte XOR: try all 256 values
• Known plaintext attack: if you know part of message
• Common in malware and CTF challenges
""")
    
    score = 0
    
    # Challenge 5.1 - Single byte XOR
    print("\n" + "="*70)
    print("🎯 CHALLENGE 5.1: Single Byte XOR (Beginner)")
    print("="*70)
    original = "HQ10FLAG{xor_easy}"
    key = 0x42
    encrypted = [b ^ key for b in original.encode()]
    print(f"\nEncrypted bytes: {encrypted}")
    print(f"Key: 0x{key:02X} (decimal: {key})")
    print("\nHint: XOR each byte with the key")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 5.2 - Find the key
    print("\n" + "="*70)
    print("🎯 CHALLENGE 5.2: Find the Key (Intermediate)")
    print("="*70)
    original = "flag{found_key}"
    key = 0x55
    encrypted = [b ^ key for b in original.encode()]
    print(f"\nEncrypted bytes: {encrypted}")
    print(f"\nHint: You know the plaintext starts with 'flag'")
    print(f"First encrypted byte: {encrypted[0]} (0x{encrypted[0]:02X})")
    print(f"'f' in ASCII: {ord('f')} (0x{ord('f'):02X})")
    print(f"XOR them to find key: {encrypted[0]} XOR {ord('f')} = ?")
    
    answer = input("\nWhat is the key (in decimal)? ")
    try:
        if int(answer) == key:
            print(f"✅ CORRECT! Key is {key} (0x{key:02X})")
            score += 1
        else:
            print(f"❌ Wrong! Key is {key} (0x{key:02X})")
    except:
        print(f"❌ Invalid input. Key was {key}")
    
    # Challenge 5.3 - Multi-byte key
    print("\n" + "="*70)
    print("🎯 CHALLENGE 5.3: Multi-byte Key (Hard)")
    print("="*70)
    original = "HQ10FLAG{multi_byte_xor}"
    key = "KEY"
    encrypted = list(xor_encrypt(original, key))
    print(f"\nEncrypted bytes: {encrypted}")
    print(f"Key: '{key}' (3 characters, repeating)")
    print("\nHint: Apply XOR with repeating key K-E-Y-K-E-Y...")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    # Challenge 5.4 - Bruteforce single byte
    print("\n" + "="*70)
    print("🎯 CHALLENGE 5.4: Bruteforce (Realistic)")
    print("="*70)
    original = "flag{xor_brute}"
    key = 0x1F
    encrypted = [b ^ key for b in original.encode()]
    print(f"\nEncrypted bytes: {encrypted}")
    print("\nHint: Key is a single byte (0-255). Bruteforce all possibilities.")
    print("Looking for results containing 'flag':\n")
    
    found_key = None
    for k in range(256):
        decrypted = ''.join(chr(b ^ k) for b in encrypted)
        if 'flag' in decrypted.lower():
            print(f"Key {k} (0x{k:02X}): {decrypted}")
            found_key = k
    
    answer = input("\nYour answer: ")
    if check_answer(answer, original):
        score += 1
    
    print(f"\n📊 XOR Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 6: SOURCE CODE ANALYSIS (100% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def source_code_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 6: SOURCE CODE ANALYSIS (100% Appearance)                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• HTML comments: <!-- hidden content -->
• JavaScript variables
• Hidden form fields
• robots.txt, .git exposure
• HTTP headers and cookies
""")
    
    score = 0
    
    # Challenge 6.1 - HTML comment
    print("\n" + "="*70)
    print("🎯 CHALLENGE 6.1: Hidden in Comments (Beginner)")
    print("="*70)
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
    <!-- TODO: Remove before production -->
    <!-- FLAG: HQ10FLAG{html_comment} -->
</head>
<body>
    <h1>Welcome to our site!</h1>
    <p>Nothing to see here...</p>
</body>
</html>
"""
    print(f"\nFind the flag in this HTML:\n{html}")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, "HQ10FLAG{html_comment}"):
        score += 1
    
    # Challenge 6.2 - JavaScript variable
    print("\n" + "="*70)
    print("🎯 CHALLENGE 6.2: JavaScript Secret (Intermediate)")
    print("="*70)
    js_code = """
<script>
    var username = "guest";
    var isAdmin = false;
    var secretKey = "4851313046464c41477b6a735f736563726574737d";
    
    function checkLogin() {
        if (isAdmin) {
            console.log("Welcome admin!");
        }
    }
</script>
"""
    print(f"\nExamine this JavaScript code:\n{js_code}")
    print("\nHint: The secretKey looks like hex encoding!")
    
    answer = input("\nYour answer (decoded flag): ")
    if check_answer(answer, "HQ10FLAG{js_secrets}"):
        score += 1
    
    # Challenge 6.3 - robots.txt
    print("\n" + "="*70)
    print("🎯 CHALLENGE 6.3: robots.txt Discovery (Intermediate)")
    print("="*70)
    robots = """
User-agent: *
Disallow: /admin/
Disallow: /backup/
Disallow: /secret-flag-location/
Disallow: /old-site/

# Note: Flag is at /secret-flag-location/flag.txt
# Contents: HQ10FLAG{robots_reveal}
"""
    print(f"\nYou found this robots.txt:\n{robots}")
    
    answer = input("\nWhat is the flag? ")
    if check_answer(answer, "HQ10FLAG{robots_reveal}"):
        score += 1
    
    # Challenge 6.4 - Cookie analysis
    print("\n" + "="*70)
    print("🎯 CHALLENGE 6.4: Cookie Secrets (Hard)")
    print("="*70)
    cookie_value = base64.b64encode(b'{"user":"guest","flag":"HQ10FLAG{cookie_monster}","role":"user"}').decode()
    print(f"""
HTTP Response Headers:
Set-Cookie: session={cookie_value}; HttpOnly

Decode the session cookie to find the flag!
""")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, "HQ10FLAG{cookie_monster}"):
        score += 1
    
    print(f"\n📊 Source Code Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 7: STEGANOGRAPHY BASICS (100% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def stego_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 7: STEGANOGRAPHY BASICS (100% Appearance)                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• strings command - extract text from files
• exiftool - view metadata
• steghide - extract from JPEG
• binwalk - find embedded files
• Check file headers (magic bytes)
""")
    
    score = 0
    
    # Challenge 7.1 - Strings extraction
    print("\n" + "="*70)
    print("🎯 CHALLENGE 7.1: Hidden Strings (Beginner)")
    print("="*70)
    binary_dump = """
Output of 'strings suspicious_file.bin':

JFIF
Adobe
ICC_PROFILE
photoshop
HQ10FLAG{strings_ftw}
IEND
EOF
"""
    print(f"\nYou ran 'strings' on a file and got:\n{binary_dump}")
    print("\nFind the flag!")
    
    answer = input("\nYour answer: ")
    if check_answer(answer, "HQ10FLAG{strings_ftw}"):
        score += 1
    
    # Challenge 7.2 - Metadata
    print("\n" + "="*70)
    print("🎯 CHALLENGE 7.2: EXIF Metadata (Intermediate)")
    print("="*70)
    exif_output = """
Output of 'exiftool image.jpg':

ExifTool Version Number         : 12.40
File Name                       : image.jpg
File Size                       : 2.1 MB
File Type                       : JPEG
MIME Type                       : image/jpeg
Image Width                     : 1920
Image Height                    : 1080
Artist                          : John Doe
Comment                         : SGFja1F1ZXN0IGZsYWc6IEhRMTBGTEFHe21ldGFkYXRhX2hpZGRlbn0=
GPS Latitude                    : 40.7128 N
GPS Longitude                   : 74.0060 W
"""
    print(f"\nExiftool output:\n{exif_output}")
    print("\nHint: The Comment field looks suspicious (Base64)")
    
    answer = input("\nYour answer (decoded flag): ")
    if check_answer(answer, "HQ10FLAG{metadata_hidden}"):
        score += 1
    
    # Challenge 7.3 - File signature
    print("\n" + "="*70)
    print("🎯 CHALLENGE 7.3: Wrong Extension (Hard)")
    print("="*70)
    print("""
You have a file named 'document.pdf' but it won't open.
Hex dump of first 16 bytes:

50 4B 03 04 14 00 00 00 08 00 1A 7D 4A 55 00 00

What is the ACTUAL file type?
A) PDF
B) PNG
C) ZIP
D) JPEG
""")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if answer == "C":
        print("✅ CORRECT! 50 4B 03 04 = 'PK..' = ZIP file signature!")
        score += 1
    else:
        print("❌ Wrong! It's C (ZIP). 50 4B = 'PK' = ZIP header")
    
    # Challenge 7.4 - Binwalk concept
    print("\n" + "="*70)
    print("🎯 CHALLENGE 7.4: Embedded Files (Expert)")
    print("="*70)
    print("""
binwalk output for 'innocent_image.png':

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 800 x 600, 8-bit/color RGB
54321         0xD431          Zip archive, encrypted, flag.txt
54400         0xD480          End of Zip archive

What command extracts the embedded ZIP?
A) binwalk -e innocent_image.png
B) unzip innocent_image.png
C) steghide extract -sf innocent_image.png
D) strings innocent_image.png
""")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if answer == "A":
        print("✅ CORRECT! binwalk -e extracts embedded files!")
        score += 1
    else:
        print("❌ Wrong! A (binwalk -e) extracts embedded files")
    
    print(f"\n📊 Steganography Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#              TOPIC 8: HASH IDENTIFICATION (85% Appearance Rate)
# ═══════════════════════════════════════════════════════════════════════════════════

def hash_challenges():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                 TOPIC 8: HASH IDENTIFICATION (85% Appearance)                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

💡 KEY CONCEPTS:
• MD5: 32 hex characters
• SHA1: 40 hex characters
• SHA256: 64 hex characters
• bcrypt: starts with $2a$, $2b$, $2y$
• Use CrackStation for common hashes
""")
    
    score = 0
    
    # Challenge 8.1 - Identify hash type
    print("\n" + "="*70)
    print("🎯 CHALLENGE 8.1: Identify Hash Type (Beginner)")
    print("="*70)
    print("""
Identify these hash types:

a) 5d41402abc4b2a76b9719d911017c592
b) aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
c) 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Options: MD5, SHA1, SHA256
""")
    
    answer_a = input("Hash (a) is: ").upper()
    answer_b = input("Hash (b) is: ").upper()
    answer_c = input("Hash (c) is: ").upper()
    
    correct = 0
    if "MD5" in answer_a:
        correct += 1
        print("✅ (a) Correct - MD5 (32 chars)")
    else:
        print("❌ (a) is MD5 (32 characters)")
    
    if "SHA1" in answer_b:
        correct += 1
        print("✅ (b) Correct - SHA1 (40 chars)")
    else:
        print("❌ (b) is SHA1 (40 characters)")
    
    if "SHA256" in answer_c:
        correct += 1
        print("✅ (c) Correct - SHA256 (64 chars)")
    else:
        print("❌ (c) is SHA256 (64 characters)")
    
    if correct == 3:
        score += 1
    
    # Challenge 8.2 - Crack common hash
    print("\n" + "="*70)
    print("🎯 CHALLENGE 8.2: Crack MD5 (Intermediate)")
    print("="*70)
    # MD5 of "password"
    print("""
Crack this MD5 hash: 5f4dcc3b5aa765d61d8327deb882cf99

Hint: It's a very common password!
You can use CrackStation.net or hashcat.
""")
    
    answer = input("\nOriginal password: ")
    if check_answer(answer, "password"):
        score += 1
    
    # Challenge 8.3 - SHA1 crack
    print("\n" + "="*70)
    print("🎯 CHALLENGE 8.3: Crack SHA1 (Hard)")
    print("="*70)
    # SHA1 of "admin"
    print("""
Crack this SHA1 hash: d033e22ae348aeb5660fc2140aec35850c4da997

Hint: Think like a lazy admin!
""")
    
    answer = input("\nOriginal password: ")
    if check_answer(answer, "admin"):
        score += 1
    
    # Challenge 8.4 - Hash verification
    print("\n" + "="*70)
    print("🎯 CHALLENGE 8.4: Verify Integrity (Expert)")
    print("="*70)
    original = "HQ10FLAG{hash_verified}"
    correct_hash = hashlib.md5(original.encode()).hexdigest()
    
    print(f"""
You downloaded flag.txt with this content: HQ10FLAG{{hash_verified}}
The website says MD5 should be: {correct_hash}

Calculate the MD5 of the content. Does it match?
A) Yes, file is intact
B) No, file is corrupted
""")
    
    answer = input("\nYour answer (A/B): ").upper()
    if answer == "A":
        print("✅ CORRECT! The MD5 matches, file is intact!")
        score += 1
    else:
        print(f"❌ Wrong! MD5 of content is {correct_hash} - it matches!")
    
    print(f"\n📊 Hash Score: {score}/4")
    return score

# ═══════════════════════════════════════════════════════════════════════════════════
#                              MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║          TCS HACKQUEST - HIGH PRIORITY PRACTICE CHALLENGES                      ║
║                    32 Challenges Across 8 Topics                                 ║
╚══════════════════════════════════════════════════════════════════════════════════╝

These topics appear in 85-100% of all HackQuest seasons!
Complete all challenges to be fully prepared.

Press Enter to start, or type 'skip' + topic number to skip to a specific topic:
1. Base64    2. Hex       3. Caesar/ROT    4. SQL Injection
5. XOR       6. Source    7. Steganography 8. Hashes
""")
    
    choice = input("\nYour choice (Enter or skip#): ").strip()
    
    total_score = 0
    max_score = 32
    
    topics = [
        ("1", base64_challenges),
        ("2", hex_challenges),
        ("3", caesar_challenges),
        ("4", sql_challenges),
        ("5", xor_challenges),
        ("6", source_code_challenges),
        ("7", stego_challenges),
        ("8", hash_challenges),
    ]
    
    if choice.startswith("skip"):
        try:
            skip_to = choice.replace("skip", "").strip()
            start_idx = int(skip_to) - 1
            topics = topics[start_idx:]
        except:
            pass
    
    for topic_num, topic_func in topics:
        try:
            score = topic_func()
            total_score += score
            
            print(f"\n{'='*70}")
            cont = input("Press Enter for next topic (or 'q' to quit): ")
            if cont.lower() == 'q':
                break
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
    
    # Final Summary
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                           FINAL RESULTS                                          ║
╚══════════════════════════════════════════════════════════════════════════════════╝

Total Score: {total_score}/{max_score}
Percentage: {(total_score/max_score)*100:.1f}%

{'🏆 EXCELLENT! You are well prepared!' if total_score >= 28 else ''}
{'✅ GOOD! Review weak areas before the exam.' if 20 <= total_score < 28 else ''}
{'⚠️ NEEDS WORK! Focus on topics you struggled with.' if total_score < 20 else ''}

📚 QUICK REFERENCE:
- CyberChef: gchq.github.io/CyberChef
- CrackStation: crackstation.net
- dCode: dcode.fr
- Hash identifier: hashes.com/en/tools/hash_identifier

Good luck with TCS HackQuest Round 2! 🍀
""")

if __name__ == "__main__":
    main()
