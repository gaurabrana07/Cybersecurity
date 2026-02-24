# 🔐 CRYPTOGRAPHY - 100 Interview Questions & Answers

## Priority Legend
- 🔴 **MOST PROBABLE** - Frequently asked, must know
- 🟠 **IMPORTANT** - Commonly asked, should know
- 🟡 **MODERATE** - Sometimes asked, good to know
- 🟢 **DEPTH** - Complex/Advanced, shows expertise

---

## SECTION 1: CRYPTOGRAPHY BASICS (Q1-Q20)

### 🔴 Q1: What is cryptography?
**Answer:**
Cryptography is the science of securing information by transforming it into an unreadable format (encryption) that can only be converted back (decryption) by authorized parties with the correct key. It provides:
- **Confidentiality** - Only intended recipients can read
- **Integrity** - Data hasn't been tampered
- **Authentication** - Verify sender identity
- **Non-repudiation** - Sender cannot deny sending

---

### 🔴 Q2: What is the difference between encryption and encoding?
**Answer:**
| Aspect | Encryption | Encoding |
|--------|------------|----------|
| **Purpose** | Security/Confidentiality | Data format conversion |
| **Key Required** | Yes | No |
| **Reversible By** | Only key holder | Anyone knowing the scheme |
| **Example** | AES, RSA | Base64, URL encoding |

Encoding is NOT security - Base64 is easily decoded by anyone.

---

### 🔴 Q3: What is the difference between symmetric and asymmetric encryption?
**Answer:**
| Aspect | Symmetric | Asymmetric |
|--------|-----------|------------|
| **Keys** | Same key for encrypt/decrypt | Public + Private key pair |
| **Speed** | Fast | Slow (100-1000x slower) |
| **Key Distribution** | Difficult (must share securely) | Easy (public key is shared) |
| **Use Case** | Bulk data encryption | Key exchange, digital signatures |
| **Examples** | AES, DES, 3DES | RSA, ECC, Diffie-Hellman |

In practice, both are combined: asymmetric for key exchange, symmetric for data.

---

### 🔴 Q4: What is a hash function? Name some common ones.
**Answer:**
A hash function is a one-way mathematical function that converts input of any size into a fixed-size output (digest). Properties:
- **Deterministic** - Same input = same output
- **One-way** - Cannot reverse to get input
- **Collision-resistant** - Hard to find two inputs with same hash
- **Avalanche effect** - Small input change = completely different hash

Common hash functions:
- **MD5** - 128-bit (broken, don't use for security)
- **SHA-1** - 160-bit (deprecated)
- **SHA-256** - 256-bit (widely used)
- **SHA-3** - Latest standard
- **bcrypt, Argon2** - For password hashing

---

### 🔴 Q5: Why is MD5 considered insecure?
**Answer:**
MD5 is insecure because:
1. **Collision attacks** - Two different inputs can produce the same hash (demonstrated in 2004)
2. **Speed** - Too fast, enables brute force attacks on passwords
3. **Rainbow tables** - Pre-computed tables exist for common passwords
4. **No salt** - Original MD5 doesn't include salting

MD5 can still be used for checksums (non-security), but never for passwords or signatures.

---

### 🔴 Q6: What is a salt in cryptography?
**Answer:**
A salt is a random value added to input before hashing. Purpose:
- **Defeats rainbow tables** - Pre-computed tables become useless
- **Unique hashes** - Same password produces different hashes for different users
- **Prevents identification** - Can't tell if two users have same password

```
Without salt: hash("password123") = abc123 (same for all users)
With salt:    hash("password123" + "randomsalt1") = xyz789
              hash("password123" + "randomsalt2") = def456
```

Salt should be:
- Unique per user/password
- Stored alongside the hash
- Generated using cryptographic random generator

---

### 🔴 Q7: What is AES? Why is it widely used?
**Answer:**
AES (Advanced Encryption Standard) is a symmetric block cipher adopted by NIST in 2001 to replace DES.

**Key features:**
- Block size: 128 bits
- Key sizes: 128, 192, or 256 bits
- Rounds: 10, 12, or 14 (based on key size)

**Why widely used:**
- Government approved (NSA uses for classified data)
- Fast in hardware and software
- No known practical attacks
- Royalty-free
- Well-analyzed and trusted

AES-256 is considered quantum-resistant for symmetric encryption.

---

### 🔴 Q8: What are the modes of operation in block ciphers?
**Answer:**
Block cipher modes determine how blocks are encrypted:

| Mode | Name | Use Case | Notes |
|------|------|----------|-------|
| **ECB** | Electronic Codebook | Never use | Same plaintext = same ciphertext (insecure) |
| **CBC** | Cipher Block Chaining | File encryption | Needs IV, sequential |
| **CTR** | Counter | Streaming | Parallelizable |
| **GCM** | Galois/Counter Mode | TLS, APIs | Provides authentication + encryption |
| **XTS** | XEX Tweakable | Disk encryption | Used in BitLocker, FileVault |

**GCM is recommended** for most applications as it provides both encryption and authentication (AEAD).

---

### 🔴 Q9: What is RSA? How does it work?
**Answer:**
RSA is an asymmetric encryption algorithm based on the difficulty of factoring large prime numbers.

**How it works:**
1. Generate two large primes: p and q
2. Compute n = p × q (modulus)
3. Compute φ(n) = (p-1)(q-1)
4. Choose e (public exponent, typically 65537)
5. Compute d where e × d ≡ 1 (mod φ(n)) (private key)

**Keys:**
- Public key: (n, e)
- Private key: (n, d)

**Operations:**
- Encrypt: ciphertext = message^e mod n
- Decrypt: message = ciphertext^d mod n

RSA is slow, so typically used for key exchange or signing, not bulk data.

---

### 🟠 Q10: What is Diffie-Hellman key exchange?
**Answer:**
Diffie-Hellman allows two parties to establish a shared secret over an insecure channel without prior shared secret.

**Process:**
1. Agree on public values: prime p and generator g
2. Alice picks private a, sends A = g^a mod p
3. Bob picks private b, sends B = g^b mod p
4. Alice computes: s = B^a mod p
5. Bob computes: s = A^b mod p
6. Both have same shared secret s!

**Security:** Based on discrete logarithm problem (hard to find a from g^a mod p).

**Vulnerability:** Susceptible to Man-in-the-Middle if not authenticated.

---

### 🟠 Q11: What is ECC (Elliptic Curve Cryptography)?
**Answer:**
ECC is asymmetric cryptography based on algebraic structure of elliptic curves over finite fields.

**Advantages over RSA:**
- Smaller key sizes for equivalent security
- Faster computation
- Less power consumption (good for mobile/IoT)

**Key size comparison:**
| Security Level | RSA Key | ECC Key |
|---------------|---------|---------|
| 80-bit | 1024 | 160 |
| 128-bit | 3072 | 256 |
| 256-bit | 15360 | 512 |

**Common curves:** P-256, P-384, Curve25519

Used in TLS, Bitcoin, Signal protocol.

---

### 🟠 Q12: What is a digital signature?
**Answer:**
A digital signature is a mathematical scheme for verifying authenticity and integrity of digital messages.

**Process:**
1. Sender hashes the message
2. Sender encrypts hash with their **private key** (signing)
3. Signature is attached to message
4. Receiver decrypts signature with sender's **public key**
5. Receiver independently hashes message
6. If hashes match, signature is valid

**Provides:**
- **Authentication** - Confirms sender identity
- **Integrity** - Message wasn't altered
- **Non-repudiation** - Sender can't deny signing

**Algorithms:** RSA, DSA, ECDSA, EdDSA

---

### 🟠 Q13: What is PKI (Public Key Infrastructure)?
**Answer:**
PKI is a framework for managing digital certificates and public-key encryption.

**Components:**
- **CA (Certificate Authority)** - Issues and signs certificates
- **RA (Registration Authority)** - Verifies identity before certificate issuance
- **Certificate** - Binds public key to identity
- **CRL (Certificate Revocation List)** - List of revoked certificates
- **OCSP** - Online Certificate Status Protocol (real-time revocation check)

**Trust hierarchy:**
```
Root CA (self-signed, offline)
    └── Intermediate CA
            └── End Entity Certificates (websites, users)
```

---

### 🟠 Q14: What is an X.509 certificate?
**Answer:**
X.509 is the standard format for public key certificates.

**Contents:**
- Version
- Serial number
- Signature algorithm
- Issuer (CA name)
- Validity period (not before, not after)
- Subject (owner identity)
- Subject's public key
- Extensions (key usage, SAN, etc.)
- CA's digital signature

**File formats:**
- **.pem** - Base64 encoded
- **.der** - Binary format
- **.crt/.cer** - Certificate files
- **.pfx/.p12** - Certificate with private key

---

### 🟠 Q15: What is TLS and how does the handshake work?
**Answer:**
TLS (Transport Layer Security) encrypts communication between client and server.

**TLS 1.3 Handshake (simplified):**
```
Client                                  Server
   |                                      |
   |------ ClientHello + Key Share ------>|
   |                                      |
   |<----- ServerHello + Key Share -------|
   |<----- Certificate ------------------ |
   |<----- CertificateVerify -------------|
   |<----- Finished ---------------------|
   |                                      |
   |------ Finished -------------------->|
   |                                      |
   |====== Encrypted Data ===============|
```

**Improvements in TLS 1.3:**
- 1-RTT handshake (was 2-RTT)
- 0-RTT resumption
- Removed weak algorithms (RC4, SHA-1, RSA key exchange)
- Forward secrecy mandatory

---

### 🟠 Q16: What is Perfect Forward Secrecy (PFS)?
**Answer:**
Perfect Forward Secrecy ensures that session keys cannot be compromised even if the server's private key is compromised in the future.

**How it works:**
- Use ephemeral (temporary) key pairs for each session
- Even if long-term key is compromised, past sessions remain secure
- Each session has unique keys that are discarded after use

**Key exchange methods with PFS:**
- DHE (Diffie-Hellman Ephemeral)
- ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)

