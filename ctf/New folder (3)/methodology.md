# Fast and Rebound - Methodology

**Challenge:** Fast and Rebound (500 pts)  
**Category:** Web / SSRF  
**URL:** http://challenge.tcshackquest.com:16353/

---

## Step-by-Step Approach

### 1. Analyzed Challenge Description
- "Internal service hiding treasure" → Target is on localhost
- "Checks the name, not where it goes" → Hostname validation only
- "Names can point differently" → DNS-based bypass needed

### 2. Explored the Application
- Found `/try` page with image URL input
- Identified `POST /fetch_image` API endpoint
- Server fetches URLs server-side (SSRF potential)

### 3. Found Hidden Hint
- In page source: `"Whispers say something listens on 8080"`
- **Internal service runs on localhost:8080**

### 4. Tested Direct Access (Blocked)
- `http://127.0.0.1:8080/` → "Invalid domain format"
- `http://localhost:8080/` → "Invalid domain format"
- Server blacklists localhost/127.0.0.1

### 5. Found the Bypass
- Used `localtest.me` (domain that resolves to 127.0.0.1)
- Server validates hostname string ✓
- But it resolves to 127.0.0.1 anyway!

### 6. Exploited the Vulnerability
- Payload: `http://localtest.me:8080/flag`
- Server accepts the domain → resolves to 127.0.0.1 → fetches internal service

---

## Final Payload

```
POST /fetch_image
{"url": "http://localtest.me:8080/flag"}
```

---

## Why It Works

| Check | Value | Result |
|-------|-------|--------|
| Hostname validation | "localtest.me" | ✅ Not blacklisted |
| DNS resolution | localtest.me | → 127.0.0.1 |
| Connection | 127.0.0.1:8080 | Internal service |

---

## Key Insight

Server validates **hostname string** but not **resolved IP address**.

`localtest.me` bypasses the check because it's a legitimate domain that always resolves to `127.0.0.1`.
