# 🔐 OWASP TOP 10 - 100 Interview Q&A

## Priority Levels
- 🔴 **Most Probable (Q1-40)**: Frequently asked in interviews
- 🟡 **Complex (Q41-70)**: Technical depth required
- 🟢 **In-Depth/Scenario (Q71-100)**: Advanced scenarios & practical

---

# 🔴 MOST PROBABLE QUESTIONS (1-40)

## Q1: What is OWASP?
**Answer:** OWASP (Open Web Application Security Project) is a nonprofit foundation that works to improve software security. They provide:
- Free security tools and resources
- Community-led projects
- Standards and guidelines (OWASP Top 10)
- Training and certifications
- Conferences worldwide

The OWASP Top 10 is their most well-known publication, listing critical web application security risks.

---

## Q2: What is the OWASP Top 10 2021? List all categories.
**Answer:**
1. **A01: Broken Access Control** - Unauthorized access to resources
2. **A02: Cryptographic Failures** - Weak/missing encryption
3. **A03: Injection** - SQL, NoSQL, command injection
4. **A04: Insecure Design** - Missing security controls in design
5. **A05: Security Misconfiguration** - Default configs, unnecessary features
6. **A06: Vulnerable Components** - Using components with known vulnerabilities
7. **A07: Identification and Authentication Failures** - Weak auth
8. **A08: Software and Data Integrity Failures** - Untrusted updates
9. **A09: Security Logging and Monitoring Failures** - Insufficient logging
10. **A10: Server-Side Request Forgery (SSRF)** - Server makes unintended requests

---

## Q3: What is Broken Access Control?
**Answer:** Broken Access Control occurs when users can act outside their intended permissions:
- Accessing other users' data (IDOR)
- Performing admin functions as regular user
- Modifying access control tokens
- Bypassing access checks via URL manipulation

**Example:** Changing `?user_id=123` to `?user_id=456` to access another user's data.

**Prevention:** Server-side enforcement, deny by default, RBAC, logging access failures.

---

## Q4: Explain IDOR (Insecure Direct Object Reference).
**Answer:** IDOR occurs when application exposes internal object references (IDs) that can be manipulated to access unauthorized resources.

**Example:**
```
https://example.com/invoice?id=12345
# Attacker changes to:
https://example.com/invoice?id=12346
```

**Prevention:**
- Server-side authorization checks
- Use indirect references (random tokens)
- Check user permissions for every request
- Avoid predictable IDs in URLs

---

## Q5: What is SQL Injection?
**Answer:** SQL Injection occurs when untrusted input is incorporated into SQL queries, allowing attackers to:
- Extract data
- Modify/delete data
- Bypass authentication
- Execute admin operations

**Example:**
```sql
# User input: ' OR '1'='1
SELECT * FROM users WHERE username='admin' AND password='' OR '1'='1'
# Always returns true!
```

**Prevention:** Parameterized queries, stored procedures, input validation, least privilege DB accounts.

---

## Q6: What are parameterized queries? Why are they important?
**Answer:** Parameterized queries (prepared statements) separate SQL logic from data. The database treats parameters as data, never as executable code.

**Vulnerable:**
```python
query = "SELECT * FROM users WHERE id = " + user_input
```

**Safe (Parameterized):**
```python
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_input,))
```

**Why important:** Completely prevents SQL injection because user input cannot alter query structure.

---

## Q7: What is Cross-Site Scripting (XSS)?
**Answer:** XSS is an injection attack where malicious scripts are injected into trusted websites.

**Types:**
- **Stored XSS:** Script saved in database, served to all users
- **Reflected XSS:** Script in URL, reflected in response
- **DOM-based XSS:** Script manipulates client-side DOM

**Impact:** Session hijacking, defacement, credential theft, malware distribution.

**Prevention:** Output encoding, CSP, input validation, HttpOnly cookies.

---

## Q8: What is the difference between Stored, Reflected, and DOM XSS?
**Answer:**
| Type | Storage | Delivery | Example |
|------|---------|----------|---------|
| **Stored** | Server/DB | Via application | Comment with script saved in DB |
| **Reflected** | None | Via URL | Malicious link with script in parameter |
| **DOM-based** | None | Client-side | Client JS writes URL param to page |

**Severity:** Stored > Reflected > DOM (generally)

Stored affects all users; Reflected requires victim to click link.

---

## Q9: How do you prevent XSS?
**Answer:**
1. **Output Encoding:** Context-aware encoding (HTML, JS, URL, CSS)
2. **Content Security Policy (CSP):** Restrict script sources
3. **Input Validation:** Whitelist allowed characters
4. **HttpOnly Cookies:** Prevent JS access to session cookies
5. **X-XSS-Protection Header:** Browser-side filtering (legacy)
6. **Use frameworks:** Modern frameworks auto-escape by default
7. **Avoid dangerous sinks:** innerHTML, eval(), document.write()

---

## Q10: What is CSRF (Cross-Site Request Forgery)?
**Answer:** CSRF tricks authenticated users into performing unwanted actions on sites where they're logged in.

**Example:** Malicious page contains:
```html
<img src="https://bank.com/transfer?to=attacker&amount=10000">
```
If user is logged into bank.com, transfer executes.

**Prevention:**
- CSRF tokens (random, unique per session)
- SameSite cookie attribute
- Verify origin/referer headers
- Re-authentication for sensitive actions

---

## Q11: What is the difference between XSS and CSRF?
**Answer:**
| XSS | CSRF |
|-----|------|
| Injects malicious script | Tricks user into making request |
| Exploits trust site has in user | Exploits trust user has in site |
| Steals data, hijacks session | Performs unwanted actions |
| Victim's browser runs attacker's code | Victim's browser makes attacker's request |
| Prevention: Output encoding, CSP | Prevention: CSRF tokens |

---

## Q12: What are Cryptographic Failures?
**Answer:** Previously "Sensitive Data Exposure" - failures to properly protect data:
- Data transmitted in cleartext
- Outdated/weak encryption algorithms (MD5, DES)
- Improper key management
- Missing encryption for sensitive data
- Weak password storage

**Prevention:** Encrypt data in transit (TLS), encrypt at rest (AES-256), use strong hashing for passwords (bcrypt, Argon2), proper key management.

---

## Q13: What is the difference between encryption and hashing?
**Answer:**
| Encryption | Hashing |
|------------|---------|
| Reversible with key | One-way (irreversible) |
| Protects confidentiality | Verifies integrity |
| For data that needs decryption | For passwords, file verification |
| AES, RSA | SHA-256, bcrypt |

