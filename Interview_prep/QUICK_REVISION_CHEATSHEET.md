# 🚀 TCS HACKQUEST - QUICK REVISION CHEATSHEET
## Last Day Review - February 25, 2026 (Interview: Feb 26, 9 AM)

---

# 📌 CIA TRIAD (Foundation of Everything)
```
CONFIDENTIALITY → Only authorized access    → Encryption, Access Control
INTEGRITY       → Data is accurate/unchanged → Hashing, Digital Signatures  
AVAILABILITY    → Systems accessible         → Backups, Redundancy, DDoS protection
```

---

# 📌 OWASP TOP 10 (2021) - MEMORIZE!
| # | Vulnerability | One-liner | Your Project |
|---|--------------|-----------|--------------|
| A01 | Broken Access Control | Accessing unauthorized resources | ✅ Scanner checks |
| A02 | Cryptographic Failures | Weak/no encryption | ✅ StegoCrypt AES-256 |
| A03 | Injection | SQLi, XSS, Command injection | ✅ 25+ SQLi, 20+ XSS payloads |
| A04 | Insecure Design | Security not built-in | - |
| A05 | Security Misconfiguration | Default creds, verbose errors | ✅ Header validation |
| A06 | Vulnerable Components | Outdated libraries | - |
| A07 | Auth Failures | Weak passwords, broken sessions | ✅ SmartBank JWT/bcrypt |
| A08 | Integrity Failures | Unsigned updates | - |
| A09 | Logging Failures | No monitoring | - |
| A10 | SSRF | Server making requests to attacker URLs | - |

---

# 📌 YOUR PROJECTS - KEY POINTS

## Web Vulnerability Scanner
```
✓ SQLi: 25+ payloads (error-based, union, blind)
✓ XSS: 20+ payloads (reflected detection)
✓ Port Scanning: Async (asyncio), 43 ports
✓ Security Headers: 10+ headers checked
✓ Directory Bruteforce: 88+ paths
✓ Regex-based detection for SQL errors
```

## StegoCrypt
```
✓ LSB Encoding: Hide data in least significant bits
✓ AES-256: Symmetric encryption (PBKDF2 key derivation)
✓ Why both? Defense in depth (hiding + encryption)
✓ Capacity: 1920x1080 image ≈ 760KB hidden data
```

## SmartBank
```
✓ JWT: Header.Payload.Signature (HS256)
✓ bcrypt: Cost factor 12, built-in salt, slow by design
✓ RBAC: Customer vs Developer modes
✓ Why bcrypt > MD5? Slow, salted, GPU-resistant
```

---

# 📌 ATTACK TYPES - ONE LINERS

| Attack | What it is |
|--------|------------|
| **SQL Injection** | Malicious SQL in user input |
| **XSS** | Inject JavaScript into web pages |
| **CSRF** | Trick user into unwanted actions |
| **SSRF** | Server makes requests to attacker URL |
| **MITM** | Intercept communication between parties |
| **Phishing** | Fake emails/sites to steal credentials |
| **Ransomware** | Encrypt files, demand payment |
| **DDoS** | Overwhelm server with traffic |
| **Brute Force** | Try all password combinations |
| **Zero-Day** | Exploit unknown to vendor |

---

# 📌 ENCRYPTION QUICK REFERENCE

| Type | Examples | Key Points |
|------|----------|------------|
| **Symmetric** | AES, DES, 3DES | Same key encrypt/decrypt, fast |
| **Asymmetric** | RSA, ECC | Public/private keys, slow |
| **Hashing** | SHA-256, MD5, bcrypt | One-way, fixed output |

```
AES-256: 2^256 combinations, quantum-safe
bcrypt: Slow (intentional), salted, adjustable cost
MD5: BROKEN - don't use for passwords
SHA-256: Good for integrity, not passwords (too fast)
```

---

# 📌 NETWORK ESSENTIALS

## OSI Model (Remember: "Please Do Not Throw Sausage Pizza Away")
```
7. Application  - HTTP, FTP, SSH
6. Presentation - SSL/TLS, encryption
5. Session      - Session management
4. Transport    - TCP/UDP, ports
3. Network      - IP, routing, ICMP
2. Data Link    - MAC, switches
1. Physical     - Cables, signals
```

