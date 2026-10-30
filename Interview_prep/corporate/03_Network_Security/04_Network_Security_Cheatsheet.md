# ⚡ NETWORK SECURITY — QUICK REFERENCE CHEATSHEET

> **Use:** Night-before-interview | Daily reference | Investigation quick-lookup

---

## 🌐 CRITICAL PORTS — MEMORIZE THESE

| Port | Protocol | Service | Security Note |
|------|----------|---------|--------------|
| **20** | TCP | FTP Data | Unencrypted — avoid |
| **21** | TCP | FTP Control | Unencrypted — avoid |
| **22** | TCP | SSH | Encrypted — use instead of Telnet |
| **23** | TCP | Telnet | NEVER use — unencrypted |
| **25** | TCP | SMTP | Mail relay — abuse for spam |
| **53** | UDP/TCP | DNS | C2 tunneling risk |
| **67/68** | UDP | DHCP | DHCP starvation, rogue DHCP |
| **80** | TCP | HTTP | Unencrypted web |
| **88** | TCP/UDP | Kerberos | AD authentication |
| **110** | TCP | POP3 | Email retrieval |
| **123** | UDP | NTP | NTP amplification DDoS |
| **139** | TCP | NetBIOS/SMB | Legacy — disable |
| **143** | TCP | IMAP | Email retrieval |
| **161/162** | UDP | SNMP | v1/v2 community strings weak |
| **389** | TCP | LDAP | Use LDAPS instead |
| **443** | TCP | HTTPS | Encrypted web |
| **445** | TCP | SMB | EternalBlue, Pass-the-Hash |
| **636** | TCP | LDAPS | Encrypted LDAP — use this |
| **1433** | TCP | MSSQL | Database |
| **1812/1813** | UDP | RADIUS | Network auth |
| **3306** | TCP | MySQL | Database |
| **3389** | TCP | RDP | High attack surface — restrict |
| **4444** | TCP | Metasploit | C2 indicator |
| **5985/5986** | TCP | WinRM | PowerShell remoting |
| **8080/8443** | TCP | HTTP/HTTPS alt | Common C2 ports |

---

## 📡 OSI MODEL — SECURITY QUICK MAP

```
L7 APPLICATION    HTTP, DNS, FTP, SMTP     WAF, DNSSEC, App controls
L6 PRESENTATION   TLS/SSL                  TLS 1.3, cipher hardening
L5 SESSION        NetBIOS, RPC             Session timeouts, tokens
L4 TRANSPORT      TCP, UDP                 SYN cookies, rate limiting
L3 NETWORK        IP, ICMP, OSPF, BGP      uRPF, BCP38, ACLs
L2 DATA LINK      Ethernet, ARP, VLAN      DAI, 802.1X, port security
L1 PHYSICAL       Cables, NICs             Physical access controls
```

---

## 🤝 TCP FLAGS — ATTACK REFERENCE

| Flag | Hex | Normal Use | Attack Use |
|------|-----|-----------|-----------|
| **SYN** | 0x02 | Start connection | SYN flood |
| **ACK** | 0x10 | Acknowledge data | ACK flood |
| **FIN** | 0x01 | Close connection gracefully | FIN scan (stealth scan) |
| **RST** | 0x04 | Abrupt close / port closed | RST injection, TCP reset attack |
| **PSH** | 0x08 | Deliver data immediately | — |
| **URG** | 0x20 | Urgent pointer | Rarely exploited |

**Nmap scans:**
```
-sS  (SYN/Stealth):  SYN → SYN-ACK(open) / RST(closed) / nothing(filtered)
-sF  (FIN):          FIN → RST(closed) / nothing(open or filtered)
-sN  (NULL):         No flags → RST(closed) / nothing(open or filtered)
-sX  (Xmas):         FIN+PSH+URG → RST(closed) / nothing(open or filtered)
-sU  (UDP):          UDP → ICMP Port Unreach(closed) / nothing(open/filtered)
```

---

## 🏗️ NETWORK ARCHITECTURE QUICK REFERENCE

### Traffic Flow Rules (Memorize)
```
Internet → External FW → DMZ → Internal FW → Internal Network

WHAT'S ALLOWED:
  Internet → DMZ:         Only HTTPS/80 to web servers, SMTP to mail relay
  DMZ → Internet:         Outbound for patches, threat intel updates
  DMZ → Internal:         ONLY specific app connections (DB queries etc.)
  Internal → DMZ:         Management access only
  Internal → Internet:    Via proxy (monitored, filtered)
  DMZ → ↑ Internet:      NOT allowed to initiate (servers shouldn't call home)

GOLDEN RULE:
  DMZ servers should NEVER initiate connections to internal network.
```

