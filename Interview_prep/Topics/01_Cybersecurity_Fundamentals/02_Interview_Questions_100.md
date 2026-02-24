# 🔐 CYBERSECURITY FUNDAMENTALS - 100 Interview Q&A

## Priority Levels
- 🔴 **Most Probable (Q1-40)**: Frequently asked in interviews
- 🟡 **Complex (Q41-70)**: Technical depth required
- 🟢 **In-Depth/Scenario (Q71-100)**: Advanced scenarios & practical

---

# 🔴 MOST PROBABLE QUESTIONS (1-40)

## Q1: What is Cybersecurity?
**Answer:** Cybersecurity is the practice of protecting systems, networks, programs, and data from digital attacks, unauthorized access, damage, or theft. It encompasses technologies, processes, and practices designed to safeguard information assets and ensure confidentiality, integrity, and availability of data.

---

## Q2: Explain the CIA Triad.
**Answer:**
- **Confidentiality**: Ensuring data is accessible only to authorized users (encryption, access controls)
- **Integrity**: Ensuring data is accurate and unaltered (hashing, checksums, digital signatures)
- **Availability**: Ensuring systems and data are accessible when needed (redundancy, backups, DDoS protection)

This is the foundational model for information security.

---

## Q3: What is the difference between a threat, vulnerability, and risk?
**Answer:**
- **Threat**: A potential cause of harm (hacker, malware, natural disaster)
- **Vulnerability**: A weakness that can be exploited (unpatched software, weak password)
- **Risk**: The probability of a threat exploiting a vulnerability and the resulting impact

**Formula**: Risk = Threat × Vulnerability × Impact

---

## Q4: What is Authentication vs Authorization?
**Answer:**
- **Authentication**: Verifying identity - "Who are you?" (passwords, biometrics, MFA)
- **Authorization**: Determining permissions - "What can you access?" (ACLs, RBAC)

Authentication always comes before authorization.

---

## Q5: What is Multi-Factor Authentication (MFA)?
**Answer:** MFA requires two or more verification factors from different categories:
- **Something you know**: Password, PIN
- **Something you have**: Phone, token, smart card
- **Something you are**: Fingerprint, face recognition

Example: Password + OTP from phone app.

---

## Q6: What is encryption? Explain symmetric vs asymmetric.
**Answer:** Encryption transforms readable data (plaintext) into unreadable format (ciphertext).

- **Symmetric**: Same key for encryption/decryption (AES, DES). Fast, used for bulk data.
- **Asymmetric**: Public key encrypts, private key decrypts (RSA, ECC). Slower, used for key exchange and digital signatures.

---

## Q7: What is a firewall?
**Answer:** A firewall is a network security device that monitors and controls incoming/outgoing traffic based on security rules. Types include:
- **Packet filtering**: Examines packet headers
- **Stateful inspection**: Tracks connection state
- **Application layer**: Inspects application data
- **Next-gen (NGFW)**: Includes IPS, DPI, threat intelligence

---

## Q8: What is the difference between IDS and IPS?
**Answer:**
- **IDS (Intrusion Detection System)**: Monitors and alerts on suspicious activity. Passive - doesn't block.
- **IPS (Intrusion Prevention System)**: Monitors, detects, AND blocks threats. Active - inline deployment.

IPS is essentially IDS with blocking capability.

---

## Q9: What is a VPN?
**Answer:** Virtual Private Network creates an encrypted tunnel over public networks, providing:
- **Privacy**: Encrypts traffic
- **Anonymity**: Hides IP address
- **Security**: Protects data on untrusted networks

Types: Site-to-site, Remote access, SSL VPN.

---

## Q10: What is phishing?
**Answer:** Phishing is a social engineering attack where attackers impersonate legitimate entities to steal credentials/sensitive data via:
- **Email phishing**: Fake emails with malicious links
- **Spear phishing**: Targeted at specific individuals
- **Whaling**: Targeting executives
- **Smishing/Vishing**: SMS and voice phishing

---

## Q11: What is malware? Name the types.
**Answer:** Malicious software designed to damage or gain unauthorized access:
- **Virus**: Attaches to files, needs user action
- **Worm**: Self-replicating, spreads automatically
- **Trojan**: Disguised as legitimate software
- **Ransomware**: Encrypts files for ransom
- **Spyware**: Secretly monitors users
- **Rootkit**: Hides deep in system
- **Adware**: Displays unwanted ads

---

## Q12: What is a DDoS attack?
**Answer:** Distributed Denial of Service floods a target with traffic from multiple sources, making services unavailable.

**Types:**
- **Volumetric**: Bandwidth flooding (UDP flood)
- **Protocol**: Exploit protocol weaknesses (SYN flood)
- **Application layer**: Target specific services (HTTP flood)

**Mitigation**: CDN, rate limiting, DDoS protection services.

---

## Q13: What is SQL Injection?
**Answer:** SQL Injection occurs when user input is incorporated into SQL queries without proper sanitization, allowing attackers to:
- Extract data
- Modify/delete data
- Bypass authentication
- Execute admin operations

**Prevention**: Parameterized queries, input validation, least privilege.

---

## Q14: What is XSS (Cross-Site Scripting)?
**Answer:** XSS injects malicious scripts into web pages viewed by other users.

**Types:**
- **Stored XSS**: Script saved in database
- **Reflected XSS**: Script in URL, reflected back
- **DOM-based XSS**: Client-side script manipulation

**Prevention**: Output encoding, CSP headers, input validation.

---

## Q15: What is the principle of Least Privilege?
**Answer:** Users and systems should have only the minimum permissions necessary to perform their tasks. This:
- Limits damage from compromised accounts
- Reduces attack surface
- Improves auditability
- Prevents privilege escalation

---

## Q16: What is Defense in Depth?
**Answer:** Security strategy using multiple layers of controls:
1. **Physical**: Guards, locks, cameras
2. **Perimeter**: Firewalls, WAF
3. **Network**: Segmentation, IDS/IPS
4. **Host**: Antivirus, hardening
5. **Application**: Secure coding, input validation
6. **Data**: Encryption, DLP

