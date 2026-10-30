# 🗺️ NETWORK SECURITY — COMPLETE ROADMAP & RESOURCES

> **Goal:** From networking fundamentals to corporate Network Security Engineer  
> **Community-Validated:** Resources marked with community tags from Reddit r/netsec, r/networking, r/homelab, SANS community, and Cisco community forums

---

## 📋 TABLE OF CONTENTS

1. [Roadmap Overview](#1-roadmap-overview)
2. [Phase 1 — Networking Foundations (0-3 months)](#2-phase-1--networking-foundations-0-3-months)
3. [Phase 2 — Core Network Security (3-6 months)](#3-phase-2--core-network-security-3-6-months)
4. [Phase 3 — Intermediate (6-12 months)](#4-phase-3--intermediate-6-12-months)
5. [Phase 4 — Advanced / Specialization (12-24 months)](#5-phase-4--advanced--specialization-12-24-months)
6. [Hands-On Lab Platforms](#6-hands-on-lab-platforms)
7. [Certifications Roadmap](#7-certifications-roadmap)
8. [Books](#8-books)
9. [YouTube & Courses](#9-youtube--courses)
10. [Blogs & Websites](#10-blogs--websites)
11. [Community-Validated "Best Of" List](#11-community-validated-best-of-list)
12. [Free Tools to Practice With](#12-free-tools-to-practice-with)
13. [Career Progression & Salary Map](#13-career-progression--salary-map)

---

## 1. Roadmap Overview

```
PHASE 1             PHASE 2               PHASE 3            PHASE 4
(0-3 months)       (3-6 months)          (6-12 months)      (12-24 months)
─────────────      ─────────────         ─────────────      ─────────────
OSI / TCP-IP       Firewall config        NGFW (Palo Alto)   Threat hunting
Subnetting         IDS/IPS (Snort)        SSL Inspection     Cloud security
Wireshark          VPN config             Zero Trust         SASE / ZTNA
Network+           Packet analysis        NetFlow/Zeek       Advanced forensics
Linux networking   Network attacks        WLAN security      PCNSE / CCNP Sec
Lab: GNS3/EVE-NG   Lab: Snort rules       DDoS mitigation    Architecture design
```

---

## 2. Phase 1 — Networking Foundations (0-3 months)

### 🎯 Goal: Understand networking deeply before adding security

### Core Networking

| Topic | Must Know Level |
|-------|----------------|
| OSI Model (all 7 layers) | Know by heart — which protocol lives where |
| TCP/IP (IPv4 + IPv6) | How packets flow end-to-end |
| Subnetting | Calculate subnets, CIDR notation, VLSM |
| TCP three-way handshake | Flags, states, attacks |
| DNS — how resolution works | Full recursive resolution flow |
| DHCP — how addressing works | DORA process |
| HTTP/HTTPS | Request/response cycle, headers, methods |
| ARP | How MAC addresses are resolved |
| Routing basics (static, OSPF, BGP) | What a routing table looks like |
| Switching (VLANs, STP, trunking) | Enterprise switch config basics |

**Resources:**
- 📺 **Professor Messer CompTIA Network+ N10-009** — Free YouTube `[Community #1 for Network+]`
  - https://www.professormesser.com/network-plus/
  - *"Professor Messer's free Network+ course is as good as any paid course"* — r/CompTIA
- 📖 **Computer Networks: A Top-Down Approach** — Kurose & Ross `[Best Textbook for Deep Understanding]`
  - *"Every concept explained intuitively from application down — the opposite of boring"*
- 📺 **NetworkChuck** — Subnetting, VLANs, practical labs `[Best for Visual Learners]`
- 🛠️ **Cisco Packet Tracer** — Free network simulation `[Community-Favorite Beginner Tool]`
  - https://www.netacad.com/courses/packet-tracer

---

### Hands-On Networking Lab

**Resources:**
- 🛠️ **GNS3** — https://www.gns3.com/ `[Community #1 for Advanced Network Labs]`
  - Emulate real Cisco, Juniper, Palo Alto devices
  - *"GNS3 is what separates people who understand networking from those who memorized answers"*
- 🛠️ **EVE-NG Community** — https://www.eve-ng.net/ `[Alternative to GNS3, web-based UI]`
  - Better web interface, more enterprise-oriented
- 🛠️ **Cisco Packet Tracer** — Easier entry point than GNS3

---

### Linux Networking

| Topic | Command |
|-------|---------|
| View interfaces | `ip a` or `ifconfig` |
| View routing table | `ip route` or `netstat -rn` |
| Test connectivity | `ping`, `traceroute`, `mtr` |
| DNS lookup | `dig`, `nslookup`, `host` |
| Port listening | `ss -tlnp` or `netstat -tlnp` |
| Firewall rules | `iptables -L` or `nft list ruleset` |
| Packet capture | `tcpdump -i eth0 port 80` |

**Resources:**
- 🎮 **OverTheWire: Bandit** — Linux fundamentals through games `[Community Classic]`
- 📺 **The Linux Command Line** — William Shotts (free PDF) `[Best Linux book for free]`
- 🎮 **TryHackMe — Linux Fundamentals Path** — Guided, beginner-friendly

---

## 3. Phase 2 — Core Network Security (3-6 months)

### 🎯 Goal: Deploy and manage basic network security controls

### Firewall Fundamentals

**Resources:**
- 📺 **Palo Alto Networks Free Training (EDU-110)** `[Community Top Pick for Firewalls]`
  - https://education.paloaltonetworks.com/learningcenter
  - Firewall Essentials course (free)
  - *"Palo Alto free training gives you real NGFW knowledge — not generic theory"*
- 📺 **Fortinet Free NSE Training** — https://training.fortinet.com/ `[Free, Excellent]`
  - NSE 1, 2, 3 are free and cover firewall concepts well
  - NSE 4 (FortiGate admin) has free resources
- 🛠️ **pfSense / OPNsense** — Free open-source firewall for home lab `[Community Favorite]`
  - Deploy on a VM, configure rules, VLANs, VPN
  - *"pfSense in a home lab teaches you more than any textbook"* — r/homelab
- 🎓 **Cisco NetAcad — Network Security** — Free courses `[Good structured content]`

---

### Packet Analysis — Wireshark Mastery

**Resources:**
- 📺 **Chris Greer (Packet Pioneer)** — YouTube `[Community #1 for Wireshark]`
  - https://www.youtube.com/@PacketPioneer
  - *"Chris Greer is THE Wireshark instructor — no one explains it better"*
- 📖 **Practical Packet Analysis** — Chris Sanders `[Community Recommended Book]`
  - https://nostarch.com/packetanalysis3
  - Goes from basics to advanced threat hunting with Wireshark
- 🎮 **Wireshark sample captures** — https://wiki.wireshark.org/SampleCaptures
  - Practice on real traffic captures covering many protocols and attacks
- 🎮 **CloudShark** — Web-based PCAP analysis — good for learning without installing

---

### IDS/IPS — Snort & Suricata

**Resources:**
- 📖 **Snort Official Documentation** — https://snort.org/documents `[Official, Comprehensive]`
- 📺 **Building Network Intrusion Detection** — Bamm Visscher, YouTube series
- 🛠️ **Security Onion** — https://securityonionsolutions.com/ `[Community #1 Recommendation]`
  - Free Linux distro combining: Zeek, Suricata, Elastic SIEM, and more
  - *"Security Onion is the fastest way to get a full NSM stack running in your lab"*
  - Deploy on a VM, connect your home lab traffic to it
- 🎮 **TryHackMe — IDS rooms** — "Snort", "Zeek" rooms (hands-on)

---

### VPN Configuration

**Resources:**
- 📺 **WireGuard Setup** — NetworkChuck YouTube `[Best WireGuard walkthrough]`
  - https://www.youtube.com/watch?v=SMIbrgoDpRU
- 🛠️ **OpenVPN Community** — Set up in your lab (free)
- 📖 **VPN — Site-to-Site IPsec** — Cisco DevNet documentation
- 🎮 **TryHackMe — OpenVPN room** — Hands-on

---

### Certification: CompTIA Network+

- **What it covers:** Full networking stack — protocols, routing, switching, troubleshooting
- **Level:** Entry
- **Community rating:** `[Essential baseline — many jobs require it]`
- *"Network+ is the foundation everything else is built on — don't skip it"* — r/netsec

---

## 4. Phase 3 — Intermediate (6-12 months)

### 🎯 Goal: Enterprise-grade network security deployment and analysis

### NGFW — Palo Alto Deep Dive

**Resources:**
- 🎓 **Palo Alto Networks EDU-110 & EDU-120** `[Industry Standard Training]`
  - Firewall Essentials (EDU-110) → Firewall: Install, Configure, Manage (EDU-120)
  - Hands-on labs with NGFW
- 🎓 **Palo Alto PCNSE Exam Prep** — Study guide available
- 🛠️ **PAN-OS VM-Series Trial** — Run Palo Alto NGFW as VM (evaluation license)
  - https://live.paloaltonetworks.com/t5/customer-resources/support-home/ta-p/214208
- 📖 **Palo Alto Documentation** — https://docs.paloaltonetworks.com/ `[Comprehensive]`

---

### Network Traffic Analysis & Threat Hunting

**Resources:**
- 📖 **The Practice of Network Security Monitoring** — Richard Bejtlich `[Community Gold Standard]`
  - *"This book defined the NSM discipline — every network security practitioner should read it"*
  - https://nostarch.com/nsm
- 🛠️ **Security Onion with PCAP hunting** — Use BOTS (Splunk) PCAPs in Security Onion
- 🎮 **Malware-Traffic-Analysis.net** — `[Community Favorite for Real Malware PCAPs]`
  - https://www.malware-traffic-analysis.net/
  - Real malware traffic captures with analysis exercises
  - *"This site is invaluable — practicing on real attack traffic is irreplaceable"*
- 🎮 **CyberDefenders** — Network forensics challenges `[Best Blue Team CTF for Network]`

---

### DNS Security

**Resources:**
- 📺 **DNS Security — Cloudflare YouTube** — Excellent DNS attack explanations
- 📖 **DNS and BIND** — Albitz & Liu (O'Reilly) — Deep DNS reference
- 🛠️ **DNSdumpster** — https://dnsdumpster.com/ — DNS reconnaissance (understand what attackers see)
- 🛠️ **PassiveDNS tools** — Understand DNS history and fast flux detection

---

### Zeek (Network Security Monitoring)

**Resources:**
- 🎓 **Zeek Official Training** — https://try.bro.org/ `[Free Interactive Zeek Tutorial]`
- 📖 **Zeek Documentation** — https://docs.zeek.org/
- 🎮 **Security Onion includes Zeek** — Practice on your home lab traffic
- 📺 **Corelight (Zeek company) YouTube** — Technical Zeek content

---

### Certification: CompTIA Security+

If not already done — covers network security extensively alongside other domains.

**Certification: Palo Alto PCNSE (if Palo Alto shop):**
- Certified Network Security Engineer
- Industry's most respected NGFW cert
- Community rating: `[Highest value for firewall-focused roles]`

---

## 5. Phase 4 — Advanced / Specialization (12-24 months)

### 🎯 Goal: Architect-level network security, cloud-native security, advanced threat detection

### SASE / Zero Trust Networking

**Resources:**
- 📖 **Zero Trust Networks** — Evan Gilman & Doug Barth `[The Definitive Zero Trust Book]`
- 🎓 **Zscaler Training** — https://training.zscaler.com/ `[Free Zero Trust courses]`
  - Zscaler Internet Access (ZIA) and Private Access (ZPA) training
  - Zscaler Zero Trust Architect certification
- 📺 **John Savill's Zero Trust Series** — YouTube `[Best free ZT content]`
- 🎓 **Cloudflare Zero Trust Documentation** — https://developers.cloudflare.com/cloudflare-one/

---

### Cloud Network Security

**Resources:**
- 🎓 **AWS Security Specialty** exam prep — covers VPC security in depth
  - Adrian Cantrill (cantrill.io) `[Community #1 for AWS cert prep]`
  - Tutorial Dojo practice exams `[Best AWS practice questions]`
- 🎓 **Azure Network Security** — SC-100 (Microsoft Security Architect)
  - Microsoft Learn path (free) `[Official, comprehensive]`
- 🎓 **GCP Professional Cloud Security Engineer** — covers GCP network security
- 📺 **freeCodeCamp AWS Security** — YouTube, 8 hours `[Best free AWS Security intro]`

---

### Advanced Network Forensics & Incident Response

**Resources:**
- 📖 **Network Forensics: Tracking Hackers Through Cyberspace** — Davidoff & Ham `[Network Forensics Bible]`
- 🛠️ **Arkime (Moloch)** — Full packet capture and search `[Enterprise PCAP at scale]`
  - https://arkime.com/ — Open source, used by many enterprises
- 🎮 **CyberDefenders — Network Forensics challenges** `[Best practice for network forensics]`
- 🎓 **SANS FOR572** — Advanced Network Forensics (if company pays) `[Gold standard, expensive]`

---

### Advanced Certifications

| Cert | Provider | Community Rating |
|------|----------|-----------------|
| **Cisco CCNP Security** | Cisco | `[Top for Cisco-heavy environments]` |
| **Palo Alto PCNSE** | Palo Alto | `[Top for Palo Alto environments]` |
| **Fortinet NSE 7** | Fortinet | `[High value in Fortinet shops]` |
| **GIAC GPEN** | SANS | `[Network penetration testing — understand attacks]` |
| **GIAC GWAPT** | SANS | `[Web app network security testing]` |
| **GIAC GNFA** | SANS | `[Network forensic analyst — advanced detection]` |
| **AWS Security Specialty** | AWS | `[High demand for cloud network security]` |
| **Certified Network Defender (CND)** | EC-Council | `[Good corporate recognition]` |

---

## 6. Hands-On Lab Platforms

| Platform | Cost | Focus | Rating |
|----------|------|-------|--------|
| **Security Onion** | Free | Full NSM stack: Zeek+Suricata+SIEM | `[#1 Home Lab NSM Platform]` |
| **GNS3** | Free | Network device emulation | `[#1 for Network Labs]` |
| **EVE-NG Community** | Free | Advanced network emulation | `[Great GNS3 Alternative]` |
| **pfSense/OPNsense** | Free | Real firewall in lab | `[Best Firewall Lab Tool]` |
| **TryHackMe** | Free/\$14 | Guided network security rooms | `[Best Guided Learning]` |
| **HackTheBox** | Free/\$14 | Network challenges, more offensive | `[Advanced Practice]` |
| **CyberDefenders** | Free/Paid | Network forensics CTF | `[Best Network CTF]` |
| **Malware-Traffic-Analysis** | Free | Real malware PCAPs | `[Unique, Invaluable]` |
| **Palo Alto VM-Series** | Free trial | Real NGFW lab | `[Best NGFW Practice]` |

### Home Lab Architecture Recommendation

```
MINIMAL NETWORK SECURITY HOME LAB:

┌─────────────────────────────────────────────────────┐
│  YOUR HOST MACHINE (16GB RAM recommended)           │
│                                                     │
│  VirtualBox / VMware Workstation                    │
│                                                     │
│  ┌─────────────────┐  ┌─────────────────────────┐  │
│  │  pfSense/OPNsense│  │  Security Onion          │  │
│  │  (Firewall)      │  │  (Zeek + Suricata + ELK) │  │
│  └─────────────────┘  └─────────────────────────┘  │
│                                                     │
│  ┌─────────────────┐  ┌─────────────────────────┐  │
│  │  Kali Linux     │  │  Windows 10 (target)    │  │
│  │  (Attacker)     │  │  (Victim)               │  │
│  └─────────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────┘

WHAT YOU CAN PRACTICE:
  - Configure pfSense firewall rules
  - Run Kali attacks → capture with Security Onion
  - Write Snort/Suricata rules to detect attacks
  - Analyze Zeek logs for threat hunting
  - Practice Wireshark analysis on captured traffic
```

---

## 7. Certifications Roadmap

```
ENTRY                        MID                         ADVANCED
─────                        ───                         ────────
CompTIA Network+         →   CompTIA Security+        →   CCNP Security
(Networking foundation)      (Security fundamentals)      (Cisco advanced)

                         →   Palo Alto PCNSA          →   Palo Alto PCNSE
                             (Associate)                  (Engineer — top cert)

                         →   Fortinet NSE 4          →   Fortinet NSE 7
                             (FortiGate admin)            (Enterprise security)

                         →   CEH (EC-Council)         →   GPEN (SANS GIAC)
                             (Attack awareness)           (Penetration testing)

                                                      →   GNFA (SANS GIAC)
                                                          (Network forensics)

                                                      →   AWS Security Specialty
                                                          (Cloud network sec)
```

---

## 8. Books

| # | Book | Author | Why Read It |
|---|------|--------|------------|
| 1 | **Computer Networks: A Top-Down Approach** | Kurose & Ross | `[Best networking textbook]` — conceptually strongest |
| 2 | **The Practice of Network Security Monitoring** | Richard Bejtlich | `[NSM Bible — Community Gold Standard]` |
| 3 | **Practical Packet Analysis** | Chris Sanders | Wireshark for security, hands-on |
| 4 | **Network Security Assessment** | Chris McNab | Assess and harden networks |
| 5 | **Zero Trust Networks** | Gilman & Barth | Modern architecture approach |
| 6 | **Network Forensics: Tracking Hackers** | Davidoff & Ham | `[Network Forensics reference]` |
| 7 | **Hacking: The Art of Exploitation** | Erickson | TCP/IP attacks from attacker's lens |
| 8 | **DNS and BIND** | Albitz & Liu | Deep DNS reference |

---

## 9. YouTube & Courses

| Channel / Course | Focus | Rating |
|------------------|-------|--------|
| **Professor Messer** | Network+, Security+ | `[#1 Free Cert Prep]` |
| **NetworkChuck** | Networking, VPN, Linux | `[Best for Beginners — Engaging]` |
| **Chris Greer (Packet Pioneer)** | Wireshark deep dives | `[#1 Wireshark Channel]` |
| **David Bombal** | Networking, ethical hacking | `[Good technical depth]` |
| **John Hammond** | Attack analysis, captures | `[Good for attacker-aware thinking]` |
| **Palo Alto Networks** | NGFW training | `[Official — Essential for NGFW]` |
| **Fortinet NSE Institute** | FortiGate training | `[Official — Free NSE courses]` |
| **SANS ICS Security** | Advanced talks, threat research | `[Expert content]` |
| **TCM Security** | Ethical hacking, network attacks | `[Good for attack perspective]` |

---

## 10. Blogs & Websites

| Resource | Focus | Rating |
|----------|-------|--------|
| **SANS Internet Storm Center** (isc.sans.edu) | Daily threat analysis | `[Daily Must-Read for Network Defenders]` |
| **Malware-Traffic-Analysis.net** | Real attack PCAPs with exercises | `[Unique — Practice with real traffic]` |
| **Packet Life** (packetlife.net) | Protocol reference, cheat sheets | `[Essential Reference Site]` |
| **Cloudflare Blog** | DDoS, DNS, network security | `[High-quality technical content]` |
| **Zeek Blog** | Network security monitoring | `[Best NSM content]` |
| **Shodan Blog** | Internet exposure, IoT security | `[See what attackers see]` |
| **ARIN, RIPE, APNIC** | BGP, routing, IP address management | `[Essential for understanding routing]` |
| **BGPmon.net** | BGP monitoring, hijack detection | `[BGP security reference]` |
| **NetSecFocus** | Network security community | `[Community discussion]` |

---

## 11. Community-Validated "Best Of" List

| Category | Best Resource | Why |
|----------|--------------|-----|
| **Start here** | Professor Messer Network+ (free) | Best free structured networking course |
| **Lab setup** | Security Onion | Fastest path to full NSM lab |
| **Packet analysis** | Chris Greer (YouTube) + Practical Packet Analysis | Best combination |
| **Firewall lab** | pfSense on VirtualBox | Free, real-world firewall experience |
| **Real attack PCAPs** | Malware-Traffic-Analysis.net | No substitute for real attack traffic |
| **NGFW training** | Palo Alto free EDU-110 | Best free enterprise firewall content |
| **Network CTF** | CyberDefenders | Employer-trusted, realistic scenarios |
| **Book: NSM** | The Practice of Network Security Monitoring | No contest — the NSM bible |
| **Book: Packets** | Practical Packet Analysis | Best Wireshark book |
| **Cert: Entry** | CompTIA Network+ | Essential foundation |
| **Cert: Mid** | PCNSE (Palo Alto) or CCNP Security | Highest employer value |
| **Cert: Advanced** | GNFA (SANS GIAC) | Network forensics gold standard |

---

## 12. Free Tools to Practice With

| Tool | Purpose | Get It |
|------|---------|--------|
| **Wireshark** | Packet capture & analysis | wireshark.org |
| **tcpdump** | Command-line packet capture | Built into Linux |
| **Nmap** | Network scanning & discovery | nmap.org |
| **Netcat (nc)** | Network debugging, port scanning | Built into Linux |
| **Zeek** | Network security monitoring | zeek.org |
| **Suricata** | IDS/IPS engine | suricata.io |
| **pfSense** | Firewall OS | pfsense.org |
| **Security Onion** | Full NSM stack | securityonionsolutions.com |
| **GNS3** | Network emulation | gns3.com |
| **Scapy** | Craft and send packets (Python) | scapy.net |
| **Hping3** | Packet crafting, testing | hping.org |
| **Masscan** | Internet-scale port scanner | github.com/robertdavidgraham/masscan |
| **DNS Dumpster** | Passive DNS reconnaissance | dnsdumpster.com |
| **Shodan** | Internet-exposed asset scanning | shodan.io (free tier) |
| **OpenVAS** | Open-source vulnerability scanner | openvas.org |
| **Arkime** | Full packet capture at scale | arkime.com |

---

## 13. Career Progression & Salary Map

```
MONTH 0-3:              MONTH 3-6:           MONTH 6-12:        MONTH 12-24:
──────────              ──────────           ───────────        ────────────
Network+ cert           Security+ cert       PCNSE / CCNP       AWS Security Spec
GNS3 lab setup          pfSense lab          Security Onion      GNFA (SANS)
Wireshark basics        Snort rule writing   NGFW administration Zero Trust design
TCP/IP mastery          VPN configuration    Cloud networking    Architecture role

JOB TARGETS:            JOB TARGETS:         JOB TARGETS:       JOB TARGETS:
──────────              ──────────           ───────────        ────────────
Network Admin           Jr. Net Sec Eng.     Net Security Eng.  Net Sec Architect
NOC Analyst             Firewall Admin       Sr. Net Sec Eng.   Cloud Net Sec Lead
₹3-5 LPA                ₹5-9 LPA             ₹9-18 LPA          ₹18-35+ LPA
(India)                 (India)              (India)            (India)
```

### Specialization Paths

```
Network Security Foundation
          │
          ├──▶ Firewall / NGFW Specialist
          │         Palo Alto PCNSE, Fortinet NSE 7, Cisco CCNP Security
          │         Target: Enterprises with on-prem NGFW
          │
          ├──▶ Cloud Network Security Engineer
          │         AWS Security Specialty, Azure Network Security
          │         Target: Cloud-first, hybrid organizations
          │
          ├──▶ Network Forensics / NSM Specialist
          │         GNFA (SANS), Security Onion expertise
          │         Target: SOC-adjacent roles, MSSP, incident response teams
          │
          ├──▶ Zero Trust / SASE Architect
          │         Zscaler ZTA, Cloudflare Access, Prisma Access
          │         Target: Large enterprises modernizing away from VPN
          │
          └──▶ Security Architect
                    TOGAF + Security expertise
                    Target: Any large organization
```

---

> **📌 Community Advice:** The biggest mistake in network security learning is rushing to "hacking" tools before understanding what normal traffic looks like. Spend serious time on Wireshark with normal traffic before analyzing attack traffic. You can't spot anomalies if you don't know what normal looks like. *"The best network security engineer I ever worked with could tell within 30 seconds of looking at packet captures whether something was wrong — because they'd spent years knowing what right looks like."* — Senior NSE on Reddit.

> **💡 Tip from practitioners:** Build your home lab and run your own traffic through Security Onion for 30 days before trying to analyze attack traffic. Learning to recognize your own browsing patterns in Zeek logs teaches you faster than any course.

