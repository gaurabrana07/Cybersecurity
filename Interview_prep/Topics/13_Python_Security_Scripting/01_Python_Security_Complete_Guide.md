# 🐍 PYTHON SECURITY SCRIPTING - COMPLETE INTERVIEW GUIDE
## TCS HACKQUEST PRIME | Gaurab Rana

---

# SECTION 1: PYTHON SECURITY FUNDAMENTALS

## Q1. Why is Python popular for security scripting?
**Answer:**
1. **Rapid development** - Quick prototype creation
2. **Rich libraries** - requests, scapy, paramiko, cryptography
3. **Cross-platform** - Works on Linux, Windows, Mac
4. **Readability** - Easy to maintain and share code
5. **Integration** - Works with C libraries, APIs, databases

*Your Experience:* "I used Python for my Web Vulnerability Scanner because of its excellent HTTP libraries and ability to quickly iterate on payload testing."

---

## Q2. What security libraries have you used in Python?
**Answer:**
```python
# Core Security Libraries
import requests      # HTTP requests, API testing
import socket        # Network scanning, raw connections
import hashlib       # Hashing (SHA-256, MD5)
import ssl           # SSL/TLS connections
import asyncio       # Async scanning (your scanner!)
import re            # Regex for pattern matching (SQL errors)
import cryptography  # AES, RSA encryption (StegoCrypt!)
from PIL import Image # Image manipulation (steganography)
```

*Your Projects:*
- Web Scanner: `requests`, `asyncio`, `re`, `urllib.parse`
- StegoCrypt: `cryptography`, `PIL`, `Fernet`

---

## Q3. Explain your Web Vulnerability Scanner's architecture.
**Answer:**
```
+-------------------+
|   Main Controller |
+-------------------+
         |
+--------+--------+--------+--------+--------+
|        |        |        |        |        |
v        v        v        v        v        v
SQLi    XSS    Port    Headers  Dir     Report
Module  Module  Scan    Check   Brute   Generator
(25+)   (20+)   (43      (10+    (88+
payloads)       ports)  headers) paths)
         |
         v
    +----------+
    | Async    |
    | Engine   |
    | (asyncio)|
    +----------+
```

Key Components:
1. **Payload Engine** - Injects 25+ SQLi and 20+ XSS payloads
2. **Async Scanner** - Uses `asyncio` for parallel port scanning
3. **Regex Detector** - Pattern matches SQL errors in responses
4. **Report Generator** - Outputs findings in structured format

---

## Q4. Write a basic SQL injection detector in Python.
**Answer:**
```python
import requests
import re

def check_sqli(url, param):
    """Test URL for SQL injection vulnerabilities"""
    
    # Common SQLi payloads
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1'--",
        "1; DROP TABLE users--",
        "' UNION SELECT NULL,NULL--",
        "1' AND '1'='1"
    ]
    
    # SQL error patterns (regex)
    sql_errors = [
        r"SQL syntax.*MySQL",
        r"Warning.*mysql_",
        r"valid MySQL result",
        r"PostgreSQL.*ERROR",
        r"ORA-\d{5}",
        r"SQLite.*error",
        r"ODBC.*error"
    ]
    
    results = []
    
    for payload in payloads:
        # Inject payload
        test_url = f"{url}?{param}={payload}"
        
        try:
            response = requests.get(test_url, timeout=10)
            
            # Check for SQL errors in response
            for pattern in sql_errors:
                if re.search(pattern, response.text, re.IGNORECASE):
                    results.append({
                        'payload': payload,
                        'error_pattern': pattern,
                        'vulnerable': True
                    })
                    break
        except Exception as e:
            continue
    
    return results

# Example usage
vulnerabilities = check_sqli("http://example.com/search", "id")
```

---

