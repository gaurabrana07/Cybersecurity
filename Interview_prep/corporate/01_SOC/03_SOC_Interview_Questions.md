# 🎯 SOC ANALYST — INTERVIEW QUESTIONS BANK

> **Coverage:**  
> 🔴 Priority Questions (Asked in 90%+ interviews)  
> 🟡 Job-Switching Questions (For laterals / domain switchers)  
> 🟢 Experience-Based Questions (Scenario / behavioral)  
> 🔵 Behavioral / Situational Questions (Corporate cultural fit)

---

## 📋 TABLE OF CONTENTS

1. [Priority Questions — Core SOC Concepts](#-priority-questions--core-soc-concepts)
2. [Priority Questions — Tools & Technology](#-priority-questions--tools--technology)
3. [Priority Questions — Processes & Frameworks](#-priority-questions--processes--frameworks)
4. [Job-Switching Questions](#-job-switching-questions)
5. [Experience-Based / Scenario Questions](#-experience-based--scenario-questions)
6. [Behavioral / Situational Questions](#-behavioral--situational-questions)
7. [SOC Manager / Lead Questions](#-soc-manager--lead-questions)
8. [Quick Fire Round](#-quick-fire-round)

---

# 🔴 PRIORITY QUESTIONS — CORE SOC CONCEPTS

> These are asked in almost every SOC interview — know them cold.

---

## Q1: What is a SOC and what are its primary functions?

**Answer:**  
A Security Operations Center (SOC) is a centralized team — combining people, processes, and technology — that continuously monitors, detects, analyzes, responds to, and recovers from cybersecurity incidents.

**Primary functions:**
- **Monitor:** 24x7 monitoring of security events via SIEM
- **Detect:** Correlate events to identify threats (True Positives)
- **Analyze:** Investigate alerts, determine scope and impact
- **Respond:** Contain, eradicate, and recover from incidents
- **Report:** Document findings, provide metrics and compliance reports
- **Improve:** Tune detection, update playbooks, run threat hunts

**Corporate-ready addition:** A SOC also supports compliance requirements (PCI-DSS, ISO 27001, SOC 2) by maintaining audit-ready log records and incident reports.

---

## Q2: What are the different tiers in a SOC and their responsibilities?

**Answer:**

| Tier | Role | Key Responsibilities |
|------|------|---------------------|
| **L1** | SOC Analyst | Alert triage, first response, ticket creation, escalation |
| **L2** | Senior Analyst | Deep investigation, malware analysis, SIEM tuning, incident reports |
| **L3** | Threat Hunter / IR | Proactive hunting, forensics, zero-day analysis, red team collaboration |
| **Manager** | SOC Manager | Strategy, SLAs, metrics, CISO reporting |
| **Support** | Threat Intel / SOC Engineer | IOC feeds, tool maintenance, SOAR playbooks |

---

## Q3: What is SIEM? How does it work?

**Answer:**  
SIEM stands for **Security Information and Event Management**. It collects, aggregates, normalizes, and correlates log data from across the environment to detect security threats in real-time.

**How it works:**
1. **Collection:** Agents/connectors send logs from firewalls, endpoints, servers, cloud
2. **Normalization:** Different log formats are parsed into a common schema (CEF, LEEF, JSON)
3. **Correlation:** Rules link related events across sources and time windows
4. **Alerting:** When correlation rules fire, alerts are generated
5. **Storage:** Logs stored for forensics and compliance (90 days hot, 1-7 years archive)

**Example:** A SIEM rule fires when: *5 failed logins from same IP within 5 minutes, followed by 1 successful login.* That's a brute force + compromise detection.

**Tools:** Splunk, Microsoft Sentinel, IBM QRadar, Elastic SIEM, ArcSight

---

## Q4: What is the difference between IDS and IPS?

**Answer:**

| | IDS | IPS |
|-|-----|-----|
| **Full name** | Intrusion Detection System | Intrusion Prevention System |
| **Position** | Out of band (passive monitoring) | Inline (sits in traffic path) |
| **Action** | Detect and alert | Detect, alert, AND block |
| **Risk** | None (doesn't touch traffic) | Can block legitimate traffic (false positives are dangerous) |
| **Example** | Snort in IDS mode | Snort in IPS mode / Palo Alto NGFW |

**Key point:** IPS being inline means false positives block real traffic — hence IPS rules must be carefully tuned before enabling blocking.

---

## Q5: What is a firewall and what types exist?

**Answer:**  
A firewall is a network security device that monitors and controls incoming/outgoing traffic based on predefined security rules.

**Types:**

| Type | What it does | Example |
|------|-------------|---------|
| **Packet Filtering** | Filters based on IP, port, protocol | Legacy ACLs |
| **Stateful Inspection** | Tracks connection state (established/new) | Most modern firewalls |
| **Application-Layer (Proxy)** | Inspects application payload | Squid proxy |
| **NGFW (Next-Gen)** | IPS + DPI + App awareness + Threat Intel | Palo Alto, Fortinet, Check Point |
| **WAF** | Specifically protects web applications | Cloudflare WAF, AWS WAF |

---

## Q6: Explain the incident response lifecycle.

**Answer:**  
Based on **NIST SP 800-61** (the industry standard):

1. **Preparation** — Playbooks, tools, training, IR plan ready before incidents happen
2. **Detection & Analysis** — Identify and validate the incident (SIEM alerts, EDR, user reports)
3. **Containment** — Short-term: isolate affected systems; Long-term: patch, fix root cause
4. **Eradication** — Remove malware, attacker access, IOCs from environment
5. **Recovery** — Restore systems, validate clean state, return to normal operations
6. **Post-Incident Activity** — PIR (Post-Incident Review), lessons learned, update playbooks

**PICERL mnemonic:** Prepare → Identify → Contain → Eradicate → Recover → Lessons Learned

---

## Q7: What is the difference between a false positive and a false negative in SOC context?

**Answer:**

| | Definition | Impact |
|-|------------|--------|
| **False Positive (FP)** | Alert fires, but there's no real threat | Wasted analyst time, alert fatigue |
| **False Negative (FN)** | Real threat exists but no alert fired | Missed attack, breach undetected |
| **True Positive (TP)** | Alert fires for a real threat | Correct detection — goal of SOC |
| **True Negative (TN)** | No alert, no threat (quiet, normal) | Normal operation |

**Most dangerous:** False Negatives — they mean attackers are in your environment undetected.  
**Most common problem:** False Positives — they cause alert fatigue, which can lead to analysts missing real TPs.

---

## Q8: What is EDR and how does it differ from traditional antivirus?

**Answer:**

| | Traditional AV | EDR |
|-|----------------|-----|
| **Detection** | Signature-based | Behavioral + signature |
| **Coverage** | Detects known malware | Detects known + unknown (zero-day) |
| **Visibility** | File scanning | Process, file, network, registry, memory |
| **Response** | Quarantine file | Isolate host, kill process, collect forensics |
| **Retrospection** | No | Yes — search past activity |
| **Examples** | Windows Defender (basic) | CrowdStrike Falcon, SentinelOne, Defender for Endpoint |

**Key EDR capability:** Even if malware is fileless (lives only in memory), EDR can detect it through behavioral analysis of PowerShell, WMI, and process injection activities.

---

## Q9: What are IOCs (Indicators of Compromise)?

**Answer:**  
IOCs are pieces of forensic data that identify potentially malicious activity on a system or network.

**Types:**
- **Network-based:** IP addresses, domains, URLs, SSL certificate hashes
- **Host-based:** File hashes (MD5/SHA256), file names/paths, registry keys, mutex names
- **Email-based:** Sender addresses, subject lines, attachment hashes
- **Behavioral:** Specific command sequences, unusual process relationships

**IOC Lifecycle:** IOCs degrade over time as attackers rotate infrastructure. IP addresses change in hours; file hashes change with each build; TTP-based detection (MITRE ATT&CK) is more durable.

---

## Q10: What is MITRE ATT&CK and why is it important for SOC?

**Answer:**  
MITRE ATT&CK is a globally accessible knowledge base of adversary **tactics, techniques, and procedures (TTPs)** based on real-world observations.

**Structure:**
- **14 Tactics** — The "why" (goals): Initial Access, Execution, Persistence, Privilege Escalation, etc.
- **Techniques** — The "how" (method): e.g., T1566 Phishing
- **Sub-techniques** — Specific variations: T1566.001 Spearphishing Attachment

**SOC uses:**
1. **Detection mapping** — Map your SIEM rules to ATT&CK to find coverage gaps
2. **Hunt hypotheses** — Use ATT&CK to guide proactive hunting
3. **Incident documentation** — Tag incidents with ATT&CK techniques for trend analysis
4. **Communication** — Common language between SOC, IR, and red teams

**ATT&CK Navigator:** Visualize your detection coverage against the full ATT&CK matrix.

---

## Q11: What is the Cyber Kill Chain?

**Answer:**  
Developed by Lockheed Martin, it models attacker progression in 7 phases:

1. **Reconnaissance** — Passive/active information gathering (OSINT, scanning)
2. **Weaponization** — Creating the payload (malware + exploit combo)
3. **Delivery** — Sending payload (email, USB, web)
4. **Exploitation** — Triggering the exploit on victim
5. **Installation** — Installing persistence (backdoor, malware)
6. **Command & Control (C2)** — Establishing communication channel
7. **Actions on Objectives** — Data theft, ransomware, sabotage

**SOC value:** Defenders can disrupt attacks at any phase. The earlier you detect, the less damage. Multiple detection points across the chain = defense in depth.

---

## Q12: What is SOAR and how does it help a SOC?

**Answer:**  
**SOAR = Security Orchestration, Automation and Response**

It automates repetitive SOC tasks and orchestrates workflows across multiple security tools.

**How it helps:**
- **Automation:** Auto-enrich alerts with threat intel (VirusTotal, internal TIP) without analyst doing it manually
- **Orchestration:** Automatically create tickets, notify teams via Slack/email, block IPs in firewall
- **Standardization:** Every alert handled consistently per playbook — no human error variation
- **Speed:** Reduces time from alert to action from 20-40 minutes to seconds

**Example workflow:**
```
SIEM alert → SOAR picks up → Auto-queries VirusTotal → 
Auto-creates ServiceNow ticket → Auto-notifies L2 via Slack →
L2 reviews pre-enriched ticket → Saves 25 min/alert
```

**Tools:** Palo Alto XSOAR, Splunk SOAR (Phantom), Microsoft Sentinel + Logic Apps

---

## Q13: How do you handle a potential phishing incident?

**Answer:**

**Step-by-step process:**

1. **Receive alert** — From email gateway, user report, or SIEM correlation
2. **Analyze email headers** — Check sender, reply-to, DKIM/DMARC/SPF alignment
3. **Analyze links** — Defang and check URLs in VirusTotal, URLScan.io
4. **Analyze attachments** — Check file hash in VirusTotal, submit to sandbox (ANY.RUN)
5. **Check for clicks/delivery** — Did users click? Did email reach inbox or get quarantined?
6. **Check post-click activity** — For users who clicked: check browser proxy logs, EDR alerts
7. **Scope** — How many users received it? (Query email gateway)
8. **Contain** — Delete email from all inboxes (email gateway purge), block malicious URLs in proxy
9. **Remediate** — Force password reset for users who entered credentials, check for OAuth app grants
10. **Report** — Ticket update, notify users, update email security rules
11. **Hunt** — Check if similar emails were previously delivered

---

## Q14: What are the most important Windows Event IDs for SOC monitoring?

**Answer:**

| Event ID | What it means | Why important |
|----------|---------------|--------------|
| 4624 | Successful logon | Baseline; anomalies suggest lateral movement |
| 4625 | Failed logon | Brute force detection |
| 4648 | Logon with explicit credentials | Pass-the-hash, credential abuse |
| 4688 | New process created | Malware execution detection |
| 4672 | Special privileges assigned to logon | Privilege escalation |
| 4697/7045 | New service installed | Persistence mechanism |
| 4698 | Scheduled task created | Persistence mechanism |
| 4720 | User account created | Backdoor account |
| 4728 | Member added to security group | Privilege escalation |
| 4776 | NTLM credential validation | Pass-the-hash, NTLM relay |
| 1102 | Audit log cleared | Anti-forensics — attacker covering tracks |
| 4719 | System audit policy changed | Tamper with logging |

---

## Q15: What is threat hunting and how does it differ from alert-based monitoring?

**Answer:**

| | Alert-Based Monitoring | Threat Hunting |
|-|----------------------|----------------|
| **Trigger** | Alert fires → investigate | Hypothesis → go looking |
| **Who** | L1/L2 analyst | L3 Threat Hunter |
| **Mindset** | Reactive | Proactive |
| **Goal** | Respond to known threats | Find unknown threats (assumed breach) |
| **Method** | Follow runbook | Creative query writing, hypothesis testing |
| **Output** | Incident ticket | New detection rule OR incident |

**Hunting process:**
1. Form hypothesis ("Are attackers using PowerShell to evade detection?")
2. Collect relevant data (PowerShell logs 4104, process creation 4688)
3. Analyze anomalies (encoded commands, download cradles, unusual parent processes)
4. Confirm or deny hypothesis
5. If confirmed: IR. Always: Convert finding to detection rule.

---

# 🔴 PRIORITY QUESTIONS — TOOLS & TECHNOLOGY

---

## Q16: Have you worked with Splunk? Give an example of a query you'd write.

**Answer:**

Yes. Splunk uses **SPL (Search Processing Language)**.

**Example — Detecting brute force:**
```splunk
index=windows EventCode=4625
| stats count by src_ip, user
| where count > 10
| sort -count
| table src_ip, user, count
```

**Example — Detect PowerShell encoded commands:**
```splunk
index=windows EventCode=4688 
| where match(CommandLine, "-[Ee][Nn][Cc]")
| table _time, ComputerName, User, CommandLine
```

**Example — Failed logins followed by success (brute force + compromise):**
```splunk
index=windows EventCode=4625 OR EventCode=4624
| transaction src_ip maxspan=5m
| search EventCode=4625 AND EventCode=4624
| table _time, src_ip, user
```

---

## Q17: How would you detect lateral movement in a network?

**Answer:**

**Lateral movement indicators:**

1. **Authentication-based:**
   - EventID 4648 (logon with explicit credentials) from workstations to workstations (unusual)
   - NTLM authentication (4776) between endpoints (pass-the-hash)
   - New admin shares connections (EventID 5140, 5145)

2. **Process-based (EDR):**
   - PsExec execution (creates PSEXESVC service on target)
   - WMI remote execution (wmiprvse.exe spawning unusual child processes)
   - PowerShell remoting (wsmprovhost.exe)

3. **Network-based:**
   - Workstation-to-workstation SMB traffic (unusual in most environments)
   - RDP from unexpected sources
   - High volume of failed connections across multiple systems

**SIEM query (Splunk):**
```splunk
index=windows EventCode=4624 Logon_Type=3
| stats dc(host) as unique_targets by src_ip
| where unique_targets > 5
```
(One IP authenticating to 5+ hosts in short time = lateral movement indicator)

---

## Q18: How do you analyze a suspicious file or hash?

**Answer:**

**Step-by-step investigation:**

1. **Do NOT execute on live system** — Immediately

2. **Static analysis:**
   - Submit hash to **VirusTotal** (check AV detections)
   - Check **Hybrid-Analysis** or **ANY.RUN**
   - Check **MalwareBazaar** (abuse.ch)
   - Identify file type (magic bytes, not just extension)
   - Run **strings** analysis — look for URLs, registry keys, suspicious strings

3. **Sandbox analysis (dynamic):**
   - Submit file to **ANY.RUN**, **Hybrid-Analysis**, or **Joe Sandbox**
   - Observe: network connections made, files created, registry keys written, processes spawned
   - Map behavior to MITRE ATT&CK

4. **Threat Intel correlation:**
   - Does this hash appear in known malware families?
   - Are the C2 IPs/domains associated with known threat actors?

5. **Document findings:**
   - File hash (SHA256 preferred), file size, type
   - Behavior summary
   - IOCs extracted (IPs, domains, other hashes dropped)
   - MITRE ATT&CK techniques observed

---

# 🔴 PRIORITY QUESTIONS — PROCESSES & FRAMEWORKS

---

## Q19: How do you prioritize multiple critical alerts simultaneously?

**Answer:**  
In a real SOC, alert storms happen. My prioritization framework:

1. **Asset criticality first:** Is the affected asset a domain controller, payment system, or critical server? That moves to top priority.
2. **Attack stage:** Active exploitation > Lateral movement > Reconnaissance (further left on kill chain = more dangerous currently)
3. **Business impact:** Will this cause financial loss, data exposure, or regulatory violation?
4. **Threat intelligence context:** Is this a known APT TTP? Targeted attack?

**Practical approach:**
- P1 Critical gets immediate personal attention
- P2 High: start triage, document, get to L2 ASAP
- Medium/Low: queue them, work through methodically
- Never close without documentation — even if FP
- Communicate to SOC Manager if overwhelmed — that's what escalation is for

---

## Q20: What is the difference between a playbook and a runbook?

**Answer:**

| | Playbook | Runbook |
|-|----------|---------|
| **Audience** | L2/L3 analysts | L1 analysts |
| **Detail level** | Strategic, decision-based | Step-by-step, granular |
| **Example** | "Ransomware Response Playbook" | "Step 1: Check hash on VT. Step 2: If > 5 AV detections, escalate..." |
| **Flexibility** | Analyst judgment required | Follow exactly as written |
| **Maintenance** | Updated after major incidents | Updated regularly as procedures evolve |

---

# 🟡 JOB-SWITCHING QUESTIONS

> For those switching from: IT support, networking, development, or other security domains.

---

## Q21: You're coming from an IT/Networking background — how does that apply to SOC work?

**Sample Answer Framework:**

*"My networking background gives me a strong foundation in [specific area]. In a SOC context, this translates directly to [how]. For example, I understand how TCP sessions work, which means when I see a SIEM alert about unusual port activity, I can quickly determine if it's a protocol violation or legitimate traffic. I've been upskilling specifically for SOC by [mention LetsDefend, TryHackMe, BTL1 cert, etc.] and have hands-on practice with [Splunk/log analysis/SIEM]."*

**Key bridge points for networking background:**
- Firewall log analysis (direct transfer)
- Understanding NetFlow/packet captures — ahead of many fresh blue teamers
- Network topology knowledge helps contextualize alerts
- IDS/IPS already familiar

---

## Q22: You're switching from development — what unique perspective do you bring?

**Sample Answer Framework:**

*"As a developer, I understand how applications work internally — how SQL queries are constructed, how API authentication works, how input validation should function. In SOC, this means when I see a WAF alert or application log anomaly, I can read the actual attack payload and understand what the attacker was trying to do. I also understand the SDLC, which helps me work with development teams during incidents without being slowed down by communication gaps."*

**Key bridge points for developer background:**
- Understanding of code helps malware analysis
- Scripting skills (Python) for SOAR, log parsing
- Application log reading is natural
- Can help SOC automate repetitive tasks

---

## Q23: What made you specifically choose the blue team / SOC path over offensive security?

**Answer framework:**

*"I find the investigative and analytical aspect of blue team work more aligned with how I think. In SOC, every alert is a puzzle — you're correlating data points, building a timeline, and trying to understand what actually happened. I'm motivated by the idea of being the team that stops real attacks from impacting real businesses and people. The detective work in threat hunting particularly excites me — proactively looking for threats that haven't triggered alerts yet."*

*(Tailor to your genuine reasons — authenticity matters here)*

---

## Q24: How long have you been preparing for a SOC role and what have you done practically?

**Answer framework (be specific):**

*"I've been preparing for [X months]. I've completed [TryHackMe SOC Level 1 path / BTL1 certification / LetsDefend exercises]. On LetsDefend, I've worked through [X challenges] including [specific alert type like phishing analysis, malware alerts]. I set up a home lab with [Splunk/ELK] where I practice writing correlation rules and analyzing sample logs. I also follow The DFIR Report weekly to see how real attacks are conducted and detected."*

**What interviewers want to hear:** Practical, consistent effort — not just "I've been reading about it."

---

## Q25: What is the biggest gap in your knowledge right now and how are you addressing it?

**Answer framework (honesty + proactivity):**

*"Currently, my weakest area is [malware analysis at the binary level / advanced SIEM rule writing / memory forensics]. I'm aware of this and actively working on it through [TCM Security's malware analysis course / Volatility practice challenges / reading The Art of Memory Forensics]. I know I'll develop further on the job, but I want to be transparent about where I am and show that I have a learning plan."*

---

# 🟢 EXPERIENCE-BASED / SCENARIO QUESTIONS

---

## Q26: Walk me through how you'd investigate a "Ransomware Detected" alert.

**Detailed Answer:**

```
STEP 1 — VERIFY THE ALERT
- Open the alert in SIEM, note: affected hostname, time, process name, detection type
- Check EDR console for more context: What process triggered? What was the parent process?

STEP 2 — INITIAL TRIAGE
- Is this a real file encryptor or a ransomware simulation test?
- Check: Are actual files being encrypted? (Look for mass file rename events in EDR)
- Check: Is this a known ransomware family? (Hash lookup in VirusTotal/MalwareBazaar)

STEP 3 — IMMEDIATE CONTAINMENT (if confirmed real)
- Isolate endpoint via EDR immediately (one-click network isolation)
- Notify L2/SOC Manager — this is P1
- Do NOT shut down the machine (memory evidence)

STEP 4 — SCOPE ASSESSMENT
- Has it spread? Check for same process hash on other systems via EDR
- Check network for lateral movement activity before ransomware detonated
- Check Active Directory for compromised accounts

STEP 5 — EVIDENCE COLLECTION
- Pull EDR telemetry: Full process tree, all network connections, files dropped
- Export SIEM logs for affected systems for the past 48-72 hours
- Note: What was the initial access vector? (Check email logs, VPN logs)

STEP 6 — ERADICATION
- Remove malicious files (if EDR hasn't already)
- Reset compromised credentials
- Block C2 IPs/domains in firewall and proxy
- Patch the exploited vulnerability

STEP 7 — RECOVERY
- Restore from clean backups (verify backup integrity first!)
- Validate system clean before reconnecting to network

STEP 8 — POST-INCIDENT
- Document full attack timeline
- PIR with all teams
- Update runbooks
- Notify legal/compliance if data was exfiltrated
```

---

## Q27: You receive 200 alerts in one shift. How do you manage?

**Answer:**

*"First, triage by severity — work all Criticals and Highs before touching Mediums. For each alert, use a consistent, fast methodology: Is this a known FP pattern? If yes, close with documentation. If not, quick enrichment (30-60 seconds: VirusTotal, CMDB lookup), then decide: escalate or close. I'd also look for alert clusters — if 50 alerts are all from the same misconfigured asset, I'd escalate that pattern to the SOC Engineer for rule tuning rather than triaging each individually. At the end of shift, any open items get clear handover notes — I never leave ambiguous items for the next shift."*

---

## Q28: You discover that an alert from yesterday was a True Positive that was marked as a False Positive. What do you do?

**Answer:**

*"First, I'd immediately reopen the incident and assess: Is the attacker still in the environment? If yes, that becomes the P1 priority right now. I'd notify the SOC Manager immediately — this is significant. For accountability: I'd document what was missed and why (without blame-shifting — take responsibility for my part). The goal is learning, not punishment. I'd also check: are there other systems affected during the time this was misclassified? We may have a wider breach. After containment, I'd suggest a runbook update or SIEM tuning to prevent the same FP misclassification from happening again. And I'd request a team review of recent similar alert closures to check if more were missed."*

---

## Q29: A user calls the SOC saying their computer is running very slowly and their files look strange. What do you do?

**Answer:**

*"This is a potential ransomware / malware infection. My immediate steps:*

*1. Ask the user NOT to shut down the machine and not to interact with unusual pop-ups*
*2. Check the user's endpoint immediately in EDR: Are there unusual processes? Mass file activity?*
*3. Check SIEM for any alerts for this endpoint in the last 24 hours*
*4. If EDR shows file encryption activity or known malware behavior — isolate endpoint immediately via EDR*
*5. Call the user back, explain we're investigating, escalate to L2*
*6. Notify user's manager / asset owner per our escalation procedure*

*The key is acting quickly while preserving evidence — not shutting down the machine destroys memory-based malware evidence."*

---

## Q30: How would you respond to discovering an insider threat in progress?

**Answer:**

*"Insider threat response is sensitive because it involves an employee. Steps:*

*1. Do not alert the suspect — covert investigation first*
*2. Immediately preserve evidence: log exports, email records, access logs with chain of custody*
*3. Notify SOC Manager, who notifies HR and Legal — they lead from here*
*4. Continue monitoring covertly — document all ongoing suspicious activity*
*5. Legal will determine if/when to engage law enforcement*
*6. Only disable the account when Legal/HR direct it — premature action can tip off the person and destroy evidence or create legal liability*
*7. If active data exfiltration is occurring in real-time, DLP controls can throttle or block without tipping off the user (preferred over direct confrontation)*

*Insider threats are not pure SOC incidents — they become joint SOC/HR/Legal/Management operations."*

---

# 🔵 BEHAVIORAL / SITUATIONAL QUESTIONS

---

## Q31: Tell me about a time you identified a problem before it became critical.

**Framework:**  
Use **STAR** (Situation, Task, Action, Result)

*Sample context: "While reviewing logs for a routine check, I noticed a pattern of after-hours access to sensitive files by a service account. The account was supposed to run automated backups only at 2 AM, but I saw it accessing HR files at 3 PM. I escalated immediately. Investigation revealed the service account's credentials had been compromised. We rotated credentials and added alerting before any data was exfiltrated."*

---

## Q32: How do you handle working under pressure during a major incident?

**Answer framework:**

*"I've learned to separate urgency from panic. During high-pressure situations, I focus on what I can control: following the playbook, communicating clearly and frequently with the team, and documenting everything in real-time. I also believe in structured communication — 'I'm doing X, I'm seeing Y, I need Z' — rather than vague status updates. My experience [from labs/CTFs/simulations] has shown me that methodical beats fast-but-scattered every time."*

---

## Q33: How do you handle disagreement with a colleague about how to handle an incident?

**Answer framework:**

*"I'd present my reasoning with evidence, not just opinion — 'I believe we should contain now because I see active file encryption starting, which suggests the window for limiting damage is closing.' If the disagreement persists and time allows, I'd loop in the SOC Manager to make the call. In critical incidents, there's no room for ego — the fastest correct decision matters more than who's right. After the incident, I'd debrief openly and update the playbook if our disagreement revealed an ambiguity."*

---

## Q34: How do you keep yourself updated with the latest threats and security news?

**Answer:**

*"My daily routine includes:*
- *Reading SANS Internet Storm Center handlers diary — 5 min, daily threat overview*
- *Following Bleeping Computer for malware news and ransomware tracking*
- *Weekly read of The DFIR Report — real attack investigations*
- *Following key threat researchers on LinkedIn/Twitter (e.g., Mandiant, CrowdStrike researchers)*
- *Subscribed to CISA alerts and bulletins (free)*
- *Participating in security Discord communities*

*I also allocate 2-3 hours weekly for hands-on practice on LetsDefend or CyberDefenders to keep my practical skills sharp, not just my theoretical knowledge."*

---

## Q35: Where do you see yourself in 3 years in the SOC domain?

**Answer framework:**

*"In 3 years, I want to be operating at L3 / Threat Hunter level — moving from reactive monitoring to proactive threat hunting. I plan to achieve [GCIH / BTL2] certification within 18 months. I'm also interested in developing detection engineering skills — writing Sigma rules and contributing to improving the SOC's detection coverage. Long-term, I'm open to specializing further in DFIR or potentially moving toward a Security Engineering or Purple Team role."*

---

# 🎯 SOC MANAGER / LEAD QUESTIONS

*(For those applying to senior/lead positions)*

---

## Q36: How would you reduce alert fatigue in a SOC you manage?

**Answer:**

*"Alert fatigue is one of the top SOC problems. My approach:*
1. *Baseline → Tune: For every rule, measure FP rate. If > 20%, tune or retire the rule*
2. *Contextual enrichment: Use SOAR to auto-enrich alerts — analysts shouldn't Google every IOC manually*
3. *Tiered alerting: Not everything needs to wake up an analyst. Low-severity alerts can auto-close with conditions, or be batch-reviewed*
4. *Regular rule review cycle: Monthly review of top 10 alert sources — which are noisy? Which missed actual threats?*
5. *Threat-intelligence-driven rules: Rules based on current relevant TTPs fire more meaningfully than generic rules*
6. *Metrics: Track FP rate, escalation rate, analyst time per alert — data drives improvements*"*

---

## Q37: How do you measure SOC effectiveness?

**Answer:**

*"Key metrics I track:*
- **MTTD** (Mean Time to Detect): How quickly we find attacks — target < 1 hour
- **MTTR** (Mean Time to Respond): Containment speed — target < 4 hours P1
- **Dwell Time**: How long attackers are in environment before detection — industry avg 200+ days; good SOC targets < 24 hours
- **False Positive Rate**: Target < 15%; high FP = rule quality issue
- **SLA Compliance**: % incidents handled within contractual SLA — > 95%
- **Detection Coverage**: % of MITRE ATT&CK techniques with active detections — visualized via ATT&CK Navigator
- **Analyst capacity**: Alerts per analyst per shift — if too high, hiring or automation needed*

*I present these to management monthly with trend analysis, not just snapshots."*

---

# ⚡ QUICK FIRE ROUND

**Common short-answer questions:**

| Question | Answer |
|----------|--------|
| What port does HTTPS use? | 443 |
| What is a DMZ? | Demilitarized zone — network segment between public internet and internal network |
| What does SIEM stand for? | Security Information and Event Management |
| What is a zero-day? | Vulnerability unknown to vendor/public, with no patch available |
| What is a CVE? | Common Vulnerabilities and Exposures — standardized vulnerability ID |
| What is CVSS? | Common Vulnerability Scoring System — severity scoring (0-10) |
| What is threat intelligence? | Evidence-based knowledge about cyber threats and threat actors |
| What does TTPs stand for? | Tactics, Techniques, and Procedures |
| What is OSINT? | Open Source Intelligence — gathering info from public sources |
| What is a C2 server? | Command and Control — attacker's server that issues commands to malware |
| What is lateral movement? | Attacker moving from compromised system to other systems in the network |
| What is privilege escalation? | Gaining higher privileges than originally authorized |
| What is persistence? | Techniques attackers use to maintain access after reboots |
| What is a playbook? | Strategic guide for handling a specific type of incident |
| What is DFIR? | Digital Forensics and Incident Response |
| What is a hash? | Fixed-size output of a one-way mathematical function (MD5, SHA1, SHA256) |
| What is the difference between SHA1 and SHA256? | SHA256 is stronger, SHA1 is deprecated (collision attacks known) |
| What is a sandbox? | Isolated environment to safely execute and observe malware behavior |
| What does EDR stand for? | Endpoint Detection and Response |
| What is UEBA? | User and Entity Behavior Analytics |
| What port does RDP use? | 3389 |
| What port does SSH use? | 22 |
| What port does SMB use? | 445 (modern), 139 (legacy NetBIOS) |
| What is WMI? | Windows Management Instrumentation — used for remote management, also abused by attackers |
| What is a golden ticket attack? | Kerberos attack forging TGTs using the KRBTGT hash, giving domain-wide access |

---

> **💡 Interview Tips:**
> 1. Always mention documentation — interviewers love analysts who document everything
> 2. Use the word "escalate" correctly — know when to escalate, never sit on a real TP
> 3. Mention MITRE ATT&CK unprompted — it shows you think in frameworks
> 4. For scenario questions, think out loud — explain your reasoning process
> 5. Never say "I would Google it" — say "I would check our internal threat intel platform and VirusTotal"

