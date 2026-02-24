"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║            TCS HACKQUEST - COMPLETE CTF TOOLS GUIDE                              ║
║                    When to Use What & How to Use It                              ║
╚══════════════════════════════════════════════════════════════════════════════════╝

This guide covers ALL essential tools for CTF challenges.
Run this file to get an interactive tool reference!
"""

def print_header(title):
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def print_section(content):
    print(content)

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 1: CYBERCHEF (MOST IMPORTANT!)
# ═══════════════════════════════════════════════════════════════════════════════════

def cyberchef_guide():
    print_header("🔧 TOOL 1: CYBERCHEF - The Swiss Army Knife of CTF")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  URL: https://gchq.github.io/CyberChef                                           ║
║  TYPE: Online (No installation needed!)                                          ║
║  PRIORITY: ⭐⭐⭐⭐⭐ MUST HAVE - Use for 80% of encoding challenges              ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE CYBERCHEF:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ Encoding/Decoding: Base64, Hex, URL, HTML entities                           │
│ ✅ Cipher cracking: ROT13, Caesar, Vigenère, XOR                                │
│ ✅ Hash operations: MD5, SHA1, SHA256                                           │
│ ✅ Data format conversion: Binary, Octal, Decimal                               │
│ ✅ String manipulation: Reverse, Find/Replace                                   │
│ ✅ Compression: Gzip, Zlib, Deflate                                             │
│ ✅ Multiple operations chained together                                         │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 ESSENTIAL CYBERCHEF RECIPES (Bookmark These!):

╭─────────────────────────────────────────────────────────────────────────────────╮
│ RECIPE 1: Multi-Layer Decode                                                    │
│ Operations: From Base64 → From Hex → ROT13                                      │
│ Use when: You see nested encoding                                               │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ RECIPE 2: XOR Bruteforce                                                        │
│ Operations: XOR Brute Force (Key length: 1)                                     │
│ Use when: Single-byte XOR encrypted data                                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ RECIPE 3: Magic (Auto-Detect)                                                   │
│ Operations: Magic (Intensive mode)                                              │
│ Use when: You don't know what encoding it is - CyberChef auto-detects!          │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ RECIPE 4: Extract Strings                                                       │
│ Operations: Strings (Min length: 4)                                             │
│ Use when: Analyzing binary data for hidden text                                 │
╰─────────────────────────────────────────────────────────────────────────────────╯

🎯 PRO TIPS:
• Use "Magic" operation when you're stuck - it auto-detects encoding!
• Save your recipes for quick access
• Use "Fork" to try multiple decode paths at once
• Drag operations to reorder them
• Click the "🔥" icon to bake (execute) your recipe

⚡ QUICK OPERATIONS CHEAT SHEET:
┌────────────────────────┬───────────────────────────────────────────────────────┐
│ Operation              │ Keyboard Shortcut / Search Term                       │
├────────────────────────┼───────────────────────────────────────────────────────┤
│ Base64 Decode          │ Search: "From Base64"                                 │
│ Hex Decode             │ Search: "From Hex"                                    │
│ ROT13                  │ Search: "ROT13"                                       │
│ XOR                    │ Search: "XOR"                                         │
│ URL Decode             │ Search: "URL Decode"                                  │
│ Magic (Auto)           │ Search: "Magic"                                       │
│ Caesar Bruteforce      │ Search: "ROT13 Brute Force"                           │
└────────────────────────┴───────────────────────────────────────────────────────┘
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 2: BROWSER DEVTOOLS (F12)
# ═══════════════════════════════════════════════════════════════════════════════════

def devtools_guide():
    print_header("🔧 TOOL 2: BROWSER DEVTOOLS (F12)")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  ACCESS: Press F12 or Right-click → Inspect                                      ║
║  TYPE: Built into every browser                                                  ║
║  PRIORITY: ⭐⭐⭐⭐⭐ ESSENTIAL for web challenges                                ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE DEVTOOLS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ Finding hidden HTML comments                                                 │
│ ✅ Viewing/modifying cookies                                                    │
│ ✅ Analyzing JavaScript code                                                    │
│ ✅ Checking network requests                                                    │
│ ✅ Modifying form values                                                        │
│ ✅ Viewing response headers                                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 DEVTOOLS TABS EXPLAINED:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 📁 ELEMENTS TAB                                                                 │
│ Purpose: View and edit HTML/CSS                                                 │
│ CTF Use:                                                                        │
│   • Find hidden comments: <!-- flag here -->                                    │
│   • Find hidden form fields: <input type="hidden" value="secret">               │
│   • Modify disabled buttons or inputs                                           │
│   • Check for data attributes: data-flag="..."                                  │
│                                                                                 │
│ Quick Search: Ctrl+F in Elements tab, search for:                               │
│   • "flag" "FLAG" "hidden" "secret" "password" "admin" "<!--"                   │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🌐 NETWORK TAB                                                                  │
│ Purpose: Monitor all HTTP requests/responses                                    │
│ CTF Use:                                                                        │
│   • See API calls and their responses                                           │
│   • Find hidden endpoints                                                       │
│   • Check response headers for flags                                            │
│   • Analyze POST request data                                                   │
│                                                                                 │
│ Pro Tip: Enable "Preserve log" to keep requests after page reload               │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 💻 CONSOLE TAB                                                                  │
│ Purpose: Execute JavaScript, view errors                                        │
│ CTF Use:                                                                        │
│   • Run: document.cookie (view cookies)                                         │
│   • Run: localStorage (view stored data)                                        │
│   • Find JS variables containing secrets                                        │
│   • Execute functions to bypass client-side validation                          │
│                                                                                 │
│ Useful Commands:                                                                │
│   document.cookie                    // View all cookies                        │
│   localStorage                       // View local storage                      │
│   Object.keys(window)                // List global variables                   │
│   atob("base64string")               // Decode Base64 in browser                │
│   btoa("string")                     // Encode to Base64                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 📦 APPLICATION TAB (Chrome) / STORAGE TAB (Firefox)                             │
│ Purpose: View cookies, localStorage, sessionStorage                             │
│ CTF Use:                                                                        │
│   • Edit cookie values directly                                                 │
│   • Find session tokens                                                         │
│   • Modify stored data                                                          │
│   • Check for cached credentials                                                │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 📄 SOURCES TAB                                                                  │
│ Purpose: View all loaded JavaScript files                                       │
│ CTF Use:                                                                        │
│   • Find hardcoded secrets in JS                                                │
│   • Analyze client-side validation logic                                        │
│   • Set breakpoints to debug                                                    │
│   • Search across all files: Ctrl+Shift+F                                       │
╰─────────────────────────────────────────────────────────────────────────────────╯

🎯 PRO TIPS:
• Ctrl+Shift+F = Search across ALL loaded files
• Ctrl+F in Elements = Search current page HTML
• Right-click cookie → Edit to modify values
• Network tab → Right-click request → Copy as cURL
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 3: BURP SUITE
# ═══════════════════════════════════════════════════════════════════════════════════

def burpsuite_guide():
    print_header("🔧 TOOL 3: BURP SUITE - Web Security Testing")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  URL: https://portswigger.net/burp/communitydownload                             ║
║  TYPE: Desktop Application (Free Community Edition)                              ║
║  PRIORITY: ⭐⭐⭐⭐ IMPORTANT for advanced web challenges                         ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE BURP SUITE:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ Intercepting and modifying HTTP requests                                     │
│ ✅ SQL Injection testing                                                        │
│ ✅ Bypassing client-side validation                                             │
│ ✅ Repeating requests with modifications                                        │
│ ✅ Brute-forcing login forms                                                    │
│ ✅ Parameter tampering                                                          │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 QUICK SETUP (Takes 2 minutes):

Step 1: Download & Install from portswigger.net
Step 2: Start Burp → Temporary Project → Use Burp Defaults
Step 3: Go to Proxy tab → Options → Note the port (default: 8080)
Step 4: Configure browser proxy: 127.0.0.1:8080
Step 5: Visit http://burp in browser to download CA certificate
Step 6: Import certificate to browser (for HTTPS interception)

📚 KEY FEATURES FOR CTF:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🎯 PROXY - Intercept                                                            │
│ Purpose: Catch and modify requests before they're sent                          │
│                                                                                 │
│ CTF Uses:                                                                       │
│   • Change POST parameters (user=admin, isAdmin=true)                           │
│   • Modify cookies on-the-fly                                                   │
│   • Bypass JavaScript validation                                                │
│   • Change request method (GET → POST)                                          │
│                                                                                 │
│ Shortcut: Ctrl+F = Forward request, Ctrl+D = Drop request                       │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🔄 REPEATER                                                                     │
│ Purpose: Manually modify and resend requests                                    │
│                                                                                 │
│ CTF Uses:                                                                       │
│   • Test SQL injection payloads manually                                        │
│   • Try different parameter values                                              │
│   • Analyze response differences                                                │
│                                                                                 │
│ Shortcut: Ctrl+R = Send request to Repeater                                     │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 💣 INTRUDER                                                                     │
│ Purpose: Automated attack tool (brute force, fuzzing)                           │
│                                                                                 │
│ CTF Uses:                                                                       │
│   • Brute force login credentials                                               │
│   • Fuzz parameters for SQLi/XSS                                                │
│   • Enumerate hidden files/directories                                          │
│                                                                                 │
│ Attack Types:                                                                   │
│   • Sniper: One position, one payload list                                      │
│   • Cluster Bomb: Multiple positions, multiple lists                            │
│                                                                                 │
│ Shortcut: Ctrl+I = Send request to Intruder                                     │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🔍 DECODER                                                                      │
│ Purpose: Encode/Decode data                                                     │
│                                                                                 │
│ Supports: URL, HTML, Base64, Hex, Binary, Gzip                                  │
│ Tip: Use "Smart Decode" for auto-detection                                      │
╰─────────────────────────────────────────────────────────────────────────────────╯

🎯 COMMON CTF ATTACK PATTERNS:

1️⃣ LOGIN BYPASS:
   Intercept login → Change: user=admin'-- OR password=anything
   
2️⃣ PRIVILEGE ESCALATION:
   Intercept request → Change: role=user → role=admin
   
3️⃣ HIDDEN PARAMETER:
   Add new parameter: &debug=true or &admin=1
   
4️⃣ COOKIE MANIPULATION:
   Change: isLoggedIn=false → isLoggedIn=true
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 4: WIRESHARK
# ═══════════════════════════════════════════════════════════════════════════════════

def wireshark_guide():
    print_header("🔧 TOOL 4: WIRESHARK - Network Packet Analysis")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  URL: https://www.wireshark.org/download.html                                    ║
║  TYPE: Desktop Application (Free)                                                ║
║  PRIORITY: ⭐⭐⭐⭐ IMPORTANT for forensics/network challenges                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE WIRESHARK:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ Analyzing .pcap / .pcapng files                                              │
│ ✅ Finding credentials in network traffic                                       │
│ ✅ Extracting files from packet captures                                        │
│ ✅ Analyzing HTTP/FTP/DNS traffic                                               │
│ ✅ Finding hidden data in packets                                               │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 ESSENTIAL DISPLAY FILTERS (Memorize These!):

╭─────────────────────────────────────────────────────────────────────────────────╮
│ FILTER                          │ PURPOSE                                       │
├─────────────────────────────────┼───────────────────────────────────────────────┤
│ http                            │ Show only HTTP traffic                        │
│ http.request                    │ Show only HTTP requests                       │
│ http.response                   │ Show only HTTP responses                      │
│ http contains "flag"            │ Find packets containing "flag"                │
│ http contains "password"        │ Find packets with passwords                   │
│ tcp.port == 80                  │ Traffic on port 80                            │
│ tcp.port == 443                 │ HTTPS traffic                                 │
│ ftp                             │ FTP traffic (often has credentials!)          │
│ ftp-data                        │ FTP file transfers                            │
│ dns                             │ DNS queries (check for exfiltration)          │
│ telnet                          │ Telnet (plaintext credentials!)               │
│ smtp                            │ Email traffic                                 │
│ frame contains "HQ10"           │ Find frames with flag prefix                  │
│ ip.addr == 192.168.1.1          │ Traffic to/from specific IP                   │
╰─────────────────────────────────────────────────────────────────────────────────╯

📚 STEP-BY-STEP PCAP ANALYSIS:

Step 1: Open PCAP file (File → Open)

Step 2: Get overview
        Statistics → Protocol Hierarchy
        (See what protocols are in the capture)

Step 3: Filter by protocol
        Type: http or ftp or dns

Step 4: Follow streams
        Right-click packet → Follow → TCP Stream
        (See full conversation in readable format!)

Step 5: Export objects
        File → Export Objects → HTTP
        (Extract all files transferred over HTTP!)

📚 COMMON CTF SCENARIOS:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SCENARIO: Find Login Credentials                                                │
│                                                                                 │
│ Steps:                                                                          │
│   1. Filter: http.request.method == "POST"                                      │
│   2. Look for login/auth endpoints                                              │
│   3. Check packet details for username/password                                 │
│   4. Or: Follow TCP Stream to see full request                                  │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SCENARIO: Extract Transferred File                                              │
│                                                                                 │
│ Steps:                                                                          │
│   1. File → Export Objects → HTTP (or FTP-DATA)                                 │
│   2. Save interesting files                                                     │
│   3. Analyze saved files for flags                                              │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SCENARIO: DNS Exfiltration                                                      │
│                                                                                 │
│ Steps:                                                                          │
│   1. Filter: dns                                                                │
│   2. Look for unusual subdomains                                                │
│   3. Subdomains might be hex/base64 encoded data                                │
│   Example: SGVsbG8.evil.com → "Hello" in Base64                                 │
╰─────────────────────────────────────────────────────────────────────────────────╯

🎯 KEYBOARD SHORTCUTS:
• Ctrl+F = Find packet
• Ctrl+G = Go to packet number
• Ctrl+Shift+F = Find string in all packets
• Right-click → Follow → TCP Stream
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 5: STEGHIDE
# ═══════════════════════════════════════════════════════════════════════════════════

def steghide_guide():
    print_header("🔧 TOOL 5: STEGHIDE - Image Steganography")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  INSTALL: apt install steghide (Linux) / Download for Windows                    ║
║  TYPE: Command Line Tool                                                         ║
║  PRIORITY: ⭐⭐⭐⭐ ESSENTIAL for steganography challenges                        ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE STEGHIDE:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ JPEG/JPG images with hidden data                                             │
│ ✅ WAV audio files with hidden data                                             │
│ ✅ When challenge says "password protected"                                     │
│ ✅ After other stego tools fail                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 ESSENTIAL COMMANDS:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ EXTRACT DATA (No Password):                                                     │
│                                                                                 │
│   steghide extract -sf image.jpg                                                │
│                                                                                 │
│   When prompted for password, just press Enter (empty password)                 │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ EXTRACT DATA (With Password):                                                   │
│                                                                                 │
│   steghide extract -sf image.jpg -p "password123"                               │
│                                                                                 │
│   Common passwords to try:                                                      │
│   • (empty - just press Enter)                                                  │
│   • password                                                                    │
│   • admin                                                                       │
│   • 123456                                                                      │
│   • The challenge name                                                          │
│   • Text visible in the image                                                   │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ GET INFO ABOUT FILE:                                                            │
│                                                                                 │
│   steghide info image.jpg                                                       │
│                                                                                 │
│   Shows: embedded file name, size, encryption algorithm                         │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ BRUTEFORCE PASSWORD (using stegcracker):                                        │
│                                                                                 │
│   pip install stegcracker                                                       │
│   stegcracker image.jpg wordlist.txt                                            │
│                                                                                 │
│   Uses rockyou.txt by default if no wordlist specified                          │
╰─────────────────────────────────────────────────────────────────────────────────╯

⚠️ IMPORTANT NOTES:
• Steghide ONLY works with JPEG and WAV files
• For PNG files, use zsteg or pngcheck instead
• If "could not extract" error, file might not have hidden data
• Or wrong password - try common ones first!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 6: EXIFTOOL
# ═══════════════════════════════════════════════════════════════════════════════════

def exiftool_guide():
    print_header("🔧 TOOL 6: EXIFTOOL - Metadata Analysis")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  INSTALL: apt install exiftool (Linux) / Download from exiftool.org              ║
║  TYPE: Command Line Tool                                                         ║
║  PRIORITY: ⭐⭐⭐⭐ ESSENTIAL for forensics challenges                            ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE EXIFTOOL:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ ANY image file (JPEG, PNG, GIF, TIFF, etc.)                                  │
│ ✅ PDF documents                                                                │
│ ✅ Audio/Video files                                                            │
│ ✅ Microsoft Office documents                                                   │
│ ✅ When looking for hidden info in file metadata                                │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 ESSENTIAL COMMANDS:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ VIEW ALL METADATA:                                                              │
│                                                                                 │
│   exiftool image.jpg                                                            │
│                                                                                 │
│   Shows: Camera info, GPS, dates, comments, author, etc.                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SEARCH FOR SPECIFIC TEXT:                                                       │
│                                                                                 │
│   exiftool image.jpg | grep -i flag                                             │
│   exiftool image.jpg | grep -i secret                                           │
│   exiftool image.jpg | findstr /i flag      (Windows)                           │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ VIEW SPECIFIC FIELDS:                                                           │
│                                                                                 │
│   exiftool -Comment image.jpg          # Just the comment field                 │
│   exiftool -Author image.jpg           # Author field                           │
│   exiftool -GPSPosition image.jpg      # GPS coordinates                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

📚 COMMON HIDING SPOTS IN METADATA:

┌────────────────────────────────────────────────────────────────────────────────┐
│ Field Name          │ Check For                                                │
├─────────────────────┼──────────────────────────────────────────────────────────┤
│ Comment             │ Often contains hidden flags or hints                     │
│ Artist/Author       │ May contain encoded data                                 │
│ Copyright           │ Hidden messages                                          │
│ Description         │ Challenge hints                                          │
│ User Comment        │ Base64 or hex encoded flags                              │
│ GPS Coordinates     │ May point to a location clue                             │
│ Thumbnail           │ Sometimes different from main image!                     │
└─────────────────────┴──────────────────────────────────────────────────────────┘

🎯 PRO TIP - Extract thumbnail (might be different from main image!):
   exiftool -b -ThumbnailImage image.jpg > thumbnail.jpg
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 7: BINWALK
# ═══════════════════════════════════════════════════════════════════════════════════

def binwalk_guide():
    print_header("🔧 TOOL 7: BINWALK - Embedded File Extraction")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  INSTALL: apt install binwalk (Linux) / pip install binwalk                      ║
║  TYPE: Command Line Tool                                                         ║
║  PRIORITY: ⭐⭐⭐⭐ ESSENTIAL for forensics/stego challenges                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE BINWALK:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ Finding files hidden inside other files                                      │
│ ✅ Analyzing firmware images                                                    │
│ ✅ When image file is suspiciously large                                        │
│ ✅ Finding ZIP/RAR archives inside images                                       │
│ ✅ Extracting embedded data                                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 ESSENTIAL COMMANDS:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SCAN FILE (No extraction):                                                      │
│                                                                                 │
│   binwalk suspicious_file.png                                                   │
│                                                                                 │
│   Output shows what's embedded and at what offset                               │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ EXTRACT EMBEDDED FILES:                                                         │
│                                                                                 │
│   binwalk -e suspicious_file.png                                                │
│   binwalk --extract suspicious_file.png                                         │
│                                                                                 │
│   Creates folder: _suspicious_file.png.extracted/                               │
│   Check this folder for extracted files!                                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ EXTRACT WITH RECURSION (for nested files):                                      │
│                                                                                 │
│   binwalk -eM suspicious_file.png                                               │
│                                                                                 │
│   Extracts files inside extracted files!                                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ ENTROPY ANALYSIS (detect encrypted/compressed data):                            │
│                                                                                 │
│   binwalk -E suspicious_file.png                                                │
│                                                                                 │
│   High entropy = encrypted or compressed data                                   │
╰─────────────────────────────────────────────────────────────────────────────────╯

📚 TYPICAL CTF SCENARIO:

You have: challenge.png (5MB - too big for a simple image!)

Step 1: binwalk challenge.png
        Output: ZIP archive at offset 0x1234

Step 2: binwalk -e challenge.png
        Creates: _challenge.png.extracted/

Step 3: cd _challenge.png.extracted
        ls
        → flag.txt found!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 8: STRINGS
# ═══════════════════════════════════════════════════════════════════════════════════

def strings_guide():
    print_header("🔧 TOOL 8: STRINGS - Extract Readable Text")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  INSTALL: Built into Linux / Download for Windows                                ║
║  TYPE: Command Line Tool                                                         ║
║  PRIORITY: ⭐⭐⭐⭐⭐ FIRST TOOL to use on any binary file!                       ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE STRINGS:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ ALWAYS try first on unknown binary files                                     │
│ ✅ Analyzing executables                                                        │
│ ✅ Finding hidden text in images/binaries                                       │
│ ✅ Quick scan for flags or passwords                                            │
│ ✅ Memory dump analysis                                                         │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 ESSENTIAL COMMANDS:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ BASIC USAGE:                                                                    │
│                                                                                 │
│   strings file.bin                                                              │
│   strings image.png                                                             │
│   strings executable.exe                                                        │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SEARCH FOR FLAG:                                                                │
│                                                                                 │
│   strings file.bin | grep -i flag                                               │
│   strings file.bin | grep -i "HQ10"                                             │
│   strings file.bin | findstr /i flag        (Windows)                           │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ MINIMUM STRING LENGTH:                                                          │
│                                                                                 │
│   strings -n 10 file.bin     # Only strings 10+ characters                      │
│   strings -n 4 file.bin      # Default is 4 characters                          │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SEARCH COMMON PATTERNS:                                                         │
│                                                                                 │
│   strings file | grep -i password                                               │
│   strings file | grep -i secret                                                 │
│   strings file | grep -i admin                                                  │
│   strings file | grep -i key                                                    │
│   strings file | grep -E "[A-Za-z0-9+/]{20,}={0,2}"   # Base64 pattern          │
╰─────────────────────────────────────────────────────────────────────────────────╯

🎯 PRO TIP: Always run strings first - it takes 2 seconds and often finds the flag!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 9: PYTHON SCRIPTING
# ═══════════════════════════════════════════════════════════════════════════════════

def python_guide():
    print_header("🔧 TOOL 9: PYTHON - Quick Scripting")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║  INSTALL: Already installed on most systems                                      ║
║  TYPE: Programming Language                                                      ║
║  PRIORITY: ⭐⭐⭐⭐⭐ ESSENTIAL for custom decoding                               ║
╚══════════════════════════════════════════════════════════════════════════════════╝

📌 WHEN TO USE PYTHON:
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ✅ Custom XOR decryption                                                        │
│ ✅ Brute-forcing when tools don't work                                          │
│ ✅ Automating repetitive tasks                                                  │
│ ✅ Complex encoding chains                                                      │
│ ✅ Web scraping for enumeration                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

📚 COPY-PASTE SCRIPTS FOR CTF:

╭─────────────────────────────────────────────────────────────────────────────────╮
│ BASE64 DECODE:                                                                  │
│                                                                                 │
│   import base64                                                                 │
│   encoded = "SGVsbG8gV29ybGQ="                                                  │
│   print(base64.b64decode(encoded).decode())                                     │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ HEX DECODE:                                                                     │
│                                                                                 │
│   hex_string = "48656c6c6f"                                                     │
│   print(bytes.fromhex(hex_string).decode())                                     │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ CAESAR/ROT BRUTEFORCE:                                                          │
│                                                                                 │
│   text = "ENCRYPTED_TEXT"                                                       │
│   for shift in range(26):                                                       │
│       result = ""                                                               │
│       for c in text:                                                            │
│           if c.isalpha():                                                       │
│               offset = ord('A') if c.isupper() else ord('a')                    │
│               result += chr((ord(c) - offset - shift) % 26 + offset)            │
│           else:                                                                 │
│               result += c                                                       │
│       print(f"Shift {shift}: {result}")                                         │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ SINGLE-BYTE XOR BRUTEFORCE:                                                     │
│                                                                                 │
│   encrypted = [0x1a, 0x0b, 0x1f, ...]  # Your encrypted bytes                   │
│   for key in range(256):                                                        │
│       decrypted = ''.join(chr(b ^ key) for b in encrypted)                      │
│       if 'flag' in decrypted.lower():                                           │
│           print(f"Key {key}: {decrypted}")                                      │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ MULTI-BYTE XOR:                                                                 │
│                                                                                 │
│   def xor_decrypt(data, key):                                                   │
│       return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])     │
│                                                                                 │
│   encrypted = bytes.fromhex("1a2b3c4d")                                         │
│   key = b"KEY"                                                                  │
│   print(xor_decrypt(encrypted, key))                                            │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ HASH GENERATION:                                                                │
│                                                                                 │
│   import hashlib                                                                │
│   text = "password"                                                             │
│   print("MD5:", hashlib.md5(text.encode()).hexdigest())                         │
│   print("SHA1:", hashlib.sha1(text.encode()).hexdigest())                       │
│   print("SHA256:", hashlib.sha256(text.encode()).hexdigest())                   │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ BINARY TO ASCII:                                                                │
│                                                                                 │
│   binary = "01001000 01101001"                                                  │
│   chars = binary.split()                                                        │
│   result = ''.join(chr(int(c, 2)) for c in chars)                               │
│   print(result)  # Output: Hi                                                   │
╰─────────────────────────────────────────────────────────────────────────────────╯
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    TOOL 10: ONLINE RESOURCES
# ═══════════════════════════════════════════════════════════════════════════════════

def online_resources():
    print_header("🌐 ONLINE TOOLS & RESOURCES")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    BOOKMARK THESE WEBSITES!                                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🔐 ENCODING/DECODING                                                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│ CyberChef          │ gchq.github.io/CyberChef       │ All-in-one tool          │
│ dCode              │ dcode.fr                       │ Cipher identifier        │
│ Base64 Decode      │ base64decode.org               │ Quick Base64             │
│ URL Decode         │ urldecoder.org                 │ URL encoding             │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🔑 HASH CRACKING                                                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│ CrackStation       │ crackstation.net               │ Hash lookup database     │
│ Hashes.com         │ hashes.com                     │ Hash identifier + crack  │
│ HashKiller         │ hashkiller.io                  │ MD5/SHA1 lookup          │
│ CMD5               │ cmd5.org                       │ MD5 database             │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🖼️ STEGANOGRAPHY ONLINE                                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│ AperiSolve         │ aperisolve.fr                  │ Auto-runs all stego!     │
│ StegOnline         │ stylesuxx.github.io/steganography │ LSB extraction        │
│ FotoForensics      │ fotoforensics.com              │ ELA analysis             │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🔍 REVERSE ENGINEERING                                                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Decompiler.com     │ decompiler.com                 │ Online decompiler        │
│ Compiler Explorer  │ godbolt.org                    │ Assembly viewer          │
│ Dogbolt            │ dogbolt.org                    │ Multiple decompilers     │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🌐 WEB SECURITY                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ HackTricks         │ book.hacktricks.xyz            │ Pentesting cheatsheets   │
│ PayloadsAllTheThings │ github.com/swisskyrepo/...   │ Payload database         │
│ GTFOBins           │ gtfobins.github.io             │ Linux privilege escal.   │
│ RequestBin         │ requestbin.com                 │ Capture HTTP requests    │
╰─────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────╮
│ 🔢 CRYPTOGRAPHY                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Boxentriq          │ boxentriq.com/code-breaking    │ Cipher tools             │
│ Cryptii            │ cryptii.com                    │ Encoding converter       │
│ RsaCtfTool         │ github.com/Ganapati/RsaCtfTool │ RSA attacks              │
│ FactorDB           │ factordb.com                   │ Factor large numbers     │
╰─────────────────────────────────────────────────────────────────────────────────╯

💡 PRO TIP: Open these in browser tabs BEFORE the competition starts!
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                    QUICK REFERENCE - WHICH TOOL FOR WHAT
# ═══════════════════════════════════════════════════════════════════════════════════

def quick_reference():
    print_header("⚡ QUICK REFERENCE - Which Tool for What?")
    print_section("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    CHALLENGE TYPE → TOOL TO USE                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────┐
│ CHALLENGE TYPE                    │ FIRST TOOL         │ ALTERNATIVES            │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ Base64/Hex/Encoding               │ CyberChef          │ Python, dCode           │
│ Caesar/ROT cipher                 │ CyberChef          │ dCode, Python           │
│ Unknown cipher                    │ dCode.fr           │ CyberChef Magic         │
│ XOR encryption                    │ CyberChef          │ Python script           │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ Hash cracking (MD5/SHA)           │ CrackStation       │ hashcat, John           │
│ Hash identification               │ Hashes.com         │ hash-identifier         │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ Image with hidden data            │ strings + exiftool │ binwalk, steghide       │
│ JPEG steganography                │ steghide           │ stegseek                │
│ PNG steganography                 │ zsteg              │ pngcheck, AperiSolve    │
│ Image - LSB encoding              │ AperiSolve         │ StegOnline              │
│ Large image file                  │ binwalk -e         │ foremost                │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ Web - find hidden content         │ DevTools (F12)     │ View source, curl       │
│ Web - modify requests             │ Burp Suite         │ DevTools Network        │
│ Web - SQL injection               │ Burp Repeater      │ sqlmap                  │
│ Web - directory enumeration       │ gobuster           │ dirb, ffuf              │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ PCAP network capture              │ Wireshark          │ tshark, NetworkMiner    │
│ Network credentials               │ Wireshark filters  │ NetworkMiner            │
│ Extract files from PCAP           │ Wireshark Export   │ binwalk                 │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ Binary/Executable analysis        │ strings            │ Ghidra, IDA             │
│ Reverse engineering               │ Ghidra             │ radare2, IDA            │
│ Memory dump analysis              │ volatility         │ strings                 │
├───────────────────────────────────┼────────────────────┼─────────────────────────┤
│ PDF with hidden data              │ pdftotext          │ qpdf, strings           │
│ File type unknown                 │ file command       │ binwalk, hexdump        │
│ Corrupted file header             │ hexedit            │ HxD (Windows)           │
└───────────────────────────────────┴────────────────────┴─────────────────────────┘

📝 DECISION FLOWCHART:

Got a file?
    │
    ├─→ Is it an image? ─────→ strings → exiftool → binwalk → steghide/zsteg
    │
    ├─→ Is it a PCAP? ───────→ Wireshark → Follow TCP Stream → Export Objects
    │
    ├─→ Is it encoded text? ─→ CyberChef Magic → Try Base64/Hex/ROT
    │
    ├─→ Is it a hash? ───────→ Identify length → CrackStation
    │
    ├─→ Is it a binary/exe? ─→ strings → file → Ghidra
    │
    └─→ Unknown? ────────────→ file command → strings → binwalk
""")