## Key Ports
```
22 = SSH       | 443 = HTTPS   | 3306 = MySQL
80 = HTTP      | 3389 = RDP    | 27017 = MongoDB
21 = FTP       | 25 = SMTP     | 6379 = Redis
23 = Telnet    | 53 = DNS      | 445 = SMB
```

## TCP vs UDP
```
TCP: Connection-oriented, reliable, ordered (HTTP, SSH)
UDP: Connectionless, fast, no guarantee (DNS, streaming)
```

---

# 📌 LINUX COMMANDS - MUST KNOW

```bash
# Who's logged in?
w; who; last

# What's listening?
ss -tulpn; netstat -tulpn

# Processes?
ps aux; top

# Find SUID files (privesc check)
find / -perm -4000 -type f 2>/dev/null

# Failed SSH logins?
grep "Failed password" /var/log/auth.log

# Recently modified files?
find / -mtime -1 -type f 2>/dev/null

# Block IP with iptables?
sudo iptables -A INPUT -s 1.2.3.4 -j DROP
```

---

# 📌 INCIDENT RESPONSE PHASES
```
1. PREPARATION    → Plans, tools, team ready
2. DETECTION      → Identify the incident
3. CONTAINMENT    → Stop the spread
4. ERADICATION    → Remove the threat
5. RECOVERY       → Restore systems
6. LESSONS LEARNED → Document, improve
```

---

# 📌 SECURITY CONCEPTS

| Concept | Meaning |
|---------|---------|
| **Zero Trust** | Never trust, always verify |
| **Defense in Depth** | Multiple security layers |
| **Least Privilege** | Minimum permissions needed |
| **SIEM** | Security Info & Event Management |
| **SOC** | Security Operations Center |
| **IDS** | Detects intrusions (alerts) |
| **IPS** | Prevents intrusions (blocks) |
| **WAF** | Web Application Firewall |
| **EDR** | Endpoint Detection & Response |
| **XDR** | Extended Detection & Response |

---

# 📌 RECENT BREACHES (2024-2025)

| Breach | Attack | Lesson |
|--------|--------|--------|
| **MOVEit** | SQL injection zero-day | Patch fast, WAF |
| **Change Healthcare** | Ransomware, no MFA | MFA everywhere! |
| **Snowflake** | Stolen credentials | MFA mandatory |
| **Microsoft** | Password spray, no MFA | Even test accounts need MFA |
| **Okta** | Session token theft | Sanitize HAR files |

---

# 📌 AI IN SECURITY

**Defense:** Anomaly detection, UEBA, malware classification, SOAR
**Offense:** AI phishing, deepfakes, adversarial ML
**Risk:** Prompt injection, data leakage, shadow AI

---

# 📌 HR QUICK ANSWERS

**Why cybersecurity?**
> Passion for protecting systems, built vulnerability scanner and steganography tools

**Why TCS HackQuest?**
> Specialized security role, enterprise-level challenges, Prime package values security skills

**Weakness?**
> Sometimes dive too deep into technical details - now I start with user requirements first

**5-year goal?**
> Senior Security Analyst/Architect, OSCP certification, lead security assessments

---

# 📌 INTERVIEW DAY CHECKLIST

## Night Before:
- [ ] Review this cheatsheet
- [ ] Review resume-based Q&A file
- [ ] Sleep early (7+ hours)

## Morning Of (Feb 26):
- [ ] Wake up 7:30 AM
- [ ] Good breakfast
- [ ] Test internet/audio/video by 8:45 AM
- [ ] Keep water, resume copy nearby
- [ ] Deep breaths - you're prepared!

## During:
- [ ] Smile, greet confidently
- [ ] Take moment before answering
- [ ] Connect answers to YOUR projects
- [ ] If unsure: "Let me think..." (don't guess)
- [ ] Ask clarifying questions if needed

---

# 🎯 FINAL REMINDERS

1. **Your projects are your strength** - bring them up!
2. **Think out loud** in scenarios - show your process
3. **It's OK to not know everything** - say "I'd research that"
4. **Show enthusiasm** for security - they want passion
5. **You've prepared 900+ questions** - trust your knowledge!

---

## 🍀 GOOD LUCK GAURAB! YOU'VE GOT THIS! 🚀

---
*Interview: February 26, 2026 | 9:00 AM*