**Use encryption for:** Files, communications, sensitive data
**Use hashing for:** Password storage, integrity checks

---

## Q14: What is Security Misconfiguration?
**Answer:** Insecure settings in applications, frameworks, servers:
- Default credentials unchanged
- Unnecessary features enabled
- Error messages revealing stack traces
- Missing security headers
- Outdated software
- Open cloud storage buckets

**Prevention:** Hardening process, disable unused features, minimal installation, automated scanning, regular updates.

---

## Q15: What are common security headers and their purpose?
**Answer:**
| Header | Purpose |
|--------|---------|
| **Strict-Transport-Security (HSTS)** | Forces HTTPS |
| **Content-Security-Policy (CSP)** | Controls resource loading |
| **X-Content-Type-Options** | Prevents MIME sniffing |
| **X-Frame-Options** | Prevents clickjacking |
| **X-XSS-Protection** | XSS filtering (deprecated) |
| **Referrer-Policy** | Controls referer header |
| **Permissions-Policy** | Restricts browser features |

---

## Q16: What is the Vulnerable and Outdated Components category?
**Answer:** Using components (libraries, frameworks) with known vulnerabilities:
- Outdated software versions
- Unmaintained libraries
- Third-party code without security review

**Impact:** Inherited vulnerabilities from dependencies.

**Prevention:**
- Regular dependency scanning
- Software Composition Analysis (SCA)
- Monitor CVEs for used components
- Automated update processes

---

## Q17: What is Software Composition Analysis (SCA)?
**Answer:** SCA tools analyze third-party components in your application:
- Identify all dependencies
- Check for known vulnerabilities (CVEs)
- License compliance
- Version tracking

**Tools:** Snyk, OWASP Dependency-Check, Dependabot, Mend (WhiteSource).

SCA should be part of CI/CD pipeline.

---

## Q18: What is Identification and Authentication Failures?
**Answer:** Weaknesses in confirming user identity:
- Permits weak passwords
- No MFA
- Credential stuffing attacks
- Session ID in URL
- Session doesn't expire
- Improper session management

**Prevention:** Strong password policies, MFA, rate limiting, secure session management, no session ID in URL.

---

## Q19: What is credential stuffing?
**Answer:** Automated attack using stolen username/password pairs from data breaches to access other services.

**How it works:**
1. Attacker obtains leaked credentials
2. Uses bots to try credentials on multiple sites
3. Exploits password reuse

**Prevention:** MFA, rate limiting, CAPTCHA, breach password detection, anomaly detection.

---

## Q20: What are Software and Data Integrity Failures?
**Answer:** Code and infrastructure not protected against integrity violations:
- Insecure CI/CD pipeline
- Auto-updates without verification
- Unsigned software packages
- Deserialization of untrusted data

**Examples:** SolarWinds attack, npm package hijacking.

**Prevention:** Digital signatures, code signing, integrity checks, secure CI/CD, verify update sources.

---

## Q21: What is Insecure Deserialization?
**Answer:** Deserializing untrusted data can lead to:
- Remote code execution
- Privilege escalation
- Injection attacks
- DoS

**Example (Java):**
```java
ObjectInputStream ois = new ObjectInputStream(userInputStream);
Object obj = ois.readObject(); // Dangerous!
```

**Prevention:** Don't deserialize untrusted data, use JSON instead of native serialization, validate input, whitelist classes.

---

## Q22: What is Security Logging and Monitoring Failures?
**Answer:** Insufficient logging and monitoring allows attackers to:
- Go undetected
- Persist in systems
- Achieve objectives without alerts

**Failures:**
- Not logging login failures
- No alerting on suspicious activity
- Logs only stored locally
- No log integrity protection

**Prevention:** Log security events, centralize logs, alert on anomalies, incident response plan, regular log review.

---

## Q23: What should be logged from a security perspective?
**Answer:**
**Must log:**
- Authentication events (success/failure)
- Authorization failures
- Input validation failures
- Application errors
- Sensitive actions (money transfers, data changes)
- Admin actions

**Never log:**
- Passwords
- API keys/secrets
- Full credit card numbers
- PII (minimize)

**Log format:** Timestamp, user, action, outcome, source IP.

---

## Q24: What is Server-Side Request Forgery (SSRF)?
**Answer:** SSRF occurs when an attacker can make the server perform requests to unintended locations.

**Example:**
```
GET /fetch?url=http://internal-server:8080/admin
```

**Impact:**
- Access internal services
- Read cloud metadata (169.254.169.254)
- Port scanning
- Bypass firewalls

**Prevention:** Whitelist URLs, block private IP ranges, validate user input, limit URL schemes.

---

## Q25: What is Insecure Design?
**Answer:** Fundamental flaws in application design, not implementation bugs:
- Missing security controls in design phase
- Business logic flaws
- Insufficient threat modeling
- Lack of security requirements

**Example:** Password recovery asks security questions that can be found on social media.

**Prevention:** Threat modeling, security requirements, secure design patterns, security in SDLC.

---

## Q26: What is the difference between Insecure Design and Security Misconfiguration?
**Answer:**
| Insecure Design | Security Misconfiguration |
|-----------------|---------------------------|
| Flaw in design phase | Flaw in deployment/config |
| Missing security control | Poorly configured control |
| Needs redesign to fix | Can fix with configuration |
| Example: No rate limiting designed | Example: Rate limiting disabled |

Insecure design = built wrong. Misconfiguration = configured wrong.

---

## Q27: What is Command Injection?
**Answer:** Executing arbitrary commands on the host OS via application.

**Example:**
```python
os.system("ping " + user_input)
# User input: "localhost; rm -rf /"
```

**Prevention:**
- Avoid shell commands
- Use parameterized APIs
- Input validation/whitelist
- Least privilege execution

---

## Q28: What is LDAP Injection?
**Answer:** Manipulating LDAP queries via user input.

**Example:**
```
username: admin)(&(password=*)
```

**Impact:** Authentication bypass, data disclosure.

**Prevention:** Input validation, escape special characters, use parameterized LDAP.

---

## Q29: What is XML External Entity (XXE)?
**Answer:** Exploiting vulnerable XML parsers to:
- Read local files
- Perform SSRF
- Execute remote code

**Example:**
```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<user>&xxe;</user>
```

**Prevention:** Disable DTD processing, disable external entities, use JSON instead.

---

## Q30: What is path/directory traversal?
**Answer:** Accessing files outside intended directory using `../` sequences.

**Example:**
```
https://example.com/file?name=../../../etc/passwd
```