## Q5. Write a basic port scanner using asyncio.
**Answer:**
```python
import asyncio
import socket

async def scan_port(host, port, timeout=1):
    """Check if a single port is open"""
    try:
        # Create connection with timeout
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )
        writer.close()
        await writer.wait_closed()
        return (port, True)  # Port is open
    except:
        return (port, False)  # Port is closed

async def scan_all_ports(host, ports):
    """Scan multiple ports concurrently"""
    tasks = [scan_port(host, port) for port in ports]
    results = await asyncio.gather(*tasks)
    
    # Filter only open ports
    open_ports = [port for port, is_open in results if is_open]
    return open_ports

def main():
    host = "scanme.nmap.org"  # Legal test target
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]
    
    # Run async scanner
    open_ports = asyncio.run(scan_all_ports(host, common_ports))
    
    print(f"Open ports on {host}: {open_ports}")

if __name__ == "__main__":
    main()
```

**Why asyncio?**
- Synchronous scanning of 1000 ports: ~16 minutes
- Async scanning of 1000 ports: ~10 seconds
- Your scanner uses this for efficiency!

---

## Q6. How does your StegoCrypt LSB encoding work in Python?
**Answer:**
```python
from PIL import Image

def hide_message(image_path, message, output_path):
    """Hide message in image using LSB steganography"""
    
    # Load image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    
    # Convert message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    binary_message += '1111111111111110'  # Delimiter
    
    data_index = 0
    
    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_message):
                break
            
            pixel = list(pixels[x, y])
            
            # Modify LSB of each color channel (R, G, B)
            for i in range(3):
                if data_index < len(binary_message):
                    # Clear LSB and set to message bit
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                    data_index += 1
            
            pixels[x, y] = tuple(pixel)
    
    img.save(output_path)
    print(f"Message hidden in {output_path}")

def extract_message(image_path):
    """Extract hidden message from image"""
    
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    
    binary_message = ""
    
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            for i in range(3):
                binary_message += str(pixel[i] & 1)
    
    # Find delimiter and convert to text
    delimiter = '1111111111111110'
    end = binary_message.find(delimiter)
    
    if end != -1:
        binary_message = binary_message[:end]
    
    # Convert binary to text
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:
            message += chr(int(byte, 2))
    
    return message
```

---

## Q7. Implement AES encryption in Python (like StegoCrypt).
**Answer:**
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def generate_key_from_password(password: str, salt: bytes = None):
    """Derive AES key from password using PBKDF2"""
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits for AES-256
        salt=salt,
        iterations=100000,
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt_message(message: str, password: str):
    """Encrypt message using AES-256"""
    key, salt = generate_key_from_password(password)
    fernet = Fernet(key)
    
    encrypted = fernet.encrypt(message.encode())
    
    # Return salt + encrypted (both needed for decryption)
    return base64.b64encode(salt + encrypted).decode()

def decrypt_message(encrypted_data: str, password: str):
    """Decrypt message using AES-256"""
    data = base64.b64decode(encrypted_data.encode())
    
    # Extract salt (first 16 bytes)
    salt = data[:16]
    encrypted = data[16:]
    
    key, _ = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    
    decrypted = fernet.decrypt(encrypted)
    return decrypted.decode()

# Example
secret = "Sensitive data"
password = "MySecurePassword123!"

encrypted = encrypt_message(secret, password)
print(f"Encrypted: {encrypted[:50]}...")

decrypted = decrypt_message(encrypted, password)
print(f"Decrypted: {decrypted}")
```

---

## Q8. Write a password strength checker in Python.
**Answer:**
```python
import re

def check_password_strength(password):
    """Evaluate password strength and return score + feedback"""
    
    score = 0
    feedback = []
    
    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    # Character type checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Common pattern checks
    common_patterns = [
        r'123', r'abc', r'qwerty', r'password',
        r'admin', r'letmein', r'welcome'
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            score -= 1
            feedback.append(f"Avoid common pattern: {pattern}")
    
    # Calculate strength level
    if score >= 7:
        strength = "STRONG"
    elif score >= 5:
        strength = "MEDIUM"
    elif score >= 3:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }

# Example
result = check_password_strength("MySecure@Pass123!")
print(f"Strength: {result['strength']}")
print(f"Score: {result['score']}/7")
```

---

## Q9. Write a hash comparison script (useful for file integrity).
**Answer:**
```python
import hashlib
import os

