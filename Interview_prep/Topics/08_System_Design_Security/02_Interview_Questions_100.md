# 🏗️ SYSTEM DESIGN SECURITY - 100 Interview Questions & Answers

## Priority Legend
- 🔴 **HIGH PRIORITY** - Most Probable (Q1-40)
- 🟡 **MEDIUM PRIORITY** - Important Concepts (Q41-70)
- 🟢 **ADVANCED** - Complex/In-Depth (Q71-100)

---

# 🔴 HIGH PRIORITY - Most Probable Questions (1-40)

---

## Q1: What is the CIA Triad and why is it fundamental to system design?
**Answer:**
The CIA Triad is the foundation of information security:

- **Confidentiality**: Only authorized users can access data
- **Integrity**: Data is accurate and unchanged
- **Availability**: Systems are accessible when needed

**In System Design:**
- Confidentiality → Encryption, access control
- Integrity → Hashing, digital signatures, validation
- Availability → Redundancy, failover, DDoS protection

Every security decision should address at least one of these.

---

## Q2: What is Defense in Depth?
**Answer:**
Defense in Depth is a layered security strategy where multiple controls protect assets.

**Layers:**
1. **Physical**: Data center security
2. **Perimeter**: Firewalls, WAF
3. **Network**: Segmentation, IDS/IPS
4. **Host**: Hardening, antivirus
5. **Application**: Input validation, authentication
6. **Data**: Encryption, access control

**Principle:** If one layer fails, others still protect. No single point of failure.

---

## Q3: What is Zero Trust Architecture?
**Answer:**
Zero Trust follows "never trust, always verify" - no implicit trust based on network location.

**Core Principles:**
1. Verify explicitly (always authenticate)
2. Use least privilege access
3. Assume breach

**Implementation:**
- Strong identity verification (MFA)
- Device validation
- Micro-segmentation
- Continuous monitoring
- Encrypt all traffic (even internal)

**Key Difference:** Traditional security trusts internal network; Zero Trust verifies everything.

---

## Q4: What is Least Privilege and how do you implement it?
**Answer:**
**Least Privilege:** Users/systems get only minimum permissions needed for their tasks.

**Implementation:**
- Role-Based Access Control (RBAC)
- Just-In-Time (JIT) access
- Regular access reviews
- Separate admin accounts
- Time-limited elevated privileges

**Example:**
- Developer needs read access to production, not admin
- Service account only gets permissions for specific APIs it calls

---

## Q5: Explain the difference between Authentication and Authorization.
**Answer:**

| Authentication | Authorization |
|----------------|---------------|
| "Who are you?" | "What can you do?" |
| Verifies identity | Verifies permissions |
| Happens first | Happens after authentication |
| Passwords, MFA, biometrics | RBAC, ACLs, policies |
| 401 Unauthorized | 403 Forbidden |

**Example:**
- Authentication: Login with username/password
- Authorization: Admin can delete users, regular user cannot

---

## Q6: What is RBAC vs ABAC?
**Answer:**

**RBAC (Role-Based Access Control):**
- Permissions assigned to roles
- Users assigned to roles
- Simple, static
- Example: Admin, Editor, Viewer roles

**ABAC (Attribute-Based Access Control):**
- Permissions based on attributes
- Dynamic, flexible
- Considers user, resource, environment, action
- Example: "HR employees can access employee records during business hours"

**When to use:**
- RBAC: Simple hierarchies, most applications
- ABAC: Complex policies, dynamic conditions

---

## Q7: How does OAuth 2.0 work?
**Answer:**
OAuth 2.0 is a delegation protocol for authorization.

**Authorization Code Flow:**
1. User clicks "Login with Google"
2. Redirect to Google's auth server
3. User authenticates with Google
4. Google redirects with authorization code
5. Backend exchanges code for tokens
6. Access token used to call API

**Key Components:**
- **Resource Owner**: User
- **Client**: Your application
- **Authorization Server**: Issues tokens
- **Resource Server**: API with protected data

**Tokens:**
- Access Token: Short-lived, access resources
- Refresh Token: Long-lived, get new access tokens

---

## Q8: What is JWT and how is it structured?
**Answer:**
JWT (JSON Web Token) is a compact token format for securely transmitting information.

**Structure:** `header.payload.signature`

```
Header:    {"alg": "HS256", "typ": "JWT"}
Payload:   {"sub": "1234", "name": "John", "exp": 1234567890}
Signature: HMACSHA256(base64(header) + "." + base64(payload), secret)
```

**Security Considerations:**
- Payload is Base64 encoded, NOT encrypted
- Always verify signature
- Set short expiration (exp)
- Use strong secrets
- Consider using JWE for sensitive data

---

## Q9: What is HTTPS and why is it essential?
**Answer:**
HTTPS = HTTP over TLS/SSL, providing:

1. **Encryption**: Data unreadable in transit
2. **Authentication**: Server identity verified by certificate
3. **Integrity**: Data not tampered with

**Why Essential:**
- Protects against MITM attacks
- Prevents eavesdropping
- Browser trust indicators
- SEO ranking factor
- Required for modern APIs (cookies, service workers)

**Modern Standard:** TLS 1.3 (faster, more secure)

---

## Q10: How do you handle passwords securely?
**Answer:**

**NEVER:**
- Store plaintext passwords
- Use MD5, SHA1 (too fast)
- Store reversibly encrypted

**ALWAYS:**
- Use slow hashing algorithms: bcrypt, Argon2, scrypt
- Use unique salt per password
- Enforce password policies
- Implement rate limiting
- Use MFA

**Implementation:**
```python
# Python example with bcrypt
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
# Verify
bcrypt.checkpw(password.encode(), hashed)
```

---

## Q11: What is input validation and why is it critical?
**Answer:**
Input validation ensures data meets expected format before processing.

**Why Critical:**
- Prevents SQL injection
- Prevents XSS
- Prevents command injection
- Prevents buffer overflows

**Best Practices:**
1. **Validate on server** (never trust client)
2. **Whitelist** preferred over blacklist
3. **Validate type, length, format, range**
4. **Encode output** for context
5. **Use parameterized queries**

**Example:**
```javascript
// Bad
const query = `SELECT * FROM users WHERE id = ${userId}`;

// Good - Parameterized
db.query('SELECT * FROM users WHERE id = ?', [userId]);
```

---

## Q12: What is SQL Injection and how do you prevent it?
**Answer:**
**SQL Injection:** Attacker inserts malicious SQL through user input.

**Example:**
```
Input: ' OR '1'='1
Query becomes: SELECT * FROM users WHERE name='' OR '1'='1'
```

**Prevention:**
1. **Parameterized queries/Prepared statements** (primary defense)
2. **ORM with proper usage**
3. **Input validation** (whitelist allowed characters)
4. **Least privilege** for database accounts
5. **WAF** as additional layer