**Without PFS:** If attacker records encrypted traffic and later obtains private key, they can decrypt all past communications.

---

### 🟡 Q17: What is the difference between stream and block ciphers?
**Answer:**
| Aspect | Block Cipher | Stream Cipher |
|--------|--------------|---------------|
| **Operation** | Fixed-size blocks | Bit by bit / byte by byte |
| **Speed** | Generally slower | Generally faster |
| **Error propagation** | Affects whole block | Affects single bit |
| **Examples** | AES, DES, Blowfish | RC4, ChaCha20, Salsa20 |
| **IV handling** | Per block (with modes) | Per stream |
| **Use case** | File encryption | Real-time streaming |

ChaCha20 is preferred stream cipher (used in TLS, WireGuard).

---

### 🟡 Q18: What is HMAC?
**Answer:**
HMAC (Hash-based Message Authentication Code) provides message authentication using a cryptographic hash function and secret key.

**Formula:**
```
HMAC(K, m) = H((K' ⊕ opad) || H((K' ⊕ ipad) || m))
```

**Properties:**
- Verifies both data integrity and authenticity
- Resistant to length extension attacks (unlike plain hash + key)
- Can use any hash function (HMAC-SHA256, HMAC-SHA512)

**Use cases:**
- API authentication
- JWT signature verification
- Session token validation

---

### 🟡 Q19: What are rainbow tables and how to defend against them?
**Answer:**
Rainbow tables are precomputed tables for reversing hash functions, used to crack password hashes.

**How they work:**
- Attacker pre-computes hashes of common passwords
- When they get a hash, they look it up in the table
- Instant password recovery if found

**Defenses:**
1. **Salt** - Add random value to each password before hashing
2. **Slow hash functions** - bcrypt, scrypt, Argon2 (computationally expensive)
3. **Key stretching** - Multiple iterations (PBKDF2)
4. **Pepper** - Secret value added server-side (stored separately)

---

### 🟡 Q20: What is key stretching?
**Answer:**
Key stretching is the process of making a weak key (like password) stronger by applying a hash function many times.

**Methods:**
- **PBKDF2** - Applies HMAC repeatedly (iterations)
- **bcrypt** - Uses Blowfish with cost factor
- **scrypt** - Memory-hard function
- **Argon2** - Winner of Password Hashing Competition (recommended)

**Example PBKDF2:**
```
derived_key = PBKDF2(password, salt, iterations=100000, keylen=32)
```

Purpose: Makes brute-force attacks much slower by requiring significant computation per guess.

---

## SECTION 2: SYMMETRIC ENCRYPTION (Q21-Q35)

### 🔴 Q21: What is DES and why is it obsolete?
**Answer:**
DES (Data Encryption Standard) was a symmetric block cipher adopted in 1977.

**Specifications:**
- Block size: 64 bits
- Key size: 56 bits (too small!)
- Rounds: 16

**Why obsolete:**
- 56-bit key can be brute-forced (2^56 = ~72 quadrillion, feasible today)
- DES Cracker broke it in 22 hours (1998)
- Theoretical and practical attacks exist

**Replaced by:**
- 3DES (Triple DES) - temporary fix
- AES - modern standard

---

### 🟠 Q22: How does 3DES work?
**Answer:**
3DES (Triple DES) applies DES three times with different keys.

**Process:**
```
Ciphertext = E_K3(D_K2(E_K1(Plaintext)))
```
- E = Encrypt, D = Decrypt
- EDE (Encrypt-Decrypt-Encrypt) mode

**Key options:**
- **Keying option 1:** K1, K2, K3 all different (168-bit)
- **Keying option 2:** K1 = K3 ≠ K2 (112-bit)
- **Keying option 3:** K1 = K2 = K3 (56-bit, equals DES)

**Status:** Deprecated by NIST (2023), use AES instead.

---

### 🟠 Q23: Explain AES encryption process.
**Answer:**
AES operates on 4×4 byte matrix called "state."

**Rounds (for AES-128: 10 rounds):**

1. **AddRoundKey** - XOR state with round key
2. **SubBytes** - Substitute each byte using S-box (non-linear)
3. **ShiftRows** - Cyclically shift rows
4. **MixColumns** - Mix columns mathematically (not in final round)
5. Repeat with new round key

**Key expansion:** Derives round keys from original key.

```
Initial Round:
    AddRoundKey
Main Rounds (9 times):
    SubBytes → ShiftRows → MixColumns → AddRoundKey
Final Round:
    SubBytes → ShiftRows → AddRoundKey
```

---

### 🟠 Q24: What is an IV (Initialization Vector)?
**Answer:**
An IV is a random value used to ensure identical plaintexts encrypt differently.

**Properties:**
- Should be random/unique per encryption
- Doesn't need to be secret (sent with ciphertext)
- Size typically equals block size (128 bits for AES)

**Consequences of IV reuse:**
- CBC: Reveals if same message encrypted twice
- CTR: Catastrophic - can recover plaintext with XOR
- GCM: Breaks authentication completely

**Best practice:** Generate cryptographically random IV for each encryption operation.

---

### 🟠 Q25: Why is ECB mode insecure?
**Answer:**
ECB (Electronic Codebook) encrypts each block independently with the same key.

**Problem:** Identical plaintext blocks → Identical ciphertext blocks

**Famous example:** ECB Penguin
- Image encrypted with ECB still shows penguin outline
- Patterns in plaintext visible in ciphertext

```
Plaintext:  [Block1][Block1][Block2][Block1]
ECB output: [AAAAA][AAAAA][BBBBB][AAAAA]
            ↑ Same blocks visible!
```

**When barely acceptable:** Single block encryption only.

**Use instead:** CBC, CTR, or GCM mode.

---

### 🟠 Q26: Explain CBC mode and its vulnerabilities.
**Answer:**
CBC (Cipher Block Chaining) XORs each plaintext block with previous ciphertext block before encryption.

**Process:**
```
C₁ = E_K(P₁ ⊕ IV)
C₂ = E_K(P₂ ⊕ C₁)
C₃ = E_K(P₃ ⊕ C₂)
```

**Advantages:**
- Identical plaintext blocks produce different ciphertext
- Widely supported

**Vulnerabilities:**
- **Padding Oracle Attack** - If server reveals padding errors, attacker can decrypt
- **Bit-flipping** - Modifying ciphertext predictably affects next decrypted block
- **Cannot parallelize** encryption (can parallelize decryption)

**Mitigation:** Use authenticated encryption (GCM) or add MAC.

---

### 🟡 Q27: What is GCM mode and why is it preferred?
**Answer:**
GCM (Galois/Counter Mode) combines CTR mode encryption with GHASH authentication.

**Provides AEAD (Authenticated Encryption with Associated Data):**
- Encryption (confidentiality)
- Authentication (integrity + authenticity)
- Can authenticate additional data without encrypting it

**Advantages:**
- Single pass encryption + authentication
- Parallelizable
- Hardware acceleration support (AES-NI)
- Industry standard for TLS 1.2/1.3

