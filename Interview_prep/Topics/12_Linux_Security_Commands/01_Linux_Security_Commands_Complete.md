# 🐧 LINUX SECURITY COMMANDS - COMPLETE GUIDE
## TCS HackQuest Interview Preparation 2026

---

# 📋 TABLE OF CONTENTS

1. [Essential Commands Overview](#part-1-essential-commands-overview)
2. [User & Permission Management](#part-2-user--permission-management)
3. [Network Security Commands](#part-3-network-security-commands)
4. [Process & System Monitoring](#part-4-process--system-monitoring)
5. [Log Analysis & Forensics](#part-5-log-analysis--forensics)
6. [File Security & Integrity](#part-6-file-security--integrity)
7. [Firewall & IPTables](#part-7-firewall--iptables)
8. [Security Scanning & Auditing](#part-8-security-scanning--auditing)
9. [Incident Response Commands](#part-9-incident-response-commands)
10. [Interview Questions & Answers](#part-10-interview-questions--answers)

---

# PART 1: ESSENTIAL COMMANDS OVERVIEW

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LINUX SECURITY COMMANDS CHEATSHEET                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  USER INFO          │  NETWORK           │  PROCESSES        │  FILES      │
│  ─────────────────  │  ────────────────  │  ───────────────  │  ────────── │
│  whoami             │  netstat -tulpn    │  ps aux           │  ls -la     │
│  id                 │  ss -tulpn         │  top / htop       │  find       │
│  who / w            │  ifconfig / ip a   │  pstree           │  locate     │
│  last               │  nmap              │  lsof             │  file       │
│  lastlog            │  tcpdump           │  strace           │  strings    │
│  cat /etc/passwd    │  iptables -L       │  kill / killall   │  md5sum     │
│  cat /etc/shadow    │  curl / wget       │  nice / renice    │  sha256sum  │
│                                                                             │
│  LOGS               │  PERMISSIONS       │  SERVICES         │  SECURITY   │
│  ─────────────────  │  ────────────────  │  ───────────────  │  ────────── │
│  journalctl         │  chmod             │  systemctl        │  chroot     │
│  dmesg              │  chown             │  service          │  sudo       │
│  tail -f /var/log/* │  chgrp             │  crontab          │  su         │
│  grep               │  umask             │  at               │  passwd     │
│  awk / sed          │  getfacl/setfacl   │  init             │  ssh-keygen │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Command Categories by Use Case

### 🔴 INCIDENT RESPONSE (Use when system is compromised)
```bash
# Who is logged in RIGHT NOW?
w
who

# What processes are running?
ps aux
ps auxf  # with tree view

# What network connections exist?
netstat -tulpn
ss -tulpn

# What files changed recently?
find / -mtime -1 -type f 2>/dev/null

# Check for suspicious cron jobs
crontab -l
cat /etc/crontab
ls -la /etc/cron.*
```

### 🟡 DAILY SECURITY MONITORING
```bash
# Failed login attempts
grep "Failed password" /var/log/auth.log

# Currently logged in users
who

# Listening services
ss -tulpn

# System resource usage
top
df -h
free -m
```

### 🟢 SECURITY HARDENING
```bash
# Find SUID files (potential privilege escalation)
find / -perm -4000 -type f 2>/dev/null

# Find world-writable files
find / -perm -002 -type f 2>/dev/null

# Check open ports
nmap -sT -O localhost

# Review firewall rules
iptables -L -n -v
```

---

# PART 2: USER & PERMISSION MANAGEMENT

---

## 2.1 User Information Commands

### `whoami` - Current User
```bash
$ whoami
gaurab

# Use case: Verify which user you're operating as
# Security: Always check before running privileged commands
```

### `id` - User ID and Groups
```bash
$ id
uid=1000(gaurab) gid=1000(gaurab) groups=1000(gaurab),27(sudo),999(docker)

$ id root
uid=0(root) gid=0(root) groups=0(root)

# Security insight: Check if user has dangerous groups (sudo, docker, wheel)
# Docker group = effectively root access!
```

### `who` / `w` - Logged In Users
```bash
$ who
gaurab   pts/0        2026-02-24 09:15 (192.168.1.100)
admin    pts/1        2026-02-24 10:30 (10.0.0.50)

$ w
 11:22:33 up 5 days,  3:14,  2 users,  load average: 0.15, 0.10, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
gaurab   pts/0    192.168.1.100    09:15    0.00s  0.05s  0.00s w
admin    pts/1    10.0.0.50        10:30    52:10  0.02s  0.02s -bash

# Security: Detect unauthorized logins
# Check for: Unknown users, unusual IPs, odd login times
```

### `last` - Login History
```bash
$ last
gaurab   pts/0        192.168.1.100    Mon Feb 24 09:15   still logged in
root     pts/1        192.168.1.50     Sun Feb 23 03:22 - 03:45  (00:23)
reboot   system boot  5.4.0-42-generic Sun Feb 23 00:00

$ last -f /var/log/btmp  # Failed logins (needs root)
admin    ssh:notty    203.0.113.50     Mon Feb 24 02:15 - 02:15  (00:00)

# Security: Look for:
# - Root logins from remote IPs
# - Logins at unusual times (3 AM?)
# - Failed login attempts (btmp)
```

### `lastlog` - Last Login for All Users
```bash
$ lastlog
Username         Port     From             Latest
root             pts/0    192.168.1.1      Mon Feb 24 08:00:00 +0530 2026
daemon                                     **Never logged in**
gaurab           pts/1    192.168.1.100    Mon Feb 24 09:15:00 +0530 2026

# Security: Identify accounts that shouldn't be logging in
# System accounts should show "Never logged in"
```

---

## 2.2 User & Password Files

### `/etc/passwd` - User Accounts
```bash
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
gaurab:x:1000:1000:Gaurab Rana:/home/gaurab:/bin/bash
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false

# Format: username:x:UID:GID:comment:home:shell
# Security checks:
# - UID 0 should only be root
# - System accounts should have /nologin or /false shell
# - Look for unexpected users
```

### Check for UID 0 Users (Root Equivalents)
```bash
$ awk -F: '($3 == "0") {print}' /etc/passwd
root:x:0:0:root:/root:/bin/bash

# Security: If any user besides root has UID 0, investigate!
# Attackers sometimes create backdoor root accounts
```

### `/etc/shadow` - Password Hashes (Root Only)
```bash
$ sudo cat /etc/shadow
root:$6$xyz...:18645:0:99999:7:::
gaurab:$6$abc...:18650:0:99999:7:::
mysql:!:18000:0:99999:7:::

# Format: username:hash:lastchange:min:max:warn:inactive:expire
# Security:
# - "!" or "*" = account disabled (good for system accounts)
# - Empty second field = NO PASSWORD (very bad!)
# - Check password age
```

### Find Accounts with No Password
```bash
$ sudo awk -F: '($2 == "") {print $1}' /etc/shadow
# Should return nothing! Any result is CRITICAL vulnerability
```

---

## 2.3 Permission Commands

### `chmod` - Change Permissions
```bash
# Symbolic mode
chmod u+x script.sh      # Add execute for owner
chmod go-w file.txt      # Remove write for group/others
chmod a+r file.txt       # Add read for all

# Numeric mode
chmod 755 script.sh      # rwxr-xr-x
chmod 644 file.txt       # rw-r--r--
chmod 600 secret.key     # rw------- (private key)
chmod 400 authorized_keys # r-------- (most secure)

# Permission numbers:
# 4 = read (r)
# 2 = write (w)
# 1 = execute (x)
# 7 = 4+2+1 = rwx
# 6 = 4+2 = rw-
# 5 = 4+1 = r-x
# 0 = ---
```

### Permission Meanings
```
┌─────────────────────────────────────────────────────────────┐
│              FILE PERMISSIONS EXPLAINED                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  -rwxr-xr-x  1  gaurab  gaurab  4096  Feb 24 10:00  file   │
│  │└┬┘└┬┘└┬┘     └──┬──┘ └──┬──┘                             │
│  │ │  │  │         │       │                                │
│  │ │  │  │         │       └── Group owner                  │
│  │ │  │  │         └── User owner                           │
│  │ │  │  └── Others (everyone else): r-x                    │
│  │ │  └── Group: r-x                                        │
│  │ └── Owner: rwx                                           │
│  └── File type (- = file, d = directory, l = link)         │
│                                                             │
│  For Directories:                                           │
│  r = list contents (ls)                                     │
│  w = create/delete files                                    │
│  x = enter directory (cd)                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### `chown` - Change Ownership
```bash
chown gaurab file.txt           # Change owner
chown gaurab:developers file.txt  # Change owner and group
chown -R gaurab:gaurab /home/gaurab  # Recursive

# Security use: Fix ownership after incident
sudo chown root:root /etc/passwd
sudo chmod 644 /etc/passwd
```

### Special Permissions (SUID, SGID, Sticky)
```bash
# SUID (4): Execute as file owner
chmod u+s /usr/bin/passwd    # or chmod 4755
ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root ...   # Note the 's'

# Why passwd needs SUID:
# Regular users can change their password
# But /etc/shadow requires root to write
# SUID lets passwd run as root temporarily

# SGID (2): Execute as file group / Inherit directory group
chmod g+s /shared/project    # or chmod 2755

# Sticky bit (1): Only owner can delete in directory
chmod +t /tmp                # or chmod 1777
ls -ld /tmp
drwxrwxrwt 10 root root ...  # Note the 't'
```

### Find SUID/SGID Files (Security Audit)
```bash
# Find all SUID files
find / -perm -4000 -type f 2>/dev/null

# Find all SGID files
find / -perm -2000 -type f 2>/dev/null

# Common legitimate SUID binaries:
# /usr/bin/passwd, /usr/bin/sudo, /usr/bin/su
# /usr/bin/ping (sometimes)

# DANGEROUS if SUID:
# /bin/bash, /bin/sh, /usr/bin/vim, /usr/bin/find
# These can be used for privilege escalation!
```

---

## 2.4 `sudo` Configuration

### Check sudo Privileges
```bash
$ sudo -l
User gaurab may run the following commands on server:
    (ALL : ALL) ALL

# More restrictive example:
User developer may run the following commands:
    (root) NOPASSWD: /usr/bin/systemctl restart nginx
    (root) /usr/bin/less /var/log/nginx/*
```

### `/etc/sudoers` Security
```bash
# NEVER edit directly - use visudo
sudo visudo

# Dangerous configurations:
gaurab ALL=(ALL) NOPASSWD: ALL  # Too permissive
%developers ALL=(ALL) /bin/bash  # Gives root shell!

# Better configurations:
%webadmins ALL=(root) /usr/bin/systemctl restart nginx
%dbadmins ALL=(postgres) /usr/bin/psql
```

---

# PART 3: NETWORK SECURITY COMMANDS

---

## 3.1 Network Information

### `ifconfig` / `ip` - Interface Configuration
```bash
# Old way (deprecated but still common)
$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>
        inet 192.168.1.100  netmask 255.255.255.0
        inet6 fe80::1  prefixlen 64
        ether 00:11:22:33:44:55

# Modern way
$ ip a
$ ip addr show
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
    inet6 fe80::1/64 scope link

# Security: Check for unexpected interfaces (tun, tap = VPN/tunnels)
```

### `netstat` / `ss` - Network Connections
```bash
# Show listening ports (most important for security!)
$ netstat -tulpn
Proto  Local Address      Foreign Address    State       PID/Program
tcp    0.0.0.0:22         0.0.0.0:*          LISTEN      1234/sshd
tcp    0.0.0.0:80         0.0.0.0:*          LISTEN      5678/nginx
tcp    127.0.0.1:3306     0.0.0.0:*          LISTEN      9012/mysqld

# Modern alternative (faster)
$ ss -tulpn

# All connections including established
$ netstat -an
$ ss -an

# Options:
# -t = TCP
# -u = UDP  
# -l = Listening
# -p = Show process (needs root for all)
# -n = Numeric (don't resolve names, faster)
```

### Security Analysis of netstat Output
```bash
# What to look for:
$ ss -tulpn

# GOOD:
tcp    127.0.0.1:3306    LISTEN   # MySQL on localhost only

# CONCERNING:
tcp    0.0.0.0:3306      LISTEN   # MySQL exposed to all interfaces!
tcp    0.0.0.0:6379      LISTEN   # Redis exposed (usually no auth)

# SUSPICIOUS:
tcp    0.0.0.0:4444      LISTEN   # Common reverse shell port
tcp    0.0.0.0:31337     LISTEN   # Known backdoor port

# Check suspicious connections:
ss -an | grep ESTABLISHED
# Look for connections to unknown IPs
```

### `lsof` - List Open Files/Connections
```bash
# What's using port 80?
$ sudo lsof -i :80
COMMAND   PID   USER   FD   NAME
nginx     1234  root   tcp  *:80 (LISTEN)
nginx     1235  www    tcp  192.168.1.100:80->10.0.0.5:54321

# All network connections by a process
$ sudo lsof -i -p 1234

# Files opened by a user
$ sudo lsof -u gaurab

# What process has a file open?
$ sudo lsof /var/log/auth.log
```

---

## 3.2 Network Scanning & Analysis

### `nmap` - Network Scanner
```bash
# Basic port scan
nmap 192.168.1.1

# Scan specific ports
nmap -p 22,80,443 192.168.1.1

# Scan port range
nmap -p 1-1000 192.168.1.1

# Service version detection
nmap -sV 192.168.1.1

# OS detection (needs root)
sudo nmap -O 192.168.1.1

# Aggressive scan (loud, detectable)
sudo nmap -A 192.168.1.1

# Stealth SYN scan (needs root)
sudo nmap -sS 192.168.1.1

# Scan entire subnet
nmap 192.168.1.0/24

# UDP scan (slow)
sudo nmap -sU -p 53,123,161 192.168.1.1

# Script scan for vulnerabilities
nmap --script vuln 192.168.1.1

# Output to file
nmap -oN scan_results.txt 192.168.1.1
nmap -oX scan_results.xml 192.168.1.1  # XML format
```

### `tcpdump` - Packet Capture
```bash
# Capture all traffic on interface
sudo tcpdump -i eth0

# Capture specific port
sudo tcpdump -i eth0 port 80

# Capture specific host
sudo tcpdump -i eth0 host 192.168.1.50

# Capture and save to file
sudo tcpdump -i eth0 -w capture.pcap

# Read saved capture
tcpdump -r capture.pcap

# Show ASCII content
sudo tcpdump -i eth0 -A port 80

# Capture only TCP SYN packets
sudo tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'

# Useful filters:
sudo tcpdump -i eth0 'src 192.168.1.50'      # Source IP
sudo tcpdump -i eth0 'dst port 443'           # Destination port
sudo tcpdump -i eth0 'tcp and port 22'        # SSH traffic
sudo tcpdump -i eth0 'icmp'                   # Ping traffic
```

### `curl` / `wget` - HTTP Testing
```bash
# Basic request
curl https://example.com

# Show headers
curl -I https://example.com

# POST request
curl -X POST -d "user=admin&pass=test" https://example.com/login

# Follow redirects
curl -L https://example.com

# Save output
curl -o file.html https://example.com
wget https://example.com/file.txt

# Test for security headers
curl -I https://example.com | grep -E "Strict-Transport|Content-Security|X-Frame"

# Send custom headers
curl -H "Authorization: Bearer token123" https://api.example.com
```

---

## 3.3 DNS & Host Resolution

### DNS Commands
```bash
# DNS lookup
nslookup example.com
dig example.com

# Reverse DNS lookup
dig -x 8.8.8.8
nslookup 8.8.8.8

# Query specific record types
dig MX example.com      # Mail servers
dig NS example.com      # Name servers
dig TXT example.com     # TXT records (SPF, DKIM)
dig ANY example.com     # All records

# Query specific DNS server
dig @8.8.8.8 example.com

# DNS zone transfer (security test)
dig axfr @ns1.example.com example.com
# Should fail on properly configured servers!
```

### `/etc/hosts` - Local DNS Override
```bash
$ cat /etc/hosts
127.0.0.1       localhost
192.168.1.10    webserver.local
10.0.0.5        database.internal

# Security: Attackers may modify this for redirection
# Check for unexpected entries!
```

---

# PART 4: PROCESS & SYSTEM MONITORING

---

## 4.1 Process Commands

### `ps` - Process Status
```bash
# Show all processes
ps aux
ps -ef

# Tree view (shows parent-child)
ps auxf
pstree

# Find specific process
ps aux | grep nginx
pgrep nginx        # Returns PID only
pidof nginx        # Returns PID only

# Detailed output columns:
# USER: Process owner
# PID: Process ID
# %CPU: CPU usage
# %MEM: Memory usage
# VSZ: Virtual memory
# RSS: Physical memory
# TTY: Terminal
# STAT: State (R=running, S=sleeping, Z=zombie)
# START: Start time
# COMMAND: Command line
```

### Security Analysis of Processes
```bash
# Find processes running as root
ps aux | awk '$1=="root" {print}'

# Find suspicious processes
ps aux | grep -E "nc|netcat|ncat|/tmp|/dev/shm"

# Check for hidden processes (comparing methods)
ps aux | wc -l
ls -1 /proc | grep -E "^[0-9]+$" | wc -l
# Numbers should be similar; big difference = hidden processes

# Find process by open port
sudo lsof -i :4444  # Check what's on suspicious port
```

### `top` / `htop` - Real-time Monitoring
```bash
$ top
# Key columns: PID, USER, %CPU, %MEM, COMMAND
# Press:
#   k = kill process
#   u = filter by user
#   1 = show individual CPUs
#   q = quit

$ htop  # Better version with colors
# Features: Mouse support, tree view, search

# Security: Watch for:
# - High CPU processes (cryptomining?)
# - Processes by unexpected users
# - Strange command names
```

### `lsof` - What's a Process Doing?
```bash
# All files opened by process
sudo lsof -p 1234

# Network connections of process
sudo lsof -i -p 1234

# Files opened by user
sudo lsof -u hacker

# What's accessing a file?
sudo lsof /etc/passwd
```

### `strace` - System Call Tracing
```bash
# Trace a running process
sudo strace -p 1234

# Trace a command
strace ls

# Trace file operations
strace -e trace=file ls

# Trace network operations
strace -e trace=network curl example.com

# Security use: What files is malware accessing?
sudo strace -e trace=open,read,write -p 1234
```

---

## 4.2 System Information

### System Details
```bash
# Hostname
hostname
hostnamectl

# OS version
cat /etc/os-release
uname -a

# Kernel version
uname -r

# CPU info
lscpu
cat /proc/cpuinfo

# Memory
free -m
cat /proc/meminfo

# Disk usage
df -h
du -sh /var/log

# Uptime
uptime
```

### Hardware & Device Info
```bash
# All hardware
lshw
lspci          # PCI devices
lsusb          # USB devices
lsblk          # Block devices (disks)

# Security: Check for unexpected USB devices
lsusb
```

---

# PART 5: LOG ANALYSIS & FORENSICS

---

## 5.1 Important Log Files

### Log Locations
```
┌─────────────────────────────────────────────────────────────┐
│              CRITICAL LOG FILES                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  /var/log/auth.log     - Authentication (SSH, sudo, login) │
│  /var/log/secure       - Same on RHEL/CentOS               │
│  /var/log/syslog       - General system messages           │
│  /var/log/messages     - Same on RHEL/CentOS               │
│  /var/log/kern.log     - Kernel messages                   │
│  /var/log/dmesg        - Boot messages                     │
│  /var/log/faillog      - Failed logins                     │
│  /var/log/lastlog      - Last login info                   │
│  /var/log/wtmp         - Login records (binary, use last)  │
│  /var/log/btmp         - Bad login attempts (use lastb)    │
│  /var/log/cron         - Cron job logs                     │
│                                                             │
│  Application Logs:                                          │
│  /var/log/apache2/     - Apache logs                       │
│  /var/log/nginx/       - Nginx logs                        │
│  /var/log/mysql/       - MySQL logs                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 5.2 Log Analysis Commands

### `grep` - Search Logs
```bash
# Find failed SSH logins
grep "Failed password" /var/log/auth.log

# Find successful logins
grep "Accepted" /var/log/auth.log

# Find sudo commands
grep "sudo:" /var/log/auth.log

# Case insensitive
grep -i "error" /var/log/syslog

# Show line numbers
grep -n "Failed" /var/log/auth.log

# Count occurrences
grep -c "Failed password" /var/log/auth.log

# Show lines before/after match
grep -B5 -A5 "Failed" /var/log/auth.log

# Multiple patterns
grep -E "Failed|Invalid|error" /var/log/auth.log

# Invert match (show lines NOT matching)
grep -v "INFO" /var/log/app.log

# Recursive search
grep -r "password" /var/log/
```

### `tail` / `head` - View Logs
```bash
# Last 10 lines
tail /var/log/auth.log

# Last 100 lines
tail -n 100 /var/log/auth.log

# Follow log in real-time (essential for monitoring!)
tail -f /var/log/auth.log

# Follow multiple files
tail -f /var/log/auth.log /var/log/syslog

# First 10 lines
head /var/log/auth.log
```

### `journalctl` - Systemd Logs
```bash
# All logs
journalctl

# Follow mode
journalctl -f

# Since boot
journalctl -b

# Specific unit
journalctl -u nginx
journalctl -u sshd

# Time range
journalctl --since "2026-02-24 08:00" --until "2026-02-24 12:00"
journalctl --since "1 hour ago"
journalctl --since yesterday

# Priority (errors and above)
journalctl -p err

# Kernel messages
journalctl -k

# Security relevant
journalctl _TRANSPORT=audit
```

### `awk` - Advanced Log Processing
```bash
# Print specific columns
awk '{print $1, $2, $3}' /var/log/auth.log

# Filter by field
awk '$9 == 404 {print}' /var/log/nginx/access.log

# Sum values
awk '{sum += $10} END {print sum}' /var/log/nginx/access.log

# Count IPs hitting server
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head

# Find brute force (more than 10 failed logins per IP)
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn | awk '$1 > 10'
```

### `sed` - Stream Editor
```bash
# Replace text
sed 's/old/new/g' file.txt

# Delete lines matching pattern
sed '/DEBUG/d' app.log

# Print specific lines
sed -n '10,20p' file.txt

# Remove blank lines
sed '/^$/d' file.txt
```

---

## 5.3 Security-Specific Log Analysis

### Find SSH Brute Force Attacks
```bash
# Count failed logins by IP
grep "Failed password" /var/log/auth.log | \
    awk '{print $(NF-3)}' | \
    sort | uniq -c | sort -rn | head -20

# Example output:
#    823  192.168.1.50
#    412  10.0.0.100
#     56  203.0.113.15

# Same with timestamp
grep "Failed password" /var/log/auth.log | \
    awk '{print $1, $2, $3, $(NF-3)}' | head
```

### Find Successful Root Logins
```bash
grep "session opened for user root" /var/log/auth.log
grep "Accepted.*root" /var/log/auth.log
```

### Check Sudo Usage
```bash
# All sudo commands
grep "COMMAND=" /var/log/auth.log

# Sudo failures
grep "authentication failure" /var/log/auth.log | grep sudo

# Sudo by specific user
grep "sudo:.*gaurab" /var/log/auth.log
```

### Web Server Log Analysis
```bash
# Top 20 IPs accessing server
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -20

# Find 404 errors (scanning?)
grep '" 404 ' /var/log/nginx/access.log

# Find SQL injection attempts
grep -E "union|select|insert|update|delete|drop|'--|1=1" /var/log/nginx/access.log

# Find potential XSS attempts
grep -i "<script" /var/log/nginx/access.log

# Requests per hour
awk '{print $4}' /var/log/nginx/access.log | cut -d: -f2 | sort | uniq -c
```

---

# PART 6: FILE SECURITY & INTEGRITY

---

## 6.1 File Search Commands

### `find` - Powerful File Search
```bash
# Find by name
find / -name "passwd" 2>/dev/null
find / -name "*.conf" 2>/dev/null

# Find by permission (SUID files - critical!)
find / -perm -4000 -type f 2>/dev/null    # SUID
find / -perm -2000 -type f 2>/dev/null    # SGID
find / -perm -0777 -type f 2>/dev/null    # World-writable

# Find by user/group
find / -user root -type f 2>/dev/null
find / -group shadow -type f 2>/dev/null

# Find by time (forensics!)
find / -mtime -1 -type f 2>/dev/null      # Modified in last day
find / -mmin -60 -type f 2>/dev/null      # Modified in last hour
find / -atime -1 -type f 2>/dev/null      # Accessed in last day
find / -ctime -1 -type f 2>/dev/null      # Changed in last day

# Find by size
find / -size +100M -type f 2>/dev/null    # Larger than 100MB
find / -size 0 -type f 2>/dev/null        # Empty files

# Find and execute command
find / -name "*.bak" -exec rm {} \;       # Delete backups
find / -perm -4000 -exec ls -l {} \;      # List SUID files

# Find writable directories in PATH (security risk!)
echo $PATH | tr ':' '\n' | xargs -I {} find {} -writable 2>/dev/null
```

### `locate` - Fast File Search
```bash
# Fast search (uses database)
locate passwd
locate "*.conf"

# Update database
sudo updatedb

# Case insensitive
locate -i PASSWORD
```

---

## 6.2 File Integrity & Hashing

### Hash Commands
```bash
# MD5 (not secure, but fast)
md5sum file.txt

# SHA-256 (secure)
sha256sum file.txt

# SHA-512
sha512sum file.txt

# Verify hash
echo "abc123hash  file.txt" | sha256sum -c

# Hash multiple files
sha256sum /usr/bin/* > hashes.txt
sha256sum -c hashes.txt  # Verify later

# Hash directory contents
find /usr/bin -type f -exec sha256sum {} \; > dir_hashes.txt
```

### File Type Analysis
```bash
# Determine file type
file suspicious_file
file /bin/bash

# Example outputs:
# malware.exe: PE32 executable (GUI) Intel 80386
# script.sh: Bourne-Again shell script, ASCII text
# image.jpg: JPEG image data, JFIF standard

# Extract strings from binary
strings /bin/bash | head
strings malware | grep -i "password\|http\|connect"

# Hex dump
hexdump -C file | head
xxd file | head
```

### Check File Attributes
```bash
# List attributes
lsattr file.txt

# Set immutable (can't delete, even as root)
sudo chattr +i important.conf

# Remove immutable
sudo chattr -i important.conf

# Attributes:
# i = immutable (can't be modified)
# a = append only
# s = secure deletion
# u = undeletable
```

---

## 6.3 Integrity Monitoring

### AIDE (Advanced Intrusion Detection Environment)
```bash
# Initialize database
sudo aide --init

# Check for changes
sudo aide --check

# Update database after legitimate changes
sudo aide --update
```

### Tripwire
```bash
# Initialize
sudo tripwire --init

# Check
sudo tripwire --check

# Update policy
sudo tripwire --update-policy
```

### Manual Integrity Check
```bash
# Create baseline
find /usr/bin -type f -exec sha256sum {} \; > /root/baseline.txt

# Later, compare
sha256sum -c /root/baseline.txt 2>&1 | grep -v "OK$"
```

---

# PART 7: FIREWALL & IPTABLES

---

## 7.1 `iptables` Basics

### View Rules
```bash
# List all rules
sudo iptables -L
sudo iptables -L -n -v    # Numeric, verbose

# List with line numbers
sudo iptables -L --line-numbers

# List specific chain
sudo iptables -L INPUT -n -v
```

### iptables Structure
```
┌─────────────────────────────────────────────────────────────┐
│                   IPTABLES CHAINS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INPUT    - Packets destined for this machine              │
│  OUTPUT   - Packets originating from this machine          │
│  FORWARD  - Packets routed through this machine            │
│                                                             │
│  Actions (targets):                                         │
│  ACCEPT   - Allow the packet                               │
│  DROP     - Silently discard                               │
│  REJECT   - Discard and send error response                │
│  LOG      - Log the packet                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Common Rules
```bash
# Allow established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH (port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow from specific IP
sudo iptables -A INPUT -s 192.168.1.100 -j ACCEPT

# Block specific IP
sudo iptables -A INPUT -s 10.0.0.50 -j DROP

# Allow localhost
sudo iptables -A INPUT -i lo -j ACCEPT

# Drop everything else (CAREFUL!)
sudo iptables -A INPUT -j DROP

# Delete a rule (by line number)
sudo iptables -D INPUT 3

# Flush all rules
sudo iptables -F
```

### Save & Restore Rules
```bash
# Save current rules
sudo iptables-save > /etc/iptables.rules

# Restore rules
sudo iptables-restore < /etc/iptables.rules

# Debian/Ubuntu persistent
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

---

## 7.2 UFW (Uncomplicated Firewall)

```bash
# Enable/disable
sudo ufw enable
sudo ufw disable

# Status
sudo ufw status
sudo ufw status verbose

# Default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow port
sudo ufw allow 22
sudo ufw allow 22/tcp
sudo ufw allow 22:25/tcp  # Range

# Allow application
sudo ufw allow 'Nginx Full'
sudo ufw allow 'OpenSSH'

# Allow from IP
sudo ufw allow from 192.168.1.0/24

# Deny
sudo ufw deny 23

# Delete rule
sudo ufw delete allow 80

# Logging
sudo ufw logging on
```

---

## 7.3 `firewalld` (RHEL/CentOS)

```bash
# Status
sudo firewall-cmd --state
sudo firewall-cmd --list-all

# Add service
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent

# Add port
sudo firewall-cmd --add-port=8080/tcp --permanent

# Remove
sudo firewall-cmd --remove-service=http --permanent

# Reload
sudo firewall-cmd --reload

# Zones
sudo firewall-cmd --get-zones
sudo firewall-cmd --zone=public --list-all
```

---

# PART 8: SECURITY SCANNING & AUDITING

---

## 8.1 Vulnerability Scanning

### Lynis - Security Auditing
```bash
# Install
sudo apt install lynis

# Run audit
sudo lynis audit system

# Scan and save report
sudo lynis audit system --report-file /tmp/lynis-report.txt

# Quick checks
sudo lynis show details BOOT-5122  # Specific test details
```

### Chkrootkit - Rootkit Scanner
```bash
# Install
sudo apt install chkrootkit

# Run scan
sudo chkrootkit

# Quiet mode (only show infected)
sudo chkrootkit -q
```

### RKHunter - Rootkit Hunter
```bash
# Install
sudo apt install rkhunter

# Update database
sudo rkhunter --update

# Run check
sudo rkhunter --check

# Check specific
sudo rkhunter --check --skip-keypress
```

### ClamAV - Antivirus
```bash
# Install
sudo apt install clamav clamav-daemon

# Update definitions
sudo freshclam

# Scan directory
clamscan -r /home

# Scan and remove infected
clamscan -r --remove /home

# Scan and move infected
clamscan -r --move=/quarantine /home
```

---

## 8.2 System Hardening Checks

### Check Running Services
```bash
# List all services
systemctl list-units --type=service

# Check enabled services
systemctl list-unit-files --state=enabled

# Disable unnecessary services
sudo systemctl disable bluetooth
sudo systemctl disable cups

# Stop service
sudo systemctl stop telnet
```

### Check Open Ports & Firewall
```bash
# Open ports
ss -tulpn
nmap -sT localhost

# Firewall status
sudo iptables -L -n
sudo ufw status
```

### Check for Updates
```bash
# Debian/Ubuntu
sudo apt update
apt list --upgradable
sudo apt upgrade

# RHEL/CentOS
sudo yum check-update
sudo yum update

# Security updates only (Ubuntu)
sudo apt install unattended-upgrades
sudo unattended-upgrades --dry-run
```

---

# PART 9: INCIDENT RESPONSE COMMANDS

---

## 9.1 Initial Response Checklist

```bash
#!/bin/bash
# Incident Response Data Collection Script

echo "=== SYSTEM INFO ===" >> ir_report.txt
date >> ir_report.txt
hostname >> ir_report.txt
uname -a >> ir_report.txt

echo "=== LOGGED IN USERS ===" >> ir_report.txt
w >> ir_report.txt
who >> ir_report.txt

echo "=== LAST LOGINS ===" >> ir_report.txt
last -n 50 >> ir_report.txt

echo "=== PROCESSES ===" >> ir_report.txt
ps auxf >> ir_report.txt

echo "=== NETWORK CONNECTIONS ===" >> ir_report.txt
ss -tulpn >> ir_report.txt
ss -an >> ir_report.txt

echo "=== OPEN FILES ===" >> ir_report.txt
lsof -i >> ir_report.txt

echo "=== CRON JOBS ===" >> ir_report.txt
crontab -l >> ir_report.txt 2>&1
cat /etc/crontab >> ir_report.txt
ls -la /etc/cron.* >> ir_report.txt

echo "=== RECENTLY MODIFIED FILES ===" >> ir_report.txt
find / -mtime -1 -type f 2>/dev/null >> ir_report.txt

echo "=== SUID FILES ===" >> ir_report.txt
find / -perm -4000 -type f 2>/dev/null >> ir_report.txt

echo "=== /tmp and /dev/shm ===" >> ir_report.txt
ls -la /tmp >> ir_report.txt
ls -la /dev/shm >> ir_report.txt
```

---

## 9.2 Evidence Collection

### Memory Acquisition
```bash
# Install LiME
git clone https://github.com/504ensicsLabs/LiME

# Dump memory
sudo insmod lime.ko "path=/evidence/memory.lime format=lime"

# Alternative with dd (less reliable)
sudo dd if=/dev/mem of=/evidence/memory.raw bs=1M
```

### Disk Forensics
```bash
# Create forensic image
sudo dd if=/dev/sda of=/evidence/disk.img bs=4M status=progress

# Mount read-only for analysis
sudo mount -o ro,loop /evidence/disk.img /mnt/evidence

# Check deleted files (install sleuthkit)
fls -r -d /dev/sda1
icat /dev/sda1 12345 > recovered_file
```

### Network Evidence
```bash
# Capture traffic
sudo tcpdump -i eth0 -w /evidence/traffic.pcap

# Get connections at time of incident
ss -tulpn > /evidence/connections_$(date +%s).txt
netstat -an > /evidence/netstat_$(date +%s).txt
```

---

## 9.3 Malware Analysis Basics

### Static Analysis
```bash
# File type
file suspicious

# Strings
strings suspicious | head -100
strings suspicious | grep -i "http\|password\|connect"

# Hash for lookup
md5sum suspicious
sha256sum suspicious
# Lookup on VirusTotal

# Dependencies
ldd suspicious

# ELF info
readelf -h suspicious
objdump -d suspicious | head
```

### Dynamic Analysis (Sandbox!)
```bash
# Use a VM! Never run malware on production!

# Monitor file access
strace -e trace=file ./suspicious

# Monitor network
strace -e trace=network ./suspicious

# Monitor all syscalls
strace -o trace.log ./suspicious
```

---

# PART 10: INTERVIEW QUESTIONS & ANSWERS

---

## Q1: "What command would you use to find all SUID binaries?"

### ✅ MODEL ANSWER:
```bash
find / -perm -4000 -type f 2>/dev/null
```
> "I use `find` with `-perm -4000` to search for files with the SUID bit set. The `2>/dev/null` redirects permission errors. SUID binaries run with owner's privileges, so unauthorized SUID files are a security risk - attackers can use them for privilege escalation. Normal SUID files include `/usr/bin/passwd` and `/usr/bin/sudo`."

---

## Q2: "How would you check who logged into the system recently?"

### ✅ MODEL ANSWER:
```bash
last
last -n 20          # Last 20 entries
lastlog             # Last login for all users
w                   # Currently logged in
who                 # Currently logged in (simpler)
```
> "I'd use `last` to see login history from `/var/log/wtmp`, `w` for current sessions with activity info, and check `/var/log/auth.log` for authentication events. For failed logins, I'd use `lastb` or `grep 'Failed' /var/log/auth.log`."

---

## Q3: "How do you check what ports are listening on a Linux server?"

### ✅ MODEL ANSWER:
```bash
ss -tulpn
# Or older systems:
netstat -tulpn
```
> "I use `ss -tulpn` where `-t` is TCP, `-u` is UDP, `-l` is listening, `-p` shows process, and `-n` shows numeric ports. I'd look for unexpected services, particularly on common backdoor ports like 4444, or services listening on 0.0.0.0 when they should be on localhost."

---

## Q4: "How would you find files modified in the last 24 hours?"

### ✅ MODEL ANSWER:
```bash
find / -mtime -1 -type f 2>/dev/null
# Or last hour:
find / -mmin -60 -type f 2>/dev/null
```
> "The `find` command with `-mtime -1` finds files modified in the last 1 day. This is crucial for incident response to find recently changed files. `-mtime` is modification time, `-atime` is access time, and `-ctime` is change time (including permission changes)."

---

## Q5: "What's the difference between /etc/passwd and /etc/shadow?"

### ✅ MODEL ANSWER:
> "**`/etc/passwd`** contains user account information - username, UID, GID, home directory, and shell. It's world-readable because many programs need it.
>
> **`/etc/shadow`** contains the actual password hashes and is only readable by root. This separation is for security - even if `/etc/passwd` is accessed, passwords aren't exposed.
>
> To check for security issues:"
```bash
# Users with UID 0 (root equivalent)
awk -F: '$3 == 0 {print}' /etc/passwd

# Users with empty password
awk -F: '$2 == "" {print}' /etc/shadow
```

---

## Q6: "How would you analyze failed SSH login attempts?"

### ✅ MODEL ANSWER:
```bash
# Find failed attempts
grep "Failed password" /var/log/auth.log

# Count by IP address
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn

# Find brute force (>10 attempts)
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | awk '$1 > 10'
```
> "I'd search auth.log for 'Failed password', then use awk to extract IPs and count attempts. High counts from single IPs indicate brute force. I'd then consider blocking with iptables or fail2ban."

---

## Q7: "Explain chmod 755 vs chmod 644"

### ✅ MODEL ANSWER:
> "Permissions are in format: owner-group-others, where 7=rwx, 6=rw-, 5=r-x, 4=r--
>
> **chmod 755** = rwxr-xr-x
> - Owner: read, write, execute
> - Group/Others: read and execute
> - Used for: Executable scripts, directories
>
> **chmod 644** = rw-r--r--
> - Owner: read and write
> - Group/Others: read only
> - Used for: Regular files, configs
>
> For security-sensitive files:"
```bash
chmod 600 ~/.ssh/id_rsa     # Private key (owner only)
chmod 400 ~/.ssh/authorized_keys  # Most secure
chmod 700 ~/.ssh            # SSH directory
```

---

## Q8: "How would you check if a system has been compromised?"

### ✅ MODEL ANSWER:
```bash
# 1. Check logged in users
w; who

# 2. Check for suspicious processes
ps auxf
ps aux | grep -E "nc|netcat|/tmp|/dev/shm"

# 3. Check network connections
ss -tulpn
ss -an | grep ESTABLISHED

# 4. Check for persistence
crontab -l
cat /etc/crontab
ls -la /etc/cron.*

# 5. Check recent file changes
find / -mtime -1 -type f 2>/dev/null | head

# 6. Check SUID files
find / -perm -4000 -type f 2>/dev/null

# 7. Check logs
tail -100 /var/log/auth.log
grep "Failed\|Accepted\|session opened" /var/log/auth.log

# 8. Check for rootkits
sudo chkrootkit -q
sudo rkhunter --check
```

---

## Q9: "What is the purpose of the sticky bit?"

### ✅ MODEL ANSWER:
> "The sticky bit (chmod +t or 1000) on a directory prevents users from deleting files they don't own, even if they have write access to the directory.
>
> Most common example: **/tmp**"
```bash
ls -ld /tmp
drwxrwxrwt 10 root root ...  # Note the 't'
```
> "Without sticky bit, anyone could delete anyone's files in /tmp. With it, only the file owner (or root) can delete. This prevents malicious deletion of other users' temporary files."

---

## Q10: "How do you block an IP address using iptables?"

### ✅ MODEL ANSWER:
```bash
# Block specific IP
sudo iptables -A INPUT -s 192.168.1.100 -j DROP

# Block IP range
sudo iptables -A INPUT -s 192.168.1.0/24 -j DROP

# Block at beginning of chain (immediately)
sudo iptables -I INPUT 1 -s 192.168.1.100 -j DROP

# Save rules
sudo iptables-save > /etc/iptables.rules

# Verify
sudo iptables -L INPUT -n --line-numbers
```
> "I use `-A INPUT` to append to the INPUT chain, `-s` for source IP, and `-j DROP` to silently discard. For persistence, I save rules and configure restore on boot."

---

## Q11: "How would you find which process is using a specific port?"

### ✅ MODEL ANSWER:
```bash
# Method 1: ss
ss -tulpn | grep :80

# Method 2: lsof
sudo lsof -i :80

# Method 3: netstat
netstat -tulpn | grep :80

# Method 4: fuser
fuser 80/tcp
```
> "I typically use `ss -tulpn | grep :PORT` or `lsof -i :PORT`. The lsof command shows more detail including the process name and user. For killing the process: `fuser -k 80/tcp`."

---

## Q12: "Explain the difference between `kill`, `kill -9`, and `kill -15`"

### ✅ MODEL ANSWER:
```bash
kill PID        # Same as kill -15
kill -15 PID    # SIGTERM - graceful shutdown (default)
kill -9 PID     # SIGKILL - force kill (cannot be ignored)
```
> "**SIGTERM (15)** asks the process to terminate gracefully - it can clean up, close files, save state. Most processes handle this properly.
>
> **SIGKILL (9)** forcefully terminates - the process can't catch or ignore it. Use only when SIGTERM doesn't work, as it may leave files corrupted or locks held.
>
> In security context: Malware may ignore SIGTERM, so you'd need SIGKILL. But first try SIGTERM for clean termination."

---

## Q13: "What logs would you check after a suspected security incident?"

### ✅ MODEL ANSWER:
```bash
# Authentication - Who logged in, sudo usage, SSH
/var/log/auth.log
/var/log/secure (RHEL)

# System messages
/var/log/syslog
/var/log/messages (RHEL)

# Kernel (kernel exploits would show here)
/var/log/kern.log
dmesg

# Web server
/var/log/apache2/access.log
/var/log/nginx/access.log

# Audit logs
/var/log/audit/audit.log

# Commands:
tail -100 /var/log/auth.log
grep -E "Failed|Accepted|sudo|session" /var/log/auth.log
journalctl --since "1 hour ago" -p err
```

---

## Q14: "How do you securely delete a file in Linux?"

### ✅ MODEL ANSWER:
```bash
# shred - overwrite file multiple times
shred -vfz -n 5 sensitive_file

# Options:
# -v = verbose
# -f = force (change permissions if needed)
# -z = add final overwrite with zeros
# -n 5 = overwrite 5 times

# Delete after shredding
shred -vfz -n 5 -u sensitive_file

# For SSDs (shred may not work due to wear leveling)
# Use full disk encryption instead
```
> "Regular `rm` only removes the directory entry - data remains until overwritten. `shred` overwrites multiple times. However, on SSDs, journaling filesystems, and RAID, shred may not work completely. The best solution is full disk encryption from the start."

---

## Q15: "What command would you use to see real-time network traffic?"

### ✅ MODEL ANSWER:
```bash
# tcpdump - capture packets
sudo tcpdump -i eth0
sudo tcpdump -i eth0 port 80 -A  # Show ASCII
sudo tcpdump -i eth0 host 192.168.1.100

# iftop - bandwidth by connection
sudo iftop -i eth0

# nethogs - bandwidth by process
sudo nethogs eth0

# vnstat - historical traffic
vnstat

# Watch connections
watch -n1 'ss -tulpn'
```
> "For detailed packet analysis, I use `tcpdump` with filters. For bandwidth monitoring, `iftop` shows per-connection usage. `nethogs` shows per-process network usage - useful for identifying which process is generating traffic."

---

# 📋 COMMAND QUICK REFERENCE

## Most Used Security Commands
```bash
# Information Gathering
whoami; id; hostname; uname -a

# Users
w; who; last; lastlog; cat /etc/passwd

# Network
ss -tulpn; netstat -an; lsof -i; nmap

# Processes
ps aux; top; pstree; lsof -p PID

# Files
find / -perm -4000; ls -la; file; strings

# Logs
tail -f /var/log/auth.log; journalctl -f; grep

# Firewall
iptables -L -n; ufw status
```

---

**Document Created**: February 2026
**For**: TCS HackQuest Prime Interview Preparation

---
