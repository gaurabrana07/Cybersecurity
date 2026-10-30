# 🗺️ OFFENSIVE RED TEAMING — COMPLETE ROADMAP & RESOURCES

> **Goal:** From security fundamentals to corporate Red Team Operator / Penetration Tester  
> **Community-Validated:** Resources marked with tags from Reddit r/netsec, r/redteamsec, r/oscp, HTB community, TCM Security community, and practitioner forums

---

## 📋 TABLE OF CONTENTS

1. [Roadmap Overview](#1-roadmap-overview)
2. [Phase 1 — Foundations (0-3 months)](#2-phase-1--foundations-0-3-months)
3. [Phase 2 — Core Offensive Skills (3-6 months)](#3-phase-2--core-offensive-skills-3-6-months)
4. [Phase 3 — Intermediate (6-12 months)](#4-phase-3--intermediate-6-12-months)
5. [Phase 4 — Advanced / Red Team (12-24 months)](#5-phase-4--advanced--red-team-12-24-months)
6. [Practice Platforms](#6-practice-platforms)
7. [Certifications Roadmap](#7-certifications-roadmap)
8. [Books](#8-books)
9. [YouTube & Courses](#9-youtube--courses)
10. [Blogs & Research](#10-blogs--research)
11. [Community-Validated "Best Of" List](#11-community-validated-best-of-list)
12. [Free Tools](#12-free-tools)
13. [Career Progression & Salary Map](#13-career-progression--salary-map)

---

## 1. Roadmap Overview

```
PHASE 1             PHASE 2              PHASE 3             PHASE 4
(0-3 months)       (3-6 months)         (6-12 months)       (12-24 months)
─────────────      ─────────────        ─────────────       ─────────────
Networking 101     Web app hacking      Active Directory     Red Team Ops
Linux mastery      Buffer overflows     Evasion techniques  C2 frameworks
Python scripting   Privilege escalation Kerberos attacks    Custom tooling
Security+          Metasploit           BloodHound          Threat actor TTPs
TryHackMe path     OSCP prep            Custom exploitation Purple teaming
CTFs (beginner)    eJPT cert            HTB Pro Labs        CRTO / CRTE cert
```

---

## 2. Phase 1 — Foundations (0-3 months)

### 🎯 Goal: Build the technical base — you cannot hack what you don't understand

### Linux Mastery (Critical)

> Red teamers live in terminals. Linux proficiency is non-negotiable.

| Skill | What to practice |
|-------|-----------------|
| File system navigation | ls, cd, find, locate |
| File operations | cp, mv, rm, chmod, chown |
| Text processing | grep, awk, sed, cut, sort, uniq |
| Process management | ps, top, kill, systemctl |
| Networking | netstat/ss, curl, wget, tcpdump, iptables |
| Scripting | Bash one-liners, pipes, redirection |
| Package management | apt, yum, pip |

**Resources:**
- 🎮 **OverTheWire: Bandit** — `[Community #1 for Linux fundamentals]`
  - https://overthewire.org/wargames/bandit/
  - *"Bandit is how every red teamer should start — learn by doing"*
- 📖 **The Linux Command Line** — William Shotts (free: linuxcommand.org) `[Best Free Linux Book]`
- 🎮 **TryHackMe — Linux Fundamentals (Parts 1-3)** — Guided, beginner-friendly

---

### Networking Fundamentals

| Topic | Why critical for red teaming |
|-------|------------------------------|
| TCP/IP, OSI model | Understanding how traffic flows — what to intercept |
| Ports & protocols | Know what's running on each port |
| DNS, HTTP, TLS | Most attacks involve these |
| Routing, subnetting | Navigate and map target networks |
| Wireshark basics | Analyze your own attack traffic |

**Resources:**
- 📺 **Professor Messer Network+** — Free YouTube `[Fastest path to solid networking]`
- 🎮 **TryHackMe — Pre-Security Path** — Best structured beginning `[Community #1 Start Point]`
  - https://tryhackme.com/path/outline/presecurity

---

### Python Scripting (Essential)

Red teamers who can write tools are far more effective than those who only run them.

| Skill | Tool use case |
|-------|--------------|
| requests library | HTTP interaction, custom exploit scripts |
| socket library | Port scanners, reverse shells |
| subprocess | Execute OS commands from Python |
| struct/ctypes | Binary exploitation |
| pwntools | Exploit development framework |

**Resources:**
- 📺 **Automate the Boring Stuff with Python** — Al Sweigart (free: automatetheboringstuff.com) `[Best Free Python Book]`
- 🎮 **HackerRank Python** — Practice track
- 📺 **TCM Security — Python 101/201** — `[Best Python for hackers course]`
  - https://academy.tcm-sec.com/

---

## 3. Phase 2 — Core Offensive Skills (3-6 months)

### 🎯 Goal: Perform standard penetration testing techniques

### Web Application Hacking

**Resources:**
- 🎮 **PortSwigger Web Security Academy** — `[Community #1 — The best free web app hacking resource]`
  - https://portswigger.net/web-security
  - All labs free, covers every OWASP category with interactive labs
  - *"Web Security Academy is what universities wish they could teach — and it's free"* — r/netsec
- 📺 **TCM Security — Practical Ethical Hacking** — `[Best all-in-one pentesting course for beginners]`
  - Covers web, AD, networks — very practitioner-focused
- 🛠️ **Burp Suite Community** — Free edition, essential tool `[Install and use daily]`
- 🎮 **DVWA (Damn Vulnerable Web Application)** — Run locally, practice SQLi, XSS, etc.
- 🎮 **TryHackMe — Web Fundamentals Path** — Guided web hacking

---

### Network Penetration Testing

**Resources:**
- 📺 **TCM Security — Practical Ethical Hacking** `[Community #1 for Entry-Level Pentest]`
  - Covers full pentest methodology: recon → exploitation → post-exploitation → reporting
  - *"This course + eJPT = job-ready junior pentester"* — multiple Reddit posts
- 🎮 **TryHackMe — Jr Penetration Tester Path** — Structured full path
  - https://tryhackme.com/path/outline/jrpenetrationtester
- 🛠️ **Metasploit Unleashed** — https://www.offensive-security.com/metasploit-unleashed/ `[Free Metasploit Guide]`

---

### Privilege Escalation

**Resources:**
- 📺 **TCM Security — Windows Privilege Escalation for Beginners** `[Community Top Pick]`
  - https://academy.tcm-sec.com/
  - *"Best structured priv esc course — covers everything you'd see in OSCP"*
- 📺 **TCM Security — Linux Privilege Escalation for Beginners** — Same quality
- 🛠️ **GTFOBins** — https://gtfobins.github.io/ `[Essential daily reference for Linux priv esc]`
  - Database of Unix binaries that can be exploited for priv esc
- 🛠️ **LOLBAS** — https://lolbas-project.github.io/ `[Windows equivalent of GTFOBins]`
  - Living Off the Land Binaries and Scripts
- 🎮 **TryHackMe — Windows / Linux Priv Esc rooms** — Hands-on practice

---

### Certification: eJPT (eLearnSecurity Junior Penetration Tester)

- **Issuer:** INE / eLearnSecurity
- **Cost:** ~\$200
- **What it covers:** Network pentesting, web app basics, host enumeration
- **Format:** Practical — 72-hour exam, compromise a network
- **Community rating:** `[Best Entry-Level Practical Pentest Cert]`
- *"eJPT is the perfect first cert — proves you can actually do pentesting, not just read about it"*
- **After eJPT:** OSCP is the natural next step

---

## 4. Phase 3 — Intermediate (6-12 months)

### 🎯 Goal: Active Directory attacks, advanced techniques, OSCP-level

### Active Directory Attacks

**The most critical skill for corporate red teaming.**

**Resources:**
- 📺 **TCM Security — Practical Active Directory** `[Community #1 for AD Red Teaming]`
  - Covers: BloodHound, Kerberoasting, AS-REP Roasting, Pass-the-Hash, DCSync, etc.
  - *"This course + GOAD lab = you're ready for corporate AD engagements"*
- 🎮 **GOAD (Game of Active Directory)** — `[Community #1 AD Practice Lab]`
  - https://github.com/Orange-Cyberdefense/GOAD
  - Pre-built intentionally vulnerable AD lab — multiple domains
- 📺 **HTB Academy — Active Directory** — Comprehensive AD module `[Very Thorough]`
- 🛠️ **BloodHound CE** — https://github.com/SpecterOps/BloodHound `[Essential Tool]`
- 🛠️ **Impacket** — https://github.com/fortra/impacket `[Essential Python library for AD attacks]`
  - GetNPUsers.py, GetUserSPNs.py, secretsdump.py, psexec.py, wmiexec.py

---

### Evasion & AV Bypass

**Resources:**
- 📺 **TCM Security — Malware Development** — `[Best intro to evasion]`
- 📺 **VirtualAlloc/shellcode injection series** — Various YouTube creators
- 📖 **Sektor7 Malware Development courses** — https://institute.sektor7.net/ `[Highly Rated by Practitioners]`
  - RED TEAM Operator: Malware Development Essentials (~\$30 lifetime)
  - *"Sektor7 taught me more about evasion than any other resource"* — r/redteamsec
- 🛠️ **ThreatCheck** — Identify which bytes trigger AV detection
- 🛠️ **DefenderCheck** — Windows Defender specific evasion testing

---

### OSCP (Offensive Security Certified Professional)

**The most recognized penetration testing certification in the industry.**

- **Issuer:** Offensive Security (OffSec)
- **Cost:** \$1,499 (includes PWK course + 90 days lab time + 1 exam attempt)
- **What it covers:** Network pentesting, Linux/Windows priv esc, AD, buffer overflows, web
- **Format:** 24-hour practical exam — compromise machines, write report in 24 hours
- **Community rating:** `[Gold Standard Pentest Certification]`
- *"OSCP changed my career — it's brutal, it's worth it, and it opens doors nothing else does"*

**OSCP Prep Resources:**
- 🎮 **HTB OSCP-like machines list** — GitHub community lists `[Essential prep list]`
- 📖 **TJnull OSCP prep guide** — Google "TJnull OSCP" `[Community bible for OSCP prep]`
- 🎮 **PG Practice (OffSec Proving Grounds)** — `[Official OSCP prep labs]`
- 🎮 **TryHackMe — Jr Penetration Tester + Offensive Pentesting paths**
- 📺 **ippsec YouTube** — HTB machine walkthroughs `[Community #1 for learning methodology]`

---

## 5. Phase 4 — Advanced / Red Team (12-24 months)

### 🎯 Goal: True red team operator — full adversary simulation, C2, evasion

### C2 Frameworks & Infrastructure

**Resources:**
- 🎓 **Cobalt Strike Training** — https://www.cobaltstrike.com/training/ `[Industry Standard C2]`
  - Free videos + paid courses
  - Most corporate red teams use Cobalt Strike
- 🛠️ **Sliver C2** — https://github.com/BishopFox/sliver `[Best Free Modern C2]`
  - Open source, actively maintained, great documentation
  - *"Sliver is what you use when you can't afford Cobalt Strike — it's excellent"*
- 📺 **Cobalt Strike YouTube** — Raphael Mudge's original tutorials `[Historical but foundational]`

---

### Threat Actor Research (APT TTPs)

**Resources:**
- 🗺️ **MITRE ATT&CK** — https://attack.mitre.org/ `[Essential — Know Every Technique]`
- 📖 **Mandiant APT Reports** — Google "Mandiant APT28", "Mandiant UNC2165" etc.
- 📖 **CrowdStrike Adversary Intelligence** — Threat actor profiles
- 📖 **SpecterOps reports** — https://posts.specterops.io/ `[Deep AD/Windows research]`
- 📖 **The DFIR Report** — https://thedfirreport.com/ `[Real attack timelines — gold for red teamers]`
  - *"Reading DFIR Report teaches you how real attackers operate — no course teaches this"*

---

### Certification: CRTO (Certified Red Team Operator)

- **Issuer:** Zero-Point Security (RastaMouse)
- **Cost:** ~£399
- **What it covers:** Cobalt Strike, full red team ops, AD attacks, evasion, OPSEC
- **Format:** 48-hour practical exam in Cobalt Strike lab
- **Community rating:** `[Best Red Team Specific Cert — Community Favorite]`
- *"CRTO > OSCP for pure red team work — it's focused on how corporate engagements actually work"*
- https://training.zeropointsecurity.co.uk/courses/red-team-ops

**Other Advanced Certs:**

| Cert | Provider | Focus | Rating |
|------|----------|-------|--------|
| **CRTE** | Altered Security | AD red teaming | `[Deep AD red team focus]` |
| **CRTL** | Zero-Point Security | Red team lead | `[Advanced CRTO follow-up]` |
| **OSED** | OffSec | Exploit development | `[Advanced — hard]` |
| **OSEP** | OffSec | Evasion + advanced pentesting | `[Advanced — respected]` |
| **CRTO** | Zero-Point Security | Red team operations | `[#1 Red Team Cert]` |

---

## 6. Practice Platforms

| Platform | Cost | Focus | Rating |
|----------|------|-------|--------|
| **TryHackMe** | Free/\$14 | Guided, beginner-friendly paths | `[#1 for Beginners]` |
| **HackTheBox** | Free/\$14 | Realistic machines, more independent | `[#1 for Intermediate+]` |
| **PortSwigger Web Academy** | Free | Web app hacking — the best | `[#1 for Web App]` |
| **GOAD** | Free | Active Directory red team lab | `[#1 AD Red Team Lab]` |
| **HTB Pro Labs** | Paid (~\$28/mo) | Full corporate network simulation | `[Best Corporate Simulation]` |
| **PG Practice** | \$19/mo | OSCP prep machines | `[Best OSCP Prep]` |
| **VulnHub** | Free | Downloadable vulnerable VMs | `[Good for offline practice]` |
| **HackTheBox Academy** | Free/Paid | Structured learning paths | `[Best Structured HTB Learning]` |
| **PentesterLab** | Free/Paid | Web-focused, code-level understanding | `[Best for Code-Level Web Attacks]` |
| **Root-Me** | Free | Challenges across categories | `[Good variety]` |

---

## 7. Certifications Roadmap

```
ENTRY                        MID                         ADVANCED
─────                        ───                         ────────
CompTIA Security+        →   eJPT (eLearnSecurity)   →   OSCP (OffSec)
(Foundation)                 (First practical cert)       (Gold standard)

                         →   CEH (EC-Council)         →   CRTO (Zero-Point)
                             (Corporate recognition)       (Red team specific)

                                                      →   OSEP (OffSec)
                                                          (Evasion/advanced)

                                                      →   CRTE (Altered Sec)
                                                          (AD deep dive)
```

---

## 8. Books

| # | Book | Author | Why Read It |
|---|------|--------|------------|
| 1 | **Penetration Testing** | Georgia Weidman | `[Best intro pentest book]` — practical from page 1 |
| 2 | **The Hacker Playbook 2 & 3** | Peter Kim | `[Community Classic]` — real engagement methodology |
| 3 | **Red Team Development and Operations** | Joe Vest & James Tubberville | Red team program building |
| 4 | **Hacking: The Art of Exploitation** | Erickson | Deep technical — buffer overflows, shellcode |
| 5 | **The Web Application Hacker's Handbook** | Stuttard & Pinto | Web hacking bible `[Still relevant]` |
| 6 | **Operator Handbook** | Joshua Picolet | Quick reference for red team operations |
| 7 | **Adversarial Tradecraft in Cybersecurity** | Dan Borges | OPSEC and real red team methodology |
| 8 | **The Art of Intrusion** | Kevin Mitnick | Real-world social engineering stories |

---

## 9. YouTube & Courses

| Channel / Course | Focus | Rating |
|------------------|-------|--------|
| **TCM Security** | Pentest training, AD attacks, OSCP prep | `[#1 Value for Money — Community Consensus]` |
| **ippsec** | HTB walkthroughs, methodology deep dives | `[#1 for Learning by Watching]` |
| **John Hammond** | CTF, malware, practical hacking | `[Best Variety — High Quality]` |
| **HackerSploit** | Metasploit, pentest tools | `[Good for Tool Learning]` |
| **Rana Khalil** | Web app hacking (PortSwigger focused) | `[Best Web App Video Content]` |
| **VbScrub** | Active Directory attacks, Windows | `[Deep AD technical content]` |
| **S3cur3Th1sSh1t** | Evasion, C2, red team ops | `[Advanced evasion content]` |
| **0xdf** | HTB writeups, methodology | `[Clean Methodology Explanations]` |
| **STÖK** | Bug bounty, recon, web hacking | `[Best for Bug Bounty Path]` |

---

## 10. Blogs & Research

| Resource | Focus | Rating |
|----------|-------|--------|
| **SpecterOps Posts** (posts.specterops.io) | Deep AD/Windows offensive research | `[Industry-Leading Research]` |
| **The DFIR Report** (thedfirreport.com) | Real attack timelines (attacker view) | `[Red Team Gold — Real TTPs]` |
| **harmj0y blog** (harmj0y.net) | Kerberos attacks, AD exploitation | `[Community Classic — Essential]` |
| **Hack Tricks** (book.hacktricks.xyz) | Comprehensive pentest wiki | `[Best All-in-One Reference]` |
| **PayloadAllTheThings** | GitHub repo of payloads | `[Essential Reference]` |
| **Red Teaming Experiments** (ired.team) | Red team techniques documented | `[Excellent Practical Reference]` |
| **S3cur3Th1sSh1t Blog** | C2, evasion techniques | `[Advanced Evasion]` |
| **AD Security** (adsecurity.org) | Sean Metcalf's AD security research | `[Foundational AD Attack Research]` |

---

## 11. Community-Validated "Best Of" List

| Category | Best Resource | Why |
|----------|--------------|-----|
| **Start here** | TryHackMe Pre-Security + Jr Pentest path | Most structured beginner path |
| **Web hacking** | PortSwigger Web Security Academy | No contest — free + interactive |
| **AD attacks** | TCM Security Practical AD course | Best value, most practical |
| **AD lab** | GOAD | Most realistic free AD environment |
| **OSCP prep** | ippsec YouTube + TJnull machine list | Community consensus since OSCP exists |
| **C2 framework** | Sliver (free) or Cobalt Strike (paid) | Sliver for learning; CS for engagements |
| **Book: Methodology** | The Hacker Playbook 3 | Real engagement methodology |
| **Book: Technical** | Hacking: Art of Exploitation | Deep technical foundation |
| **Cert: First** | eJPT | Practical proof of skill for entry level |
| **Cert: Career-defining** | OSCP | Opens more doors than any other cert |
| **Cert: Red Team** | CRTO | Best red team specific cert available |
| **Reference: Attacks** | HackTricks | Best all-in-one pentest reference |
| **Reference: Payloads** | PayloadAllTheThings | Essential payload repository |

---

## 12. Free Tools

| Tool | Purpose | Link |
|------|---------|------|
| **Nmap** | Port scanning, service enumeration | nmap.org |
| **Metasploit** | Exploitation framework | metasploit.com |
| **Burp Suite Community** | Web app proxy, testing | portswigger.net |
| **Gobuster / ffuf** | Directory/subdomain brute force | GitHub |
| **Nikto** | Web server vulnerability scanner | GitHub |
| **SQLmap** | Automated SQL injection | sqlmap.org |
| **Impacket** | Python AD attack tools | github.com/fortra/impacket |
| **BloodHound CE** | AD attack path analysis | github.com/SpecterOps/BloodHound |
| **SharpHound** | BloodHound data collector | GitHub |
| **Mimikatz** | Credential dumping | github.com/gentilkiwi/mimikatz |
| **Rubeus** | Kerberos attack tool | github.com/GhostPack/Rubeus |
| **PowerView** | AD enumeration | github.com/PowerShellMafia/PowerSploit |
| **CrackMapExec (CME)** | Swiss army knife for AD | github.com/byt3bl33d3r/CrackMapExec |
| **Responder** | LLMNR/NBT-NS poisoning | github.com/lgandx/Responder |
| **Sliver C2** | Modern C2 framework | github.com/BishopFox/sliver |
| **linPEAS/winPEAS** | Linux/Windows priv esc enum | github.com/carlospolop/PEASS-ng |
| **GTFOBins** | Linux priv esc reference | gtfobins.github.io |
| **LOLBAS** | Windows priv esc reference | lolbas-project.github.io |
| **Subfinder** | Subdomain discovery | github.com/projectdiscovery/subfinder |
| **amass** | DNS enumeration | github.com/OWASP/Amass |
| **theHarvester** | Email/subdomain harvesting | GitHub |
| **Maltego (Free)** | OSINT graphing | maltego.com |
| **OWASP ZAP** | Web app scanner (free alt to Burp Pro) | zaproxy.org |

---

## 13. Career Progression & Salary Map

```
MONTH 0-3:              MONTH 3-6:           MONTH 6-12:        MONTH 12-24:
──────────              ──────────           ───────────        ────────────
TryHackMe path          eJPT cert            OSCP prep          OSCP + CRTO
Linux mastery           HTB Easy boxes       HTB Medium boxes   Advanced AD
Web basics              Web Academy labs     AD red team labs   C2 development
Python scripting        Full pentest reports GOAD practice      APT TTPs study

JOB TARGETS:            JOB TARGETS:         JOB TARGETS:       JOB TARGETS:
──────────              ──────────           ───────────        ────────────
SOC Analyst             Jr. Pentester        Pentester          Red Team Operator
(build blue know.)      Jr. Red Teamer       Vulnerability Eng  Sr. Pentester
Bug Bounty Hunting      Security Analyst     Bug Bounty Pro     Red Team Lead
₹3-6 LPA                ₹5-10 LPA            ₹10-20 LPA         ₹20-40+ LPA
(India)                 (India)              (India)            (India)
```

### Specialization Paths

```
Offensive Security Foundation
          │
          ├──▶ Web Application Penetration Tester
          │         OSCP + Burp Suite expertise + web research
          │         Target: Product companies, fintech, e-commerce
          │
          ├──▶ Network / Infrastructure Pentester
          │         OSCP + AD expertise + CRTE
          │         Target: MSSP, consulting firms
          │
          ├──▶ Red Team Operator
          │         OSCP + CRTO + C2 expertise + evasion
          │         Target: Large enterprises, government, finance
          │
          ├──▶ Bug Bounty Hunter (Independent)
          │         OSCP + web expertise + automation
          │         Target: HackerOne, Bugcrowd programs
          │
          └──▶ Exploit Developer / Vulnerability Researcher
                    OSED + reverse engineering + deep binary skills
                    Target: Security vendors, government, elite consulting
```

---

> **📌 Community Advice:** The most important skill isn't knowing specific tools — it's methodology. Tools change, get detected, or break. Methodology doesn't. Learn WHY each technique works, not just HOW to run a script. *"The best pentesters I've hired couldn't name the latest CVE off the top of their head — but they could think through any situation and find a path. That's what matters."* — Senior Red Team Lead, Reddit.

> **⚠️ Important:** Always practice on authorized systems only. Use TryHackMe, HackTheBox, GOAD, and your own lab. Unauthorized access is a crime regardless of intent.

