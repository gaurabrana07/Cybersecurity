# 🛡️ SECURITY OPERATIONS CENTER (SOC) — CORPORATE COMPLETE GUIDE

> **Audience:** Entry-level to Mid-level SOC Analysts entering corporate environments  
> **Scope:** Everything essential — concepts, architecture, tools, workflows, real-world cases  
> **Last Updated:** 2026

---

## 📋 TABLE OF CONTENTS

1. [What is a SOC?](#1-what-is-a-soc)
2. [SOC Architecture & Models](#2-soc-architecture--models)
3. [SOC Tiers & Roles](#3-soc-tiers--roles)
4. [Day in the Life of a SOC Analyst](#4-day-in-the-life-of-a-soc-analyst)
5. [Core SOC Processes](#5-core-soc-processes)
6. [SIEM — Deep Dive](#6-siem--deep-dive)
7. [SOAR — Automation & Orchestration](#7-soar--automation--orchestration)
8. [EDR / XDR — Endpoint Detection](#8-edr--xdr--endpoint-detection)
9. [Threat Intelligence in SOC](#9-threat-intelligence-in-soc)
10. [Alert Triage & Incident Handling](#10-alert-triage--incident-handling)
11. [Log Sources & Log Management](#11-log-sources--log-management)
12. [Threat Hunting](#12-threat-hunting)
13. [KPIs & SOC Metrics](#13-kpis--soc-metrics)
14. [SOC Tools Ecosystem](#14-soc-tools-ecosystem)
15. [Real-World Case Studies](#15-real-world-case-studies)
16. [Common Attack Patterns SOC Faces](#16-common-attack-patterns-soc-faces)
17. [Frameworks Used in SOC](#17-frameworks-used-in-soc)
18. [SOC in Corporate Environments (TCS, Infosys, Wipro, Big4)](#18-soc-in-corporate-environments)

---

## 1. What is a SOC?

A **Security Operations Center (SOC)** is a centralized unit — people, processes, and technology — responsible for continuously monitoring, detecting, analyzing, responding to, and recovering from cybersecurity incidents.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SECURITY OPERATIONS CENTER                        │
├──────────────┬──────────────┬──────────────┬────────────────────────┤
│   MONITOR    │    DETECT    │   ANALYZE    │       RESPOND          │
│  (24x7x365)  │ (Correlation)│  (Triage)    │  (Containment/Eradication) │
│              │              │              │                        │
│  SIEM Logs   │  SIEM Rules  │  Playbooks   │  SOAR Automation       │
│  EDR Alerts  │  ML Models   │  Kill Chain  │  Incident Response     │
│  NetFlow     │  IOCs/TTPs   │  MITRE ATT&CK│  Forensics             │
└──────────────┴──────────────┴──────────────┴────────────────────────┘
```

### SOC vs NOC vs CSIRT

| Feature | SOC | NOC | CSIRT |
|---------|-----|-----|-------|
| **Focus** | Security threats | Network uptime | Incident response |
| **Primary Tool** | SIEM, EDR | NMS, SNMP | Forensics, IR tools |
| **Works on** | Alerts, TTPs | Performance, outages | Active incidents |
| **Activation** | Continuous (24x7) | Continuous | On-demand |
| **Output** | Incident reports | Availability SLA | Post-incident reports |

---

## 2. SOC Architecture & Models

### SOC Models

| Model | Description | Best For | Drawback |
|-------|-------------|----------|----------|
| **In-House** | Internal team, owned infra | Large enterprises, sensitive sectors | High cost (\$2-5M/yr), 24x7 staffing |
| **MSSP** | Managed Security Service Provider | SMBs, companies without security team | Less context about your environment |
| **Hybrid** | Internal L1/L2 + MSSP for L3 | Mid-sized enterprises | Coordination overhead |
| **Virtual SOC** | Fully remote analysts, cloud-based tools | Startups, cost-conscious orgs | Communication lag |
| **Co-Managed** | MSSP augments internal team | Growing orgs with partial capability | Split responsibility confusion |

### Physical SOC Layout (Enterprise)

```
┌─────────────────────────────────────────────────────────────────┐
│                        SOC FLOOR                                │
│                                                                 │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                │
│  │  L1 PODS   │  │  L2 PODS   │  │  L3/THREAT │                │
│  │ (Analysts) │  │(Sr Analysts│  │  HUNTERS   │                │
│  │  8-10 seats│  │  4-6 seats)│  │  2-3 seats)│                │
│  └────────────┘  └────────────┘  └────────────┘                │
│                                                                 │
│  ┌──────────────────────────────────────────┐                  │
│  │         MAIN SIEM DASHBOARD              │                  │
│  │     (Large screens, real-time feeds)     │                  │
│  └──────────────────────────────────────────┘                  │
│                                                                 │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                │
│  │   SOC MGR  │  │ THREAT INTEL│  │  IR ROOM   │                │
│  │  (Office)  │  │  ANALYST   │  │ (War Room) │                │
│  └────────────┘  └────────────┘  └────────────┘                │
└─────────────────────────────────────────────────────────────────┘
```

### SOC Maturity Model (CMMI-based)

| Level | Name | Characteristics |
|-------|------|----------------|
| **1** | Initial | Ad-hoc, reactive, no standard processes |
| **2** | Managed | Basic SIEM, some runbooks, defined SLAs |
| **3** | Defined | Documented playbooks, threat intel feeds, regular training |
| **4** | Quantitatively Managed | KPIs tracked, SOAR deployed, metrics-driven decisions |
| **5** | Optimizing | Proactive hunting, ML/AI, continuous improvement culture |

---

## 3. SOC Tiers & Roles

### Tier Structure

```
                    ┌──────────────────┐
                    │    SOC MANAGER   │  ← Strategy, SLAs, reporting to CISO
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
    ┌─────────▼──────┐ ┌─────▼──────┐ ┌────▼────────────┐
    │  TIER 1 (L1)   │ │ TIER 2 (L2)│ │   TIER 3 (L3)   │
    │  SOC Analyst   │ │Sr. Analyst  │ │  Threat Hunter  │
    │                │ │            │ │  / IR Specialist │
    │ • Alert triage │ │• Deep invest│ │• Advanced forensics│
    │ • First response│ │• Malware rev│ │• Zero-day analysis │
    │ • Ticket creation│ │• SIEM tuning│ │• Red-team collab│
    │ • Basic runbooks│ │• Threat corr│ │• Hunt hypotheses│
    └────────────────┘ └────────────┘ └─────────────────┘
              │              │              │
    ┌─────────▼──────────────▼──────────────▼─────────────┐
    │              SUPPORT ROLES                           │
    │  Threat Intel Analyst | Forensics | Security Engineer│
    └──────────────────────────────────────────────────────┘
```

### Detailed Role Responsibilities

#### L1 — SOC Analyst
- Monitor SIEM dashboards for alerts (100-500 alerts/shift is common)
- Apply alert triage: True Positive / False Positive / Benign True Positive
- Follow runbooks/playbooks for known alert types
- Create and assign incident tickets (ServiceNow, JIRA)
- Escalate to L2 if alert is confirmed or complex
- Document initial findings in ticket

#### L2 — Senior SOC Analyst
- Deep-dive investigation on escalated incidents
- Correlate events across multiple log sources
- Perform basic malware analysis (static: hashes, strings; dynamic: sandbox)
- Write/tune SIEM detection rules
- Coordinate with asset owners for context
- Produce detailed incident reports

#### L3 — Threat Hunter / IR Specialist
- Proactively hunt for threats not caught by rules
- Advanced forensics (memory dumps, disk images)
- Reverse engineering of malware samples
- Work with Red Team for purple team exercises
- Develop new detection content (Sigma rules, YARA rules)
- Lead major incident response

#### Threat Intelligence Analyst
- Collect, analyze, and disseminate threat intel (tactical, operational, strategic)
- Manage IOC feeds (IP, domain, hash, URL)
- Map adversary TTPs to MITRE ATT&CK
- Produce threat intel reports for leadership

#### SOC Engineer / Security Engineer
- Build and maintain SOC tooling infrastructure
- Integrate new log sources into SIEM
- Maintain SOAR playbooks
- Performance tuning of SIEM rules

---

## 4. Day in the Life of a SOC Analyst

### Shift Handover (Critical!)
```
START OF SHIFT:
├── Review shift handover notes from previous analyst
├── Check open incidents and their current status
├── Review overnight high/critical alerts
├── Acknowledge active ongoing investigations
└── Confirm tool health (SIEM, EDR, ticketing system up?)

DURING SHIFT:
├── Monitor SIEM dashboard for real-time alerts
├── Triage each alert (prioritize by severity: Critical > High > Medium > Low)
├── Open tickets for confirmed incidents
├── Investigate using enrichment tools (VirusTotal, Shodan, internal CMDB)
├── Apply runbooks for common scenarios
├── Escalate when threshold is met
└── Document everything in ticket notes

END OF SHIFT:
├── Update all open tickets with current status
├── Prepare detailed handover notes
├── Highlight any critical pending investigations
└── Flag any tool issues or false positive patterns to SOC Engineer
```

### Real Corporate SOC Workflow (TCS/Infosys style)

1. **Alert fires in SIEM** → Auto-creates ticket in ServiceNow
2. **L1 picks ticket** → Checks alert details, looks up asset in CMDB
3. **Enrichment** → VirusTotal for IPs/hashes, internal Threat Intel platform
4. **Decision:** 
   - False Positive → Close ticket with reason documented
   - Benign True Positive → Close with explanation
   - True Positive → Escalate to L2 with evidence
5. **L2 deep-dives** → Full timeline reconstruction
6. **Containment** → Block IP in firewall, isolate endpoint via EDR
7. **L2/L3 resolves** → Eradication and recovery
8. **Post-Incident** → PIR (Post-Incident Review), update runbook if needed

---

## 5. Core SOC Processes

### 5.1 Incident Response Lifecycle (NIST SP 800-61)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  PREPARE    │───▶│   DETECT    │───▶│  CONTAIN/   │───▶│ POST-INCIDENT│
│             │    │  & ANALYZE  │    │  ERADICATE  │    │  ACTIVITY   │
│• Playbooks  │    │• Alert review│   │• Isolate    │    │• Lessons    │
│• Tools ready│    │• Correlation │   │• Remove     │    │  learned    │
│• Training   │    │• Triage      │   │• Patch      │    │• Report     │
│• Contacts   │    │• Escalation  │   │• Restore    │    │• Update     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### 5.2 Alert Triage Framework

```
ALERT RECEIVED
      │
      ▼
Is the alert from a known noisy/misconfigured source?
      │
   YES → Tune rule / Close as False Positive → Document reason
      │
      NO
      │
      ▼
Does the behavior match known attack patterns / IOCs?
      │
   YES → Confirm True Positive → Escalate with evidence
      │
      NO
      │
      ▼
Is this unusual for the asset / user / time-of-day?
      │
   YES → Escalate as suspicious → L2 investigation
      │
      NO → Close as Benign True Positive → Document
```

### 5.3 Escalation Matrix

| Severity | Response Time | Action | Escalate To |
|----------|--------------|--------|-------------|
| **Critical** (P1) | 15 min | Immediate response | L2, SOC Manager, CISO |
| **High** (P2) | 1 hour | Urgent investigation | L2 |
| **Medium** (P3) | 4 hours | Standard investigation | L2 if needed |
| **Low** (P4) | 24 hours | Best effort | Close/document |

### 5.4 Playbook vs Runbook

| | Playbook | Runbook |
|-|----------|---------|
| **Definition** | Strategic guide for incident type | Step-by-step tactical procedure |
| **Audience** | L2/L3 | L1 |
| **Example** | "How to handle ransomware" | "Step 1: Check hash on VT. Step 2: ..." |
| **Detail Level** | High-level | Granular |

---

## 6. SIEM — Deep Dive

### What is SIEM?

**Security Information and Event Management** — collects, aggregates, correlates, and analyzes log data from across the environment to detect threats in real-time.

```
LOG SOURCES                    SIEM ENGINE                   OUTPUT
───────────                    ──────────                    ──────
Firewalls      ──┐            ┌────────────────┐            Alerts
IDS/IPS        ──┤            │  Log Collection │            Dashboards
Windows Events ──┤   ──────▶  │  Normalization  │  ──────▶  Reports
Linux Syslog   ──┤            │  Correlation    │            Compliance
Cloud Logs     ──┤            │  Alerting       │            Forensics
App Logs       ──┤            │  Storage        │
DNS/Proxy      ──┘            └────────────────┘
```

### SIEM Core Functions

| Function | Description | Example |
|----------|-------------|---------|
| **Log Collection** | Aggregate logs from all sources | 10,000 EPS (Events per Second) |
| **Normalization** | Parse different log formats to common schema | CEF, LEEF, JSON |
| **Correlation** | Link related events across sources and time | Alert: 5 failed logins + 1 success from same IP |
| **Alerting** | Generate alerts when correlation rules fire | "Brute Force Detected" |
| **Dashboards** | Visual real-time monitoring | Alert trends, geographic maps |
| **Reporting** | Compliance and executive reports | Monthly security posture report |
| **UEBA** | User Entity Behavior Analytics | Detect insider threats via behavioral baseline |

### Key SIEM Concepts

**EPS (Events Per Second):** Measure of SIEM capacity. Enterprise SIEM handles 10,000-100,000+ EPS.

**Data Retention:** Typically 90 days hot (searchable) + 1-7 years cold (archived). Compliance drives this.

**Use Cases / Detection Rules:**
```
Example correlation rule (pseudo-logic):
IF:
  EventType = "Failed Login"
  AND Count > 5
  AND TimeWindow = 5 minutes
  AND Source IP = Same
THEN:
  Fire alert: "Potential Brute Force Attack"
  Severity: HIGH
  Assign to: L1 Queue
```

### Popular SIEM Platforms

| SIEM | Vendor | Common Use | Key Feature |
|------|--------|------------|-------------|
| **Splunk** | Splunk Inc. | Large enterprises | SPL query language, vast ecosystem |
| **Microsoft Sentinel** | Microsoft | Azure/M365 environments | KQL, cloud-native, ML built-in |
| **IBM QRadar** | IBM | Banking, govt | Flow analysis (NetFlow), strong correlation |
| **LogRhythm** | LogRhythm | Mid-market | Built-in SOAR, SmartResponse |
| **Elastic SIEM** | Elastic | Startups, MSSP | Open-source ELK base, cost-effective |
| **ArcSight** | Micro Focus | Govt, compliance-heavy | Mature, CEF standard inventor |
| **Exabeam** | Exabeam | UEBA focus | Behavioral analytics leader |

### SPL Query Examples (Splunk)

```splunk
# Find failed logins in last 24h
index=windows EventCode=4625
| stats count by src_ip, user
| where count > 10
| sort -count

# Detect privilege escalation
index=windows EventCode=4672 OR EventCode=4673
| table _time, user, Privileges, ComputerName

# DNS exfiltration detection (long domain names)
index=dns
| eval domain_len=len(query)
| where domain_len > 50
| stats count by query, src_ip
```

### KQL Examples (Microsoft Sentinel)

```kql
// Brute force detection
SecurityEvent
| where EventID == 4625
| summarize FailedCount = count() by IpAddress, Account, bin(TimeGenerated, 5m)
| where FailedCount > 10
| order by FailedCount desc

// Suspicious PowerShell execution
DeviceProcessEvents
| where FileName == "powershell.exe"
| where ProcessCommandLine has_any ("-enc", "-nop", "DownloadString", "IEX")
| project TimeGenerated, DeviceName, AccountName, ProcessCommandLine
```

---

## 7. SOAR — Automation & Orchestration

### What is SOAR?

**Security Orchestration, Automation and Response** — automates repetitive SOC tasks and orchestrates workflows across multiple security tools.

```
ALERT FIRES IN SIEM
        │
        ▼
   SOAR PICKS UP
        │
        ├── Auto-enrich: Query VirusTotal for IOCs
        ├── Auto-lookup: Check CMDB for asset owner
        ├── Auto-notify: Send Slack alert to L2
        ├── Auto-block: Add IP to firewall blocklist (if threshold met)
        └── Auto-ticket: Create ServiceNow ticket with all evidence pre-filled
        
Result: L1 analyst gets a pre-enriched, pre-documented ticket
        (Saves 20-40 min per alert)
```

### SOAR vs SIEM

| | SIEM | SOAR |
|-|------|------|
| **Function** | Detect and alert | Respond and automate |
| **Input** | Raw logs | SIEM alerts + API calls |
| **Output** | Alerts, dashboards | Actions, tickets, reports |
| **Analyst Work** | Manual triage | Reduced manual effort |

### Popular SOAR Platforms

| Platform | Notes |
|----------|-------|
| **Palo Alto XSOAR** | Most popular, 600+ integrations, Python playbooks |
| **Splunk SOAR (Phantom)** | Tight Splunk integration |
| **Microsoft Sentinel + Logic Apps** | Cloud-native, no-code automation |
| **IBM QRadar SOAR** | Paired with QRadar |
| **Swimlane** | Low-code, strong compliance focus |

---

## 8. EDR / XDR — Endpoint Detection

### EDR (Endpoint Detection & Response)

```
TRADITIONAL AV           EDR
──────────────           ───
Signature-based     VS   Behavioral analysis
Detect known            Detect unknown (zero-day)
Quarantine files        Isolate host, kill process, collect forensics
Reactive                Proactive + retrospective
```

**What EDR captures:**
- Process creation (parent-child relationships)
- File operations (create, modify, delete, rename)
- Network connections (destination IP, port, process)
- Registry modifications
- Script execution (PowerShell, cmd, bash)
- Memory injections

### EDR in SOC Workflow

```
Malware executes on endpoint
        │
EDR agent detects anomalous behavior
        │
EDR sends alert to SIEM / XDR Console
        │
SOC Analyst investigates in EDR console:
  ├── View process tree
  ├── Check parent process
  ├── Inspect command line arguments
  ├── See all network connections made
  └── Check file hashes against threat intel
        │
If confirmed malicious:
  ├── Isolate host (one click in EDR console)
  ├── Kill malicious process
  ├── Delete malicious files
  └── Collect forensic artifacts (memory dump, file)
```

### Popular EDR/XDR Solutions

| Tool | Vendor | Key Strength |
|------|--------|-------------|
| **CrowdStrike Falcon** | CrowdStrike | Cloud-native, Threat Graph, best detection rate |
| **Microsoft Defender for Endpoint** | Microsoft | Deep Windows integration, free for M365 E5 |
| **SentinelOne** | SentinelOne | Autonomous response, full rollback capability |
| **Carbon Black** | VMware | Enterprise, strong telemetry |
| **Cortex XDR** | Palo Alto | Strong XDR, links endpoint+network+cloud |

### XDR vs EDR

| | EDR | XDR |
|-|-----|-----|
| **Scope** | Endpoint only | Endpoint + Network + Cloud + Email + Identity |
| **Correlation** | Within endpoint | Cross-source correlation |
| **Detection** | Endpoint TTPs | Multi-stage attack chains |

---

## 9. Threat Intelligence in SOC

### Intelligence Pyramid

```
                    ┌──────────────────┐
                    │    STRATEGIC     │  ← Exec briefings, trend reports
                    │  (For C-Suite)   │    "APT groups targeting our sector"
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │   OPERATIONAL    │  ← TTPs, campaign analysis
                    │ (For IR & L3)    │    "This campaign uses spear phishing"
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │    TACTICAL      │  ← IOCs: IPs, domains, hashes
                    │  (For L1/L2)     │    "Block these 50 IPs in firewall"
                    └──────────────────┘
```

### IOC Types

| IOC Type | Example | Lifespan |
|----------|---------|----------|
| IP Address | 192.168.1.100 | Hours-Days (rotates fast) |
| Domain | malicious-c2.xyz | Days-Weeks |
| URL | hxxp://evil[.]com/payload | Days |
| File Hash (MD5/SHA256) | 5f4dcc3b5aa765d61d8327de... | Weeks-Months |
| YARA Rule | Pattern matching rule | Months-Years |
| Sigma Rule | SIEM detection rule | Permanent |

### Threat Intel Platforms (TIP)

| Platform | Type | Notes |
|----------|------|-------|
| **MISP** | Open-source | Industry standard for IOC sharing |
| **Recorded Future** | Commercial | Premium intel, dark web monitoring |
| **Anomali** | Commercial | STIX/TAXII support, enterprise |
| **VirusTotal** | Freemium | Quick IOC lookup, AV multi-scan |
| **AlienVault OTX** | Free | Community-driven IOC feeds |
| **Threat Crowd** | Free | Domain/IP reputation |

### STIX & TAXII

- **STIX** (Structured Threat Information eXpression): Standardized language for describing threat intel
- **TAXII** (Trusted Automated eXchange of Intelligence Information): Protocol for sharing STIX data

---

## 10. Alert Triage & Incident Handling

### Triage Decision Framework

```
ALERT RECEIVED
     │
     ├─▶ STEP 1: Gather Context
     │         ├── What asset triggered it? (Check CMDB)
     │         ├── Who owns the asset? (IT owner, business owner)
     │         ├── What is the asset's sensitivity? (Critical/High/Medium/Low)
     │         └── Is this asset in a high-risk segment? (DMZ, finance, HR)
     │
     ├─▶ STEP 2: Enrich IOCs
     │         ├── Check IP/domain on VirusTotal, ThreatCrowd
     │         ├── Check hash on VirusTotal, Hybrid-Analysis
     │         ├── Look up internal Threat Intel Platform
     │         └── Check if IP is internal, external, cloud provider, CDN
     │
     ├─▶ STEP 3: Correlate
     │         ├── Are there other alerts for same source in last 24h?
     │         ├── Has this IP/hash been seen before?
     │         ├── Is this part of a larger campaign?
     │         └── What does the MITRE ATT&CK mapping say?
     │
     └─▶ STEP 4: Decide & Act
               ├── FALSE POSITIVE → Close, document, tune rule if needed
               ├── BENIGN TP → Close with explanation ("IT team doing vulnerability scan")
               └── TRUE POSITIVE → Escalate with: Timeline, IOCs, Affected assets, Recommended action
```

### Incident Severity Classification

| Severity | Examples | SLA |
|----------|----------|-----|
| **P1 Critical** | Ransomware active, data exfiltration, C2 active | 15 min response |
| **P2 High** | Successful phishing, lateral movement detected | 1 hour |
| **P3 Medium** | Failed brute force, policy violation, recon | 4 hours |
| **P4 Low** | Informational alerts, minor policy violations | 24 hours |

### Containment Strategies

| Threat Type | Containment Action |
|-------------|-------------------|
| Malware on endpoint | Isolate via EDR, disable network access |
| Compromised credentials | Force password reset, disable account, revoke sessions |
| C2 communication | Block IP/domain in firewall + proxy, kill process |
| Ransomware | Isolate entire network segment, activate IR plan |
| Data exfiltration | Block egress, notify DLP team, preserve evidence |

---

## 11. Log Sources & Log Management

### Critical Log Sources (What to Monitor)

```
NETWORK LAYER:
├── Firewall logs (allow/deny rules, traffic)
├── IDS/IPS alerts
├── NetFlow / IPFIX (traffic metadata)
├── DNS logs (queries, responses)
├── Proxy/Web Gateway logs (URLs visited)
└── VPN logs (connections, user+IP mapping)

ENDPOINT LAYER:
├── Windows Event Logs (Security, System, Application)
│   ├── 4624/4625 - Login success/failure
│   ├── 4648 - Explicit credential use
│   ├── 4688 - Process creation
│   ├── 4697/4698 - Service/scheduled task creation
│   ├── 4720/4728 - Account/group management
│   ├── 7045 - New service installed
│   └── 1102/4719 - Audit log cleared
├── Linux Syslog / Auth log / Audit log
└── EDR telemetry (process, file, network, registry)

APPLICATION LAYER:
├── Web server logs (Apache, Nginx, IIS)
├── Application logs (custom app events)
├── Database logs (queries, schema changes)
└── Email server logs (SMTP, exchange)

CLOUD/IDENTITY:
├── Azure AD / AWS CloudTrail / GCP Cloud Audit Logs
├── Microsoft 365 Unified Audit Log
├── SSO / SAML logs
└── MFA logs

PHYSICAL/OTHER:
├── Physical access logs
├── Badge reader logs
└── CCTV integration (rare)
```

### Windows Event IDs — Must Know

| Event ID | Meaning | Why It Matters |
|----------|---------|---------------|
| 4624 | Successful logon | Baseline; anomalies = lateral movement |
| 4625 | Failed logon | Brute force detection |
| 4648 | Explicit credential logon | Pass-the-hash / credential abuse |
| 4663 | File access | Data exfiltration detection |
| 4672 | Special privileges assigned | Privilege escalation |
| 4688 | Process creation | Malware execution |
| 4697 | Service installed | Persistence mechanism |
| 4698 | Scheduled task created | Persistence mechanism |
| 4720 | User account created | Backdoor account creation |
| 4728 | Member added to security group | Privilege escalation |
| 7045 | New service installed (System log) | Persistence |
| 1102 | Audit log cleared | Anti-forensics / attacker covering tracks |
| 4776 | NTLM authentication | Pass-the-hash, NTLM relay |

---

## 12. Threat Hunting

### What is Threat Hunting?

Proactive search for threats that **evaded automated detection**. Hypothesis-driven, not alert-driven.

```
REACTIVE (Alerting)          PROACTIVE (Hunting)
──────────────────           ───────────────────
Wait for alert          VS   Go looking for threats
Alert-driven                 Hypothesis-driven
L1/L2 analyst               L3 Threat Hunter
Rule-based                   Creative, exploratory
Respond to known            Find unknown / assumed breach
```

### Threat Hunting Process

```
1. HYPOTHESIS
   "Attackers may be using living-off-the-land (LotL) techniques
    via PowerShell to avoid detection"

2. DATA COLLECTION
   Pull PowerShell script block logs (Event 4104)
   Pull process creation logs for powershell.exe (Event 4688)

3. INVESTIGATION
   Search for:
   - encoded commands (-enc, -EncodedCommand)
   - download cradles (IEX, Invoke-WebRequest, DownloadString)
   - suspicious parent processes (e.g., winword.exe → powershell.exe)

4. ANALYSIS
   Correlate findings with threat intel
   Check affected assets

5. OUTCOME
   If threat found → Incident Response
   If no threat → New detection rule created (convert hunt to alert)
   Always → Document hunt methodology
```

### Common Hunting Hypotheses

| Hypothesis | What to Hunt | Tools |
|------------|-------------|-------|
| Living off the Land (LotL) | Abuse of built-in tools: PowerShell, WMI, certutil, mshta | EDR, SIEM |
| Lateral movement | Pass-the-hash, PsExec, WMI remote exec | Windows Event logs, NetFlow |
| Persistence | Scheduled tasks, registry run keys, new services | EDR, Windows logs |
| C2 beaconing | Periodic outbound connections, unusual ports | NetFlow, DNS, Proxy logs |
| Data staging/exfiltration | Large file creation in temp dirs, compression, uploads | File events, Proxy logs |

---

## 13. KPIs & SOC Metrics

### Key SOC Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **MTTD** (Mean Time to Detect) | Avg time from attack start to detection | < 1 hour (world-class: minutes) |
| **MTTR** (Mean Time to Respond) | Avg time from detection to containment | < 4 hours for P1 |
| **MTTC** (Mean Time to Contain) | Time to stop spread | < 1 hour for P1 |
| **Alert Volume** | Alerts per day | Track trend; alert fatigue if too high |
| **False Positive Rate** | % alerts that are FP | < 20% (aim for < 10%) |
| **Escalation Rate** | % L1 alerts escalated to L2 | 10-30% typical |
| **SLA Compliance** | % incidents meeting response SLA | > 95% |
| **Dwell Time** | Time attacker is in environment before detection | < 24 hours (industry avg: 200+ days) |

### Analyst Performance Metrics

| Metric | L1 | L2 |
|--------|----|----|
| Alerts processed/shift | 50-150 | 10-30 |
| Avg triage time/alert | 5-15 min | 30-120 min |
| Tickets created/shift | 5-20 | 5-15 |
| False positive rate | < 15% | N/A |

---

## 14. SOC Tools Ecosystem

### Complete Tool Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SOC TOOL ECOSYSTEM                             │
├──────────────┬──────────────┬─────────────────┬────────────────────┤
│  DETECTION   │   RESPONSE   │  INTELLIGENCE   │  MANAGEMENT        │
├──────────────┼──────────────┼─────────────────┼────────────────────┤
│ Splunk       │ Palo Alto    │ MISP            │ ServiceNow         │
│ Sentinel     │ XSOAR        │ Recorded Future │ JIRA               │
│ QRadar       │ Splunk SOAR  │ AlienVault OTX  │ TheHive            │
│ Elastic SIEM │              │ VirusTotal      │ Confluence         │
├──────────────┼──────────────┼─────────────────┼────────────────────┤
│  ENDPOINT    │   NETWORK    │  FORENSICS      │  VULNERABILITY     │
├──────────────┼──────────────┼─────────────────┼────────────────────┤
│ CrowdStrike  │ Zeek/Bro     │ Volatility      │ Nessus/Tenable     │
│ Defender MDE │ Suricata     │ Autopsy         │ Qualys             │
│ SentinelOne  │ Darktrace    │ FTK             │ Rapid7 InsightVM   │
│ Carbon Black │ NetFlow tools│ SIFT Workstation│                    │
└──────────────┴──────────────┴─────────────────┴────────────────────┘
```

---

## 15. Real-World Case Studies

### Case Study 1: Ransomware Attack — Manufacturing Company (2023)

**Scenario:** A large manufacturing company's SOC detected ransomware spreading across the network at 2 AM.

**Timeline:**
```
11:45 PM - Phishing email delivered with malicious Excel attachment
12:03 AM - Macro executes, downloads Cobalt Strike beacon
12:15 AM - Lateral movement begins via PsExec to file servers
01:47 AM - EDR alert fires: mass file encryption detected
01:52 AM - SOC L1 receives alert, escalates immediately (P1)
01:58 AM - L2 confirms ransomware (LockBit variant), isolates 3 endpoints
02:05 AM - SOC Manager and CISO notified, IR team activated
02:10 AM - Network segment quarantined to stop spread
02:30 AM - 47 systems isolated, backups confirmed clean
06:00 AM - Recovery begins from clean backups
14:00 PM - Critical systems restored

Total impact: 47 systems, 12 hours downtime
```

**Key Learnings:**
- Initial email should have been caught by email gateway — gap in phishing training
- C2 beacon ran for 1.5 hours before EDR caught it — EDR rule tuning needed
- Backups saved the company from \$2M+ ransom
- Network segmentation limited blast radius

**SOC Actions:**
- EDR isolation cut off C2 communication
- Firewall rules blocked known LockBit C2 IPs
- SOAR playbook auto-blocked IOCs across all controls

---

### Case Study 2: Insider Threat — Financial Services (2024)

**Scenario:** SOC noticed unusual data export activity from a soon-to-depart employee.

**Detection Method:** UEBA (User Entity Behavior Analytics) in SIEM flagged behavioral anomaly — 5x increase in file downloads from SharePoint.

**Timeline:**
```
Week 1-3: Employee gives 3-week notice
Week 2: UEBA baseline shows normal: ~50 file downloads/day
Week 3 Day 1: Employee downloads 2,400 files (47x normal)
            → UEBA alert fires: "Anomalous Data Access"
Week 3 Day 1 (L2 Investigation):
  - Files downloaded: customer data, contracts, source code
  - Destination: personal OneDrive sync (DLP alert also triggered)
  - Time: outside normal working hours (10 PM)
Week 3 Day 2: HR + Legal + SOC joint review
Week 3 Day 3: Employee account disabled, legal hold placed on data
```

**Key Learnings:**
- Behavioral analytics critical — signature-based would have missed this
- DLP and UEBA correlation strengthened the case
- Legal chain of custody preserved correctly — prosecution viable
- Offboarding procedures updated (revoking access earlier)

---

### Case Study 3: Business Email Compromise (BEC) — Healthcare (2023)

**Scenario:** Attacker gained access to CFO email account and redirected \$2.3M wire transfer.

**Attack Chain:**
```
1. Spear phishing email to CFO with Microsoft 365 login page
2. CFO enters credentials → attacker captures them
3. Attacker logs in from Nigeria (new geography = risk signal)
4. Azure AD Conditional Access: "Unfamiliar sign-in properties" alert
5. Alert goes to SOC — L1 marks it as "travel" (MISTAKE)
6. Attacker sets inbox rules: forward financial emails to attacker
7. Attacker intercepts wire transfer request, changes bank details
8. \$2.3M transferred to attacker's mule account
9. Finance team calls CFO directly 3 days later — fraud discovered
```

**What SOC Should Have Done:**
- The Azure AD alert should have been L2 escalated (geo-impossible travel)
- MFA would have prevented the initial compromise
- SOAR should have auto-blocked the login and notified CFO directly

**Key Learnings:**
- Alert fatigue is dangerous — "travel" dismissal cost \$2.3M
- MFA is non-negotiable for executives
- Email security monitoring must include inbox rule changes (Event 4724 equivalent in Exchange)

---

### Case Study 4: Supply Chain Attack — SolarWinds Style

**Scenario:** A SOC detecting a supply chain compromise where legitimate software update was backdoored.

**Why it's hard to detect:**
```
Normal update: SolarWinds → Software signed ✓ → Pushed to clients ✓
Supply chain:  Attacker injects backdoor into SolarWinds build
               → Still signed ✓ → Still legitimate ✓
               → Traditional detection completely blind

How it was caught (eventually):
- FireEye noticed their own red team tools being stolen
- Investigated, found Sunburst backdoor
- Backdoor used specific beaconing pattern:
  - Waited 12-14 days before activating (avoiding sandboxes)
  - Used legitimate-looking subdomains of avsvmcloud[.]com
  - Blend in: mimicked legitimate SolarWinds traffic
```

**SOC Detection Approach:**
- Monitor for outbound DNS queries to unusual subdomains
- Behavioral baselines on new network connections from SolarWinds binaries
- Threat intel integration with ISACs (Information Sharing and Analysis Centers)

---

## 16. Common Attack Patterns SOC Faces

### Attack Pattern Matrix

| Attack | Detection Source | Key Indicators |
|--------|-----------------|---------------|
| **Phishing** | Email gateway, O365 logs | Suspicious sender, malicious URL/attachment, login from new IP after click |
| **Brute Force** | SIEM (auth logs) | 10+ failed logins/5min from same IP |
| **Pass-the-Hash** | Windows 4648/4624 | NTLM logon Type 3, no domain credential use |
| **Kerberoasting** | 4769 event (Kerberos ticket) | Many TGS requests for service accounts |
| **Lateral Movement** | EDR, NetFlow, auth logs | PsExec, WMI, new admin connections between workstations |
| **C2 Beaconing** | Proxy, DNS logs | Regular interval outbound connections, unusual ports |
| **Data Exfiltration** | DLP, Proxy | Large outbound transfers, compression utilities, cloud storage uploads |
| **Ransomware** | EDR, file monitoring | Mass file rename/encryption, shadow copy deletion, ransom note creation |
| **Privilege Escalation** | Windows 4672, EDR | Token impersonation, UAC bypass, exploits |
| **Persistence** | Windows 4697/4698, registry | New services, scheduled tasks, registry run keys |

---

## 17. Frameworks Used in SOC

### MITRE ATT&CK

The most important framework in SOC operations. Maps adversary techniques to 14 tactics.

```
TACTICS (Left to Right = Attack Progression):
Reconnaissance → Resource Dev → Initial Access → Execution → Persistence →
Privilege Escalation → Defense Evasion → Credential Access → Discovery →
Lateral Movement → Collection → Command & Control → Exfiltration → Impact

Example - Ransomware Mapped to ATT&CK:
T1566.001 - Phishing: Spearphishing Attachment (Initial Access)
T1059.001 - PowerShell (Execution)
T1547.001 - Registry Run Keys (Persistence)
T1548.002 - UAC Bypass (Privilege Escalation)
T1070.001 - Clear Windows Event Logs (Defense Evasion)
T1003.001 - LSASS Memory (Credential Access)
T1021.002 - SMB/Admin Shares (Lateral Movement)
T1486     - Data Encrypted for Impact (Impact)
```

### Cyber Kill Chain (Lockheed Martin)

```
1. RECONNAISSANCE  → Gather info (OSINT, scanning)
2. WEAPONIZATION   → Create payload (malware + exploit)
3. DELIVERY        → Send payload (email, web, USB)
4. EXPLOITATION    → Trigger exploit on victim system
5. INSTALLATION    → Install backdoor/malware
6. C2              → Establish command and control
7. ACTIONS ON OBJ  → Data theft, ransomware, sabotage
```

**SOC value:** If you block any phase, you disrupt the attack. Multiple detection opportunities.

### Diamond Model

Four features of every intrusion:
- **Adversary** — Who is attacking?
- **Infrastructure** — What C2 IP/domains are they using?
- **Capability** — What tools/malware do they use?
- **Victim** — Who/what is being targeted?

---

## 18. SOC in Corporate Environments

### How TCS/Infosys/Wipro SOC Works (Service Delivery SOC)

```
CLIENT ──────────────────────────── MSSP SOC
                                    (TCS, Infosys, Wipro)
Client environment                  Shared SOC platform
├── Firewall logs              ──▶  ├── Multi-tenant SIEM
├── EDR agents                      ├── Client-isolated views
├── AD logs                   ──▶  ├── Dedicated client L1/L2
└── Cloud logs                      └── 24x7 monitoring
                                    
Key difference from in-house:
- SOC analyst handles MULTIPLE clients simultaneously
- Must context-switch between environments
- Client-specific runbooks and escalation contacts
- SLA-driven (contractual obligations)
- Monthly/quarterly security reports for each client
```

### Certifications for SOC Career (Corporate Value)

| Certification | Level | Issued By | Value |
|---------------|-------|-----------|-------|
| **CompTIA Security+** | Entry | CompTIA | Minimum bar for most SOC L1 |
| **CompTIA CySA+** | Mid | CompTIA | Blue team focused, SOC specific |
| **CEH** | Mid | EC-Council | Good for corporate (recognized by HRs) |
| **BTL1/BTL2** | Mid | Security Blue Team | Hands-on blue team certs |
| **Splunk Core Certified User** | Tool | Splunk | SIEM-specific, high value |
| **SC-200** | Mid | Microsoft | Sentinel/MDE specific |
| **GCIH** | Advanced | SANS GIAC | Incident handling, gold standard |
| **GCIA** | Advanced | SANS GIAC | Intrusion analysis |

### Key Documentation in Corporate SOC

| Document | Purpose |
|----------|---------|
| **Playbook** | Strategic guide per incident type |
| **Runbook** | Step-by-step procedure for L1 |
| **IR Plan** | Who does what during major incidents |
| **Asset Register / CMDB** | What assets exist, who owns them |
| **Threat Model** | What threats are most relevant to org |
| **SOC Charter** | Scope, authority, responsibilities of SOC |
| **SLA Agreement** | Response time commitments to client |
| **Post-Incident Report (PIR)** | Lessons learned after incidents |
| **Threat Hunt Report** | Findings from proactive hunts |

---

> **💡 Pro Tip:** In a corporate SOC interview, always mention that you understand the difference between managing alerts and managing incidents. Alert management is triage; incident management is the full lifecycle. This distinction shows maturity.

> **📝 Note for Freshers entering Corporate SOC:** Your first 3 months will be mostly L1 work — alert triage. Focus on: (1) speed of triage, (2) documentation quality, (3) knowing when to escalate. Don't try to be a hero — escalation is the right call when uncertain.

