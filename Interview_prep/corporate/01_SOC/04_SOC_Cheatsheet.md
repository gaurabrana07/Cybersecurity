# ⚡ SOC ANALYST — QUICK REFERENCE CHEATSHEET

> **Use:** Night-before-interview review | Daily SOC reference | Quick lookup during investigations

---

## 🔐 CRITICAL WINDOWS EVENT IDs

| Event ID | What Happened | Key Use Case |
|----------|--------------|-------------|
| **4624** | Successful logon | Baseline tracking, anomaly detection |
| **4625** | Failed logon | Brute force detection |
| **4648** | Explicit credential logon | Pass-the-hash, credential abuse |
| **4663** | File object access | Data exfiltration |
| **4672** | Special privileges to logon | Privilege escalation |
| **4688** | New process created | Malware execution |
| **4697** | Service installed | Persistence |
| **4698** | Scheduled task created | Persistence |
| **4719** | Audit policy changed | Anti-forensics |
| **4720** | User account created | Backdoor account |
| **4728** | Member added to security group | Privilege escalation |
| **4776** | NTLM credential validation | Pass-the-hash, NTLM relay |
| **7045** | New service installed (System log) | Persistence |
| **1102** | Audit log cleared | Anti-forensics |

---

## 🌐 CRITICAL PORTS & PROTOCOLS

| Port | Protocol | Notes |
|------|----------|-------|
| 20/21 | FTP | Unencrypted file transfer (risk) |
| 22 | SSH | Encrypted remote access |
| 23 | Telnet | Unencrypted (never use) |
| 25 | SMTP | Email sending |
| 53 | DNS | C2 via DNS tunneling risk |
| 80 | HTTP | Unencrypted web |
| 88 | Kerberos | Authentication (AD) |
| 110 | POP3 | Email retrieval |
| 135 | RPC | Microsoft RPC (pivot point) |
| 139 | NetBIOS | Legacy SMB |
| 143 | IMAP | Email retrieval |
| 389 | LDAP | Directory services (AD) |
| 443 | HTTPS | Encrypted web |
| 445 | SMB | File sharing, Pass-the-hash vector |
| 636 | LDAPS | Encrypted LDAP |
| 1433 | MSSQL | Microsoft SQL Server |
| 3306 | MySQL | MySQL database |
| 3389 | RDP | Remote Desktop (major attack surface) |
| 4444 | Metasploit default | C2 indicator |
| 5985/5986 | WinRM | PowerShell remoting |
| 8080/8443 | HTTP/HTTPS alt | Common C2 ports |

---

## 🔍 MITRE ATT&CK TACTICS (in order)

```
1.  TA0043 - Reconnaissance
2.  TA0042 - Resource Development
3.  TA0001 - Initial Access
4.  TA0002 - Execution
5.  TA0003 - Persistence
6.  TA0004 - Privilege Escalation
7.  TA0005 - Defense Evasion
8.  TA0006 - Credential Access
9.  TA0007 - Discovery
10. TA0008 - Lateral Movement
11. TA0009 - Collection
12. TA0011 - Command and Control
13. TA0010 - Exfiltration
14. TA0040 - Impact
```

---

## 🎯 COMMON ATTACK → DETECTION MAPPING

| Attack | Key IOCs / Detection |
|--------|---------------------|
| **Phishing** | Suspicious sender, malicious URL/attachment, login from new IP |
| **Brute Force** | 10+ failed logins (Event 4625) from same IP in 5 min |
| **Pass-the-Hash** | NTLM Type 3 logon (4624) without prior password auth, Event 4648 |
| **Kerberoasting** | Many TGS requests (Event 4769) for service accounts |
| **Pass-the-Ticket** | Abnormal Kerberos ticket usage, unusual TGT reuse |
| **Golden Ticket** | KRBTGT hash used, ticket lifetime > domain policy |
| **Lateral Movement** | Workstation-to-workstation SMB, PsExec service (PSEXESVC), WMI |
| **C2 Beaconing** | Regular interval outbound connections, beacon jitter patterns |
| **Data Exfiltration** | Large outbound transfers, compression tools, cloud uploads |
| **Ransomware** | Mass file rename/encryption, shadow copy deletion (vssadmin) |
| **Privilege Escalation** | Event 4672, UAC bypass techniques, token impersonation |
| **Persistence** | New scheduled tasks (4698), registry run keys, new services (7045) |
| **Defense Evasion** | Log clearing (1102), disable security tools, timestomping |

