# 🛡️ SOC OPERATIONS & SECURITY MONITORING
## TCS HackQuest Interview Guide | MEDIUM-HIGH PRIORITY

---

# 🎯 PRIORITY RATING: ⭐⭐⭐⭐ (HIGH)
> TCS has large SOC operations for clients - very relevant

---

# 📋 TABLE OF CONTENTS

1. [SOC Overview](#soc-overview)
2. [SOC Roles & Tiers](#soc-roles--tiers)
3. [SIEM Technology](#siem-technology)
4. [Log Management](#log-management)
5. [Alert Triage](#alert-triage)
6. [Threat Hunting](#threat-hunting)
7. [SOC Tools & Technologies](#soc-tools--technologies)
8. [Interview Questions & Answers](#interview-questions--answers)

---

# SOC OVERVIEW

## What is a Security Operations Center?

```
┌─────────────────────────────────────────────────────────────┐
│              SECURITY OPERATIONS CENTER (SOC)               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A centralized facility where security professionals        │
│  monitor, detect, analyze, and respond to cybersecurity     │
│  events using tools, processes, and human expertise.        │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                    SOC Functions                      │  │
│  │                                                       │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐     │  │
│  │  │MONITOR  │ │ DETECT  │ │ ANALYZE │ │ RESPOND │     │  │
│  │  │ 24/7    │→│ Alerts  │→│ Triage  │→│ Action  │     │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘     │  │
│  │                                                       │  │
│  │            SIEM │ EDR │ SOAR │ Threat Intel          │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## SOC Models:

| Model | Description | Pros | Cons |
|-------|-------------|------|------|
| **In-house** | Internal SOC team | Full control, deep knowledge | Expensive, 24/7 staffing |
| **MSSP** | Outsourced to provider | Cost-effective, expertise | Less control, context |
| **Hybrid** | Mix of internal + MSSP | Balanced | Coordination needed |
| **Virtual** | Remote analysts | Flexible | Communication challenges |

## SOC Maturity Levels:

```
Level 1: REACTIVE
├── Basic monitoring
├── Signature-based detection
└── Incident response only

Level 2: PROACTIVE  
├── Log correlation
├── Vulnerability management
├── Threat intelligence integration

Level 3: OPTIMIZED
├── Advanced analytics
├── Threat hunting
├── Automation (SOAR)

Level 4: ADAPTIVE
├── AI/ML integration
├── Predictive capabilities
└── Continuous improvement
```

---

# SOC ROLES & TIERS

## SOC Tier Structure:

```
┌─────────────────────────────────────────────────────────────┐
│                    SOC TIER MODEL                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                     ┌─────────────┐                         │
│                     │   TIER 3    │                         │
│                     │ Expert/Hunt │                         │
│                     │   (2-3)     │                         │
│                     └──────┬──────┘                         │
│                            │                                │
│              ┌─────────────┴─────────────┐                  │
│              │          TIER 2           │                  │
│              │    Incident Responder     │                  │
│              │         (4-6)             │                  │
│              └─────────────┬─────────────┘                  │
│                            │                                │
│         ┌──────────────────┴──────────────────┐             │
│         │              TIER 1                 │             │
│         │       Security Analyst / Triage     │             │
│         │            (8-12 per shift)         │             │
│         └─────────────────────────────────────┘             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Tier Responsibilities:

### Tier 1 - Security Analyst (Triage)

```
Responsibilities:
├── Monitor SIEM alerts 24/7
├── Initial alert triage
├── Classify true/false positives
├── Basic investigation
├── Escalate to Tier 2 if needed
├── Create tickets
├── Follow playbooks/runbooks
└── Basic remediation

Skills Required:
├── Security fundamentals
├── SIEM query basics
├── Networking (TCP/IP, ports)
├── Operating systems (Windows/Linux)
└── Analytical thinking
```

### Tier 2 - Incident Responder

```
Responsibilities:
├── Deep-dive investigation
├── Complex alert analysis
├── Incident response
├── Malware analysis (basic)
├── Threat hunting (reactive)
├── Develop detection rules
├── Mentor Tier 1 analysts
└── Escalate to Tier 3 if needed

Skills Required:
├── Advanced SIEM skills
├── Forensics basics
├── Scripting (Python, PowerShell)
├── Advanced networking
├── Malware analysis fundamentals
└── Incident handling experience
```

### Tier 3 - Expert/Threat Hunter

```
Responsibilities:
├── Advanced threat hunting
├── Malware reverse engineering
├── Advanced forensics
├── Detection engineering
├── Red team coordination
├── Tool development
├── Research & innovation
└── Process improvement

Skills Required:
├── Expert-level security knowledge
├── Advanced programming
├── Reverse engineering
├── Threat intelligence
├── Incident response leadership
└── Research skills
```

## Additional SOC Roles:

| Role | Responsibility |
|------|----------------|
| **SOC Manager** | Team leadership, metrics, reporting |
| **Threat Intel Analyst** | IOC collection, threat analysis |
| **Detection Engineer** | Rule creation, tuning, SIEM admin |
| **Purple Team** | Red+Blue coordination, gap assessment |
| **Automation Engineer** | SOAR development, process automation |

---

# SIEM TECHNOLOGY

## What is SIEM?

```
┌─────────────────────────────────────────────────────────────┐
│     SECURITY INFORMATION & EVENT MANAGEMENT (SIEM)          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SIEM = SIM (Security Information Management)               │
│       + SEM (Security Event Management)                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                 SIEM Architecture                    │   │
│  │                                                      │   │
│  │  Log Sources → Collection → Normalization →         │   │
│  │  Correlation → Alerting → Investigation             │   │
│  │                                                      │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │ Servers  │  │ Network  │  │  Cloud   │          │   │
│  │  │ Windows  │  │ Firewall │  │  AWS     │          │   │
│  │  │ Linux    │  │ IDS/IPS  │  │  Azure   │          │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘          │   │
│  │       │             │             │                 │   │
│  │       └─────────────┼─────────────┘                 │   │
│  │                     ▼                               │   │
│  │              ┌──────────────┐                       │   │
│  │              │     SIEM     │                       │   │
│  │              │  Correlation │                       │   │
│  │              │   Alerting   │                       │   │
│  │              └──────────────┘                       │   │
│  │                     │                               │   │
│  │                     ▼                               │   │
│  │              ┌──────────────┐                       │   │
│  │              │   Analyst    │                       │   │
│  │              │   Console    │                       │   │
│  │              └──────────────┘                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Major SIEM Platforms:

### 1. Splunk

```
Key Features:
├── Powerful search (SPL - Search Processing Language)
├── Dashboards & visualizations
├── Splunk Enterprise Security (ES) add-on
├── Machine learning capabilities
├── Extensive integrations

SPL Query Examples:
# Find failed logins
index=windows EventCode=4625 | stats count by src_ip

# Look for PowerShell execution
index=windows EventCode=4104 | table _time, ScriptBlockText

# Network connections to unusual ports
index=network dest_port>10000 | stats count by dest_ip, dest_port
```

### 2. Microsoft Sentinel (Cloud-native)

```
Key Features:
├── Azure-native SIEM
├── Built-in AI and automation
├── KQL (Kusto Query Language)
├── Integration with Microsoft 365 Defender
├── SOAR capabilities built-in

KQL Query Examples:
// Failed sign-ins
SigninLogs
| where ResultType != 0
| summarize count() by UserPrincipalName, IPAddress

// Suspicious PowerShell
SecurityEvent
| where EventID == 4688
| where CommandLine has "powershell" and CommandLine has "-enc"
```

### 3. ELK Stack (Elastic)

```
Components:
├── Elasticsearch - Storage & search
├── Logstash - Log processing
├── Kibana - Visualization
├── Beats - Log shipping agents

Open Source Option:
├── Free to use
├── Large community
├── Security add-on (paid for some features)

Query Examples (Lucene):
event.code:4625 AND winlog.event_data.Status:0xc000006d
process.name:powershell.exe AND process.command_line:*-enc*
```

### 4. Other SIEM Solutions:

| Product | Type | Notes |
|---------|------|-------|
| **IBM QRadar** | Enterprise | Strong correlation |
| **ArcSight** | Enterprise | Legacy but powerful |
| **LogRhythm** | Mid-market | User-friendly |
| **Sumo Logic** | Cloud | SaaS model |
| **Google Chronicle** | Cloud | Petabyte scale |

## SIEM Use Cases:

```
1. THREAT DETECTION
   ├── Brute force attacks
   ├── Malware activity
   ├── Lateral movement
   └── Data exfiltration

2. COMPLIANCE
   ├── Audit logging
   ├── Access monitoring
   ├── Report generation
   └── Policy violations

3. INCIDENT RESPONSE
   ├── Investigation
   ├── Timeline construction
   ├── IOC searching
   └── Forensic queries

4. THREAT HUNTING
   ├── Hypothesis testing
   ├── Behavioral analytics
   ├── Anomaly detection
   └── Pattern searching
```

---

# LOG MANAGEMENT

## Critical Log Sources:

```
┌─────────────────────────────────────────────────────────────┐
│                 CRITICAL LOG SOURCES                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NETWORK:                         ENDPOINT:                 │
│  ├── Firewall logs                ├── Windows Event Logs    │
│  ├── IDS/IPS logs                 ├── Linux syslog          │
│  ├── Proxy logs                   ├── EDR telemetry         │
│  ├── DNS logs                     ├── Antivirus logs        │
│  ├── VPN logs                     └── PowerShell logs       │
│  └── NetFlow data                                           │
│                                                             │
│  IDENTITY:                        APPLICATION:              │
│  ├── Active Directory             ├── Web server logs       │
│  ├── Azure AD/Entra ID            ├── Database logs         │
│  ├── IAM logs                     ├── Application logs      │
│  ├── MFA logs                     └── API logs              │
│  └── Privileged access logs                                 │
│                                                             │
│  CLOUD:                           SECURITY TOOLS:           │
│  ├── AWS CloudTrail               ├── WAF logs              │
│  ├── Azure Activity Logs          ├── DLP logs              │
│  ├── GCP Audit Logs               ├── CASB logs             │
│  └── Kubernetes audit             └── Email security logs   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Windows Event IDs to Know:

| Event ID | Description | Security Relevance |
|----------|-------------|-------------------|
| **4624** | Successful login | Normal, check type |
| **4625** | Failed login | Brute force indicator |
| **4648** | Explicit credential logon | Pass-the-hash |
| **4672** | Special privileges assigned | Admin logon |
| **4688** | Process creation | Command execution |
| **4698** | Scheduled task created | Persistence |
| **4720** | User account created | Account creation |
| **4732** | Member added to local group | Privilege escalation |
| **7045** | Service installed | Persistence |
| **1102** | Audit log cleared | Covering tracks |

## Log Retention Best Practices:

```
HOT STORAGE (Fast, Expensive):
├── 30-90 days
├── Fully indexed
├── Immediate search
└── Use for investigations

WARM STORAGE (Slower, Cheaper):
├── 90 days - 1 year
├── Compressed
├── Slower queries
└── Compliance needs

COLD STORAGE (Archive):
├── 1-7 years
├── Compliance requirements
├── Not indexed
└── Rare access
```

---

# ALERT TRIAGE

## Alert Lifecycle:

```
┌─────────────────────────────────────────────────────────────┐
│                  ALERT TRIAGE WORKFLOW                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ALERT GENERATED                                         │
│     │                                                       │
│     ▼                                                       │
│  2. INITIAL REVIEW (< 5 min)                                │
│     ├── What triggered the alert?                           │
│     ├── Is context complete?                                │
│     └── Quick sanity check                                  │
│     │                                                       │
│     ▼                                                       │
│  3. CLASSIFICATION                                          │
│     ├── TRUE POSITIVE → Investigate                         │
│     ├── FALSE POSITIVE → Document, tune rule               │
│     └── SUSPICIOUS → Investigate further                   │
│     │                                                       │
│     ▼                                                       │
│  4. SEVERITY ASSIGNMENT                                      │
│     ├── Critical → Immediate escalation                     │
│     ├── High → Investigate now                              │
│     ├── Medium → Investigate today                          │
│     └── Low → Queue for review                              │
│     │                                                       │
│     ▼                                                       │
│  5. INVESTIGATION / ESCALATION                              │
│     │                                                       │
│     ▼                                                       │
│  6. RESOLUTION & DOCUMENTATION                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Triage Questions:

```
CONTEXT:
├── What user/system is involved?
├── What action was taken?
├── When did this happen?
├── Is this normal for this user/system?
└── What's the business context?

INVESTIGATION:
├── Check user's typical behavior
├── Check system's normal activity
├── Look for related events
├── Check threat intel for IOCs
└── Check other detections on same entity

DECISION:
├── Is this a real threat?
├── What's the impact if real?
├── What's the confidence level?
└── What action is needed?
```

## Handling False Positives:

```
When you identify a false positive:

1. DOCUMENT IT
   ├── Why it's a false positive
   ├── Evidence supporting decision
   └── Recommendation for tuning

2. TUNE THE RULE (with approval)
   ├── Add exclusions
   ├── Adjust thresholds
   ├── Improve logic
   └── Test before deploying

3. TRACK METRICS
   ├── False positive rate per rule
   ├── Analyst time wasted
   └── Tuning requests
```

---

# THREAT HUNTING

## What is Threat Hunting?

```
┌─────────────────────────────────────────────────────────────┐
│                   THREAT HUNTING                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Proactive, iterative search through networks to detect     │
│  and isolate advanced threats that evade existing           │
│  security solutions.                                        │
│                                                             │
│  Traditional Detection:                                     │
│  Alert → Investigate (REACTIVE)                             │
│                                                             │
│  Threat Hunting:                                            │
│  Hypothesis → Search → Discover (PROACTIVE)                 │
│                                                             │
│  Purpose:                                                   │
│  ├── Find threats that bypass detection                     │
│  ├── Reduce dwell time                                      │
│  ├── Discover gaps in visibility                            │
│  └── Improve detection rules                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Threat Hunting Process:

```
1. HYPOTHESIS GENERATION
   └── "Attackers may be using scheduled tasks for persistence"

2. DATA COLLECTION  
   └── Gather relevant logs, telemetry

3. INVESTIGATION
   └── Query, analyze, look for anomalies

4. FINDINGS
   └── Document what was found (or not found)

5. RESPONSE
   └── Remediate if threat found
   
6. IMPROVEMENT
   └── Create detection rule if gap found
```

## Hunting Techniques:

### Intelligence-Driven:
- Hunt based on known threat actor TTPs
- Use threat intel reports
- Search for IOCs from intel feeds

### Hypothesis-Driven:
- "What if attacker is using X technique?"
- Based on MITRE ATT&CK framework
- Test assumptions about environment

### Baseline Analysis:
- Know what's normal
- Look for deviations
- Statistical anomalies

## Example Hunts:

```
HUNT: Suspicious PowerShell Execution

Hypothesis: Attackers often use encoded PowerShell

Query (Splunk):
index=windows EventCode=4688 CommandLine=*powershell* 
| regex CommandLine="(-enc|-encodedcommand|-e\s)"
| table _time, Computer, User, CommandLine

What to look for:
├── Encoded commands
├── Download cradles
├── Bypass execution policy
└── Unusual parent processes

HUNT: Lateral Movement via PsExec

Hypothesis: Attackers use PsExec-style tools

Query:
index=windows EventCode=7045 ServiceName=PSEXEC*
OR
index=windows EventCode=4688 CommandLine=*psexec*

What to look for:
├── PSEXEC service creation
├── Remote service execution
├── Unusual times
└── Unusual users
```

## MITRE ATT&CK for Hunting:

```
Use ATT&CK to structure hunts:

Technique: T1053.005 (Scheduled Task)
├── What logs show scheduled task creation?
├── EventID 4698 (task created)
├── Event ID 106 (in Task Scheduler log)
└── Hunt: New scheduled tasks with encoded commands

Technique: T1003.001 (LSASS Memory)
├── What logs show LSASS access?
├── Sysmon Event 10 (process access)
├── Hunt: Processes accessing LSASS
```

---

# SOC TOOLS & TECHNOLOGIES

## Core SOC Technology Stack:

```
┌─────────────────────────────────────────────────────────────┐
│                SOC TECHNOLOGY STACK                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LAYER 1: DATA COLLECTION                                   │
│  ├── Log shippers (Beats, Splunk Forwarders, NXLog)         │
│  ├── Network taps/SPAN                                      │
│  └── Agents (EDR, Sysmon)                                   │
│                                                             │
│  LAYER 2: AGGREGATION & ANALYSIS                            │
│  ├── SIEM (Splunk, Sentinel, ELK)                           │
│  ├── NDR (Network Detection & Response)                     │
│  └── EDR (CrowdStrike, Defender, SentinelOne)               │
│                                                             │
│  LAYER 3: ENRICHMENT                                        │
│  ├── Threat Intelligence Platforms                          │
│  ├── MISP, OpenCTI, ThreatConnect                           │
│  └── Reputation services                                    │
│                                                             │
│  LAYER 4: AUTOMATION & RESPONSE                             │
│  ├── SOAR (Phantom, Demisto/XSOAR, Swimlane)                │
│  ├── Ticketing (ServiceNow, Jira)                           │
│  └── Case Management                                        │
│                                                             │
│  LAYER 5: REPORTING & METRICS                               │
│  ├── Dashboards                                             │
│  ├── Reports                                                │
│  └── KPIs                                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## EDR (Endpoint Detection & Response):

| Product | Vendor | Key Feature |
|---------|--------|-------------|
| **Falcon** | CrowdStrike | Cloud-native, threat intel |
| **Defender for Endpoint** | Microsoft | M365 integration |
| **SentinelOne** | SentinelOne | AI-powered, autonomous |
| **Carbon Black** | VMware | Process recording |
| **Cortex XDR** | Palo Alto | Cross-data correlation |

EDR Capabilities:
```
├── Real-time monitoring
├── Process tree visualization
├── Behavioral detection
├── File analysis
├── Network connections
├── Remote response (isolate, kill process)
└── Forensic data collection
```

## SOAR (Security Orchestration, Automation & Response):

```
┌─────────────────────────────────────────────────────────────┐
│                       SOAR                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PURPOSE: Automate repetitive SOC tasks                     │
│                                                             │
│  Example Playbook: Phishing Investigation                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ 1. SIEM alert → Trigger playbook                     │   │
│  │ 2. Extract email indicators (URLs, IPs, hashes)      │   │
│  │ 3. Query threat intel (VirusTotal, OTX)              │   │
│  │ 4. If malicious:                                     │   │
│  │    ├── Block sender                                  │   │
│  │    ├── Delete email from other mailboxes             │   │
│  │    ├── Add IOCs to blocklist                         │   │
│  │    └── Create ticket                                 │   │
│  │ 5. Notify analyst for review                         │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  Benefits:                                                  │
│  ├── Faster response (minutes vs hours)                     │
│  ├── Consistency (same process every time)                  │
│  ├── Documentation (automatic)                              │
│  └── Focus analysts on complex tasks                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Threat Intelligence Platforms:

| Platform | Type | Use Case |
|----------|------|----------|
| **MISP** | Open Source | IOC sharing |
| **OpenCTI** | Open Source | CTI platform |
| **VirusTotal** | Commercial | File/URL analysis |
| **AlienVault OTX** | Free | Community intel |
| **Recorded Future** | Commercial | Premium intel |

---

# INTERVIEW QUESTIONS & ANSWERS

---

## Q1: "What are the different tiers in a SOC and their responsibilities?"

### ✅ MODEL ANSWER:
> "A typical SOC has three tiers:
>
> **Tier 1 - Security Analyst/Triage:**
> - First line of defense - monitors SIEM 24/7
> - Initial alert triage and classification
> - Distinguishes true vs false positives
> - Follows playbooks for common scenarios
> - Escalates complex issues to Tier 2
> - Documents findings in ticketing system
>
> **Tier 2 - Incident Responder:**
> - Deep-dive investigation of escalated alerts
> - Complex incident response
> - Basic malware and forensic analysis
> - Creates and tunes detection rules
> - Mentors Tier 1 analysts
> - Escalates to Tier 3 for advanced threats
>
> **Tier 3 - Expert/Threat Hunter:**
> - Proactive threat hunting
> - Advanced malware reverse engineering
> - Detection engineering at scale
> - Research and tool development
> - Handles nation-state level threats
>
> **Supporting roles include:** SOC Manager (metrics, team leadership), Threat Intel Analyst (IOC collection), and Detection Engineer (rule creation).
>
> As a fresher, I'd likely start at Tier 1, building foundational skills before advancing."

---

## Q2: "What is SIEM and why is it important?"

### ✅ MODEL ANSWER:
> "SIEM stands for Security Information and Event Management. It combines SIM (log storage/analysis) with SEM (real-time monitoring/correlation).
>
> **What SIEM Does:**
>
> ```
> Collect → Normalize → Store → Correlate → Alert → Investigate
> ```
>
> 1. **Collects logs** from across the environment (servers, firewalls, endpoints)
> 2. **Normalizes** different log formats into consistent structure
> 3. **Stores** for compliance and investigation
> 4. **Correlates** events to detect patterns
> 5. **Alerts** on suspicious activity
> 6. **Enables investigation** and forensics
>
> **Why It's Important:**
>
> - **Single pane of glass**: See all security events in one place
> - **Detection**: Find attacks that single devices miss
> - **Compliance**: Meet logging requirements (PCI-DSS, HIPAA)
> - **Forensics**: Historical data for investigation
>
> **Example Use Case:**
> A single failed login isn't suspicious. But SIEM can correlate:
> - 50 failed logins from one IP → Brute force attack
> - Failed logins followed by success, then unusual data access → Compromised account
>
> **Major SIEM platforms I'm aware of:** Splunk, Microsoft Sentinel, ELK Stack, IBM QRadar."

---

## Q3: "How would you triage a security alert?"

### ✅ MODEL ANSWER:
> "I follow a systematic approach for alert triage:
>
> **Step 1: Initial Review (< 5 min)**
> - What triggered the alert?
> - What entity is involved (user, IP, system)?
> - Do I have enough context?
>
> **Step 2: Gather Context**
> - Is this user/system known?
> - What's their normal behavior?
> - Check related events before/after
> - Look up any IOCs in threat intel
>
> **Step 3: Classification**
> - **True Positive**: Real security event
> - **False Positive**: Benign activity triggering alert
> - **Suspicious**: Need more investigation
>
> **Step 4: Key Questions**
> ```
> WHO: What user/account?
> WHAT: What action was taken?
> WHERE: What system/asset?
> WHEN: Time and duration?
> WHY: Business context?
> ```
>
> **Step 5: Decision**
> - If TRUE POSITIVE: Investigate, escalate if needed
> - If FALSE POSITIVE: Document reason, request rule tuning
> - If INCONCLUSIVE: Escalate to Tier 2
>
> **Example:**
> Alert: Multiple failed logins from IP 185.x.x.x
> - Check: Is this IP known? (No, foreign IP)
> - Check: Which accounts targeted? (Multiple admin accounts)
> - Check: Any successful logins? (No)
> - Classification: **True Positive** - Brute force attack
> - Action: Block IP, check other systems, report"

---

## Q4: "What Windows Event IDs are most important for security monitoring?"

### ✅ MODEL ANSWER:
> "Here are the critical Windows Event IDs I'd monitor:
>
> **Authentication Events:**
> | Event ID | Description |
> |----------|-------------|
> | **4624** | Successful logon |
> | **4625** | Failed logon |
> | **4648** | Explicit credential logon (pass-the-hash) |
> | **4672** | Special privileges assigned (admin login) |
>
> **Account Changes:**
> | Event ID | Description |
> |----------|-------------|
> | **4720** | User account created |
> | **4732** | Member added to security group |
> | **4728** | Member added to global security group |
>
> **Process Execution:**
> | Event ID | Description |
> |----------|-------------|
> | **4688** | New process created |
> | **4104** | PowerShell script block logging |
>
> **Persistence & Evasion:**
> | Event ID | Description |
> |----------|-------------|
> | **7045** | New service installed |
> | **4698** | Scheduled task created |
> | **1102** | Audit log cleared (covering tracks) |
>
> **Practical Example for SIEM correlation:**
> ```
> Rule: Potential Brute Force Attack
> EventID=4625 | count by src_ip | where count > 10 in 5 minutes
>
> Rule: Admin Account Compromise
> EventID=4625 (multiple) → EventID=4624 → EventID=4672
> (Failed logins, then success, then admin privileges)
> ```
>
> I'd also enable Sysmon for detailed process tracking and PowerShell transcription logging."

---

## Q5: "What is threat hunting and how is it different from monitoring?"

### ✅ MODEL ANSWER:
> "**Monitoring (Reactive):**
> - Wait for alerts to fire
> - Investigate alerts generated by rules
> - Relies on known signatures/patterns
> - Can miss sophisticated threats
>
> **Threat Hunting (Proactive):**
> - Actively search for threats
> - Based on hypotheses, not alerts
> - Finds threats that evade detection
> - Improves detection capabilities
>
> **Threat Hunting Process:**
>
> ```
> 1. HYPOTHESIS
>    "Attackers may be using scheduled tasks for persistence"
>
> 2. DATA GATHERING
>    Collect relevant logs (Event ID 4698, Task Scheduler logs)
>
> 3. INVESTIGATION
>    Query for unusual scheduled tasks
>    - Created by non-admin users
>    - Running encoded PowerShell
>    - Created outside business hours
>
> 4. FINDINGS
>    Document results (threats found or not)
>
> 5. IMPROVEMENT
>    If threat found → Remediate
>    If gap found → Create new detection rule
> ```
>
> **Key Difference:**
>
> | Aspect | Monitoring | Hunting |
> |--------|------------|---------|
> | Trigger | Alert fires | Hypothesis |
> | Approach | Reactive | Proactive |
> | Focus | Known threats | Unknown threats |
> | Outcome | Case closure | Detection improvement |
>
> **Using MITRE ATT&CK:**
> I'd structure hunts around ATT&CK techniques. For example, hunting for T1053.005 (Scheduled Task) persistence."

---

## Q6: "How would you reduce false positives in a SOC?"

### ✅ MODEL ANSWER:
> "False positives waste analyst time and cause alert fatigue. Here's how to reduce them:
>
> **1. Better Detection Rules**
> - Add context to rules (not just pattern matching)
> - Use thresholds appropriately
> - Consider time-of-day, user role, asset criticality
>
> **Example - Before:**
> ```
> Alert: failed_login_count > 5
> Problem: Fires for every user who forgot password
> ```
>
> **Example - After:**
> ```
> Alert: failed_login_count > 10 
>        AND source_ip NOT in known_corporate_range
>        AND target_account in admin_accounts
> Result: More targeted, relevant alerts
> ```
>
> **2. Whitelisting/Exclusions**
> - Known good applications
> - Scheduled maintenance windows
> - Documented exceptions
>
> **3. Baseline Analysis**
> - Understand normal behavior
> - Define what's 'unusual' based on data
> - Use behavioral analytics
>
> **4. Feedback Loop**
> - Track false positive rates per rule
> - Analysts document why alerts are false positives
> - Regular rule review and tuning
>
> **5. Enrichment**
> - Add threat intel (is this IP known bad?)
> - Add asset context (is this a critical server?)
> - Add user context (is this an admin?)
>
> **Metrics to Track:**
> - False positive rate by rule
> - Time spent on false positives
> - Analyst feedback scores
>
> Goal is to ensure analysts trust alerts and respond quickly to real threats."

---

## Q7: "Explain SOAR and how it helps a SOC."

### ✅ MODEL ANSWER:
> "SOAR stands for Security Orchestration, Automation, and Response.
>
> **Three Components:**
>
> 1. **Orchestration**: Connecting different security tools
> 2. **Automation**: Automating repetitive tasks
> 3. **Response**: Taking action automatically or semi-automatically
>
> **How SOAR Helps:**
>
> **Problem Without SOAR:**
> ```
> Analyst gets phishing alert
> 1. Open email in sandbox (2 min)
> 2. Check URL in VirusTotal (2 min)
> 3. Check sender reputation (2 min)
> 4. Look up similar emails (3 min)
> 5. Block sender if malicious (2 min)
> 6. Delete from other mailboxes (5 min)
> 7. Document in ticket (5 min)
> Total: 20+ minutes per alert
> ```
>
> **With SOAR:**
> ```
> Playbook triggered automatically:
> 1. Extract indicators → 0 sec
> 2. Check VirusTotal → 5 sec
> 3. Check reputation → 2 sec
> 4. If malicious: Block + Delete → 10 sec
> 5. Create ticket with details → auto
> 6. Notify analyst for review
> Total: < 1 minute, analyst reviews result
> ```
>
> **Benefits:**
> - **Speed**: Minutes vs hours for response
> - **Consistency**: Same process every time
> - **Documentation**: Automatic audit trail
> - **Scalability**: Handle more alerts with same team
>
> **Popular SOAR Platforms:**
> - Palo Alto XSOAR (Demisto)
> - Splunk Phantom
> - Swimlane
> - Microsoft Sentinel (built-in SOAR)
>
> SOAR lets analysts focus on complex investigations rather than repetitive tasks."

---

## Q8: "What log sources would you want in a SIEM?"

### ✅ MODEL ANSWER:
> "I'd prioritize log sources by security value:
>
> **High Priority (Must Have):**
>
> | Category | Sources |
> |----------|---------|
> | **Identity** | Active Directory, Azure AD, MFA logs |
> | **Endpoint** | Windows Security Events, EDR telemetry |
> | **Network** | Firewall (allow/deny), IDS/IPS, DNS |
> | **Email** | Email gateway, O365/Google Workspace |
>
> **Medium Priority:**
>
> | Category | Sources |
> |----------|---------|
> | **Proxy** | Web proxy logs (URLs accessed) |
> | **VPN** | Remote access logs |
> | **Cloud** | AWS CloudTrail, Azure Activity, GCP Audit |
> | **Database** | Query logs for sensitive DBs |
>
> **Extended Visibility:**
>
> | Category | Sources |
> |----------|---------|
> | **Applications** | Critical app logs |
> | **WAF** | Web attack detection |
> | **DLP** | Data movement |
> | **Physical** | Badge access (insider threat) |
>
> **Key Principle - Answer the Questions:**
> ```
> WHO accessed WHAT, from WHERE, WHEN?
> 
> Identity logs → WHO
> Endpoint logs → WHAT actions
> Network logs → WHERE (source/destination)
> All logs → WHEN (timestamps)
> ```
>
> **Example Coverage Gap:**
> If I only have firewall logs:
> - See: Network traffic allowed/denied
> - Miss: What the user did on the endpoint
> - Miss: Authentication events
>
> That's why comprehensive logging is critical for threat detection."

---

## Q9: "How do you stay updated on security threats?"

### ✅ MODEL ANSWER:
> "I use multiple sources to stay current:
>
> **Threat Intelligence Sources:**
> - **CISA Advisories** - Government alerts
> - **Vendor blogs** (Microsoft, CrowdStrike, Mandiant)
> - **VirusTotal** - Sample analysis
> - **Twitter/X** - Security researchers
>
> **Research & News:**
> - **Krebs on Security** - Investigative reporting
> - **BleepingComputer** - Daily security news
> - **The Hacker News** - Quick updates
> - **Dark Reading** - Industry analysis
>
> **Learning Resources:**
> - **MITRE ATT&CK** - Threat techniques
> - **SANS Reading Room** - Research papers
> - **Security podcasts** - Darknet Diaries, Security Weekly
>
> **Community:**
> - **Reddit** (r/netsec, r/cybersecurity)
> - **Discord communities**
> - **CTF participation** - Hands-on learning
>
> **Practical Application:**
> When I hear about a new threat:
> 1. Understand the technique (what it does)
> 2. Check if we're vulnerable (exposure)
> 3. Look for IOCs to search for (detection)
> 4. Add detection rules if needed (prevention)
>
> **Example:**
> When Spring4Shell came out:
> - Read advisories to understand vulnerability
> - Identified affected systems
> - Searched logs for exploitation attempts
> - Created detection rules
>
> Continuous learning is essential since threats evolve constantly."

---

## Q10: "What metrics would you track for SOC performance?"

### ✅ MODEL ANSWER:
> "I'd track metrics across efficiency, effectiveness, and security posture:
>
> **Time Metrics:**
>
> | Metric | Definition | Target |
> |--------|------------|--------|
> | **MTTD** | Mean Time to Detect | Minimize |
> | **MTTA** | Mean Time to Acknowledge | < 15 min |
> | **MTTI** | Mean Time to Investigate | By severity |
> | **MTTR** | Mean Time to Respond | By severity |
>
> **Quality Metrics:**
>
> | Metric | What It Measures |
> |--------|-----------------|
> | **False Positive Rate** | Rule quality |
> | **Escalation Accuracy** | Analyst skill |
> | **Cases Reopened** | Resolution quality |
>
> **Volume Metrics:**
>
> | Metric | Purpose |
> |--------|---------|
> | **Alerts per Day** | Workload planning |
> | **Incidents by Severity** | Risk trending |
> | **Incidents by Type** | Threat landscape |
>
> **Analyst Metrics (Carefully!):**
> - Cases handled per analyst
> - Training completion
> - Quality scores
> (Avoid pure volume metrics that encourage rushing)
>
> **Example Dashboard:**
> ```
> Weekly SOC Metrics:
> ├── Alerts Processed: 1,200
> │   ├── True Positives: 180 (15%)
> │   ├── False Positives: 1,020 (85%)
> │
> ├── MTTD: 4 hours (down from 6)
> ├── MTTR: 2 hours for high severity
> │
> └── Action Items:
>     ├── 85% FP rate - need rule tuning
>     └── Investigate detection gap for lateral movement
> ```
>
> Good metrics drive improvement; bad metrics drive wrong behaviors."

---

# 📋 SOC ANALYST QUICK REFERENCE

## Daily SOC Checklist:
```
□ Review overnight alerts
□ Check for critical/high severity incidents
□ Review threat intelligence updates
□ Check system health (SIEM, EDR, collectors)
□ Attend shift handoff briefing
□ Update tickets/documentation
□ Escalate issues as needed
```

## SIEM Query Cheat Sheet:

### Splunk:
```spl
# Failed logins
index=windows EventCode=4625 | stats count by src_ip

# PowerShell execution
index=windows EventCode=4104 | table _time, ScriptBlockText

# Lateral movement
index=windows EventCode=4648 | stats count by Account_Name
```

### KQL (Sentinel):
```kql
// Failed sign-ins
SigninLogs
| where ResultType != 0
| summarize Count=count() by UserPrincipalName

// Process creation
SecurityEvent
| where EventID == 4688
| project TimeGenerated, Account, CommandLine
```

---

**Document Created**: February 2026
**Priority**: ⭐⭐⭐⭐ HIGH - Very relevant for TCS SOC operations
