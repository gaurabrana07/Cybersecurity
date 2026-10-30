# 🎯 NETWORK SECURITY — INTERVIEW QUESTIONS BANK

> **Coverage:**  
> 🔴 Priority Questions (Core concepts — asked in 90%+ interviews)  
> 🟡 Job-Switching Questions  
> 🟢 Experience-Based / Scenario Questions  
> 🔵 Behavioral / Situational Questions

---

## 📋 TABLE OF CONTENTS

1. [Priority — Networking Fundamentals](#-priority--networking-fundamentals)
2. [Priority — Firewalls & Network Controls](#-priority--firewalls--network-controls)
3. [Priority — Protocols & Encryption](#-priority--protocols--encryption)
4. [Priority — Attacks & Defense](#-priority--attacks--defense)
5. [Priority — Network Architecture](#-priority--network-architecture)
6. [Job-Switching Questions](#-job-switching-questions)
7. [Experience-Based / Scenario Questions](#-experience-based--scenario-questions)
8. [Behavioral / Situational Questions](#-behavioral--situational-questions)
9. [Quick Fire Round](#-quick-fire-round)

---

# 🔴 PRIORITY — NETWORKING FUNDAMENTALS

---

## Q1: Explain the OSI model and give a security example at each layer.

**Answer:**

| Layer | Name | Protocol Examples | Attack | Defense |
|-------|------|-------------------|--------|---------|
| 7 | Application | HTTP, DNS, FTP | SQL injection, XSS | WAF, Input validation |
| 6 | Presentation | TLS, SSL | SSL stripping, weak ciphers | TLS 1.3, cipher hardening |
| 5 | Session | NetBIOS, RPC | Session hijacking | Secure session mgmt, timeouts |
| 4 | Transport | TCP, UDP | SYN flood, TCP hijacking | SYN cookies, rate limiting |
| 3 | Network | IP, ICMP | IP spoofing, ICMP flood | uRPF, ingress filtering |
| 2 | Data Link | Ethernet, ARP | ARP poisoning, MAC flood | DAI, port security |
| 1 | Physical | Cables, signals | Physical tapping | Physical access controls |

**Interview tip:** Be ready to say "Firewalls primarily operate at Layers 3-4 (stateful) and Layer 7 (NGFW)" — this shows architectural understanding.

---

## Q2: Explain the TCP three-way handshake and how it can be exploited.

**Answer:**

**Normal handshake:**
1. Client → Server: **SYN** (seq=x) — "I want to connect"
2. Server → Client: **SYN-ACK** (seq=y, ack=x+1) — "OK, you're acknowledged"
3. Client → Server: **ACK** (ack=y+1) — "Connection established"

**SYN Flood Attack:**
- Attacker sends massive SYN packets with spoofed source IPs
- Server responds with SYN-ACK and stores half-open connection in state table
- ACK never arrives (spoofed IPs) → state table fills up
- Legitimate connections rejected

**Defense — SYN Cookies:**
- Server encodes connection parameters in the sequence number (the "cookie")
- Server sends SYN-ACK but does NOT store state
- When valid ACK arrives, server regenerates state from cookie
- Spoofed SYNs: no ACK arrives → no state ever created → no resource exhaustion

---

## Q3: What is the difference between TCP and UDP? When is each used from a security perspective?

**Answer:**

| | TCP | UDP |
|-|-----|-----|
| **Connection** | Connection-oriented (handshake) | Connectionless |
| **Reliability** | Guaranteed, ordered delivery | Best-effort, no guarantee |
| **Speed** | Slower (overhead) | Faster |
| **Header size** | 20 bytes | 8 bytes |
| **Use cases** | HTTP, SSH, FTP — where data integrity matters | DNS, VoIP, streaming, DHCP |

**Security perspective:**
- **TCP attacks:** SYN flood, session hijacking, RST injection — stateful nature creates attack surface
- **UDP attacks:** UDP flood, DNS amplification — connectionless = easy to spoof and amplify
- **UDP amplification:** Attacker sends small spoofed request (victim's IP as source) → server sends large response to victim → bandwidth DDoS
- **DNS amplification ratio:** Up to 70x (small 30-byte query → 3,000-byte response)

---

## Q4: What is ARP and how can it be exploited?

**Answer:**

**ARP (Address Resolution Protocol):** Maps IP addresses to MAC addresses on the local network.

**Normal flow:**
```
PC-A wants to talk to 192.168.1.5
→ Broadcasts ARP request: "Who has 192.168.1.5?"
→ PC-B responds: "I have 192.168.1.5, my MAC is AA:BB:CC:DD:EE:FF"
→ PC-A caches this in ARP table, sends traffic to that MAC
```

**ARP Poisoning / Spoofing:**
- ARP has NO authentication — any machine can claim any IP
- Attacker broadcasts fake ARP: "I have 192.168.1.1 (gateway), my MAC is attacker's MAC"
- Victims update their ARP cache → send traffic to attacker
- Attacker captures traffic (MITM) and forwards it → invisible to victims
- Can intercept HTTP traffic, steal credentials, inject content

**Detection:** Duplicate MAC-to-IP mappings in ARP table; IDS alerts for gratuitous ARP traffic.

**Defense:**
- **Dynamic ARP Inspection (DAI):** Switch validates ARP packets against DHCP snooping binding table
- **Static ARP entries** for critical devices (not scalable but effective)
- **Encryption:** Even if MITM, can't read TLS-encrypted traffic (certificate mismatch would alert user)

---

## Q5: What is subnetting? Give an example.

**Answer:**

Subnetting divides a network into smaller logical sub-networks.

**Example:**
```
Network: 192.168.1.0/24

Split into 4 subnets (/26 = 2 bits borrowed):
  Subnet 1: 192.168.1.0/26   → Hosts: .1 to .62   (62 usable hosts)
  Subnet 2: 192.168.1.64/26  → Hosts: .65 to .126  (62 usable hosts)
  Subnet 3: 192.168.1.128/26 → Hosts: .129 to .190 (62 usable hosts)
  Subnet 4: 192.168.1.192/26 → Hosts: .193 to .254 (62 usable hosts)

/26 mask = 255.255.255.192
Binary:  11111111.11111111.11111111.11000000
                                    ↑↑ subnet bits
```

**Security relevance:**
- Subnets create isolation boundaries where firewalls/ACLs can be enforced
- Network segmentation IS subnet segmentation with security controls at boundaries
- VLAN = Layer 2 segmentation; subnets = Layer 3 segmentation (often implemented together)

---

## Q6: How does DNS work? What are the most important DNS record types?

**Answer:**

**DNS Resolution Flow:**
1. Browser checks local cache
2. OS checks hosts file
3. OS queries DNS resolver (configured in network settings)
4. Resolver checks its cache — if hit, returns answer
5. If miss: Recursive resolution → Root NS → TLD NS (.com) → Authoritative NS for domain
6. Answer returned + cached with TTL

**Critical DNS Record Types:**

| Record | Purpose | Security Relevance |
|--------|---------|-------------------|
| **A** | Domain → IPv4 | Monitor for unauthorized changes (hijacking) |
| **AAAA** | Domain → IPv6 | Same as A |
| **MX** | Mail server | SPF/DMARC validation, phishing vectors |
| **CNAME** | Alias to another name | Subdomain takeover risk |
| **TXT** | Text info | SPF, DKIM, DMARC records stored here |
| **NS** | Authoritative nameservers | Hijacking target |
| **PTR** | IP → Domain (reverse DNS) | Used in log analysis, spam detection |
| **SOA** | Zone authority info | Zone transfer target |
| **CAA** | Authorized CAs for domain | Prevent unauthorized cert issuance |
| **DNSKEY/DS** | DNSSEC signing | DNSSEC chain of trust |

---

# 🔴 PRIORITY — FIREWALLS & NETWORK CONTROLS

---

## Q7: What is the difference between stateless and stateful firewalls?

**Answer:**

**Stateless (Packet Filter):**
- Each packet evaluated independently based on rules (source IP, dest IP, port, protocol)
- No memory of previous packets
- Fast, simple, low overhead
- Cannot distinguish: "Is this a new connection or part of an established one?"
- Weakness: An attacker can craft a packet that looks like a response and slip through

**Stateful:**
- Tracks connection state in a state table (SYN, ESTABLISHED, FIN-WAIT, etc.)
- Knows if a packet is part of an established connection
- Can allow return traffic automatically for outbound connections
- Cannot see application payload

**Practical difference:**
```
Stateless rule to allow web browsing:
  PERMIT TCP any → any:80 (outbound)
  PERMIT TCP any:80 → any (inbound — needed for responses)
  Problem: Inbound rule allows ANY packet from port 80, not just responses

Stateful rule:
  PERMIT TCP any → any:80 ESTABLISHED
  → Firewall automatically allows matching return traffic
  → Inbound traffic on port 80 only allowed if it's part of established session
```

---

## Q8: What is a NGFW and what can it do that a traditional firewall cannot?

**Answer:**

**NGFW = Next-Generation Firewall** — combines traditional stateful inspection with:

| Capability | Traditional Firewall | NGFW |
|-----------|---------------------|------|
| Port/protocol control | ✅ | ✅ |
| Application identification | ❌ | ✅ (identify Netflix traffic on port 443) |
| User identity | ❌ | ✅ (block by user, not just IP) |
| SSL/TLS inspection | ❌ | ✅ (decrypt, inspect, re-encrypt) |
| IPS | ❌ | ✅ (signature + behavioral) |
| URL filtering | ❌ | ✅ (categories: gambling, malware) |
| Threat intelligence | ❌ | ✅ (block known malicious IPs/domains) |
| File inspection | ❌ | ✅ (sandbox suspected files) |
| DNS security | ❌ | ✅ |

**Key example:** Traditional firewall sees HTTPS on port 443 — allows it (trusted port). NGFW decrypts the HTTPS and sees it's actually malware C2 communication — blocks it.

---

## Q9: What is NAT and what security implications does it have?

**Answer:**

**NAT (Network Address Translation):** Translates private IP addresses to a public IP for internet communication.

```
TYPES:
Static NAT:  One private IP ↔ One public IP (one-to-one)
Dynamic NAT: Pool of public IPs assigned from pool (many-to-many)
PAT/Masquerade: Many private IPs → One public IP + different ports (most common)

PAT FLOW:
  PC 192.168.1.10:4500 → Internet → NAT translates to: 203.0.113.1:10500
  Server responds to 203.0.113.1:10500 → NAT translates back to 192.168.1.10:4500
```

**Security implications:**
- **Hides internal topology** — attackers can't easily enumerate internal IPs (some protection)
- **One-way initiation** — by default, NAT only allows internally-initiated connections (basic firewall effect)
- **NOT a security control** — does not inspect traffic, can be bypassed
- **Complicates forensics** — multiple users share one public IP, must correlate with NAT logs to identify source
- **IP-based blocking is harder** — blocking one public IP blocks all users behind it

---

## Q10: What is Network Access Control (NAC)?

**Answer:**

**NAC** enforces security policy before a device is allowed on the network — check first, then grant access.

**What NAC checks:**
- Is the device managed (in MDM/inventory)?
- Is the operating system up to date with patches?
- Is antivirus running and up to date?
- Is the device compliant with corporate security policy?
- Who is the user (authentication via 802.1X)?

**NAC outcomes:**
- **Compliant device:** Full network access to appropriate VLAN
- **Non-compliant:** Placed in remediation VLAN (access to patch servers only)
- **Unknown device:** Guest VLAN (internet only)
- **Unauthorized user:** Blocked

**Tools:** Cisco ISE, Aruba ClearPass, ForeScout, Microsoft Network Policy Server (NPS)

**Why it matters:** Stops compromised or unmanaged devices from joining the internal network — even if someone plugs in physically.

---

# 🔴 PRIORITY — PROTOCOLS & ENCRYPTION

---

## Q11: How does TLS work? What makes TLS 1.3 better than TLS 1.2?

**Answer:**

**TLS handshake (simplified):**
1. Client sends **ClientHello** (supported cipher suites, TLS versions, random)
2. Server sends **ServerHello** (chosen cipher, certificate, server key share)
3. Client verifies certificate (valid CA? Not expired? Domain match? Not revoked?)
4. Key exchange (ECDHE — both compute the same shared secret without transmitting it)
5. Both derive symmetric session keys from shared secret + random values
6. Encrypted communication begins

**TLS 1.3 improvements over 1.2:**

| Aspect | TLS 1.2 | TLS 1.3 |
|--------|---------|---------|
| **Round trips** | 2-RTT (slower) | 1-RTT (faster); 0-RTT for resumed sessions |
| **Forward secrecy** | Optional (RSA key exchange has none) | Mandatory (ECDHE only) |
| **Cipher suites** | Many, including weak ones | Only 5 strong suites, no weak options |
| **Removed features** | RSA key exchange, static DH, RC4, 3DES, MD5 | All removed |
| **Downgrade attacks** | Possible (POODLE, BEAST) | Protocol prevents downgrade |

**Perfect Forward Secrecy (PFS):** Each session uses a unique ephemeral key. If the server's long-term private key is stolen later, it cannot decrypt past sessions. TLS 1.3 makes this mandatory.

---

## Q12: What is a VPN and how does IPsec work?

**Answer:**

**VPN:** Creates an encrypted tunnel over an untrusted network (internet) to securely connect remote users or networks.

**IPsec phases:**
```
PHASE 1 (IKE — Internet Key Exchange):
  Goal: Authenticate peers + establish secure channel for Phase 2
  Method: Certificate or pre-shared key authentication
  Creates: IKE Security Association (SA)
  IKEv2: 4 messages (faster, more secure than IKEv1)

PHASE 2 (IPsec):
  Goal: Negotiate parameters for actual data encryption
  Creates: IPsec SA (defines encryption/integrity algorithms, lifetime)
  Uses: AES for encryption, SHA-256/384 for integrity

IPSEC MODES:
  Transport:  Encrypts payload only; IP header unchanged (host-to-host)
  Tunnel:     Encrypts entire original packet + new outer header (site-to-site)

IPSEC PROTOCOLS:
  AH (Auth Header):    Integrity only, NO encryption
  ESP (Encap Security Payload): Encryption + integrity → ALWAYS USE ESP
```

---

## Q13: What is DNS tunneling and how do you detect it?

**Answer:**

**DNS tunneling:** Attacker encodes data (C2 communications, exfiltrated data) inside DNS queries/responses, using DNS as a covert channel.

**Why it works:** Firewalls typically allow DNS traffic (UDP/TCP port 53) — DNS is fundamental and blocking it breaks the internet.

**How it works:**
```
Malware on corporate machine:
  → Encodes "ls -la /sensitive" in base64: "bHMgLWxhIC9zZW5zaXRpdmU="
  → Sends DNS query: bHMgLWxhIC9zZW5zaXRpdmU.attacker-c2.com
  → Attacker's DNS server receives query → decodes → executes command
  → Response encoded in DNS TXT record → returned to malware
  → All looks like normal DNS traffic to network monitors
```

**Detection indicators:**
1. **Query length:** Normal domains < 30 chars; tunneled = 100+ chars
2. **Subdomain entropy:** Random/encoded subdomains (high character diversity)
3. **Query frequency:** Normal user queries ~50-200/day; tunneling = thousands
4. **Response size:** TXT records unusually large
5. **Same domain, many subdomains:** One domain queried hundreds of times with different encoded subdomains
6. **Beacon timing:** Regular interval queries (beaconing pattern)

**SIEM detection:**
```splunk
index=dns
| eval query_len=len(query)
| where query_len > 50
| stats count by query, src_ip
| where count > 10
```

---

# 🔴 PRIORITY — ATTACKS & DEFENSE

---

## Q14: How does a DDoS attack work? What are the main types?

**Answer:**

**DDoS (Distributed Denial of Service):** Overwhelm a target with traffic/requests from many sources simultaneously to deny service to legitimate users.

**Types:**

**1. Volumetric — Flood bandwidth:**
- UDP Flood, ICMP Flood
- Amplification attacks (DNS, NTP, Memcached) — small spoofed request → huge response to victim
- Memcached amplification: 50,000x amplification — 1 byte query → 50KB response

**2. Protocol — Exhaust connection state:**
- SYN Flood — fills TCP state table
- Smurf (ICMP broadcast amplification)
- Ping of Death (malformed oversized ICMP)

**3. Application Layer (L7) — Hardest to mitigate:**
- HTTP GET/POST flood — legitimate-looking requests that overwhelm server
- Slowloris — open many connections, send headers slowly → server connection pool exhausted
- SSL exhaustion — expensive TLS handshakes overwhelm server CPU

**Mitigation:**
- Volumetric: Upstream scrubbing (Cloudflare, Akamai) — absorb Tbps
- Protocol: SYN cookies, ingress filtering (BCP38), rate limiting
- L7: WAF with behavioral analysis, CAPTCHA, rate limiting per IP/session

---

## Q15: What is a Man-in-the-Middle (MITM) attack? How do you prevent it?

**Answer:**

**MITM:** Attacker secretly intercepts communications between two parties who believe they're talking directly to each other.

**Attack methods:**
- **ARP poisoning** (LAN) — Redirect traffic through attacker's machine
- **Rogue WiFi** (Evil twin) — Fake AP, all traffic through attacker
- **SSL stripping** — Downgrade HTTPS to HTTP (requires active ARP attack or rogue AP)
- **BGP hijacking** — Reroute internet traffic at routing level
- **DNS hijacking** — Redirect domain to attacker's IP

**Prevention:**
- **Encryption (TLS):** Even if traffic intercepted, can't read it without private key
- **Certificate validation:** Browser/OS warns when certificate doesn't match or isn't trusted
- **HSTS (HTTP Strict Transport Security):** Browsers refuse to connect via HTTP after first HTTPS visit
- **Certificate Pinning:** App only accepts specific certificate/CA (prevents rogue cert MITM)
- **DNSSEC:** Cryptographically validates DNS responses
- **MFA:** Even if credentials captured, attacker can't authenticate without second factor (for most MFA types)
- **802.11w (MFP):** Prevents rogue AP deauthentication attacks

---

## Q16: Explain VLAN hopping. How does it occur and how is it prevented?

**Answer:**

**VLAN Hopping:** Attack to send traffic from one VLAN to another VLAN that should be isolated from it.

**Method 1 — Switch Spoofing:**
- Normal ports: Access mode (one VLAN)
- Trunk ports: Carry multiple VLANs (for inter-switch links)
- Attack: Attacker pretends to be a switch (sends DTP frames) → switches negotiate trunk link
- Now attacker is on trunk → can send/receive traffic to/from ALL VLANs

**Method 2 — Double Tagging:**
- Attacker adds two 802.1Q VLAN tags to their frame
- First switch strips outer tag (attacker's native VLAN) → forwards inner-tagged frame
- Second switch sees inner tag → routes to target VLAN
- Requires attacker to be on native VLAN

**Prevention:**
- Disable DTP (Dynamic Trunking Protocol) on all access ports: `switchport nonegotiate`
- Explicitly configure all ports as access or trunk (no auto modes)
- Change native VLAN from VLAN 1 to an unused VLAN
- Never assign user ports to native VLAN
- Disable unused ports and assign them to a "dead" VLAN

---

## Q17: What is port scanning? What are the most common Nmap scan types?

**Answer:**

**Port scanning:** Probe network hosts to determine which ports are open (services running) — reconnaissance step in any attack.

**Common Nmap scans:**

| Scan | Flag | How | When to use |
|------|------|-----|------------|
| **TCP Connect** | `-sT` | Full 3-way handshake | When you have no raw socket privileges |
| **SYN/Stealth** | `-sS` | Send SYN → wait → send RST, never complete | Default, faster, fewer logs on target |
| **UDP** | `-sU` | Send UDP → ICMP Port Unreachable = closed; no response = open/filtered | Detect UDP services |
| **FIN** | `-sF` | Send FIN → RST = closed; no response = open (RFC 793) | Evade some firewalls |
| **NULL** | `-sN` | No flags → RST = closed | Evade some firewalls |
| **Xmas** | `-sX` | FIN+PSH+URG → RST = closed | Evade some firewalls |
| **OS Detection** | `-O` | Analyze TCP/IP stack behavior | Fingerprint target OS |
| **Service Version** | `-sV` | Banner grabbing | Identify service versions |
| **Aggressive** | `-A` | OS + version + scripts + traceroute | Full recon |

**Detection of port scans:**
- IDS signature for: one IP connecting to many ports on one host in short time
- Firewall logs: many connection attempts, mostly rejected
- Threshold: > 15 unique ports in 5 seconds from same source = alert

---

# 🔴 PRIORITY — NETWORK ARCHITECTURE

---

## Q18: What is a DMZ and why is it important?

**Answer:**

**DMZ (Demilitarized Zone):** A network segment between the public internet and the internal network that hosts services that must be accessible from the internet.

**Why it's needed:**
- Web servers, mail relays, and public APIs must be reachable from internet
- But they must not have direct access to the sensitive internal network
- DMZ creates a controlled boundary between public and private

**Architecture:**
```
Internet → External Firewall → DMZ → Internal Firewall → Internal Network

Key rules:
  Internet → DMZ:      Only HTTPS/80 to web servers, SMTP to mail relay
  DMZ → Internal:      ONLY specific application connections required (e.g., app-to-DB on 5432)
  Internal → DMZ:      Management only (from admin workstations)
  DMZ → Internet:      Outbound for updates only

CRITICAL RULE: DMZ servers should NEVER initiate connections to internal network.
               Attackers who compromise a DMZ server cannot pivot inward directly.
```

---

## Q19: What is network segmentation and why does it matter for security?

**Answer:**

**Network segmentation:** Dividing a network into isolated sub-networks with security controls enforced at the boundaries.

**Without segmentation:**
- One compromised workstation → direct access to all servers, all databases, all other workstations
- Ransomware spreads to everything instantly
- Lateral movement is trivially easy

**With segmentation:**
- Finance workstations can only reach Finance app servers
- Finance app servers can only reach Finance database
- No workstation-to-workstation traffic permitted (stops worm propagation)
- Even if attacker compromises a workstation, they're contained in that VLAN

**Implementation levels:**
1. **VLAN segmentation** — Layer 2 isolation + Layer 3 ACLs between VLANs
2. **Firewall-based segmentation** — Security policy enforced at firewall between segments
3. **Micro-segmentation** — Workload-level policy (East-West firewall on every VM)

**Compliance requirement:** PCI-DSS requires isolation of cardholder data environment (CDE) from all other networks — this is achieved through segmentation.

---

## Q20: What is Zero Trust and how does it differ from the traditional perimeter model?

**Answer:**

**Traditional Perimeter ("Castle and Moat"):**
- Network boundary = trust boundary
- Inside network = trusted
- Outside network = untrusted
- Once inside, relatively free movement

**Problem:** Phishing, insider threats, and supply chain attacks get attackers inside. Then they have trusted access.

**Zero Trust ("Never trust, always verify"):**
- No implicit trust based on network location
- Every access request verified: identity + device + context + risk
- Least-privilege access even for internal users
- Assume breach — act as if attacker is already inside

**Zero Trust in practice:**
- MFA for every application, from any location (not just when remote)
- Conditional Access: evaluate risk signals on every login
- Micro-segmentation: no lateral movement even for authenticated users
- Continuous monitoring: session-level detection, not just perimeter alerts
- Just-in-time access: no standing privilege

**Practical difference:** "Corporate VPN" model puts you on the network. ZTNA puts you in a tunnel to ONLY the specific application you need — you never touch the broader network.

---

# 🟡 JOB-SWITCHING QUESTIONS

---

## Q21: You're switching from a NOC (Network Operations Center) role to Network Security. How does your experience translate?

**Sample Answer:**

*"In NOC, I developed deep expertise in network monitoring and troubleshooting — skills that are directly foundational to network security. I understand normal traffic patterns (so I can spot anomalies), I know how to read NetFlow and firewall logs (different context but same data), and I've responded to network incidents (outages vs. security incidents require similar structured response processes). The key difference I'm working to build is the security threat perspective — understanding attack techniques so I can recognize them in the monitoring data I already know how to read. I've been building this through [TryHackMe / Security Onion lab / PCAP analysis on malware-traffic-analysis.net] and am [working toward Security+/CCNP Security]."*

---

## Q22: Coming from a pure networking background — what's the biggest mindset shift for network security?

**Answer:**

*"In pure networking, success means traffic flows where it should. In network security, success means traffic flows where it should AND nothing malicious is happening. The shift is from thinking about connectivity to thinking about threat modeling — for every traffic flow, asking: could an attacker abuse this? Is this the minimum access needed? The other shift is from reactive troubleshooting to proactive monitoring. Network engineers fix problems after users complain; network security engineers find problems before they're noticed. I've been developing that proactive mindset through threat hunting exercises and by studying how attackers think using MITRE ATT&CK."*

---

## Q23: How would you approach assessing the security posture of a network you've just been given responsibility for?

**Answer:**

*"Methodically — discovery before changes:*

*Week 1: Understand what exists*
*- Network diagram review (if it exists — often outdated)*
*- Run authorized discovery scan (Nmap) to find actual assets*
*- Check firewall rule sets — any obvious issues (any/any rules, stale rules)?*
*- Review VLAN/segmentation design*

*Week 2-3: Identify gaps*
*- Shodan search for my IP ranges — what can attackers see from internet?*
*- TLS certificate scan — any expired, weak, or misconfigured certs?*
*- Open service inventory — any Telnet, unencrypted HTTP, FTP exposed?*
*- Vulnerability scan results review*

*Month 2: Prioritize and fix*
*- Internet-facing criticals first (High CVSS + publicly exposed)*
*- Quick wins: disable Telnet, enforce TLS, close unnecessary ports*
*- Medium-term: segmentation improvements, firewall rule cleanup*
*- Long-term: roadmap for major architecture improvements*"*

---

# 🟢 EXPERIENCE-BASED / SCENARIO QUESTIONS

---

## Q24: You receive an alert that a server is making outbound connections to an unknown IP on port 4444. Walk me through your investigation.

**Answer:**

```
Port 4444 = Metasploit Meterpreter default C2 port → High suspicion

STEP 1 — GATHER CONTEXT
  - What server is this? (Check CMDB — owner, criticality, business function)
  - When did connections start? (Pull firewall/NetFlow logs)
  - How frequent? (Beacon pattern = malware C2)
  - What process is making the connection? (EDR → which process → parent process)

STEP 2 — ENRICH THE IOC
  - Look up destination IP in VirusTotal, Shodan, internal TIP
  - Is this IP on any blocklists / threat intel feeds?
  - Who owns this IP? (ASN lookup — cloud provider? VPS? suspicious ISP?)
  - Any other servers connecting to same IP?

STEP 3 — ASSESS SEVERITY
  - If IP is confirmed malicious → P1 Incident
  - If process is suspicious (unexpected parent, encoded cmdline) → P1 Incident
  - If legitimate business reason → close with documentation

STEP 4 — CONTAINMENT (if confirmed malicious)
  - Block destination IP at firewall immediately
  - Isolate server via EDR or VLAN change
  - Notify SOC Manager → P1 IR process
  - Preserve evidence: memory dump, disk image, full PCAP if possible

STEP 5 — INVESTIGATION
  - Determine initial access: How did malware get on server?
  - Timeline: When did it first connect? What happened before that?
  - Scope: Did it move laterally? Other systems affected?

STEP 6 — ERADICATION + RECOVERY
  - Remove malware, rebuild server from known-good image
  - Patch initial access vector
  - Update IDS/firewall rules to block this C2 pattern
```

---

## Q25: A user reports they can access a network share they shouldn't be able to. How do you investigate?

**Answer:**

*"First, I'd verify — have the user show me specifically what share they can access. Then I'd investigate from the network and identity layer:*

*Network layer:*
*- Is there a firewall rule that should be blocking this access? Check if rule exists, if it's applied to the right interface, and if it's ordered correctly (rules are first-match)*
*- Is the traffic going through the expected path? (Routing might send it through a different interface that has different rules)*

*Identity layer (with AD team):*
*- What groups is this user a member of?*
*- What group has access to that share?*
*- Is there a nested group that's granting access unexpectedly?*

*Common causes:*
*- VLAN misconfiguration — user is in VLAN that shouldn't reach the share server*
*- Firewall rule too broad — "any source" instead of specific subnet*
*- Missing deny rule — traffic flowing through path with no rule = permit by default in some configurations*
*- AD group misconfiguration (covered by IAM team)*

*Resolution: Tighten the rule with specific source IP/subnet, retest access, document the change."*

---

## Q26: The organization wants to implement network monitoring but there's encrypted traffic everywhere. How do you approach this?

**Answer:**

*"This is a very real challenge — the majority of traffic is now TLS encrypted. My layered approach:*

*What we CAN see without decryption:*
*- NetFlow/IPFIX metadata: who talks to whom, how much, when, duration (C2 beaconing visible)*
*- DNS queries: what domains are being resolved (even before connection is made)*
*- TLS metadata: Server Name Indication (SNI) shows which hostname without decryption, certificate info*
*- Connection patterns: new/rare external destinations, unusual ports, geographic anomalies*

*SSL/TLS Inspection (where feasible):*
*- Deploy on NGFW for general internet traffic — decrypt, inspect, re-encrypt*
*- Requires pushing internal CA cert to all managed devices*
*- Exclusion policy for: banking, healthcare, HR systems, certificate-pinned apps*
*- Legal and compliance review needed — employee privacy policies vary by region*

*EDR as complement:*
*- EDR sees the process making the connection, command line, file activity — even if network is encrypted*
*- Behavioral analysis doesn't require packet content*

*Recommendation: NetFlow + DNS monitoring + EDR covers 80% of what SSL inspection provides, with far less complexity and legal risk. Add SSL inspection for highest-risk segments (internet-facing servers, high-value user populations) selectively."*

---

# 🔵 BEHAVIORAL / SITUATIONAL QUESTIONS

---

## Q27: Tell me about a time you had to make a quick decision that affected the network.

**Framework (STAR):**

*"SITUATION: During an incident at [lab/previous role/internship], I identified what appeared to be ransomware lateral movement via SMB — I could see in [firewall/IDS logs] that one compromised machine was attempting connections to every other machine on the subnet using port 445.*

*TASK: Needed to decide whether to block all SMB traffic (would impact business operations) or try a targeted response.*

*ACTION: I escalated immediately to the SOC Manager — explained the evidence and my two options: (1) broad block affecting all file shares, or (2) isolate the specific compromised machine via VLAN change. Recommended option 2 as least-impact. Manager agreed. I implemented the VLAN change to isolate the machine within 3 minutes of escalation.*

*RESULT: Spread was contained to 3 machines. File servers were never affected. Business operations continued uninterrupted. Post-incident, I helped write a runbook for similar scenarios."*

---

## Q28: How do you explain firewall rule changes to non-technical stakeholders?

**Answer:**

*"I translate it to business language. Instead of 'We need to add a rule permitting TCP from subnet 10.1.2.0/24 to 10.3.0.5 on port 1433,' I say: 'The new Finance reporting application needs to connect to the Finance database. We need to open a specific pathway between those two systems — imagine a locked door between the two rooms. We're adding a door that only Finance systems can use, only to reach the database, and only for database traffic. All other traffic will still be blocked.'*

*For risk communication: 'This change is low risk because it's a minimal, specific permission between two internal, trusted systems — not to the internet. The alternative — not making the change — means the Finance app doesn't work, which impacts [business outcome].'*

*Approval documentation: I always attach the business justification, the risk assessment, and my recommended approval, so stakeholders can make an informed decision rather than just rubber-stamp."*

---

# ⚡ QUICK FIRE ROUND

| Question | Answer |
|----------|--------|
| What port does HTTP use? | 80 |
| What port does HTTPS use? | 443 |
| What port does SSH use? | 22 |
| What port does Telnet use? | 23 |
| What port does FTP data use? | 20 |
| What port does FTP control use? | 21 |
| What port does DNS use? | 53 (UDP + TCP) |
| What port does SMTP use? | 25 |
| What port does RDP use? | 3389 |
| What port does SMB use? | 445 (modern), 139 (legacy) |
| What port does LDAP use? | 389 |
| What port does LDAPS use? | 636 |
| What port does Kerberos use? | 88 |
| What port does SNMP use? | 161 (queries), 162 (traps) |
| What port does NTP use? | 123 |
| What port does DHCP use? | 67 (server), 68 (client) |
| What is the loopback address? | 127.0.0.1 (IPv4), ::1 (IPv6) |
| What is APIPA range? | 169.254.0.0/16 |
| What is a RFC1918 private range? | 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 |
| What is CIDR? | Classless Inter-Domain Routing — flexible subnet notation |
| What does uRPF do? | Unicast Reverse Path Forwarding — validates source IP by checking routing table |
| What is BCP38? | Network Ingress Filtering standard — prevents IP spoofing by ISPs |
| What is DAI? | Dynamic ARP Inspection — validates ARP packets against DHCP snooping table |
| What is 802.1X? | Port-based network access control — authenticate before getting network access |
| What is SPAN port? | Switched Port Analyzer — mirror port for passive traffic monitoring |
| What is TTL? | Time to Live — prevents infinite routing loops; decremented each hop |
| What does HSTS do? | Force HTTPS connections — browser refuses HTTP even if user types it |
| What is DANE? | DNS-Based Authentication of Named Entities — binds TLS cert to DNS |
| What is BGP? | Border Gateway Protocol — routing protocol between autonomous systems (internet) |
| What is OSPF? | Open Shortest Path First — interior routing protocol |
| What is a broadcast domain? | Network segment where broadcasts reach all hosts |
| What is a collision domain? | Network segment where collisions can occur (hub) |
| How many hosts in /24? | 254 usable (256 - network - broadcast) |
| How many hosts in /26? | 62 usable |
| How many hosts in /30? | 2 usable (point-to-point links) |
| What is gratuitous ARP? | ARP announcement not in response to a request — used in ARP poisoning |

---

> **💡 Network Security Interview Tips:**
> 1. Draw diagrams — when asked about architecture, offer to sketch it out. Interviewers love candidates who think visually
> 2. Always explain the "why" behind security controls — "we segment because lateral movement is the #1 post-compromise technique"
> 3. Know your port numbers cold — they come up in logs and interviews constantly
> 4. Reference real incidents (NotPetya, Colonial Pipeline) when discussing why controls matter — shows you understand real-world impact
> 5. Never say "just block everything" — always acknowledge the business needs vs security tradeoffs