```python
# Safe parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

---

## Q13: What is XSS and how do you prevent it?
**Answer:**
**XSS (Cross-Site Scripting):** Injecting malicious scripts into web pages.

**Types:**
- **Stored**: Script saved in database
- **Reflected**: Script in URL/request
- **DOM-based**: Client-side manipulation

**Prevention:**
1. **Output encoding** (HTML, JavaScript, URL context)
2. **Content Security Policy (CSP)**
3. **HttpOnly cookies** (XSS can't steal session)
4. **Input validation**
5. **Use frameworks with auto-escaping**

**Example:**
```html
<!-- Vulnerable -->
<div>Hello, <?= $username ?></div>

<!-- Safe -->
<div>Hello, <?= htmlspecialchars($username, ENT_QUOTES) ?></div>
```

---

## Q14: What is CSRF and how do you prevent it?
**Answer:**
**CSRF (Cross-Site Request Forgery):** Attacker tricks user into submitting unwanted request.

**Example:**
User logged into bank.com visits malicious site with:
```html
<img src="https://bank.com/transfer?to=attacker&amount=1000">
```

**Prevention:**
1. **CSRF tokens** (random token in form, verified on server)
2. **SameSite cookies** (Strict or Lax)
3. **Verify Origin/Referer headers**
4. **Re-authentication for sensitive actions**

```html
<form method="POST">
    <input type="hidden" name="csrf_token" value="random_token_here">
</form>
```

---

## Q15: What are security headers and which ones are important?
**Answer:**

| Header | Purpose |
|--------|---------|
| **Content-Security-Policy** | Controls resource loading, prevents XSS |
| **X-Content-Type-Options** | Prevents MIME type sniffing |
| **X-Frame-Options** | Prevents clickjacking |
| **Strict-Transport-Security** | Forces HTTPS |
| **X-XSS-Protection** | Browser XSS filter (deprecated) |
| **Referrer-Policy** | Controls referer information |
| **Permissions-Policy** | Controls browser features |

**Example:**
```
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
```

---

## Q16: How do you secure an API?
**Answer:**

**Authentication:**
- OAuth 2.0 / JWT
- API keys (for service-to-service)
- Mutual TLS

**Authorization:**
- Verify permissions on every request
- Don't trust client-side checks

**Transport:**
- HTTPS only
- Certificate validation

**Input/Output:**
- Validate all inputs
- Rate limiting
- Don't expose sensitive data in errors

**Monitoring:**
- Log all requests
- Alert on anomalies

---

## Q17: What is rate limiting and how do you implement it?
**Answer:**
**Rate Limiting:** Restricting number of requests a client can make in a time period.

**Purpose:**
- Prevent brute force attacks
- Prevent DoS
- Control resource usage
- Ensure fair usage

**Algorithms:**
| Algorithm | Description |
|-----------|-------------|
| Fixed Window | X requests per time window |
| Sliding Window | Rolling time window |
| Token Bucket | Tokens added at rate, consumed per request |
| Leaky Bucket | Requests processed at fixed rate |

**Response:** HTTP 429 Too Many Requests

---

## Q18: What is the shared responsibility model in cloud?
**Answer:**
Security responsibilities are divided between cloud provider and customer.

**Provider Handles:**
- Physical security
- Infrastructure
- Hypervisor (IaaS)
- Platform (PaaS)

**Customer Handles:**
- Data
- Identity/Access
- Application security
- Configuration

**Model Varies by Service:**
- **IaaS**: Customer handles most (OS, apps, data)
- **PaaS**: Provider handles platform, customer handles app/data
- **SaaS**: Provider handles most, customer handles data/access

---

## Q19: What is encryption at rest vs in transit?
**Answer:**

**At Rest:**
- Data stored on disk
- Protects against physical theft, unauthorized access
- Methods: AES-256, disk encryption, database encryption
- Examples: AWS S3 encryption, BitLocker

**In Transit:**
- Data moving across networks
- Protects against eavesdropping, MITM
- Methods: TLS/SSL, VPN
- Examples: HTTPS, TLS for database connections

**Best Practice:** Use BOTH - encrypt data at rest AND in transit.

---

## Q20: What is a Web Application Firewall (WAF)?
**Answer:**
WAF is a security appliance that filters HTTP/HTTPS traffic to web applications.

**Protects Against:**
- SQL injection
- XSS
- CSRF
- File inclusion
- Known CVEs

**Modes:**
- **Detection**: Log and alert
- **Prevention**: Block malicious requests

**Deployment:**
- Cloud: AWS WAF, Cloudflare, Azure WAF
- On-premise: ModSecurity, F5

**Limitation:** Not a replacement for secure code - it's an additional layer.

---

## Q21: How do you handle secrets management?
**Answer:**

**DON'T:**
- Hardcode in source code
- Store in version control
- Use environment variables for production

**DO:**
- Use dedicated secrets management tools
- Rotate regularly
- Audit access
- Encrypt at rest

**Tools:**
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager

**Best Practices:**
- Just-in-time access
- Least privilege
- Automatic rotation
- Audit logging

---

## Q22: What is network segmentation?
**Answer:**
Dividing network into segments to control traffic flow and limit breach impact.

**Benefits:**
- Contains breaches (lateral movement prevention)
- Reduces attack surface
- Compliance requirements
- Better monitoring

**Common Segments:**
- **DMZ**: Public-facing servers
- **Internal**: User workstations
- **Database**: Backend data tier
- **Management**: Admin systems

**Implementation:**
- VLANs
- Firewalls between segments
- Security groups (cloud)
- Micro-segmentation (within segments)

---

## Q23: What is a DMZ?
**Answer:**
**DMZ (Demilitarized Zone):** Network segment between external internet and internal network.

**Contents:**
- Web servers
- Mail servers
- DNS servers
- Public APIs

**Architecture:**
```
Internet → Outer Firewall → DMZ → Inner Firewall → Internal Network
```

**Purpose:**
- Expose services without exposing internal network
- Additional security layer
- If DMZ compromised, internal network still protected

---

## Q24: How do you design a secure login system?
**Answer:**

**Components:**
1. **Strong password requirements**
2. **Rate limiting** (prevent brute force)
3. **Account lockout** (temporary)
4. **CAPTCHA** after failed attempts
5. **MFA** (TOTP, hardware keys)
6. **Secure session management**
7. **Secure password storage** (bcrypt)

**Security Features:**
- Account lockout notifications
- Login notifications for new devices
- Session invalidation on password change
- Secure cookies (HttpOnly, Secure, SameSite)

---

## Q25: What is session management and how do you secure it?
**Answer:**
Session management maintains user state across requests.

**Secure Practices:**
1. **Generate secure session IDs** (random, sufficient length)
2. **Use secure cookies**: HttpOnly, Secure, SameSite
3. **Set expiration** (idle and absolute timeout)
4. **Regenerate ID** after login (prevent session fixation)
5. **Invalidate on logout** (server-side)
6. **Protect against CSRF**

**Cookie Flags:**
```
Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict; Path=/
```

---

## Q26: What is the OWASP Top 10?
**Answer:**
OWASP Top 10 is the most critical web application security risks.

**2021 Version:**
1. **A01** - Broken Access Control
2. **A02** - Cryptographic Failures
3. **A03** - Injection
4. **A04** - Insecure Design
5. **A05** - Security Misconfiguration
6. **A06** - Vulnerable Components
7. **A07** - Authentication Failures
8. **A08** - Software and Data Integrity Failures
9. **A09** - Security Logging Failures
10. **A10** - Server-Side Request Forgery

---

## Q27: What is Insecure Direct Object Reference (IDOR)?
**Answer:**
**IDOR:** Accessing resources by manipulating direct references (IDs).

**Example:**
```
GET /api/orders/12345  → User's order
GET /api/orders/12346  → Someone else's order (IDOR!)
```

**Prevention:**
1. **Authorization checks** on every request
2. **Indirect references** (mapped to user context)
3. **Access control lists**
4. **Validate user owns resource**

```python
# Vulnerable
order = Order.get(order_id)