### VLAN Security Design
| VLAN | Name | Access Policy |
|------|------|--------------|
| 10 | Management (OOB) | Admin workstations only |
| 20 | Servers (Prod) | Specific application ports only |
| 30 | Corporate Users | Internet + specific internal servers |
| 40 | DMZ | Internet-facing, restricted internal |
| 50 | Development | Isolated from production |
| 60 | Guest | Internet only, no internal |
| 70 | OT/SCADA | Isolated/air-gapped, no internet |
| 80 | Security | Read-only access to all VLANs |

---

## ⚔️ NETWORK ATTACK QUICK MAP

| Attack | Layer | What happens | Detection | Defense |
|--------|-------|-------------|-----------|---------|
| **SYN Flood** | L4 | Exhaust TCP state table | Half-open connections spike | SYN cookies |
| **UDP Flood** | L4 | Saturate bandwidth | Traffic spike | Rate limiting, upstream scrubbing |
| **DNS Amp.** | L3/L7 | Small query → huge response | Traffic from many sources | BCP38, RRL |
| **ARP Poisoning** | L2 | Redirect traffic through attacker | Duplicate MAC-IP mappings | DAI, static ARP |
| **VLAN Hopping** | L2 | Jump between VLANs | DTP frames from access port | Disable DTP, explicit port modes |
| **IP Spoofing** | L3 | Forge source IP | Ingress filter violations | uRPF, BCP38 |
| **Slowloris** | L7 | Hold connections open | Many partial connections | Connection timeout, max conn/IP |
| **DNS Tunneling** | L7 | C2 over DNS | Long queries, high frequency | DNS analytics, DPI |
| **SSL Stripping** | L6 | Downgrade HTTPS→HTTP | HTTP traffic to HTTPS sites | HSTS |
| **BGP Hijacking** | L3 | Reroute internet traffic | BGPmon route anomalies | RPKI |
| **Smurf** | L3 | ICMP broadcast amplification | Many ICMP from many sources | Disable directed broadcasts |
| **MITM** | Multiple | Intercept communications | Cert errors, ARP anomalies | Encryption, DAI, HSTS |

---

## 🔒 FIREWALL RULE DESIGN — QUICK REFERENCE

```
RULE STRUCTURE:
  Action | Source | Destination | Service | Log?

RULE ORDER (first match wins — critical!):
  1. Explicit DENY (threat intel blocklist)
  2. PERMIT management traffic
  3. PERMIT required application traffic
  4. DENY ALL (implicit or explicit)

RULE DESIGN PRINCIPLES:
  ✅ Least privilege — only what's needed
  ✅ Log denied traffic (for detection)
  ✅ Log permitted traffic for critical zones
  ✅ Document each rule with change ticket
  ✅ Review rules every 6 months
  ❌ Never any/any
  ❌ Never "temporary" rules without expiry date
  ❌ Never copy rules without understanding them
```

---

## 🔐 TLS QUICK REFERENCE

### TLS Versions
| Version | Status |
|---------|--------|
| SSL 2.0/3.0 | NEVER — broken |
| TLS 1.0 | Deprecated — disable |
| TLS 1.1 | Deprecated — disable |
| TLS 1.2 | Acceptable (with proper ciphers) |
| **TLS 1.3** | **Recommended — always** |

### Cipher Suite Reading
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
     ↑         ↑        ↑         ↑
  Key Exch   Auth    Encryption   MAC

GOOD: ECDHE/DHE (forward secrecy), AES-128/256, GCM, SHA256+
BAD:  NULL, RC4, DES/3DES, MD5, SHA1, EXPORT, RSA key exchange
```

### Certificate Validation Steps (Browser)
```
1. Valid signature from trusted CA?
2. Not expired?
3. Domain matches CN or SAN field?
4. Not revoked? (OCSP / CRL check)
5. Certificate chain valid?
```

---

## 📶 WIRELESS SECURITY QUICK REFERENCE

| Protocol | Status | Weakness |
|----------|--------|---------|
| WEP | BROKEN | RC4 IV reuse — crack in minutes |
| WPA | Deprecated | TKIP weak, dictionary attacks |
| WPA2-Personal | Acceptable | PMKID attack on weak passwords |
| WPA2-Enterprise | Recommended | Secure with proper EAP method |
| WPA3 | Best | Most secure, newer devices |

**Enterprise WiFi (802.1X):**
```
Device → AP (Authenticator) → RADIUS → AD/LDAP
                               ↓
                    VLAN assigned based on user/device type
