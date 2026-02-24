# 🌐 NETWORK SECURITY - Complete Guide

## Table of Contents
1. [OSI Model](#osi-model)
2. [TCP/IP Model](#tcpip-model)
3. [Common Protocols](#common-protocols)
4. [Network Security Concepts](#network-security-concepts)
5. [Firewalls](#firewalls)
6. [Network Attacks](#network-attacks)
7. [VPN & Tunneling](#vpn--tunneling)
8. [Interview Questions](#interview-questions)
9. [Learning Resources](#learning-resources)

---

## OSI Model

### What is the OSI Model?

The **OSI (Open Systems Interconnection)** model is a conceptual framework that standardizes how network communication works in **7 layers**.

### The 7 Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                    OSI MODEL (7 LAYERS)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 7 │ APPLICATION    │ HTTP, FTP, SMTP, DNS               │
│          │                │ User-level protocols               │
│  ────────┼────────────────┼───────────────────────────────────  │
│  Layer 6 │ PRESENTATION   │ SSL/TLS, Encryption, JPEG, ASCII   │
│          │                │ Data formatting/encryption         │
│  ────────┼────────────────┼───────────────────────────────────  │
│  Layer 5 │ SESSION        │ NetBIOS, RPC, Sessions             │
│          │                │ Connection management              │
│  ────────┼────────────────┼───────────────────────────────────  │
│  Layer 4 │ TRANSPORT      │ TCP, UDP                           │
│          │                │ End-to-end delivery                │
│  ────────┼────────────────┼───────────────────────────────────  │
│  Layer 3 │ NETWORK        │ IP, ICMP, Routers                  │
│          │                │ Logical addressing, routing        │
│  ────────┼────────────────┼───────────────────────────────────  │
│  Layer 2 │ DATA LINK      │ Ethernet, MAC, Switches            │
│          │                │ Physical addressing                │
│  ────────┼────────────────┼───────────────────────────────────  │
│  Layer 1 │ PHYSICAL       │ Cables, Hubs, Bits                 │
│          │                │ Physical transmission              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Memory Trick

**Top to Bottom:** "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing"
**Bottom to Top:** "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way"

### Layer Details

#### Layer 7 - Application Layer

- **Purpose:** Interface between network and user applications
- **Protocols:** HTTP, HTTPS, FTP, SMTP, DNS, SSH, Telnet
- **Security:** Web Application Firewalls (WAF), Input validation
- **Attacks:** SQL Injection, XSS, Phishing

```
┌─────────────────────────────────────────────────────────────┐
│                 APPLICATION LAYER                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Web Browser ──────► HTTP Request ──────► Web Server        │
│                                                             │
│  Email Client ─────► SMTP ──────────────► Mail Server       │
│                                                             │
│  DNS Client ───────► DNS Query ─────────► DNS Server        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Layer 6 - Presentation Layer

- **Purpose:** Data translation, encryption, compression
- **Functions:**
  - Encryption/Decryption (SSL/TLS)
  - Data compression
  - Character encoding (ASCII, EBCDIC)
  - Serialization (JSON, XML)
- **Security:** TLS/SSL encryption

#### Layer 5 - Session Layer

- **Purpose:** Establish, manage, terminate sessions
- **Functions:**
  - Session establishment
  - Session maintenance
  - Session termination
  - Authentication/Authorization
- **Protocols:** NetBIOS, RPC, PPTP

#### Layer 4 - Transport Layer

- **Purpose:** End-to-end communication, reliability
- **Key Concepts:**

```
┌─────────────────────────────────────────────────────────────┐
│             TCP vs UDP COMPARISON                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│         TCP                           UDP                   │
│  ┌─────────────────┐          ┌─────────────────┐          │
│  │ Connection-     │          │ Connectionless  │          │
│  │ oriented        │          │                 │          │
│  │                 │          │                 │          │
│  │ Reliable        │          │ Unreliable      │          │
│  │ (Acknowledgment)│          │ (No ACK)        │          │
│  │                 │          │                 │          │
│  │ Ordered         │          │ No ordering     │          │
│  │                 │          │                 │          │
│  │ Slower          │          │ Faster          │          │
│  │                 │          │                 │          │
│  │ HTTP, FTP,      │          │ DNS, DHCP,      │          │
│  │ SSH, SMTP       │          │ Streaming, VoIP │          │
│  └─────────────────┘          └─────────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

- **TCP Three-Way Handshake:**

```
CLIENT                                     SERVER
   │                                          │
   │  ────────── SYN ─────────────────────►  │  Step 1: Client initiates
   │                                          │
   │  ◄────────── SYN-ACK ────────────────── │  Step 2: Server acknowledges
   │                                          │
   │  ────────── ACK ─────────────────────►  │  Step 3: Connection established
   │                                          │
   │  ═══════════ DATA ═══════════════════  │  Data transfer begins
   │                                          │
```

#### Layer 3 - Network Layer

- **Purpose:** Logical addressing and routing
- **Key Concepts:**
  - IP Addressing (IPv4, IPv6)
  - Routing (determining path)
  - Packet fragmentation
- **Devices:** Routers, Layer 3 Switches
- **Protocols:** IP, ICMP, ARP, OSPF, BGP
- **Security:** ACLs, IP filtering, IPSec

```
┌─────────────────────────────────────────────────────────────┐
│               IP ADDRESS STRUCTURE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IPv4: 192.168.1.100                                        │
│        └──┬──┘ └─┬─┘                                        │
│       Network  Host                                         │
│                                                             │
│  Subnet Mask: 255.255.255.0 (/24)                           │
│                                                             │
│  Classes:                                                   │
│    Class A: 1.0.0.0   - 126.255.255.255  (Large networks)   │
│    Class B: 128.0.0.0 - 191.255.255.255  (Medium networks)  │
│    Class C: 192.0.0.0 - 223.255.255.255  (Small networks)   │
│                                                             │
│  Private Ranges:                                            │
│    10.0.0.0/8        (Class A)                              │
│    172.16.0.0/12     (Class B)                              │
│    192.168.0.0/16    (Class C)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Layer 2 - Data Link Layer

- **Purpose:** Physical addressing, error detection
- **Key Concepts:**
  - MAC Addresses (48-bit hardware address)
  - Frame formatting
  - Error detection (CRC)
- **Devices:** Switches, Bridges
- **Protocols:** Ethernet, PPP, ARP
- **Attacks:** MAC Spoofing, ARP Poisoning

```
MAC Address: 00:1A:2B:3C:4D:5E
             └─────────┘ └────┘
             Vendor ID   Device ID
```

#### Layer 1 - Physical Layer

- **Purpose:** Physical transmission of raw bits
- **Media:** Cables (Cat5e, Cat6, Fiber), Wireless (Wi-Fi)
- **Devices:** Hubs, Repeaters, Network Interface Cards
- **Concepts:** Voltage levels, frequencies, connectors

### Security at Each Layer

| Layer | Common Attacks | Security Controls |
|-------|----------------|-------------------|
| **7 - Application** | SQL Injection, XSS, Phishing | WAF, Input validation |
| **6 - Presentation** | SSL stripping, weak encryption | Strong TLS, certificate pinning |
| **5 - Session** | Session hijacking | Secure session management |
| **4 - Transport** | SYN flood, port scanning | Firewalls, rate limiting |
| **3 - Network** | IP spoofing, routing attacks | IPSec, ACLs |
| **2 - Data Link** | ARP poisoning, MAC spoofing | Port security, 802.1X |
| **1 - Physical** | Cable tapping, jamming | Physical security, encryption |

---

## TCP/IP Model

### TCP/IP vs OSI

```
┌─────────────────────────────────────────────────────────────┐
│              OSI vs TCP/IP MODEL                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│        OSI Model          │       TCP/IP Model              │
│    ┌─────────────────┐    │    ┌─────────────────┐          │
│    │  Application    │    │    │                 │          │
│    ├─────────────────┤    │    │  Application    │          │
│    │  Presentation   │    │    │                 │          │
│    ├─────────────────┤    │    └─────────────────┘          │
│    │  Session        │    │                                 │
│    ├─────────────────┤    │    ┌─────────────────┐          │
│    │  Transport      │◄───┼───►│  Transport      │          │
│    ├─────────────────┤    │    └─────────────────┘          │
│    │  Network        │◄───┼───►┌─────────────────┐          │
│    ├─────────────────┤    │    │  Internet       │          │
│    │  Data Link      │    │    └─────────────────┘          │
│    ├─────────────────┤    │    ┌─────────────────┐          │
│    │  Physical       │◄───┼───►│  Network Access │          │
│    └─────────────────┘    │    └─────────────────┘          │
│                                                             │
│    7 Layers               │    4 Layers                     │
│    Theoretical            │    Practical                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### TCP/IP Layers Explained

| Layer | Function | Protocols |
|-------|----------|-----------|
| **Application** | User services | HTTP, FTP, DNS, SSH, SMTP |
| **Transport** | End-to-end delivery | TCP, UDP |
| **Internet** | Routing, addressing | IP, ICMP, ARP |
| **Network Access** | Physical transmission | Ethernet, Wi-Fi |

---

## Common Protocols

### Port Numbers Reference

```
┌─────────────────────────────────────────────────────────────┐
│               COMMON PORT NUMBERS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PORT    │ PROTOCOL │ SERVICE                               │
│  ────────┼──────────┼─────────────────────────────────────  │
│  20, 21  │ TCP      │ FTP (Data, Control)                   │
│  22      │ TCP      │ SSH (Secure Shell)                    │
│  23      │ TCP      │ Telnet (Insecure!)                    │
│  25      │ TCP      │ SMTP (Email sending)                  │
│  53      │ TCP/UDP  │ DNS (Domain resolution)               │
│  67, 68  │ UDP      │ DHCP (IP assignment)                  │
│  80      │ TCP      │ HTTP (Web)                            │
│  110     │ TCP      │ POP3 (Email retrieval)                │
│  143     │ TCP      │ IMAP (Email retrieval)                │
│  443     │ TCP      │ HTTPS (Secure Web)                    │
│  445     │ TCP      │ SMB (File sharing)                    │
│  3306    │ TCP      │ MySQL                                 │
│  3389    │ TCP      │ RDP (Remote Desktop)                  │
│  5432    │ TCP      │ PostgreSQL                            │
│  8080    │ TCP      │ HTTP Alternate                        │
│                                                             │
│  Port Ranges:                                               │
│  0-1023     : Well-known (System)                           │
│  1024-49151 : Registered                                    │
│  49152-65535: Dynamic/Private                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### DNS (Domain Name System)

**What it does:** Translates domain names to IP addresses

```
┌─────────────────────────────────────────────────────────────┐
│                    DNS RESOLUTION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User types: www.google.com                                 │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │ Local Cache │────►│ ISP DNS     │────►│ Root DNS    │   │
│  │             │     │ Resolver    │     │ (.)         │   │
│  └─────────────┘     └─────────────┘     └──────┬──────┘   │
│                                                  │          │
│                           ┌──────────────────────┘          │
│                           ▼                                 │
│                    ┌─────────────┐     ┌─────────────┐      │
│                    │ .com TLD    │────►│ google.com  │      │
│                    │ Server      │     │ Auth Server │      │
│                    └─────────────┘     └──────┬──────┘      │
│                                               │             │
│  Returns: 142.250.189.206 ◄───────────────────┘             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**DNS Record Types:**
| Record | Purpose | Example |
|--------|---------|---------|
| **A** | IPv4 address | google.com → 142.250.189.206 |
| **AAAA** | IPv6 address | google.com → 2607:f8b0:... |
| **CNAME** | Alias | www.google.com → google.com |
| **MX** | Mail server | google.com → mail.google.com |
| **TXT** | Text info | SPF, DKIM records |
| **NS** | Name server | google.com NS ns1.google.com |

### DHCP (Dynamic Host Configuration Protocol)

**What it does:** Automatically assigns IP addresses to devices

```
┌─────────────────────────────────────────────────────────────┐
│               DHCP DORA PROCESS                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    CLIENT                              DHCP SERVER          │
│       │                                      │              │
│       │ ──── D (Discover) ────────────────►  │              │
│       │      "Who can give me an IP?"        │              │
│       │                                      │              │
│       │ ◄──── O (Offer) ──────────────────── │              │
│       │      "I can offer you 192.168.1.10"  │              │
│       │                                      │              │
│       │ ──── R (Request) ─────────────────►  │              │
│       │      "I'll take 192.168.1.10"        │              │
│       │                                      │              │
│       │ ◄──── A (Acknowledgment) ─────────── │              │
│       │      "Confirmed! It's yours."        │              │
│       │                                      │              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### ARP (Address Resolution Protocol)

**What it does:** Maps IP addresses to MAC addresses

```
Device needs to communicate with 192.168.1.1
       │
       ▼
ARP Request (Broadcast): "Who has 192.168.1.1?"
       │
       ▼
ARP Reply (Unicast): "I have it! My MAC is 00:11:22:33:44:55"
       │
       ▼
Device stores mapping in ARP cache
```

**Security Issue:** ARP has no authentication → ARP Poisoning attacks possible

### HTTP/HTTPS

```
┌─────────────────────────────────────────────────────────────┐
│               HTTP vs HTTPS                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│           HTTP                        HTTPS                 │
│    ┌─────────────────┐         ┌─────────────────┐         │
│    │  Port 80        │         │  Port 443       │         │
│    │  No encryption  │         │  TLS encrypted  │         │
│    │  Vulnerable to  │         │  Protected from │         │
│    │  eavesdropping  │         │  eavesdropping  │         │
│    │                 │         │                 │         │
│    │   🔓 Insecure   │         │   🔒 Secure     │         │
│    └─────────────────┘         └─────────────────┘         │
│                                                             │
│    HTTP Data Flow:                                          │
│    Browser ──── plain text ──── Server                      │
│                                                             │
│    HTTPS Data Flow:                                         │
│    Browser ──── encrypted ───── Server                      │
│                  (TLS 1.3)                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Network Security Concepts

### Firewalls

```
┌─────────────────────────────────────────────────────────────┐
│                  FIREWALL TYPES                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PACKET FILTERING (Stateless)                            │
│     └── Checks: Source/Dest IP, Port, Protocol              │
│     └── Layer: 3-4                                          │
│     └── Fast but limited context                            │
│                                                             │
│  2. STATEFUL INSPECTION                                      │
│     └── Tracks connection state                             │
│     └── Layer: 3-4                                          │
│     └── More intelligent decisions                          │
│                                                             │
│  3. APPLICATION LAYER (Proxy)                                │
│     └── Inspects application data                           │
│     └── Layer: 7                                            │
│     └── Deep packet inspection                              │
│                                                             │
│  4. NEXT-GEN FIREWALL (NGFW)                                 │
│     └── All above + IPS, Application awareness              │
│     └── Layer: 3-7                                          │
│     └── Modern enterprise solution                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### IDS vs IPS

```
┌─────────────────────────────────────────────────────────────┐
│                  IDS vs IPS                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IDS (Intrusion Detection System)                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Traffic ───► IDS (copies) ───► Alert! 🔔            │   │
│  │         └────────────────────► Continues to target   │   │
│  │                                                      │   │
│  │  PASSIVE: Detects and alerts, does NOT block        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  IPS (Intrusion Prevention System)                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Traffic ───► IPS ───► Blocks malicious ❌           │   │
│  │               └──────► Allows legitimate ✓           │   │
│  │                                                      │   │
│  │  ACTIVE: Detects AND blocks threats                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### DMZ (Demilitarized Zone)

```
┌─────────────────────────────────────────────────────────────┐
│                  DMZ ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   INTERNET                                                  │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────────┐                                           │
│  │ FIREWALL 1  │────────────────────────────────────────┐  │
│  └─────────────┘                                        │  │
│       │                                                 │  │
│       ▼                                                 │  │
│  ┌─────────────────────────────────────────────────┐   │  │
│  │                    DMZ                           │   │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │   │  │
│  │  │Web Server│  │Mail Server│ │DNS Server│       │   │  │
│  │  └──────────┘  └──────────┘  └──────────┘       │   │  │
│  │      Public-facing servers                       │   │  │
│  └─────────────────────────────────────────────────┘   │  │
│       │                                                 │  │
│       ▼                                                 │  │
│  ┌─────────────┐                                       │  │
│  │ FIREWALL 2  │◄──────────────────────────────────────┘  │
│  └─────────────┘                                          │
│       │                                                    │
│       ▼                                                    │
│  ┌─────────────────────────────────────────────────┐      │
│  │              INTERNAL NETWORK                    │      │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │      │
│  │  │Database  │  │Workstations │App Servers│      │      │
│  │  └──────────┘  └──────────┘  └──────────┘       │      │
│  │      Protected internal resources               │      │
│  └─────────────────────────────────────────────────┘      │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Network Attacks

### Common Network Attacks

#### 1. DDoS (Distributed Denial of Service)

```
┌─────────────────────────────────────────────────────────────┐
│                    DDoS ATTACK                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    Bot 1 ─────┐                                             │
│               │                                             │
│    Bot 2 ─────┼──────► Target Server ───► Service Down ❌    │
│               │        (Overwhelmed)                        │
│    Bot N ─────┘                                             │
│    (Thousands)                                               │
│                                                             │
│  Types:                                                     │
│  • Volumetric: Flood bandwidth (UDP flood)                  │
│  • Protocol: Exhaust resources (SYN flood)                  │
│  • Application: Target app layer (HTTP flood)               │
│                                                             │
│  Prevention:                                                │
│  • CDN (Cloudflare, Akamai)                                │
│  • Rate limiting                                           │
│  • Traffic analysis                                        │
│  • Anycast distribution                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### 2. Man-in-the-Middle (MITM)

```
┌─────────────────────────────────────────────────────────────┐
│                    MITM ATTACK                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NORMAL:                                                    │
│  Client ═══════════════════════════════════► Server         │
│                                                             │
│  MITM:                                                      │
│  Client ────► ATTACKER ────► Server                         │
│         ◄────          ◄────                                │
│                  │                                          │
│                  ▼                                          │
│         Intercepts, reads,                                  │
│         modifies data!                                      │
│                                                             │
│  Prevention:                                                │
│  • HTTPS/TLS everywhere                                    │
│  • Certificate pinning                                     │
│  • HSTS (HTTP Strict Transport Security)                   │
│  • VPN for untrusted networks                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### 3. ARP Poisoning/Spoofing

```
┌─────────────────────────────────────────────────────────────┐
│                ARP POISONING ATTACK                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NORMAL ARP:                                                │
│  Victim ──► ARP: Who has Gateway? ──► Gateway responds      │
│                                                             │
│  ARP POISONING:                                             │
│  Attacker sends fake ARP replies:                           │
│  "I'm the gateway!" (to Victim)                            │
│  "I'm the Victim!" (to Gateway)                            │
│                                                             │
│  Result: All traffic flows through Attacker                 │
│                                                             │
│  Prevention:                                                │
│  • Static ARP entries                                      │
│  • Dynamic ARP Inspection (DAI)                            │
│  • VPN for encryption                                      │
│  • 802.1X authentication                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### 4. DNS Poisoning/Spoofing

```
NORMAL: User types bank.com → Gets real IP (142.250.x.x)
ATTACK: User types bank.com → Gets attacker's IP (Evil site!)

Prevention:
• DNSSEC (DNS Security Extensions)
• DNS over HTTPS (DoH)
• Reputable DNS providers
```

#### 5. Port Scanning

```
Attacker scans target to find open services:

nmap -sS 192.168.1.100

PORT    STATE  SERVICE
22/tcp  open   ssh
80/tcp  open   http
443/tcp open   https
3306/tcp open  mysql  ← Security risk!

Prevention:
• Close unnecessary ports
• Firewall rules
• Port knocking
• IDS/IPS monitoring
```

---

## VPN & Tunneling

### VPN Types

```
┌─────────────────────────────────────────────────────────────┐
│                    VPN TYPES                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. REMOTE ACCESS VPN                                        │
│     ┌────────────┐     Encrypted Tunnel      ┌──────────┐  │
│     │Remote User │══════════════════════════►│Corporate │  │
│     │(Home/Mobile)    (Internet)             │Network   │  │
│     └────────────┘                           └──────────┘  │
│                                                             │
│  2. SITE-TO-SITE VPN                                         │
│     ┌──────────┐     Encrypted Tunnel      ┌──────────┐    │
│     │ Office A │══════════════════════════►│ Office B │    │
│     │ Network  │        (Internet)         │ Network  │    │
│     └──────────┘                           └──────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### VPN Protocols

| Protocol | Security | Speed | Use Case |
|----------|----------|-------|----------|
| **OpenVPN** | High | Medium | General purpose |
| **WireGuard** | High | Fast | Modern, lightweight |
| **IPSec** | High | Medium | Enterprise, site-to-site |
| **L2TP/IPSec** | High | Medium | Legacy support |
| **PPTP** | Low ⚠️ | Fast | Avoid (deprecated) |

### IPSec Modes

```
┌─────────────────────────────────────────────────────────────┐
│                  IPSec MODES                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TRANSPORT MODE:                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Original IP Header │ ESP/AH │ Encrypted Payload     │  │
│  └──────────────────────────────────────────────────────┘  │
│  • Encrypts payload only                                   │
│  • Used for host-to-host                                   │
│                                                             │
│  TUNNEL MODE:                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ New IP Header │ ESP/AH │ Original IP + Payload       │  │
│  └──────────────────────────────────────────────────────┘  │
│  • Encrypts entire original packet                         │
│  • Used for VPN gateways                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Interview Questions

### Basic Questions

**Q1: Explain the OSI model and its layers.**
> "The OSI model is a 7-layer conceptual framework for network communication. From bottom to top: Physical (bits), Data Link (frames/MAC), Network (packets/IP), Transport (segments/TCP,UDP), Session (connection management), Presentation (encryption/formatting), Application (user protocols like HTTP). Each layer provides services to the layer above it."

**Q2: What is the difference between TCP and UDP?**
> "TCP is connection-oriented, reliable, and ordered - it uses three-way handshake and acknowledgments, making it suitable for HTTP, FTP, email. UDP is connectionless and unreliable but faster, suitable for DNS, streaming, VoIP where some packet loss is acceptable."

**Q3: What is a firewall and what are its types?**
> "A firewall is a network security device that monitors and controls traffic based on security rules. Types include: Packet filtering (stateless, checks headers), Stateful inspection (tracks connections), Application layer/proxy (deep inspection), and Next-Gen Firewalls (combined with IPS, application awareness)."

### Advanced Questions

**Q4: How would you defend against a DDoS attack?**
> "Defense in depth: Use CDN services like Cloudflare for traffic distribution, implement rate limiting at multiple layers, deploy anycast to distribute traffic globally, use scrubbing services to filter malicious traffic, have ISP-level blackholing as last resort, and maintain incident response plans."

**Q5: Explain ARP poisoning and how to prevent it.**
> "ARP poisoning exploits the lack of authentication in ARP protocol. An attacker sends fake ARP replies, associating their MAC with the gateway IP, redirecting traffic through them. Prevention includes Dynamic ARP Inspection on switches, static ARP entries for critical hosts, 802.1X port authentication, and VPNs for encryption."

---

## Learning Resources

### 📚 Websites

| Website | Link | What You'll Learn |
|---------|------|-------------------|
| **Professor Messer** | https://www.professormesser.com/ | Network+ certification prep |
| **Cisco Networking Academy** | https://www.netacad.com/ | Industry-standard networking |
| **Cybrary** | https://www.cybrary.it/ | Free security courses |
| **NetworkLessons** | https://networklessons.com/ | Deep networking concepts |
| **OWASP** | https://cheatsheetseries.owasp.org/ | Security cheat sheets |

### 🎥 YouTube Videos

| Video | Link | Duration |
|-------|------|----------|
| **OSI Model Explained** | https://www.youtube.com/watch?v=vv4y_uOneC0 | ~15 min |
| **TCP/IP Explained** | https://www.youtube.com/watch?v=2QGgEk20RXM | ~20 min |
| **NetworkChuck - Networking** | https://www.youtube.com/watch?v=S7MNX_UD7vY | ~45 min |
| **Firewalls Explained** | https://www.youtube.com/watch?v=kDEX1HXybrU | ~12 min |
| **Practical Networking** | https://www.youtube.com/c/PracticalNetworking | Full Channel |

### 📖 Courses

| Course | Platform | Link |
|--------|----------|------|
| **CompTIA Network+** | Professor Messer | https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/ |
| **Cisco CCNA** | Cisco NetAcad | https://www.netacad.com/courses/networking |
| **Network Fundamentals** | Coursera | https://www.coursera.org/learn/computer-networking |
| **Practical Networking** | Udemy | https://www.udemy.com/course/complete-networking-fundamentals-course-ccna-start/ |

### 🛠️ Practice Labs

| Lab | Link | Description |
|-----|------|-------------|
| **Packet Tracer** | https://www.netacad.com/courses/packet-tracer | Cisco network simulator |
| **GNS3** | https://www.gns3.com/ | Advanced network simulator |
| **Wireshark** | https://www.wireshark.org/ | Network packet analysis |
| **TryHackMe - Networking** | https://tryhackme.com/room/introtolan | Interactive learning |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│           NETWORK SECURITY QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  OSI LAYERS: Please Do Not Throw Sausage Pizza Away         │
│  (Physical, Data Link, Network, Transport, Session,         │
│   Presentation, Application)                                │
│                                                             │
│  KEY PROTOCOLS:                                             │
│  HTTP: 80 | HTTPS: 443 | SSH: 22 | DNS: 53 | FTP: 21       │
│  SMTP: 25 | RDP: 3389 | MySQL: 3306                        │
│                                                             │
│  TCP vs UDP:                                                │
│  TCP = Reliable, connection-oriented (HTTP, FTP)           │
│  UDP = Fast, connectionless (DNS, streaming)               │
│                                                             │
│  SECURITY DEVICES:                                          │
│  Firewall = Filter traffic by rules                        │
│  IDS = Detect and alert (passive)                          │
│  IPS = Detect and block (active)                           │
│                                                             │
│  COMMON ATTACKS & PREVENTION:                               │
│  DDoS → CDN, rate limiting                                 │
│  MITM → TLS/HTTPS, certificate pinning                     │
│  ARP Poisoning → DAI, static ARP                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Next Topic: [Cryptography](../04_Cryptography/01_Cryptography_Fundamentals.md)*