# Secure
order = Order.get(order_id, user_id=current_user.id)
if not order:
    return 403
```

---

## Q28: What is Security Misconfiguration?
**Answer:**
Security issues from improper configuration of systems.

**Examples:**
- Default credentials enabled
- Unnecessary services running
- Verbose error messages
- Directory listing enabled
- Missing security headers
- Outdated software

**Prevention:**
- Hardening checklists (CIS Benchmarks)
- Configuration management (IaC)
- Regular audits
- Automated scanning
- Remove default accounts
- Disable unnecessary features

---

## Q29: How do you handle error messages securely?
**Answer:**

**DON'T expose:**
- Stack traces
- Database errors
- File paths
- System information
- SQL queries

**DO:**
- Log detailed errors server-side
- Show generic user-friendly messages
- Use error codes for support
- Different handling for different environments

**Example:**
```python
try:
    # database operation
except DatabaseError as e:
    log.error(f"Database error: {e}")  # Server log
    return {"error": "An error occurred. Reference: ERR-12345"}  # User response
```

---

## Q30: What is Content Security Policy (CSP)?
**Answer:**
CSP is an HTTP header that controls what resources can be loaded on a page.

**Prevents:**
- XSS attacks
- Data injection
- Clickjacking

**Example:**
```
Content-Security-Policy: 
    default-src 'self'; 
    script-src 'self' https://trusted.com;
    style-src 'self' 'unsafe-inline';
    img-src *;
    frame-ancestors 'none'
