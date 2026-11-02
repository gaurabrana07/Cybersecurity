# 🛡️ Blue Teaming & Defensive Engineering — Cheatsheet
> **Night-Before Interview & Desk-Side Operational Reference**  
> **Covers:** Windows & Linux Forensics · Event IDs & Sysmon · Volatility 3 · KAPE & Zimmerman Tools · Sigma & YARA · Threat Hunting KQL/SPL · Containment One-Liners

---

## 🗺️ INCIDENT RESPONSE & ORDER OF VOLATILITY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 ORDER OF VOLATILITY (RFC 3227) — TOP DOWN                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Registers, CPU Cache, Architectural State (Lost in nanoseconds)          │
│ 2. Physical Memory (RAM): Running processes, unencrypted keys, active conns │
│ 3. Network State: ARP cache, routing tables, active TCP/UDP endpoints       │
│ 4. Ephemeral Filesystems: Swap space, pagefile.sys, /tmp, AppData\Local\Temp │
│ 5. Disk Non-Volatile Storage: NTFS ($MFT, $LogFile), Registry, Event Logs   │
│ 6. Remote Logging & Archival Backups: SIEM streams, cold repository copies  │
└─────────────────────────────────────────────────────────────────────────────┘

CRITICAL RULE: NEVER pull the power plug on a machine encrypted with BitLocker/FileVault.
               Capture volatile memory (RAM) first -> Triage artifacts -> Isolate.
```

---

## 🪟 WINDOWS FORENSIC ARTIFACTS MASTER MAP

| Forensic Question | Artifact | Disk Location | Parser Tool | Key Evidence Provided |
|---|---|---|---|---|
| **Did it run?** | **Prefetch** | `C:\Windows\Prefetch\*.pf` | `PECmd.exe` | Run count, first/last execution time, files/DLLs loaded in first 10s. |
| **Did it run?** | **ShimCache** | `SYSTEM` Hive (`AppCompatCache`) | `AppCompatCacheParser.exe` | File path, size, last modified time, execution flag. (Written on reboot). |
| **Did it run?** | **Amcache** | `C:\Windows\appcompat\Programs\Amcache.hve` | `AmcacheParser.exe` | **SHA-1 binary hash**, compile timestamp, file path. Persists after deletion! |
| **Did it run?** | **BAM / DAM** | `SYSTEM` Hive (`Services\bam\State\UserSettings\<SID>`) | `RegistryExplorer` | User SID execution timestamp (Windows 10/11 down to the second). |
| **Did it run?** | **UserAssist** | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | `RegistryExplorer` | GUI application execution count & last run time (ROT13 encoded). |
| **Was file open?** | **LNK Files** | `C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Recent\` | `JLECmd.exe` | Target file path, creation/mod timestamps of target, volume serial number. |
| **Was file open?** | **Jump Lists** | `AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\` | `JLECmd.exe` | Application taskbar recent history, pinned files, access timestamps. |
| **Folder traversal?** | **Shellbags** | `UsrClass.dat` & `NTUSER.DAT` | `ShellBagsExplorer` | Proves user navigated to specific folder (even if deleted or on USB). |
| **Filesystem actions**| **$MFT** | Root volume: `C:\$MFT` | `MFTECmd.exe` | All files/folders, `$SIA` vs `$FNA` timestamps (Timestomp detection). |
| **File changes?** | **$UsnJrnl** | `C:\$Extend\$UsnJrnl:$J` | `MFTECmd.exe` | Low-level file transactions (creation, deletion, rename, data overwrite). |

---

## 📋 WINDOWS LOGON TYPES CHEAT SHEET (EVENT ID 4624)

```
┌──────────┬──────────────────────────┬───────────────────────────────────────┐
│ LOGON    │ NAME                     │ INVESTIGATIVE SIGNIFICANCE            │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 2   │ Interactive              │ User logged on locally at physical    │
│          │                          │ keyboard/console.                     │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 3   │ Network                  │ Accessed via network (SMB, WMI, RPC,  │
│          │                          │ PsExec, shared folders). NORMAL for   │
│          │                          │ servers, SUSPICIOUS for workstations. │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 4   │ Batch                    │ Scheduled task execution.             │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 5   │ Service                  │ Service startup by Windows SCM.       │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 7   │ Unlock                   │ Workstation unlocked by user.         │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 9   │ NewCredentials           │ "runas /netonly" — Used by Mimikatz   │
│          │                          │ sekurlsa::pth (Pass-the-Hash).        │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 10  │ RemoteInteractive        │ RDP / Terminal Services session.      │
├──────────┼──────────────────────────┼───────────────────────────────────────┤
│ Type 11  │ CachedInteractive        │ Logged on with cached credentials     │
│          │                          │ (Domain Controller unreachable).      │
└──────────┴──────────────────────────┴───────────────────────────────────────┘
```

---

## 🔍 CRITICAL EVENT IDS QUICK LOOKUP

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       WINDOWS SECURITY EVENT LOGS                           │
├──────────────┬──────────────────────────────────────────────────────────────┤
│ EVENT ID     │ TACTICAL INVESTIGATIVE MEANING                               │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ 4624         │ Successful Account Logon (Check Logon Type & IP address)     │
│ 4625         │ Failed Account Logon (Spikes = Brute-force / Spraying)       │
│ 4648         │ Logon attempted with explicit credentials (runas)            │
│ 4672         │ Special privileges assigned to new logon (Administrator)     │
│ 4688         │ Process Creation (Must enable command-line auditing!)        │
│ 4697 / 7045  │ Service installed in the system (Common lateral persistence) │
│ 4720         │ A user account was created                                   │
│ 4728 / 4732  │ Account added to Security Global / Local Group (Privilege)   │
│ 4768         │ Kerberos TGT requested (Check for AS-REP pre-auth disabled)  │
│ 4769         │ Kerberos TGS requested (Ticket Encryption 0x17 = RC4 Roast)  │
│ 1102 / 104   │ Audit Log was cleared (Sec 1102, Sys 104 = Anti-forensics)   │
│ 4104         │ PowerShell Script Block Logging (De-obfuscates execution)    │
└──────────────┴──────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                            SYSMON EVENT LOGS                                │
├──────────────┬──────────────────────────────────────────────────────────────┤
│ SYSMON ID    │ TACTICAL INVESTIGATIVE MEANING                               │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ Event ID 1   │ Process Creation (Full path, command line, hashes, parent)   │
│ Event ID 3   │ Network Connection (Process mapped to external IP & Port)    │
│ Event ID 7   │ Image Loaded (DLL loading — tracks DLL Sideloading)          │
│ Event ID 8   │ CreateRemoteThread (Detects process injection)               │
│ Event ID 10  │ ProcessAccess (Detects LSASS credential dumping)             │
│ Event ID 11  │ FileCreate (Detects droppers, staging, ransomware extensions)│
│ Event ID 12  │ Registry Object Create/Delete                                │
│ Event ID 13  │ Registry Value Set (Persistence run keys, service configs)   │
│ Event ID 22  │ DNS Query (Detects C2 domains & DNS tunneling)               │
└──────────────┴──────────────────────────────────────────────────────────────┘
```