def calculate_file_hash(filepath, algorithm='sha256'):
    """Calculate hash of a file"""
    hash_func = hashlib.new(algorithm)
    
    with open(filepath, 'rb') as f:
        # Read in chunks for large files
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def verify_file_integrity(filepath, expected_hash, algorithm='sha256'):
    """Verify file hasn't been tampered with"""
    actual_hash = calculate_file_hash(filepath, algorithm)
    return actual_hash == expected_hash

def compare_directories(dir1, dir2):
    """Compare file hashes between two directories"""
    differences = []
    
    for root, dirs, files in os.walk(dir1):
        for file in files:
            path1 = os.path.join(root, file)
            path2 = path1.replace(dir1, dir2)
            
            if os.path.exists(path2):
                hash1 = calculate_file_hash(path1)
                hash2 = calculate_file_hash(path2)
                
                if hash1 != hash2:
                    differences.append({
                        'file': file,
                        'hash1': hash1[:16] + "...",
                        'hash2': hash2[:16] + "..."
                    })
            else:
                differences.append({
                    'file': file,
                    'status': 'Missing in dir2'
                })
    
    return differences

# Example
file_hash = calculate_file_hash("important_file.txt")
print(f"SHA-256: {file_hash}")
```

---

## Q10. Write a basic web scraper with security headers check.
**Answer:**
```python
import requests

def check_security_headers(url):
    """Check a website for security headers"""
    
    # Security headers to check
    security_headers = {
        'Strict-Transport-Security': 'HSTS - Forces HTTPS',
        'Content-Security-Policy': 'CSP - Prevents XSS',
        'X-Frame-Options': 'Prevents clickjacking',
        'X-Content-Type-Options': 'Prevents MIME sniffing',
        'X-XSS-Protection': 'XSS filter (legacy)',
        'Referrer-Policy': 'Controls referer info',
        'Permissions-Policy': 'Controls browser features',
        'Cache-Control': 'Cache directives',
        'X-Permitted-Cross-Domain-Policies': 'Flash/PDF policies',
        'Cross-Origin-Embedder-Policy': 'COEP',
        'Cross-Origin-Opener-Policy': 'COOP',
        'Cross-Origin-Resource-Policy': 'CORP'
    }
    
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        results = {
            'url': url,
            'status_code': response.status_code,
            'present': [],
            'missing': []
        }
        
        for header, description in security_headers.items():
            if header in headers:
                results['present'].append({
                    'header': header,
                    'value': headers[header][:50],
                    'description': description
                })
            else:
                results['missing'].append({
                    'header': header,
                    'description': description
                })
        
        return results
        
    except Exception as e:
        return {'error': str(e)}

# Example
results = check_security_headers("https://www.google.com")
print(f"\n{results['url']}")
print(f"Status: {results['status_code']}")
print(f"\nPresent Headers ({len(results['present'])}):")
for h in results['present'][:5]:
    print(f"  ✓ {h['header']}")
print(f"\nMissing Headers ({len(results['missing'])}):")
for h in results['missing'][:5]:
    print(f"  ✗ {h['header']}")
```

---

# SECTION 2: NETWORK SECURITY WITH PYTHON

## Q11. Write a simple packet sniffer in Python.
**Answer:**
```python
import socket
import struct

