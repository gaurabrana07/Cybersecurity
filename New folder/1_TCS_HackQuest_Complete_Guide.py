"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    TCS HACKQUEST SEASON 10 - COMPLETE STUDY GUIDE               ║
║                         CYBERSECURITY CTF PREPARATION                            ║
║                              ROUND 2 PREPARATION                                 ║
╚══════════════════════════════════════════════════════════════════════════════════╝

🎯 WHAT IS TCS HACKQUEST?
========================
- TCS HackQuest is a CYBERSECURITY competition based on "Capture The Flag" (CTF) format
- Started in 2016 by TCS to find talented ethical hackers
- Winners get prizes worth up to ₹5 Lakhs and job offers in TCS Cybersecurity unit
- Flag format: HQ10FLAG{...} or HQ10{...} for hidden keys (Season 10)

📋 CONTEST STRUCTURE (SEASON 10)
================================
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ROUND 1: Online CTF Challenge (6 hours)                                         │
│   - Online challenge-based test                                                 │
│   - Solve challenges & capture flags                                            │
│   - Submit detailed report with screenshots                                     │
│   - Three difficulty levels: Beginner, Intermediate, Expert                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│ ROUND 2: Proctored Online (Your round tomorrow!)                                │
│   Activity 1: Penetration Testing on hosted challenges                          │
│   Activity 2: Case Explanation (3-4 hours) - Explain your approach              │
│   - Conducted via MS Teams/Webex (Camera ON required)                           │
│   - More advanced challenges                                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│ FINAL ROUND: In-Person Jury Evaluation at TCS Premises                          │
└─────────────────────────────────────────────────────────────────────────────────┘

🔥 ROUND 2 SPECIFIC TOPICS (IMPORTANT!)
=======================================
1. System Exploitation
2. Penetration Testing of Web Applications  
3. Mobile Security
4. Digital Forensics
5. Threat Hunting
6. Incident Response
7. Source Code Analysis

═══════════════════════════════════════════════════════════════════════════════════
                              SYLLABUS & TOPICS
═══════════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
#                        1. WEB APPLICATION SECURITY
# ============================================================================
"""
🌐 WEB APPLICATION SECURITY (HIGH PRIORITY)
============================================

A) SQL INJECTION (SQLi)
-----------------------
- What: Inserting malicious SQL queries through user inputs
- Types:
  • In-band SQLi (Error-based, Union-based)
  • Blind SQLi (Boolean-based, Time-based)
  • Out-of-band SQLi

Common Payloads:
"""
sql_injection_payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "admin'--",
    "' UNION SELECT NULL, NULL, NULL --",
    "' UNION SELECT username, password FROM users --",
    "1' AND SLEEP(5) --",  # Time-based blind
    "1' AND 1=1 --",       # Boolean-based blind
]

"""
B) CROSS-SITE SCRIPTING (XSS)
-----------------------------
- What: Injecting malicious scripts into web pages
- Types:
  • Reflected XSS (Non-persistent)
  • Stored XSS (Persistent)
  • DOM-based XSS
"""
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "javascript:alert('XSS')",
    "<iframe src='javascript:alert(1)'>",
]

"""
C) COMMAND INJECTION
--------------------
- What: Executing system commands through vulnerable inputs
"""
command_injection_payloads = [
    "; ls -la",
    "| cat /etc/passwd",
    "& whoami",
    "`id`",
    "$(cat /etc/passwd)",
    "; cat /etc/shadow",
]

"""
D) LOCAL FILE INCLUSION (LFI) / DIRECTORY TRAVERSAL
---------------------------------------------------
- What: Accessing files outside intended directory
"""
lfi_payloads = [
    "../../../etc/passwd",
    "....//....//....//etc/passwd",
    "/etc/passwd%00",
    "....\/....\/....\/etc/passwd",
    "php://filter/convert.base64-encode/resource=index.php",
]

"""
E) CROSS-SITE REQUEST FORGERY (CSRF)
------------------------------------
- What: Tricking users to perform unintended actions
- Look for: Missing CSRF tokens, No referrer validation

F) SERVER-SIDE REQUEST FORGERY (SSRF)
-------------------------------------
- What: Making server perform requests to internal resources
- Targets: localhost, 127.0.0.1, internal IPs (192.168.x.x, 10.x.x.x)

G) INSECURE DIRECT OBJECT REFERENCE (IDOR)
------------------------------------------
- What: Accessing unauthorized resources by changing IDs
- Example: /user/profile?id=123 → Try /user/profile?id=124
"""

# ============================================================================
#                        2. CRYPTOGRAPHY
# ============================================================================
"""
🔐 CRYPTOGRAPHY (MEDIUM-HIGH PRIORITY)
======================================

A) ENCODING vs ENCRYPTION
-------------------------
Encoding (NOT encryption):
  • Base64 - Characters: A-Za-z0-9+/=
  • Base32 - Characters: A-Z2-7=
  • Hex    - Characters: 0-9a-f
  • URL Encoding - %20, %3D, etc.
"""