---

## 🧠 VOLATILITY 3 COMMAND CHEAT SHEET

```bash
# ═══ BASIC PROCESS TRIAGE ═══
vol -f mem.raw windows.pslist              # List active and unlinked processes
vol -f mem.raw windows.pstree              # Hierarchical process parent-child tree
vol -f mem.raw windows.psscan              # Scans pool allocations for terminated/hidden processes
vol -f mem.raw windows.cmdline             # Full command line arguments for every process

# ═══ NETWORK CONNECTIONS ═══
vol -f mem.raw windows.netscan             # Active and terminated TCP/UDP endpoints & sockets

# ═══ CODE INJECTION & MEMORY ANOMALIES ═══
vol -f mem.raw windows.malfind             # Scan VAD for executable unbacked allocations (RWX)
vol -f mem.raw -o ./dumps windows.malfind --dump --pid <PID>   # Dump injected shellcode
vol -f mem.raw windows.ldrmodules --pid <PID> # Detect unlinked/hidden DLLs in PEB
vol -f mem.raw windows.vadinfo --pid <PID> # Detailed memory protection flags for process

# ═══ CREDENTIAL & REGISTRY EXTRACTION ═══
vol -f mem.raw windows.hashdump            # Extract NTLM hashes from SAM hive
vol -f mem.raw windows.lsadump             # Extract LSA secrets (cached passwords, service creds)
vol -f mem.raw windows.registry.hivelist   # List active registry hives in memory
vol -f mem.raw windows.registry.printkey -K "Software\Microsoft\Windows\CurrentVersion\Run"

# ═══ DUMPING SUSPICIOUS BINARIES ═══
vol -f mem.raw -o ./out windows.dumpfiles --pid <PID> # Dump process executable image to disk
```

---

## 🛠️ ERIC ZIMMERMAN & KAPE CLI COMMANDS