**Prevention:** Validate input, canonicalize paths, chroot/jail, whitelist allowed files.

---

## Q31: What is clickjacking?
**Answer:** Tricking users into clicking hidden elements by overlaying transparent iframes.

**Attack:** Attacker embeds target site in invisible iframe, user clicks thinking they're on attacker's page.

**Prevention:**
- X-Frame-Options: DENY or SAMEORIGIN
- Content-Security-Policy: frame-ancestors 'self'
- Frame-busting scripts (less reliable)

---

## Q32: What is HTTP response splitting?
**Answer:** Injecting headers by inserting CRLF (`\r\n`) characters.

**Example:**
```
GET /redirect?url=http://evil.com%0d%0aSet-Cookie:session=attacker
```

**Impact:** XSS, cache poisoning, session hijacking.

**Prevention:** Input validation, encode CR/LF characters.

---

## Q33: What is an open redirect vulnerability?
**Answer:** Application redirects to URL from user input without validation.

**Example:**
```
https://trusted.com/redirect?url=https://evil.com
```

**Impact:** Phishing attacks, credential theft (users trust original domain).

**Prevention:** Whitelist redirect destinations, validate against allowed domains, avoid user-controlled redirects.

---

## Q34: What is HTTP Parameter Pollution?
**Answer:** Submitting multiple parameters with same name to bypass security controls.

**Example:**
```
https://example.com/transfer?amount=100&amount=10000
```

Different servers handle duplicates differently (first wins, last wins, concatenate).

**Prevention:** Consistent parameter handling, validation, WAF rules.

---

## Q35: What is session fixation?
**Answer:** Attacker sets known session ID for victim before authentication.

**Steps:**
1. Attacker gets valid session ID
2. Tricks victim to use that session ID
3. Victim authenticates
4. Attacker hijacks authenticated session

**Prevention:** Regenerate session ID after authentication, don't accept session IDs from URLs.

---

## Q36: What is the Content-Security-Policy (CSP) header?
**Answer:** CSP restricts resource loading to prevent XSS and data injection.

**Example:**
```
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com
```

**Directives:**
- `default-src`: Default policy
- `script-src`: Script sources
- `style-src`: Stylesheet sources
- `img-src`: Image sources
- `report-uri`: Report violations

---

## Q37: What is a WAF (Web Application Firewall)?
**Answer:** Layer 7 firewall that filters HTTP traffic based on rules.

**Protects against:**
- SQL injection
- XSS
- CSRF
- DDoS
- OWASP Top 10 threats

**Modes:** Detection (logging), Prevention (blocking).

**Examples:** AWS WAF, Cloudflare, ModSecurity.

---

## Q38: What is rate limiting and why is it important?
**Answer:** Controlling number of requests from a user/IP over time.

**Prevents:**
- Brute force attacks
- Credential stuffing
- DoS attacks
- API abuse

**Implementation:**
- Per IP, per user, per API key
- Return 429 Too Many Requests
- Use sliding window or token bucket algorithms

---

## Q39: What is business logic vulnerability?
**Answer:** Flaws in application logic that can be exploited, not technical bugs.

**Examples:**
- Using coupon code multiple times
- Money transfer with negative amount (crediting instead)
- Skipping checkout steps

**Prevention:** Security review of business flows, threat modeling, proper state management.

---

## Q40: What are security testing methodologies for web applications?
**Answer:**
1. **SAST (Static):** Analyze source code
2. **DAST (Dynamic):** Test running application
3. **IAST (Interactive):** Instrument application during testing
4. **Penetration Testing:** Manual expert testing
5. **Bug Bounty:** Crowdsourced testing

**Framework:** OWASP Testing Guide, OWASP ASVS (Application Security Verification Standard).

---

# 🟡 COMPLEX QUESTIONS (41-70)

## Q41: Explain Blind SQL Injection with examples.
**Answer:** Attacker can execute SQL injection but doesn't see results directly.

**Types:**

**Boolean-based:**
```sql
# If page loads differently when TRUE:
?id=1 AND 1=1  (TRUE - normal page)
?id=1 AND 1=2  (FALSE - different page)
```

**Time-based:**
```sql
?id=1; IF(1=1, WAITFOR DELAY '0:0:5')
# Page loads slowly = TRUE
```

**Method:** Extract data bit by bit based on application behavior.

**Prevention:** Same as regular SQL injection - parameterized queries.

---

## Q42: What is Second-Order SQL Injection?
**Answer:** SQL injection where payload is stored and executed later.

**Example:**
1. User registers with username: `admin'--`
2. Application stores in database
3. Later, admin function queries: `SELECT * FROM users WHERE username='admin'--'`
4. Injection executes

**Prevention:** Parameterized queries everywhere, not just at input.

---

## Q43: How would you bypass WAF for SQL injection?
**Answer:** (For testing/understanding - not malicious use)

**Techniques:**
- **Encoding:** `%27` for `'`, `%00` null bytes
- **Case variation:** `SeLeCt`, `UniOn`
- **Comments:** `/**/`, `/*!50000SELECT*/`
- **Alternative syntax:** `||` instead of `CONCAT`
- **Whitespace variants:** `SELECT%09*%09FROM`
- **HTTP Parameter Pollution**

**Why this matters:** Understanding helps build better WAF rules.

---

## Q44: Explain DOM-based XSS in detail with examples.
**Answer:** Client-side JavaScript handles user input unsafely.

**Example:**
```javascript
// URL: example.com/page#<script>alert(1)</script>
var hash = location.hash.substring(1);
document.getElementById('content').innerHTML = hash; // Vulnerable!
```

**Sources (dangerous input):**
- `location.href`, `location.hash`
- `document.referrer`
- `window.name`

**Sinks (dangerous output):**
- `innerHTML`, `outerHTML`
- `eval()`, `setTimeout(string)`
- `document.write()`

**Prevention:** Avoid dangerous sinks, use textContent instead of innerHTML.

---

## Q45: How do you implement a secure CSP policy?
**Answer:**
**Start restrictive:**
```
Content-Security-Policy: 
  default-src 'self';
  script-src 'self';
  style-src 'self';
  img-src 'self' https://cdn.example.com;
  connect-src 'self';
  font-src 'self';
  frame-ancestors 'none';
  form-action 'self';
  base-uri 'self';
  report-uri /csp-report
```

**Steps:**
1. Start with `report-only` mode
2. Monitor violations
3. Adjust policy based on legitimate needs
4. Move to enforcement

**Avoid:** `'unsafe-inline'`, `'unsafe-eval'` when possible.