import base64
import binascii

def encoding_examples():
    text = "HackQuest Flag"
    
    # Base64 Encoding/Decoding
    b64_encoded = base64.b64encode(text.encode()).decode()
    b64_decoded = base64.b64decode(b64_encoded).decode()
    print(f"Base64: {text} -> {b64_encoded}")
    
    # Hex Encoding/Decoding  
    hex_encoded = text.encode().hex()
    hex_decoded = bytes.fromhex(hex_encoded).decode()
    print(f"Hex: {text} -> {hex_encoded}")
    
    # Binary
    binary = ' '.join(format(ord(c), '08b') for c in text)
    print(f"Binary: {text} -> {binary}")

"""
B) CLASSICAL CIPHERS
--------------------
1. Caesar Cipher (ROT13 is special case with shift=13)
2. Vigenère Cipher
3. Substitution Cipher
4. Atbash Cipher
"""

def caesar_cipher(text, shift):
    """Caesar cipher encoder/decoder"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def rot13(text):
    """ROT13 - Special case of Caesar with shift=13"""
    return caesar_cipher(text, 13)

def caesar_bruteforce(ciphertext):
    """Try all 26 shifts"""
    print("Caesar Cipher Bruteforce:")
    for shift in range(26):
        print(f"Shift {shift:2d}: {caesar_cipher(ciphertext, shift)}")

"""
C) MODERN CRYPTOGRAPHY
----------------------
1. Symmetric: AES, DES, 3DES, RC4
2. Asymmetric: RSA, ECC
3. Hashing: MD5, SHA1, SHA256, SHA512
4. HMAC

D) HASH CRACKING
----------------
- Rainbow tables
- Dictionary attacks
- John the Ripper, Hashcat
- Online: CrackStation, MD5Decrypt
"""

# Common hash patterns
hash_patterns = {
    "MD5": "32 hex characters (a-f, 0-9)",
    "SHA1": "40 hex characters",
    "SHA256": "64 hex characters",
    "SHA512": "128 hex characters",
    "NTLM": "32 hex characters (Windows)",
    "bcrypt": "$2a$, $2b$, $2y$ prefix",
}

# ============================================================================
#                        3. DIGITAL FORENSICS
# ============================================================================
"""
🔍 DIGITAL FORENSICS (HIGH PRIORITY FOR ROUND 2)
=================================================

A) FILE ANALYSIS
----------------
1. Magic Bytes/File Signatures
"""
file_signatures = {
    "PNG": b'\x89PNG\r\n\x1a\n',
    "JPEG": b'\xff\xd8\xff',
    "GIF": b'GIF87a' or b'GIF89a',
    "PDF": b'%PDF',
    "ZIP": b'PK\x03\x04',
    "RAR": b'Rar!\x1a\x07',
    "ELF": b'\x7fELF',
    "EXE/DLL": b'MZ',
    "7z": b"7z\xbc\xaf'",
}

"""
2. Metadata Analysis
   - EXIF data in images (GPS, camera info, timestamps)
   - Tools: exiftool, strings, file

3. Steganography
   - Hidden data in images/audio
   - Tools: steghide, zsteg, stegsolve, binwalk

B) MEMORY FORENSICS
-------------------
- Analyzing RAM dumps
- Tool: Volatility Framework
- Extract: passwords, processes, network connections, registry

C) DISK FORENSICS
-----------------
- Analyzing disk images
- Tools: Autopsy, FTK Imager, sleuthkit
- Look for: deleted files, hidden partitions, slack space

D) NETWORK FORENSICS
--------------------
- Analyzing packet captures (.pcap files)
- Tool: Wireshark, tshark, NetworkMiner
"""

# Wireshark Filters
wireshark_filters = {
    "HTTP traffic": "http",
    "Specific IP": "ip.addr == 192.168.1.1",
    "TCP port": "tcp.port == 80",
    "HTTP POST": "http.request.method == POST",
    "Contains string": "frame contains 'flag'",
    "DNS queries": "dns",
    "FTP traffic": "ftp",
    "Follow TCP stream": "tcp.stream eq 0",
}

# ============================================================================
#                        4. REVERSE ENGINEERING
# ============================================================================
"""
⚙️ REVERSE ENGINEERING (MEDIUM PRIORITY)
=========================================

A) STATIC ANALYSIS (Without running)
------------------------------------
- Disassemblers: IDA Pro, Ghidra (free), radare2
- Decompilers: Ghidra, IDA Pro
- String analysis: strings command

B) DYNAMIC ANALYSIS (While running)
-----------------------------------
- Debuggers: GDB, x64dbg, OllyDbg
- ltrace, strace (Linux)