# ═══════════════════════════════════════════════════════════════════════════════════
#                              MAIN MENU
# ═══════════════════════════════════════════════════════════════════════════════════

def main():
    tools = {
        "1": ("CyberChef (MOST IMPORTANT)", cyberchef_guide),
        "2": ("Browser DevTools (F12)", devtools_guide),
        "3": ("Burp Suite", burpsuite_guide),
        "4": ("Wireshark", wireshark_guide),
        "5": ("Steghide", steghide_guide),
        "6": ("Exiftool", exiftool_guide),
        "7": ("Binwalk", binwalk_guide),
        "8": ("Strings", strings_guide),
        "9": ("Python Scripting", python_guide),
        "10": ("Online Resources", online_resources),
        "Q": ("Quick Reference - Which Tool for What?", quick_reference),
        "A": ("Show ALL guides", None),
    }
    
    while True:
        print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              TCS HACKQUEST - CTF TOOLS GUIDE                                     ║
║                  Select a tool to learn about:                                   ║
╚══════════════════════════════════════════════════════════════════════════════════╝

  1.  CyberChef ⭐⭐⭐⭐⭐        6.  Exiftool (Metadata)
  2.  Browser DevTools (F12)    7.  Binwalk (Embedded files)
  3.  Burp Suite                8.  Strings (Text extraction)
  4.  Wireshark (PCAP)          9.  Python Scripting
  5.  Steghide (Stego)          10. Online Resources
  
  Q.  ⚡ QUICK REFERENCE - Which tool for what?
  A.  📚 Show ALL guides
  X.  Exit

""")
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == "X":
            print("\nGood luck with HackQuest! 🍀\n")
            break
        elif choice == "A":
            for key, (name, func) in tools.items():
                if func:
                    func()
                    input("\nPress Enter to continue...")
        elif choice in tools:
            name, func = tools[choice]
            if func:
                func()
                input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