```powershell
# ═══ KAPE TRIAGE ACQUISITION ═══
# Rapid live triage targeting critical artifacts (Prefetch, MFT, Registry, Logs)
kape.exe --tsource C: --tdest D:\TriageOut --target KapeTriage --flush --gui false

# ═══ MFT PARSING (MFTECmd) ═══
MFTECmd.exe -f "C:\Triage\$MFT" --csv "C:\Analysis\MFT" --csvf mft_parsed.csv

# ═══ PREFETCH PARSING (PECmd) ═══
PECmd.exe -d "C:\Windows\Prefetch" --csv "C:\Analysis\Prefetch"

# ═══ SHIMCACHE PARSING (AppCompatCacheParser) ═══
AppCompatCacheParser.exe -f "C:\Triage\Windows\System32\config\SYSTEM" --csv "C:\Analysis\Shim"

# ═══ AMCACHE PARSING (AmcacheParser) ═══
AmcacheParser.exe -f "C:\Triage\Windows\appcompat\Programs\Amcache.hve" --csv "C:\Analysis\Amcache"

# ═══ JUMP LISTS & LNK FILES (JLECmd & LECmd) ═══
JLECmd.exe -d "C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Recent" --csv "C:\Analysis\JumpLists"
LECmd.exe -d "C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Recent" --csv "C:\Analysis\LNK"

# ═══ EVTX LOG PARSING (EvtxECmd) ═══
EvtxECmd.exe -d "C:\Windows\System32\Winevt\Logs" --csv "C:\Analysis\EventLogs"
```

---

## 📜 SIGMA RULE SYNTAX & COMPILATION CHEAT

```yaml
# ═══ SIGMA TEMPLATE (Rule Anatomy) ═══
title: Suspicious Certutil Download Command
id: 5a25e24a-2598-444a-b92c-5674720970b5
status: production
description: Detects the use of certutil.exe to download files from remote URLs
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\certutil.exe'
        CommandLine|contains:
            - '-urlcache'
            - '-split'
    condition: selection
falsepositives:
    - Highly rare in enterprise environments. Inspect certificate enrollment scripts.
level: high
tags:
    - attack.defense_evasion
    - attack.t1105
```

```bash
# ═══ PY-SIGMA CLI CONVERSION ═══
# Convert to Microsoft Sentinel KQL
sigma convert -t kusto -p microsoft_sysmon certutil_rule.yml

# Convert to Splunk SPL
sigma convert -t splunk -p sysmon certutil_rule.yml

# Convert to Elastic Lucene / ES|QL
sigma convert -t elasticsearch certutil_rule.yml
```

---

## 🧬 YARA RULE PATTERN REFERENCE

```yara
rule Suspicious_Injected_Beacon_Pattern {
    meta:
        description = "Detects in-memory Cobalt Strike Beacon malleable HTTP indicators"
        author = "Corporate Blue Team"
        severity = "CRITICAL"
        threat = "COBALT_STRIKE"

    strings:
        // Wide and ASCII strings
        $str1 = "HTTP/1.1 200 OK" ascii
        $str2 = "%s.4444.%s" wide
        
        // Hex byte patterns with wildcards (? represents variable byte)
        $hex_code = { 8B 45 ?? 83 C0 ?? 89 45 ?? 8B 4D }
        
        // Regular expression pattern
        $re_c2 = /submit\.php\?id=[a-zA-Z0-9]{8,16}/

    condition:
        // Match condition against file or memory buffer
        (uint16(0) == 0x5A4D or uint32(0) == 0x464C457F) and // MZ or ELF Header
        filesize < 2MB and
        (2 of ($str*) or $hex_code or $re_c2)
}
```

---

## 🐧 LINUX LIVE FORENSICS QUICK COMMANDS

```bash
# ═══ ACTIVE PROCESSES & HIDDEN BINARIES ═══
ps auxefww                                # View full command line of all processes
ls -la /proc/*/exe | grep "(deleted)"     # Identify running processes whose binaries were wiped from disk

# ═══ NETWORK CONNECTIONS ═══
ss -tulpne                                # List listening and established TCP/UDP sockets with PIDs
lsof -i -P -n                             # Show all network sockets opened by process names

# ═══ LOGS & AUTHENTICATION ═══
tail -f /var/log/auth.log                 # Debian/Ubuntu SSH, sudo, and su authentication
tail -f /var/log/secure                   # RHEL/CentOS authentication log
last -F                                   # Historic user logins with full timestamps (parsed from /var/log/wtmp)
lastb                                     # Failed login attempts (parsed from /var/log/btmp)

# ═══ PERSISTENCE LOCATIONS ═══
crontab -l                                # User cron jobs
cat /etc/crontab; ls -la /etc/cron.*      # System cron schedules
ls -la /etc/systemd/system/*.service      # Systemd service persistence
ls -la /etc/systemd/system/*.timer        # Systemd timer persistence

# ═══ MODIFIED FILES IN LAST 24 HOURS ═══
find / -mtime -1 -type f 2>/dev/null | grep -v "/proc" | grep -v "/sys"

# ═══ LOADED KERNEL MODULES (ROOTKIT HUNT) ═══
lsmod
cat /proc/modules
```

---

## 🔎 THREAT HUNTING SPLUNK (SPL) & SENTINEL (KQL)