If one layer fails, others provide protection.

---

## Q17: What is a Zero-Day vulnerability?
**Answer:** A software vulnerability unknown to the vendor with no available patch. Called "zero-day" because developers have had zero days to fix it.

**Characteristics:**
- No signature-based detection
- Highly valuable to attackers
- Requires behavior-based detection

---

## Q18: What is penetration testing?
**Answer:** Authorized simulated cyberattack to evaluate security. Phases:
1. **Reconnaissance**: Information gathering
2. **Scanning**: Identify vulnerabilities
3. **Exploitation**: Attempt to exploit
4. **Post-exploitation**: Assess impact
5. **Reporting**: Document findings

Types: Black box, White box, Gray box.

---

## Q19: What is the difference between Black Hat, White Hat, and Gray Hat hackers?
**Answer:**
- **White Hat**: Ethical hackers, authorized testing, improve security
- **Black Hat**: Malicious hackers, unauthorized access, criminal intent
- **Gray Hat**: Find vulnerabilities without permission but don't exploit maliciously

---

## Q20: What is Social Engineering?
**Answer:** Psychological manipulation to trick people into revealing information or performing actions:
- **Phishing**: Fake communications
- **Pretexting**: Fabricated scenarios
- **Baiting**: Offering something enticing
- **Tailgating**: Following authorized person
- **Quid pro quo**: Offering service for information

---

## Q21: What is hashing? Name common algorithms.
**Answer:** Hashing is a one-way function that converts data into a fixed-size string (hash). Used for:
- Password storage
- File integrity verification
- Digital signatures

**Algorithms:**
- MD5 (128-bit, deprecated)
- SHA-1 (160-bit, deprecated)
- SHA-256 (256-bit, secure)
- bcrypt (password hashing)

---

## Q22: What is the difference between encoding, encryption, and hashing?
**Answer:**
- **Encoding**: Data transformation for compatibility (Base64). Reversible, no key.
- **Encryption**: Data protection using key. Reversible with correct key.
- **Hashing**: One-way transformation. Irreversible, used for integrity.

---

## Q23: What is a Man-in-the-Middle (MITM) attack?
**Answer:** Attacker intercepts communication between two parties, potentially:
- Eavesdropping on data
- Modifying messages
- Injecting malicious content

**Prevention**: HTTPS, certificate pinning, avoiding public WiFi.

---

## Q24: What is HTTPS and how does it work?
**Answer:** HTTPS = HTTP + TLS/SSL encryption.

**Process:**
1. Client requests secure connection
2. Server sends certificate with public key
3. Client verifies certificate
4. Client/server negotiate session key
5. Encrypted communication begins

Protects: Confidentiality, integrity, authenticity.

---

## Q25: What is a digital certificate?
**Answer:** Electronic document binding a public key to an identity, issued by Certificate Authority (CA).

**Contains:**
- Subject name
- Public key
- Issuer name
- Validity period
- Digital signature of CA

Used in HTTPS, email signing, code signing.

---

## Q26: What is the OSI model? Name the layers.
**Answer:** Open Systems Interconnection - 7-layer network model:
1. **Physical**: Cables, signals
2. **Data Link**: MAC addresses, switches
3. **Network**: IP addressing, routing
4. **Transport**: TCP/UDP, ports
5. **Session**: Session management
6. **Presentation**: Encryption, compression
7. **Application**: HTTP, FTP, DNS

---

## Q27: What are common ports a security professional should know?
**Answer:**
| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3389 | RDP |
| 3306 | MySQL |

---

## Q28: What is a Security Operations Center (SOC)?
**Answer:** Centralized unit monitoring organization's security posture 24/7:
- Monitor alerts and logs
- Detect and respond to threats
- Investigate incidents
- Maintain security tools

**Roles**: SOC Analyst (L1, L2, L3), SOC Manager, Threat Hunter.

---

## Q29: What is SIEM?
**Answer:** Security Information and Event Management - platform that:
- Collects logs from multiple sources
- Correlates events
- Detects anomalies
- Generates alerts
- Supports compliance reporting

**Examples**: Splunk, IBM QRadar, Microsoft Sentinel, ELK Stack.

---

## Q30: What is vulnerability assessment vs penetration testing?
**Answer:**
- **Vulnerability Assessment**: Identifies and lists vulnerabilities without exploitation. Broader scope, automated.
- **Penetration Testing**: Actively exploits vulnerabilities to determine real impact. Deeper, manual.

VA finds weaknesses; Pentest proves exploitability.

---

## Q31: What is the difference between TCP and UDP?
**Answer:**
| TCP | UDP |
|-----|-----|
| Connection-oriented | Connectionless |
| Reliable delivery | No guarantee |
| Error checking | No error recovery |
| Ordered packets | May arrive out of order |
| Slower | Faster |
| HTTP, FTP, SSH | DNS, VoIP, streaming |

---

## Q32: What is ARP and ARP poisoning?
**Answer:** ARP (Address Resolution Protocol) maps IP addresses to MAC addresses.

**ARP Poisoning**: Attacker sends fake ARP responses, associating their MAC with legitimate IP, enabling:
- MITM attacks
- Session hijacking
- DoS

**Prevention**: Static ARP entries, DAI, encrypted protocols.

---

## Q33: What is DNS and DNS spoofing?
**Answer:** DNS translates domain names to IP addresses.

**DNS Spoofing**: Corrupts DNS cache to redirect users to malicious sites.

**Prevention**: DNSSEC, DNS monitoring, secure DNS servers.

---

## Q34: What is a honeypot?
**Answer:** Decoy system designed to lure attackers:
- **Purpose**: Study attack methods, detect intrusions, distract attackers
- **Types**: Low-interaction (simulated), High-interaction (real systems)

Not for production; purely for research/detection.

---

## Q35: What is the difference between a virus and a worm?
**Answer:**
| Virus | Worm |
|-------|------|
| Needs host file | Standalone program |
| Requires user action | Self-propagates |
| Attaches to programs | Exploits vulnerabilities |
| Spreads slower | Spreads rapidly |