C) COMMON PATTERNS TO LOOK FOR
------------------------------
1. Hardcoded strings/passwords
2. XOR operations (common obfuscation)
3. Comparison functions (strcmp, memcmp)
4. Input validation routines
"""

def xor_decrypt(data, key):
    """XOR decryption - commonly used in CTF challenges"""
    if isinstance(key, str):
        key = key.encode()
    if isinstance(data, str):
        data = data.encode()
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

# ============================================================================
#                        5. NETWORK SECURITY
# ============================================================================
"""
🌐 NETWORK SECURITY
===================

A) RECONNAISSANCE
-----------------
- nmap scanning
- Identifying open ports and services
- Banner grabbing
"""
nmap_commands = {
    "Basic scan": "nmap -sV target",
    "All ports": "nmap -p- target",
    "Aggressive": "nmap -A target",
    "Stealth scan": "nmap -sS target",
    "UDP scan": "nmap -sU target",
    "Scripts": "nmap --script=vuln target",
}

"""
B) COMMON PORTS
---------------
"""
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Proxy",
}

# ============================================================================
#                        6. PASSWORD CRACKING
# ============================================================================
"""
🔓 PASSWORD CRACKING
====================

A) TECHNIQUES
-------------
1. Dictionary Attack - Using wordlists
2. Brute Force - All combinations
3. Rainbow Tables - Precomputed hashes
4. Rule-based - Modifications to wordlist

B) TOOLS
--------
- John the Ripper
- Hashcat
- Hydra (for online attacks)
- CrackStation (online)

C) COMMON WORDLISTS
-------------------
- rockyou.txt (14 million passwords)
- SecLists collection
"""

# ============================================================================
#                        7. LINUX COMMANDS FOR CTF
# ============================================================================
"""
🐧 ESSENTIAL LINUX COMMANDS
============================
"""
linux_commands = {
    # File Analysis
    "file": "Determine file type",
    "strings": "Extract printable strings",
    "xxd": "Hex dump",
    "hexdump": "Hex dump alternative",
    "binwalk": "Analyze/extract embedded files",
    
    # Text Processing
    "grep": "Search text patterns",
    "cat": "Display file contents",
    "head/tail": "Show beginning/end",
    "awk": "Text processing",
    "sed": "Stream editor",
    "sort | uniq": "Find unique values",
    
    # Network
    "netcat (nc)": "Network connections",
    "curl/wget": "HTTP requests",
    "tcpdump": "Capture packets",
    "nslookup/dig": "DNS queries",
    
    # System
    "ps aux": "Running processes",
    "netstat -tulpn": "Network connections",
    "find / -name 'flag*'": "Find files",
    "chmod": "Change permissions",
    "sudo -l": "Check sudo privileges",
}

# ============================================================================
#                        8. TOOLS CHECKLIST
# ============================================================================
"""
🛠️ RECOMMENDED TOOLS (Have these ready!)
==========================================

WEB EXPLOITATION:
-----------------
□ Burp Suite (intercept/modify requests)
□ Browser Developer Tools (F12)
□ curl / wget
□ SQLmap (automated SQL injection)
□ Nikto (web scanner)
□ DirBuster / Gobuster (directory bruteforce)

FORENSICS:
----------
□ Wireshark (packet analysis)
□ Volatility (memory forensics)
□ Autopsy (disk forensics)
□ exiftool (metadata)
□ steghide, zsteg (steganography)
□ binwalk (embedded files)
□ foremost/scalpel (file carving)

CRYPTOGRAPHY:
-------------
□ CyberChef (online - MUST HAVE!)
□ John the Ripper / Hashcat
□ OpenSSL
□ Python (pycryptodome library)

REVERSE ENGINEERING:
--------------------
□ Ghidra (free, excellent decompiler)
□ GDB (debugger)
□ radare2 / r2
□ strings, objdump, ltrace

GENERAL:
--------
□ Kali Linux VM or WSL
□ Python 3 with common libraries
□ Netcat (nc)
□ nmap
"""

# ============================================================================
#                        9. CTF FLAG FORMATS
# ============================================================================
"""
🚩 FLAG FORMATS TO LOOK FOR
============================

TCS HackQuest Season 10:
- HQ10FLAG{...}
- HQ10{...} (hidden keys)

Common CTF formats:
- flag{...}
- FLAG{...}
- CTF{...}
- picoCTF{...}

