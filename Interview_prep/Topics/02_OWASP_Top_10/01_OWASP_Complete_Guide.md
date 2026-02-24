# 🛡️ OWASP TOP 10 - Complete Guide (2021 Edition)

## Table of Contents
1. [What is OWASP?](#what-is-owasp)
2. [A01: Broken Access Control](#a01-broken-access-control)
3. [A02: Cryptographic Failures](#a02-cryptographic-failures)
4. [A03: Injection](#a03-injection)
5. [A04: Insecure Design](#a04-insecure-design)
6. [A05: Security Misconfiguration](#a05-security-misconfiguration)
7. [A06: Vulnerable Components](#a06-vulnerable-and-outdated-components)
8. [A07: Authentication Failures](#a07-identification-and-authentication-failures)
9. [A08: Software & Data Integrity Failures](#a08-software-and-data-integrity-failures)
10. [A09: Security Logging Failures](#a09-security-logging-and-monitoring-failures)
11. [A10: Server-Side Request Forgery](#a10-server-side-request-forgery-ssrf)
12. [Interview Questions](#interview-questions)
13. [Learning Resources](#learning-resources)

---

## What is OWASP?

### Overview

**OWASP** = **O**pen **W**eb **A**pplication **S**ecurity **P**roject

- A **nonprofit foundation** dedicated to improving software security
- Provides **free, open-source** tools, documentation, and standards
- The **OWASP Top 10** is the most recognized security awareness document

```
┌─────────────────────────────────────────────────────────────────┐
│                    OWASP TOP 10 (2021)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  A01 ► Broken Access Control            (Up from #5)           │
│  A02 ► Cryptographic Failures           (Renamed from #3)      │
│  A03 ► Injection                        (Down from #1)         │
│  A04 ► Insecure Design                  (NEW)                  │
│  A05 ► Security Misconfiguration        (Up from #6)           │
│  A06 ► Vulnerable Components            (Up from #9)           │
│  A07 ► Authentication Failures          (Down from #2)         │
│  A08 ► Software & Data Integrity        (NEW - merged)         │
│  A09 ► Logging & Monitoring Failures    (Up from #10)          │
│  A10 ► SSRF                             (NEW)                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Why is OWASP Important?

| Reason | Details |
|--------|---------|
| **Industry Standard** | Used by companies worldwide for security assessments |
| **Interview Essential** | Asked in 99% of cybersecurity interviews |
| **Compliance** | Referenced by PCI-DSS, HIPAA, SOX requirements |
| **Practical Focus** | Based on real-world vulnerability data |

---

## A01: Broken Access Control

### What is Access Control?

Access control enforces that users **cannot act outside their intended permissions**.

### The Logic

```
┌─────────────────────────────────────────────────────────────┐
│                  ACCESS CONTROL CONCEPTS                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Authentication: WHO are you? (Login)                       │
│         ↓                                                   │
│  Authorization: WHAT can you do? (Permissions)              │
│         ↓                                                   │
│  Access Control: ENFORCE the rules                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Types of Access Control Vulnerabilities

#### 1. Vertical Privilege Escalation
User gains access to **higher privilege level** (e.g., regular user → admin)

```
Normal Flow:
  User (Role: Customer) ─────► Cannot access /admin/users

Broken Access Control:
  User (Role: Customer) ─────► Can access /admin/users (VULNERABILITY!)
```

#### 2. Horizontal Privilege Escalation
User accesses **another user's data** at the same privilege level

```
Normal Flow:
  User A ───► /profile?id=123 ───► Sees User A's data

Broken Access Control:
  User A ───► /profile?id=456 ───► Sees User B's data (VULNERABILITY!)
```

#### 3. IDOR (Insecure Direct Object Reference)

```
VULNERABLE CODE:
GET /api/documents/12345

If the server doesn't verify ownership:
- Attacker changes ID to 12346, 12347...
- Gets access to other users' documents!
```

### Real-World Example

```
# Vulnerable API endpoint
GET /api/orders/{orderId}

# Attacker modifies orderId
GET /api/orders/1001  → Their order ✓
GET /api/orders/1002  → Someone else's order ✗ (VULNERABLE!)
GET /api/orders/1003  → Another person's order ✗ (VULNERABLE!)
```

### Prevention Strategies

```python
# WRONG - No authorization check
@app.route('/api/orders/<order_id>')
def get_order(order_id):
    return Order.query.get(order_id)  # BAD!

# CORRECT - Verify ownership
@app.route('/api/orders/<order_id>')
@login_required
def get_order(order_id):
    order = Order.query.get(order_id)
    if order.user_id != current_user.id:
        return "Forbidden", 403  # GOOD!
    return order
```

### Prevention Checklist

| Control | Implementation |
|---------|----------------|
| **Deny by default** | Block access unless explicitly allowed |
| **Server-side validation** | Never trust client-side checks alone |
| **Ownership verification** | Check if user owns the resource |
| **Rate limiting** | Prevent brute-force enumeration |
| **Audit logging** | Log all access control failures |

---

## A02: Cryptographic Failures

### What is it?

Failure to properly protect **sensitive data** using cryptography (or not using it at all).

### The Logic

```
┌─────────────────────────────────────────────────────────────┐
│              SENSITIVE DATA EXPOSURE POINTS                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DATA AT REST        DATA IN TRANSIT       DATA IN USE      │
│  (Stored in DB)     (Network transfer)    (In memory)       │
│                                                             │
│  ┌─────────┐        ┌─────────┐          ┌─────────┐       │
│  │   💾    │───────►│   🌐    │─────────►│   💻    │       │
│  │Database │        │ Network │          │ Browser │       │
│  └─────────┘        └─────────┘          └─────────┘       │
│                                                             │
│  Encrypt with       Use TLS/HTTPS        Minimize          │
│  AES-256                                 exposure          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Common Failures

| Failure Type | Example | Impact |
|--------------|---------|--------|
| **Weak algorithms** | MD5 for passwords, DES encryption | Easy to crack |
| **No encryption** | Plain HTTP, unencrypted storage | Data exposure |
| **Poor key management** | Hardcoded keys, weak keys | Key compromise |
| **Improper TLS config** | Old TLS versions, weak ciphers | MITM attacks |

### Vulnerable vs Secure Examples

```
❌ VULNERABLE - Storing passwords in plaintext or weak hash
password_hash = md5(password)  # BAD - MD5 is broken

✅ SECURE - Using proper password hashing
password_hash = bcrypt.hash(password)  # GOOD - Slow, salted

---

❌ VULNERABLE - Hardcoded encryption key
SECRET_KEY = "my_secret_key_123"  # BAD - Exposed in code

✅ SECURE - Environment variables or secret manager
SECRET_KEY = os.environ.get('SECRET_KEY')  # GOOD

---

❌ VULNERABLE - HTTP for sensitive data
http://example.com/login  # BAD - Traffic is visible

✅ SECURE - HTTPS everywhere
https://example.com/login  # GOOD - Encrypted
```

### Sensitive Data Classification

| Data Type | Examples | Required Protection |
|-----------|----------|---------------------|
| **Credentials** | Passwords, API keys | Hash (bcrypt), encrypt |
| **PII** | SSN, passport, address | Encrypt at rest & transit |
| **Financial** | Credit cards, bank accounts | PCI-DSS compliance |
| **Health** | Medical records | HIPAA compliance |

### Prevention Strategies

```
┌─────────────────────────────────────────────────────────────┐
│              CRYPTOGRAPHIC BEST PRACTICES                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CLASSIFY YOUR DATA                                       │
│     └── Know what's sensitive, apply appropriate controls   │
│                                                             │
│  2. ENCRYPT IN TRANSIT                                       │
│     └── TLS 1.3, HSTS, proper certificate management        │
│                                                             │
│  3. ENCRYPT AT REST                                          │
│     └── AES-256, proper key management                      │
│                                                             │
│  4. USE PROPER PASSWORD STORAGE                              │
│     └── bcrypt, scrypt, or Argon2 with salting             │
│                                                             │
│  5. AVOID WEAK ALGORITHMS                                    │
│     └── No MD5, SHA1 for security, DES, RC4               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## A03: Injection

### What is Injection?

Attacker **injects malicious code/commands** through user input that gets executed by the application.

### Types of Injection

```
┌─────────────────────────────────────────────────────────────┐
│                    INJECTION TYPES                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ SQL INJECTION   │  │ COMMAND INJECT. │                  │
│  │ (Database)      │  │ (OS Commands)   │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ XSS             │  │ LDAP INJECTION  │                  │
│  │ (JavaScript)    │  │ (Directory)     │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ XML INJECTION   │  │ NOSQL INJECTION │                  │
│  │ (XXE/XPATH)     │  │ (MongoDB, etc.) │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### SQL Injection Deep Dive

#### How It Works

```
LEGITIMATE QUERY:
SELECT * FROM users WHERE username = 'john' AND password = 'secret123'

ATTACKER INPUT:
Username: admin'--
Password: anything

RESULTING QUERY:
SELECT * FROM users WHERE username = 'admin'--' AND password = 'anything'
                                            ↑
                                    Comment starts here
                                    (password check ignored!)
```

#### Types of SQL Injection

```
┌─────────────────────────────────────────────────────────────┐
│               SQL INJECTION TYPES                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. IN-BAND (Classic)                                        │
│     ├── Error-based: Extracts data from error messages      │
│     └── UNION-based: Uses UNION to combine results          │
│                                                             │
│  2. BLIND                                                    │
│     ├── Boolean-based: True/False responses                 │
│     └── Time-based: Delays indicate success                 │
│                                                             │
│  3. OUT-OF-BAND                                              │
│     └── Uses external channel (DNS, HTTP) for data          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### SQL Injection Examples

```sql
-- Authentication Bypass
' OR '1'='1'--
' OR 1=1--
admin'--

-- UNION Attack (extract data)
' UNION SELECT username, password FROM users--

-- Dropping Tables (Destructive)
'; DROP TABLE users;--

-- Time-based Blind (detect vulnerability)
'; IF (1=1) WAITFOR DELAY '0:0:5'--
```

### Command Injection

```
VULNERABLE CODE:
ping = os.system("ping " + user_input)

ATTACKER INPUT:
user_input = "8.8.8.8; cat /etc/passwd"

RESULTING COMMAND:
ping 8.8.8.8; cat /etc/passwd
              ↑
         Malicious command executed!
```

### Prevention Strategies

```python
# ❌ VULNERABLE - String concatenation
query = "SELECT * FROM users WHERE id = " + user_input

# ✅ SECURE - Parameterized query (Prepared Statement)
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_input,))

# ✅ SECURE - ORM (Object-Relational Mapping)
user = User.query.filter_by(id=user_input).first()
```

### Prevention Checklist

| Prevention | Implementation |
|------------|----------------|
| **Parameterized queries** | Use prepared statements, never concatenate |
| **Input validation** | Whitelist allowed characters |
| **ORM usage** | Use frameworks like SQLAlchemy, Hibernate |
| **Least privilege** | DB user with minimal permissions |
| **WAF** | Web Application Firewall rules |

---

## A04: Insecure Design

### What is it?

**Flaws in the design/architecture** itself, not implementation bugs. Even perfect code can't fix bad design.

### The Logic

```
┌─────────────────────────────────────────────────────────────┐
│      IMPLEMENTATION BUG vs DESIGN FLAW                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IMPLEMENTATION BUG:                                         │
│  "The code is wrong"                                        │
│  Example: SQL Injection due to missing parameterization     │
│  Fix: Correct the code                                      │
│                                                             │
│  DESIGN FLAW:                                                │
│  "The architecture is wrong"                                │
│  Example: Password reset sends password via email           │
│  Fix: Redesign the feature                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Examples of Insecure Design

| Scenario | Design Flaw | Secure Design |
|----------|-------------|---------------|
| **Cinema booking** | No limit on ticket purchases | Rate limiting, max tickets per user |
| **Password reset** | Security question: "Mother's maiden name" | Email/SMS verification code |
| **Payment** | Price sent from client-side | Price calculated server-side |
| **Account lockout** | None | Lock after 5 failed attempts |

### Threat Modeling

```
┌─────────────────────────────────────────────────────────────┐
│                 STRIDE THREAT MODEL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  S - Spoofing          Can attacker pretend to be someone? │
│  T - Tampering         Can attacker modify data?           │
│  R - Repudiation       Can attacker deny actions?          │
│  I - Information Disc. Can attacker access private data?   │
│  D - Denial of Service Can attacker crash the system?      │
│  E - Elevation of Priv Can attacker gain higher access?   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Prevention

| Control | Description |
|---------|-------------|
| **Threat modeling** | Identify threats early in design |
| **Security requirements** | Define security needs upfront |
| **Secure design patterns** | Use proven architectures |
| **Security review** | Review designs before implementation |

---

## A05: Security Misconfiguration

### What is it?

Insecure **default configurations**, missing hardening, or **improper settings**.

### Common Misconfigurations

```
┌─────────────────────────────────────────────────────────────┐
│               MISCONFIGURATION EXAMPLES                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✗ Default credentials (admin/admin, root/root)            │
│  ✗ Unnecessary services enabled                            │
│  ✗ Debug mode in production                                │
│  ✗ Directory listing enabled                               │
│  ✗ Verbose error messages                                  │
│  ✗ Missing security headers                                │
│  ✗ Cloud storage publicly accessible                       │
│  ✗ Outdated software/frameworks                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Security Headers

```
# Essential HTTP Security Headers

Content-Security-Policy: default-src 'self';
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin-when-cross-origin
```

### Prevention Checklist

| Area | Action |
|------|--------|
| **Credentials** | Change all default passwords |
| **Services** | Disable unnecessary features |
| **Errors** | Generic error messages in production |
| **Headers** | Implement security headers |
| **Updates** | Regular patching schedule |
| **Review** | Automated configuration scanning |

---

## A06: Vulnerable and Outdated Components

### What is it?

Using **libraries, frameworks, or components** with known vulnerabilities.

### The Logic

```
┌─────────────────────────────────────────────────────────────┐
│          COMPONENT VULNERABILITY CHAIN                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Your Application                                           │
│       │                                                     │
│       └──► Framework (e.g., Spring Boot 2.5.0)              │
│                 │                                           │
│                 └──► Library (e.g., Log4j 2.14.1)           │
│                           │                                 │
│                           └──► CVE-2021-44228 (CRITICAL!)   │
│                                                             │
│  Even if YOUR code is secure, vulnerable dependencies       │
│  can compromise your entire application!                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Famous Examples

| Vulnerability | Component | Impact |
|---------------|-----------|--------|
| **Log4Shell** (2021) | Log4j | Remote code execution, millions affected |
| **Heartbleed** (2014) | OpenSSL | Memory leak, expose passwords |
| **Struts2** (2017) | Apache Struts | Equifax breach, 147M records |

### Prevention

```
┌─────────────────────────────────────────────────────────────┐
│         COMPONENT SECURITY PRACTICES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. INVENTORY                                                │
│     └── Know all components and versions                    │
│                                                             │
│  2. MONITOR                                                  │
│     └── Subscribe to CVE alerts for your stack             │
│                                                             │
│  3. UPDATE                                                   │
│     └── Regular patching schedule                           │
│                                                             │
│  4. SCAN                                                     │
│     └── Use SCA tools (OWASP Dependency-Check, Snyk)       │
│                                                             │
│  5. MINIMIZE                                                 │
│     └── Remove unused dependencies                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tools for Scanning

| Tool | Language/Platform | Link |
|------|-------------------|------|
| **OWASP Dependency-Check** | Multi-language | https://owasp.org/www-project-dependency-check/ |
| **Snyk** | Multi-language | https://snyk.io/ |
| **npm audit** | JavaScript | Built into npm |
| **Safety** | Python | https://pyup.io/safety/ |

---

## A07: Identification and Authentication Failures

### What is it?

Weaknesses in **verifying user identity** and **session management**.

### Common Vulnerabilities

```
┌─────────────────────────────────────────────────────────────┐
│          AUTHENTICATION FAILURES                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✗ Weak password policies                                   │
│  ✗ Missing brute-force protection                          │
│  ✗ Plain text/weak password storage                        │
│  ✗ Missing MFA for sensitive actions                       │
│  ✗ Session fixation                                        │
│  ✗ Session tokens in URLs                                  │
│  ✗ Sessions not invalidated on logout                      │
│  ✗ Long/infinite session timeouts                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Session Management

```
SECURE SESSION LIFECYCLE:

┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Login  │───►│ Generate │───►│  Valid  │───►│ Logout │
│         │    │ New SID  │    │ Session │    │        │
└─────────┘    └──────────┘    └────┬────┘    └────┬───┘
                                    │              │
                               ┌────▼────┐    ┌────▼────┐
                               │ Timeout │    │ Destroy │
                               │ Check   │    │ Session │
                               └─────────┘    └─────────┘
```

### Prevention Strategies

```python
# Password hashing with bcrypt
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
```

| Control | Implementation |
|---------|----------------|
| **Strong passwords** | Min 8 chars, complexity, no common passwords |
| **Rate limiting** | Lock after 5 failures, CAPTCHA |
| **MFA** | TOTP, SMS, hardware keys |
| **Secure sessions** | Random IDs, HttpOnly, Secure flags |
| **Proper logout** | Invalidate session server-side |

---

## A08: Software and Data Integrity Failures

### What is it?

Failures in **verifying the integrity** of software updates, critical data, or CI/CD pipelines.

### Types

```
┌─────────────────────────────────────────────────────────────┐
│         INTEGRITY FAILURE TYPES                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. INSECURE DESERIALIZATION                                 │
│     └── Untrusted data deserialized without validation      │
│                                                             │
│  2. INSECURE CI/CD PIPELINE                                  │
│     └── Compromised build/deploy process                    │
│                                                             │
│  3. UNSIGNED UPDATES                                         │
│     └── Software updates without signature verification     │
│                                                             │
│  4. SUPPLY CHAIN ATTACKS                                     │
│     └── Malicious code in dependencies                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Insecure Deserialization

```
ATTACK FLOW:

┌──────────────────┐     ┌──────────────────┐
│  Attacker sends  │────►│  Application     │
│  malicious       │     │  deserializes    │
│  serialized data │     │  without checks  │
└──────────────────┘     └────────┬─────────┘
                                  │
                         ┌────────▼─────────┐
                         │  Code Execution  │
                         │  (RCE!)          │
                         └──────────────────┘
```

### Prevention

| Control | Implementation |
|---------|----------------|
| **Digital signatures** | Verify software/update authenticity |
| **Integrity checks** | Checksums for dependencies |
| **Secure CI/CD** | Protected pipelines, access control |
| **Avoid deserialization** | Use safe formats (JSON) if possible |

---

## A09: Security Logging and Monitoring Failures

### What is it?

**Insufficient logging**, making it impossible to **detect, escalate, or recover** from attacks.

### What Should Be Logged?

```
┌─────────────────────────────────────────────────────────────┐
│              ESSENTIAL SECURITY EVENTS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✓ Authentication (success/failure)                        │
│  ✓ Authorization failures                                  │
│  ✓ Input validation failures                               │
│  ✓ High-value transactions                                 │
│  ✓ Session management events                               │
│  ✓ Administrative actions                                  │
│  ✓ Data access patterns                                    │
│  ✓ Application errors                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Log Format Best Practice

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "WARN",
  "event": "AUTHENTICATION_FAILURE",
  "user": "john@example.com",
  "ip": "192.168.1.100",
  "user_agent": "Mozilla/5.0...",
  "details": "Invalid password attempt 3 of 5",
  "request_id": "abc123"
}
```

### Prevention

| Control | Implementation |
|---------|----------------|
| **Centralized logging** | SIEM (Splunk, ELK Stack) |
| **Real-time alerting** | Automated anomaly detection |
| **Log protection** | Append-only, tamper-evident |
| **Incident response** | Documented procedures |

---

## A10: Server-Side Request Forgery (SSRF)

### What is it?

Attacker makes the **server fetch a URL** they control, potentially accessing **internal resources**.

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    SSRF ATTACK FLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ATTACKER                    SERVER                        │
│      │                           │                          │
│      │  Request:                 │                          │
│      │  /fetch?url=http://       │                          │
│      │  internal-api:8080/admin  │                          │
│      │──────────────────────────►│                          │
│      │                           │                          │
│      │                           │  Server fetches          │
│      │                           │  internal URL!           │
│      │                           │◄─────────────────┐       │
│      │                           │                  │       │
│      │  Returns internal data!   │  INTERNAL-API    │       │
│      │◄──────────────────────────│  (Attacker can't │       │
│      │                           │   reach directly)│       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Attack Examples

```
# Access internal services
/fetch?url=http://localhost:8080/admin
/fetch?url=http://169.254.169.254/latest/meta-data/  # AWS metadata

# Access internal network
/fetch?url=http://192.168.1.1/admin

# Read local files (if file:// allowed)
/fetch?url=file:///etc/passwd
```

### Prevention

| Control | Implementation |
|---------|----------------|
| **URL validation** | Whitelist allowed domains |
| **Block internal IPs** | Deny 127.0.0.1, 10.x, 192.168.x, 169.254.x |
| **Block protocols** | Only allow http/https, block file://, gopher:// |
| **Network segmentation** | Limit server's internal access |

---

## Interview Questions

### Basic Questions

**Q1: What is the OWASP Top 10?**
> "The OWASP Top 10 is a standard awareness document representing the most critical security risks to web applications. It's published by the Open Web Application Security Project based on real-world vulnerability data. The current version is from 2021 and includes vulnerabilities like Broken Access Control, Injection, Cryptographic Failures, and SSRF."

**Q2: Explain SQL Injection and how to prevent it.**
> "SQL Injection occurs when untrusted user input is concatenated into SQL queries, allowing attackers to modify the query logic. Prevention includes using parameterized queries (prepared statements), input validation, ORM frameworks, and least-privilege database accounts."

### Advanced Questions

**Q3: What's the difference between Insecure Design and Security Misconfiguration?**
> "Insecure Design refers to fundamental flaws in the architecture that cannot be fixed by implementing correctly - it requires redesigning the feature. Security Misconfiguration refers to improperly configured security controls in an otherwise well-designed system. For example, no rate limiting is a design flaw; leaving default credentials is misconfiguration."

**Q4: How would you protect an application from the OWASP Top 10?**
> "I would implement a layered defense: Access control with deny-by-default, encryption for sensitive data, parameterized queries for injection prevention, threat modeling during design, security headers and hardening, dependency scanning, MFA and proper session management, code signing and integrity checks, comprehensive logging with alerting, and URL validation with network segmentation for SSRF protection."

---

## Learning Resources

### 📚 Websites

| Website | Link | What You'll Learn |
|---------|------|-------------------|
| **OWASP Official** | https://owasp.org/Top10/ | Official Top 10 documentation |
| **PortSwigger Academy** | https://portswigger.net/web-security | Free interactive labs |
| **HackTheBox Academy** | https://academy.hackthebox.com | Hands-on web security |
| **TryHackMe OWASP** | https://tryhackme.com/room/owasptop10 | Interactive learning |
| **OWASP WebGoat** | https://owasp.org/www-project-webgoat/ | Practice vulnerable app |

### 🎥 YouTube Videos

| Video | Link | Duration |
|-------|------|----------|
| **OWASP Top 10 Explained** | https://www.youtube.com/watch?v=rWHvp7rUka8 | ~25 min |
| **SQL Injection Complete Guide** | https://www.youtube.com/watch?v=1nJgupaUPEQ | ~45 min |
| **Web Security - freeCodeCamp** | https://www.youtube.com/watch?v=F5KJVuii0Yw | 2+ hours |
| **NetworkChuck - Hacking** | https://www.youtube.com/watch?v=3Kq1MIfTWCE | ~30 min |
| **Professor Messer Security+** | https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv | Full Course |

### 📖 Courses

| Course | Platform | Link |
|--------|----------|------|
| **Web Security Testing** | PortSwigger | https://portswigger.net/web-security |
| **Secure Coding in Python** | Pluralsight | https://www.pluralsight.com/courses/secure-coding-python |
| **OWASP Top 10 Course** | Udemy | https://www.udemy.com/course/owasp-top-10-web-application-security/ |
| **Application Security** | Coursera | https://www.coursera.org/learn/application-security |

### 🛠️ Practice Labs

| Lab | Link | Description |
|-----|------|-------------|
| **OWASP WebGoat** | https://owasp.org/www-project-webgoat/ | Intentionally vulnerable app |
| **DVWA** | https://dvwa.co.uk/ | Damn Vulnerable Web Application |
| **HackTheBox** | https://www.hackthebox.com/ | Real hacking challenges |
| **TryHackMe** | https://tryhackme.com/ | Beginner-friendly labs |
| **PortSwigger Labs** | https://portswigger.net/web-security/all-labs | Free web security labs |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              OWASP TOP 10 (2021) QUICK REFERENCE             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A01 BROKEN ACCESS CONTROL                                   │
│      └─ Prevention: Server-side validation, deny by default │
│                                                             │
│  A02 CRYPTOGRAPHIC FAILURES                                  │
│      └─ Prevention: Encrypt data, proper key management     │
│                                                             │
│  A03 INJECTION                                               │
│      └─ Prevention: Parameterized queries, input validation │
│                                                             │
│  A04 INSECURE DESIGN                                         │
│      └─ Prevention: Threat modeling, secure patterns        │
│                                                             │
│  A05 SECURITY MISCONFIGURATION                               │
│      └─ Prevention: Hardening, remove defaults              │
│                                                             │
│  A06 VULNERABLE COMPONENTS                                   │
│      └─ Prevention: Dependency scanning, regular updates    │
│                                                             │
│  A07 AUTHENTICATION FAILURES                                 │
│      └─ Prevention: MFA, rate limiting, secure sessions     │
│                                                             │
│  A08 INTEGRITY FAILURES                                      │
│      └─ Prevention: Digital signatures, secure CI/CD        │
│                                                             │
│  A09 LOGGING FAILURES                                        │
│      └─ Prevention: Comprehensive logging, SIEM             │
│                                                             │
│  A10 SSRF                                                    │
│      └─ Prevention: URL whitelisting, block internal IPs    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Next Topic: [Network Security](../03_Network_Security/01_OSI_Model.md)*
