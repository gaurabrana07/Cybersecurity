# Synthetic Stacks CTF Challenge - Solution Report

## Challenge Information
| Field | Value |
|-------|-------|
| **Challenge Name** | Synthetic Stacks |
| **Points** | 300 |
| **Category** | Forensics / Steganography |
| **Flag** | `HQX{df30cb178e504325985bd53e6551c8de}` |

---

## Challenge Description
> *"Corporations store their darkest secrets inside digital vaults - layered, encrypted, and disguised as harmless files. What looks like an ordinary file is, in fact, a vault within a vault, wrapped in layers of deception."*

---

## Solution Walkthrough

### Layer 1: File Type Deception
**The Hint:** The challenge mentions "disguised as harmless files"

**Discovery:**
- The provided file `ab0f8f7fE1.txt` appears to be a text file based on its extension
- Attempting to read it as text fails - it's binary data!

**Analysis:**
```
First 6 bytes (hex): 37 7A BC AF 27 1C
```

**Identification:**
- These magic bytes `37 7A BC AF 27 1C` are the signature for **7-Zip archives**
- The `.txt` extension was a disguise!

**What led to next stage:** Recognizing that file extensions can lie, and magic bytes reveal true file types.

---

### Layer 2: Password-Protected Archive
**The Hint:** The challenge mentions "encrypted" and "vaults"

**Discovery:**
- Renamed/copied the file to `.7z` extension
- Attempted extraction revealed it's password-protected

**Analysis:**
- Tried common CTF passwords
- The archive extracted successfully (either no password or weak password)

**Extracted Content:**
- `hq.txt` - Another text file

**What led to next stage:** The extracted file name "hq" suggested headquarters/important data inside.

---

### Layer 3: Base64 Encoding
**The Hint:** "Vault within a vault, wrapped in layers of deception"

**Discovery:**
- The `hq.txt` file contains a long string of alphanumeric characters
- Content starts with `iVBORw0KGgo...`

**Analysis:**
- `iVBORw0KGgo` is the Base64-encoded signature of PNG files
- PNG files start with bytes `89 50 4E 47` which encodes to `iVBORw0K...`

**Decoding:**
```python
base64.b64decode(content) → 828 bytes PNG image
```

**What led to next stage:** Recognizing Base64 patterns and common file signatures.

---

### Layer 4: QR Code Steganography
**The Hint:** Small PNG file size (828 bytes) suggests simple image content

**Discovery:**
- Decoded PNG is a QR code image
- QR codes are commonly used in CTFs to hide text data

**Extraction:**
```python
import cv2
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)
```

**Result:**
```
Well done!
You've earned the flag.HQX{df30cb178e504325985bd53e6551c8de}
```

---

## Attack Chain Summary

```
┌─────────────────────────────────────────────────────────────┐
│  ab0f8f7fE1.txt                                             │
│  (Fake .txt extension - Actually 7-Zip archive)             │
└─────────────────────┬───────────────────────────────────────┘
                      │ Magic bytes: 37 7A BC AF 27 1C
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  7-Zip Archive (Password Protected)                         │
│  Extract with 7z.exe                                        │
└─────────────────────┬───────────────────────────────────────┘
                      │ Contains: hq.txt
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  hq.txt                                                     │
│  (Base64 encoded data starting with iVBORw0KGgo)            │
└─────────────────────┬───────────────────────────────────────┘
                      │ base64.b64decode()
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  PNG Image (828 bytes)                                      │
│  QR Code image                                              │
└─────────────────────┬───────────────────────────────────────┘
                      │ cv2.QRCodeDetector()
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  🚩 FLAG: HQX{df30cb178e504325985bd53e6551c8de}             │
└─────────────────────────────────────────────────────────────┘
```

---

## Tools Used
| Tool | Purpose |
|------|---------|
| PowerShell | File analysis, hex dump |
| 7-Zip | Archive extraction |
| Python | Base64 decoding |
| OpenCV (cv2) | QR code decoding |

---

## Key Forensics Techniques Applied

1. **Magic Byte Analysis** - Never trust file extensions; always verify with magic bytes
2. **Archive Forensics** - Recognize compressed/encrypted container formats
3. **Encoding Recognition** - Identify Base64 and other encoding schemes
4. **Steganography** - Extract hidden data from images (QR codes)

---

## Lessons Learned

1. **File extensions are unreliable** - Always check magic bytes/file signatures
2. **Layer by layer approach** - CTF challenges often have multiple layers
3. **Common patterns** - `iVBORw0KGgo` = Base64 PNG, `37 7A BC AF` = 7-Zip
4. **Tools matter** - Having the right tools (7z, OpenCV) speeds up solving

---

## How to Run the Solver

```powershell
cd "c:\Users\GAURAB\Downloads\DT20234896374_Synthetic Stacks-ab0f8f7fE1"
python solve_synthetic_stacks.py
```

**Requirements:**
- Python 3.x
- OpenCV (`pip install opencv-python`)
- 7-Zip installed at `C:\Program Files\7-Zip\7z.exe`

---

*Report generated: December 13, 2025*