---

## Q46: What is template injection and its types?
**Answer:** Injecting code into template engines.

**Server-Side Template Injection (SSTI):**
```python
# User input directly in template
render_template_string(user_input)

# Payload: {{7*7}} → Shows 49
# RCE: {{config.__class__.__init__.__globals__['os'].popen('id').read()}}
```

**Client-Side Template Injection (CSTI):**
AngularJS, Vue.js client-side template engines.

**Prevention:** Never render user input as template, use sandboxed templates.

---

## Q47: Explain JWT attacks and how to prevent them.
**Answer:**
**Attacks:**
1. **Algorithm confusion:** Change `alg` to `none` or HS256→RS256
2. **Weak secret:** Brute force HMAC secret
3. **Token capture:** Steal and reuse tokens
4. **No expiration check**
5. **Information disclosure:** Sensitive data in payload

**Prevention:**
- Whitelist algorithms server-side
- Use strong secrets (256+ bits)
- Short expiration times
- HTTPS only
- Don't store sensitive data in payload
- Implement token revocation

---

## Q48: What is Mass Assignment vulnerability?
**Answer:** Application allows users to modify object properties they shouldn't have access to.

**Example:**
```json
// User sends:
{
  "email": "user@example.com",
  "role": "admin"  // Shouldn't be allowed!
}
```

**Prevention:**
- Whitelist allowed fields
- Use DTOs (Data Transfer Objects)
- Don't bind request directly to database objects
- Explicit field assignment

---

## Q49: Explain HTTP Request Smuggling.
**Answer:** Desynchronization between front-end and back-end servers in interpreting HTTP request boundaries.

**Techniques:**
- CL.TE: Front-end uses Content-Length, back-end uses Transfer-Encoding
- TE.CL: Opposite

**Impact:**
- Bypass security controls
- Cache poisoning
- Session hijacking

**Prevention:** Use HTTP/2 end-to-end, normalize parsing, disable connection reuse.

---

## Q50: What is Prototype Pollution in JavaScript?
**Answer:** Attacker modifies Object.prototype, affecting all JavaScript objects.

**Example:**
```javascript
// Vulnerable merge function
merge({}, JSON.parse('{"__proto__":{"admin":true}}'))

// Now all objects have admin: true
let obj = {};
console.log(obj.admin); // true
```

**Impact:** XSS, authentication bypass, RCE.

**Prevention:** Use `Object.create(null)`, validate input keys, freeze prototypes.

---

## Q51: How would you test for SSRF vulnerabilities?
**Answer:**
**Tests:**
1. Internal IP access: `http://127.0.0.1`, `http://localhost`, `http://192.168.x.x`
2. AWS metadata: `http://169.254.169.254/latest/meta-data/`
3. DNS rebinding: Use Burp Collaborator
4. URL encoding bypass: `http://127.1`, `http://2130706433`
5. Protocol smuggling: `gopher://`, `file:///`

**Look for:** URL parameters for images, webhooks, imports.

**Blind SSRF:** Use out-of-band detection (Burp Collaborator).

---

## Q52: What is NoSQL Injection?
**Answer:** Injection attacks against NoSQL databases (MongoDB, Redis).

**Example (MongoDB):**
```javascript
// User input: {"$gt": ""}
db.users.find({username: input, password: {"$gt": ""}})
// Returns users if password is greater than empty string (all)
```

**Operators abused:** `$ne`, `$gt`, `$regex`, `$where`

**Prevention:** Input validation, parameterized queries, disable JavaScript execution.

---

## Q53: Explain OAuth 2.0 security vulnerabilities.
**Answer:**
1. **Authorization code interception:** Use PKCE
2. **Open redirect:** Validate redirect_uri exactly
3. **CSRF in OAuth flow:** Use state parameter
4. **Token leakage via referrer:** Use fragment for tokens
5. **Scope overreach:** Request minimal scopes
6. **Client secret exposure:** Don't embed in mobile apps

**Mitigations:** PKCE, strict redirect validation, state parameter, short-lived tokens.

---

## Q54: What is account enumeration and how to prevent it?
**Answer:** Attacker determines valid usernames from application responses.

**Indicators:**
- Different error messages ("Invalid username" vs "Invalid password")
- Different response times
- Password reset confirms email exists

**Prevention:**
- Generic error messages: "Invalid credentials"
- Consistent response times
- CAPTCHA on login
- Don't confirm email existence in password reset

---

## Q55: Explain Cache Poisoning attacks.
**Answer:** Attacker injects malicious content into cache served to other users.

**Types:**
1. **Web cache poisoning:** Unkeyed headers affect cached response
2. **DNS cache poisoning:** Corrupt DNS resolver cache

**Example (Web):** `X-Forwarded-Host` header with malicious domain, cached, served to others.

**Impact:** XSS to all users, credential theft.

**Prevention:** Don't cache responses with dynamic headers, validate all inputs, proper cache keys.

---

## Q56: What is Host Header Injection?
**Answer:** Manipulating Host header to:
- Password reset link poisoning
- Cache poisoning
- SSRF via Host header
- Access virtual hosts

**Example:**
```
POST /reset-password HTTP/1.1
Host: attacker.com  # Password reset link uses this
```

**Prevention:** Validate Host header against whitelist, don't use Host header in absolute URLs.

---

## Q57: Explain Race Condition vulnerabilities in web applications.
**Answer:** Time-of-check to time-of-use (TOCTOU) issues.

**Examples:**
- Redeem coupon multiple times by sending concurrent requests
- Transfer more money than available (check balance, transfer - async)
- Follow user multiple times

**Testing:** Burp Intruder with concurrent requests, Turbo Intruder.

**Prevention:** Database transactions, row-level locking, atomic operations, idempotency keys.

---

## Q58: What is subdomain takeover?
**Answer:** Claiming control of abandoned subdomains pointing to external services.

**Example:**
1. Company sets `blog.company.com` → GitHub Pages
2. GitHub repo deleted but DNS still points to GitHub
3. Attacker creates GitHub repo claiming subdomain
4. Attacker controls `blog.company.com`

**Impact:** Phishing, stealing cookies, reputation damage.

**Prevention:** Regular DNS audits, remove unused records, use CNAME verification.

---

## Q59: Explain WebSocket security concerns.
**Answer:**
**Vulnerabilities:**
- Cross-Site WebSocket Hijacking (CSWSH)
- Origin header bypass
- Missing authentication per message
- Injection through messages

**Prevention:**
- Validate Origin header
- Authenticate at connection and per message
- Use WSS (WebSocket Secure)
- Input validation on messages
- Implement proper authorization