```

**Directives:**
- `default-src`: Fallback for all
- `script-src`: JavaScript sources
- `style-src`: CSS sources
- `img-src`: Image sources
- `frame-ancestors`: Prevents clickjacking

---

## Q31: What is a DDoS attack and how do you mitigate it?
**Answer:**
**DDoS (Distributed Denial of Service):** Overwhelming a system with traffic from multiple sources.

**Types:**
- **Volumetric**: Bandwidth exhaustion (UDP flood)
- **Protocol**: Protocol exploit (SYN flood)
- **Application**: HTTP flood, slowloris

**Mitigation:**
1. **CDN/Edge protection** (Cloudflare, AWS Shield)
2. **Rate limiting**
3. **Geographic filtering**
4. **CAPTCHA** for suspicious traffic
5. **Over-provisioning**
6. **Anycast network**
7. **WAF rules**

---

## Q32: What is Secure SDLC?
**Answer:**
Integrating security throughout the Software Development Lifecycle.

**Phases:**
| Phase | Security Activity |
|-------|-------------------|
| Requirements | Security requirements, risk assessment |
| Design | Threat modeling, security architecture |
| Development | Secure coding, SAST, code review |
| Testing | DAST, penetration testing |
| Deployment | Secure configuration, secrets management |
| Operations | Monitoring, incident response, patching |

**Benefits:**
- Catch issues early (cheaper to fix)
- Security built-in, not bolted-on
- Reduced vulnerabilities in production

---

## Q33: What is Threat Modeling?
**Answer:**
Structured approach to identifying and addressing security threats.

**Common Frameworks:**
- **STRIDE**: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- **PASTA**: Process for Attack Simulation and Threat Analysis
- **DREAD**: Damage, Reproducibility, Exploitability, Affected Users, Discoverability

**Process:**
1. Diagram the system
2. Identify threats (STRIDE)
3. Rate risks
4. Define mitigations
5. Validate

---

## Q34: What is SAST vs DAST?
**Answer:**

| SAST (Static) | DAST (Dynamic) |
|---------------|----------------|
| Analyzes source code | Tests running application |
| White box | Black box |
| Early in SDLC | Later in SDLC |
| Finds code-level issues | Finds runtime issues |
| Many false positives | More accurate |
| Tools: SonarQube, Checkmarx | Tools: OWASP ZAP, Burp Suite |

**Best Practice:** Use both - SAST early, DAST before release.

---

## Q35: What is Software Composition Analysis (SCA)?
**Answer:**
SCA identifies and manages open-source components in your codebase.

**Checks:**
- Known vulnerabilities (CVEs)
- License compliance
- Outdated versions

**Tools:**
- Snyk
- Dependabot
- OWASP Dependency-Check
- WhiteSource

**Why Important:**
- 80%+ of code is open source dependencies
- Supply chain attacks increasing
- Compliance requirements

---

## Q36: How do you secure microservices?
**Answer:**

**Challenges:**
- Large attack surface
- Service-to-service auth
- Network complexity

**Solutions:**
1. **Service mesh** (Istio, Linkerd) for mTLS
2. **API gateway** for edge security
3. **Zero Trust** between services
4. **JWT/OAuth** for authentication
5. **Network policies** (Kubernetes)
6. **Secrets management**
7. **Container security**

---

## Q37: What is mTLS (Mutual TLS)?
**Answer:**
**mTLS:** Both client and server present certificates for authentication.

**Standard TLS:**
- Server proves identity to client
- Client not verified

**Mutual TLS:**
- Server proves identity to client
- Client proves identity to server
- Bidirectional authentication

**Use Cases:**
- Microservices communication
- Zero Trust networks
- API authentication
- IoT devices

---

## Q38: What is an API Gateway?
**Answer:**
API Gateway is an entry point that handles cross-cutting concerns for APIs.

**Security Functions:**
- Authentication/Authorization
- Rate limiting
- Input validation
- SSL termination
- Request/response transformation
- Logging and monitoring
- WAF integration

**Popular Solutions:**
- Kong
- AWS API Gateway
- Azure API Management
- Apigee

---

## Q39: How do you secure containers?
**Answer:**

**Image Security:**
- Use minimal base images (alpine, distroless)
- Scan for vulnerabilities (Trivy, Clair)
- Don't run as root
- Sign images

**Runtime Security:**
- Read-only filesystem
- Resource limits
- Network policies
- Seccomp profiles
- No privileged containers

**Orchestration:**
- Role-Based Access Control
- Pod Security Policies/Standards
- Network segmentation
- Secrets management

---

## Q40: What is Infrastructure as Code (IaC) security?
**Answer:**
Security practices for infrastructure defined in code (Terraform, CloudFormation).

**Risks:**
- Misconfigurations
- Hardcoded secrets
- Overly permissive rules
- Drift from secure baseline

**Security Measures:**
1. **Scan IaC** (checkov, tfsec, Snyk IaC)
2. **Secrets detection** (git-secrets, truffleHog)
3. **Policy as Code** (OPA, Sentinel)
4. **Version control** and review
5. **Drift detection**

---

# 🟡 MEDIUM PRIORITY - Important Concepts (41-70)

---

## Q41: Explain SSL/TLS handshake.
**Answer:**

1. **Client Hello**: Supported cipher suites, TLS version
2. **Server Hello**: Chosen cipher, certificate
3. **Certificate Verification**: Client validates server cert
4. **Key Exchange**: Client sends pre-master secret (RSA) or Diffie-Hellman
5. **Session Keys**: Both derive symmetric keys
6. **Finished**: Verify handshake integrity
7. **Encrypted Communication**: Using symmetric keys

**TLS 1.3 Improvements:**
- 1-RTT handshake (faster)
- 0-RTT resumption
- Removed weak ciphers

---

## Q42: What is Perfect Forward Secrecy?
**Answer:**
**PFS:** Compromise of long-term keys doesn't compromise past session keys.

**How it works:**
- Ephemeral key exchange (DH or ECDH)
- New keys per session
- Past traffic remains secure

**Cipher suites with PFS:**
- ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)
- DHE (Diffie-Hellman Ephemeral)

**Without PFS:** If private key leaked, all past traffic can be decrypted.

---

## Q43: What is certificate pinning?
**Answer:**
**Certificate Pinning:** Hardcoding expected certificate/public key in application.

**Benefits:**
- Prevents MITM attacks
- Doesn't trust entire CA chain
- Protection against CA compromise

**Challenges:**
- Certificate rotation requires app updates
- Difficult to manage at scale
- Can break debugging/proxying

**Alternatives:**
- Certificate Transparency monitoring
- Short-lived certificates
- CAA records

---

## Q44: How do you implement MFA securely?
**Answer:**

**Methods (strongest to weakest):**
1. Hardware keys (FIDO2/WebAuthn)
2. Authenticator apps (TOTP)
3. Push notifications
4. SMS (avoid if possible)

**Implementation Considerations:**
- Backup codes (stored securely)
- Recovery process
- Remember device options
- MFA bypass prevention
- Phishing-resistant MFA (FIDO2)

**TOTP Implementation:**
- Share secret during setup (QR code)
- Time-based codes (30 seconds)
- Allow clock skew tolerance

---

## Q45: What is Single Sign-On (SSO)?
**Answer:**
**SSO:** One authentication grants access to multiple applications.

**Protocols:**
- **SAML 2.0**: XML-based, enterprise (Identity Provider initiated)
- **OIDC/OAuth 2.0**: Modern, REST-based (Token-based)

**Benefits:**
- Better user experience
- Centralized authentication
- Stronger security policies
- Easier offboarding

**Security Considerations:**
- SSO is single point of failure
- Protect IdP heavily
- Session management across apps
- Token security

---

## Q46: What is SAML vs OIDC?
**Answer:**

| Aspect | SAML | OIDC |
|--------|------|------|
| Format | XML | JSON |
| Year | 2005 | 2014 |
| Transport | HTTP POST/Redirect | HTTP, REST |
| Tokens | Assertions | JWT |
| Use Case | Enterprise SSO | Modern apps, mobile |
| Complexity | More complex | Simpler |

**When to use:**
- SAML: Enterprise, legacy systems
- OIDC: Modern apps, APIs, mobile

---

## Q47: How do you implement secure password reset?
**Answer:**

**Secure Flow:**
1. User requests reset
2. Generate secure random token
3. Store token hash with expiration
4. Send link via email
5. User clicks link, enters new password
6. Verify token, invalidate after use
7. Notify user of change

**Security Measures:**
- Rate limit requests
- Don't reveal if account exists
- Short token expiration (1 hour)
- Invalidate existing sessions
- Log and alert

---

## Q48: What is CORS and why is it important?
**Answer:**
**CORS (Cross-Origin Resource Sharing):** Browser security limiting cross-origin requests.

**Same-Origin Policy:** Browser restricts scripts from making requests to different origins.

**CORS Headers:**
```
Access-Control-Allow-Origin: https://trusted.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
```

**Security Concerns:**
- Avoid `Access-Control-Allow-Origin: *` with credentials
- Validate origin header
- Don't reflect any origin

---

## Q49: What is Clickjacking and how do you prevent it?
**Answer:**
**Clickjacking:** Tricking users to click hidden elements by overlaying transparent iframes.

**Prevention:**
1. **X-Frame-Options header:**
   ```
   X-Frame-Options: DENY
   X-Frame-Options: SAMEORIGIN
   ```

2. **Content-Security-Policy:**
   ```
   Content-Security-Policy: frame-ancestors 'none'
   ```

3. **JavaScript frame-busting** (legacy)

---

## Q50: What is SSRF and how do you prevent it?
**Answer:**
**SSRF (Server-Side Request Forgery):** Attacker makes server send requests to unintended destinations.

**Risks:**
- Access internal services
- Cloud metadata endpoints
- Port scanning internal network

**Prevention:**
1. **Whitelist** allowed URLs/domains
2. **Block** internal IP ranges (10.x, 192.168.x, 169.254.x)
3. **Disable** redirects or validate destinations
4. **Use** network segmentation
5. **Block** cloud metadata IPs

```python
# Block internal IPs
import ipaddress
ip = ipaddress.ip_address(hostname)
if ip.is_private or ip.is_loopback:
    raise BlockedError()