**Requirements:**
- **Never reuse IV** with same key (catastrophic!)
- 96-bit IV recommended

---

### 🟡 Q28: What is Blowfish? Is it still secure?
**Answer:**
Blowfish is a symmetric block cipher designed by Bruce Schneier (1993).

**Specifications:**
- Block size: 64 bits
- Key size: 32-448 bits
- Rounds: 16

**Status:**
- The algorithm itself is not broken
- 64-bit block size is a weakness (birthday attack after 2^32 blocks)
- Replaced by Twofish and AES

**Still used in:** bcrypt password hashing (which is secure).

For new applications, use AES or ChaCha20.

---

### 🟡 Q29: What is ChaCha20?
**Answer:**
ChaCha20 is a stream cipher designed by Daniel Bernstein, an improvement over Salsa20.

**Features:**
- 256-bit key, 96-bit nonce
- 20 rounds
- ARX design (Add-Rotate-XOR) - no S-boxes

**Advantages:**
- Fast in software (no special hardware needed)
- Constant-time implementation (resistant to timing attacks)
- Simple design, well-analyzed

**Use cases:**
- ChaCha20-Poly1305 in TLS 1.3
- WireGuard VPN
- Mobile devices (where AES-NI unavailable)

---

### 🟡 Q30: What is authenticated encryption?
**Answer:**
Authenticated Encryption provides both confidentiality (encryption) and integrity/authenticity (authentication) in a single operation.

**Types:**
- **AEAD (Authenticated Encryption with Associated Data):**
  - Encrypts payload
  - Authenticates both payload AND additional data (headers, etc.)
  - Examples: AES-GCM, ChaCha20-Poly1305

**Why needed:**
- Encrypt-then-MAC can be implemented incorrectly
- Prevents ciphertext modification attacks
- Single API reduces implementation errors

**Tag:** Authentication tag is produced alongside ciphertext, must be verified before decryption.

---

### 🟡 Q31: What is XTS mode used for?
**Answer:**
XTS (XEX-based Tweaked-codebook mode with ciphertext Stealing) is designed for disk encryption.

**Features:**
- Uses two keys (one for encryption, one for tweak)
- Each sector encrypted independently
- No authentication (length-preserving)

**Why for disk encryption:**
- Random access needed (can decrypt any sector independently)
- Length-preserving (ciphertext same size as plaintext)
- Sector number acts as tweak (same data in different sectors produces different ciphertext)

**Used in:**
- BitLocker (Windows)
- FileVault (macOS)
- dm-crypt/LUKS (Linux)

---

### 🟢 Q32: Explain the padding oracle attack.
**Answer:**
Padding oracle attack exploits systems that reveal whether decryption padding is valid.