def sniff_packets():
    """Basic packet sniffer (requires root/admin)"""
    
    # Create raw socket
    # On Windows: use socket.IPPROTO_IP
    # On Linux: use socket.IPPROTO_TCP
    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sniffer.bind(("0.0.0.0", 0))
        
        # Include IP headers
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        
        print("Sniffing packets... (Ctrl+C to stop)")
        
        while True:
            # Receive packet
            raw_data, addr = sniffer.recvfrom(65535)
            
            # Parse IP header (first 20 bytes)
            ip_header = raw_data[:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            
            version = iph[0] >> 4
            protocol = iph[6]
            src_ip = socket.inet_ntoa(iph[8])
            dst_ip = socket.inet_ntoa(iph[9])
            
            print(f"Protocol: {protocol} | {src_ip} -> {dst_ip}")
            
    except PermissionError:
        print("Error: Run with administrator privileges")
    except KeyboardInterrupt:
        print("\nStopped.")

# Note: Requires root/admin privileges
# For ethical use only on authorized networks!
```

---

## Q12. Write a subdomain enumeration script.
**Answer:**
```python
import socket
import concurrent.futures

def check_subdomain(domain, subdomain):
    """Check if subdomain exists"""
    full_domain = f"{subdomain}.{domain}"
    
    try:
        ip = socket.gethostbyname(full_domain)
        return (full_domain, ip)
    except socket.gaierror:
        return None

def enumerate_subdomains(domain, wordlist=None):
    """Find subdomains using dictionary attack"""
    
    # Default common subdomains
    if wordlist is None:
        wordlist = [
            'www', 'mail', 'ftp', 'admin', 'api', 
            'dev', 'test', 'staging', 'beta', 'app',
            'blog', 'shop', 'store', 'portal', 'vpn',
            'cdn', 'static', 'assets', 'img', 'images',
            'mobile', 'm', 'secure', 'login', 'auth',
            'db', 'database', 'backup', 'git', 'jenkins'
        ]
    
    found = []
    
    # Use thread pool for faster enumeration
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {
            executor.submit(check_subdomain, domain, sub): sub 
            for sub in wordlist
        }
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                found.append(result)
                print(f"[+] Found: {result[0]} -> {result[1]}")
    
    return found

# Example
print("Enumerating subdomains for example.com...")
results = enumerate_subdomains("example.com")
print(f"\nTotal found: {len(results)}")
```

---

## Q13. Write a basic banner grabber.
**Answer:**
```python
import socket

def grab_banner(host, port, timeout=5):
    """Grab service banner from open port"""
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        
        # Some services need a request
        if port in [80, 8080]:
            sock.send(b"HEAD / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
        elif port == 25:  # SMTP
            pass  # SMTP sends banner automatically
        elif port == 21:  # FTP
            pass  # FTP sends banner automatically
        
        banner = sock.recv(1024).decode('utf-8', errors='ignore')
        sock.close()
        
        return banner.strip()
        
    except Exception as e:
        return None

def scan_with_banners(host, ports):
    """Scan ports and grab banners"""
    
    results = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            
            result = sock.connect_ex((host, port))
            
            if result == 0:
                banner = grab_banner(host, port)
                results.append({
                    'port': port,
                    'status': 'open',
                    'banner': banner[:100] if banner else 'N/A'
                })
            
            sock.close()
            
        except:
            continue
    
    return results

# Example
results = scan_with_banners("scanme.nmap.org", [22, 80, 443])
for r in results:
    print(f"Port {r['port']}: {r['banner'][:50]}...")
```

---

# SECTION 3: SECURE CODING PRACTICES

## Q14. How do you prevent SQL injection in Python?
**Answer:**
```python
import sqlite3

# ❌ VULNERABLE - String concatenation
def bad_login(username, password):
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    # Attacker input: username = "admin'--"
    # Becomes: SELECT * FROM users WHERE username='admin'--' AND password=''

# ✅ SAFE - Parameterized queries
def safe_login(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    # Parameters are escaped automatically

# ✅ SAFE - ORM (SQLAlchemy)
from sqlalchemy.orm import Session

def orm_login(db: Session, username: str, password: str):
    return db.query(User).filter(
        User.username == username,
        User.password == password
    ).first()
```

---

## Q15. How do you prevent XSS in Python web apps?
**Answer:**
```python
from html import escape
from markupsafe import Markup, escape as markup_escape

# ❌ VULNERABLE - Direct user input in HTML
def bad_greeting(name):
    return f"<h1>Hello, {name}</h1>"
    # Attacker input: name = "<script>alert('XSS')</script>"

# ✅ SAFE - HTML escape user input
def safe_greeting(name):
    return f"<h1>Hello, {escape(name)}</h1>"
    # Output: <h1>Hello, &lt;script&gt;alert('XSS')&lt;/script&gt;</h1>

# ✅ SAFE - Flask auto-escaping in templates (Jinja2)
# templates/greeting.html
# <h1>Hello, {{ name }}</h1>  ← Auto-escaped!

# ✅ Content Security Policy header
def add_csp_header(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

---

## Q16. Secure password handling in Python.
**Answer:**
```python
import bcrypt
import secrets
import hashlib

# ❌ WRONG - Plain MD5
def bad_hash(password):
    return hashlib.md5(password.encode()).hexdigest()
    # Fast, no salt, rainbow table vulnerable

# ✅ CORRECT - bcrypt (what you used in SmartBank!)
def hash_password(password: str) -> bytes:
    """Hash password with bcrypt"""
    salt = bcrypt.gensalt(rounds=12)  # Cost factor 12
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example
password = "MySecurePassword123!"
hashed = hash_password(password)
print(f"Hash: {hashed}")

# Verify
is_valid = verify_password("MySecurePassword123!", hashed)
print(f"Valid: {is_valid}")  # True

is_valid = verify_password("WrongPassword", hashed)
print(f"Valid: {is_valid}")  # False

# ✅ Generate secure random tokens
def generate_token(length=32):
    """Generate cryptographically secure random token"""
    return secrets.token_urlsafe(length)

api_key = generate_token()
print(f"API Key: {api_key}")
```

---

## Q17. Secure file handling in Python.
**Answer:**
```python
import os
import pathlib

# ❌ VULNERABLE - Path traversal
def bad_read_file(filename):
    with open(f"/uploads/{filename}", 'r') as f:
        return f.read()
    # Attacker input: filename = "../../../etc/passwd"

# ✅ SAFE - Sanitize path
def safe_read_file(filename, base_dir="/uploads"):
    """Safely read file preventing path traversal"""
    
    # Get absolute paths
    base = pathlib.Path(base_dir).resolve()
    file_path = pathlib.Path(base_dir, filename).resolve()
    
    # Ensure file is within base directory
    if not str(file_path).startswith(str(base)):
        raise ValueError("Invalid path - possible path traversal attack")
    
    if not file_path.exists():
        raise FileNotFoundError("File not found")
    
    with open(file_path, 'r') as f:
        return f.read()

# ✅ SAFE - Use os.path.basename to get just filename
def sanitize_filename(filename):
    """Remove path components, keep just filename"""
    return os.path.basename(filename)

# ✅ SAFE - Validate extension
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.pdf'}

def validate_extension(filename):
    ext = pathlib.Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"File extension {ext} not allowed")
    return True
```

---

## Q18. Secure API requests in Python.
**Answer:**
```python
import requests
import os
from requests.auth import HTTPBasicAuth

# ❌ WRONG - Hardcoded credentials
def bad_api_call():
    api_key = "sk-12345abcdef"  # Exposed in code!
    requests.get("https://api.example.com", headers={"Authorization": f"Bearer {api_key}"})

# ✅ CORRECT - Environment variables
def secure_api_call():
    api_key = os.environ.get('API_KEY')
    if not api_key:
        raise ValueError("API_KEY environment variable not set")
    
    response = requests.get(
        "https://api.example.com/data",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,  # Always set timeout
        verify=True  # Verify SSL certificates
    )
    
    return response.json()

# ✅ CORRECT - Using .env file with python-dotenv
from dotenv import load_dotenv

load_dotenv()  # Load .env file
api_key = os.getenv('API_KEY')

# ✅ Certificate pinning for high-security
def pinned_request(url):
    # Pin to specific certificate
    response = requests.get(
        url,
        verify='/path/to/certificate.pem'
    )
    return response
```

---

# SECTION 4: YOUR PROJECT CODE EXAMPLES

## Q19. Walk me through your SQLi detection regex.
**Answer:**
```python
import re

# SQL error patterns from your Web Vulnerability Scanner
SQL_ERROR_PATTERNS = [
    # MySQL errors
    r"SQL syntax.*MySQL",
    r"Warning.*mysql_.*",
    r"valid MySQL result",
    r"MySqlClient\.",
    r"MySQL Query fail",
    r"SQL syntax.*MariaDB server",
    
    # PostgreSQL errors
    r"PostgreSQL.*ERROR",
    r"Warning.*\Wpg_.*",
    r"valid PostgreSQL result",
    r"Npgsql\.",
    r"PG::SyntaxError:",
    
    # Microsoft SQL Server
    r"Driver.* SQL[\-\_\ ]*Server",
    r"OLE DB.* SQL Server",
    r"(\W|\A)SQL Server.*Driver",
    r"Warning.*mssql_.*",
    r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}",
    r"\bODBC SQL Server Driver\b",
    
    # Oracle errors
    r"\bORA-\d{5}",
    r"Oracle error",
    r"Oracle.*Driver",
    r"Warning.*\Woci_.*",
    r"Warning.*\Wora_.*",
    
    # SQLite errors
    r"SQLite[\d∗\w]*Error",
    r"Warning.*sqlite_.*",
    r"SQLite.*syntax",
    
    # Generic patterns
    r"unclosed quotation mark",
    r"quoted string not properly terminated",
    r"you have an error in your SQL syntax"
]

def detect_sqli_error(response_text):
    """Check if response contains SQL error indicating vulnerability"""
    
    for pattern in SQL_ERROR_PATTERNS:
        match = re.search(pattern, response_text, re.IGNORECASE)
        if match:
            return {
                'vulnerable': True,
                'pattern_matched': pattern,
                'evidence': match.group(0)
            }
    
    return {'vulnerable': False}

# Example
sample_response = "Error: You have an error in your SQL syntax near 'admin'"
result = detect_sqli_error(sample_response)
print(result)  # {'vulnerable': True, 'pattern_matched': ...}
```

---

## Q20. Explain your StegoCrypt architecture.
**Answer:**
```python
"""
StegoCrypt Architecture:

+-------------------+     +------------------+     +----------------+
|   Input Message   | --> |   AES-256        | --> |    LSB        |
|                   |     |   Encryption     |     |   Encoding    |
+-------------------+     +------------------+     +----------------+
                                  |                        |
                           PBKDF2 Key                Cover Image
                           Derivation                      |
                                  |                        v
                           User Password          Stego Image Output

Decryption Flow (reverse):
+----------------+     +------------------+     +-------------------+
|  Stego Image   | --> |    LSB          | --> |   AES-256        |
|                |     |    Extraction   |     |   Decryption     |
+----------------+     +------------------+     +-------------------+
                                                        |
                                                        v
                                                 Original Message
"""

class StegoCrypt:
    def __init__(self, password: str):
        self.password = password
        self.salt = None
    
    def _derive_key(self, salt: bytes = None):
        """Derive AES key from password using PBKDF2"""
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        import os
        import base64
        
        if salt is None:
            salt = os.urandom(16)
        self.salt = salt
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        return key
    
    def _encrypt(self, message: str) -> bytes:
        """Encrypt message with AES-256"""
        from cryptography.fernet import Fernet
        
        key = self._derive_key()
        fernet = Fernet(key)
        return self.salt + fernet.encrypt(message.encode())
    
    def _lsb_hide(self, image_path: str, data: bytes, output_path: str):
        """Hide encrypted data in image using LSB"""
        from PIL import Image
        
        img = Image.open(image_path)
        pixels = img.load()
        
        # Convert data to binary
        binary = ''.join(format(byte, '08b') for byte in data)
        binary += '1111111111111110'  # Delimiter
        
        idx = 0
        for y in range(img.height):
            for x in range(img.width):
                if idx >= len(binary):
                    break
                pixel = list(pixels[x, y])
                for i in range(3):  # R, G, B
                    if idx < len(binary):
                        pixel[i] = (pixel[i] & ~1) | int(binary[idx])
                        idx += 1
                pixels[x, y] = tuple(pixel)
        
        img.save(output_path)
    
    def hide(self, message: str, image_path: str, output_path: str):
        """Main method: encrypt and hide message"""
        encrypted = self._encrypt(message)
        self._lsb_hide(image_path, encrypted, output_path)
        print(f"Message hidden in {output_path}")
    
    # Similar extract methods for decryption...
```

---

# SECTION 5: COMMON INTERVIEW SCENARIOS

## Q21. "Write a script to bruteforce a login page."
**Answer:** *(For authorized testing only!)*
```python
import requests
from concurrent.futures import ThreadPoolExecutor

def bruteforce_login(url, username, password_list, csrf_token_field=None):
    """
    Bruteforce login form
    NOTE: For authorized penetration testing only!
    """
    
    session = requests.Session()
    
    def try_password(password):
        # Get fresh page (for CSRF token if needed)
        response = session.get(url)
        
        # Extract CSRF token if used
        csrf_token = None
        if csrf_token_field:
            import re
            match = re.search(f'name="{csrf_token_field}" value="([^"]+)"', response.text)
            if match:
                csrf_token = match.group(1)
        
        # Prepare payload
        payload = {
            'username': username,
            'password': password
        }
        if csrf_token:
            payload[csrf_token_field] = csrf_token
        
        # Attempt login
        response = session.post(url, data=payload)
        
        # Check for success indicators
        if 'Invalid' not in response.text and 'incorrect' not in response.text.lower():
            return password
        return None
    
    # Try each password
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(try_password, password_list)
        for result in results:
            if result:
                return result
    
    return None

# Usage (authorized testing only!)
# passwords = ['password123', 'admin', 'letmein', ...]
# result = bruteforce_login('https://test.com/login', 'admin', passwords)
```

---

## Q22. "How would you detect if a file is malicious?"
**Answer:**
```python
import hashlib
import os
import magic  # python-magic library

def analyze_file(filepath):
    """Basic malware analysis of a file"""
    
    analysis = {
        'filename': os.path.basename(filepath),
        'size': os.path.getsize(filepath),
        'indicators': []
    }
    
    # 1. Check hash against known malware (would query VirusTotal API)
    with open(filepath, 'rb') as f:
        content = f.read()
        analysis['md5'] = hashlib.md5(content).hexdigest()
        analysis['sha256'] = hashlib.sha256(content).hexdigest()
    
    # 2. Check file type vs extension mismatch
    mime = magic.Magic(mime=True)
    detected_type = mime.from_file(filepath)
    analysis['mime_type'] = detected_type
    
    # Extension mismatch (hiding executables)
    ext = os.path.splitext(filepath)[1].lower()
    if detected_type == 'application/x-executable' and ext in ['.jpg', '.pdf', '.txt']:
        analysis['indicators'].append('SUSPICIOUS: Executable masquerading as document')
    
    # 3. Check for suspicious strings
    suspicious_strings = [
        b'cmd.exe', b'powershell', b'/bin/sh', b'/bin/bash',
        b'CreateProcess', b'VirtualAlloc', b'WriteProcessMemory',
        b'socket', b'connect', b'recv', b'send',
        b'RegSetValue', b'HKEY_', b'autorun',
        b'base64', b'eval(', b'exec('
    ]
    
    for s in suspicious_strings:
        if s in content:
            analysis['indicators'].append(f'Found suspicious string: {s.decode()}')
    
    # 4. High entropy (possible encryption/packing)
    import math
    entropy = calculate_entropy(content)
    analysis['entropy'] = entropy
    if entropy > 7.5:
        analysis['indicators'].append('HIGH ENTROPY: Possibly encrypted/packed')
    
    return analysis

def calculate_entropy(data):
    """Calculate Shannon entropy of data"""
    import math
    from collections import Counter
    
    if not data:
        return 0
    
    counter = Counter(data)
    length = len(data)
    
    entropy = 0
    for count in counter.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
    
    return entropy

# Example
# result = analyze_file("suspicious_file.exe")
# print(result)
```

---

## Q23. Write a log analyzer for security events.
**Answer:**
```python
import re
from collections import Counter
from datetime import datetime

def analyze_auth_log(log_path):
    """Analyze authentication logs for security events"""
    
    analysis = {
        'failed_logins': [],
        'successful_logins': [],
        'brute_force_suspects': [],
        'suspicious_ips': Counter()
    }
    
    # Patterns for auth.log / secure log
    patterns = {
        'failed_ssh': r'Failed password for (\w+) from ([\d.]+)',
        'failed_invalid': r'Invalid user (\w+) from ([\d.]+)',
        'success': r'Accepted password for (\w+) from ([\d.]+)',
        'timestamp': r'^(\w{3}\s+\d+\s+\d+:\d+:\d+)'
    }
    
    with open(log_path, 'r') as f:
        for line in f:
            # Check for failed logins
            match = re.search(patterns['failed_ssh'], line)
            if match:
                user, ip = match.groups()
                timestamp = re.search(patterns['timestamp'], line)
                analysis['failed_logins'].append({
                    'user': user,
                    'ip': ip,
                    'time': timestamp.group(1) if timestamp else 'unknown'
                })
                analysis['suspicious_ips'][ip] += 1
            
            # Check for invalid users (enumeration attempt)
            match = re.search(patterns['failed_invalid'], line)
            if match:
                user, ip = match.groups()
                analysis['failed_logins'].append({
                    'user': user,
                    'ip': ip,
                    'type': 'invalid_user'
                })
                analysis['suspicious_ips'][ip] += 1
            
            # Check for successful logins
            match = re.search(patterns['success'], line)
            if match:
                user, ip = match.groups()
                analysis['successful_logins'].append({
                    'user': user,
                    'ip': ip
                })
    
    # Identify brute force attempts (>5 failures from same IP)
    for ip, count in analysis['suspicious_ips'].items():
        if count >= 5:
            analysis['brute_force_suspects'].append({
                'ip': ip,
                'failed_attempts': count
            })
    
    return analysis

# Summary report
def generate_report(analysis):
    print("=" * 50)
    print("SECURITY LOG ANALYSIS REPORT")
    print("=" * 50)
    print(f"\nTotal failed logins: {len(analysis['failed_logins'])}")
    print(f"Total successful logins: {len(analysis['successful_logins'])}")
    print(f"\nBrute Force Suspects:")
    for suspect in analysis['brute_force_suspects']:
        print(f"  ⚠️  {suspect['ip']}: {suspect['failed_attempts']} failures")
    
    print(f"\nTop 5 Suspicious IPs:")
    for ip, count in analysis['suspicious_ips'].most_common(5):
        print(f"  {ip}: {count} events")
```

---

# SECTION 6: QUICK REFERENCE

## Key Security Libraries
```python
# Web Requests & Scraping
import requests           # HTTP library
from bs4 import BeautifulSoup  # HTML parsing

# Cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import hashlib
import bcrypt             # Password hashing

# Network
import socket             # Raw sockets
import ssl                # SSL/TLS
import paramiko           # SSH

# Image Processing (Steganography)
from PIL import Image     # Pillow

# Async
import asyncio
import aiohttp            # Async HTTP

# Data
import json
import base64
import struct

# System
import os
import subprocess
import platform
```

## Security Code Patterns
```python
# ✓ Always validate input
# ✓ Use parameterized queries
# ✓ Hash passwords with bcrypt
# ✓ Use environment variables for secrets
# ✓ Set timeouts on network requests
# ✓ Validate file paths (prevent traversal)
# ✓ Use HTTPS and verify certificates
# ✓ Log security events
# ✓ Handle exceptions gracefully
# ✗ Never log passwords
# ✗ Never hardcode credentials
# ✗ Never trust user input
# ✗ Never use MD5/SHA1 for passwords
```

---

# 📌 FINAL TIPS

1. **Connect to your projects** - "In my Web Scanner, I used..." or "StegoCrypt implements..."
2. **Explain the WHY** - Why bcrypt? Why async? Why LSB?
3. **Think security-first** - Always mention input validation, error handling
4. **Know the libraries** - requests, bcrypt, cryptography, asyncio
5. **Write clean code** - Use functions, handle exceptions, add comments

---

*Good luck with your interview, Gaurab! 🚀*
*February 26, 2026 | 9:00 AM*