---

## Q36: What is a botnet?
**Answer:** Network of compromised computers (bots/zombies) controlled by attacker (botmaster) via C&C server.

**Uses:**
- DDoS attacks
- Spam campaigns
- Cryptocurrency mining
- Credential theft

**Example**: Mirai botnet.

---

## Q37: What is the NIST Cybersecurity Framework?
**Answer:** Framework for managing cybersecurity risk with 5 functions:
1. **Identify**: Understand assets and risks
2. **Protect**: Implement safeguards
3. **Detect**: Identify cybersecurity events
4. **Respond**: Take action on incidents
5. **Recover**: Restore capabilities

---

## Q38: What is PII?
**Answer:** Personally Identifiable Information - data that can identify an individual:
- **Direct PII**: Name, SSN, email
- **Indirect PII**: Date of birth, ZIP code, gender (combined to identify)

Must be protected under GDPR, CCPA, HIPAA.

---

## Q39: What is data classification?
**Answer:** Categorizing data based on sensitivity:
- **Public**: No restrictions
- **Internal**: Business use only
- **Confidential**: Limited access
- **Restricted/Secret**: Highest protection

Determines protection requirements and handling procedures.

---

## Q40: What is incident response?
**Answer:** Structured approach to handling security incidents:
1. **Preparation**: Plans, tools, team
2. **Detection & Analysis**: Identify incident
3. **Containment**: Prevent spread
4. **Eradication**: Remove threat
5. **Recovery**: Restore systems
6. **Lessons Learned**: Improve processes

---

# 🟡 COMPLEX QUESTIONS (41-70)

## Q41: Explain the difference between stateful and stateless firewalls.
**Answer:**
- **Stateless**: Examines each packet independently based on rules (source/dest IP, port). No context of connection state. Faster but less secure.

- **Stateful**: Tracks active connections, makes decisions based on connection state and context. Understands if packet is part of established connection. More secure but more resource-intensive.

**Example**: Stateful firewall knows a response packet belongs to an outgoing request.

---

## Q42: What is PKI (Public Key Infrastructure)?
**Answer:** Framework for managing digital certificates and public keys:

**Components:**
- **CA (Certificate Authority)**: Issues certificates
- **RA (Registration Authority)**: Verifies requests
- **Certificate Repository**: Stores certificates
- **CRL (Certificate Revocation List)**: Lists revoked certificates

**Uses**: HTTPS, email encryption, code signing, VPN.

---

## Q43: Explain the TLS handshake process.
**Answer:**
1. **Client Hello**: Client sends supported ciphers, TLS version
2. **Server Hello**: Server selects cipher, sends certificate
3. **Certificate Verification**: Client validates server certificate
4. **Key Exchange**: Asymmetric exchange of pre-master secret
5. **Session Keys**: Both derive symmetric session keys
6. **Finished**: Encrypted communication begins

TLS 1.3 reduces this to one round-trip.

---

## Q44: What is the difference between SAST and DAST?
**Answer:**
| SAST | DAST |
|------|------|
| Static Application Security Testing | Dynamic Application Security Testing |
| Analyzes source code | Tests running application |
| White-box | Black-box |
| Early in SDLC | Later in SDLC |
| Finds code flaws | Finds runtime issues |
| Fast, many false positives | Slower, fewer false positives |

**Tools**: SAST (SonarQube), DAST (OWASP ZAP).

---

## Q45: Explain session hijacking and prevention methods.
**Answer:** Attacker takes over valid user session by stealing session token.

**Methods:**
- Session sniffing (unencrypted traffic)
- Session fixation (forcing known session ID)
- XSS (stealing cookies)
- MITM attacks

**Prevention:**
- Use HTTPS
- Regenerate session ID after login
- Set HttpOnly and Secure cookie flags
- Implement session timeout
- Bind session to IP/user-agent

---

## Q46: What is privilege escalation? Types and prevention.
**Answer:** Gaining higher privileges than authorized.

**Types:**
- **Vertical**: Lower to higher privilege (user → admin)
- **Horizontal**: Same level, different user (user A → user B)

**Methods**: Exploiting vulnerabilities, misconfigurations, weak permissions.

**Prevention**: Least privilege, patch management, proper access controls, monitoring.

---

## Q47: Explain buffer overflow attacks.
**Answer:** Input exceeds allocated buffer, overwriting adjacent memory:
- Can overwrite return addresses
- Execute arbitrary code
- Crash application

**Types**: Stack-based, Heap-based.

**Prevention:**
- Input validation
- ASLR (Address Space Layout Randomization)
- DEP (Data Execution Prevention)
- Stack canaries
- Secure coding practices

---

## Q48: What is the difference between WAF and traditional firewall?
**Answer:**
| Traditional Firewall | WAF |
|---------------------|-----|
| Network layer (3-4) | Application layer (7) |
| IP/port filtering | HTTP traffic inspection |
| Blocks by IP/protocol | Blocks SQL injection, XSS |
| Network protection | Web app protection |

WAF understands HTTP and can detect application-specific attacks.

---

## Q49: Explain OAuth 2.0 grant types.
**Answer:**
1. **Authorization Code**: Most secure, for server-side apps. Exchanges code for token.
2. **Implicit**: For SPAs (deprecated). Token returned directly.
3. **Client Credentials**: Machine-to-machine. No user involved.
4. **Resource Owner Password**: User gives credentials to app (legacy).
5. **Device Code**: For input-limited devices (smart TV).
6. **PKCE**: Enhanced authorization code for public clients.

---

## Q50: What is JWT? Explain structure and security concerns.
**Answer:** JSON Web Token - compact token format.

**Structure**: `header.payload.signature` (Base64-encoded)