---

## Q60: What is GraphQL security? Common vulnerabilities?
**Answer:**
**Vulnerabilities:**
1. **Introspection:** Reveals entire schema
2. **Excessive queries:** Nested queries cause DoS
3. **Injection in arguments**
4. **Broken authorization:** Query any data
5. **Batching attacks:** Multiple operations abuse

**Prevention:**
- Disable introspection in production
- Query depth/complexity limits
- Input validation
- Proper authorization per resolver
- Rate limiting

---

## Q61: Explain Server-Side Includes (SSI) Injection.
**Answer:** Injecting SSI directives into pages that process them.

**Payload:**
```
<!--#exec cmd="ls" -->
<!--#include virtual="/etc/passwd" -->
```

**Impact:** File inclusion, command execution.

**Prevention:** Disable SSI, input validation, proper encoding.

---

## Q62: What is CRLF Injection and its impacts?
**Answer:** Injecting Carriage Return Line Feed characters (%0d%0a) to:
- HTTP Response Splitting
- Log injection
- Header manipulation

**Example:**
```
?redirect=%0d%0aSet-Cookie:%20admin=true
```

**Impact:** XSS, cache poisoning, session fixation.

**Prevention:** Strip or encode CR/LF in inputs.

---

## Q63: Explain XML Injection vs XXE.
**Answer:**
**XML Injection:** Manipulating XML structure
```xml
<user><name>admin</name><role>user</role></user>
# Input: admin</name><role>admin
```

**XXE:** Exploiting XML parser external entity processing
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
```

**Prevention:** Input validation (XML Injection), disable DTD/external entities (XXE).

---

## Q64: What is CORS misconfiguration?
**Answer:** Cross-Origin Resource Sharing improperly configured allowing unauthorized cross-origin access.

**Dangerous configurations:**
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

**Impact:** Data theft via malicious website.

**Prevention:**
- Whitelist specific origins
- Don't reflect Origin header
- Never use `*` with credentials
- Validate Origin header

---

## Q65: Explain password storage best practices.
**Answer:**
**Do:**
- Use adaptive hashing: bcrypt, Argon2, scrypt
- Unique salt per password
- High work factor
- Hash server-side

**Don't:**
- Plain text storage
- MD5, SHA-1 for passwords
- Reversible encryption
- Same salt for all passwords

**Example (bcrypt):**
```python
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
```

---

## Q66: What is Content Type mismatch vulnerability?
**Answer:** Browser interprets file differently than intended based on content, not declared type.

**Example:** Upload `image.jpg` containing HTML/JS, browser renders as HTML.

**Prevention:**
- X-Content-Type-Options: nosniff
- Validate file content, not just extension
- Serve uploaded files from separate domain
- Set correct Content-Type

---

## Q67: Explain File Upload vulnerabilities.
**Answer:**
**Attack vectors:**
1. Upload web shell (.php, .jsp)
2. Upload with double extension (file.php.jpg)
3. Content-Type manipulation
4. Upload path traversal
5. Null byte injection (file.php%00.jpg)

**Prevention:**
- Whitelist allowed extensions
- Validate MIME type AND content
- Random file names
- Store outside web root
- Serve from separate domain
- Virus scanning

---

## Q68: What is the difference between encoding, escaping, and sanitization?
**Answer:**
**Encoding:** Converting characters to safe representation
- HTML encoding: `<` → `&lt;`
- URL encoding: ` ` → `%20`

**Escaping:** Adding escape characters before special characters
- SQL: `'` → `\'` (but use parameterized queries!)

**Sanitization:** Removing or replacing dangerous content
- Strip HTML tags completely
- Remove script elements

**Best practice:** Output encoding is context-specific; input sanitization alone is insufficient.

---

## Q69: What is HTTP Strict Transport Security (HSTS)?
**Answer:** Header that forces browsers to use HTTPS:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

**Protection against:**
- Downgrade attacks
- Cookie hijacking
- MITM on first request (with preload)

**Preload:** Submit to browser preload list for protection on first visit.

**Warning:** Commit to HTTPS - misconfiguration can make site inaccessible.

---

## Q70: Explain API security based on OWASP API Top 10.
**Answer:**
| # | Vulnerability | Prevention |
|---|---------------|------------|
| 1 | Broken Object Level Auth | Authorization checks on every request |
| 2 | Broken Authentication | Strong auth, MFA, rate limiting |
| 3 | Broken Property Level Auth | Whitelist returned fields |
| 4 | Unrestricted Resource Consumption | Rate limiting, pagination |
| 5 | Broken Function Level Auth | Role-based access control |
| 6 | Unrestricted Business Flows | Anti-automation mechanisms |
| 7 | SSRF | URL validation, allowlists |
| 8 | Security Misconfiguration | Security hardening |
| 9 | Improper Inventory | API documentation, deprecation |
| 10 | Unsafe API Consumption | Validate third-party responses |

---

# 🟢 IN-DEPTH / SCENARIO QUESTIONS (71-100)

## Q71: SCENARIO - You discover SQL injection in production login page. Walk through response.
**Answer:**
**Immediate (Hour 1):**
1. Assess severity: Can data be extracted? Admin bypass?
2. Enable WAF rules to block SQLi patterns
3. Review logs for exploitation attempts
4. Document evidence

**Short-term (Hours 2-4):**
5. Develop and test patch (parameterized queries)
6. Deploy fix to production
7. Database audit for signs of compromise
8. Check for similar vulnerabilities elsewhere

**Investigation:**
9. Timeline of vulnerability introduction
10. Log analysis for past exploitation
11. Assess data exposure

**Post-incident:**
12. SAST/DAST integration in CI/CD
13. Developer training
14. Security code review process

---

## Q72: SCENARIO - Penetration test reveals stored XSS in user profile bio. How do you remediate?
**Answer:**
**Analysis:**
1. Identify all locations bio is displayed
2. Check if other fields are similarly vulnerable
3. Assess impact (who sees profile bios?)

**Fix:**
4. Output encoding where bio is displayed (HTML context)
5. Input validation (restrict allowed characters if appropriate)
6. Implement CSP to mitigate impact

**Testing:**
7. Verify fix in staging
8. Test various XSS payloads
9. Deploy with monitoring

**Prevention:**
10. Framework auto-escaping enabled
11. SAST rules for output encoding
12. Security testing in sprint cycles

---

