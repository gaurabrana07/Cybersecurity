# Know Meh Better - CTF Challenge Writeup
## Challenge: 300 Points

---

## 📋 Challenge Description

> *"This program knows you… but do YOU know it?"*  
> The executable hides its thoughts behind layers of bytecode. Only someone patient enough to peel away the masks can discover its secret. Try to understand how it thinks and maybe—just maybe—it will share the flag with you.

**Files Provided:**
- `know_meh_better.exe` - Windows executable
- `output_4aCd7fBcD8.txt` - Contains encoded data

---

## 🔍 Stage 1: Initial Reconnaissance

### What I Found:
- The `.txt` file contains a hex-like string ending with `==`:
  ```
  0123322c1714694427216d173a393b543f5a221179133d1f22346a033467374b2e0523412c033f543c6a131d2e31115e4625==
  ```

### Hints That Led to Next Stage:
1. **"layers of bytecode"** → Suggested the executable contains Python bytecode
2. **"peel away the masks"** → Multiple encoding layers to decode
3. The `==` suffix initially suggested Base64, but the characters were all hex digits

---

## 🔍 Stage 2: Executable Analysis

### Actions Taken:
- Extracted ASCII strings from the executable
- Found references to:
  - `python27.dll` - Python 2.7 runtime
  - `PYZ-00.pyz` - PyInstaller archive marker
  - `know_meh_better.pyc` - Compiled Python bytecode
  - `encodings.*` - Python encoding modules

### Hints That Led to Next Stage:
1. **PyInstaller signature** → Could extract and decompile the Python code
2. **Python 2.7** → Important for understanding encoding behavior
3. **References to "xor" in strings** → Encryption method used

---

## 🔍 Stage 3: Extracting Python Bytecode

### Tools Used:
- `pyinstxtractor.py` - Extracts files from PyInstaller executables

### Command:
```powershell
python pyinstxtractor.py know_meh_better.exe
```

### Files Extracted:
```
know_meh_better.exe_extracted/
├── know_meh_better.pyc     ← Main program bytecode
├── python27.dll
├── PYZ-00.pyz
└── ... (other support files)
```

### Hints That Led to Next Stage:
1. Successfully extracted `know_meh_better.pyc` - the main program
2. Now needed to decompile the `.pyc` file to readable Python code

---

## 🔍 Stage 4: Decompiling Python Bytecode

### Tools Used:
- `uncompyle6` - Python bytecode decompiler

### Command:
```powershell
uncompyle6 know_meh_better.pyc
```

### Key Code Discovered:
```python
import random
FLAG = 'HQX{fake_flag}'
slt = len.__doc__  # ← THE XOR KEY!

def encode_flag(flg):
    encoded = ''.join([chr(ord(flg[i]) ^ ord(slt[i % len(slt)])) 
                       for i in range(len(flg))]).encode('utf-8').encode('hex')
    return encoded

def decode_flag(flg):
    encoded_bytes = flg.decode('hex')
    decoded = ''.join([chr(ord(encoded_bytes[i]) ^ ord(slt[i % len(slt)])) 
                       for i in range(len(encoded_bytes))])
    return decoded
```

### Hints That Led to Next Stage:
1. **`slt = len.__doc__`** → The XOR key is Python's `len` function docstring
2. **Encoding process**: Original → XOR with key → Hex encode
3. **"This is a fake flag btw"** → The real flag is in the output file, not the code

---

## 🔍 Stage 5: Identifying the XOR Key

### Discovery:
```python
>>> len.__doc__
'Return the number of items in a container.'
```

This 45-character string is used as a repeating XOR key.

### Hints That Led to Next Stage:
- Now had both the encoded data and the key
- Just needed to reverse the encoding process

---

## 🔍 Stage 6: Decoding the Flag

### Decoding Process (Reverse Order):

#### Step 1: Hex Decode
```python
encoded_hex = "0123322c1714694427216d173a393b543f5a221179133d1f22346a033467374b2e0523412c033f543c6a131d2e31115e4625"
encoded_bytes = bytes.fromhex(encoded_hex)
# Result: 50 bytes
```

#### Step 2: XOR Decrypt
```python
xor_key = "Return the number of items in a container."
decrypted = ''.join([chr(encoded_bytes[i] ^ ord(xor_key[i % len(xor_key)])) 
                     for i in range(len(encoded_bytes))])
# Result: "SFFYezI0ODMyOTY1MzMwYzIzOGJjZGVkMjM5MjQ1NDAxZDc0fQ"
```

#### Step 3: Base64 Decode
```python
import base64
flag = base64.b64decode("SFFYezI0ODMyOTY1MzMwYzIzOGJjZGVkMjM5MjQ1NDAxZDc0fQ==")
# Result: "HQX{24832965330c238bcded239245401d74}"
```

---

## 🚩 FLAG

```
HQX{24832965330c238bcded239245401d74}
```

---

## 📊 Encoding Layers Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    ENCODING (Program)                        │
├─────────────────────────────────────────────────────────────┤
│  Original Flag                                               │
│       ↓                                                      │
│  Base64 Encode                                               │
│       ↓                                                      │
│  XOR with len.__doc__                                        │
│       ↓                                                      │
│  Hex Encode                                                  │
│       ↓                                                      │
│  output_4aCd7fBcD8.txt                                       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    DECODING (Solution)                       │
├─────────────────────────────────────────────────────────────┤
│  output_4aCd7fBcD8.txt                                       │
│       ↓                                                      │
│  Hex Decode                                                  │
│       ↓                                                      │
│  XOR with len.__doc__                                        │
│       ↓                                                      │
│  Base64 Decode                                               │
│       ↓                                                      │
│  🚩 FLAG: HQX{24832965330c238bcded239245401d74}              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| PowerShell | File analysis, string extraction |
| pyinstxtractor.py | Extract PyInstaller executables |
| uncompyle6 | Decompile Python bytecode |
| Python 3 | Run decoding script |

---

## 💡 Key Takeaways

1. **Challenge hints matter** - "bytecode" directly pointed to Python
2. **PyInstaller executables can be unpacked** - Using pyinstxtractor
3. **Python bytecode can be decompiled** - Using uncompyle6
4. **Look for obfuscated keys** - `len.__doc__` is a clever way to hide a string
5. **Multiple encoding layers** - XOR + Hex + Base64 require systematic reversal

---

## 📁 Solution Files

- `solve_flag.py` - Automated solution script
- `WRITEUP.md` - This report
