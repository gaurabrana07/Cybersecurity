# 🗺️ SOC ANALYST — COMPLETE ROADMAP & RESOURCES

> **Goal:** From zero to corporate SOC Analyst (L1 → L2 → L3 / Threat Hunter)  
> **Community-Validated:** Resources marked with community tags based on Reddit r/netsec, r/blueteamsec, Discord communities, and practitioner feedback

---

## 📋 TABLE OF CONTENTS

1. [Roadmap Overview](#1-roadmap-overview)
2. [Phase 1 — Foundations (0-3 months)](#2-phase-1--foundations-0-3-months)
3. [Phase 2 — Core SOC Skills (3-6 months)](#3-phase-2--core-soc-skills-3-6-months)
4. [Phase 3 — Intermediate (6-12 months)](#4-phase-3--intermediate-6-12-months)
5. [Phase 4 — Advanced (12-24 months)](#5-phase-4--advanced-12-24-months)
6. [Hands-On Lab Platforms](#6-hands-on-lab-platforms)
7. [Certifications Roadmap](#7-certifications-roadmap)
8. [Books](#8-books)
9. [YouTube Channels](#9-youtube-channels)
10. [Blogs & Websites](#10-blogs--websites)
11. [Community-Validated "Best Of" List](#11-community-validated-best-of-list)
12. [Free Tools to Practice With](#12-free-tools-to-practice-with)
13. [Career Progression Map](#13-career-progression-map)

---

## 1. Roadmap Overview

```
PHASE 1           PHASE 2            PHASE 3           PHASE 4
(0-3 months)     (3-6 months)       (6-12 months)     (12-24 months)
─────────────    ─────────────      ─────────────     ─────────────
Networking       SIEM Basics        SIEM Advanced     Threat Hunting
OS Fundamentals  Log Analysis       SOAR              Malware Analysis
Security 101     Incident Response  Threat Intel      Forensics
CompTIA Sec+     Wireshark          EDR Deep Dive     MITRE ATT&CK
Linux            Alert Triage       Splunk/Sentinel    Purple Teaming
                 BTL1/CySA+         Hunting Basics     GCIH/GCIA
```

---

## 2. Phase 1 — Foundations (0-3 months)

### 🎯 Goal: Build the base that everything else sits on

### Networking Fundamentals (MUST)

| Topic | Why it matters in SOC |
|-------|----------------------|
| OSI Model (all 7 layers) | Log data references layers — know what lives where |
| TCP/IP, UDP | Packet analysis, understanding network traffic |
| DNS | C2 beaconing via DNS, DNS exfiltration detection |
| HTTP/HTTPS | Web attack analysis, proxy log reading |
| DHCP, ARP | DHCP starvation, ARP poisoning detection |
| Ports & Protocols | Know the common 100+ ports cold |
| Subnetting | Understanding IP ranges, VLANs, network segmentation |
| Firewalls, NAT | Firewall log interpretation |
| VPN | VPN logs, split tunneling risks |

**Resources:**
- 📺 **Professor Messer CompTIA Network+** — Free on YouTube `[Reddit-Top-Rated]`
  - https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/
- 📺 **NetworkChuck** — Networking fundamentals in engaging format `[YouTube-Popular]`
- 📖 **Computer Networks: A Top-Down Approach** — Kurose & Ross (textbook, thorough)
- 🛠️ **Cisco Packet Tracer** — Free network simulation tool `[Community-Recommended]`

---

### Operating Systems

| Topic | Resource |
|-------|----------|
| Windows fundamentals (AD, registry, services) | TryHackMe "Pre-Security" path |
| Linux fundamentals (bash, file system, permissions) | OverTheWire: Bandit `[Community-Classic]` |
| Windows Event Logs | Microsoft documentation + Ultimatewindowssecurity.com |
| Active Directory concepts | TryHackMe AD rooms |

**Resources:**
- 🎮 **TryHackMe — Pre-Security Path** — `[Most Recommended for Beginners]`
  - https://tryhackme.com/path/outline/presecurity
  - *"This single path prepared me better than any course I paid for"* — r/cybersecurity
- 📖 **The Linux Command Line** — William Shotts (free PDF online) `[Community-Classic]`
- 🛠️ **OverTheWire Bandit** — Linux wargame for hands-on practice

---

### Security Fundamentals

| Topic | Notes |
|-------|-------|
| CIA Triad | Foundation of all security decisions |
| Authentication vs Authorization | Know every type of auth |
| Cryptography basics (symmetric, asymmetric, hashing) | SSL/TLS inspection, encrypted traffic |
| Common attack types overview | Phishing, MITM, DoS, SQL injection |
| Security controls (preventive, detective, corrective) | Map tools to control types |

**Resources:**
- 📺 **Professor Messer CompTIA Security+ SY0-701** — Free `[#1 Community Pick for Sec+]`
- 📚 **CompTIA Security+ Get Certified Get Ahead** — Mike Chapple & David Seidl
- 🎮 **TryHackMe — SOC Level 1 Path** — `[Best structured blue team path]`

---

## 3. Phase 2 — Core SOC Skills (3-6 months)

### 🎯 Goal: Become job-ready as L1 SOC Analyst

### SIEM Fundamentals

**Learning Path:**
1. Understand what SIEM is and does
2. Learn a specific SIEM (Splunk or Microsoft Sentinel recommended)
3. Practice writing queries
4. Learn to build correlation rules
5. Understand dashboards and reporting

**Resources:**

**Splunk (Most Common in Enterprise):**
- 🎓 **Splunk Free Training** — https://www.splunk.com/en_us/training/free-courses.html `[Official, Free]`
  - "Splunk Fundamentals 1" is free and covers what you need
- 🎮 **Boss of the SOC (BOTS)** — Splunk's CTF dataset `[Practitioner-Favorite]`
  - https://bots.splunk.com/
  - *"BOTS datasets are gold — this is how you actually learn Splunk"* — Reddit consensus
- 📺 **Splunk by John's Academy** — YouTube tutorials
- 🎓 **Splunk Core Certified User** — Exam after this phase

**Microsoft Sentinel:**
- 🎓 **Microsoft Learn — SC-200 Path** — Free `[Best for Azure environments]`
  - https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-sentinel/
- 📺 **John Savill's SC-200 Sentinel tutorials** — YouTube `[Highly rated]`
- 🎮 **Microsoft Sentinel Ninja Training** — gamified learning path

---

### Log Analysis

**Resources:**
- 🎮 **Blue Team Labs Online** — `[Community Top Pick for log analysis]`
  - https://blueteamlabs.online/
  - Free tier has excellent log analysis challenges
  - *"BTL Online is what actually taught me to read logs"* — multiple Reddit posts
- 🎮 **CyberDefenders** — https://cyberdefenders.org/ `[Best Blue Team CTF Platform]`
  - SOC-focused challenges, pcap analysis, log review
  - Trusted by many hiring managers as proof of skill
- 🛠️ **Wireshark** — Network traffic analysis
  - Practice file: Wireshark Sample Captures (wiki.wireshark.org)
  - Book: *Practical Packet Analysis* — Chris Sanders `[Community-Recommended]`

---

### Incident Response Fundamentals

**Resources:**
- 📖 **NIST SP 800-61** — Computer Security Incident Handling Guide (free PDF)
  - The industry standard — read this cover to cover
- 📖 **Applied Incident Response** — Steve Anson `[Practitioner-Recommended Book]`
- 🎮 **TryHackMe — SOC Level 1 Path** — IR-focused rooms
- 📺 **Gerald Auger (Simply Cyber)** — IR concepts explained well `[YouTube-Recommended]`

---

### Alert Triage Practice

**Where to practice:**
- 🎮 **LetsDefend.io** — `[#1 Community Pick for Alert Triage Practice]`
  - https://letsdefend.io/
  - Simulates real SOC environment with tickets, SIEM, email analysis
  - *"LetsDefend is the closest thing to working in a real SOC"* — r/blueteamsec
  - Free tier available, paid tier worth it
- 🎮 **TryHackMe** — Specific rooms: "Investigating with ELK 101", "SIEM"

---

### Certification: BTL1 (Blue Team Level 1)

- **Issuer:** Security Blue Team (securityblue.team)
- **Cost:** ~\$399
- **What it covers:** Security fundamentals, phishing analysis, threat intel, SIEM, digital forensics, IR
- **Format:** 24-hour practical exam (hands-on, not MCQ)
- **Community rating:** `[Top Blue Team Cert for Beginners]`
- *"BTL1 is what CompTIA CySA+ wishes it was — pure hands-on"* — r/netsec
- **Worth it?** Absolutely for entry-level. Shows employers you can actually DO the work.

---

## 4. Phase 3 — Intermediate (6-12 months)

### 🎯 Goal: Operate confidently as L2 SOC Analyst

### Advanced SIEM

- Write complex correlation rules
- Tune rules to reduce false positives
- Understand EPS, data retention, licensing
- Build custom dashboards for management

**Resources:**
- 📖 **Splunk Enterprise Security Certified Admin** study guide
- 🎮 **Boss of the SOC v3 dataset** — Advanced Splunk scenarios
- 📺 **Tarlogic Intelligence Blog** — Advanced SIEM content

---

### SOAR

**Resources:**
- 🎓 **Palo Alto XSOAR Free Training** — `[Most Complete SOAR Training]`
  - https://www.paloaltonetworks.com/services/education/digital-learning
- 📺 **XSOAR YouTube tutorials** — XSOAR official channel
- 🎮 **Build your own SOAR playbook** — Set up free XSOAR Community Edition

---

### Threat Intelligence

**Resources:**
- 📖 **Intelligence-Driven Incident Response** — Rebekah Brown & Scott Roberts `[Essential Read]`
  - *"Changed how I think about threats — from reactive to strategic"*
- 🎓 **OpenCTI** — Free TIP platform to practice with
  - https://www.opencti.io/
- 🎮 **MISP Setup** — Set up your own MISP instance
  - https://www.misp-project.org/
- 📺 **John Hammond** — Threat intel deep dives on YouTube

---

### EDR Deep Dive

**Resources:**
- 🎮 **CrowdStrike University** — Free courses with trial account `[Employer-Recognized]`
- 🎮 **Microsoft Defender for Endpoint Trial** — 30-day enterprise trial available
- 📺 **TCM Security — Practical Malware Analysis & Triage** `[Community Top Pick]`
  - https://academy.tcm-sec.com/
  - Hands-on malware analysis to understand what EDR detects

---

### MITRE ATT&CK

**Resources:**
- 🗺️ **ATT&CK Navigator** — https://mitre-attack.github.io/attack-navigator/ `[Essential Tool]`
  - Map detections to ATT&CK, visualize coverage gaps
- 📖 **ATT&CK Framework Documentation** — attack.mitre.org (free)
- 🎮 **AttackIQ Academy** — Free ATT&CK training `[Community-Recommended]`
  - https://academy.attackiq.com/
  - *"Best free ATT&CK training available"* — multiple practitioners
- 🎮 **Atomic Red Team** — Simulate ATT&CK techniques in lab
  - https://github.com/redcanaryco/atomic-red-team

---

### Certification: CompTIA CySA+

- **What it covers:** Threat analysis, vulnerability management, incident response, SIEM, SOC operations
- **Level:** Intermediate
- **Community rating:** `[Good corporate recognition, pairs well with BTL1]`
- *"CySA+ helped me explain my blue team skills to HR that didn't understand BTL1"* — r/cybersecurity

---

## 5. Phase 4 — Advanced (12-24 months)

### 🎯 Goal: L3 Analyst / Threat Hunter / IR Specialist

### Threat Hunting

**Resources:**
- 📖 **The Threat Hunter Playbook** — Jose Rodriguez `[Open Source, Community Gold Standard]`
  - https://threathunterplaybook.com/
  - *"This is the book for threat hunting — and it's free"*
- 📖 **Practical Threat Intelligence and Data-Driven Threat Hunting** — Valentina Palacín
- 🎮 **Sigma Rules** — Write your own detection rules
  - https://github.com/SigmaHQ/sigma
- 🎮 **HELK** — Hunting ELK — free hunting lab
  - https://github.com/Cyb3rWard0g/HELK
- 🎮 **ThreatHunting.net** — Community resources

---

### Digital Forensics & Incident Response (DFIR)

**Resources:**
- 🎓 **SANS FOR508** — Advanced Incident Response & Threat Hunting `[Gold Standard, Expensive]`
  - If company pays, take it. Career-defining course.
- 📖 **The Art of Memory Forensics** — Ligh, Case, Levy `[The Definitive Memory Forensics Book]`
- 🛠️ **Volatility** — Memory forensics framework (free)
  - https://www.volatilityfoundation.org/
- 🛠️ **SIFT Workstation** — Free DFIR toolkit by SANS
- 🎮 **CyberDefenders** — Advanced DFIR challenges
- 📺 **13Cubed (Richard Davis)** — Best YouTube channel for DFIR `[Community Consensus]`
  - *"13Cubed's videos are better than most paid courses"*

---

### Malware Analysis

**Resources:**
- 📖 **Practical Malware Analysis** — Sikorski & Honig `[The Bible of Malware Analysis]`
  - *"This book is referenced in every malware analysis course ever"*
- 🎓 **TCM Security — Practical Malware Analysis & Triage** `[Best Value Course]`
  - https://academy.tcm-sec.com/p/practical-malware-analysis-triage
- 🎮 **ANY.RUN** — Interactive malware sandbox (free tier)
- 🎮 **Hybrid Analysis** — Free sandbox
- 🛠️ **Flare VM** — Windows malware analysis environment
  - https://github.com/mandiant/flare-vm
- 🛠️ **REMnux** — Linux malware analysis distribution

---

### Certifications at This Level

| Cert | Provider | Community Rating | Cost |
|------|----------|-----------------|------|
| **GCIH** | SANS GIAC | `[Gold Standard for IR]` | \$2,499 (with course) |
| **GCIA** | SANS GIAC | `[Top for Intrusion Analysis]` | \$2,499 (with course) |
| **BTL2** | Security Blue Team | `[Best value advanced blue team]` | \$999 |
| **eCIR** | eLearnSecurity | `[Good, more affordable]` | ~\$400 |
| **SC-200** | Microsoft | `[High value if org is Azure]` | ~\$165 |

---

## 6. Hands-On Lab Platforms

### Platform Comparison

| Platform | Cost | Focus | Community Rating |
|----------|------|-------|-----------------|
| **TryHackMe** | Free/\$14/mo | Guided, beginner-friendly | `[Best for Beginners]` |
| **LetsDefend** | Free/\$25/mo | SOC simulation, alert triage | `[Best SOC Practice]` |
| **CyberDefenders** | Free/Paid | Blue team CTF challenges | `[Best Blue Team CTF]` |
| **Blue Team Labs Online** | Free/Paid | Log analysis, forensics | `[Great for Log Skills]` |
| **HackTheBox** | Free/\$14/mo | More offensive, some defensive | `[Advanced Users]` |
| **SANS Cyber Ranges** | Paid | Professional-grade simulations | `[Enterprise Quality]` |
| **Splunk BOTS** | Free | Splunk-specific SOC scenarios | `[Must do for Splunk users]` |

---

## 7. Certifications Roadmap

```
ENTRY LEVEL              MID LEVEL              ADVANCED
────────────             ─────────              ────────
CompTIA Security+    →   CompTIA CySA+      →   GCIH (SANS)
(Foundation)             (Blue team focus)      (Incident Handler)

BTL1                 →   BTL2               →   GCIA (SANS)
(Practical blue team)    (Advanced practical)   (Intrusion Analyst)

Splunk Core User     →   Splunk ES Cert     →   Splunk Enterprise
                         Admin                   Architect

                         SC-200 (Sentinel)  →   SC-100 (Azure Sec)
```

---

## 8. Books

### Essential Reading (In Order)

| # | Book | Author | Why Read It |
|---|------|--------|------------|
| 1 | **CompTIA Security+ Get Certified Get Ahead** | Mike Chapple | Foundation cert prep |
| 2 | **The Practice of Network Security Monitoring** | Richard Bejtlich | `[Community Classic]` NSM fundamentals |
| 3 | **Applied Incident Response** | Steve Anson | Practical IR procedures |
| 4 | **Intelligence-Driven Incident Response** | Brown & Roberts | Threat intel in IR |
| 5 | **The Blue Team Handbook** | Don Murdoch | SOC tactical reference `[Pocket Guide]` |
| 6 | **Practical Malware Analysis** | Sikorski & Honig | When you're ready for malware |
| 7 | **The Art of Memory Forensics** | Ligh et al. | Memory forensics deep dive |
| 8 | **Threat Hunting with Elastic Stack** | Andrew Pease | Modern hunting |

---

## 9. YouTube Channels

| Channel | Focus | Community Rating |
|---------|-------|-----------------|
| **John Hammond** | Malware analysis, CTF, DFIR | `[Top Pick Overall]` |
| **Gerald Auger (Simply Cyber)** | SOC career, blue team concepts | `[Best Career Advice]` |
| **13Cubed (Richard Davis)** | DFIR, memory forensics, Windows | `[Best DFIR Channel]` |
| **TCM Security** | Ethical hacking, also blue team | `[Best Value Training]` |
| **SANS ICS Security** | SANS public talks, threat intel | `[Expert Level Content]` |
| **HuskyHacks** | Threat research, malware | `[Up and Coming]` |
| **Seytonic** | Security news, concepts | `[Good for News/Concepts]` |
| **NetworkChuck** | Networking, Linux, entry-level | `[Best for Beginners]` |

---

## 10. Blogs & Websites

| Resource | Focus | Rating |
|----------|-------|--------|
| **SANS Internet Storm Center** (isc.sans.edu) | Daily threat analysis | `[Practitioner Daily Read]` |
| **Bleeping Computer** | Malware news, IR writeups | `[Industry News Standard]` |
| **The DFIR Report** (thedfirreport.com) | Real incident writeups | `[Gold Standard for IR Reports]` |
| **Red Canary Threat Detection Report** | Annual TTPs report | `[Annual Must-Read]` |
| **Mandiant/FireEye Blog** | APT research, threat intel | `[Industry Leading Research]` |
| **Microsoft Security Blog** | Threat actor tracking, Azure security | `[Essential for M365/Sentinel]` |
| **Unit 42 (Palo Alto)** | Threat research | `[Top Threat Intel Source]` |
| **Ultimatewindowssecurity.com** | Windows Event IDs reference | `[Best Windows Event Reference]` |
| **Sigma HQ** | Detection engineering rules | `[Essential for Detection]` |

---

## 11. Community-Validated "Best Of" List

These are resources that consistently appear as top recommendations across Reddit (r/netsec, r/blueteamsec, r/cybersecurity), Discord security communities, and LinkedIn polls:

### 🥇 #1 Picks by Category

| Category | Best Resource | Why |
|----------|--------------|-----|
| **Start here** | TryHackMe SOC Level 1 Path | Structured, guided, covers all SOC basics |
| **Alert Triage Practice** | LetsDefend.io | Closest to real SOC work |
| **Blue Team CTF** | CyberDefenders.org | Employer-trusted, realistic |
| **Log Analysis** | Blue Team Labs Online | Specific, focused log challenges |
| **SIEM Learning** | Splunk BOTS Dataset | Real SOC scenarios, free |
| **Cert for Entry** | BTL1 | Proves you can do the work, not just know theory |
| **Book: Concepts** | The Blue Team Handbook | Concise, tactical, practical |
| **Book: Malware** | Practical Malware Analysis | No contest |
| **IR Real Cases** | The DFIR Report | Real attack writeups, invaluable |
| **YouTube: Career** | Simply Cyber (Gerald Auger) | Best SOC career guidance |
| **YouTube: Technical** | 13Cubed | Best DFIR technical content |

---

## 12. Free Tools to Practice With

### Set Up Your Home Lab

```
MINIMUM HOME LAB:
├── VirtualBox or VMware (free)
├── Windows 10/11 VM (evaluation license)
├── Ubuntu/Kali Linux VM
├── Splunk Free License (500MB/day)
└── ELK Stack (fully free)

RECOMMENDED ADDITIONS:
├── MISP (Threat Intel Platform)
├── Velociraptor (DFIR tool)
├── Suricata IDS
├── Zeek (Network Analysis)
└── OpenCTI (Threat Intel)
```

### Key Free Tools

| Tool | Purpose | Where to Get |
|------|---------|-------------|
| **Wireshark** | Packet analysis | wireshark.org |
| **Splunk (free)** | SIEM practice | splunk.com/free-trial |
| **Elastic SIEM** | SIEM alternative | elastic.co |
| **Volatility** | Memory forensics | volatilityfoundation.org |
| **Autopsy** | Disk forensics | sleuthkit.org |
| **MISP** | Threat intel | misp-project.org |
| **Sigma** | Detection rules | github.com/SigmaHQ/sigma |
| **YARA** | Malware detection | virustotal.github.io/yara |
| **ANY.RUN** | Online sandbox | any.run |
| **VirusTotal** | IOC lookup | virustotal.com |
| **Shodan** | Internet-wide scanning | shodan.io |

---

## 13. Career Progression Map

```
MONTH 0-3:          MONTH 3-6:          MONTH 6-12:        MONTH 12-24:
──────────          ──────────          ───────────        ────────────
Networking          BTL1 Exam           CySA+ Exam         GCIH or BTL2
Security+           LetsDefend          Advanced SIEM      Threat Hunting
Linux basics        Log analysis        Threat Intel       Malware Analysis
TryHackMe           CyberDefenders      SOAR basics        DFIR

JOB TARGETS:        JOB TARGETS:        JOB TARGETS:       JOB TARGETS:
──────────          ──────────          ───────────        ────────────
SOC Analyst L1      SOC Analyst L1      SOC Analyst L2     L3/Threat Hunter
(Fresher)           (Experienced)       (Sr. Analyst)      IR Specialist
₹3-5 LPA            ₹5-8 LPA            ₹8-15 LPA          ₹15-25+ LPA
(India)             (India)             (India)            (India)
```

### Salary Benchmarks (India, 2025-26)

| Role | Experience | Salary Range |
|------|-----------|-------------|
| SOC Analyst L1 | 0-1 yr | ₹3-6 LPA |
| SOC Analyst L2 | 1-3 yr | ₹6-12 LPA |
| SOC Analyst L3 / Sr. | 3-5 yr | ₹12-20 LPA |
| Threat Hunter | 4-7 yr | ₹18-30 LPA |
| SOC Lead / Manager | 5-10 yr | ₹25-45 LPA |

---

> **📌 Community Advice:** The biggest mistake people make is spending too long on theory and certifications without hands-on practice. Every week, spend at least 2-3 hours on platforms like LetsDefend, CyberDefenders, or your home lab. Theory without practice doesn't hold up in interviews or on the job.

> **💡 Tip from practitioners:** Follow The DFIR Report (thedfirreport.com) from Day 1 — even if you don't understand everything at first. As you learn, you'll understand more and more, and it keeps you connected to real attacks happening right now.

