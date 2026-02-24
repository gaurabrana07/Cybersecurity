# Area 64 CTF Challenge - Writeup Report

## Challenge Information

| Field | Details |
|-------|---------|
| **Challenge Name** | Area 64 |
| **Challenge ID** | DT20234896374 |
| **File Analyzed** | 4DFB3A68bb.txt |
| **Category** | Cryptography / Encoding |
| **Difficulty** | Easy |
| **Flag** | `HQX{70c5d525ca0e27806553b4a49bf4ccf8}` |

---

## Executive Summary

This report documents the methodology used to successfully capture the flag in the "Area 64" CTF challenge. The challenge involved analyzing a text file containing a hidden message encoded in Base64 format.

---

## Methodology

### Step 1: Initial Reconnaissance

Upon receiving the challenge, I first examined the contents of the provided file `4DFB3A68bb.txt`.

**File Contents:**
```
To get inside the Area 64, you need a key. Look around and you might find it.
WW91J3JlIGluc2lkZSBBcmVhIDY0LiBIZXJlJ3MgeW91ciBrZXkgOiBIUVh7NzBjNWQ1MjVjYTBlMjc4MDY1NTNiNGE0OWJmNGNjZjh9
```

**Observations:**
- Line 1: A hint suggesting that a "key" is hidden somewhere
- Line 2: A suspicious string of alphanumeric characters

### Step 2: Pattern Recognition

The second line exhibited characteristics typical of **Base64 encoding**:
- Contained only alphanumeric characters (A-Z, a-z, 0-9)
- Included `+` and `/` characters (standard Base64 alphabet)
- String length was a multiple of 4 (as required by Base64)
- No special characters or spaces

**Hypothesis:** The second line is a Base64 encoded message containing the flag.

### Step 3: Decoding Process

I decoded the Base64 string using the following methods:

#### Method A: PowerShell (Windows)
```powershell
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("WW91J3JlIGluc2lkZSBBcmVhIDY0LiBIZXJlJ3MgeW91ciBrZXkgOiBIUVh7NzBjNWQ1MjVjYTBlMjc4MDY1NTNiNGE0OWJmNGNjZjh9"))
```

#### Method B: Python
```python
import base64
encoded = "WW91J3JlIGluc2lkZSBBcmVhIDY0LiBIZXJlJ3MgeW91ciBrZXkgOiBIUVh7NzBjNWQ1MjVjYTBlMjc4MDY1NTNiNGE0OWJmNGNjZjh9"
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)
```

#### Method C: Linux/Bash
```bash
echo "WW91J3JlIGluc2lkZSBBcmVhIDY0LiBIZXJlJ3MgeW91ciBrZXkgOiBIUVh7NzBjNWQ1MjVjYTBlMjc4MDY1NTNiNGE0OWJmNGNjZjh9" | base64 -d
```

### Step 4: Flag Extraction

**Decoded Message:**
```
You're inside Area 64. Here's your key : HQX{70c5d525ca0e27806553b4a49bf4ccf8}
```

**Captured Flag:** `HQX{70c5d525ca0e27806553b4a49bf4ccf8}`

---

## Technical Analysis

### Base64 Encoding Overview

Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format. It is commonly used to:
- Encode data for transmission over text-based protocols
- Embed binary data in text files
- Obfuscate (not encrypt) information

### Flag Format Analysis

| Component | Value | Description |
|-----------|-------|-------------|
| Prefix | `HQX` | Challenge/CTF identifier |
| Hash | `70c5d525ca0e27806553b4a49bf4ccf8` | 32-character hexadecimal string (MD5 format) |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| VS Code | File analysis and code editing |
| PowerShell | Base64 decoding on Windows |
| Python 3 | Scripting the decode process |

---

## Lessons Learned

1. **Always examine all content** - The hint on line 1 confirmed that something was hidden
2. **Recognize encoding patterns** - Base64 has distinct characteristics that are easy to identify
3. **Use multiple decoding methods** - Having fallback methods ensures success across platforms

---

## Conclusion

The Area 64 challenge was successfully completed by:
1. Analyzing the provided text file
2. Identifying the Base64 encoded string
3. Decoding the string to reveal the hidden message
4. Extracting the flag from the decoded content

**Final Flag:** `HQX{70c5d525ca0e27806553b4a49bf4ccf8}`

---

## Author

**Solved By:** GAURAB  
**Date:** December 13, 2025

---

*This report was generated as part of the CTF challenge documentation.*