**Security Concerns:**
- Payload is encoded, NOT encrypted (don't store sensitive data)
- Verify signature always
- Check expiration (exp claim)
- Algorithm confusion attacks (alg: none)
- Must use HTTPS
- Token can't be revoked until expiry

---

## Q51: Explain the Cyber Kill Chain.
**Answer:** Lockheed Martin's attack phases:
1. **Reconnaissance**: Research target
2. **Weaponization**: Create exploit
3. **Delivery**: Send to target (email, USB)
4. **Exploitation**: Execute vulnerability
5. **Installation**: Install malware
6. **Command & Control**: Establish communication
7. **Actions on Objectives**: Achieve goals (exfiltrate data)

**Defense**: Break any link to stop attack.

---

## Q52: What is the MITRE ATT&CK framework?
**Answer:** Knowledge base of adversary tactics and techniques based on real-world observations.

**Components:**
- **Tactics**: Why (objectives like Initial Access, Persistence)
- **Techniques**: How (methods like Phishing, Credential Dumping)
- **Procedures**: Specific implementations

**Uses**: Threat modeling, detection engineering, red teaming, gap analysis.

---

## Q53: Explain CSRF attack and prevention.
**Answer:** Cross-Site Request Forgery tricks user's browser into making unwanted requests to a site where they're authenticated.

**Example**: Hidden form on malicious site submits money transfer to bank where user is logged in.

**Prevention:**
- CSRF tokens (unique per session/request)
- SameSite cookie attribute
- Verify origin/referer headers
- Re-authentication for sensitive actions

---

## Q54: What is the difference between symmetric and asymmetric encryption use cases?
**Answer:**
**Symmetric (AES)**:
- Bulk data encryption
- File/disk encryption
- Database encryption
- VPN tunnels

**Asymmetric (RSA)**:
- Key exchange
- Digital signatures
- Certificate-based authentication
- Email encryption (initial exchange)

**Hybrid approach**: Use asymmetric to exchange symmetric key, then symmetric for data.

---

## Q55: Explain forward secrecy (Perfect Forward Secrecy).
**Answer:** Even if long-term private key is compromised, past session keys cannot be derived.

**How it works**: Each session uses unique ephemeral keys (Diffie-Hellman).

**Benefit**: Compromising server's private key doesn't decrypt historical traffic.

**Implementation**: ECDHE in TLS.

---

## Q56: What is a rainbow table and how to prevent rainbow table attacks?
**Answer:** Precomputed table of hash values for common passwords.

**Attack**: Compare stolen hashes against rainbow table for quick lookup.

**Prevention:**
- **Salting**: Add random value before hashing (unique per password)
- **Key stretching**: Use algorithms like bcrypt, scrypt, Argon2
- Strong password policies

---

## Q57: Explain network segmentation and micro-segmentation.
**Answer:**
**Network Segmentation**: Dividing network into separate zones (VLANs, subnets) with controlled traffic between them.

**Micro-segmentation**: Granular segmentation at workload level, often in cloud/virtualized environments. Each application/service isolated.

**Benefits**: Limits lateral movement, contains breaches, better monitoring.

---

## Q58: What is the difference between EDR, XDR, and MDR?
**Answer:**
- **EDR (Endpoint Detection & Response)**: Monitors endpoints, detects threats, enables response.

- **XDR (Extended Detection & Response)**: Integrates multiple security products (endpoint, network, cloud) for unified detection.

- **MDR (Managed Detection & Response)**: Third-party service providing monitoring and response capabilities.

---

## Q59: Explain container security challenges.
**Answer:**
**Challenges:**
- Image vulnerabilities (outdated base images)
- Secrets management in containers
- Container escape attacks
- Network security between containers
- Runtime security
- Orchestration security (Kubernetes RBAC)

**Mitigations:**
- Scan images
- Use minimal base images
- Don't run as root
- Network policies
- Runtime protection

---

## Q60: What is threat modeling? Name methodologies.
**Answer:** Systematic process to identify threats and mitigations early in design.

**Methodologies:**
- **STRIDE**: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- **PASTA**: Process for Attack Simulation and Threat Analysis
- **DREAD**: Damage, Reproducibility, Exploitability, Affected users, Discoverability

**Process**: Define scope → Identify assets → Identify threats → Prioritize → Mitigate.

---

## Q61: Explain the difference between vulnerability and exploit.
**Answer:**
- **Vulnerability**: Weakness in system that could be exploited (CVE-listed)
- **Exploit**: Code/technique that takes advantage of vulnerability

**Relationship**: Vulnerability exists first; exploit is developed to abuse it.

**Example**: CVE-2021-44228 (Log4Shell) is vulnerability; actual payload is exploit.

---

## Q62: What is SSRF (Server-Side Request Forgery)?
**Answer:** Attacker tricks server into making requests to unintended locations.

**Impact:**
- Access internal services
- Port scanning internal network
- Read cloud metadata (169.254.169.254)
- Bypass firewalls

**Prevention:**
- Validate/whitelist URLs
- Block private IP ranges
- Use allowlists for destinations
- Disable unnecessary URL schemes

---

## Q63: Explain race conditions in security context.
**Answer:** Timing vulnerability where outcome depends on sequence/timing of events.

**TOCTOU (Time of Check to Time of Use)**: Security check valid at check time but not at use time.

**Example**: Check if user has permission, but permission revoked before action executes.

**Prevention**: Atomic operations, proper locking, re-validation.

---

## Q64: What is memory forensics?
**Answer:** Analysis of volatile memory (RAM) dumps for:
- Running processes
- Network connections
- Encryption keys
- Malware artifacts
- User activity

**Tools**: Volatility, Rekall

**Acquisition**: Must capture before power off (RAM contents lost).

---

## Q65: Explain the concept of Security Orchestration, Automation, and Response (SOAR).
**Answer:** Platform that:
- **Orchestrates**: Connects security tools
- **Automates**: Runs playbooks without human intervention
- **Responds**: Takes action on threats

**Benefits:**
- Faster response
- Consistent handling
- Reduced analyst fatigue
- Scalability

**Examples**: Splunk SOAR, Palo Alto XSOAR, IBM Resilient.

---

## Q66: What is fuzzing in security testing?
**Answer:** Automated technique sending random/malformed data to find vulnerabilities.

**Types:**
- **Dumb fuzzing**: Random mutations
- **Smart fuzzing**: Understanding of protocol/format
- **Coverage-guided**: Uses code coverage feedback

**Finds**: Buffer overflows, crashes, memory corruptions.

**Tools**: AFL, LibFuzzer, Radamsa.

---

## Q67: Explain certificate pinning and its limitations.
**Answer:** Application only accepts specific certificate(s), preventing MITM even with valid CA-issued certificates.

**Implementation**: Embed cert/hash in app, compare during handshake.

**Limitations:**
- Certificate rotation difficult
- Difficult to update pinned certs
- Can break debugging/monitoring
- If compromised, requires app update

---

## Q68: What is the difference between blue team, red team, and purple team?
**Answer:**
- **Blue Team**: Defenders - monitor, detect, respond to threats
- **Red Team**: Attackers - simulate real attacks to test defenses
- **Purple Team**: Collaboration between red and blue to improve detection and response

Purple team exercises maximize learning from red team activities.

---

## Q69: Explain security headers and their purpose.
**Answer:**
| Header | Purpose |
|--------|---------|
| **HSTS** | Force HTTPS |
| **X-Frame-Options** | Prevent clickjacking |
| **X-Content-Type-Options** | Prevent MIME sniffing |
| **X-XSS-Protection** | XSS filtering (legacy) |
| **CSP** | Control resource loading |
| **Referrer-Policy** | Control referer header |
| **Permissions-Policy** | Control browser features |

---

## Q70: What is the principle of separation of duties?
**Answer:** No single person should control all aspects of a critical function.

**Examples:**
- Developer can't deploy to production alone
- Admin can't also approve their own access
- Separate roles for creating and approving transactions

**Benefits**: Prevents fraud, reduces errors, ensures accountability.

---

# 🟢 IN-DEPTH / SCENARIO QUESTIONS (71-100)

## Q71: SCENARIO - Your company detected a ransomware infection on 5 workstations. Walk through your response.
**Answer:**
1. **Containment**: Immediately isolate infected machines from network (disable NIC, disconnect cables)
2. **Identify scope**: Check for lateral movement, scan other systems
3. **Preserve evidence**: Don't reboot - capture memory dumps
4. **Notify stakeholders**: Management, legal, potentially law enforcement
5. **Identify ransomware variant**: Check ransom note, file extensions
6. **Check for decryptors**: NoMoreRansom project
7. **Restore from backups**: After ensuring backups aren't infected
8. **Eradicate**: Identify entry point, patch vulnerability
9. **Recover**: Restore systems, monitor closely
10. **Post-incident**: Document lessons, update controls

---

## Q72: SCENARIO - A critical vulnerability (CVSS 10.0) is announced affecting your production web server. What do you do?
**Answer:**
1. **Assessment**: Confirm vulnerable version in use, check exploit availability
2. **Risk analysis**: Is it actively exploited? Is our server internet-facing?
3. **Interim mitigation**: WAF rules, network restrictions if patch not ready
4. **Emergency patching**: Follow change management but expedited
5. **Testing**: Test patch in staging if time permits
6. **Deployment**: Apply patch with rollback plan
7. **Verification**: Confirm vulnerability resolved
8. **Monitoring**: Watch for exploitation attempts
9. **Communication**: Update stakeholders
10. **Documentation**: Record timeline and actions

---

## Q73: How would you investigate a suspected data breach?
**Answer:**
1. **Preserve evidence**: Forensic copies of affected systems
2. **Identify compromise timeline**: When did unauthorized access start?
3. **Determine scope**: What data was accessed? How much?
4. **Identify attack vector**: How did attacker get in?
5. **Review logs**: Network flow, authentication logs, application logs
6. **Memory analysis**: Check for IOCs if systems still running
7. **Interview personnel**: Did anyone notice anomalies?
8. **Document everything**: Chain of custody maintained
9. **Assess regulatory impact**: PII involved? Notification required?
10. **Prepare report**: For legal, management, potentially authorities

---

## Q74: Design a secure authentication system for a banking application.
**Answer:**
**Requirements:**
- MFA mandatory (2+ factors)
- Strong password policy (12+ chars, complexity)
- Account lockout after failed attempts
- Device fingerprinting
- Session management with short timeouts
- Secure password storage (Argon2)
- Encrypted transmission (TLS 1.3)
- Out-of-band verification for sensitive operations
- Risk-based authentication (unusual location/device)
- Comprehensive audit logging
- Rate limiting on authentication endpoints
- Passwordless options (FIDO2)

---

## Q75: SCENARIO - You discover an employee is exfiltrating data to personal cloud storage. How do you handle this?
**Answer:**
1. **Document evidence**: Take screenshots, preserve logs
2. **Don't alert the employee**: Continue monitoring
3. **Involve HR and Legal**: Follow company policy
4. **Assess data sensitivity**: What was taken?
5. **Forensic investigation**: Determine full scope
6. **DLP review**: Why wasn't this blocked?
7. **Coordinate response**: When to confront, involve authorities?
8. **Disable access**: At appropriate time
9. **Interview employee**: With HR/Legal present
10. **Remediation**: Revoke access, assess damage, improve controls

---

## Q76: Explain how you would implement security in a microservices architecture.
**Answer:**
**Service-to-service:**
- Mutual TLS (mTLS) for all communication
- Service mesh (Istio) for policy enforcement
- API gateway for external access

**Authentication/Authorization:**
- OAuth 2.0 with short-lived JWTs
- Centralized identity provider
- RBAC per service

**Network:**
- Network policies limiting inter-service communication
- Micro-segmentation
- East-west traffic monitoring

**Runtime:**
- Container security (non-root, minimal images)
- Secrets management (Vault)
- Security scanning in CI/CD

**Observability:**
- Distributed tracing
- Centralized logging
- Security monitoring per service

---

## Q77: A third-party vendor requests API access to your system. What security considerations?
**Answer:**
1. **Due diligence**: Vendor security assessment
2. **Least privilege**: Only necessary endpoints/data
3. **Dedicated API credentials**: Not shared accounts
4. **Rate limiting**: Prevent abuse
5. **IP whitelisting**: If possible
6. **Separate environment**: Not production if feasible
7. **Monitoring**: Log all vendor access
8. **Data minimization**: Return only required fields
9. **Contractual**: Security requirements in agreement
10. **Expiration**: Access time-limited, regular review
11. **Encryption**: TLS required, sensitive data encrypted
12. **Revocation plan**: How to quickly cut access if needed

---

## Q78: SCENARIO - Your web application is under SQL injection attack. Explain immediate and long-term actions.
**Answer:**
**Immediate:**
1. Identify affected endpoints from WAF/logs
2. Block attacking IPs (if identifiable)
3. Enable emergency WAF rules for SQLi patterns
4. Take application offline if severe
5. Assess if data was extracted
6. Preserve logs for investigation

**Long-term:**
1. Patch vulnerable code (parameterized queries)
2. Input validation refactoring
3. Code review for similar vulnerabilities
4. Security testing (SAST/DAST)
5. Developer security training
6. Database monitoring for anomalous queries
7. Least privilege on DB accounts
8. WAF rule tuning

---

## Q79: Design a security monitoring strategy for a cloud-native application.
**Answer:**
**Data Sources:**
- Cloud provider logs (CloudTrail, VPC Flow)
- Application logs
- Container/Kubernetes logs
- API gateway logs
- WAF logs
- Network flow data

**Collection:**
- Centralized logging (ELK/Splunk)
- Log integrity protection
- Appropriate retention

**Detection:**
- SIEM correlation rules
- Behavioral analytics
- ML for anomaly detection
- Threat intelligence integration

**Response:**
- SOAR integration
- Automated playbooks
- Alert prioritization
- On-call rotation

**Metrics:**
- MTTD (Mean Time to Detect)
- MTTR (Mean Time to Respond)
- False positive ratio

---

## Q80: How would you secure a DevOps/CI/CD pipeline?
**Answer:**
**Code:**
- Pre-commit hooks (secrets scanning)
- SAST in pull requests
- Dependency scanning (SCA)

**Build:**
- Hardened build agents
- Ephemeral build environments
- Signed artifacts

**Test:**
- DAST in staging
- Security unit tests
- Infrastructure as Code scanning

**Deploy:**
- Secrets management (Vault)
- Container image scanning
- Immutable infrastructure
- GitOps with signed commits

**Runtime:**
- Runtime protection
- Monitoring and alerting
- Automated rollback capability

**Access:**
- Least privilege for pipelines
- MFA for CI/CD platforms
- Audit logging

---

## Q81: SCENARIO - Executive clicks phishing link, enters credentials. What's your response?
**Answer:**
1. **Immediately reset credentials**: All accounts for that user
2. **Revoke active sessions**: Force re-authentication everywhere
3. **Enable enhanced monitoring**: Watch for suspicious login attempts
4. **Check for unauthorized access**: Review login history
5. **Scan the endpoint**: For malware if link was malicious
6. **Check email rules**: Attackers often create forwarding rules
7. **Review recent sent emails**: Check for BEC attempts
8. **Notify security team**: Escalate appropriately
9. **Additional MFA**: Ensure MFA active on all accounts
10. **Targeted training**: Executive security awareness
11. **Report phishing**: To email provider, block sender
12. **Document incident**: For records and improvement

---

## Q82: How do you balance security with user experience?
**Answer:**
**Strategies:**
- **Risk-based authentication**: Only require step-up for risky actions
- **SSO**: One login for multiple applications
- **Passwordless**: FIDO2/biometrics are both secure and convenient
- **Progressive security**: Adjust friction based on sensitivity
- **Smart MFA**: Push notifications vs. typing codes
- **Security that enables**: Position security as enabler, not blocker
- **User education**: Explain why measures exist
- **Feedback loops**: Gather user input on security friction
- **Automation**: Reduce manual security steps

**Philosophy**: Security that people bypass is no security at all.

---

## Q83: Explain your approach to vulnerability management.
**Answer:**
**Process:**
1. **Discovery**: Continuous asset inventory
2. **Scanning**: Regular automated scans (authenticated)
3. **Prioritization**: Risk-based (CVSS + context)
4. **Remediation SLAs**: Based on severity and exposure
5. **Tracking**: Dashboard with metrics
6. **Verification**: Confirm fixes worked
7. **Exceptions**: Documented, time-limited, compensating controls

**Prioritization factors:**
- CVSS score
- Asset criticality
- Exposure (internet-facing?)
- Exploit availability
- Business context

**Metrics:**
- Number of vulnerabilities by severity
- Mean time to remediate
- Vulnerability aging
- Coverage percentage

---

## Q84: SCENARIO - Your company is acquiring another company. What security considerations for IT integration?
**Answer:**
**Pre-acquisition:**
- Security due diligence
- Review their security posture, incidents, compliance
- Assess technical debt

**During integration:**
1. **Network isolation**: Keep networks separate initially
2. **Identity**: Don't immediately merge directories
3. **Access control**: Least privilege, role-based
4. **Asset inventory**: Discover acquired assets
5. **Vulnerability assessment**: Scan acquired systems
6. **Security baseline**: Apply corporate standards
7. **Compliance gap analysis**: GDPR, PCI-DSS
8. **Data classification**: Understand data flows

**Post-integration:**
- Gradual trust extension
- Unified security monitoring
- Cultural alignment on security

---

## Q85: How would you implement Zero Trust architecture in an enterprise?
**Answer:**
**Phases:**

**Phase 1 - Foundation:**
- Identity provider consolidation
- MFA everywhere
- Device management/EDR
- Network visibility

**Phase 2 - Network:**
- Micro-segmentation
- Software-defined perimeter
- Remove implicit trust zones
- East-west traffic inspection

**Phase 3 - Application:**
- Application-level access (not network-level)
- Context-aware policies
- API security
- User and entity behavior analytics

**Phase 4 - Data:**
- Data classification
- Data loss prevention
- Encryption everywhere
- Rights management

**Continuous:**
- Continuous verification
- Adaptive policies
- Automation

---

## Q86: Explain how you would handle key management in an enterprise.
**Answer:**
**Infrastructure:**
- Hardware Security Modules (HSMs) for key storage
- Centralized KMS (AWS KMS, Azure Key Vault, HashiCorp Vault)

**Policies:**
- Key lifecycle management (creation, rotation, revocation, destruction)
- Separation of duties (key custodians)
- Access controls on keys
- Audit logging of key usage

**Practices:**
- Never store keys with encrypted data
- Different keys for different purposes
- Regular rotation (automated)
- Key escrow for critical keys
- Incident response for key compromise

**Compliance:**
- Meet regulatory requirements (PCI-DSS for payment keys)
- Document key management procedures

---

## Q87: SCENARIO - Your company must achieve SOC 2 compliance. Outline your approach.
**Answer:**
**Phase 1 - Preparation:**
1. Determine scope and Trust Services Criteria
2. Gap analysis against SOC 2 requirements
3. Prioritize remediation efforts
4. Assign control owners

**Phase 2 - Implementation:**
5. Implement/enhance controls
6. Document policies and procedures
7. Train staff on compliance requirements
8. Establish evidence collection processes

**Phase 3 - Testing:**
9. Internal audit/readiness assessment
10. Address findings
11. Collect evidence for audit period

**Phase 4 - Audit:**
12. Engage auditor
13. Support audit process
14. Address any issues identified

**Ongoing:**
15. Continuous monitoring
16. Annual renewal
17. Regular internal audits

---

## Q88: How would you design security for a mobile banking application?
**Answer:**
**Authentication:**
- Biometric + PIN fallback
- Device binding
- Risk-based step-up
- Session timeout

**Data Protection:**
- No sensitive data in local storage
- Certificate pinning
- Secure enclave for crypto operations
- Memory protection

**Communication:**
- TLS 1.3 minimum
- Mutual authentication
- API security

**App Security:**
- Obfuscation
- Tamper detection
- Root/jailbreak detection
- No debug in production

**Backend:**
- Transaction signing
- Fraud detection
- Velocity checks
- Out-of-band confirmation for high-risk actions

---

## Q89: SCENARIO - Log4Shell (CVE-2021-44228) is announced. Walk through your response at scale.
**Answer:**
**Hour 0-4:**
1. Activate incident response team
2. Inventory Java applications (including third-party)
3. Identify internet-facing vulnerable systems
4. Deploy WAF rules to block JNDI lookups
5. Communicate severity to leadership

**Hour 4-24:**
6. Prioritize patching (internet-facing first)
7. Restrict outbound LDAP/RMI if possible
8. Monitor for exploitation attempts
9. Patch accessible systems
10. Coordinate with vendors for third-party apps

**Day 2-7:**
11. Deep sweep for embedded Log4j
12. Patch remaining systems
13. Validate patches applied correctly
14. Review logs for prior compromise
15. Forensics if exploitation detected

**Post-incident:**
16. Lessons learned
17. Improve software inventory
18. Enhance dependency management

---

## Q90: Explain cryptographic agility and why it matters.
**Answer:**
**Cryptographic Agility**: Ability to readily switch to alternative cryptographic algorithms without major system changes.

**Why it matters:**
- Algorithms become weak over time (MD5, SHA-1, DES)
- Quantum computing will break RSA/ECC
- Regulatory changes may mandate specific algorithms
- New vulnerabilities discovered

**Implementation:**
- Abstract cryptographic operations
- Configurable algorithm selection
- Support algorithm negotiation
- Hybrid approaches during transitions
- Inventory cryptographic usage

**Example**: Preparing for post-quantum cryptography by implementing hybrid key exchange now.

---

## Q91: SCENARIO - Your CEO receives wire transfer request from "CFO" - suspected BEC. What do you do?
**Answer:**
1. **STOP the transaction**: Do not process immediately
2. **Verify out-of-band**: Call CFO on known number
3. **Check email headers**: Look for spoofing indicators
4. **Review recent activity**: Has CFO account been compromised?
5. **If compromised**: Trigger incident response
6. **If spoofed**: Report to email provider, block sender
7. **Alert finance team**: Verify other recent transactions
8. **Awareness**: Remind executives of this threat
9. **Implement controls**: Dual authorization for wire transfers
10. **Document**: Record for future reference

**Prevention:** Verification procedures for large transfers, email security, executive training.

---

## Q92: How do you approach security architecture review?
**Answer:**
**Process:**
1. **Understand context**: Business purpose, data handled, users
2. **Review documentation**: Architecture diagrams, data flows
3. **Apply threat modeling**: STRIDE or similar
4. **Assess against standards**: OWASP, CIS, industry-specific
5. **Review controls**: Authentication, authorization, encryption
6. **Check integrations**: Third-party security
7. **Evaluate resilience**: Availability, disaster recovery
8. **Consider compliance**: Regulatory requirements
9. **Prioritize findings**: Risk-based
10. **Provide recommendations**: Actionable, phased

**Artifacts:**
- Security requirements document
- Threat model
- Findings and recommendations
- Risk register

---

## Q93: SCENARIO - Your company decides to move to cloud. What's your security strategy?
**Answer:**
**Assessment:**
- Understand shared responsibility model
- Evaluate cloud provider security
- Assess data classification

**Architecture:**
- Design for cloud-native security
- Implement proper IAM
- Network segmentation (VPCs)
- Encryption in transit and at rest

**Migration:**
- Security review for each workload
- Lift-and-shift vs. rearchitect decision
- Avoid lifting legacy vulnerabilities

**Operations:**
- Cloud-native security tools
- CSPM (Cloud Security Posture Management)
- CWPP (Cloud Workload Protection)
- Automated compliance checking

**Governance:**
- Cloud security policies
- Guardrails via policy-as-code
- Cost monitoring (security cost too)
- Training for teams

---

## Q94: Explain supply chain security concerns and mitigations.
**Answer:**
**Threats:**
- Compromised third-party software (SolarWinds)
- Malicious dependencies (npm, PyPI)
- Hardware implants
- Vendor compromise

**Mitigations:**
**Software:**
- Dependency scanning
- Pin versions, verify hashes
- Software Bill of Materials (SBOM)
- Vendor security assessments

**Vendors:**
- Due diligence
- Contractual security requirements
- Regular audits
- Least privilege access

**Code:**
- Signed commits
- Code review
- Protected branches
- Build reproducibility

**Monitoring:**
- Detect anomalies in updates
- Threat intelligence on supply chain attacks

---

## Q95: SCENARIO - Penetration test reveals critical vulnerability in production system. It can't be patched immediately. What do you do?
**Answer:**
**Immediate mitigations:**
1. **Network controls**: Restrict access to affected system
2. **WAF rules**: Block known exploit patterns
3. **Enhanced monitoring**: Alert on exploitation attempts
4. **Disable vulnerable feature**: If possible
5. **Reduce attack surface**: Remove unnecessary services

**Process:**
6. Document compensating controls
7. Risk acceptance if needed (time-limited, management sign-off)
8. Track patch timeline
9. Communicate to stakeholders
10. Plan maintenance window

**Follow-up:**
11. Apply patch as soon as possible
12. Verify remediation
13. Review why patching took time
14. Improve patch management process

---

## Q96: How do you measure security program effectiveness?
**Answer:**
**Metrics categories:**

**Vulnerability Management:**
- Mean time to remediate by severity
- Percentage of systems scanned
- Vulnerability density trends

**Detection:**
- Mean time to detect (MTTD)
- Alert-to-incident ratio
- False positive rate

**Response:**
- Mean time to respond (MTTR)
- Incidents by type
- Containment time

**Compliance:**
- Control effectiveness
- Audit findings over time
- Policy exceptions

**Risk:**
- Risk score trends
- Issues closed vs. opened
- Time to address findings

**Training:**
- Phishing simulation click rates
- Security awareness scores

**Presentation**: Dashboard for executives, detailed for teams.

---

## Q97: SCENARIO - You're designing security for an IoT deployment (10,000 devices). What considerations?
**Answer:**
**Device Security:**
- Secure boot
- Hardware root of trust
- Secure firmware updates
- Minimal attack surface
- No default credentials

**Communication:**
- TLS/DTLS for all traffic
- Certificate-based auth
- API security
- Network segmentation

**Management:**
- Centralized device management
- Automated provisioning
- Remote wipe capability
- Inventory and monitoring

**Challenges:**
- Resource constraints (crypto)
- Physical access
- Long lifecycles
- Diverse vendors

**Network:**
- Dedicated IoT network
- Firewall rules per device type
- Anomaly detection

---

## Q98: Explain your approach to security awareness training.
**Answer:**
**Strategy:**
- **Risk-based**: Focus on biggest threats (phishing, social engineering)
- **Role-based**: Different content for developers, executives, general staff
- **Continuous**: Not just annual training
- **Engaging**: Videos, games, simulations

**Components:**
1. Onboarding training
2. Regular phishing simulations
3. Targeted training based on simulation results
4. Security champions program
5. Just-in-time training (when accessing sensitive systems)
6. Executive briefings

**Measurement:**
- Phishing click rates over time
- Reporting of suspicious emails
- Quiz scores
- Incident trends

**Culture:**
- Make it positive, not punitive
- Celebrate good behaviors
- Easy reporting mechanisms

---

## Q99: SCENARIO - A critical production service experiences a DDoS attack. Walk through your response.
**Answer:**
**Immediate (minutes):**
1. Validate it's DDoS (not system failure)
2. Enable DDoS protection if not active
3. Engage CDN/cloud provider's DDoS team
4. Activate rate limiting

**Short-term (hours):**
5. Analyze attack patterns
6. Implement specific filters (IP ranges, geographic)
7. Scale resources if volumetric
8. Enable challenge mechanisms (CAPTCHA)
9. Communicate with stakeholders

**If overwhelmed:**
10. Consider null-routing affected IPs
11. Work with ISP for upstream filtering
12. Failover to clean IP space
13. Consider taking service offline temporarily

**Recovery:**
14. Monitor for attack resumption
15. Analyze logs for attribution/IOCs
16. Update DDoS playbook
17. Consider dedicated DDoS protection service

---

## Q100: What do you see as the biggest cybersecurity challenges in the next 5 years?
**Answer:**
**Emerging threats:**
- **Quantum computing**: Breaking current encryption
- **AI-powered attacks**: Sophisticated, adaptive threats
- **Supply chain attacks**: Increasing complexity

**Technology challenges:**
- **Cloud security at scale**: Misconfigurations remain common
- **IoT proliferation**: Massive attack surface
- **API security**: APIs everywhere, often insecure

**Talent/Process:**
- **Skills shortage**: Not enough trained professionals
- **Alert fatigue**: Too many tools, too many alerts
- **Security debt**: Legacy systems with accumulated vulnerabilities

**Regulatory:**
- **Privacy regulations**: Global compliance complexity
- **Cybersecurity regulations**: Increasing mandates

**Preparation:**
- Cryptographic agility for post-quantum
- AI for defense, not just offense
- Security automation
- Continuous training and adaptation

---

# 📊 QUICK REVISION CARD

```
TOP 10 MOST FREQUENTLY ASKED:
1. CIA Triad
2. Threat vs Vulnerability vs Risk
3. Authentication vs Authorization
4. IDS vs IPS
5. Symmetric vs Asymmetric encryption
6. SQL Injection/XSS
7. Incident Response phases
8. OWASP Top 10
9. Zero Trust
10. Defense in Depth

REMEMBER:
• CIA = Confidentiality, Integrity, Availability
• Risk = Threat × Vulnerability × Impact
• AuthN first, then AuthZ
• NIST Framework: Identify, Protect, Detect, Respond, Recover
• Kill Chain: Recon → Weaponize → Deliver → Exploit → Install → C2 → Actions
```

---

**Good luck with your interview!** 🚀