Look in:
- Source code comments
- Hidden HTML elements
- HTTP headers
- Cookies
- File metadata
- Base64 encoded strings
- Hex strings
"""

# ============================================================================
#                        10. QUICK REFERENCE - ENCODING/DECODING
# ============================================================================

def quick_decode_check(suspicious_string):
    """
    Quick function to try common decodings on a suspicious string
    Useful during CTF when you find encoded data
    """
    print(f"\n🔍 Analyzing: {suspicious_string[:50]}...")
    print("=" * 60)
    
    # Try Base64
    try:
        decoded = base64.b64decode(suspicious_string).decode('utf-8', errors='ignore')
        if decoded.isprintable():
            print(f"✅ Base64 decoded: {decoded}")
    except:
        print("❌ Not valid Base64")
    
    # Try Hex
    try:
        decoded = bytes.fromhex(suspicious_string).decode('utf-8', errors='ignore')
        if decoded.isprintable():
            print(f"✅ Hex decoded: {decoded}")
    except:
        print("❌ Not valid Hex")
    
    # Try ROT13
    rot13_result = rot13(suspicious_string)
    print(f"🔄 ROT13: {rot13_result}")
    
    # Try reversing
    print(f"🔄 Reversed: {suspicious_string[::-1]}")

# ============================================================================
#                        PRACTICE CHALLENGES
# ============================================================================
"""
📝 PRACTICE CHALLENGES (Try these!)
====================================

BEGINNER LEVEL:
1. Decode: U0dGamExRjFaWE4wSUZObFlYTnZiaUF4TUE9PQ==
   (Hint: Double Base64)

2. Find the flag in this HTML comment:
   <!-- Flag is: ZmxhZ3toaWRkZW5faW5faHRtbH0= -->

3. ROT13 decode: UPG{fvzcyr_ebgngvba}

INTERMEDIATE LEVEL:
4. SQL Injection: Login bypass with admin account
   Username: admin' --
   Password: anything

5. Analyze this packet capture for credentials (use Wireshark)

6. XOR Challenge: 
   Encrypted: [0x17, 0x0a, 0x14, 0x06, 0x3b, 0x2e, 0x36, 0x24]
   Key: "SECRET"

EXPERT LEVEL:
7. Reverse engineer a binary to find hardcoded password
8. Memory forensics - Extract credentials from RAM dump
9. Web exploitation chain: SQLi -> File upload -> RCE
"""

# ============================================================================
#                        ROUND 2 SPECIFIC TIPS
# ============================================================================
"""
⭐ ROUND 2 SPECIFIC TIPS
========================

1. BEFORE THE TEST:
   □ Test your camera and microphone
   □ Stable internet connection
   □ Keep Kali Linux/tools ready
   □ Have note-taking app ready
   □ Keep water bottle nearby

2. DURING THE TEST:
   □ Read challenge descriptions carefully
   □ Start with easier challenges first
   □ Take screenshots of EVERYTHING
   □ Document your approach step-by-step
   □ Keep track of time
   □ Don't brute-force (may get blocked)

3. FOR CASE EXPLANATION:
   □ Be ready to explain your methodology
   □ Know why you used specific tools
   □ Be confident about your approach
   □ Admit if you don't know something
   □ Show your problem-solving thought process

4. COMMON MISTAKES TO AVOID:
   □ Don't use automated scanners blindly
   □ Don't skip reading the hints
   □ Don't forget to submit the report
   □ Don't share credentials with others
   □ Don't give up too early on challenges
"""

# ============================================================================
#                        QUICK PRACTICE SOLUTIONS
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("TCS HACKQUEST SEASON 10 - ROUND 2 PREPARATION")
    print("=" * 70)
    
    print("\n📚 PRACTICE SOLUTIONS:\n")
    
    # Challenge 1: Double Base64
    print("1. Double Base64 Challenge:")
    encoded = "U0dGamExRjFaWE4wSUZObFlYTnZiaUF4TUE9PQ=="
    first_decode = base64.b64decode(encoded).decode()
    second_decode = base64.b64decode(first_decode).decode()
    print(f"   First decode: {first_decode}")
    print(f"   Second decode: {second_decode}")
    
    # Challenge 2: HTML Comment Base64
    print("\n2. HTML Comment Challenge:")
    flag_b64 = "ZmxhZ3toaWRkZW5faW5faHRtbH0="
    print(f"   Decoded: {base64.b64decode(flag_b64).decode()}")
    
    # Challenge 3: ROT13
    print("\n3. ROT13 Challenge:")
    rot13_text = "UPG{fvzcyr_ebgngvba}"
    print(f"   Decoded: {rot13(rot13_text)}")
    
    # Challenge 6: XOR
    print("\n6. XOR Challenge:")
    encrypted = [0x17, 0x0a, 0x14, 0x06, 0x3b, 0x2e, 0x36, 0x24]
    key = "SECRET"
    decrypted = xor_decrypt(bytes(encrypted), key)
    print(f"   Decrypted: {decrypted.decode()}")
    
    print("\n" + "=" * 70)
    print("🎯 Good luck with your TCS HackQuest Round 2!")
    print("=" * 70)
    
    # Run encoding examples
    print("\n📖 ENCODING EXAMPLES:")
    encoding_examples()