## Q73: How would you secure an authentication system against OWASP Top 10?
**Answer:**
**A01 (Access Control):** Proper session binding, verify authorization on every request
**A02 (Crypto Failures):** bcrypt for passwords, TLS for transport
**A03 (Injection):** Parameterized queries for user lookup
**A04 (Insecure Design):** Account lockout, rate limiting, MFA
**A05 (Misconfiguration):** Secure headers, no default accounts
**A06 (Vulnerable Components):** Update auth libraries regularly
**A07 (Auth Failures):** Strong password policy, session management
**A08 (Integrity):** Secure password reset flow
**A09 (Logging):** Log all auth events
**A10 (SSRF):** Not directly applicable to auth

---

## Q74: SCENARIO - Customer reports their account was compromised despite using unique password. Investigation steps?
**Answer:**
1. **Account review:** Login history, IP addresses, devices
2. **Session analysis:** Any concurrent sessions? Session hijacking?
3. **Recent changes:** Password resets, email changes
4. **Attack vector analysis:**
   - Session cookie theft (XSS?)
   - Session fixation
   - Account recovery bypass
   - MFA bypass
   - Malware on customer device
5. **Network logs:** Any suspicious requests
6. **Similar cases:** Check other accounts from same IP
7. **Customer interview:** Recent phishing, device compromise?

**Remediation based on findings.**

---

## Q75: Design a secure password reset flow.
**Answer:**
**Flow:**
1. User enters email
2. **Server:** Don't confirm email existence (generic message)
3. Generate cryptographically random token (32+ bytes)
4. Store hashed token with expiration (15-30 min)
5. Send link via email (HTTPS only)
6. On reset page: Verify token, prompt new password
7. **After reset:** Invalidate token, invalidate all sessions, email notification

**Security measures:**
- Rate limiting on request
- Log all reset attempts
- Token single-use
- Require re-authentication for sensitive actions after reset
- Don't include username in reset email

---

## Q76: How would you implement defense-in-depth for a web application?
**Answer:**
**Perimeter:**
- WAF with OWASP rules
- DDoS protection
- Rate limiting

**Network:**
- Network segmentation
- VPN for admin access
- TLS everywhere

**Application:**
- Input validation
- Output encoding
- Parameterized queries
- Security headers
- CSRF protection

**Session:**
- Secure session management
- MFA
- Session timeout

**Data:**
- Encryption at rest
- Minimal data retention
- Access logging

**Monitoring:**
- Centralized logging
- SIEM alerts
- Regular testing

---

## Q77: SCENARIO - You find an endpoint returning sensitive data without authentication. How do you handle it?
**Answer:**
**Immediate:**
1. Confirm vulnerability (is auth really missing?)
2. Assess data sensitivity and exposure
3. Check logs for past access
4. Implement emergency fix (add authentication) or disable endpoint

**Investigation:**
5. How did this happen? Recent change?
6. Who has accessed this endpoint?
7. Regulatory implications (PII exposed?)

**Remediation:**
8. Proper fix with code review
9. Check for similar issues
10. Add security testing to CI/CD

**Follow-up:**
11. Incident report
12. Breach notification if required
13. Process improvements

---

## Q78: Explain how you would secure a file upload feature.
**Answer:**
**Validation:**
```
1. Whitelist allowed extensions (.jpg, .png, .pdf)
2. Check file signature/magic bytes (not just extension)
3. Validate Content-Type header
4. Limit file size
5. Virus scanning
```

**Storage:**
```
6. Generate random filename
7. Store outside web root
8. Separate domain for serving files
9. No execute permissions
```

**Serving:**
```
10. Content-Type set correctly
11. Content-Disposition: attachment for downloads
12. X-Content-Type-Options: nosniff
```

**Additional:**
```
13. Rate limit uploads
14. Log all upload activities
15. Regular cleanup of temporary files
```

---

## Q79: SCENARIO - SAST tool reports 500 SQL injection findings. How do you prioritize?
**Answer:**
**Triage:**
1. Filter false positives (review sample)
2. Identify unique vs duplicate findings
3. Categorize by confidence level

**Prioritization factors:**
4. **Exposure:** Internet-facing vs internal
5. **Authentication:** Pre-auth vs post-auth
6. **Data sensitivity:** What data is queried
7. **Exploitability:** Complexity of exploit
8. **CVSS-like scoring**

**Approach:**
9. Fix high-priority items first
10. Group by code pattern for batch fixes
11. Update coding standards
12. Developer training
13. Add SAST to PR checks to prevent new issues

---

## Q80: How would you implement secure API authentication?
**Answer:**
**Options:**
1. **API Keys:** Simple, good for service-to-service
2. **OAuth 2.0:** User delegation, granular scopes
3. **JWT:** Stateless, good for microservices

**Best practices:**
- Transmit over HTTPS only
- Short-lived tokens (15 min)
- Refresh token rotation
- Proper token storage (not localStorage)
- Scope validation on every request
- Rate limiting per API key/user
- Revocation mechanism
- Audit logging

**Implementation:**
- Validate token on every request
- Check expiration, signature, claims
- Authorization after authentication

---

## Q81: SCENARIO - Security scan shows XSS in 200+ pages due to vulnerable template. Remediation strategy?
**Answer:**
**Root cause:**
1. Identify vulnerable template component
2. Understand why auto-escaping isn't working

**Fix approach:**
3. Fix at template/framework level if possible (single fix)
4. Update framework to enable default escaping
5. If individual fixes needed, prioritize by:
   - User-facing vs admin pages
   - Severity of content displayed

**Deployment:**
6. Test thoroughly in staging
7. Deploy incrementally
8. Monitor for issues

**Prevention:**
9. Framework configuration enforces escaping
10. SAST rules for output encoding
11. Security testing in CI/CD

---

## Q82: Explain your approach to securing third-party dependencies.
**Answer:**
**Inventory:**
1. Software Bill of Materials (SBOM)
2. Know all direct and transitive dependencies

**Scanning:**
3. SCA tools in CI/CD (Snyk, Dependabot)
4. Block builds with critical vulnerabilities
5. Daily scans of deployed applications

**Updates:**
6. Automated security updates
7. Regular update cadence
8. Test updates before deploying

**Policy:**
9. Approved dependency sources
10. License compliance
11. Maximum age for dependencies
12. No dependencies with unpatched critical CVEs

**Vendoring:**
13. Consider vendoring critical dependencies
14. Verify checksums

---