```

---

## Q51: How do you secure file uploads?
**Answer:**

**Validations:**
1. **File type**: Check magic bytes, not just extension
2. **File size**: Enforce limits
3. **Filename**: Sanitize, generate new name
4. **Content scanning**: Antivirus

**Storage:**
- Store outside webroot
- Use random filenames
- Separate domain for serving files
- Set proper Content-Type
- Consider CDN

**Prevent:**
- Path traversal (../)
- Executable uploads
- File inclusion attacks

---

## Q52: What is SQL Injection in stored procedures?
**Answer:**
Even stored procedures can be vulnerable if they build dynamic SQL.

**Vulnerable:**
```sql
CREATE PROCEDURE GetUser @name VARCHAR(100)
AS
    EXEC('SELECT * FROM users WHERE name = ''' + @name + '''')
```

**Safe:**
```sql
CREATE PROCEDURE GetUser @name VARCHAR(100)
AS
    SELECT * FROM users WHERE name = @name
```

**Key:** Parameterization must happen at the query execution level, not just at the API level.

---

## Q53: What is NoSQL injection?
**Answer:**
**NoSQL Injection:** Exploiting NoSQL databases through injected operators.

**MongoDB Example:**
```javascript
// Vulnerable
db.users.find({name: req.query.name})

// Attack: ?name[$ne]=anything (returns all users)
{name: {$ne: "anything"}}
```

**Prevention:**
- Input validation (type checking)
- Sanitize operators
- Use parameterized queries
- ORM/ODM protections

---

## Q54: What is XML External Entity (XXE)?
**Answer:**
**XXE:** Exploiting XML parsers to include external entities.

**Attack:**
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>&xxe;</data>
```

**Prevention:**
- Disable external entity processing
- Disable DTD processing
- Use JSON instead of XML
- Validate and sanitize XML

**Fix (Java):**
```java
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

---

## Q55: What is deserialization attack?
**Answer:**
**Deserialization Attack:** Exploiting unsafe deserialization to execute code.

**Risk:** Untrusted data deserialized can instantiate arbitrary objects.

**Prevention:**
- Don't deserialize untrusted data
- Use safe formats (JSON instead of native serialization)
- Integrity checks (signing)
- Restrict deserializable classes
- Update libraries

**Affected Languages:** Java, .NET, PHP, Python, Ruby

---

## Q56: How do you implement secure logging?
**Answer:**

**Log:**
- Authentication events (login, logout, failures)
- Authorization decisions
- Input validation failures
- Security events
- Errors and exceptions

**DON'T Log:**
- Passwords
- Session tokens
- Credit card numbers
- PII without masking

**Security:**
- Centralized logging (SIEM)
- Tamper protection
- Retention policies
- Access control

**Format:** Include timestamp, user, action, outcome, source IP

---

## Q57: What is log injection and how to prevent it?
**Answer:**
**Log Injection:** Injecting malicious content into logs.

**Risks:**
- Log forging (fake entries)
- CRLF injection (new log lines)
- Log4Shell (code execution)

**Prevention:**
- Sanitize user input before logging
- Encode newlines (\n, \r)
- Use structured logging (JSON)
- Validate data types

**Example:**
```python
# Bad
logger.info(f"User login: {username}")

# If username = "admin\n2024-01-01 - User transfer: $1000000"
# Creates fake log entry
```

---

## Q58: What is a Replay Attack and how to prevent it?
**Answer:**
**Replay Attack:** Capturing and retransmitting valid data to perform unauthorized actions.

**Prevention:**
1. **Timestamps**: Reject old requests (>5 min)
2. **Nonces**: One-time use tokens
3. **Sequence numbers**: Track and reject duplicates
4. **Challenge-response**: Fresh challenge each time
5. **Signed requests**: Include timestamp in signature

**API Implementation:**
```
Request header: X-Timestamp: 1640000000
Request header: X-Signature: HMAC(body + timestamp, secret)
```

---

## Q59: What is security monitoring and why is it important?
**Answer:**
**Security Monitoring:** Continuous observation of systems for security events.

**Components:**
- Log aggregation
- Event correlation
- Anomaly detection
- Alerting
- Incident response

**Key Metrics:**
- Failed authentication attempts
- Privilege escalations
- Access to sensitive data
- Configuration changes
- Unusual traffic patterns

**Tools:** SIEM (Splunk, ELK), EDR, UEBA

---

## Q60: What is the principle of Fail Secure vs Fail Open?
**Answer:**

**Fail Secure (Fail Closed):**
- When system fails, deny access
- More secure but may impact availability
- Example: Firewall crashes → block all traffic

**Fail Open:**
- When system fails, allow access
- Maintains availability but less secure
- Example: Badge system fails → doors unlock

**Best Practice:** Default to fail secure for security systems unless safety requires fail open (fire exits).

---

## Q61: How do you handle sensitive data exposure?
**Answer:**

**Identify Sensitive Data:**
- PII, financial, health data
- Credentials, tokens
- Business-critical data

**Protections:**
1. **Classification**: Know what's sensitive
2. **Encryption**: At rest and in transit
3. **Access control**: Minimum necessary
4. **Masking**: In logs, displays
5. **Retention**: Don't keep longer than needed
6. **Disposal**: Secure deletion

**Compliance:** GDPR, PCI-DSS, HIPAA have specific requirements

---

## Q62: What is data masking?
**Answer:**
**Data Masking:** Obscuring sensitive data while maintaining usability.

**Types:**
- **Static**: Permanent transformation for non-prod
- **Dynamic**: On-the-fly masking based on user role
- **Tokenization**: Replace with tokens, maintain mapping

**Examples:**
```
Credit Card: 1234-5678-9012-3456 → ****-****-****-3456
SSN: 123-45-6789 → ***-**-6789
Email: john.doe@email.com → j***@email.com
```

---

## Q63: What is key management?
**Answer:**
**Key Management:** Lifecycle management of cryptographic keys.

**Lifecycle:**
1. **Generation**: Use secure random sources
2. **Distribution**: Secure channels
3. **Storage**: HSM, key vault
4. **Rotation**: Regular schedule
5. **Backup**: Secure, encrypted
6. **Revocation**: When compromised
7. **Destruction**: Secure erasure

**Services:**
- AWS KMS
- Azure Key Vault
- HashiCorp Vault
- Hardware Security Modules (HSM)

---

## Q64: What is HSM (Hardware Security Module)?
**Answer:**
**HSM:** Physical device for secure key storage and crypto operations.

**Features:**
- Tamper-resistant hardware
- Keys never leave HSM
- FIPS 140-2 certified
- High-speed crypto operations

**Use Cases:**
- Certificate Authority
- Payment processing
- Database encryption keys
- Code signing

**Cloud Equivalents:**
- AWS CloudHSM
- Azure Dedicated HSM
- Google Cloud HSM

---

## Q65: How do you implement audit logging for compliance?
**Answer:**

**Requirements:**
- Who did what, when, where
- Immutable records
- Retention periods
- Access control

**Implementation:**
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "user_id": "user123",
  "action": "read",
  "resource": "customer_record",
  "resource_id": "cust456",
  "ip_address": "192.168.1.100",
  "outcome": "success"
}
```

**Protection:**
- Centralized, separate system
- Write-once storage
- Digital signatures
- Access restricted

---

## Q66: What is Security Information and Event Management (SIEM)?
**Answer:**
**SIEM:** Platform for collecting, analyzing, and responding to security events.

**Functions:**
1. **Collection**: Aggregate logs from all sources
2. **Normalization**: Standard format
3. **Correlation**: Connect related events
4. **Analysis**: Detect threats
5. **Alerting**: Notify on incidents
6. **Dashboards**: Visualization
7. **Compliance**: Reporting

**Popular Solutions:**
- Splunk
- Microsoft Sentinel
- IBM QRadar
- Elastic Security

---

## Q67: What is the difference between IDS and IPS?
**Answer:**

| IDS (Intrusion Detection) | IPS (Intrusion Prevention) |
|---------------------------|----------------------------|
| Detection only | Detection + Prevention |
| Passive monitoring | Inline (active) |
| Alerts on threats | Blocks threats |
| No latency impact | May add latency |
| Post-attack visibility | Real-time blocking |

**Deployment:**
- IDS: Mirror/tap traffic (out of band)
- IPS: Inline (traffic flows through)

---

## Q68: What is vulnerability management?
**Answer:**
Continuous process of identifying, evaluating, and addressing vulnerabilities.

**Process:**
1. **Discovery**: Asset inventory
2. **Scanning**: Automated vulnerability scans
3. **Assessment**: Prioritize by risk
4. **Remediation**: Patch, configure, accept
5. **Verification**: Rescan to confirm fix
6. **Documentation**: Track and report

**Prioritization Factors:**
- CVSS score
- Exploitability
- Business impact
- Asset exposure

---

## Q69: What is penetration testing methodology?
**Answer:**

**Phases:**
1. **Planning**: Scope, rules of engagement
2. **Reconnaissance**: Passive/active information gathering
3. **Scanning**: Port scanning, vulnerability scanning
4. **Exploitation**: Attempt to exploit vulnerabilities
5. **Post-Exploitation**: Pivot, escalate, exfiltrate
6. **Reporting**: Document findings, recommendations

**Types:**
- Black Box: No prior knowledge
- White Box: Full access to code/docs
- Gray Box: Some information provided

---

## Q70: What is bug bounty program?
**Answer:**
**Bug Bounty:** Reward program for reporting security vulnerabilities.

**Benefits:**
- Crowdsourced security testing
- Continuous testing
- Cost-effective
- Diverse skill sets

**Components:**
- Scope definition
- Rules of engagement
- Reward structure
- Responsible disclosure policy

**Platforms:**
- HackerOne
- Bugcrowd
- Synack

---

# 🟢 ADVANCED - Complex/In-Depth Questions (71-100)

---

## Q71: How would you design a secure authentication system from scratch?
**Answer:**

**Components:**
1. **Registration**
   - Email verification
   - Password requirements (length, complexity)
   - bcrypt hashing with unique salt
   - Rate limiting

2. **Login**
   - Username enumeration prevention
   - Rate limiting/account lockout
   - MFA requirement
   - Secure session creation
   - Device fingerprinting

3. **Session Management**
   - Secure random session IDs
   - HttpOnly, Secure, SameSite cookies
   - Idle/absolute timeout
   - Session invalidation

4. **Password Reset**
   - Secure token generation
   - Time-limited tokens
   - Email verification
   - Old session invalidation

5. **Security Features**
   - Login notifications
   - Session listing
   - Trusted devices
   - Security questions (optional, weak)

---

## Q72: Design a secure API rate limiting system.
**Answer:**

**Requirements:**
- Per-user limiting
- Per-IP limiting (unauthenticated)
- Different limits for different endpoints
- Graceful degradation

**Architecture:**
```
Request → API Gateway → Rate Limiter (Redis) → Service
```

**Implementation:**
- Token Bucket algorithm
- Redis for distributed state
- Sliding window for accuracy

**Limits:**
```yaml
endpoints:
  /api/login:
    requests: 10
    per: minute
  /api/data:
    requests: 100
    per: minute
```

**Response:**
- 429 Too Many Requests
- Retry-After header
- Rate limit headers (X-RateLimit-*)

---

## Q73: How would you implement secure file storage?
**Answer:**

**Architecture:**
```
Client → API → File Service → Object Storage (S3)
```

**Security Measures:**
1. **Upload**
   - Validate file type (magic bytes)
   - Size limits
   - Antivirus scanning
   - Generate random filename
   - Encrypt before storage

2. **Storage**
   - Encryption at rest (SSE-S3, SSE-KMS)
   - Separate bucket from application
   - Private by default
   - Versioning for recovery

3. **Download**
   - Authorization check
   - Pre-signed URLs with expiration
   - Serve from different domain (XSS protection)
   - Content-Disposition header

---

## Q74: Design a secure multi-tenant architecture.
**Answer:**

**Isolation Models:**
1. **Separate databases**: Strongest isolation
2. **Separate schemas**: Good isolation
3. **Shared tables with tenant_id**: Lowest isolation, most efficient

**Security Measures:**
- Tenant ID in every query
- Row-level security
- Separate encryption keys per tenant
- Audit logging per tenant
- Network isolation (for high security)

**Access Control:**
```python
# Every query includes tenant check
def get_data(tenant_id, user_id):
    # Verify user belongs to tenant
    if not user_has_tenant_access(user_id, tenant_id):
        raise Forbidden
    # Include tenant_id in query
    return db.query(f"SELECT * FROM data WHERE tenant_id = ?", tenant_id)
```

---

## Q75: How do you design secure microservices communication?
**Answer:**

**Authentication:**
- mTLS (service mesh: Istio, Linkerd)
- JWT tokens (propagated)
- Service accounts

**Authorization:**
- Central policy engine (OPA)
- Service-to-service ACLs
- Scope-based access

**Transport:**
- Encrypt all internal traffic
- Certificate rotation
- No trust based on network location

**Observability:**
- Distributed tracing
- Centralized logging
- Request ID propagation

---

## Q76: Design a secure secret rotation system.
**Answer:**

**Requirements:**
- Zero-downtime rotation
- Automated process
- Audit trail
- Rollback capability

**Process:**
1. Generate new secret
2. Update secret manager
3. Enable dual-secret acceptance (overlap period)
4. Roll out to services
5. Verify new secret usage
6. Disable old secret
7. Log and notify

**Implementation:**
```yaml
rotation:
  database_passwords:
    frequency: 30 days
    overlap_period: 1 hour
    notification: ops@company.com
```

---

## Q77: How do you implement Zero Trust for internal applications?
**Answer:**

**Components:**

1. **Identity**: Strong authentication for every request
   - MFA required
   - Continuous verification

2. **Device**: Verify device security posture
   - Managed device requirement
   - Endpoint protection status
   - Patch level

3. **Network**: Micro-segmentation
   - No implicit trust
   - Least privilege network access
   - Encrypted internal traffic

4. **Application**: Per-application authorization
   - Context-aware access
   - Just-in-time access

5. **Data**: Encryption and classification
   - Encrypt everywhere
   - DLP controls

**Tools:** BeyondCorp, Zscaler, Okta, Azure AD Conditional Access

---

## Q78: Design an incident response system.
**Answer:**

**Components:**

1. **Detection**
   - SIEM correlation rules
   - EDR alerts
   - User reports
   - Automated anomaly detection

2. **Triage**
   - Severity classification
   - Initial assessment
   - Escalation procedures

3. **Response**
   - Playbook automation
   - Communication (internal, external)
   - Containment actions
   - Evidence preservation

4. **Recovery**
   - System restoration
   - Verification
   - Monitoring

5. **Post-Incident**
   - Root cause analysis
   - Lessons learned
   - Control improvements

**Automation:**
- SOAR platforms (Phantom, XSOAR)
- Automated containment
- Ticket creation

---

## Q79: How do you secure a CI/CD pipeline?
**Answer:**

**Pipeline Security:**

1. **Source Code**
   - Protected branches
   - Code review requirements
   - Signed commits

2. **Build**
   - Ephemeral build environments
   - Dependency scanning (SCA)
   - SAST scanning
   - No secrets in code

3. **Test**
   - DAST scanning
   - Security unit tests
   - Container scanning

4. **Deploy**
   - Secrets injection (Vault)
   - Image signing
   - Infrastructure scanning
   - Immutable deployments

5. **Runtime**
   - Monitoring
   - Runtime protection
   - Drift detection

**Principles:**
- Least privilege for CI/CD system
- Audit everything
- Separate production credentials

---

## Q80: Design a secure logging architecture.
**Answer:**

**Architecture:**
```
Applications → Log Agents → Log Aggregator → SIEM/Storage
```

**Components:**

1. **Collection**
   - Structured logging (JSON)
   - Include correlation IDs
   - PII masking at source

2. **Transport**
   - TLS encryption
   - Authentication
   - Reliable delivery

3. **Storage**
   - Immutable/append-only
   - Encryption at rest
   - Retention policies
   - Access controls

4. **Analysis**
   - SIEM integration
   - Alerting rules
   - Dashboard

**Log Content:**
- Timestamp, hostname, service
- User ID, request ID
- Action, outcome
- Masked sensitive data

---

## Q81: How do you design defense against insider threats?
**Answer:**

**Prevention:**
1. **Access Control**: Least privilege
2. **Separation of Duties**: Split critical functions
3. **Background Checks**: For sensitive positions
4. **Clean Desk Policy**: Physical security
5. **DLP**: Data Loss Prevention

**Detection:**
1. **UEBA**: User behavior analytics
2. **Audit Logging**: Comprehensive logs
3. **Anomaly Detection**: Unusual access patterns
4. **Privileged Session Monitoring**: Record admin actions

**Response:**
1. Quick access revocation
2. Forensic capability
3. Incident procedures

---

## Q82: Design a secure backup system.
**Answer:**

**3-2-1 Rule:**
- 3 copies of data
- 2 different media types
- 1 offsite location

**Security:**
1. Encryption at rest and in transit
2. Separate backup credentials
3. Immutable backups (prevent ransomware)
4. Access controls
5. Integrity verification

**Testing:**
- Regular restore tests
- Documented procedures
- Recovery time objectives

**Air-Gapped Backups:**
- Offline copies for ransomware protection

---

## Q83: How do you implement security for serverless functions?
**Answer:**

**Challenges:**
- Short-lived
- Limited visibility
- Shared responsibility

**Security Measures:**

1. **Code**
   - Input validation
   - Secure dependencies
   - No hardcoded secrets

2. **Configuration**
   - Least privilege IAM roles
   - Short timeouts
   - Memory limits
   - VPC for internal resources

3. **Secrets**
   - Environment variables from secrets manager
   - Encrypted

4. **Monitoring**
   - Function-level logging
   - Tracing
   - Anomaly detection

**Tools:** AWS Lambda Power Tuning, Serverless Framework security plugins

---

## Q84: Design a secure data pipeline.
**Answer:**

**Security at Each Stage:**

1. **Ingestion**
   - Validate data format
   - Schema enforcement
   - Authentication for data sources

2. **Processing**
   - Encrypted in transit
   - Data masking/anonymization
   - Access controls on processing systems

3. **Storage**
   - Encryption at rest
   - Column-level encryption for sensitive fields
   - Access logging

4. **Quality**
   - Data validation
   - Anomaly detection
   - Lineage tracking

5. **Consumption**
   - Row-level security
   - Column masking by role
   - Audit access

---

## Q85: How do you implement secure GraphQL APIs?
**Answer:**

**Unique Risks:**
- Complex queries (DoS)
- Introspection exposure
- Authorization complexity

**Security Measures:**

1. **Query Depth Limiting**: Prevent deeply nested queries
2. **Query Complexity Analysis**: Score and limit complexity
3. **Rate Limiting**: Per-user, per-query
4. **Disable Introspection**: In production
5. **Authorization**: Field-level permission checks
6. **Input Validation**: Type system helps but validate more

```graphql
# Example depth limiting
# Blocked: deeply nested
query {
  users {
    posts {
      comments {
        author {
          posts { ... }
        }
      }
    }
  }
}
```

---

## Q86: Design secure mobile app backend.
**Answer:**

**Authentication:**
- OAuth 2.0 with PKCE (no client secret)
- Biometric authentication
- Short-lived tokens
- Refresh token rotation

**Transport:**
- Certificate pinning
- TLS 1.3

**API Security:**
- Rate limiting
- Device attestation (Android SafetyNet, iOS DeviceCheck)
- Request signing

**Data:**
- Minimize data on device
- Secure local storage (Keychain, Keystore)
- Encrypted backups

---

## Q87: How do you handle security for WebSocket connections?
**Answer:**

**Security Measures:**

1. **Authentication**
   - Token in initial connection
   - Re-validate periodically
   - No token in URL (logged)

2. **Authorization**
   - Check permissions for each message type
   - Channel/room authorization

3. **Transport**
   - WSS (WebSocket Secure) only
   - Origin validation

4. **Input Validation**
   - Validate all messages
   - Rate limit messages
   - Size limits

5. **Connection Management**
   - Idle timeouts
   - Maximum connections per user

---

## Q88: Design a secure payment processing system.
**Answer:**

**PCI-DSS Requirements:**
- Never store full card data
- Tokenization
- Encryption
- Network segmentation
- Logging

**Architecture:**
```
Client → Your App → Payment Gateway → Processor
           ↓
        Tokenization
```

**Security Measures:**
1. Use tokenization (never handle raw card data)
2. Payment gateway handles PCI compliance
3. HTTPS everywhere
4. Strong authentication
5. Fraud detection
6. Audit logging
7. PCI-DSS compliance scope reduction

---

## Q89: How do you implement API versioning securely?
**Answer:**

**Versioning Strategies:**
- URL path: `/v1/users`
- Header: `API-Version: 1`
- Query: `?version=1`

**Security Considerations:**

1. **Sunset Deprecated Versions**
   - Security vulnerabilities in old versions
   - Force upgrade path

2. **Consistent Security Controls**
   - Same auth across versions
   - Don't leave old versions unpatched

3. **Documentation**
   - Clear deprecation timeline
   - Migration guides

4. **Monitoring**
   - Track version usage
   - Alert on deprecated version use

---

## Q90: Design a secure customer data export (GDPR right to access).
**Answer:**

**Requirements:**
- Complete data export
- Machine-readable format (JSON, CSV)
- Secure delivery
- Identity verification

**Process:**
1. Authenticate request (strong auth, MFA)
2. Verify identity (may require additional verification)
3. Queue export job
4. Generate encrypted archive
5. Secure delivery (secure link, encryption)
6. Link expires after short period
7. Audit logging

**Security:**
- Don't include other users' data
- Encrypt export file
- Short-lived download links
- Rate limit requests

---

## Q91: How do you implement secure data deletion (GDPR right to erasure)?
**Answer:**

**Challenges:**
- Data in multiple systems
- Backups contain data
- Legal retention requirements

**Implementation:**

1. **Catalog Data Locations**
   - All databases
   - Caches
   - Analytics
   - Logs
   - Backups
   - Third parties

2. **Deletion Process**
   - Soft delete first
   - Cascade to related data
   - Remove from caches
   - Mark in backups (restore with deletion)
   - Anonymize where deletion not possible

3. **Verification**
   - Confirm deletion
   - Provide certification

4. **Exclusions**
   - Legal requirements
   - Legitimate business needs (documented)

---

## Q92: Design a secure OAuth 2.0 implementation.
**Answer:**

**Best Practices:**

1. **Use Authorization Code + PKCE**
   - No implicit flow
   - Code exchange with PKCE challenge

2. **Token Security**
   - Short access token lifetime (minutes)
   - Long refresh token (rotate on use)
   - Refresh token binding

3. **State Parameter**
   - Prevent CSRF
   - Unique per request

4. **Redirect URI Validation**
   - Exact match, no wildcards
   - HTTPS required

5. **Scope Minimization**
   - Request minimum scopes
   - Incremental authorization

---

## Q93: How do you secure webhook implementations?
**Answer:**

**Receiving Webhooks:**
1. **Signature Verification**: Validate HMAC signature
2. **Timestamp Validation**: Prevent replay (reject old)
3. **IP Whitelisting**: If provider publishes IPs
4. **Idempotency**: Handle duplicate deliveries
5. **Async Processing**: Don't block on handling

**Sending Webhooks:**
1. **Sign Payloads**: HMAC-SHA256
2. **Include Timestamp**: In signature
3. **HTTPS Only**: Validate certificates
4. **Retry Logic**: With backoff
5. **Secret Rotation**: Support multiple secrets

```python
# Verification example
expected_sig = hmac.new(secret, timestamp + payload, sha256).hexdigest()
if not hmac.compare_digest(expected_sig, received_sig):
    raise InvalidSignature
```

---

## Q94: Design security for a real-time messaging system.
**Answer:**

**End-to-End Encryption (E2EE):**
- Public/private key pairs per user
- Key exchange on connection
- Server cannot read messages
- Forward secrecy with ratcheting

**Server Security:**
- Authentication on connect
- Authorization for channels
- Rate limiting
- Message validation
- Abuse detection

**Metadata Protection:**
- Minimize stored metadata
- Encrypted message timestamps
- Anonymous delivery (optional)

**Key Management:**
- Device key sync
- Key backup (optional)
- Account recovery

---

## Q95: How do you implement secure search?
**Answer:**

**Challenges:**
- Search exposes data patterns
- Encryption complicates search
- Authorization per result

**Approaches:**

1. **Searchable Encryption**
   - Homomorphic encryption
   - Limited operations

2. **Search Authorization**
   - Filter results by user permissions
   - Row-level security in database

3. **Query Validation**
   - Prevent injection
   - Limit result size
   - Rate limiting

4. **Audit**
   - Log search queries
   - Monitor for data harvesting

---

## Q96: Design a secure service mesh.
**Answer:**

**Components:**

1. **mTLS Everywhere**
   - Certificate per service
   - Automatic rotation
   - CA management

2. **Authorization Policies**
   - Service-to-service rules
   - Method-level control

3. **Observability**
   - Distributed tracing
   - Access logging
   - Metrics

4. **Implementations:**
   - Istio
   - Linkerd
   - Consul Connect

**Example Policy:**
```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
spec:
  rules:
  - from:
    - source:
        principals: ["service-a"]
    to:
    - operation:
        methods: ["GET"]
        paths: ["/api/*"]
```

---

## Q97: How do you implement security for edge computing?
**Answer:**

**Challenges:**
- Physical access risks
- Limited resources
- Network connectivity

**Security Measures:**

1. **Device Security**
   - Secure boot
   - Hardware security module (TPM)
   - Encrypted storage

2. **Communication**
   - mTLS to cloud
   - Certificate pinning
   - Offline capability

3. **Updates**
   - Signed firmware
   - Rollback protection
   - Secure update channel

4. **Access Control**
   - Local authentication
   - Remote management security
   - Audit logging (synced when connected)

---

## Q98: Design a secure identity federation.
**Answer:**

**Components:**

1. **Identity Providers (IdPs)**
   - Multiple external providers (Google, Azure AD)
   - Internal IdP

2. **Federation Hub**
   - Normalize claims
   - Just-in-time provisioning
   - Attribute mapping

3. **Service Providers (SPs)**
   - Trust federation assertions
   - Local authorization

**Security:**
- Signed assertions (SAML) or tokens (JWT)
- Short validity periods
- Token binding
- Consistent MFA requirements

**Protocols:**
- SAML 2.0
- OIDC Federation
- WS-Federation

---

## Q99: How do you implement privacy by design?
**Answer:**

**Principles:**

1. **Proactive**: Build privacy in from start
2. **Default Settings**: Privacy-friendly defaults
3. **Embedded**: Part of design, not add-on
4. **Win-Win**: Security AND functionality
5. **Lifecycle**: Protection throughout data lifecycle
6. **Visibility**: Open and transparent
7. **User-Centric**: Respect user interests

**Implementation:**
- Privacy Impact Assessment
- Data minimization
- Purpose limitation
- Consent management
- Anonymization/pseudonymization
- Privacy-preserving analytics

---

## Q100: How do you build a security culture in an organization?
**Answer:**

**Components:**

1. **Leadership**
   - Executive support
   - Security as business priority
   - Budget allocation

2. **Training**
   - Regular awareness training
   - Role-specific training (developers, admins)
   - Phishing simulations
   - New hire onboarding

3. **Processes**
   - Secure SDLC
   - Incident response
   - Code review requirements
   - Change management

4. **Metrics**
   - Security KPIs
   - Vulnerability trends
   - Training completion
   - Incident response times

5. **Recognition**
   - Security champions
   - Bug bounty recognition
   - Positive reinforcement

6. **Communication**
   - Security newsletter
   - Post-incident sharing
   - Best practices documentation

---

# 📚 Quick Reference - System Design Security Checklist

| Area | Key Controls |
|------|--------------|
| Authentication | MFA, strong passwords, account lockout |
| Authorization | RBAC/ABAC, least privilege |
| Input | Validation, parameterized queries |
| Output | Encoding, Content-Type |
| Transport | HTTPS/TLS 1.3, certificate validation |
| Storage | Encryption at rest, access control |
| Secrets | Vault, rotation, no hardcoding |
| Logging | Centralized, immutable, no sensitive data |
| Headers | CSP, HSTS, X-Frame-Options |
| API | Rate limiting, authentication, versioning |
| Dependencies | SCA scanning, updates |
| Infrastructure | Segmentation, hardening, patching |

---

**Good luck with your TCS HackQuest interview!** 🚀