---

## 🛠️ SOC TOOLS QUICK REFERENCE

| Category | Tool | Quick Note |
|----------|------|-----------|
| **SIEM** | Splunk | SPL queries, best ecosystem |
| **SIEM** | Microsoft Sentinel | KQL, cloud-native, Azure/M365 |
| **SIEM** | IBM QRadar | NetFlow analysis, strong correlation |
| **EDR** | CrowdStrike Falcon | Best detection rate, cloud-native |
| **EDR** | Microsoft Defender MDE | Deep Windows integration |
| **EDR** | SentinelOne | Autonomous response, rollback |
| **SOAR** | Palo Alto XSOAR | 600+ integrations |
| **SOAR** | Splunk SOAR | Tight Splunk integration |
| **TIP** | MISP | Open-source IOC sharing |
| **TIP** | Recorded Future | Premium threat intel |
| **Sandbox** | ANY.RUN | Interactive, free tier |
| **IOC Lookup** | VirusTotal | Multi-AV scan, reputation |
| **Network** | Wireshark | Packet capture analysis |
| **Network** | Zeek/Bro | Network traffic analysis |
| **Forensics** | Volatility | Memory forensics |
| **Forensics** | Autopsy | Disk forensics |
| **Tickets** | ServiceNow | Enterprise ITSM |
| **Vuln Mgmt** | Tenable/Nessus | Vulnerability scanning |

---

## 📊 INCIDENT SEVERITY QUICK CHART

| Level | Examples | Response SLA |
|-------|----------|-------------|
| **P1 Critical** | Ransomware active, Active data exfiltration, C2 established | 15 min |
| **P2 High** | Confirmed phishing with credential harvest, Lateral movement | 1 hour |
| **P3 Medium** | Failed brute force, Policy violation, Recon activity | 4 hours |
| **P4 Low** | Informational alerts, Minor violations | 24 hours |

---

## 🔄 INCIDENT RESPONSE — PICERL

```
P - Prepare    → Playbooks, tools, training ready
I - Identify   → Detect and validate the incident
C - Contain    → Short-term: isolate; Long-term: patch
E - Eradicate  → Remove malware, attacker access
R - Recover    → Restore, validate, return to normal
L - Lessons    → PIR, update playbooks, improve
```

---

## 🔍 ALERT TRIAGE — QUICK DECISION

```
ALERT RECEIVED
    ↓
Known FP pattern? → YES → Close (document reason) + tune rule if recurring
    ↓ NO
Asset critical? → YES → Escalate immediately
    ↓ Maybe
Enrich IOCs (VirusTotal, TIP)
    ↓
Malicious? → YES → True Positive → Escalate with evidence
    ↓ NO
Unusual behavior for asset? → YES → Escalate as suspicious
    ↓ NO
Benign True Positive → Close with explanation
```

---

## 🔑 AUTHENTICATION LOGON TYPES (Windows)

| Logon Type | Name | Notes |
|-----------|------|-------|
| 2 | Interactive | Local keyboard logon |
| 3 | Network | Mapped drive, UNC path |
| 4 | Batch | Scheduled tasks |
| 5 | Service | Service account logon |
| 7 | Unlock | Screen unlock |
| 8 | NetworkCleartext | Basic auth / IIS |
| 9 | NewCredentials | RunAs / PsExec |
| 10 | RemoteInteractive | RDP |
| 11 | CachedInteractive | Offline domain logon |

---

## 🧠 SPLUNK — KEY SPL COMMANDS