## Q83: SCENARIO - You're building an e-commerce site. What OWASP Top 10 controls are most critical?
**Answer:**
**A01 Access Control:** Users can't access others' orders
**A02 Cryptographic:** Payment data encrypted, passwords hashed
**A03 Injection:** Parameterized queries for product search, orders
**A04 Insecure Design:** Rate limiting on checkout, fraud detection
**A05 Misconfiguration:** PCI DSS compliant configuration
**A06 Vulnerable Components:** Payment SDK updated regularly
**A07 Authentication:** MFA, secure password reset
**A08 Integrity:** Signed price data, CSRF protection on checkout
**A09 Logging:** All transactions logged, alerts on anomalies
**A10 SSRF:** If any URL fetching features

**Additional:** PCI DSS compliance, fraud detection, session security.

---

## Q84: How would you test for IDOR vulnerabilities?
**Answer:**
**Approach:**
1. Create two user accounts (User A, User B)
2. Identify all resource identifiers (IDs in URLs, JSON)
3. Map all endpoints with identifiers

**Testing:**
4. Access User B's resources using User A's session
5. Try sequential IDs (123, 124, 125)
6. Try encoded/hashed IDs (still might be predictable)
7. Test different HTTP methods (GET, POST, PUT, DELETE)
8. Check JSON responses for extra data

**Tools:**
9. Burp Suite - Autorize plugin
10. Manual testing with multiple sessions

**What to look for:**
11. Different response when accessing own vs others' resources
12. Partial data leakage

---

## Q85: SCENARIO - Client wants 100% security guarantee. How do you respond?
**Answer:**
**Honest response:**
1. No system is 100% secure - security is risk management
2. We implement defense-in-depth to minimize risk
3. We follow industry standards (OWASP, NIST)

**What we can commit to:**
4. Regular security testing (SAST, DAST, pentest)
5. Vulnerability management with defined SLAs
6. Incident response plan
7. Security monitoring and alerting
8. Regular dependency updates
9. Compliance with relevant standards

**Metrics we can provide:**
10. Time to remediate vulnerabilities
11. Penetration test findings trend
12. Security incident statistics
13. Compliance certifications

---

## Q86: Explain secure session management best practices.
**Answer:**
**Session creation:**
- Generate cryptographically random session ID
- Regenerate ID after authentication
- Bind session to user context

**Session storage:**
- Server-side session storage
- Don't store sensitive data in session
- Set appropriate expiration

**Cookie flags:**
```
Set-Cookie: sessionid=xxx; Secure; HttpOnly; SameSite=Strict; Path=/
```

**Session termination:**
- Logout invalidates session server-side
- Timeout (idle and absolute)
- Terminate on password change

**Protection:**
- Don't expose session ID in URL
- Implement concurrent session control
- Monitor for session anomalies

---

## Q87: SCENARIO - Bug bounty researcher reports critical vulnerability. Response process?
**Answer:**
**Acknowledge (Within 24h):**
1. Thank researcher
2. Confirm receipt
3. Set expectation for updates

**Triage (1-2 days):**
4. Reproduce vulnerability
5. Assess severity and impact
6. Assign to appropriate team

**Remediation:**
7. Develop fix
8. Test thoroughly
9. Deploy fix
10. Verify fix with researcher if applicable

**Coordination:**
11. Agree on disclosure timeline
12. Keep researcher updated
13. Process bounty payment

**Closure:**
14. Public acknowledgment (if researcher agrees)
15. Update researcher with final status
16. Internal lessons learned

---

## Q88: How would you implement security in a microservices architecture following OWASP guidelines?
**Answer:**
**Service-to-service (A01, A07):**
- Mutual TLS (mTLS)
- Service mesh for policy enforcement
- JWT for authorization claims

**API Gateway (A03, A05):**
- Central authentication
- Input validation
- Rate limiting
- Security headers

**Each service (A03):**
- Parameterized queries
- Input validation
- Output encoding

**Secrets (A02):**
- External secrets management (Vault)
- No hardcoded secrets
- Short-lived credentials

**Logging (A09):**
- Distributed tracing
- Centralized logging
- Security event monitoring

**Dependencies (A06):**
- Container image scanning
- Dependency scanning per service

---

## Q89: Explain how to prevent brute force attacks.
**Answer:**
**Account level:**
- Progressive delays between attempts
- Account lockout after N failures
- CAPTCHA after failed attempts

**Application level:**
- Rate limiting per IP
- Rate limiting per username
- Device fingerprinting
- Geographic anomaly detection

**Authentication:**
- MFA (prevents password-only attacks)
- Passwordless options
- Long, complex passwords encouraged

**Monitoring:**
- Alert on failed login spikes
- Track credential stuffing patterns
- IP reputation checking

**User experience:**
- Clear lockout messaging
- Secure unlock process

---

## Q90: SCENARIO - Audit reveals developers are committing API keys to Git. How do you address this?
**Answer:**
**Immediate:**
1. Rotate all exposed credentials
2. Scan repo history for secrets
3. Remove secrets from history (git filter-branch or BFG)

**Prevention tools:**
4. Pre-commit hooks (GitLeaks, git-secrets)
5. CI/CD secret scanning
6. GitHub/GitLab secret scanning

**Process:**
7. Secrets management solution (Vault, AWS Secrets Manager)
8. Environment variables for secrets
9. .gitignore for config files with secrets

**Training:**
10. Developer security training
11. Documentation on secrets handling
12. Make it easy to do the right thing

**Monitoring:**
13. Alert on secrets in repos
14. Regular audits

---

## Q91: How would you design a secure registration/signup flow?
**Answer:**
**Requirements:**
1. Strong password requirements (12+, complexity)
2. Email verification
3. CAPTCHA to prevent automation
4. Rate limiting

**Implementation:**
5. Parameterized queries
6. Username/email enumeration prevention
7. bcrypt for password storage
8. Secure email verification tokens

**Flow:**
1. User submits form (CAPTCHA verified)
2. Validate input
3. Check if email exists (generic response regardless)
4. Hash password, store user
5. Generate email verification token
6. Send verification email
7. On verification, activate account

**Security measures:**
- CSRF token
- Input validation
- Logging

---

## Q92: Explain Insecure Direct Object Reference vs IDOB (Broken Object Level Authorization).
**Answer:**
**IDOR (Original term):**
Specific case of exposing internal object references.
```
/api/users/123
# Change to /api/users/124 to access another user
```

**BOLA (Current OWASP API Top 10 term):**
Broader category - any failure to validate authorization at object level.
```
GET /api/accounts/456/transactions
# Server doesn't verify caller owns account 456
```

**Key difference:** BOLA is the broader concept; IDOR is a specific manifestation where the object ID is directly exposed.