```kql
// ═══ SENTINEL KQL: HUNTING UNUSUAL PARENT PROCESSES ═══
DeviceProcessEvents
| where ProcessCommandLine has_any ("powershell", "cmd.exe", "wscript.exe")
| where InitiatingProcessFileName in~ ("wmiprvse.exe", "spoolsv.exe", "sqlservr.exe", "outlook.exe")
| project Timestamp, DeviceName, InitiatingProcessFileName, FileName, ProcessCommandLine, AccountName
| summarize Count = count() by InitiatingProcessFileName, FileName, ProcessCommandLine
| sort by Count asc

// ═══ SENTINEL KQL: DETECTING LSASS MEMORY ACCESS VIA HANDLE ACCESS ═══
DeviceEvents
| where ActionType == "OpenProcessApiCall"
| where TargetProcessFileName =~ "lsass.exe"
| where AdditionalFields contains "0x1010" or AdditionalFields contains "0x1F0FFF" // Read/VM rights
| where InitiatingProcessFileName !in~ ("MsMpEng.exe", "csfalconservice.exe")
```

```spl
# ═══ SPLUNK SPL: LONG-TAIL RARE COMMAND-LINE STACKING ═══
index=sysmon EventCode=1 (Image="*\\powershell.exe" OR Image="*\\cmd.exe")
| eval LowerCommand = lower(CommandLine)
| stats count, values(Computer) as Hosts by Image, LowerCommand
| sort + count
| head 25

# ═══ SPLUNK SPL: KERBEROASTING RC4 DETECTION (EVENT ID 4769) ═══
index=wineventlog EventCode=4769 Ticket_Encryption_Type="0x17"
| stats count by Target_Name, Service_Name, IpAddress
| where count > 10
| sort - count
```

---

## 🛑 EMERGENCY CONTAINMENT POWER-COMMANDS

```powershell
# ═══ INSTANT USER REVOACTION (MICROSOFT 365 / ENTRA ID) ═══
# Invalidate all active tokens, forcing re-authentication across all apps
Revoke-AzureADUserAllRefreshToken -ObjectId "<User-Object-ID>"

# ═══ PROCESS TERMINATION & SUSPENSION ═══
# Suspend process without killing it (preserves RAM state for analysis)
pssuspend.exe <PID>

# ═══ NETWORK ISOLATION (LOCAL FIREWALL EMERGENCY DROP) ═══
# Drop all inbound and outbound traffic except essential management
netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound
# Allow emergency forensic connection from analyst workstation IP
netsh advfirewall firewall add rule name="IR_Admin" dir=in action=allow protocol=TCP localport=5985 remoteip=192.168.1.50

# ═══ DUMP LIVE PROCESS MEMORY (PROCDUMP) ═══
procdump.exe -ma <PID> C:\IR_Triage\dump_<PID>.dmp
```

---

## 🔤 DEFENSIVE ACRONYMS QUICK GLOSSARY

| Acronym | Full Form | Tactical Defensive Meaning |
|---|---|---|
| **DFIR** | Digital Forensics & Incident Response | Post-breach surgical investigation, evidence recovery, root cause analysis. |
| **DaC** | Detection-as-Code | Writing, versioning, testing, and deploying detection rules via Git & CI/CD. |
| **VAD** | Virtual Address Descriptor | Memory tree mapping process memory allocations and permission flags. |
| **DEP / W^X** | Data Execution Prevention / Write XOR Execute | Prevents memory pages from being both writable and executable simultaneously. |
| **ASR** | Attack Surface Reduction | Windows rules blocking common exploit vectors (Office child processes, etc.). |
| **WDAC** | Windows Defender Application Control | Enterprise-grade executable whitelisting at the Windows kernel level. |
| **LAPS** | Local Administrator Password Solution | Automatically rotates unique local administrator passwords on every endpoint. |
| **AMSI** | Antimalware Scan Interface | Windows interface allowing AV/EDR to inspect de-obfuscated script buffers. |
| **HVCI** | Hypervisor-Protected Code Integrity | Virtualization-based security enforcing kernel memory safety (Credential Guard). |
| **MFT** | Master File Table | NTFS database holding metadata, file attributes, and timestamps for all files. |
| **USN** | Update Sequence Number | NTFS transaction journal recording low-level filesystem modifications. |
| **AiTM** | Adversary-in-the-Middle | Reverse proxy phishing (Evilginx2) capturing session tokens to bypass MFA. |
| **IOC** | Indicator of Compromise | Reactive artifact (hash, IP, domain) proving an intrusion occurred. |
| **TTP** | Tactics, Techniques & Procedures | Behavioral pattern of adversary tradecraft mapped to MITRE ATT&CK. |

---

*Corporate Edition | Blue Teaming & Defensive Security Series | Module 04 of 04*
