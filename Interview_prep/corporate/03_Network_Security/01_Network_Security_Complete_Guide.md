# 🌐 NETWORK SECURITY — CORPORATE COMPLETE GUIDE

> **Audience:** Entry to Mid-level Network Security Engineers, Security Analysts, and Corporate Security professionals  
> **Scope:** Beyond basics — enterprise architecture, advanced protocols, real-world attack analysis, defensive engineering  
> **Last Updated:** 2026

---

## 📋 TABLE OF CONTENTS

1. [Network Security Fundamentals](#1-network-security-fundamentals)
2. [OSI Model — Security at Every Layer](#2-osi-model--security-at-every-layer)
3. [TCP/IP Deep Dive — What Happens Under the Hood](#3-tcpip-deep-dive)
4. [Firewall Architecture & Engineering](#4-firewall-architecture--engineering)
5. [IDS/IPS — Intrusion Detection & Prevention](#5-idsips--intrusion-detection--prevention)
6. [Network Segmentation & DMZ Architecture](#6-network-segmentation--dmz-architecture)
7. [VPN Technologies](#7-vpn-technologies)
8. [DNS Security (DNSSEC, DNS over HTTPS, DNS attacks)](#8-dns-security)
9. [TLS/SSL — Deep Dive](#9-tlsssl--deep-dive)
10. [Network Attack Taxonomy](#10-network-attack-taxonomy)
11. [DDoS — Detection, Mitigation & Enterprise Response](#11-ddos--detection-mitigation--enterprise-response)
12. [Wireless Security](#12-wireless-security)
13. [Network Monitoring & Traffic Analysis](#13-network-monitoring--traffic-analysis)
14. [Zero Trust Networking](#14-zero-trust-networking)
15. [Cloud Networking Security (AWS, Azure)](#15-cloud-networking-security)
16. [Network Security Tools Ecosystem](#16-network-security-tools-ecosystem)
17. [Real-World Case Studies](#17-real-world-case-studies)
18. [Day in the Life of a Network Security Engineer](#18-day-in-the-life-of-a-network-security-engineer)
19. [Network Security in Corporate Environments](#19-network-security-in-corporate-environments)

---

## 1. Network Security Fundamentals

### The CIA Triad Applied to Networks

| CIA Principle | Network Example | Attack Violating It |
|--------------|----------------|---------------------|
| **Confidentiality** | Encrypting traffic (TLS, VPN) | Packet sniffing, MITM |
| **Integrity** | Digital signatures, checksums, TLS MAC | Packet injection, ARP poisoning |
| **Availability** | Redundant links, DDoS mitigation | DDoS, link flooding |

### Defense in Depth — Network Model

```
INTERNET
    │
    ▼
┌──────────────────────────────────────────────────────────────┐
│  EDGE LAYER                                                  │
│  DDoS Scrubbing (Cloudflare/Akamai) → Border Router → ISP   │
└──────────────────────────────────────┬───────────────────────┘
                                       │
┌──────────────────────────────────────▼───────────────────────┐
│  PERIMETER LAYER                                             │
│  External Firewall (NGFW) → WAF → Load Balancer             │
└──────────────────────────────────────┬───────────────────────┘
                                       │
┌──────────────────────────────────────▼───────────────────────┐
│  DMZ (DEMILITARIZED ZONE)                                    │
│  Web Servers │ API Gateways │ Reverse Proxies │ Mail Relays  │
└──────────────────────────────────────┬───────────────────────┘
                                       │
┌──────────────────────────────────────▼───────────────────────┐
│  INTERNAL PERIMETER                                          │
│  Internal Firewall → IDS/IPS → NAC                          │
└──────────────────────────────────────┬───────────────────────┘
                                       │
┌──────────────────────────────────────▼───────────────────────┐
│  INTERNAL NETWORK (SEGMENTED)                                │
│  ├── Corporate LAN (VLANs by department)                     │
│  ├── Server VLAN (data center)                               │
│  ├── OT/SCADA VLAN (isolated)                                │
│  └── Guest VLAN (internet-only)                              │
└──────────────────────────────────────┬───────────────────────┘
                                       │
┌──────────────────────────────────────▼───────────────────────┐
│  ENDPOINT LAYER                                              │
│  EDR │ Host Firewall │ HIDS │ DLP agent                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. OSI Model — Security at Every Layer

### Security Controls at Each Layer

```
LAYER 7 — APPLICATION
  Protocols:   HTTP, HTTPS, DNS, FTP, SMTP, SSH
  Attacks:     SQL Injection, XSS, CSRF, DNS Poisoning, Phishing
  Controls:    WAF, App-layer firewall, Input validation, DNSSEC

LAYER 6 — PRESENTATION
  Protocols:   TLS/SSL, JPEG, ASCII
  Attacks:     SSL stripping, weak cipher exploitation, malformed data
  Controls:    TLS 1.3 enforcement, certificate pinning, cipher hardening

LAYER 5 — SESSION
  Protocols:   NetBIOS, RPC, SSH sessions
  Attacks:     Session hijacking, replay attacks
  Controls:    Session tokens, secure cookies, timeout policies

LAYER 4 — TRANSPORT
  Protocols:   TCP, UDP
  Attacks:     SYN flood, TCP session hijacking, UDP flood
  Controls:    TCP SYN cookies, rate limiting, stateful inspection

LAYER 3 — NETWORK
  Protocols:   IP, ICMP, OSPF, BGP
  Attacks:     IP spoofing, ICMP flood, routing attacks (BGP hijack)
  Controls:    Ingress/egress filtering, uRPF, BGP authentication

LAYER 2 — DATA LINK
  Protocols:   Ethernet, ARP, MAC, 802.1Q (VLAN)
  Attacks:     ARP poisoning, MAC flooding, VLAN hopping
  Controls:    Dynamic ARP Inspection (DAI), port security, 802.1X

LAYER 1 — PHYSICAL
  Hardware:    Cables, NICs, switches, hubs
  Attacks:     Physical tapping, hardware tampering, signal interception
  Controls:    Physical access controls, tamper-evident seals, fiber (harder to tap)
```

### Protocol Data Units (PDUs) by Layer

| Layer | PDU Name | Example |
|-------|---------|---------|
| 7-5 | Data | HTTP request payload |
| 4 | Segment (TCP) / Datagram (UDP) | TCP segment with port numbers |
| 3 | Packet | IP packet with source/dest IP |
| 2 | Frame | Ethernet frame with MAC addresses |
| 1 | Bits | Electrical/optical signals |

---

## 3. TCP/IP Deep Dive

### TCP Three-Way Handshake

```
CLIENT                          SERVER
  │                               │
  │──── SYN (seq=x) ────────────▶│  Step 1: Client initiates
  │                               │
  │◀─── SYN-ACK (seq=y, ack=x+1)─│  Step 2: Server responds
  │                               │
  │──── ACK (ack=y+1) ──────────▶│  Step 3: Connection established
  │                               │
  │═══════ DATA EXCHANGE ═════════│
  │                               │
  │──── FIN ────────────────────▶│  Teardown begins
  │◀─── FIN-ACK ─────────────────│
  │──── ACK ────────────────────▶│  Connection closed
```

**SYN Flood Attack:** Attacker sends massive SYN packets → server allocates half-open connections for each → exhausts connection table → legitimate connections denied.

**Defense:** SYN cookies — server doesn't allocate state until ACK received; the cookie encodes connection parameters.

### TCP Flags (Know All 6)

| Flag | Name | Purpose | Attack Use |
|------|------|---------|-----------|
| **SYN** | Synchronize | Initiate connection | SYN flood |
| **ACK** | Acknowledge | Acknowledge received data | ACK flood |
| **FIN** | Finish | Graceful close | FIN scan (stealthy port scan) |
| **RST** | Reset | Abrupt close | TCP reset injection |
| **PSH** | Push | Send data immediately | N/A directly |
| **URG** | Urgent | Priority data | Rarely used/exploited |

**Nmap scan types using flags:**
- `-sS` (SYN/stealth scan): Send SYN → SYN-ACK = open, RST = closed, no response = filtered
- `-sF` (FIN scan): Send FIN → RST = closed (no response on filtered or open per RFC)
- `-sN` (NULL scan): No flags → avoids some IDS signatures

### TCP vs UDP Comparison

| | TCP | UDP |
|-|-----|-----|
| **Connection** | Connection-oriented (3-way handshake) | Connectionless |
| **Reliability** | Guaranteed delivery, ordered | No guarantees |
| **Speed** | Slower (overhead) | Faster |
| **Use cases** | HTTP, SSH, FTP, SMTP | DNS, VoIP, streaming, DHCP |
| **Attack surface** | SYN flood, session hijack | UDP flood, DNS amplification |
| **Header size** | 20 bytes min | 8 bytes |

### IP Header — Key Fields for Security

```
IP HEADER (20 bytes minimum):
┌─────────┬──────────────┬──────────────────────────┐
│ Version │ IHL │ DSCP   │     Total Length          │
├─────────┴──────────────┼───────────┬───────────────┤
│     Identification     │  Flags    │ Fragment Offset│
├────────────────────────┼───────────┴───────────────┤
│  TTL    │  Protocol    │     Header Checksum        │
├─────────┴──────────────┴───────────────────────────┤
│                  Source IP Address                  │
├─────────────────────────────────────────────────────┤
│               Destination IP Address                │
└─────────────────────────────────────────────────────┘

SECURITY-RELEVANT FIELDS:
- TTL: Decremented by 1 per hop. Reaches 0 → packet dropped.
  Attack: TTL manipulation to bypass IDS
- Protocol: 6=TCP, 17=UDP, 1=ICMP
  Attack: ICMP tunneling (covert channel)
- Source IP: Spoofable (no validation in base IP)
  Attack: IP spoofing, DDoS amplification
- Flags: Don't Fragment (DF), More Fragments (MF)
  Attack: Fragmentation attacks to bypass IDS
```

---

## 4. Firewall Architecture & Engineering

### Firewall Types — Detailed

#### Packet Filtering Firewall (Layer 3-4)
```
Decision based on: Source IP, Dest IP, Protocol, Port
Stateless — each packet evaluated independently
Fast, low overhead
Example rule:
  PERMIT TCP 0.0.0.0/0 → 10.0.0.5 port 443
  DENY ALL

Weakness: Cannot distinguish between packets of established sessions
          Cannot inspect application payload
```

#### Stateful Inspection Firewall (Layer 3-4 + State)
```
Tracks connection state in state table:
  SYN → half-open state recorded
  SYN-ACK + ACK → full connection recorded
  FIN → connection removed

Allows: "Permit established connections returning inbound"
  without explicit rule for return traffic

Weakness: Still cannot inspect application payload
```

#### Application Layer / Proxy Firewall (Layer 7)
```
Acts as proxy — terminates connection, inspects payload, re-originates
Sees: Full HTTP requests, FTP commands, DNS queries
Can detect: SQL injection in URLs, malicious HTTP headers, protocol violations
Slower than packet filtering but much more visibility

Example: Web proxy inspects HTTPS after SSL inspection
```

#### NGFW — Next-Generation Firewall (Most Common in Enterprise)
```
Combines ALL of above PLUS:
├── Application Identification (not just port — identify Netflix traffic on 443)
├── User Identity (who, not just what IP)
├── SSL/TLS Inspection (decrypt, inspect, re-encrypt)
├── IPS (signature + behavioral detection)
├── Threat Intelligence integration (block known malicious IPs/domains)
├── URL Filtering (categories: social media, gambling, malware)
├── File Inspection (extract and sandbox files from traffic)
└── DNS Security

Vendors: Palo Alto Networks, Fortinet, Check Point, Cisco Firepower
```

### Firewall Rule Design Principles

```
GOLDEN RULE: Default Deny All — only permit what's explicitly needed

RULE ORDER MATTERS (evaluated top to bottom, first match wins):
  Rule 1: DENY known bad IPs (threat intel blocklist)
  Rule 2: PERMIT required external services (DNS, NTP)
  Rule 3: PERMIT specific application traffic (HTTPS to web servers)
  Rule 4: DENY ALL (implicit or explicit)

FIREWALL RULE ELEMENTS:
┌──────┬────────────┬──────────────┬──────────────┬──────────┬────────┐
│ Rule │  Source    │ Destination  │   Service    │ Action   │  Log   │
├──────┼────────────┼──────────────┼──────────────┼──────────┼────────┤
│  1   │ Any        │ Blacklist IPs│  Any         │ DENY     │  YES   │
│  2   │ Corp LAN   │ Any          │ HTTPS (443)  │ PERMIT   │  NO    │
│  3   │ Any        │ DMZ Web      │ HTTP/HTTPS   │ PERMIT   │  YES   │
│  4   │ Any        │ Any          │  Any         │ DENY     │  YES   │
└──────┴────────────┴──────────────┴──────────────┴──────────┴────────┘

BEST PRACTICES:
- Least privilege: Only open what's needed
- Log denied traffic (for detection)
- Log permitted traffic for critical zones
- Rule review every 6 months — remove stale rules
- Document every rule with a change ticket reference
```

### SSL/TLS Inspection (Deep Dive)

```
WHY SSL INSPECTION?
  Problem: 70%+ of malware uses HTTPS for C2 to evade detection
  Solution: NGFW decrypts → inspects → re-encrypts

HOW IT WORKS:
User → [NGFW decrypts TLS] → NGFW inspects payload → [NGFW re-encrypts] → Server
         ↑                                                    ↑
    Uses its own cert signed by internal CA      New TLS session to server

REQUIREMENTS:
  - Internal CA certificate pushed to all endpoints (trusted)
  - Policy to exclude: banking sites, healthcare, where cert pinning used
  - Compliance consideration: HR data, legal comms may have privacy requirements

RISKS:
  - Certificate errors if CA not pushed to all devices
  - Privacy concerns (can see employee personal traffic if unrestricted)
  - Certificate pinning apps will break (must be excluded)
```

---

## 5. IDS/IPS — Intrusion Detection & Prevention

### Detection Methods

| Method | How | Pros | Cons |
|--------|-----|------|------|
| **Signature-based** | Match traffic against known attack patterns | Low FP for known attacks | Blind to zero-days, evasion possible |
| **Anomaly-based** | Deviate from baseline behavior | Detects unknown attacks | High FP, requires learning period |
| **Heuristic** | Rule-based logic for suspicious patterns | Balance between above | Still requires maintenance |
| **Protocol analysis** | Validate protocol conformance | Catches protocol violations | Complex to implement |

### IDS/IPS Placement

```
DEPLOYMENT OPTIONS:

1. NETWORK-BASED (NIDS/NIPS):
   ┌──────────┐         ┌──────────┐
   │  Router  │────┬────│  Switch  │────Internal
   └──────────┘   │    └──────────┘
                  │
              ┌───▼──────┐
              │  IDS     │ (Span port — passive copy)
              │  Sensor  │ (IPS inline — between router and switch)
              └──────────┘

2. HOST-BASED (HIDS):
   Installed on each endpoint
   Examples: OSSEC, Wazuh, Tripwire
   Monitors: File integrity, log files, registry, running processes

3. INLINE (IPS):
   Traffic MUST pass through → can block
   Risk: Single point of failure → bypass mode if IPS fails
   
4. OUT-OF-BAND (IDS):
   Receives copy via SPAN/TAP → cannot block, only alert
   No impact on traffic flow
   Risk: Cannot stop attack in progress
```

### Snort & Suricata — Rule Writing

**Snort/Suricata Rule Structure:**
```
action  protocol  src_ip  src_port  direction  dst_ip  dst_port  (options)

EXAMPLES:

# Detect SSH brute force
alert tcp any any -> $HOME_NET 22 (msg:"Potential SSH Brute Force";
  threshold:type threshold, track by_src, count 10, seconds 60;
  classtype:attempted-admin; sid:1000001;)

# Detect SQL injection attempt
alert http any any -> $HTTP_SERVERS any (msg:"SQL Injection Attempt";
  content:"UNION SELECT"; nocase; http_uri;
  classtype:web-application-attack; sid:1000002;)

# Detect Mimikatz via user-agent
alert http $HOME_NET any -> any any (msg:"Mimikatz User Agent";
  content:"mimikatz"; nocase; http_header;
  classtype:trojan-activity; sid:1000003;)

# Detect DNS tunneling (unusually long DNS queries)
alert dns any any -> any 53 (msg:"Possible DNS Tunneling - Long Query";
  dns_query; content:!".microsoft.com"; isdataat:100;
  classtype:bad-unknown; sid:1000004;)
```

---

## 6. Network Segmentation & DMZ Architecture

### Why Segmentation Matters

**Without segmentation:**
```
Attacker compromises one workstation
→ Has direct access to ALL servers, ALL databases, ALL workstations
→ Lateral movement is trivially easy
→ Ransomware spreads everywhere instantly
```

**With segmentation:**
```
Attacker compromises one workstation in Finance VLAN
→ Cannot directly reach HR VLAN (ACLs block)
→ Cannot reach Production Servers (firewall between user and server VLANs)
→ Cannot reach OT/SCADA (air-gapped or heavily restricted)
→ Blast radius contained
```

### VLAN Design — Enterprise Standard

```
VLAN ARCHITECTURE:

VLAN 10 — Management (OOB)
  → Network devices, server management ports
  → Strictly restricted — only from admin workstations

VLAN 20 — Servers (Production)
  → Application servers, database servers
  → Only permits required application ports

VLAN 30 — User LAN (Corporate)
  → Employee workstations
  → Internet access, specific internal servers

VLAN 40 — DMZ
  → Web servers, mail relays, API gateways
  → Internet-facing, restricted internal access

VLAN 50 — Development
  → Dev/test environments
  → Isolated from production

VLAN 60 — Guest
  → Internet only, no internal access
  → Isolated from all internal VLANs

VLAN 70 — OT/SCADA
  → Operational technology, industrial systems
  → Heavily restricted or air-gapped
  → No direct internet access ever

VLAN 80 — Security
  → SOC tools, SIEM, vulnerability scanners
  → Read-only access to all other VLANs for monitoring
```

### DMZ Architecture — Three-Zone Model

```
INTERNET
    │
    ▼
┌─────────────────┐
│  External       │  ← BGP/routing to ISP
│  Router         │  ← BGP, prefix filtering
└────────┬────────┘
         │
┌────────▼────────┐
│  External NGFW  │  ← First line — drops everything not explicitly permitted
│  (Palo Alto/    │  ← Threat intelligence feeds
│   Fortinet)     │  ← Geo-blocking
└────────┬────────┘
         │
┌────────▼────────────────────────────────────────────┐
│                  DMZ ZONE                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │  Web Server │  │ Mail Relay  │  │ API Gateway │ │
│  │  (Nginx)    │  │ (Postfix)   │  │             │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
└────────────────────────────────┬────────────────────┘
                                 │
                    ┌────────────▼────────┐
                    │  Internal NGFW      │  ← Only specific DMZ→Internal traffic
                    │                    │  ← Logs everything
                    └────────────┬────────┘
                                 │
                    ┌────────────▼────────────────────┐
                    │      INTERNAL NETWORK           │
                    │  App Servers │ DB Servers │ Users│
                    └─────────────────────────────────┘

KEY PRINCIPLE: DMZ servers should NEVER initiate connections to internal network.
              Internal servers initiate connections TO DMZ (pull model) if needed.
```

### Micro-Segmentation (Modern Approach)

Traditional segmentation works at VLAN/subnet level. Micro-segmentation enforces policy at the workload/VM level:

```
Traditional: "Finance VLAN can talk to DB VLAN"
Micro-seg:   "Only Finance-App-01 can reach DB-Finance on port 1433,
              from 9 AM to 6 PM, using this specific service account"
```

**Tools:** VMware NSX, Illumio, Guardicore (Akamai), Cisco ACI

---

## 7. VPN Technologies

### VPN Types Comparison

| Type | Protocol | Use Case | Pros | Cons |
|------|----------|---------|------|------|
| **IPsec Site-to-Site** | IKEv2/IPsec | Branch office to HQ | High performance, hardware accelerated | Complex config |
| **Remote Access VPN** | SSL/TLS or IPsec | Employee remote work | Flexible, works through NAT | Performance overhead |
| **SSL VPN** | TLS | Browser-based access | No client needed, works everywhere | Limited capabilities |
| **WireGuard** | Modern UDP | Fast remote access | Extremely fast, simple, modern crypto | Newer, less enterprise support |
| **OpenVPN** | TLS | Open-source | Cross-platform, flexible | Slower than WireGuard |
| **MPLS VPN** | ISP-level | Enterprise WAN | Guaranteed QoS, no internet traversal | Expensive, ISP-dependent |

### IPsec — How it Works

```
IPSEC PHASES:

PHASE 1 (IKE — Internet Key Exchange):
  - Authenticate peers (certificates or pre-shared key)
  - Negotiate IKE SA (Security Association) parameters
  - Establish secure channel for Phase 2 negotiation
  - IKEv1: Main mode (6 messages) or Aggressive mode (3 messages — less secure)
  - IKEv2: Simplified, always 4 messages, more secure

PHASE 2 (IPsec SA):
  - Negotiate IPsec parameters (encryption, hashing, lifetime)
  - Establish IPsec tunnel for actual data

IPSEC MODES:
  Transport mode:  Encrypts payload only — IP header intact
                   Used for host-to-host (end-to-end)
  
  Tunnel mode:     Encrypts entire original IP packet + new outer header
                   Used for site-to-site VPN (network-to-network)

IPSEC PROTOCOLS:
  AH (Authentication Header):    Integrity + authentication, NO encryption
  ESP (Encapsulating Security Payload): Encryption + integrity + authentication
  → Always use ESP in corporate environments (AH doesn't encrypt)
```

### Split Tunneling — Security Risk

```
SPLIT TUNNELING:
  Corporate traffic → goes through VPN (encrypted, protected)
  Internet traffic  → goes directly to internet (bypasses corporate controls)

SECURITY RISK:
  User connects from home WiFi → internet traffic not inspected
  If user visits malicious site on personal traffic:
  → Malware downloads to laptop
  → Malware is now ON the corporate device, inside the VPN tunnel
  → Lateral movement possible

RECOMMENDATION: Disable split tunneling for corporate devices
                Or route all traffic through VPN with internet breakout at corporate edge
                (security controls apply to all traffic)
```

---

## 8. DNS Security

### DNS — How It Works

```
USER TYPES: www.google.com

1. Browser checks local cache
2. OS checks /etc/hosts (Windows: C:\Windows\System32\drivers\etc\hosts)
3. OS queries configured DNS resolver (ISP DNS, 8.8.8.8, etc.)
4. DNS Resolver checks its cache
5. If not cached → Recursive resolution:
   Resolver → Root Nameservers → TLD (.com) → Authoritative NS for google.com → Answer
6. Response returned to user + cached with TTL
```

### DNS Attack Types

| Attack | Description | Detection | Defense |
|--------|-------------|-----------|---------|
| **DNS Cache Poisoning** | Inject false records into resolver cache | Unusual NXDOMAIN spikes, record mismatch | DNSSEC, source port randomization |
| **DNS Hijacking** | Modify DNS records at registrar or resolver | Monitor DNS records for unauthorized changes | Registry lock, DNSSEC |
| **DNS Tunneling** | Encode data in DNS queries (C2 channel) | Long subdomain queries, high query volume | DNS analytics, UEBA on DNS |
| **DNS Amplification (DDoS)** | Send small queries, amplify large responses to victim | Traffic spike from many sources | BCP38, response rate limiting |
| **NXDOMAIN Attack** | Flood resolver with non-existent domain queries | High NXDOMAIN error rate | Rate limiting, NXDOMAIN caching |
| **Fast Flux** | Rapidly rotate IP addresses for C2 domain | Short TTL values, many IPs per domain | Threat intel, passive DNS analysis |
| **Domain Generation Algorithms (DGA)** | Malware generates thousands of random domains | Pattern detection, entropy analysis | ML-based DNS analytics |

### DNS Tunneling Detection (Critical for SOC)

```
NORMAL DNS:
  Query: google.com → short, dictionary-word-based
  Frequency: Normal user patterns

DNS TUNNELING (C2 communication):
  Query: aGVsbG8gd29ybGQ.maliciousdomain.com
         (base64 encoded data as subdomain)
  
DETECTION SIGNALS:
  1. Unusually long subdomain labels (>50 chars)
  2. High query rate for same domain with different subdomains
  3. Unusual characters in queries (base64: A-Z, a-z, 0-9, +, /, =)
  4. Large response sizes for TXT records
  5. Consistent beacon timing (regular intervals)

SPLUNK QUERY:
  index=dns
  | eval sub_len=len(query)
  | where sub_len > 50
  | stats count by query, src_ip
  | sort -count
```

### DNSSEC

**DNS Security Extensions** — adds cryptographic signatures to DNS records so resolvers can verify authenticity.

```
WITHOUT DNSSEC:
  Attacker can spoof DNS response → user goes to fake site

WITH DNSSEC:
  Each DNS record signed with zone's private key
  Resolver validates signature using public key
  Tampered record → validation fails → query rejected

CHAIN OF TRUST:
  Root zone (signed) → .com zone (signed) → google.com (signed)
  
DNSSEC doesn't encrypt DNS — it validates authenticity.
For privacy (hide queries): Use DNS over HTTPS (DoH) or DNS over TLS (DoT)
```

---

## 9. TLS/SSL — Deep Dive

### TLS Handshake (TLS 1.3 — Modern)

```
CLIENT                                          SERVER
  │                                               │
  │──── ClientHello ────────────────────────────▶│
  │     (supported ciphers, TLS version,          │
  │      client random, session ID)               │
  │                                               │
  │◀─── ServerHello ─────────────────────────────│
  │     (chosen cipher, server random,            │
  │      server certificate, server key share)    │
  │                                               │
  │  [Client verifies certificate:                │
  │   - Valid signature from trusted CA?          │
  │   - Not expired?                              │
  │   - Domain matches? (CN / SAN)                │
  │   - Not revoked? (OCSP / CRL)]                │
  │                                               │
  │──── ClientKeyExchange ──────────────────────▶│
  │     (pre-master secret encrypted with         │
  │      server's public key)                     │
  │                                               │
  │  Both derive session keys from:               │
  │  pre-master secret + client random + server   │
  │  random → symmetric session key               │
  │                                               │
  │──── Finished (encrypted) ───────────────────▶│
  │◀─── Finished (encrypted) ────────────────────│
  │                                               │
  │══════════ Encrypted Application Data ════════│
```

### TLS Versions — What's Acceptable

| Version | Status | Notes |
|---------|--------|-------|
| SSL 2.0/3.0 | **NEVER USE** | Completely broken (POODLE, etc.) |
| TLS 1.0 | **Deprecated** | BEAST attack, should be disabled |
| TLS 1.1 | **Deprecated** | Disabled by most browsers |
| **TLS 1.2** | **Acceptable** | Still widely supported, secure with proper cipher config |
| **TLS 1.3** | **Recommended** | Forward secrecy always, faster, removes weak ciphers |

### Cipher Suite — Reading It

```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS:        Protocol (TLS)
ECDHE:      Key exchange (Elliptic Curve Diffie-Hellman Ephemeral)
RSA:        Authentication (RSA certificate used to sign ECDHE parameters)
AES_256:    Bulk encryption (AES with 256-bit key)
GCM:        Mode (Galois/Counter Mode — authenticated encryption)
SHA384:     MAC algorithm (message authentication)

GOOD CIPHER INDICATORS:
  - ECDHE or DHE (provides Perfect Forward Secrecy)
  - AES-128 or AES-256
  - GCM mode (preferred over CBC)
  - SHA256 or SHA384

BAD CIPHER INDICATORS:
  - NULL (no encryption)
  - RC4 (broken stream cipher)
  - DES/3DES (64-bit block — SWEET32 attack)
  - MD5 or SHA1 (weak hash)
  - RSA key exchange (no forward secrecy)
  - EXPORT (deliberately weakened — FREAK/Logjam)
```

### Certificate Attacks & Defenses

| Attack | Description | Defense |
|--------|-------------|---------|
| **MITM via rogue cert** | Attacker gets cert for your domain from rogue CA | Certificate Transparency logs, CAA records |
| **SSL Stripping** | Downgrade HTTPS to HTTP | HSTS (HTTP Strict Transport Security) |
| **Certificate Spoofing** | Valid cert for lookalike domain (paypa1.com) | User training, EV certificates |
| **BEAST** | Block cipher attack on TLS 1.0 | Use TLS 1.2+ |
| **POODLE** | SSL 3.0 padding oracle | Disable SSL 3.0 |
| **CRIME/BREACH** | Exploit TLS compression | Disable TLS compression |
| **Heartbleed** | OpenSSL buffer over-read leaks private keys | Patch OpenSSL, rotate certs + keys |

**Certificate Transparency (CT):** All publicly trusted CAs must log certificates to public CT logs. Allows detection of unauthorized certificates issued for your domain.

**CAA Records (DNS):** Specify which CAs are authorized to issue certificates for your domain.
```
acme.com CAA 0 issue "letsencrypt.org"
acme.com CAA 0 issuewild ";"    ← no wildcard certs allowed
```

---

## 10. Network Attack Taxonomy

### Passive Attacks (Eavesdropping)

| Attack | Description | Detection | Defense |
|--------|-------------|-----------|---------|
| **Packet Sniffing** | Capture network traffic in promiscuous mode | Detect promiscuous mode NICs, encryption anomalies | Encryption (TLS), switch-based segmentation |
| **Traffic Analysis** | Analyze patterns even if encrypted | Hard to detect | Traffic padding, onion routing (Tor) |
| **Port Scanning** | Probe open ports to map attack surface | IDS signatures for scan patterns | Firewall rules, port knocking |

### Active Attacks

| Attack | Description | Detection | Defense |
|--------|-------------|-----------|---------|
| **ARP Poisoning** | Send fake ARP replies to redirect traffic | ARP inspection alerts, duplicate MACs | Dynamic ARP Inspection (DAI), static ARP, encryption |
| **MITM** | Intercept communications | Certificate errors, unusual network nodes | Encryption, certificate pinning, MFA |
| **IP Spoofing** | Forge source IP address | Ingress filtering alerts | uRPF (Unicast Reverse Path Forwarding), BCP38 |
| **Session Hijacking** | Steal session token | Anomalous session reuse from different IP | Secure session management, HTTPS, token binding |
| **DNS Poisoning** | Inject false DNS records | DNS monitoring, DNSSEC validation failures | DNSSEC, secure DNS resolvers |
| **BGP Hijacking** | Advertise false routes to redirect internet traffic | Route monitoring (BGPmon) | RPKI, BGP authentication |

### Reconnaissance Techniques (What Attackers Do First)

```
PASSIVE RECON (no direct target contact):
├── WHOIS lookup (registrant info, DNS servers)
├── DNS enumeration (subdomains, MX records, SPF)
├── Google dorking (find exposed files, login pages)
├── LinkedIn/social media (employee names, tech stack)
├── Shodan/Censys (exposed services, banners)
├── Certificate Transparency (subdomains via certs)
└── Job postings (reveal tech stack, security tools)

ACTIVE RECON (direct target contact — detectable):
├── Port scanning (nmap -sS, -sV for version detection)
├── Service version enumeration (banner grabbing)
├── SNMP enumeration (v1/v2 community strings)
├── SMTP enumeration (VRFY, EXPN commands)
├── Web application fingerprinting
└── Network topology mapping (traceroute, TTL analysis)
```

---

## 11. DDoS — Detection, Mitigation & Enterprise Response

### DDoS Attack Types

```
VOLUMETRIC ATTACKS (Flood bandwidth):
├── UDP Flood (random port flooding)
├── ICMP Flood (ping flood)
├── DNS Amplification (send small DNS queries, amplify large responses)
│     Amplification factor: up to 4500x
│     Attack: Spoof victim's IP in DNS query → massive response to victim
├── NTP Amplification (up to 556x)
└── Memcached Amplification (up to 50,000x!)

PROTOCOL ATTACKS (Exhaust state/resources):
├── SYN Flood (exhaust TCP state table)
├── Smurf Attack (ICMP to broadcast address with spoofed source)
├── Ping of Death (malformed oversized ICMP packet)
└── Teardrop (malformed fragmented IP packets)

APPLICATION LAYER ATTACKS (Layer 7 — hardest to mitigate):
├── HTTP GET/POST Flood (millions of legitimate-looking requests)
├── Slowloris (open many connections, send headers slowly)
│     → Exhausts web server connection pool
│     → 1 attacker machine can take down a server
├── SSL Exhaustion (expensive TLS handshakes)
└── DNS Application Flood (overwhelm authoritative DNS)
```

### DDoS Mitigation Architecture

```
LAYERED MITIGATION:

LAYER 1 — UPSTREAM (ISP/Cloud):
  Cloudflare, Akamai, AWS Shield Advanced
  → Absorb volumetric attacks (10+ Tbps capacity)
  → Anycast routing → nearest PoP handles traffic
  → BGP blackholing for extreme events

LAYER 2 — NETWORK EDGE:
  Rate limiting at border router
  BCP38 — filter spoofed source IPs
  ACLs to block known attack sources
  S/RTBH (Selective/Remote Triggered Black Hole)

LAYER 3 — APPLICATION (WAF + CDN):
  WAF challenges suspicious clients (CAPTCHA, JS challenge)
  CDN absorbs GET floods by serving cached content
  Rate limiting per IP, per session, per endpoint
  Geo-blocking if attack from specific regions

LAYER 4 — SERVER:
  SYN cookies for SYN floods
  Connection rate limiting
  Timeout tuning (close idle connections faster)
```

### Enterprise DDoS Response Playbook

```
ALERT: DDoS in progress

MINUTE 0-5:
  ├── Confirm it's a DDoS (not a bug or traffic spike)
  ├── Identify attack type (volumetric? L7? protocol?)
  ├── Activate DDoS response bridge (NOC + SOC + Network team)
  └── Check if upstream scrubbing already engaged (Cloudflare/Akamai auto-detects)

MINUTE 5-15:
  ├── If volumetric: Contact ISP to enable upstream filtering / blackholing
  ├── If L7: Engage WAF team — implement rate limiting, geo-block origin country
  ├── Enable aggressive mitigation mode on edge devices
  └── Status update to management and stakeholders

MINUTE 15-60:
  ├── Fine-tune mitigation (avoid over-blocking legitimate users)
  ├── Monitor: Is attack decreasing? Shifting vectors?
  ├── Preserve evidence (NetFlow, PCAP samples) for post-incident
  └── Regular stakeholder updates (every 15 min)

HOUR 1+:
  ├── Maintain mitigation — attacks can last hours or days
  ├── Identify target IP(s) — consider IP rotation for critical services
  └── Post-incident: Origin analysis, attribution attempt
```

---

## 12. Wireless Security

### Wireless Security Protocols

| Protocol | Year | Encryption | Status | Weakness |
|----------|------|-----------|--------|---------|
| **WEP** | 1997 | RC4 (40-bit) | BROKEN — NEVER USE | IV reuse, crackable in minutes |
| **WPA** | 2003 | TKIP/RC4 | Deprecated | TKIP weak, dictionary attacks |
| **WPA2-Personal** | 2004 | AES-CCMP | Acceptable | PMKID attack, weak passwords crackable |
| **WPA2-Enterprise** | 2004 | AES-CCMP + 802.1X | Recommended | Secure if cert validation enforced |
| **WPA3-Personal** | 2018 | AES + SAE | Best for personal | Dragonblood (patched) |
| **WPA3-Enterprise** | 2018 | 192-bit security | Best for enterprise | Newer, limited device support |

### Enterprise Wireless Security (802.1X)

```
CORPORATE WiFi AUTHENTICATION (WPA2/WPA3-Enterprise):

Device connects to SSID
        │
        ▼
Authenticator (Wireless Controller/AP)
        │
        ▼
RADIUS Server (FreeRADIUS, Cisco ISE, Microsoft NPS)
        │
        ▼
RADIUS checks: Is certificate valid? Is user in AD? Device compliant?
        │
  YES → ▼   NO → DENY access
Access granted + VLAN assigned based on user/device type

COMPONENTS:
  Supplicant: Client device
  Authenticator: Access Point / Wireless Controller
  Authentication Server: RADIUS (RADIUS auth against AD/LDAP)
  EAP Methods:
    EAP-TLS:     Certificate-based (most secure — requires client cert)
    PEAP-MSCHAPv2: Username/password inside TLS tunnel (most common)
    EAP-TTLS:    More flexible inner methods
```

### Wireless Attacks

| Attack | Description | Defense |
|--------|-------------|---------|
| **Evil Twin / Rogue AP** | Set up fake AP with same SSID as corporate | 802.1X (certificate validates real network), WIDS |
| **Deauthentication Attack** | Send forged deauth frames → disconnect clients | 802.11w (Management Frame Protection) |
| **PMKID Attack** | Capture PMKID without full handshake, crack offline | Strong WPA2 passphrase or WPA3 |
| **KRACK** | Key Reinstallation Attack on WPA2 | Patched — keep firmware updated |
| **WPS PIN Attack** | Brute force WPS 8-digit PIN (only 11,000 combinations) | Disable WPS |
| **Karma Attack** | Respond to all probe requests → MITM | Disable probing for old networks on devices |

---

## 13. Network Monitoring & Traffic Analysis

### NetFlow / IPFIX

NetFlow captures traffic metadata (not full packets) — who talked to whom, when, how much.

```
NETFLOW RECORD CONTAINS:
  Source IP, Destination IP
  Source Port, Destination Port
  Protocol (TCP/UDP/ICMP)
  Bytes transferred
  Packets count
  Start time, End time
  Interface (in/out)
  TCP flags

WHAT IT CAN DETECT:
  ├── Port scans (one IP → many IPs on many ports in short time)
  ├── Data exfiltration (large upload to unusual external IP)
  ├── C2 beaconing (regular small connections to external IP)
  ├── Lateral movement (unusual internal-to-internal connections)
  └── DDoS (massive traffic from many sources to one target)

WHAT IT CANNOT DETECT:
  └── Payload content (for that: full PCAP or IDS)
```

### Wireshark — Key Analysis Skills

```
WIRESHARK DISPLAY FILTERS:

# Filter by protocol
http
tls
dns
tcp

# Filter by IP
ip.addr == 192.168.1.100
ip.src == 192.168.1.100
ip.dst == 8.8.8.8

# Filter by port
tcp.port == 443
tcp.dstport == 22

# Combination
ip.addr == 10.0.0.1 && tcp.port == 80

# Find failed connections (RST)
tcp.flags.reset == 1

# Find large transfers
tcp.len > 1000

# DNS queries only
dns.flags.response == 0

# HTTP POST requests
http.request.method == "POST"

# Look for cleartext credentials
http contains "password"

WIRESHARK FOLLOW TCP STREAM:
  Right-click packet → Follow → TCP Stream
  → See full conversation in human-readable form

STATISTICS → Conversations:
  → See all unique IP pairs and data volumes
  → Quick way to spot unusual high-volume transfers
```

### Zeek (Bro) — Network Security Monitoring

Zeek extracts metadata from traffic into structured logs:

```
ZEEK LOG FILES:
  conn.log     → Every connection (src/dst IP, port, bytes, duration)
  dns.log      → DNS queries and responses
  http.log     → HTTP transactions (URI, host, user-agent, status)
  ssl.log      → TLS connections (cert info, version, cipher)
  files.log    → Files extracted from network traffic
  weird.log    → Protocol violations and unusual activity

HUNTING WITH ZEEK:
  # Find long-running connections (potential C2 beaconing)
  cat conn.log | zeek-cut src_ip dst_ip duration | sort -k3 -n | tail -20

  # Find DNS queries with long names (potential tunneling)
  cat dns.log | zeek-cut query | awk '{print length, $0}' | sort -n | tail -20

  # Find unusual user-agents
  cat http.log | zeek-cut user_agent | sort | uniq -c | sort -n
```

---

## 14. Zero Trust Networking

### From Perimeter to Zero Trust

```
PERIMETER (CASTLE-AND-MOAT):
  Inside network = Trusted
  Outside network = Untrusted
  Controls at the boundary only

  Problem: Once attacker is inside (phishing, insider), free movement

ZERO TRUST:
  "Never trust, always verify"
  Every request verified regardless of origin
  Micro-segmentation between all workloads
  Identity is verified, not location

ZERO TRUST PRINCIPLES (NIST SP 800-207):
  1. All data sources and computing services are resources
  2. All communication is secured regardless of network location
  3. Access to resources is granted on per-session basis
  4. Access to resources is determined by dynamic policy
  5. Enterprise monitors and measures integrity of assets
  6. Authentication and authorization is dynamic and strictly enforced
  7. Collect as much information as possible to improve posture
```

### Software-Defined Perimeter (SDP)

```
TRADITIONAL VPN:
  Connect to VPN → access to entire network segment

SDP / ZERO TRUST NETWORK ACCESS (ZTNA):
  User authenticates (identity + device posture)
  → Gets access to ONLY specific application, not the network
  → Cannot see other resources even if on same "VPN"
  → Application-level access, not network-level

ZTNA WORKFLOW:
  User → ZTNA Client → ZTNA Controller (verify identity + device)
       → Controller authorizes → creates encrypted tunnel to specific app
       → User accesses only that app — nothing else

TOOLS:
  Zscaler Private Access (ZPA)
  Palo Alto Prisma Access
  Cloudflare Access
  Tailscale (modern WireGuard-based)
```

---

## 15. Cloud Networking Security

### AWS VPC Security

```
AWS NETWORK SECURITY LAYERS:

SECURITY GROUPS (Stateful):
  Instance-level firewall
  Allow rules only (deny is implicit)
  Stateful: if you allow outbound, inbound response auto-allowed
  Example: Allow port 443 inbound from 0.0.0.0/0

NETWORK ACLs (Stateless):
  Subnet-level firewall
  Allow AND Deny rules
  Stateless: must explicitly allow inbound AND outbound
  Numbered rules — lower number = higher priority
  Use for broad subnet-level controls

VPC FLOW LOGS:
  Capture IP traffic metadata for all network interfaces
  Stored in S3 or CloudWatch
  Used for: Security analysis, compliance, troubleshooting
  Similar to NetFlow but for cloud

PRIVATE vs PUBLIC SUBNETS:
  Public subnet: Route to Internet Gateway (IGW) — internet-accessible
  Private subnet: No IGW route — internal only
                  Outbound via NAT Gateway (one-way internet access)

AWS NETWORK FIREWALL:
  Managed stateful + stateless rules
  Suricata-compatible rule groups
  Sits at VPC perimeter
```

### Azure Network Security

```
AZURE NETWORK SECURITY CONCEPTS:

NSG (Network Security Groups):
  Applied to subnets or NICs
  Stateful — like AWS Security Groups
  Priority-based rules (lower number = higher priority)
  Default rules: allow VNet traffic, allow Load Balancer, deny all inbound internet

AZURE FIREWALL:
  Fully managed, cloud-native NGFW
  Application FQDN rules (whitelist *.google.com not just IPs)
  DNAT for inbound connections
  Integrates with Azure Monitor

AZURE DDoS PROTECTION:
  Basic: Automatically enabled for all Azure services (free)
  Standard: Enhanced for VNet resources — SLA, attack analytics (\$2,944/month)

PRIVATE ENDPOINT:
  Access Azure PaaS services (Storage, SQL) over private IP
  Traffic stays within Azure backbone — never traverses internet
  Essential for compliance requirements
```

---

## 16. Network Security Tools Ecosystem

```
┌─────────────────────────────────────────────────────────────────────┐
│               NETWORK SECURITY TOOL ECOSYSTEM                       │
├──────────────┬──────────────┬──────────────────┬────────────────────┤
│  SCANNING &  │   MONITORING │  PACKET ANALYSIS │  FIREWALL/NGFW     │
│  RECON       │              │                  │                    │
├──────────────┼──────────────┼──────────────────┼────────────────────┤
│ Nmap         │ Zeek/Bro     │ Wireshark        │ Palo Alto NGFW     │
│ Masscan      │ ntopng       │ tcpdump          │ Fortinet FortiGate │
│ Shodan       │ PRTG         │ NetworkMiner     │ Check Point        │
│ Censys       │ SolarWinds   │ Moloch/Arkime    │ Cisco ASA/FTD      │
├──────────────┼──────────────┼──────────────────┼────────────────────┤
│  IDS/IPS     │   VPN        │   DDoS MITIGATION│  VULNERABILITY     │
├──────────────┼──────────────┼──────────────────┼────────────────────┤
│ Snort        │ OpenVPN      │ Cloudflare       │ Nessus/Tenable     │
│ Suricata     │ WireGuard    │ Akamai Prolexic  │ Qualys             │
│ OSSEC        │ Cisco AnyConn│ AWS Shield       │ Rapid7 Nexpose     │
│ Wazuh        │ GlobalProtect│ Arbor Networks   │ OpenVAS            │
└──────────────┴──────────────┴──────────────────┴────────────────────┘
```

---

## 17. Real-World Case Studies

### Case Study 1: NotPetya — The Most Destructive Network Attack in History (2017)

**What happened:**
NotPetya started as a supply chain attack via a compromised Ukrainian tax software update (MEDoc). Once inside, it used multiple propagation mechanisms:

```
PROPAGATION METHODS (what made it catastrophic):
  1. EternalBlue exploit → SMB vulnerability → worm to unpatched Windows
  2. Mimikatz → dump credentials from memory
  3. Use credentials → PsExec + WMIC for remote execution on patched machines
  
RESULT:
  - Spread globally in minutes (leveraged existing admin credentials)
  - Maersk (shipping): lost 45,000 PCs, 4,000 servers, 2,500 applications → $300M loss
  - FedEx TNT: $400M loss
  - Merck Pharmaceuticals: $870M loss
  - Total: ~$10 billion in damages
```

**Network security failures:**
- No network segmentation — one infection spread everywhere
- SMB open between all workstations (no firewall between users)
- Outdated systems (EternalBlue was patched 2 months prior)
- Shared admin credentials across many systems

**Lessons:**
- Patch management is network security
- East-west (internal) firewall rules are as important as north-south
- Disable SMBv1 (EternalBlue only affects SMBv1)
- Segment OT/IT networks — Maersk's shipping operations should have been completely separate

---

### Case Study 2: BGP Hijacking — When the Internet Gets Rerouted

**Real incidents:**

**2018 — Amazon Route 53 BGP hijack:**
```
Attackers announced BGP routes for Amazon's DNS servers from a small ISP
→ Traffic for myetherwallet.com (crypto wallet) redirected to attacker server
→ Users got fake site with valid-looking (but attacker-controlled) certificate
→ Users entered credentials → crypto stolen
→ $152,000 stolen in ~2 hours

ROOT CAUSE:
  - BGP has no authentication by default
  - Smaller ISPs don't always filter customer route announcements
  - No RPKI (Route Origin Validation) at time

DEFENSE (RPKI):
  Route Origin Authorization (ROA) records published
  Routers check: Is this AS authorized to announce this prefix?
  If not → route filtered
```

---

### Case Study 3: Capital One AWS S3 Data Breach (2019)

**What happened:**
A misconfigured WAF allowed a former AWS employee to exploit an SSRF (Server-Side Request Forgery) vulnerability.

```
ATTACK CHAIN:
  1. Attacker found misconfigured WAF (allowed unfiltered requests)
  2. SSRF: Sent request to AWS metadata service (169.254.169.254)
     → Retrieved temporary IAM credentials for EC2 instance role
  3. Used stolen credentials to list and download S3 buckets
  4. Downloaded 100 million customer records

ROOT CAUSE ANALYSIS — Network perspective:
  - WAF misconfigured — should have blocked SSRF attempts
  - EC2 instance role had overly broad S3 access (least privilege failure)
  - AWS metadata service endpoint should have been blocked/restricted
  - No monitoring/alerting on unusual S3 data access volume

PREVENTION:
  - IMDSv2 (requires token-based requests — prevents SSRF to metadata)
  - S3 bucket policies restrict access to specific principals
  - CloudTrail + SIEM alert on bulk S3 downloads
  - WAF rules to block requests to 169.254.169.254
```

---

### Case Study 4: Mirai Botnet — IoT DDoS Record Breaker (2016)

**What happened:**
Mirai malware infected hundreds of thousands of IoT devices (cameras, DVRs) using default credentials and launched the largest DDoS attacks in history.

```
ATTACK MECHANISM:
  1. Scan internet for Telnet (port 23) and SSH (port 22) on IoT devices
  2. Try 61 default username/password combinations
  3. If successful → device joins botnet
  4. Botnet directed to flood targets with UDP/TCP traffic

IMPACT:
  - Dyn DNS provider DDoS → Amazon, Netflix, Reddit, Twitter, GitHub offline
  - 620 Gbps against security journalist Brian Krebs
  - 1.1 Tbps against OVH (then-record)

WHY IT WORKED:
  - Hundreds of thousands of IoT devices with default credentials
  - No network monitoring on IoT devices
  - No segmentation (IoT on same network as everything else)

LESSONS:
  - IoT VLAN isolation — IoT devices should have NO access to corporate network
  - Default credential scanning (Shodan finds yours before attackers do)
  - Port 23 (Telnet) should NEVER be open on internet-facing devices
  - DDoS mitigation at cloud level (single ISP link cannot handle Tbps attacks)
```

---

## 18. Day in the Life of a Network Security Engineer

### Morning: Monitoring & Maintenance

```
07:30 - Review overnight alerts from SIEM/NGFW dashboard
        → Firewall policy violations
        → IPS alerts
        → VPN authentication failures (brute force?)
        → Unusual traffic patterns from NetFlow

08:00 - Check firewall health and performance
        → CPU/memory utilization (high = DDoS?)
        → Session table utilization
        → SSL inspection throughput

08:30 - Review pending firewall change requests
        → Validate business justification
        → Check against security policy
        → Approve/deny with documented reasoning

09:00 - Certificate expiry check
        → Any certs expiring in next 30 days?
        → Coordinate renewal with teams (avoid outage)
```

### Midday: Technical & Project Work

```
10:00 - Network security project work
        → Deploying new VLAN for acquisitioned company
        → Implementing microsegmentation for finance servers
        → Configuring new IPS signatures for recent CVEs

12:00 - Vulnerability scan review
        → Weekly scan results from Nessus/Qualys
        → Prioritize: internet-facing critical > internal high
        → Coordinate patches with server teams

14:00 - Incident support
        → SOC escalation: "Suspicious outbound traffic from Server X"
        → Pull NetFlow for server → pull NGFW logs → pull IPS alerts
        → Determine: legitimate traffic pattern or exfiltration?
        → Coordinate response: block in firewall? isolate VLAN?
```

### Afternoon: Reviews & Documentation

```
15:00 - Firewall rule review (quarterly or on rotation)
        → Identify stale rules (last hit > 6 months ago)
        → Identify overly permissive rules (any/any)
        → Prepare change request to clean up

16:00 - Threat intelligence integration
        → Update blocklists with new IOC feeds
        → Check: has our IP range appeared in threat intel feeds?
        → Review newly published CVEs affecting network devices

17:00 - Documentation and reporting
        → Update network topology diagrams
        → Document firewall changes
        → Prepare weekly security metrics report
```

---

## 19. Network Security in Corporate Environments

### Enterprise Network Security Challenges

| Challenge | Reality | Solution |
|-----------|---------|---------|
| **Legacy systems** | Old servers that can't be patched | Compensating controls: WAF, network segmentation, IPS rules |
| **Shadow IT** | Cloud apps bypassing corporate controls | CASB, DNS filtering, DLP on outbound |
| **Remote work** | All traffic now leaves corporate network | ZTNA, cloud-based security stack (SASE) |
| **IoT expansion** | Everything is on the network now | IoT VLAN, NAC, device discovery |
| **Cloud migration** | Workloads leaving on-premises | Cloud-native controls + hybrid monitoring |
| **Encrypted traffic** | Can't see what's happening in TLS | SSL inspection (with privacy policy) |
| **Compliance** | PCI-DSS CDE isolation, HIPAA | Network segmentation, documented data flows |

### Key Network Security Certifications

| Certification | Issuer | Value |
|---------------|--------|-------|
| **CompTIA Network+** | CompTIA | Entry-level networking foundation |
| **CompTIA Security+** | CompTIA | Includes significant network security |
| **Cisco CCNA Security** | Cisco | Network security with Cisco focus |
| **Cisco CCNP Security** | Cisco | Advanced, NGFW/IPS/VPN specialization |
| **Palo Alto PCNSE** | Palo Alto | Industry-leading NGFW certification |
| **Fortinet NSE 4-7** | Fortinet | FortiGate focused, widely used |
| **GIAC GPEN** | SANS | Network penetration testing |
| **GIAC GWAPT** | SANS | Web app penetration testing |

---

> **💡 Corporate Reality:** In large enterprises, network security is often split into teams: network engineers (who configure routing/switching/firewalls) and security architects (who define policy). The best network security professionals bridge both — they understand both the technical implementation AND the threat model that drives the policy. "Why" matters as much as "how."

> **📝 New Corporate Tip:** The most important skill in corporate network security isn't knowing firewall rules — it's knowing how to justify them to stakeholders. Every rule change requires a ticket, a business justification, and a review. Learn to think in terms of: "What's the business need? What's the minimum access needed to meet it? What's the risk? Who approves it?"

