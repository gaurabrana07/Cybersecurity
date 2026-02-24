# 🚨 INCIDENT RESPONSE & DIGITAL FORENSICS
## TCS HackQuest Interview Guide | HIGH PRIORITY

---

# 🎯 PRIORITY RATING: ⭐⭐⭐⭐ (HIGH)
> Core security skill - every security role involves incident handling

---

# 📋 TABLE OF CONTENTS

1. [Incident Response Fundamentals](#incident-response-fundamentals)
2. [NIST Incident Response Framework](#nist-incident-response-framework)
3. [Common Incident Types](#common-incident-types)
4. [Digital Forensics Basics](#digital-forensics-basics)
5. [Forensic Tools & Techniques](#forensic-tools--techniques)
6. [Evidence Handling](#evidence-handling)
7. [Incident Response Playbooks](#incident-response-playbooks)
8. [Interview Questions & Answers](#interview-questions--answers)

---

# INCIDENT RESPONSE FUNDAMENTALS

## What is Incident Response?

```
┌─────────────────────────────────────────────────────────────┐
│         INCIDENT RESPONSE DEFINITION                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Incident Response (IR) is the organized approach to        │
│  handling security breaches or attacks.                     │
│                                                             │
│  Goals:                                                     │
│  ├── Minimize damage                                        │
│  ├── Reduce recovery time and costs                         │
│  ├── Preserve evidence                                      │
│  └── Prevent future incidents                               │
│                                                             │
│  Security Event vs Incident:                                │
│  ├── Event: Any observable occurrence                       │
│  │   (login, file access, network connection)               │
│  │                                                          │
│  └── Incident: Event that threatens CIA                     │
│      (unauthorized access, malware, data breach)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Incident Severity Levels:

| Level | Description | Response Time | Example |
|-------|-------------|---------------|---------|
| **Critical** | Business-stopping, data breach | Immediate (15 min) | Ransomware, active breach |
| **High** | Significant impact, potential breach | 1 hour | Malware on critical server |
| **Medium** | Limited impact, contained | 4 hours | Phishing email, policy violation |
| **Low** | Minimal impact | Next business day | Failed login attempts |

---

# NIST INCIDENT RESPONSE FRAMEWORK

## Four Phases:

```
┌─────────────────────────────────────────────────────────────┐
│           NIST IR LIFECYCLE                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐                    ┌──────────────┐       │
│  │ 1.PREPARATION │◄──────────────────│4.POST-       │       │
│  │              │                    │  INCIDENT    │       │
│  └──────┬───────┘                    └──────▲───────┘       │
│         │                                   │               │
│         ▼                                   │               │
│  ┌──────────────┐                    ┌──────┴───────┐       │
│  │2.DETECTION & │──────────────────▶│3.CONTAINMENT│       │
│  │  ANALYSIS    │                    │ ERADICATION │       │
│  │              │                    │ RECOVERY    │       │
│  └──────────────┘                    └──────────────┘       │
│                                                             │
│              Continuous improvement loop                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Phase 1: PREPARATION

### Key Activities:
```
┌─────────────────────────────────────────────────────────────┐
│              PREPARATION PHASE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  People:                                                    │
│  ├── Establish IR team and roles                            │
│  ├── Train team members                                     │
│  ├── Define escalation procedures                           │
│  └── Establish communication channels                       │
│                                                             │
│  Processes:                                                 │
│  ├── Create IR policies and procedures                      │
│  ├── Develop playbooks for common incidents                 │
│  ├── Define severity levels                                 │
│  └── Legal and PR coordination                              │
│                                                             │
│  Technology:                                                │
│  ├── Logging infrastructure (SIEM)                          │
│  ├── Forensic tools ready                                   │
│  ├── Backup and recovery tested                             │
│  └── Communication tools (secure channels)                  │
│                                                             │
│  Jump Bag (IR Kit):                                         │
│  ├── Forensic workstation                                   │
│  ├── Write blockers                                         │
│  ├── External drives                                        │
│  ├── Documentation templates                                │
│  └── Contact lists                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Phase 2: DETECTION & ANALYSIS

### Detection Sources:
| Source | Examples |
|--------|----------|
| **SIEM** | Correlation alerts, anomalies |
| **EDR** | Endpoint alerts, process behavior |
| **IDS/IPS** | Network signatures |
| **User Reports** | Phishing, suspicious activity |
| **External** | Threat intel, vendor notifications |

### Analysis Steps:
```
1. Initial Triage
   └─ Is this a real incident or false positive?

2. Scoping
   └─ What systems/data are affected?

3. Evidence Collection
   └─ Preserve logs, memory, disk images

4. Timeline Construction
   └─ What happened and when?

5. IOC Identification
   └─ IPs, hashes, domains, behaviors
```

### Indicators of Compromise (IOCs):
```
┌─────────────────────────────────────────────────────────────┐
│              TYPES OF IOCs                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Network:                                                   │
│  ├── IP addresses                                           │
│  ├── Domain names                                           │
│  ├── URLs                                                   │
│  └── Network traffic patterns                               │
│                                                             │
│  Host:                                                      │
│  ├── File hashes (MD5, SHA256)                              │
│  ├── File names and paths                                   │
│  ├── Registry keys                                          │
│  ├── Process names                                          │
│  └── Services                                               │
│                                                             │
│  Email:                                                     │
│  ├── Sender addresses                                       │
│  ├── Subject lines                                          │
│  ├── Attachment hashes                                      │
│  └── Reply-to addresses                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Phase 3: CONTAINMENT, ERADICATION & RECOVERY

### Containment Strategies:

```
┌─────────────────────────────────────────────────────────────┐
│              CONTAINMENT STRATEGIES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SHORT-TERM CONTAINMENT (Immediate):                        │
│  ├── Isolate affected systems from network                  │
│  ├── Block malicious IPs/domains                            │
│  ├── Disable compromised accounts                           │
│  └── Preserve evidence before changes                       │
│                                                             │
│  LONG-TERM CONTAINMENT:                                     │
│  ├── Apply temporary fixes/patches                          │
│  ├── Remove attacker access                                 │
│  ├── Enhanced monitoring                                    │
│  └── Keep systems running if needed                         │
│                                                             │
│  Containment Decision Factors:                              │
│  ├── Need to preserve evidence?                             │
│  ├── Business impact of taking system down?                 │
│  ├── Risk of attacker destroying evidence?                  │
│  └── Legal requirements?                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Eradication:
- Remove malware/backdoors
- Close vulnerabilities exploited
- Reset compromised credentials
- Rebuild systems if necessary

### Recovery:
- Restore from clean backups
- Rebuild systems from known good images
- Gradual return to production
- Enhanced monitoring after recovery

## Phase 4: POST-INCIDENT

### Lessons Learned:
```
┌─────────────────────────────────────────────────────────────┐
│              POST-INCIDENT ACTIVITIES                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Lessons Learned Meeting (within 2 weeks):                  │
│  ├── What happened? (timeline)                              │
│  ├── What went well?                                        │
│  ├── What could be improved?                                │
│  ├── What actions to prevent recurrence?                    │
│  └── Assign owners and deadlines                            │
│                                                             │
│  Documentation:                                             │
│  ├── Incident report (detailed timeline)                    │
│  ├── Technical findings                                     │
│  ├── Business impact assessment                             │
│  └── Recommendations                                        │
│                                                             │
│  Improvements:                                               │
│  ├── Update playbooks                                       │
│  ├── Patch vulnerabilities                                  │
│  ├── Improve detection rules                                │
│  └── Update training                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# COMMON INCIDENT TYPES

## 1. Ransomware

```
┌─────────────────────────────────────────────────────────────┐
│              RANSOMWARE RESPONSE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DETECTION:                                                 │
│  ├── Multiple files encrypted in short time                 │
│  ├── Ransom notes appearing                                 │
│  ├── Known ransomware file extensions                       │
│  └── Mass file renames                                      │
│                                                             │
│  IMMEDIATE ACTIONS:                                         │
│  1. Isolate affected systems IMMEDIATELY                    │
│  2. Don't turn off systems (evidence in memory)             │
│  3. Identify ransomware variant (No More Ransom project)    │
│  4. Preserve ransom note (has decryption instructions)      │
│  5. Check backup integrity                                  │
│                                                             │
│  DO NOT:                                                    │
│  ✗ Pay ransom (no guarantee, funds criminals)              │
│  ✗ Delete encrypted files                                  │
│  ✗ Run antivirus immediately (can delete encryption key)   │
│                                                             │
│  RECOVERY:                                                  │
│  ├── Restore from clean backups                             │
│  ├── Check for decryption tools (NoMoreRansom.org)          │
│  ├── Rebuild affected systems                               │
│  └── Patch entry point vulnerability                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 2. Phishing Compromise

```
Detection → Scope → Contain → Eradicate → Recover

1. User reports phishing email
2. Check if link was clicked
3. Check if credentials entered
4. If credentials entered:
   - Reset password immediately
   - Terminate all sessions
   - Enable MFA
   - Check for unauthorized access
   - Check for forwarding rules
5. Block sender and similar emails
6. Notify other potential recipients
```

## 3. Data Breach

```
┌─────────────────────────────────────────────────────────────┐
│              DATA BREACH RESPONSE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. IDENTIFY SCOPE:                                         │
│     ├── What data was accessed?                             │
│     ├── How many records?                                   │
│     ├── What type of data (PII, PHI, financial)?           │
│     └── Over what time period?                              │
│                                                             │
│  2. LEGAL/COMPLIANCE:                                       │
│     ├── Notify legal team immediately                       │
│     ├── Determine notification requirements                 │
│     │   GDPR: 72 hours to authority                         │
│     │   HIPAA: 60 days to individuals                       │
│     └── Preserve evidence for investigation                 │
│                                                             │
│  3. INVESTIGATION:                                          │
│     ├── How did breach occur?                               │
│     ├── Was it insider or external?                         │
│     ├── Is attacker still present?                          │
│     └── Document everything                                 │
│                                                             │
│  4. NOTIFICATION:                                           │
│     ├── Notify affected individuals                         │
│     ├── Offer credit monitoring if appropriate              │
│     └── Prepare public statement if needed                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 4. Insider Threat

```
Key Challenges:
- May have legitimate access
- Need to balance privacy with security
- Often involves HR and legal

Response:
1. Involve HR/Legal before confrontation
2. Preserve evidence quietly
3. Monitor without tipping off
4. Document all activities
5. Coordinate termination/action with HR
```

---

# DIGITAL FORENSICS BASICS

## What is Digital Forensics?

```
┌─────────────────────────────────────────────────────────────┐
│              DIGITAL FORENSICS                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  The process of collecting, preserving, analyzing, and      │
│  presenting digital evidence in a legally admissible way.   │
│                                                             │
│  Types:                                                     │
│  ├── Computer Forensics (disks, files)                      │
│  ├── Network Forensics (packets, logs)                      │
│  ├── Memory Forensics (RAM analysis)                        │
│  ├── Mobile Forensics (phones, tablets)                     │
│  └── Cloud Forensics (cloud artifacts)                      │
│                                                             │
│  Key Principles:                                            │
│  ├── Evidence Integrity (don't modify)                      │
│  ├── Chain of Custody (document handling)                   │
│  ├── Documentation (every action recorded)                  │
│  └── Repeatability (results can be reproduced)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Order of Volatility:

Collect evidence in order from most volatile to least:

```
Most Volatile (Collect First)
        │
        ▼
┌───────────────────┐
│  1. CPU Registers │  ← Nanoseconds
├───────────────────┤
│  2. CPU Cache     │  ← Nanoseconds
├───────────────────┤
│  3. RAM           │  ← Power loss = gone
├───────────────────┤
│  4. Network state │  ← Connections change
├───────────────────┤
│  5. Running procs │  ← Can terminate
├───────────────────┤
│  6. Disk          │  ← More stable
├───────────────────┤
│  7. Floppies/USB  │  ← Removable
├───────────────────┤
│  8. CD/DVD        │  ← Read-only
├───────────────────┤
│  9. Printouts     │  ← Physical
├───────────────────┤
│  10. Archives     │  ← Off-site backups
└───────────────────┘
        │
        ▼
Least Volatile (Collect Last)
```

## Forensic Acquisition:

### Types of Images:
| Type | Description | When to Use |
|------|-------------|-------------|
| **Physical** | Bit-by-bit copy of entire disk | Full investigation |
| **Logical** | Copy of files and folders | Quick analysis |
| **Memory** | RAM dump | Malware analysis |
| **Triage** | Targeted artifacts | Rapid response |

### Forensic Imaging Process:
```
1. Document original state (photos)
2. Connect via write-blocker
3. Calculate source hash (MD5/SHA256)
4. Create forensic image
5. Calculate image hash
6. Verify hashes match
7. Document chain of custody
```

---

# FORENSIC TOOLS & TECHNIQUES

## Disk Forensics Tools:

| Tool | Purpose | Type |
|------|---------|------|
| **FTK Imager** | Imaging, preview | Free |
| **EnCase** | Full forensic suite | Commercial |
| **Autopsy** | Analysis platform | Open Source |
| **dd/dc3dd** | Linux imaging | Free |
| **Sleuth Kit** | Command-line tools | Open Source |

## Memory Forensics:

### Volatility Framework (Most Important):

```bash
# Identify OS profile
volatility -f memory.dump imageinfo

# List processes
volatility -f memory.dump --profile=Win10x64 pslist

# Find hidden processes
volatility -f memory.dump --profile=Win10x64 psscan

# Network connections
volatility -f memory.dump --profile=Win10x64 netscan

# Command history
volatility -f memory.dump --profile=Win10x64 cmdscan

# Check for injected code
volatility -f memory.dump --profile=Win10x64 malfind
```

### What Memory Analysis Reveals:
- Running processes (including hidden)
- Network connections
- Loaded DLLs
- Open files
- Registry keys
- Command history
- Encryption keys
- Malware artifacts

## Network Forensics:

### Tools:
| Tool | Purpose |
|------|---------|
| **Wireshark** | Packet analysis |
| **tcpdump** | Command-line capture |
| **NetworkMiner** | Artifact extraction |
| **Zeek (Bro)** | Network monitoring |

### Key Network Artifacts:
```
- Pcap files (packet captures)
- Firewall logs
- Proxy logs
- DNS query logs
- NetFlow data
- VPN logs
```

## Log Analysis:

### Important Logs (Windows):
```
Security.evtx    - Logins, logoffs, permissions
System.evtx      - System events, services
Application.evtx - Application errors
PowerShell logs  - Script execution
```

### Important Logs (Linux):
```
/var/log/auth.log    - Authentication
/var/log/syslog      - System messages
/var/log/apache2/    - Web server
/var/log/secure      - Security events
~/.bash_history      - Command history
```

### Log Analysis Tools:
- Splunk
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Graylog
- grep/awk/sed (command line)

---

# EVIDENCE HANDLING

## Chain of Custody:

```
┌─────────────────────────────────────────────────────────────┐
│              CHAIN OF CUSTODY                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Documentation of evidence handling from collection to      │
│  presentation, ensuring integrity and admissibility.        │
│                                                             │
│  Must Record:                                               │
│  ├── Who collected evidence                                 │
│  ├── When (date/time)                                       │
│  ├── Where (location)                                       │
│  ├── How (method/tools)                                     │
│  ├── Why (case reference)                                   │
│  └── Every transfer of evidence                             │
│                                                             │
│  Example Form:                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Evidence ID: EVD-2026-0001                           │   │
│  │ Description: Dell Laptop, Serial: ABC123             │   │
│  │ Collected by: John Smith                             │   │
│  │ Date/Time: 2026-02-24 14:30                         │   │
│  │ Location: Server Room B-203                          │   │
│  │ Hash: SHA256:abc123...                              │   │
│  │                                                      │   │
│  │ Transfer Log:                                        │   │
│  │ 14:30 Collected by J.Smith → Lab                    │   │
│  │ 15:00 Received by M.Jones (Forensics)               │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Evidence Integrity:

### Hashing:
```bash
# Calculate hash before and after to prove integrity
md5sum evidence.dd > evidence.md5
sha256sum evidence.dd > evidence.sha256

# Verify integrity
md5sum -c evidence.md5
sha256sum -c evidence.sha256
```

### Write Blockers:
- Hardware devices that prevent writes to source media
- Ensure evidence is not modified during acquisition
- Required for legal admissibility

---

# INCIDENT RESPONSE PLAYBOOKS

## Playbook: Malware Infection

```
┌─────────────────────────────────────────────────────────────┐
│         MALWARE INCIDENT PLAYBOOK                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SEVERITY: High                                             │
│  TIME TO RESPOND: 1 hour                                    │
│                                                             │
│  1. INITIAL TRIAGE (15 min)                                 │
│     □ Confirm malware presence                              │
│     □ Identify affected system(s)                           │
│     □ Note malware indicators (file, hash, behavior)        │
│                                                             │
│  2. CONTAINMENT (30 min)                                    │
│     □ Isolate system from network                           │
│     □ Block malware C2 IPs/domains at firewall              │
│     □ Preserve memory dump (if possible)                    │
│     □ Create disk image                                     │
│                                                             │
│  3. ANALYSIS (2-4 hours)                                    │
│     □ Submit sample to sandbox (Any.run, VirusTotal)        │
│     □ Check hash on threat intel platforms                  │
│     □ Identify malware family and capabilities              │
│     □ Determine lateral movement                            │
│     □ Check other endpoints for IOCs                        │
│                                                             │
│  4. ERADICATION                                             │
│     □ Run AV scan in safe mode                              │
│     □ Remove malware artifacts                              │
│     □ Check persistence mechanisms                          │
│     □ Rebuild if unable to clean                            │
│                                                             │
│  5. RECOVERY                                                │
│     □ Restore from known good backup                        │
│     □ Install patches                                       │
│     □ Reset credentials if needed                           │
│     □ Monitor for re-infection                              │
│                                                             │
│  6. POST-INCIDENT                                           │
│     □ Document timeline                                     │
│     □ Update detection rules                                │
│     □ Share IOCs                                           │
│     □ Conduct lessons learned                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Playbook: Credential Compromise

```
1. IDENTIFY
   □ Which credential was compromised?
   □ How was it compromised (phishing, breach, reuse)?
   □ When did compromise occur?

2. CONTAIN
   □ Disable/reset compromised credential
   □ Terminate active sessions
   □ Enable MFA if not already

3. INVESTIGATE
   □ Review authentication logs
   □ Check for unauthorized access
   □ Look for data access/exfiltration
   □ Check for persistence (new accounts, keys)

4. REMEDIATE
   □ Reset related passwords
   □ Review access permissions
   □ Check for lateral movement
   □ Update security controls

5. RECOVER
   □ Restore normal access
   □ Enhanced monitoring for 30 days
   □ User awareness training
```

---

# INTERVIEW QUESTIONS & ANSWERS

---

## Q1: "Walk me through how you would handle a ransomware incident."

### ✅ MODEL ANSWER:
> "I would follow the NIST incident response framework:
>
> **1. Detection (First 15 minutes)**
> - Confirm ransomware (check ransom note, file extensions)
> - Identify affected systems
> - Note the variant if possible
>
> **2. Containment (Immediate)**
> - **Isolate affected systems** from network immediately
> - Don't turn them off (evidence in memory)
> - Block malicious IPs/domains at firewall
> - Disable affected accounts
>
> **3. Investigation**
> - Identify patient zero (first infected system)
> - Determine entry vector (phishing, RDP, exploit)
> - Check for lateral movement
> - Assess data exfiltration (double extortion trend)
>
> **4. Eradication**
> - Check NoMoreRansom.org for decryptor
> - Remove malware and persistence mechanisms
> - Patch the vulnerability exploited
>
> **5. Recovery**
> - Restore from clean backups (test backup integrity first)
> - Rebuild systems from known good images
> - Gradual reconnection with monitoring
>
> **6. Post-Incident**
> - Document timeline and actions
> - Lessons learned meeting
> - Improve detection rules
> - Consider reporting to authorities
>
> **Key decision: Don't pay ransom** - no guarantee of decryption, funds criminal operations."

---

## Q2: "What is the order of volatility and why is it important?"

### ✅ MODEL ANSWER:
> "Order of volatility refers to collecting evidence from most volatile (easily lost) to least volatile.
>
> **Order (Most to Least Volatile):**
>
> 1. **CPU Registers/Cache** - Nanoseconds
> 2. **RAM** - Lost on power off
> 3. **Network Connections** - Can disconnect
> 4. **Running Processes** - Can terminate
> 5. **Disk** - Relatively stable
> 6. **Removable Media** - Can be removed
> 7. **Backups/Archives** - Most stable
>
> **Why It Matters:**
>
> **Example - Investigating malware:**
> If I turn off the computer first:
> - Memory dump lost - can't see running malware
> - Network connections lost - can't see C2 server
> - Decryption keys lost - can't recover ransomware key
>
> **Correct approach:**
> 1. First: Capture memory (live acquisition)
> 2. Then: Capture running processes, network state
> 3. Then: Create disk image
> 4. Finally: Power off and preserve
>
> This is why in my ransomware answer I said 'don't turn off systems' - preserving volatile evidence is critical."

---

## Q3: "How would you preserve evidence during a security incident?"

### ✅ MODEL ANSWER:
> "Evidence preservation follows forensic principles:
>
> **1. Don't Modify the Original**
> - Use write blockers for disk access
> - Work on copies, not originals
> - Document original state (photos)
>
> **2. Proper Acquisition**
> ```
> Memory: Use tools like FTK Imager, DumpIt
> Disk: Create bit-by-bit forensic image
> Logs: Export to secure storage immediately
> ```
>
> **3. Hash Everything**
> ```bash
> # Calculate hash before any analysis
> sha256sum evidence.img > evidence.sha256
> 
> # Verify after any operation
> sha256sum -c evidence.sha256
> ```
>
> **4. Chain of Custody**
> - Document who handled evidence
> - When it was transferred
> - Where it's stored
> - Every action taken
>
> **5. Secure Storage**
> - Locked cabinet or safe
> - Access controls
> - Environmental controls
>
> **Example:**
> ```
> Collection: Image created by J.Smith at 14:30
> Hash: SHA256:abc123...
> Transfer: To forensic lab at 15:00
> Storage: Evidence locker #7
> ```
>
> This ensures evidence is admissible if legal action is needed."

---

## Q4: "What forensic artifacts would you examine on a Windows system?"

### ✅ MODEL ANSWER:
> "I would examine artifacts in order of importance for the investigation:
>
> **User Activity:**
> - Recent files (C:\\Users\\*\\Recent)
> - Prefetch (C:\\Windows\\Prefetch) - execution history
> - Jump lists - recently accessed files
> - Browser history
> - USB device history
>
> **System Activity:**
> - Event logs (Security, System, Application)
> - Registry (SAM, SYSTEM, SOFTWARE, NTUSER.DAT)
> - Scheduled tasks
> - Services
>
> **Persistence Mechanisms:**
> - Run/RunOnce registry keys
> - Startup folder
> - Scheduled tasks
> - Services
> - WMI subscriptions
>
> **Network Activity:**
> - DNS cache
> - ARP cache
> - Network connections (netstat)
> - Firewall logs
>
> **Malware Indicators:**
> - Suspicious executables
> - DLLs in unusual locations
> - Processes running from temp folders
> - Encoded PowerShell commands
>
> **Key Registry Locations:**
> ```
> HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
> HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
> HKLM\\SYSTEM\\CurrentControlSet\\Services
> ```
>
> Tools I'd use: Autopsy, Volatility, Registry Explorer, Event Log Explorer."

---

## Q5: "Explain the difference between live forensics and dead forensics."

### ✅ MODEL ANSWER:
> "**Live (Online) Forensics:**
> - System is running
> - Can capture volatile data (RAM, processes, connections)
> - Risk of evidence alteration
> - Time-sensitive
>
> **Dead (Offline) Forensics:**
> - System is powered off
> - Work on disk images
> - No volatile data available
> - More controlled environment
>
> **When to Use Each:**
>
> | Situation | Approach | Reason |
> |-----------|----------|--------|
> | Ransomware | Live first | Preserve memory, encryption keys |
> | Insider theft | Careful live | Don't alert suspect |
> | Malware analysis | Live → Dead | Get memory, then full disk |
> | Post-incident | Dead | System already off |
>
> **Live Forensics Process:**
> 1. Memory dump first (most volatile)
> 2. Running processes
> 3. Network connections
> 4. Open files/handles
> 5. Then disk imaging
>
> **Dead Forensics Process:**
> 1. Connect via write blocker
> 2. Hash original disk
> 3. Create bit-by-bit image
> 4. Verify hash
> 5. Analyze image copy
>
> In most incidents, I'd use a **hybrid approach** - collect live data first, then power off and do full disk analysis."

---

## Q6: "What is Volatility and how would you use it?"

### ✅ MODEL ANSWER:
> "Volatility is an open-source memory forensics framework for analyzing RAM dumps.
>
> **Key Capabilities:**
>
> **Process Analysis:**
> ```bash
> # List processes
> volatility -f mem.dump --profile=Win10x64 pslist
> 
> # Find hidden processes
> volatility -f mem.dump --profile=Win10x64 psscan
> 
> # Process tree
> volatility -f mem.dump --profile=Win10x64 pstree
> ```
>
> **Malware Detection:**
> ```bash
> # Find injected code
> volatility -f mem.dump --profile=Win10x64 malfind
> 
> # Check DLLs
> volatility -f mem.dump --profile=Win10x64 dlllist
> ```
>
> **Network Analysis:**
> ```bash
> # Active connections
> volatility -f mem.dump --profile=Win10x64 netscan
> ```
>
> **User Activity:**
> ```bash
> # Command history
> volatility -f mem.dump --profile=Win10x64 cmdscan
>
> # Console input/output
> volatility -f mem.dump --profile=Win10x64 consoles
> ```
>
> **Workflow:**
> 1. Identify profile: `volatility imageinfo`
> 2. List processes: look for suspicious names/paths
> 3. Check network connections: unusual external IPs
> 4. Look for injection: malfind for code injection
> 5. Extract suspicious files: for further analysis
>
> I've used similar analysis thinking in my vulnerability scanner - looking for patterns that indicate malicious activity."

---

## Q7: "How would you investigate a phishing incident?"

### ✅ MODEL ANSWER:
> "I would follow this process:
>
> **1. Initial Report**
> - Get original email (with full headers)
> - Note if user clicked or entered credentials
>
> **2. Email Analysis**
> ```
> Check headers:
> - Received path (where it actually came from)
> - SPF/DKIM/DMARC results
> - Return-Path vs From mismatch
> 
> Check content:
> - Links (hover, don't click)
> - Attachments (submit to sandbox)
> - Urgency language
> ```
>
> **3. Scope Assessment**
> - Check email gateway for similar emails
> - How many users received it?
> - Who clicked?
> - Who submitted credentials?
>
> **4. Containment**
> ```
> If credentials entered:
> - Reset password immediately
> - Force logout all sessions
> - Enable MFA
> - Check for unauthorized access
> - Check for mailbox rules (forwarding)
> 
> For all recipients:
> - Delete email
> - Block sender domain
> - Block phishing URL
> ```
>
> **5. Investigation (if credentials compromised)**
> - Review authentication logs
> - Check for data access
> - Look for lateral movement
> - Check for persistence
>
> **6. Post-Incident**
> - User awareness notification
> - Add IOCs to detection systems
> - Update email filters
>
> I'd use tools like: Email gateway logs, AD/Azure AD sign-in logs, PhishTank, VirusTotal, URL scanning services."

---

## Q8: "What metrics would you use to measure incident response effectiveness?"

### ✅ MODEL ANSWER:
> "I would track both time-based and quality metrics:
>
> **Time Metrics:**
>
> | Metric | Definition | Target |
> |--------|------------|--------|
> | **MTTD** | Mean Time To Detect | Minimize |
> | **MTTA** | Mean Time To Acknowledge | < 15 min |
> | **MTTC** | Mean Time To Contain | Severity-based |
> | **MTTR** | Mean Time To Resolve | Severity-based |
>
> **Quality Metrics:**
>
> - **False Positive Rate**: % of alerts that aren't real
> - **Escalation Accuracy**: % correctly escalated
> - **Repeat Incidents**: Same root cause recurring
> - **Post-Incident Actions**: % completed on time
>
> **Volume Metrics:**
>
> - Incidents by severity
> - Incidents by type
> - Incidents by source
> - Incidents by business unit
>
> **Example Dashboard:**
> ```
> This Month:
> ├── Total Incidents: 45
> │   ├── Critical: 2 (MTTR: 4 hours)
> │   ├── High: 8 (MTTR: 12 hours)
> │   ├── Medium: 20 (MTTR: 3 days)
> │   └── Low: 15 (MTTR: 5 days)
> │
> ├── MTTD: 2.5 hours (↓ from 4 hours)
> ├── False Positive Rate: 23%
> └── Repeat Incidents: 3 (need root cause)
> ```
>
> These metrics help identify where to improve - high MTTD might mean better detection tools needed, high repeat incidents mean root causes aren't being addressed."

---

## Q9: "How would you handle a situation where you suspect an insider threat?"

### ✅ MODEL ANSWER:
> "Insider threats require a careful, coordinated approach:
>
> **1. Initial Suspicion**
> - Don't confront or alert the suspect
> - Document observations
> - Involve HR and Legal immediately
>
> **2. Authorization**
> - Get written approval for investigation
> - Define scope and boundaries
> - Ensure legal compliance (privacy laws)
>
> **3. Covert Investigation**
> ```
> Monitor (without detection):
> - Email activity (with legal approval)
> - File access patterns
> - Network traffic
> - Badge access logs
> - Working hours
> ```
>
> **4. Evidence Collection**
> - Preserve logs before they rotate
> - Document everything
> - Maintain chain of custody
> - Keep evidence secure
>
> **5. Analysis**
> - Timeline of suspicious activities
> - Data accessed or copied
> - External communications
> - Financial indicators
>
> **6. Coordination**
> - HR for employment implications
> - Legal for advice and potential prosecution
> - Management for business decisions
> - Possibly law enforcement
>
> **Key Principles:**
> - Confidentiality - only need-to-know
> - Legal compliance - privacy laws matter
> - Objectivity - follow evidence, not assumptions
> - Documentation - assume it may go to court
>
> **Do NOT:**
> - Confront without HR/Legal
> - Access personal accounts without approval
> - Share suspicions widely
> - Make accusations without evidence"

---

## Q10: "What is the incident response team structure?"

### ✅ MODEL ANSWER:
> "A typical IR team includes these roles:
>
> **Core Team:**
>
> | Role | Responsibilities |
> |------|-----------------|
> | **IR Manager** | Overall coordination, decisions |
> | **Triage Analyst** | Initial alert review, severity |
> | **Forensic Analyst** | Evidence collection, analysis |
> | **Malware Analyst** | Reverse engineering, IOC extraction |
> | **Threat Intel** | Context, attribution, IOC enrichment |
>
> **Extended Team:**
>
> | Role | When Engaged |
> |------|--------------|
> | **Legal** | Data breach, compliance, prosecution |
> | **HR** | Insider threats, employee impact |
> | **Communications/PR** | Public disclosure, customer notification |
> | **IT Operations** | System recovery, patching |
> | **Business Owners** | Impact assessment, priorities |
> | **Executive Sponsor** | High-severity decisions, resources |
>
> **RACI for Critical Incident:**
> ```
> R - Responsible  A - Accountable  C - Consulted  I - Informed
>
> Activity         IR Lead  Analyst  Legal  Exec
> ─────────────────────────────────────────────────
> Detection           A        R       I      I
> Containment         A        R       C      I
> Investigation       A        R       C      I
> Notification        A        C       R      A
> Recovery            C        R       I      I
> Lessons Learned     R        C       C      I
> ```
>
> For smaller organizations, roles may be combined, but separation of duties should be maintained where possible."

---

# 📋 INCIDENT RESPONSE QUICK REFERENCE

## First 30 Minutes Checklist:
```
□ Confirm incident (not false positive)
□ Document initial observations
□ Determine severity
□ Notify IR manager/team
□ Begin containment if needed
□ Start evidence preservation
□ Open incident ticket
□ Begin timeline documentation
```

## Key Phone Numbers Template:
```
IR Manager: _______________
Security Team Lead: _______________
Legal Contact: _______________
HR Contact: _______________
IT Operations: _______________
Executive Sponsor: _______________
External IR Firm: _______________
Law Enforcement: _______________
```

---

**Document Created**: February 2026
**Priority**: ⭐⭐⭐⭐ HIGH - Core security skill