**How CBC padding works (PKCS#7):**
- If last block needs 3 bytes padding: add `03 03 03`
- Padding is verified after decryption

**Attack:**
1. Attacker modifies ciphertext byte
2. Server decrypts and checks padding
3. Different error for invalid padding vs invalid data
4. Attacker learns information about plaintext
5. Repeat to recover entire message

**Prevention:**
- Use authenticated encryption (GCM)
- Don't reveal padding errors
- Verify MAC before attempting decryption
- Use constant-time comparison

---

### 🟢 Q33: What is key wrapping?
**Answer:**
Key wrapping is encrypting one key with another key for secure storage or transport.

**Use cases:**
- Encrypting DEK (Data Encryption Key) with KEK (Key Encryption Key)
- Storing keys in database
- Key export/import

**Standard:** AES Key Wrap (RFC 3394)
- Adds integrity check
- Deterministic (no IV needed)
- Ciphertext 64 bits longer than plaintext

**Hierarchy:**
```
Master Key (HSM)
    └── Key Encryption Key (KEK)
            └── Data Encryption Key (DEK)
```

---

### 🟢 Q34: What is format-preserving encryption?
**Answer:**
Format-Preserving Encryption (FPE) encrypts data while preserving its format.

**Example:**
- Credit card: 4532-1234-5678-9012 → 7891-4523-0147-8523
- SSN: 123-45-6789 → 987-65-4321

**Use cases:**
- Tokenization of payment data
- PCI-DSS compliance (encrypted data still looks like card number)
- Legacy systems that expect specific format

**Standards:**
- FF1, FF3-1 (NIST SP 800-38G)

**Trade-off:** Smaller domain = weaker security.

---

### 🟢 Q35: Explain meet-in-the-middle attack.
**Answer:**
Meet-in-the-middle attack is used against double encryption, reducing effective key length.

**Against 2DES:**
- Expected: 56 + 56 = 112-bit security
- Actual: 57-bit security only!

**How it works:**
1. Encrypt plaintext with all possible K1 → store results
2. Decrypt ciphertext with all possible K2
3. Find match in stored results
4. Complexity: 2^56 + 2^56 instead of 2^112

**Why 3DES uses EDE:**
- Provides backward compatibility
- Still vulnerable but 112-bit effective security acceptable

**Lesson:** Doubling encryption doesn't double security.

---

## SECTION 3: ASYMMETRIC ENCRYPTION (Q36-Q50)

### 🔴 Q36: What is the mathematical basis of RSA security?
**Answer:**
RSA security is based on the **integer factorization problem**.

**The hard problem:**
Given n = p × q (where p and q are large primes), finding p and q is computationally infeasible.

**Why it works:**
- Multiplication is easy: 61 × 53 = 3233
- Factoring is hard: Given 3233, find 61 and 53

**Key sizes:**
- 1024-bit: Deprecated (factorable with sufficient resources)
- 2048-bit: Current minimum
- 4096-bit: High security

**Threat:** Quantum computers could factor using Shor's algorithm (post-quantum cryptography needed).

---

### 🔴 Q37: What are common RSA key sizes and their security levels?
**Answer:**
| RSA Key Size | Security Bits | Status |
|--------------|---------------|--------|
| 512-bit | <50 | Broken |
| 1024-bit | 80 | Deprecated, avoid |
| 2048-bit | 112 | Minimum acceptable |
| 3072-bit | 128 | Recommended |
| 4096-bit | 140 | High security |

**NIST recommendations:**
- 2048-bit minimum until 2030
- 3072-bit for beyond 2030

**Note:** Larger keys = slower operations. ECC provides same security with smaller keys.

---

### 🟠 Q38: What is RSA padding and why is it crucial?
**Answer:**
Raw/textbook RSA is insecure. Padding adds randomness and structure.

**PKCS#1 v1.5 padding:**
- Adds random bytes before encryption
- Vulnerable to Bleichenbacher attack (chosen ciphertext)
- Still used but prefer OAEP

**OAEP (Optimal Asymmetric Encryption Padding):**
- Provably secure in random oracle model
- Uses hash functions and random seed
- Recommended for encryption

**PSS (Probabilistic Signature Scheme):**
- For digital signatures
- Randomized, provably secure

**Key point:** Always use proper padding, never raw RSA.

---

### 🟠 Q39: What is the difference between RSA encryption and RSA signing?
**Answer:**
| Operation | RSA Encryption | RSA Signing |
|-----------|---------------|-------------|
| **Sender uses** | Recipient's public key | Sender's private key |
| **Receiver uses** | Recipient's private key | Sender's public key |
| **Purpose** | Confidentiality | Authentication |
| **What's processed** | The data/key | Hash of data |

**Encryption:**
- Alice encrypts with Bob's public key
- Only Bob can decrypt with his private key

**Signing:**
- Alice signs message hash with her private key
- Anyone can verify with Alice's public key

---

### 🟠 Q40: How does ECDSA work?
**Answer:**
ECDSA (Elliptic Curve Digital Signature Algorithm) provides digital signatures using elliptic curves.

**Key generation:**
- Choose random private key d (integer)
- Compute public key Q = d × G (point on curve)

**Signing:**
1. Hash message: h = H(m)
2. Generate random k
3. Calculate point: (x, y) = k × G
4. Calculate r = x mod n
5. Calculate s = k⁻¹(h + d × r) mod n
6. Signature = (r, s)

**Verification:**
1. Compute w = s⁻¹ mod n
2. Compute u₁ = h × w, u₂ = r × w
3. Compute point (x, y) = u₁ × G + u₂ × Q
4. Valid if r = x mod n

**Critical:** k must be unique per signature (reuse leaks private key - Sony PS3 hack).

---

### 🟠 Q41: What is EdDSA and Ed25519?
**Answer:**
EdDSA (Edwards-curve Digital Signature Algorithm) is a modern signature scheme.

**Ed25519** is EdDSA using Curve25519:
- 128-bit security
- 32-byte public keys
- 64-byte signatures
- Very fast

**Advantages over ECDSA:**
- Deterministic (no random k needed, avoids PS3-style bugs)
- Faster than ECDSA
- Simpler implementation
- Resistant to side-channel attacks

**Used in:**
- SSH keys (ssh-ed25519)
- Signal protocol
- Cryptocurrency (Solana)
- WireGuard

---

### 🟠 Q42: What is Diffie-Hellman vulnerability and how to mitigate?
**Answer:**
Classic DH is vulnerable to **Man-in-the-Middle (MITM)** attacks.

**Attack:**
```
Alice                 Mallory                Bob
  |------ A ------->|                          |
  |                 |------ A' ------->       |
  |                 |<------ B' ------|       |
  |<------ B -------|                          |
  
  Alice-Mallory key ≠ Mallory-Bob key
  Mallory can decrypt and re-encrypt all traffic
```

**Mitigations:**
1. **Authenticated DH** - Sign DH values with long-term keys
2. **Use within TLS** - Certificate authenticates server
3. **ECDHE in TLS** - Ephemeral + authenticated

---

### 🟠 Q43: What is the difference between DH and ECDH?
**Answer:**
| Aspect | DH (Classic) | ECDH |
|--------|--------------|------|
| **Math basis** | Multiplicative group of integers mod p | Elliptic curve group |
| **Key size for 128-bit security** | 3072 bits | 256 bits |
| **Speed** | Slower | Faster |
| **Standardization** | Well established | Modern standard |

**Process comparison:**
- DH: g^a mod p, g^b mod p → g^(ab) mod p
- ECDH: aG, bG → abG (point multiplication)

**ECDHE** = Ephemeral ECDH (new keys per session, provides PFS).

---

### 🟡 Q44: What are the security assumptions in cryptography?
**Answer:**
Cryptographic systems rely on computational hardness assumptions:

**Symmetric:**
- AES: No known structural attacks
- Based on substitution-permutation network strength

**Asymmetric:**
| Algorithm | Hard Problem |
|-----------|--------------|
| RSA | Integer Factorization |
| DH/DSA | Discrete Logarithm |
| ECDH/ECDSA | Elliptic Curve Discrete Logarithm |
| Lattice-based | Shortest Vector Problem |

**Key point:** These aren't proven hard, just believed hard based on decades of analysis.

---

### 🟡 Q45: What is key escrow?
**Answer:**
Key escrow is storing copies of encryption keys with a third party for recovery or lawful interception.

**Use cases:**
- Enterprise key recovery (employee leaves/forgets)
- Legal compliance (court-ordered access)

**Controversies:**
- **Clipper Chip (1990s)** - US government backdoor proposal, rejected
- Single point of failure
- Trust issues with escrow agent

**Modern alternative:**
- Split-knowledge (M of N key sharing)
- Hardware Security Modules (HSMs)

---

### 🟡 Q46: What is a certificate chain and how is it validated?
**Answer:**
Certificate chain links end-entity certificate to trusted root CA.

**Chain structure:**
```
Root CA (self-signed, in browser/OS trust store)
    ↓ Signs
Intermediate CA
    ↓ Signs
End-entity certificate (website)
```

**Validation process:**
1. Verify end-entity certificate signature using intermediate CA public key
2. Verify intermediate CA certificate using root CA public key
3. Check root CA is in trust store
4. For each certificate:
   - Check not expired
   - Check not revoked (CRL/OCSP)
   - Check key usage allows signing
   - Verify domain matches (for TLS)

---

### 🟡 Q47: What is certificate pinning?
**Answer:**
Certificate pinning hardcodes expected certificate or public key in application.

**Types:**
- **Certificate pinning** - Pin specific certificate
- **Public key pinning** - Pin public key (survives certificate renewal)
- **CA pinning** - Pin issuing CA

**Benefits:**
- Prevents MITM even if attacker has valid certificate
- Protects against CA compromise

**Challenges:**
- Certificate rotation requires app update
- Can cause outages if done incorrectly
- Deprecated in browsers (HPKP removed)

**Best practice:** Pin intermediate CA + backup pins.

---

### 🟢 Q48: Explain the Bleichenbacher attack on RSA.
**Answer:**
Bleichenbacher attack (1998) is a padding oracle attack against RSA PKCS#1 v1.5.

**How it works:**
1. Attacker sends malformed ciphertexts to server
2. Server reveals if PKCS#1 padding is valid
3. Through millions of queries, attacker learns plaintext

**Oracle:**
- Valid padding → different error/timing
- Invalid padding → different response

**Impact:** Can decrypt RSA without private key!

**Prevention:**
- Use OAEP padding instead
- Don't reveal padding validity (constant-time processing)
- Use TLS 1.3 (removes RSA key exchange)

---

### 🟢 Q49: What is threshold cryptography?
**Answer:**
Threshold cryptography distributes cryptographic operations among multiple parties.

**Threshold signatures (t-of-n):**
- Private key split into n shares
- At least t shares needed to sign
- No single party has full key

**Use cases:**
- Cryptocurrency wallets (multi-sig)
- CA key protection
- Distributed key generation

**Example:** 3-of-5 threshold
- 5 parties hold shares
- Any 3 can create signature
- 2 or fewer cannot

---

### 🟢 Q50: What is post-quantum cryptography?
**Answer:**
Post-quantum cryptography (PQC) develops algorithms resistant to quantum computer attacks.

**Quantum threats:**
- Shor's algorithm breaks RSA, ECC, DH
- Grover's algorithm weakens symmetric crypto (double key size)

**NIST PQC standards (2024):**
| Algorithm | Type | Use |
|-----------|------|-----|
| ML-KEM (Kyber) | Lattice-based | Key encapsulation |
| ML-DSA (Dilithium) | Lattice-based | Digital signatures |
| SLH-DSA (SPHINCS+) | Hash-based | Digital signatures |

**Migration strategy:**
- Hybrid mode (classical + PQC)
- "Harvest now, decrypt later" threat motivates early adoption

---

## SECTION 4: HASHING & PASSWORD SECURITY (Q51-Q65)

### 🔴 Q51: What makes a good password hashing algorithm?
**Answer:**
Password hashing has different requirements than general hashing:

**Requirements:**
1. **Slow** - Computationally expensive (opposite of general hashing)
2. **Memory-hard** - Requires significant memory (defeats GPU attacks)
3. **Salted** - Unique salt per password
4. **Adjustable cost** - Can increase iterations as hardware improves

**Recommended algorithms (in order):**
1. **Argon2id** - Winner of Password Hashing Competition
2. **bcrypt** - Proven, widely supported
3. **scrypt** - Memory-hard
4. **PBKDF2** - Acceptable with high iterations (100,000+)

**Never use:** MD5, SHA-1, SHA-256 (without key stretching)

---

### 🔴 Q52: How does bcrypt work?
**Answer:**
bcrypt is based on Blowfish cipher, designed for password hashing.

**Components:**
- Cost factor (2^cost iterations)
- Salt (128-bit random)
- Password

**Output format:**
```
$2b$12$R9h/cIPz0gi.URNNX3kh2OPST9/PgBk...
 │  │  │                 │
 │  │  │                 └── Hash (184-bit)
 │  │  └── Salt (128-bit, base64)
 │  └── Cost factor (2^12 = 4096 iterations)
 └── Algorithm version
```

**Key feature:** Adaptive - increase cost factor as hardware gets faster.

**Limitation:** 72-byte password maximum.

---

### 🔴 Q53: What is Argon2 and why is it recommended?
**Answer:**
Argon2 won the Password Hashing Competition (2015) and is the recommended standard.

**Variants:**
- **Argon2d** - Data-dependent, faster, GPU-resistant
- **Argon2i** - Data-independent, side-channel resistant
- **Argon2id** - Hybrid, recommended for passwords

**Parameters:**
- Memory cost (KB to use)
- Time cost (iterations)
- Parallelism (threads)

**Example:**
```
Argon2id$v=19$m=65536,t=3,p=4$salt$hash
```

**Advantages:**
- Memory-hard (defeats ASICs and GPUs)
- Configurable for different environments
- Resistant to side-channel attacks
- Modern design based on competition

---

### 🟠 Q54: What is a pepper and how does it differ from salt?
**Answer:**
| Aspect | Salt | Pepper |
|--------|------|--------|
| **Storage** | With hash in DB | Separate (config/HSM) |
| **Per-password** | Yes, unique each | No, same for all |
| **Public** | Yes | Secret |
| **Purpose** | Prevent rainbow tables | Additional secret layer |

**How pepper helps:**
- If database is breached, attacker doesn't have pepper
- Even with hash + salt, can't crack without pepper

**Implementation:**
```python
# Method 1: Prepend to password
hash = bcrypt(pepper + password + salt)

# Method 2: Encrypt hash
hash = AES_encrypt(bcrypt(password + salt), pepper_key)
```

---

### 🟠 Q55: Explain PBKDF2.
**Answer:**
PBKDF2 (Password-Based Key Derivation Function 2) derives strong keys from passwords.

**Algorithm:**
```
DK = PBKDF2(PRF, Password, Salt, Iterations, KeyLength)
```

**How it works:**
1. Combine password + salt + counter
2. Apply PRF (usually HMAC-SHA256) iteratively
3. XOR results of each iteration
4. Produce derived key of desired length

**Parameters:**
- PRF: HMAC-SHA256 or HMAC-SHA512
- Iterations: 100,000+ (OWASP recommendation: 600,000 for SHA-256)
- Salt: At least 128 bits, random

**Limitation:** Not memory-hard, vulnerable to GPU/ASIC attacks. Prefer Argon2 or bcrypt.

---

### 🟠 Q56: What is a cryptographic hash collision?
**Answer:**
Collision occurs when two different inputs produce the same hash output.

**Types:**
- **Generic collision:** Find any two inputs with same hash
- **Preimage attack:** Given hash, find input that produces it
- **Second preimage:** Given input1, find input2 with same hash

**Birthday paradox:**
For n-bit hash, collision expected after ~2^(n/2) attempts
- MD5 (128-bit): ~2^64 operations (feasible)
- SHA-256 (256-bit): ~2^128 operations (infeasible)

**Real-world collision:**
- MD5: First collision found 2004
- SHA-1: "SHAttered" attack 2017 (two PDFs, same hash)

---

### 🟠 Q57: What is length extension attack?
**Answer:**
Length extension attack exploits hash functions that process input in blocks.

**Vulnerable functions:** MD5, SHA-1, SHA-256 (Merkle-Damgård construction)

**Attack:**
Given H(message) and length, attacker can compute H(message || padding || extra) without knowing original message.

**Example:**
```
Original: H(secret + "amount=100") = abc123
Attack:   H(secret + "amount=100" + padding + "&amount=999") = def456
Attacker can compute def456 without knowing secret!
```

**Prevention:**
- Use HMAC instead of H(key || message)
- Use SHA-3 (sponge construction, not vulnerable)
- Use H(key || H(key || message))

---

### 🟡 Q58: What is SHA-3 and how is it different from SHA-2?
**Answer:**
SHA-3 (Keccak) uses fundamentally different design than SHA-2.

**Comparison:**
| Aspect | SHA-2 | SHA-3 |
|--------|-------|-------|
| Design | Merkle-Damgård | Sponge construction |
| Length extension | Vulnerable | Immune |
| Year | 2001 | 2015 |
| Performance | Generally faster | Slower in software |

**SHA-3 variants:**
- SHA3-256, SHA3-512 (fixed output)
- SHAKE128, SHAKE256 (variable output - XOF)

**When to use SHA-3:**
- New designs where extra security margin needed
- When length extension resistance required without HMAC
- Diversity (not same design family as SHA-2)

---

### 🟡 Q59: What is scrypt?
**Answer:**
scrypt is a memory-hard password hashing function.

**Parameters:**
- N: CPU/memory cost (power of 2)
- r: Block size
- p: Parallelism

**Memory-hard:**
- Requires significant RAM to compute
- Defeats GPU attacks (GPUs have limited memory per core)

**Example:**
```
scrypt(password, salt, N=16384, r=8, p=1, dkLen=32)
```

**Used in:**
- Litecoin mining (resistant to ASICs initially)
- Password storage (alternative to bcrypt)

**vs Argon2:** scrypt came first, Argon2 is more configurable and newer.

---

### 🟡 Q60: Explain timing attacks on hash comparison.
**Answer:**
Timing attack measures time differences in string comparison to deduce secret value.

**Vulnerable comparison:**
```python
def compare(hash1, hash2):
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            return False  # Returns early!
    return True
```

**Attack:**
- First byte match → slightly longer time
- Attacker tries all first bytes, finds which takes longest
- Repeat for each position

**Prevention - constant-time comparison:**
```python
import hmac
hmac.compare_digest(hash1, hash2)  # Always same time
```

**Or manually:**
```python
def safe_compare(a, b):
    if len(a) != len(b):
        return False
    result = 0
    for x, y in zip(a, b):
        result |= x ^ y
    return result == 0
```

---

### 🟡 Q61: What is HKDF and when is it used?
**Answer:**
HKDF (HMAC-based Key Derivation Function) derives keys from a shared secret.

**Two phases:**
1. **Extract:** Create pseudorandom key (PRK) from input
2. **Expand:** Generate output key material (OKM) of any length

```
PRK = HMAC-Hash(salt, IKM)
OKM = HKDF-Expand(PRK, info, length)
```

**Use cases:**
- Derive encryption key from DH shared secret
- Derive multiple keys from one master key
- Key derivation in TLS 1.3

**Not for passwords:** HKDF is fast, use Argon2/bcrypt for passwords.

---

### 🟢 Q62: What is a commitment scheme in cryptography?
**Answer:**
Commitment scheme allows committing to a value while keeping it hidden, then revealing it later.

**Properties:**
- **Hiding:** Commitment doesn't reveal value
- **Binding:** Cannot change committed value

**Example (simplified):**
1. Alice commits: sends hash(value || random_nonce)
2. Later reveals: sends value + nonce
3. Bob verifies: hash(value || nonce) matches commitment

**Use cases:**
- Coin flipping over network
- Auction sealed bids
- Zero-knowledge proofs
- Password-authenticated key exchange

---

### 🟢 Q63: What is proof of work?
**Answer:**
Proof of Work (PoW) requires computational effort to produce result that's easy to verify.

**How Bitcoin PoW works:**
1. Combine block data + nonce
2. Hash (SHA-256 twice)
3. If hash < target difficulty → valid block
4. Otherwise, try different nonce

**Properties:**
- Hard to compute (many hashes to find valid nonce)
- Easy to verify (single hash check)
- Adjustable difficulty

**Uses:**
- Cryptocurrency mining (Bitcoin, Ethereum pre-merge)
- Email anti-spam (Hashcash)
- DoS protection

---

### 🟢 Q64: What is the birthday attack?
**Answer:**
Birthday attack exploits birthday paradox to find hash collisions.

**Birthday paradox:**
In group of 23 people, 50% chance two share birthday.
In group of 70, 99.9% chance.

**Applied to hashes:**
For n-bit hash, expect collision after ~2^(n/2) attempts.

| Hash | Bits | Naive | Birthday Attack |
|------|------|-------|-----------------|
| MD5 | 128 | 2^128 | 2^64 |
| SHA-256 | 256 | 2^256 | 2^128 |

**Attack process:**
1. Generate many random inputs
2. Hash each, store results
3. Look for collision in stored hashes
4. ~√(2^n) = 2^(n/2) attempts needed

**Defense:** Use hash functions with sufficient output length.

---

### 🟢 Q65: What is key encapsulation mechanism (KEM)?
**Answer:**
KEM is a method to securely establish shared symmetric key using asymmetric cryptography.

**Process:**
1. Generate random symmetric key
2. Encapsulate (encrypt) using recipient's public key
3. Send encapsulation to recipient
4. Recipient decapsulates using private key
5. Both have shared symmetric key

**vs Key Exchange:**
- KEM: One party generates key, sends to other
- Key Exchange (DH): Both parties contribute to key

**Post-quantum KEM:**
- ML-KEM (Kyber) - NIST standard
- Used in hybrid TLS (classical + post-quantum)

**Advantage:** Security proof is cleaner than RSA encryption.

---

## SECTION 5: PROTOCOLS & APPLICATIONS (Q66-Q80)

### 🔴 Q66: How does HTTPS work?
**Answer:**
HTTPS = HTTP over TLS. Provides encryption, authentication, and integrity.

**Process:**
1. **TCP handshake** (SYN, SYN-ACK, ACK)
2. **TLS handshake:**
   - Client sends supported ciphers, TLS version
   - Server sends certificate, chosen cipher
   - Key exchange (ECDHE)
   - Derive session keys
   - Finished messages
3. **Encrypted HTTP** communication

**What TLS provides:**
- **Encryption:** Symmetric encryption with negotiated key
- **Authentication:** Server certificate verified
- **Integrity:** MAC on every message

**Port:** 443 (vs HTTP 80)

---

### 🔴 Q67: What ciphersuites are recommended for TLS?
**Answer:**
Modern TLS 1.3 ciphersuites:
```
TLS_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
TLS_CHACHA20_POLY1305_SHA256
```

**TLS 1.2 recommendations:**
```
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305
```

**Avoid:**
- RSA key exchange (no forward secrecy)
- CBC mode ciphers (BEAST, Lucky13)
- RC4, DES, 3DES
- MD5, SHA-1 for signatures
- TLS 1.0, 1.1

**Key points:**
- ECDHE for key exchange (forward secrecy)
- AEAD cipher (GCM or ChaCha20-Poly1305)
- SHA-256 or SHA-384

---

### 🔴 Q68: What is certificate transparency?
**Answer:**
Certificate Transparency (CT) is a system for monitoring and auditing TLS certificates.

**How it works:**
1. CA submits certificate to CT logs
2. Log returns Signed Certificate Timestamp (SCT)
3. SCT embedded in certificate or TLS handshake
4. Browser verifies SCT presence
5. Anyone can monitor logs for mis-issued certificates

**Benefits:**
- Detect misissued certificates
- Catch rogue CAs
- Post-hoc auditing

**Requirement:** Chrome requires CT for all certificates since 2018.

**Logs:** Operated by Google, Cloudflare, DigiCert, etc.

---

### 🟠 Q69: Explain S/MIME for email encryption.
**Answer:**
S/MIME (Secure/Multipurpose Internet Mail Extensions) provides email signing and encryption.

**Operations:**
- **Sign:** Sender's private key signs message digest
- **Encrypt:** Symmetric key encrypted with recipient's public key
- **Sign and Encrypt:** Both operations

**Certificate format:** X.509

**Process (encryption):**
1. Generate random symmetric key
2. Encrypt message with symmetric key
3. Encrypt symmetric key with recipient's public key
4. Package as S/MIME message

**vs PGP:**
- S/MIME uses X.509 certificates (hierarchical trust)
- PGP uses web of trust
- S/MIME better enterprise support

---

### 🟠 Q70: How does SSH authentication work?
**Answer:**
SSH supports multiple authentication methods:

**Password authentication:**
- Encrypted over SSH channel
- Susceptible to brute force

**Public key authentication (recommended):**
1. Client sends public key identifier
2. Server checks authorized_keys file
3. Server sends random challenge encrypted with public key
4. Client decrypts with private key, sends response
5. Server verifies

**Setup:**
```bash
# Generate key pair
ssh-keygen -t ed25519

# Copy public key to server
ssh-copy-id user@server
```

**Key types (in order of preference):**
1. Ed25519 (recommended)
2. ECDSA
3. RSA (4096-bit)

---

### 🟠 Q71: What is JWT security best practices?
**Answer:**
**Do:**
- Use strong signing algorithms (RS256, ES256, EdDSA)
- Keep secret keys secure
- Set short expiration (exp claim)
- Validate all claims
- Use HTTPS only
- Include issuer (iss) and audience (aud)

**Don't:**
- Use "none" algorithm (CVE-2015-9235)
- Use HS256 with public key confusion
- Store sensitive data (tokens are easily decoded)
- Use symmetric keys in distributed systems

**Algorithm attacks:**
```javascript
// Attack: Change algorithm in header
{
  "alg": "none",  // Server might accept without verification!
  "typ": "JWT"
}

// Attack: Confuse RS256 with HS256
// If server uses RS256, attacker changes to HS256
// Uses public key as HMAC secret
```

**Libraries should never allow "none" algorithm.**

---

### 🟠 Q72: What is Signal Protocol?
**Answer:**
Signal Protocol provides end-to-end encrypted messaging with advanced features.

**Key components:**
- **X3DH (Extended Triple Diffie-Hellman):** Key agreement
- **Double Ratchet:** Forward secrecy per message

**Properties:**
- **End-to-end encryption:** Only endpoints can read
- **Forward secrecy:** Past messages safe if key compromised
- **Break-in recovery:** Future messages safe after compromise
- **Deniability:** Cannot prove who sent message

**Used by:**
- Signal
- WhatsApp
- Facebook Messenger (secret conversations)
- Skype (private conversations)

**Key insight:** Double ratchet advances key with every message, limiting damage of key compromise.

---

### 🟡 Q73: How does VPN encryption work?
**Answer:**
VPNs encrypt traffic between client and server.

**Common protocols:**

**OpenVPN:**
- Uses TLS for control channel
- AES for data encryption
- UDP or TCP transport

**WireGuard:**
- ChaCha20 for symmetric encryption
- Curve25519 for key exchange
- Poly1305 for authentication
- Very fast, small codebase

**IPSec:**
- IKE for key exchange
- ESP for encryption
- AH for authentication (deprecated)
- Enterprise use

**What VPN protects:**
- Encrypts traffic from ISP
- Hides destination from network
- Masks IP from destination

**What VPN doesn't protect:**
- Traffic after VPN server
- Metadata (timing, size)
- VPN provider can see traffic

---

### 🟡 Q74: What is mTLS (mutual TLS)?
**Answer:**
mTLS authenticates both client and server (vs standard TLS authenticating only server).

**Process:**
1. Standard TLS handshake begins
2. Server requests client certificate (CertificateRequest)
3. Client sends certificate
4. Server verifies client certificate
5. Client proves possession of private key

**Use cases:**
- API authentication (instead of API keys)
- Service-to-service communication (microservices)
- Zero Trust architecture
- Enterprise internal services

**Implementation:**
```nginx
# Nginx mTLS config
ssl_client_certificate /path/to/ca.crt;
ssl_verify_client on;
```

**Advantage:** Strong authentication without passwords/tokens.

---

### 🟡 Q75: What is DNSSEC?
**Answer:**
DNSSEC adds cryptographic signatures to DNS responses.

**Problem solved:**
- DNS spoofing (attacker returns fake IP)
- Cache poisoning

**How it works:**
1. DNS zones signed with private key
2. Public key published in DNS (DNSKEY record)
3. Signatures stored in RRSIG records
4. Chain of trust from root
5. Resolver validates signatures

**Records:**
- **DNSKEY:** Public key
- **RRSIG:** Signature over resource records
- **DS:** Delegation signer (links to parent zone)
- **NSEC/NSEC3:** Proof of non-existence

**Limitation:** Only provides authentication, not encryption (use DoH/DoT for privacy).

---

### 🟡 Q76: What is code signing?
**Answer:**
Code signing uses digital signatures to verify software authenticity and integrity.

**Process:**
1. Developer hashes code
2. Signs hash with private key
3. Attaches signature and certificate
4. User verifies signature
5. OS/app checks certificate trust

**Benefits:**
- Confirms software source
- Detects tampering
- Required by app stores and OS (macOS Gatekeeper)

**Platforms:**
- Windows: Authenticode
- macOS: Apple code signing
- Android: APK signing
- Browser extensions: Web store signing

**Key management is critical:** Stolen code signing key = signed malware (e.g., SolarWinds).

---

### 🟢 Q77: What is homomorphic encryption?
**Answer:**
Homomorphic encryption allows computation on encrypted data without decryption.

**Types:**
- **Partially homomorphic:** One operation (RSA: multiplication only)
- **Somewhat homomorphic:** Limited operations
- **Fully homomorphic (FHE):** Any computation

**Example:**
```
E(a) + E(b) = E(a + b)
E(a) × E(b) = E(a × b)
```
Compute on ciphertexts, result decrypts to answer.

**Use cases:**
- Cloud computing on sensitive data
- Private machine learning
- Encrypted databases
- Secure voting

**Limitation:** Very slow (1000x+ overhead). Active research area.

---

### 🟢 Q78: What is secure multi-party computation (MPC)?
**Answer:**
MPC allows multiple parties to jointly compute function without revealing their private inputs.

**Example - Millionaire's problem:**
- Alice and Bob want to know who's richer
- Neither reveals their wealth
- MPC outputs only comparison result

**Techniques:**
- Garbled circuits
- Secret sharing
- Oblivious transfer

**Real-world uses:**
- Private auctions
- Privacy-preserving analytics
- Cryptocurrency custody (threshold signatures)
- Salary comparison without disclosure

**Key property:** No single party learns others' inputs.

---

### 🟢 Q79: What is zero-knowledge proof?
**Answer:**
Zero-knowledge proof proves statement is true without revealing any information beyond validity.

**Properties:**
- **Completeness:** If statement true, verifier accepts
- **Soundness:** If statement false, verifier rejects
- **Zero-knowledge:** Verifier learns nothing beyond statement validity

**Classic example - Ali Baba cave:**
- Prove you know password to door without revealing it
- Verifier asks you to exit from specific side
- Repeat many times to gain confidence

**Types:**
- **Interactive:** Requires back-and-forth
- **Non-interactive (NIZK):** Single proof message

**Applications:**
- zk-SNARKs (Zcash privacy)
- zk-Rollups (Ethereum scaling)
- Authentication without secrets
- Privacy-preserving identity

---

### 🟢 Q80: What is a hardware security module (HSM)?
**Answer:**
HSM is a dedicated cryptographic processor that manages and protects keys.

**Features:**
- Tamper-resistant hardware
- Keys stored securely (never exported in plaintext)
- Cryptographic operations happen inside HSM
- FIPS 140-2/140-3 certified

**Use cases:**
- CA private keys
- Payment processing (PCI-DSS)
- Database encryption keys
- Code signing keys

**Types:**
- **On-premise:** SafeNet, Thales
- **Cloud:** AWS CloudHSM, Azure Dedicated HSM, GCP Cloud HSM

**Key principle:** Keys never leave HSM boundary. Operations request sent to HSM, results returned.

---

## SECTION 6: ATTACKS & VULNERABILITIES (Q81-Q90)

### 🔴 Q81: What are common cryptographic implementation mistakes?
**Answer:**
| Mistake | Consequence |
|---------|-------------|
| Using ECB mode | Patterns visible |
| Reusing IV/nonce | Key recovery possible |
| Rolling own crypto | Likely vulnerabilities |
| Hardcoding keys | Key exposure |
| Weak random generation | Predictable keys |
| No authentication | Ciphertext modification |
| String comparison for MACs | Timing attack |
| Using MD5/SHA1 | Collision attacks |

**Golden rule:** Use established libraries, don't implement crypto yourself.

---

### 🔴 Q82: What is a known-plaintext attack?
**Answer:**
Attack where adversary has both plaintext and corresponding ciphertext samples.

**Scenario:**
- Attacker knows file header is always "PNG..."
- Knows ciphertext for that position
- Uses relationship to attack

**Vulnerable:**
- Weak algorithms (XOR cipher)
- Stream ciphers with reused key
- Poor implementations

**Defense:**
- Modern algorithms (AES, ChaCha) designed to resist
- Use unique keys/IVs
- Authenticated encryption

**Enigma:** Broken partly due to known plaintexts (weather reports, standard phrases).

---

### 🟠 Q83: What is a side-channel attack?
**Answer:**
Side-channel attacks exploit physical implementation rather than algorithm weakness.

**Types:**
| Attack | Measures | Targets |
|--------|----------|---------|
| Timing | Execution time | Key-dependent branches |
| Power analysis | Power consumption | Key bits during operation |
| Electromagnetic | EM emissions | Hardware operations |
| Cache timing | Memory access patterns | Key-dependent access |
| Acoustic | Sound | HDD seeks, fan speed |

**Defense:**
- Constant-time implementations
- Power masking
- Random delays
- Noise injection

**Example:** Spectre/Meltdown exploit CPU cache side channels.

---

### 🟠 Q84: What is key substitution attack?
**Answer:**
Attacker finds different key that produces same signature/output.

**HMAC variant:**
- Given HMAC(K1, M) = T
- Find K2 where HMAC(K2, M') = T for some M'

**Digital signature variant:**
- Signature valid under multiple public keys
- Attacker's key validates another's signature

**Prevention:**
- Include public key in signed data
- Use strong signature schemes (EdDSA includes public key)
- Verify signer identity separately

---

### 🟠 Q85: Explain nonce reuse catastrophe.
**Answer:**
Reusing nonce (number used once) with same key catastrophically breaks security.

**CTR mode:**
```
Ciphertext1 = Plaintext1 ⊕ AES(Key, Nonce||1)
Ciphertext2 = Plaintext2 ⊕ AES(Key, Nonce||1)  // Same nonce!

Ciphertext1 ⊕ Ciphertext2 = Plaintext1 ⊕ Plaintext2
```
Attacker gets XOR of plaintexts!

**GCM mode:**
- Nonce reuse allows recovering authentication key
- Can forge messages

**Real incidents:**
- PS3 hack (ECDSA with reused k)
- NSA Suite B implementation bugs

**Prevention:**
- Counter-based nonces
- Random nonces with sufficient length
- Never reuse nonce with same key

---

### 🟡 Q86: What is the ROBOT attack?
**Answer:**
ROBOT (Return Of Bleichenbacher's Oracle Threat) is RSA padding oracle attack discovered in 2017.

**Target:** Servers supporting RSA key exchange in TLS.

**How it worked:**
- Variations of Bleichenbacher 1998 attack
- Different error responses for valid/invalid padding
- Allows decryption of captured traffic

**Affected:**
- Facebook, Paypal (patched)
- Many TLS implementations
- Hardware appliances (F5, Cisco)

**Mitigation:**
- Disable RSA key exchange
- Use TLS 1.3 (no RSA key exchange)
- Constant-time padding check

---

### 🟡 Q87: What is BEAST attack?
**Answer:**
BEAST (Browser Exploit Against SSL/TLS) exploits TLS 1.0 CBC mode.

**Vulnerability:**
- TLS 1.0 uses previous record's last block as IV
- IV is predictable
- Allows chosen-plaintext attack

**Attack:**
1. Inject guessed byte into page request
2. Force victim to send request
3. Compare encrypted blocks
4. Recover cookies byte by byte

**Mitigation:**
- Use TLS 1.2+ (random IV)
- 1/n-1 record splitting
- Disable CBC ciphersuites

---

### 🟡 Q88: What is Lucky Thirteen attack?
**Answer:**
Lucky Thirteen exploits timing differences in TLS CBC mode padding verification.

**Vulnerability:**
- MAC-then-encrypt in TLS
- Padding verification time varies
- Timing reveals padding validity

**Why "Lucky 13":**
- TLS header is 13 bytes
- Attack depends on this value

**Impact:**
- Plaintext recovery (similar to padding oracle)

**Mitigation:**
- Constant-time padding check
- Use AEAD ciphersuites (GCM, ChaCha20-Poly1305)
- TLS 1.3 (no CBC)

---

### 🟢 Q89: What is a fault injection attack?
**Answer:**
Fault injection induces errors in cryptographic computation to reveal secrets.

**Methods:**
- Voltage glitching
- Clock glitching
- Laser fault injection
- Electromagnetic pulse

**Example - RSA-CRT:**
1. Induce fault during one CRT computation
2. Get faulty signature S'
3. Factor modulus: gcd(S'^e - M, N) = p

**Targets:**
- Smart cards
- Secure elements
- HSMs (high-end)

**Defense:**
- Redundant computation
- Verification before output
- Fault detection circuits
- Protected hardware

---

### 🟢 Q90: What is a quantum computing threat to cryptography?
**Answer:**
Quantum computers threaten current cryptographic systems.

**Shor's algorithm impacts:**
| Algorithm | Threat | Status |
|-----------|--------|--------|
| RSA | Broken | Replace |
| ECDSA/ECDH | Broken | Replace |
| DH | Broken | Replace |
| AES-128 | Weakened | Use AES-256 |
| SHA-256 | Weakened | Still secure |

**Grover's algorithm:**
- Quadratic speedup for search
- Halves effective key length
- AES-128 → 64-bit security
- AES-256 → 128-bit security (still safe)

**Timeline:**
- "Cryptographically Relevant Quantum Computer" (CRQC)
- Estimates: 10-20 years
- Harvest now, decrypt later threat

**Solution:** Post-quantum cryptography (ML-KEM, ML-DSA).

---

## SECTION 7: PRACTICAL & SCENARIO-BASED (Q91-Q100)

### 🔴 Q91: How would you securely store passwords in a database?
**Answer:**
```python
import bcrypt
import secrets

# Registration
def hash_password(password: str) -> str:
    # bcrypt includes salt automatically
    salt = bcrypt.gensalt(rounds=12)  # 2^12 = 4096 iterations
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

# Verification
def verify_password(password: str, stored_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), stored_hash.encode())
```

**Key points:**
1. Use bcrypt/Argon2 (not MD5/SHA)
2. Salt is automatic in bcrypt
3. Adjustable cost factor
4. Never store plaintext
5. Use constant-time comparison

---

### 🔴 Q92: How would you implement secure API authentication?
**Answer:**
**Option 1: JWT (stateless)**
```
Client → POST /login {credentials}
Server → JWT token (signed with RS256)
Client → GET /api {Authorization: Bearer <token>}
Server → Verify signature, check exp, return data
```

**Option 2: OAuth 2.0 (delegated)**
- Use authorization code flow
- Short-lived access tokens
- Refresh tokens for renewal

**Option 3: mTLS (certificate-based)**
- Client authenticates with certificate
- Strong authentication, no passwords

**Best practices:**
- HTTPS only
- Short token expiry
- Secure token storage (HttpOnly cookies)
- Rate limiting
- Audit logging

---

### 🔴 Q93: You discovered your TLS certificate private key was leaked. What do you do?
**Answer:**
**Immediate actions:**
1. **Revoke certificate** - Contact CA, request revocation
2. **Generate new key pair** - Never reuse compromised key
3. **Request new certificate** - With new key
4. **Deploy new certificate** - Update all servers
5. **Review logs** - Check for exploitation

**Investigation:**
1. When was key compromised?
2. How was it accessed?
3. Was traffic recorded (can be decrypted)?
4. If no PFS, past traffic is compromised

**Prevention:**
- Use ECDHE for forward secrecy
- Secure key storage (HSM)
- Monitor certificate transparency
- Short certificate validity

---

### 🟠 Q94: How would you securely exchange files between two systems?
**Answer:**
**Option 1: GPG/PGP encryption**
```bash
# Encrypt for recipient
gpg --encrypt --recipient recipient@email.com file.pdf

# Recipient decrypts
gpg --decrypt file.pdf.gpg
```

**Option 2: Age (modern alternative)**
```bash
# Generate keys
age-keygen -o key.txt

# Encrypt
age -r recipient_pubkey file.pdf > file.pdf.age

# Decrypt
age -d -i key.txt file.pdf.age > file.pdf
```

**Option 3: Automated/programmatic**
- SCP/SFTP (SSH-based)
- TLS-encrypted API transfer
- Cloud storage with client-side encryption

**Key considerations:**
- Verify recipient's public key
- Secure key exchange channel
- Include signature for authentication

---

### 🟠 Q95: A developer wants to use MD5 "just for checksums." Advise them.
**Answer:**
**Context matters:**

**Acceptable (non-security):**
- File integrity for accidental corruption
- Cache keying
- De-duplication
- Legacy compatibility requirements

**Never acceptable:**
- Password hashing
- Digital signatures
- Integrity against malicious modification
- Any security context

**Recommendation:**
```
"MD5 for simple checksums is technically okay, but I'd recommend 
SHA-256 instead because:
1. Only marginally slower on modern hardware
2. Future-proof if security context changes
3. Avoids confusion/code reuse in security contexts
4. Same API surface in most libraries

If performance critical, use xxHash or BLAKE3 for non-crypto."
```

---

### 🟠 Q96: Explain how you'd implement encryption at rest for a database.
**Answer:**
**Levels of encryption:**

**1. Full Disk Encryption (FDE)**
- BitLocker (Windows), LUKS (Linux)
- Protects against physical theft
- Doesn't protect running system

**2. Transparent Data Encryption (TDE)**
- Database-level (SQL Server, Oracle)
- Automatic encrypt/decrypt
- Protects database files

**3. Column-level encryption**
```sql
-- Encrypt sensitive columns
INSERT INTO users (name, ssn_encrypted) 
VALUES ('John', EncryptByKey(Key_GUID('SSNKey'), @ssn));
```
- Granular protection
- Application must handle keys

**4. Application-level encryption**
- Encrypt before storing
- Database never sees plaintext
- Most secure, most complex

**Key management:**
- Use KMS (AWS KMS, Azure Key Vault)
- Separate DEK and KEK
- Regular key rotation

---

### 🟡 Q97: How would you design a secure password reset flow?
**Answer:**
**Recommended flow:**
```
1. User requests reset → enters email
2. Server generates cryptographically random token (32+ bytes)
3. Store hash of token (not token itself)
4. Set expiration (15-30 minutes)
5. Send link with token via email
6. User clicks link → verify token hash matches
7. User sets new password
8. Invalidate token, invalidate all sessions
9. Notify user of password change
```

**Security considerations:**
- Token must be cryptographically random
- Store HASH of token (if DB compromised, tokens useless)
- Short expiration
- One-time use
- Rate limit requests
- Don't reveal if email exists
- Invalidate all active sessions
- Log reset events

---

### 🟡 Q98: How do you handle cryptographic key rotation?
**Answer:**
**Strategy:**

**1. Key versioning**
```json
{
  "keyId": "key-v3",
  "ciphertext": "..."
}
```
Include key version with encrypted data.

**2. Rotation process:**
1. Generate new key
2. New encryptions use new key
3. Keep old keys for decryption
4. Background re-encryption of old data
5. After migration, retire old keys

**3. Key types:**
- **Symmetric keys:** Re-encrypt data
- **Asymmetric keys:** Publish new public key, keep old private
- **TLS certificates:** Request new cert, deploy, revoke old

**4. KMS support:**
- AWS KMS automatic rotation
- Azure Key Vault versioning

**Key point:** Always maintain ability to decrypt old data during transition.

---

### 🟢 Q99: Design end-to-end encryption for a messaging app.
**Answer:**
**Signal Protocol approach:**

**Setup:**
1. Each user generates:
   - Identity key pair (long-term)
   - Signed prekey (medium-term)
   - One-time prekeys (ephemeral)
2. Publish public keys to server

**Key agreement (X3DH):**
1. Sender performs 4 DH operations:
   - (Identity_A, SignedPrekey_B)
   - (Identity_A, OneTimePrekey_B)
   - (Ephemeral_A, SignedPrekey_B)
   - (Ephemeral_A, OneTimePrekey_B)
2. Derive shared secret from DH results

**Messaging (Double Ratchet):**
1. Each message advances ratchet
2. DH ratchet: New key pair periodically
3. Symmetric ratchet: New key each message
4. Forward secrecy per message

**Key properties:**
- Past messages protected if current key leaked
- Future messages protected after compromise recovery
- Server never has keys

---

### 🟢 Q100: Prepare a migration plan from RSA-2048 to post-quantum cryptography.
**Answer:**
**Phase 1: Assessment (Now)**
- Inventory all cryptographic usage
- Identify RSA/ECC dependencies
- Assess "harvest now, decrypt later" risk
- Prioritize high-sensitivity systems

**Phase 2: Hybrid Implementation (Near-term)**
```
TLS: ECDHE + ML-KEM (both algorithms)
Signatures: ECDSA + ML-DSA
```
- Fallback if PQC vulnerable
- Compatibility maintained

**Phase 3: Testing (1-2 years)**
- Lab testing with PQC libraries
- Performance benchmarking
- Key size impact (ML-KEM keys larger)
- Protocol updates

**Phase 4: Deployment (2-5 years)**
- Gradual rollout
- Update TLS configurations
- Code signing with hybrid
- HSM support verification

**Phase 5: Pure PQC (Long-term)**
- Remove classical algorithms
- Full migration complete

**Resources:**
- NIST PQC standards
- liboqs (Open Quantum Safe)
- Cloudflare/Google PQC experiments

---

## 📋 Quick Revision - Top 20 Must-Know Concepts

1. **AES-256-GCM** - Standard symmetric encryption
2. **RSA-2048/4096** - Asymmetric minimum key sizes
3. **ECDHE** - Key exchange with forward secrecy
4. **Bcrypt/Argon2** - Password hashing
5. **SHA-256** - Standard cryptographic hash
6. **JWT + RS256** - API authentication
7. **TLS 1.3** - Current transport security
8. **Never ECB mode** - Always use CBC/GCM/CTR
9. **Salt every password** - Unique per user
10. **Never reuse nonces** - Catastrophic with same key
11. **HMAC for authentication** - Not raw hash + key
12. **Certificate chain** - Root → Intermediate → End-entity
13. **Key rotation** - Version keys, gradual migration
14. **HSM for critical keys** - CA keys, signing keys
15. **Post-quantum coming** - ML-KEM, ML-DSA
16. **Perfect forward secrecy** - Ephemeral keys
17. **Constant-time comparison** - Prevent timing attacks
18. **PKCS#1 OAEP** - RSA encryption padding
19. **X.509 certificates** - Identity binding
20. **Zero Trust crypto** - Verify everything, encrypt everywhere

---

*End of 100 Interview Questions - Cryptography*
