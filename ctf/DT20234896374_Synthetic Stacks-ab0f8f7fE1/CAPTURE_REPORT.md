# Synthetic Stacks CTF - Capture Report

**Challenge:** Synthetic Stacks (300 pts)  
**Flag:** `HQX{df30cb178e504325985bd53e6551c8de}`

---

## Methodology

### Step 1: File Analysis
- Received a file named `ab0f8f7fE1.txt`
- File appeared to be a text file but failed to open as text
- Examined the magic bytes (first 6 bytes of the file)
- Magic bytes `37 7A BC AF 27 1C` revealed it was a **7-Zip archive**

### Step 2: Archive Extraction
- Renamed the file extension from `.txt` to `.7z`
- Attempted to extract the archive
- Found the archive was password protected
- Tried common passwords and discovered password: **123456**
- Successfully extracted a file named `hq.txt`

### Step 3: Content Analysis
- Opened the extracted `hq.txt` file
- Found a long string of alphanumeric characters
- Recognized the pattern starting with `iVBORw0KGgo`
- This is the **Base64 signature for PNG images**

### Step 4: Image Decoding
- Decoded the Base64 string to binary data
- Saved the decoded data as a PNG image (828 bytes)
- Opened the image and found it was a **QR code**

### Step 5: Flag Extraction
- Scanned the QR code using a QR reader
- QR code contained the message: "Well done! You've earned the flag."
- **Captured the flag:** `HQX{df30cb178e504325985bd53e6551c8de}`

---

## Key Findings

- File extension was fake (`.txt` hiding a `.7z` archive)
- Archive password: `123456`
- Hidden content: Base64 encoded PNG image
- PNG contained: QR code with the flag

---

**🚩 FLAG: `HQX{df30cb178e504325985bd53e6551c8de}`**