```

**Wireless Attacks:**
```
Evil Twin        → Fake AP with same SSID → Defense: 802.1X (cert validates real network)
Deauthentication → Kick clients off → Defense: 802.11w (MFP)
PMKID Attack     → Offline password crack → Defense: Strong passphrase or WPA3
WPS Attack       → Brute force 8-digit PIN → Defense: Disable WPS
```

---

## 🌊 DDOS MITIGATION QUICK LAYERS

```
LAYER         TOOL                    WHAT IT HANDLES
─────         ────                    ───────────────
Cloud/ISP     Cloudflare, Akamai      Volumetric (Tbps) — absorbs before hitting you
ISP           Null-routing/blackhole  Emergency — drops all traffic to attacked IP
Edge Router   ACLs, rate limiting     Filter known bad sources, rate limit per IP
Firewall      SYN cookies             SYN flood specifically
WAF           Behavioral rules        L7 flood, Slowloris, HTTP flood
App Server    Connection limits       Per-IP connection count limits, CAPTCHA
```

---

## 🔍 TRAFFIC ANALYSIS — WIRESHARK FILTERS

```bash
# Filter by protocol
http | tls | dns | tcp | udp | icmp | arp

# Filter by IP
ip.addr == 10.0.0.1
ip.src == 10.0.0.1
ip.dst == 8.8.8.8

# Filter by port
tcp.port == 443
tcp.dstport == 22

# Find RST packets (closed/reset connections)
tcp.flags.reset == 1

# Find SYN packets (connection attempts)
tcp.flags.syn == 1 and tcp.flags.ack == 0

# Find large payloads
tcp.len > 1000

# HTTP POST
http.request.method == "POST"

# DNS queries only
dns.flags.response == 0

# Find cleartext passwords (educational/authorized testing only)
http contains "password"

# Combination filter
ip.addr == 10.0.0.5 and tcp.port == 445
```

---

## 📊 SUBNETTING QUICK REFERENCE

| CIDR | Mask | Hosts | Network Bits | Use Case |
|------|------|-------|-------------|---------|
| /24 | 255.255.255.0 | 254 | 24 | Standard LAN |
| /25 | 255.255.255.128 | 126 | 25 | Split /24 in 2 |
| /26 | 255.255.255.192 | 62 | 26 | Split /24 in 4 |
| /27 | 255.255.255.224 | 30 | 27 | Small segment |
| /28 | 255.255.255.240 | 14 | 28 | DMZ / small VLAN |
| /29 | 255.255.255.248 | 6 | 29 | Very small segment |
| /30 | 255.255.255.252 | 2 | 30 | Point-to-point links |
| /32 | 255.255.255.255 | 1 | 32 | Single host route |

**Private IP Ranges (RFC1918):**
```
10.0.0.0/8          → 10.0.0.0 - 10.255.255.255
172.16.0.0/12       → 172.16.0.0 - 172.31.255.255
192.168.0.0/16      → 192.168.0.0 - 192.168.255.255
169.254.0.0/16      → APIPA (auto-assigned when DHCP fails)
127.0.0.0/8         → Loopback
```

---

## 📋 KEY NETWORK SECURITY ACRONYMS

| Acronym | Full Form |
|---------|-----------|
| NGFW | Next-Generation Firewall |
| DMZ | Demilitarized Zone |
| NAC | Network Access Control |
| NAT | Network Address Translation |
| PAT | Port Address Translation |
| IDS | Intrusion Detection System |
| IPS | Intrusion Prevention System |
| NIDS | Network-based IDS |
| HIDS | Host-based IDS |
| NSM | Network Security Monitoring |
| uRPF | Unicast Reverse Path Forwarding |
| BCP38 | Best Current Practice 38 (anti-spoofing) |
| DAI | Dynamic ARP Inspection |
| RPKI | Resource Public Key Infrastructure |
| ZTNA | Zero Trust Network Access |
| SASE | Secure Access Service Edge |
| SDP | Software-Defined Perimeter |
| WAF | Web Application Firewall |
| DDoS | Distributed Denial of Service |
| NTP | Network Time Protocol |
| SNMP | Simple Network Management Protocol |
| BGP | Border Gateway Protocol |
| OSPF | Open Shortest Path First |
| ACL | Access Control List |
| VLAN | Virtual Local Area Network |
| STP | Spanning Tree Protocol |
| DTP | Dynamic Trunking Protocol |
| BPDU | Bridge Protocol Data Unit |
| MTU | Maximum Transmission Unit |
| MSS | Maximum Segment Size |
| TTL | Time to Live |
| QoS | Quality of Service |
| MPLS | Multiprotocol Label Switching |
| GRE | Generic Routing Encapsulation |
| ESP | Encapsulating Security Payload (IPsec) |
| AH | Authentication Header (IPsec) |
| IKE | Internet Key Exchange |
| PFS | Perfect Forward Secrecy |
| HSTS | HTTP Strict Transport Security |
| CT | Certificate Transparency |
| OCSP | Online Certificate Status Protocol |
| CRL | Certificate Revocation List |
| CAA | Certification Authority Authorization |
| SNI | Server Name Indication |
| MFP | Management Frame Protection (802.11w) |
| PCAP | Packet Capture |

---

> **🔖 Print this and review every port, every attack, every acronym — these appear constantly.**
> 
> **Interview reminder:** When answering architecture questions — always mention the attack it prevents. Don't just describe the control; explain the threat model. That's what separates senior candidates.