```splunk
index=<name>               # Select data source
| stats count by field     # Count grouped by field
| table field1 field2      # Show specific columns
| where count > 10         # Filter by condition
| sort -count              # Sort descending by count
| timechart count          # Graph over time
| eval newfield=expr       # Create calculated field
| rex field=field "regex"  # Extract with regex
| transaction src_ip       # Group events by IP into sessions
| dedup field              # Remove duplicates
| head 10                  # Show top 10 results
```

---

## 🧠 KQL (Microsoft Sentinel) — KEY COMMANDS

```kql
SecurityEvent                     // Table name
| where EventID == 4625           // Filter
| summarize count() by IpAddress  // Group/count
| order by count_ desc            // Sort
| project Time, User, IP          // Select columns
| take 10                         // Top 10
| extend field = expression       // Create field
| bin(TimeGenerated, 1h)          // Time bucketing
| join (OtherTable) on CommonField // Join tables
```

---

## 📋 KEY ACRONYMS

| Acronym | Meaning |
|---------|---------|
| SIEM | Security Information and Event Management |
| SOAR | Security Orchestration, Automation and Response |
| EDR | Endpoint Detection and Response |
| XDR | Extended Detection and Response |
| TIP | Threat Intelligence Platform |
| IOC | Indicator of Compromise |
| TTPs | Tactics, Techniques and Procedures |
| ATT&CK | Adversarial Tactics, Techniques and Common Knowledge |
| IR | Incident Response |
| DFIR | Digital Forensics and Incident Response |
| PIR | Post-Incident Review |
| UEBA | User and Entity Behavior Analytics |
| CMDB | Configuration Management Database |
| SLA | Service Level Agreement |
| EPS | Events Per Second |
| FP | False Positive |
| TP | True Positive |
| FN | False Negative |
| TN | True Negative |
| MTTD | Mean Time to Detect |
| MTTR | Mean Time to Respond |
| C2 | Command and Control |
| APT | Advanced Persistent Threat |
| TGT | Ticket Granting Ticket (Kerberos) |
| TGS | Ticket Granting Service (Kerberos) |
| NTLM | NT LAN Manager (authentication) |
| PTH | Pass the Hash |
| DLP | Data Loss Prevention |
| NSM | Network Security Monitoring |
| LotL | Living off the Land (attack technique) |
| MSSP | Managed Security Service Provider |
| NOC | Network Operations Center |
| CSIRT | Computer Security Incident Response Team |

---

## 🔥 MUST-KNOW MALWARE FAMILIES

| Family | Type | Notable For |
|--------|------|------------|
| **WannaCry** | Ransomware/Worm | EternalBlue exploit, global 2017 attack |
| **NotPetya** | Wiper/Ransomware | Most destructive cyberattack ever (\$10B) |
| **Emotet** | Banking Trojan/Loader | Modular, spam campaigns, loader for Ryuk |
| **Ryuk** | Ransomware | Targets enterprises, often via Emotet |
| **Cobalt Strike** | RAT/C2 Framework | Legitimate red team tool abused by attackers |
| **Mimikatz** | Credential Dumper | Dumps Windows credentials from LSASS |
| **Metasploit** | Exploit Framework | Attacker and defender tool |
| **LockBit** | Ransomware | Most prolific ransomware gang 2022-2024 |
| **ALPHV/BlackCat** | Ransomware | Rust-based, affiliate model |
| **Sunburst** | Backdoor | SolarWinds supply chain attack |

---

## 🎯 FRAMEWORKS AT A GLANCE

| Framework | What it is | Used for |
|-----------|-----------|---------|
| **MITRE ATT&CK** | TTPs knowledge base | Detection mapping, hunting, IR |
| **Cyber Kill Chain** | 7-phase attack model | Understanding attack progression |
| **Diamond Model** | Adversary-Infrastructure-Capability-Victim | Threat intel analysis |
| **NIST CSF** | Identify-Protect-Detect-Respond-Recover | Security program framework |
| **NIST 800-61** | IR guide | Incident response lifecycle |
| **ISO 27001** | ISMS standard | Security management certification |
| **PICERL** | IR mnemonic | Quick IR recall |

---

> **🔖 Print this page and keep it at your desk during your first 3 months in SOC.**

