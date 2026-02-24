# Address Abyss - CTF Challenge Solution Report

**Challenge:** Address Abyss  
**Points:** 300  
**Category:** Network Analysis / Forensics  
**Flag:** `HQX{e1f63411d00cc00f8445e9bb0860d9f4}`

---

## Challenge Description

A massive dump of network logs hides a secret. Only entries with IPs in the ranges `92.7.X.Y` (IPv4) and `2510:a1:X::Y` (IPv6-like) matter. Each X is an index, each Y a value. Extract the pairs, arrange the values by their indices, and reconstruct the flag from the fragments.

---

## Solution Approach

### Step 1: Understanding the Pattern

The challenge hints that:
- **IPv4 format:** `92.7.X.Y` where X = index (decimal), Y = character value
- **IPv6-like format:** `2510:a1:X::Y` where X = index (hexadecimal), Y = character value

The key insight is that **valid entries have Y as a single character** (hex digit or special character like `{` or `}`).

### Step 2: Filtering Valid Entries

The log file contains ~18,000 lines of noise mixed with valid entries. Most entries have:
- Invalid formats (extra characters, symbols like `#`, `$`, `%`, etc.)
- Multi-digit Y values (e.g., `92.7.843.634`)

**Valid entries must match:**
- IPv4: `92.7.<number>.<single_hex_digit>`
- IPv6: `2510:a1:<hex>::<single_character>`

### Step 3: Extracting Valid IPv4 Entries

Using pattern matching, I found 21 valid IPv4 entries:

| IP Address | Index | Character |
|------------|-------|-----------|
| 92.7.5.1 | 5 | 1 |
| 92.7.7.6 | 7 | 6 |
| 92.7.8.3 | 8 | 3 |
| 92.7.9.4 | 9 | 4 |
| 92.7.10.1 | 10 | 1 |
| 92.7.11.1 | 11 | 1 |
| 92.7.13.0 | 13 | 0 |
| 92.7.14.0 | 14 | 0 |
| 92.7.17.0 | 17 | 0 |
| 92.7.18.0 | 18 | 0 |
| 92.7.20.8 | 20 | 8 |
| 92.7.21.4 | 21 | 4 |
| 92.7.22.4 | 22 | 4 |
| 92.7.23.5 | 23 | 5 |
| 92.7.25.9 | 25 | 9 |
| 92.7.28.0 | 28 | 0 |
| 92.7.29.8 | 29 | 8 |
| 92.7.30.6 | 30 | 6 |
| 92.7.31.0 | 31 | 0 |
| 92.7.33.9 | 33 | 9 |
| 92.7.35.4 | 35 | 4 |

### Step 4: Extracting Valid IPv6-like Entries

Found 15 valid IPv6-like entries (index in hexadecimal):

| IP Address | Index (Hex) | Index (Dec) | Character |
|------------|-------------|-------------|-----------|
| 2510:a1:0::H | 0 | 0 | H |
| 2510:a1:1::Q | 1 | 1 | Q |
| 2510:a1:2::X | 2 | 2 | X |
| 2510:a1:3::{ | 3 | 3 | { |
| 2510:a1:4::e | 4 | 4 | e |
| 2510:a1:6::f | 6 | 6 | f |
| 2510:a1:c::d | c | 12 | d |
| 2510:a1:f::c | f | 15 | c |
| 2510:a1:10::c | 10 | 16 | c |
| 2510:a1:13::f | 13 | 19 | f |
| 2510:a1:18::e | 18 | 24 | e |
| 2510:a1:1a::b | 1a | 26 | b |
| 2510:a1:1b::b | 1b | 27 | b |
| 2510:a1:20::d | 20 | 32 | d |
| 2510:a1:22::f | 22 | 34 | f |
| 2510:a1:24::} | 24 | 36 | } |

### Step 5: Combining and Sorting

Merging all entries and sorting by index:

| Index | Source | Character |
|-------|--------|-----------|
| 0 | IPv6 | H |
| 1 | IPv6 | Q |
| 2 | IPv6 | X |
| 3 | IPv6 | { |
| 4 | IPv6 | e |
| 5 | IPv4 | 1 |
| 6 | IPv6 | f |
| 7 | IPv4 | 6 |
| 8 | IPv4 | 3 |
| 9 | IPv4 | 4 |
| 10 | IPv4 | 1 |
| 11 | IPv4 | 1 |
| 12 | IPv6 | d |
| 13 | IPv4 | 0 |
| 14 | IPv4 | 0 |
| 15 | IPv6 | c |
| 16 | IPv6 | c |
| 17 | IPv4 | 0 |
| 18 | IPv4 | 0 |
| 19 | IPv6 | f |
| 20 | IPv4 | 8 |
| 21 | IPv4 | 4 |
| 22 | IPv4 | 4 |
| 23 | IPv4 | 5 |
| 24 | IPv6 | e |
| 25 | IPv4 | 9 |
| 26 | IPv6 | b |
| 27 | IPv6 | b |
| 28 | IPv4 | 0 |
| 29 | IPv4 | 8 |
| 30 | IPv4 | 6 |
| 31 | IPv4 | 0 |
| 32 | IPv6 | d |
| 33 | IPv4 | 9 |
| 34 | IPv6 | f |
| 35 | IPv4 | 4 |
| 36 | IPv6 | } |

### Step 6: Reconstructing the Flag

Reading characters in order from index 0 to 36:

```
H Q X { e 1 f 6 3 4 1 1 d 0 0 c c 0 0 f 8 4 4 5 e 9 b b 0 8 6 0 d 9 f 4 }
```

---

## Final Flag

```
HQX{e1f63411d00cc00f8445e9bb0860d9f4}
```

---

## Tools Used

- **PowerShell** - For pattern matching with `Select-String`
- **Python** - For automated extraction (see `solve_flag.py`)

---

## Key Takeaways

1. **Pattern Recognition:** The challenge required identifying valid IP patterns among thousands of noise entries
2. **Mixed Radix:** IPv4 used decimal indices while IPv6 used hexadecimal indices
3. **Character Encoding:** The flag characters were hidden in the last octet (IPv4) or after `::` (IPv6)
4. **Filtering Criteria:** Valid entries had single-character values, while noise had multi-character or special symbol values

---

## Commands Used

```powershell
# Find valid IPv4 entries
Get-Content ip_logs_50DF6ce4BF.txt | Select-String -Pattern "^92\.7\.\d+\.[0-9a-fA-F]$"

# Find valid IPv6-like entries
Get-Content ip_logs_50DF6ce4BF.txt | Select-String -Pattern "^2510:a1:[0-9a-fA-F]+::[0-9a-fA-F]$"

# Find flag prefix (indices 0-3)
Get-Content ip_logs_50DF6ce4BF.txt | Select-String -Pattern "2510:a1:[0-3]::"

# Find closing brace (index 36 = 0x24)
Get-Content ip_logs_50DF6ce4BF.txt | Select-String -Pattern "2510:a1:24::"
```

---

*Report generated for CTF documentation purposes*