**Prevention:** Server-side authorization check for every object access.

---

## Q93: SCENARIO - You need to implement CSRF protection. Compare approaches.
**Answer:**
**1. Synchronizer Token:**
```html
<input type="hidden" name="csrf" value="random-token">
```
- Generate random token per session
- Include in forms
- Validate on server
- Most common approach

**2. Double Submit Cookie:**
- Set CSRF token in cookie
- Also send in request body/header
- Compare on server
- Stateless

**3. SameSite Cookie:**
```
Set-Cookie: session=xxx; SameSite=Strict
```
- Browser-enforced
- Not sent cross-site
- Limited browser support (older browsers)

**4. Custom Header:**
```javascript
fetch(url, { headers: { 'X-CSRF-Token': token } })
```
- CORS prevents cross-origin addition
- Good for APIs

**Recommendation:** Combination - Synchronizer token + SameSite=Lax.

---

## Q94: How would you secure error handling in a web application?
**Answer:**
**Don't expose:**
- Stack traces
- Database errors
- File paths
- Internal IPs
- Version numbers
- Framework details

**Implementation:**
```python
try:
    # Application code
except Exception as e:
    logger.error(f"Internal error: {e}")  # Log details
    return "An error occurred", 500  # Generic response
```

**Per environment:**
- Development: Detailed errors OK
- Production: Generic messages only

**Custom error pages:**
- 404, 500, etc. with minimal information
- Consistent branding

**Logging:**
- Log full details securely
- Correlation IDs for tracing

---

## Q95: SCENARIO - Security team has limited resources. How do you prioritize OWASP Top 10?
**Answer:**
**Critical (Address first):**
1. **Injection (A03):** High impact, common
2. **Broken Access Control (A01):** Data exposure risk
3. **Cryptographic Failures (A02):** Data breach implications

**High priority:**
4. **Auth Failures (A07):** Account compromise
5. **Security Misconfiguration (A05):** Often easy to fix

**Important:**
6. **Vulnerable Components (A06):** Automated scanning helps
7. **SSRF (A10):** If applicable to architecture

**Strategic:**
8. **Insecure Design (A04):** Long-term architecture
9. **Integrity Failures (A08):** CI/CD security
10. **Logging Failures (A09):** Detection capability

**Approach:** Automated tools for A03, A05, A06. Manual focus on A01, A07.

---

## Q96: Explain XML security beyond XXE.
**Answer:**
**XXE:** External entity processing (covered)

**Billion Laughs (DoS):**
```xml
<!DOCTYPE lolz [
  <!ENTITY lol "lol">
  <!ENTITY lol2 "&lol;&lol;&lol;">
  <!-- Exponential expansion -->
]>
```

**XPath Injection:**
```xml
username: ' or '1'='1
XPath: //users/user[username/text()='' or '1'='1']
```

**XML Injection:**
Manipulating XML structure through input.

**Prevention:**
- Disable DTD processing
- Limit entity expansion
- Input validation
- Use JSON where possible

---

## Q97: SCENARIO - Implementing security for a public API. Design considerations?
**Answer:**
**Authentication:**
- OAuth 2.0 for user actions
- API keys for server-to-server
- JWT tokens with short expiry

**Authorization:**
- Scope-based access
- Rate limiting per client
- Quota enforcement

**Input validation:**
- Schema validation (OpenAPI spec)
- Request size limits
- Content-Type validation

**Protection:**
- TLS required
- CORS configured properly
- Rate limiting
- DDoS protection
- WAF rules

**Monitoring:**
- Request logging
- Anomaly detection
- API versioning

**Documentation:**
- Security requirements clear
- Example requests
- Error responses documented

---

## Q98: How do you handle sensitive data in logs?
**Answer:**
**Never log:**
- Passwords
- API keys/secrets
- Credit card numbers
- Full SSN
- Session tokens
- Private keys

**Mask/redact:**
```
Credit card: **** **** **** 1234
SSN: ***-**-1234
Email: u***@example.com
```

**Implementation:**
```python
def sanitize_log(data):
    data = re.sub(r'password=\S+', 'password=***', data)
    data = re.sub(r'\b\d{16}\b', '****', data)  # CC numbers
    return data
```

**Architecture:**
- Log sanitization library
- Automated PII detection
- Separate sensitive logs
- Encryption of log files
- Access control on logs

---

## Q99: SCENARIO - Competitor releases similar product. You suspect code theft. How do you investigate (security perspective)?
**Answer:**
**Internal investigation:**
1. Review access logs for code repositories
2. Check for unusual data exfiltration patterns
3. Review VPN/remote access logs
4. Check DLP alerts
5. Email/communication review (with legal approval)
6. Departed employee analysis

**Technical indicators:**
7. Large downloads before departure
8. Personal device syncing
9. Unusual file access patterns
10. Cloud storage uploads

**Prevention lessons:**
11. Code access monitoring
12. DLP for source code
13. Exit procedures include access audit
14. Non-compete/NDA enforcement

*Note: Work with legal throughout this process.*

---

## Q100: Final comprehensive question - How do you build a security culture that addresses OWASP Top 10?
**Answer:**
**Training:**
- Developer security training (OWASP focused)
- Secure coding standards
- Champions program

**Process:**
- Security in SDLC
- Threat modeling in design
- Security code review
- CI/CD security gates

**Tooling:**
- SAST (injection, crypto issues)
- DAST (runtime vulnerabilities)
- SCA (vulnerable components)
- Secret scanning

**Governance:**
- Security requirements in stories
- Bug bounty program
- Metrics and dashboards

**Feedback:**
- Blameless post-mortems
- Celebrate security wins
- Make security easy, not bureaucratic

**Continuous improvement:**
- Track OWASP Top 10 trends
- Update training annually
- Adapt to new threats

---

# 📊 QUICK REVISION CARD

```
OWASP TOP 10 (2021) AT A GLANCE:

A01: Broken Access Control
     → Server-side enforcement, deny by default

A02: Cryptographic Failures  
     → TLS, AES-256, bcrypt for passwords

A03: Injection
     → Parameterized queries, input validation

A04: Insecure Design
     → Threat modeling, security requirements

A05: Security Misconfiguration
     → Hardening, minimal installation

A06: Vulnerable Components
     → SCA scanning, regular updates

A07: Auth Failures
     → MFA, strong passwords, session management

A08: Integrity Failures
     → Signed code, verified updates

A09: Logging Failures
     → Log security events, centralize, alert

A10: SSRF
     → URL validation, deny internal ranges
```

---

**Good luck with your interview!** 🚀
