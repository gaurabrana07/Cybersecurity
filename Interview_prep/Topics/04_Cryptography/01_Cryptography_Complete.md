# 🔑 CRYPTOGRAPHY - Complete Guide

## Table of Contents
1. [What is Cryptography?](#what-is-cryptography)
2. [Cryptographic Concepts](#cryptographic-concepts)
3. [Symmetric Encryption](#symmetric-encryption)
4. [Asymmetric Encryption](#asymmetric-encryption)
5. [Hashing](#hashing)
6. [Digital Signatures](#digital-signatures)
7. [Public Key Infrastructure (PKI)](#public-key-infrastructure-pki)
8. [TLS/SSL](#tlsssl)
9. [Common Attacks on Cryptography](#common-attacks-on-cryptography)
10. [Interview Questions](#interview-questions)
11. [Learning Resources](#learning-resources)

---

## What is Cryptography?

### Definition

**Cryptography** is the science of **securing communication and data** by transforming information into an unreadable format that can only be decoded by authorized parties.

### Why Cryptography Matters

```
┌─────────────────────────────────────────────────────────────┐
│            CRYPTOGRAPHY & CIA TRIAD                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONFIDENTIALITY ─────► Encryption keeps data secret        │
│                                                             │
│  INTEGRITY ───────────► Hashing detects modifications       │
│                                                             │
│  AUTHENTICATION ──────► Digital signatures verify identity  │
│                                                             │
│  NON-REPUDIATION ─────► Cannot deny sending a message       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Terminology

| Term | Definition |
|------|------------|
| **Plaintext** | Original readable message |
| **Ciphertext** | Encrypted (unreadable) message |
| **Encryption** | Process of converting plaintext to ciphertext |
| **Decryption** | Process of converting ciphertext to plaintext |
| **Key** | Secret value used in encryption/decryption |
| **Cipher** | Algorithm used for encryption |

---

## Cryptographic Concepts

### The Basic Process

```
┌─────────────────────────────────────────────────────────────┐
│                ENCRYPTION PROCESS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   PLAINTEXT              ENCRYPTION             CIPHERTEXT  │
│  ┌─────────┐            ┌─────────┐            ┌─────────┐ │
│  │ Hello   │ ─────────► │Algorithm│ ─────────► │X#7kM@!  │ │
│  │ World   │     +      │ (AES)   │            │2pQ9#    │ │
│  └─────────┘    KEY     └─────────┘            └─────────┘ │
│                                                             │
│   ─────────────────────────────────────────────────────────  │
│                                                             │
│   CIPHERTEXT             DECRYPTION             PLAINTEXT   │
│  ┌─────────┐            ┌─────────┐            ┌─────────┐ │
│  │X#7kM@!  │ ─────────► │Algorithm│ ─────────► │ Hello   │ │
│  │2pQ9#    │     +      │ (AES)   │            │ World   │ │
│  └─────────┘    KEY     └─────────┘            └─────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Types of Cryptography

```
┌─────────────────────────────────────────────────────────────┐
│               CRYPTOGRAPHY TYPES                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. SYMMETRIC ENCRYPTION                                     │
│     └── Same key for encryption & decryption                │
│     └── Fast, used for bulk data                            │
│     └── Examples: AES, DES, 3DES, Blowfish                  │
│                                                             │
│  2. ASYMMETRIC ENCRYPTION                                    │
│     └── Two keys: Public (encrypt) + Private (decrypt)      │
│     └── Slower, used for key exchange & signatures          │
│     └── Examples: RSA, ECC, Diffie-Hellman                  │
│                                                             │
│  3. HASHING                                                  │
│     └── One-way function (cannot reverse)                   │
│     └── Fixed-size output regardless of input               │
│     └── Examples: SHA-256, SHA-3, bcrypt                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Symmetric Encryption

### How It Works

**Same key** is used for both encryption and decryption.

```
┌─────────────────────────────────────────────────────────────┐
│              SYMMETRIC ENCRYPTION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    SHARED SECRET KEY                         │
│                          🔑                                  │
│                     ┌────┴────┐                             │
│                     ▼         ▼                             │
│  SENDER          Encrypt   Decrypt          RECEIVER        │
│  ┌──────┐       ┌──────┐   ┌──────┐        ┌──────┐        │
│  │Plain │──────►│Cipher│───►│Cipher│───────►│Plain │        │
│  │Text  │       │Text  │   │Text  │        │Text  │        │
│  └──────┘       └──────┘   └──────┘        └──────┘        │
│                                                             │
│  KEY DISTRIBUTION PROBLEM:                                   │
│  How do you securely share the key?                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Common Symmetric Algorithms

| Algorithm | Key Size | Block Size | Status |
|-----------|----------|------------|--------|
| **AES** | 128/192/256 bits | 128 bits | ✅ Current standard |
| **3DES** | 168 bits | 64 bits | ⚠️ Legacy, avoid |
| **DES** | 56 bits | 64 bits | ❌ Broken, deprecated |
| **Blowfish** | 32-448 bits | 64 bits | ⚠️ Replaced by Twofish |
| **ChaCha20** | 256 bits | Stream | ✅ Modern, fast |

### AES (Advanced Encryption Standard)

```
┌─────────────────────────────────────────────────────────────┐
│                    AES DETAILS                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  • Adopted by NIST in 2001                                  │
│  • Symmetric block cipher                                   │
│  • Block size: 128 bits                                     │
│  • Key sizes: 128, 192, or 256 bits                        │
│                                                             │
│  Rounds based on key size:                                  │
│    AES-128: 10 rounds                                       │
│    AES-192: 12 rounds                                       │
│    AES-256: 14 rounds                                       │
│                                                             │
│  Each round performs:                                       │
│    1. SubBytes (substitution)                               │
│    2. ShiftRows (permutation)                               │
│    3. MixColumns (mixing)                                   │
│    4. AddRoundKey (XOR with round key)                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Block Cipher Modes

```
┌─────────────────────────────────────────────────────────────┐
│              BLOCK CIPHER MODES                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ECB (Electronic Codebook) - ❌ INSECURE                     │
│  ├── Same plaintext block = Same ciphertext block           │
│  └── Pattern leakage (famous penguin example)               │
│                                                             │
│  CBC (Cipher Block Chaining) - ✅ Secure                     │
│  ├── Each block XORed with previous ciphertext             │
│  ├── Requires Initialization Vector (IV)                    │
│  └── Sequential (cannot parallelize)                        │
│                                                             │
│  CTR (Counter Mode) - ✅ Secure                              │
│  ├── Turns block cipher into stream cipher                  │
│  ├── Can parallelize                                       │
│  └── Random access to encrypted data                        │
│                                                             │
│  GCM (Galois/Counter Mode) - ✅ RECOMMENDED                  │
│  ├── CTR + Authentication tag                              │
│  ├── Provides confidentiality AND integrity                │
│  └── Used in TLS 1.3                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Pros & Cons

| Pros | Cons |
|------|------|
| ✅ Very fast | ❌ Key distribution problem |
| ✅ Low computational overhead | ❌ Each pair needs unique key |
| ✅ Good for large data | ❌ Doesn't provide non-repudiation |

---

## Asymmetric Encryption

### How It Works

Uses a **key pair**: Public key (share freely) + Private key (keep secret)

```
┌─────────────────────────────────────────────────────────────┐
│            ASYMMETRIC ENCRYPTION                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BOB wants to send secret message to ALICE                  │
│                                                             │
│        BOB                                  ALICE           │
│        │                                      │             │
│        │  1. Alice shares her PUBLIC KEY      │             │
│        │◄─────────────────────────────────────│             │
│        │      🔓 (can share with anyone)      │             │
│        │                                      │             │
│        │  2. Bob encrypts with Alice's        │             │
│        │     PUBLIC KEY                       │             │
│   ┌─────────┐                                 │             │
│   │Plaintext│                                 │             │
│   │ + 🔓    │                                 │             │
│   └────┬────┘                                 │             │
│        ▼                                      │             │
│   ┌─────────┐                                 │             │
│   │Ciphertext│─────────────────────────────►  │             │
│   └─────────┘  3. Sends ciphertext            │             │
│                                               │             │
│                   4. Alice decrypts with      │             │
│                      PRIVATE KEY              │             │
│                           ┌─────────┐         │             │
│                           │Ciphertext         │             │
│                           │ + 🔐    │         │             │
│                           └────┬────┘         │             │
│                                ▼              │             │
│                           ┌─────────┐         │             │
│                           │Plaintext│         │             │
│                           └─────────┘         │             │
│                                                             │
│  🔓 Public Key = Encrypt (or verify signature)              │
│  🔐 Private Key = Decrypt (or create signature)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Common Asymmetric Algorithms

| Algorithm | Key Size | Use Case | Status |
|-----------|----------|----------|--------|
| **RSA** | 2048-4096 bits | Encryption, signatures | ✅ Common |
| **ECC** | 256-384 bits | Same as RSA, smaller keys | ✅ Modern, efficient |
| **Diffie-Hellman** | 2048+ bits | Key exchange only | ✅ Common |
| **ECDH** | 256-384 bits | Key exchange | ✅ Modern |
| **DSA** | 2048 bits | Signatures only | ⚠️ Being phased out |

### RSA Algorithm

```
┌─────────────────────────────────────────────────────────────┐
│                    RSA OVERVIEW                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  KEY GENERATION:                                            │
│  1. Choose two large prime numbers: p and q                 │
│  2. Calculate n = p × q (modulus)                           │
│  3. Calculate φ(n) = (p-1)(q-1)                             │
│  4. Choose public exponent e (commonly 65537)               │
│  5. Calculate private exponent d (modular inverse)          │
│                                                             │
│  PUBLIC KEY:  (n, e)                                        │
│  PRIVATE KEY: (n, d)                                        │
│                                                             │
│  ENCRYPTION:   C = M^e mod n                                │
│  DECRYPTION:   M = C^d mod n                                │
│                                                             │
│  Security based on difficulty of factoring large primes     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Elliptic Curve Cryptography (ECC)

```
┌─────────────────────────────────────────────────────────────┐
│                    ECC vs RSA                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ECC 256-bit ≈ RSA 3072-bit (equivalent security)          │
│                                                             │
│  Benefits:                                                  │
│  ✅ Smaller keys                                            │
│  ✅ Faster computations                                     │
│  ✅ Less bandwidth                                          │
│  ✅ Better for mobile/IoT                                   │
│                                                             │
│  Common Curves:                                             │
│  • P-256 (secp256r1) - NIST recommended                    │
│  • P-384, P-521                                            │
│  • Curve25519 - Modern, fast                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Pros & Cons

| Pros | Cons |
|------|------|
| ✅ Solves key distribution | ❌ Slow (1000x slower than symmetric) |
| ✅ Digital signatures | ❌ Larger key sizes |
| ✅ Non-repudiation | ❌ Computationally expensive |

### Hybrid Encryption (Real-World Usage)

```
┌─────────────────────────────────────────────────────────────┐
│              HYBRID ENCRYPTION (TLS)                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PROBLEM: Asymmetric is secure but slow                     │
│          Symmetric is fast but has key distribution issue   │
│                                                             │
│  SOLUTION: Use both!                                        │
│                                                             │
│  1. Use ASYMMETRIC to securely exchange a symmetric key     │
│  2. Use SYMMETRIC for actual data encryption                │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Step 1: Key Exchange (Asymmetric)                    │  │
│  │         Client ──── RSA/ECDH ────► Server            │  │
│  │         (Exchange symmetric session key)              │  │
│  │                                                       │  │
│  │ Step 2: Data Transfer (Symmetric)                     │  │
│  │         Client ════ AES-256-GCM ════ Server           │  │
│  │         (Fast encrypted communication)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hashing

### What is Hashing?

A **one-way function** that converts any input into a fixed-size output (digest/hash).

### Properties of Good Hash Functions

```
┌─────────────────────────────────────────────────────────────┐
│            HASH FUNCTION PROPERTIES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. DETERMINISTIC                                            │
│     Same input → Always same output                         │
│                                                             │
│  2. FIXED OUTPUT SIZE                                        │
│     Any input size → Fixed hash size                        │
│     "Hello" → 64 char SHA-256                               │
│     (1GB file) → 64 char SHA-256                            │
│                                                             │
│  3. ONE-WAY (Pre-image Resistance)                           │
│     Cannot reverse hash to get original                     │
│     Hash → ❌ → Original                                    │
│                                                             │
│  4. COLLISION RESISTANT                                      │
│     Nearly impossible for two inputs to produce same hash   │
│                                                             │
│  5. AVALANCHE EFFECT                                         │
│     Tiny change → Completely different hash                 │
│     "Hello" ≠ "hello" (different hashes)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Hash Examples

```
Input: "Hello World"

MD5:    b10a8db164e0754105b7a99be72e3fe5           (128 bits) ❌ Broken
SHA-1:  0a4d55a8d778e5022fab701977c5d840bbc486d0   (160 bits) ❌ Broken
SHA-256: a591a6d40bf420404a011733cfb7b190...        (256 bits) ✅ Secure
SHA-3:  369183d3786773cef4e56c7b849...               (256 bits) ✅ Secure

Input: "Hello World!" (added exclamation)

SHA-256: 7f83b1657ff1fc53b92dc18148a1d65d...  (COMPLETELY DIFFERENT!)
```

### Common Hash Algorithms

| Algorithm | Output Size | Status | Use Case |
|-----------|-------------|--------|----------|
| **MD5** | 128 bits | ❌ Broken | Checksums only (not security) |
| **SHA-1** | 160 bits | ❌ Broken | Avoid |
| **SHA-256** | 256 bits | ✅ Secure | General purpose |
| **SHA-3** | 224-512 bits | ✅ Secure | Future-proof |
| **bcrypt** | 184 bits | ✅ Secure | Password hashing |
| **Argon2** | Variable | ✅ Secure | Password hashing (recommended) |

### Password Hashing

```
┌─────────────────────────────────────────────────────────────┐
│            PASSWORD HASHING BEST PRACTICES                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ❌ WRONG WAY:                                               │
│     password_hash = SHA256(password)                        │
│     • Fast to compute = Fast to crack                       │
│     • No salt = Rainbow table attacks work                  │
│                                                             │
│  ✅ RIGHT WAY:                                               │
│     password_hash = bcrypt(password, salt, cost=12)         │
│                                                             │
│  WHY bcrypt/Argon2 IS BETTER:                               │
│  1. SALTING: Random salt added to each password             │
│     └── Same password → Different hashes                    │
│     └── Defeats rainbow tables                              │
│                                                             │
│  2. COST FACTOR: Intentionally slow                         │
│     └── bcrypt with cost=12: ~250ms per hash               │
│     └── SHA-256: Millions per second                       │
│     └── Slows down brute force attacks                     │
│                                                             │
│  3. MEMORY-HARD (Argon2):                                    │
│     └── Requires significant memory                         │
│     └── Hard to parallelize on GPUs                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Hashing vs Encryption

| Hashing | Encryption |
|---------|------------|
| One-way (irreversible) | Two-way (reversible) |
| Fixed output size | Output size varies |
| No key required | Key required |
| Verify integrity | Protect confidentiality |

---

## Digital Signatures

### What is a Digital Signature?

A cryptographic proof that a message:
1. **Came from a specific sender** (authentication)
2. **Was not modified** (integrity)
3. **Sender cannot deny sending** (non-repudiation)

### How Digital Signatures Work

```
┌─────────────────────────────────────────────────────────────┐
│              DIGITAL SIGNATURE PROCESS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SIGNING (Sender):                                          │
│  ┌──────────┐                                               │
│  │ Message  │                                               │
│  └────┬─────┘                                               │
│       │                                                     │
│       ▼                                                     │
│  ┌──────────┐     ┌──────────────┐     ┌─────────────┐     │
│  │  Hash    │────►│ Hash Value   │────►│ Encrypt with│     │
│  │ Function │     │ (e.g. SHA256)│     │ PRIVATE KEY │     │
│  └──────────┘     └──────────────┘     └──────┬──────┘     │
│                                               │             │
│                                        ┌──────▼──────┐      │
│                                        │  SIGNATURE  │      │
│                                        └─────────────┘      │
│                                                             │
│  Send: Message + Signature                                  │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  VERIFICATION (Receiver):                                   │
│                                                             │
│  ┌──────────┐     ┌──────────┐          ┌──────────┐       │
│  │ Message  │────►│   Hash   │──────────│ Hash A   │       │
│  └──────────┘     │ Function │          └────┬─────┘       │
│                   └──────────┘               │             │
│                                              │ Compare     │
│  ┌───────────┐     ┌──────────────┐         │             │
│  │ Signature │────►│ Decrypt with │──────┐  │             │
│  └───────────┘     │ PUBLIC KEY   │      │  │             │
│                    └──────────────┘      │  │             │
│                                          ▼  ▼             │
│                                    ┌───────────┐          │
│                                    │ Hash A =  │          │
│                                    │ Hash B ?  │          │
│                                    └─────┬─────┘          │
│                                          │                │
│                               ┌──────────┴──────────┐     │
│                               ▼                     ▼     │
│                          ✅ VALID            ❌ INVALID   │
│                          (Authentic)         (Tampered)   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Digital Signature Algorithms

| Algorithm | Based On | Status |
|-----------|----------|--------|
| **RSA Signature** | RSA | ✅ Common |
| **ECDSA** | Elliptic Curves | ✅ Modern, efficient |
| **Ed25519** | Edwards Curves | ✅ Fast, secure |
| **DSA** | Discrete Log | ⚠️ Being replaced |

---

## Public Key Infrastructure (PKI)

### What is PKI?

A framework for **managing digital certificates** and **public key encryption**.

### PKI Components

```
┌─────────────────────────────────────────────────────────────┐
│                    PKI COMPONENTS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              CERTIFICATE AUTHORITY (CA)               │  │
│  │   ├── Root CA (Self-signed, highly protected)        │  │
│  │   └── Intermediate CA (Issues end-entity certs)     │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                  │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              DIGITAL CERTIFICATE                      │  │
│  │   ├── Subject (who the cert is for)                  │  │
│  │   ├── Public Key                                     │  │
│  │   ├── Issuer (CA that signed it)                     │  │
│  │   ├── Validity Period                                │  │
│  │   └── Digital Signature (of CA)                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                  │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              REGISTRATION AUTHORITY (RA)              │  │
│  │   └── Verifies identity before cert issuance        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         CERTIFICATE REVOCATION LIST (CRL)            │  │
│  │   └── List of revoked certificates                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Certificate Chain of Trust

```
┌─────────────────────────────────────────────────────────────┐
│              CERTIFICATE CHAIN                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│       ┌─────────────────┐                                   │
│       │   ROOT CA       │  (Self-signed, trusted by OS)     │
│       │   Certificate   │                                   │
│       └────────┬────────┘                                   │
│                │ Signs                                      │
│                ▼                                            │
│       ┌─────────────────┐                                   │
│       │ INTERMEDIATE CA │  (Signed by Root)                 │
│       │   Certificate   │                                   │
│       └────────┬────────┘                                   │
│                │ Signs                                      │
│                ▼                                            │
│       ┌─────────────────┐                                   │
│       │   END ENTITY    │  (Your website certificate)       │
│       │   Certificate   │                                   │
│       │  (example.com)  │                                   │
│       └─────────────────┘                                   │
│                                                             │
│   Browser verifies chain from end entity up to trusted root │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### X.509 Certificate Fields

| Field | Description |
|-------|-------------|
| **Version** | Certificate format version (v3 is current) |
| **Serial Number** | Unique identifier from CA |
| **Subject** | Entity the certificate identifies |
| **Issuer** | CA that issued the certificate |
| **Validity** | Not Before / Not After dates |
| **Public Key** | Subject's public key |
| **Extensions** | Additional info (SAN, key usage) |
| **Signature** | CA's digital signature |

---

## TLS/SSL

### What is TLS?

**Transport Layer Security (TLS)** provides encrypted communication over networks. SSL is the deprecated predecessor.

### TLS Versions

| Version | Status | Notes |
|---------|--------|-------|
| SSL 3.0 | ❌ Deprecated | POODLE vulnerability |
| TLS 1.0 | ❌ Deprecated | Weak, PCI non-compliant |
| TLS 1.1 | ❌ Deprecated | Weak |
| TLS 1.2 | ✅ Acceptable | Still widely used |
| TLS 1.3 | ✅ Recommended | Faster, more secure |

### TLS 1.3 Handshake

```
┌─────────────────────────────────────────────────────────────┐
│              TLS 1.3 HANDSHAKE (1-RTT)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     CLIENT                              SERVER              │
│        │                                   │                │
│        │ ─────── ClientHello ────────────► │                │
│        │        (Supported ciphers,        │                │
│        │         Key share, Extensions)    │                │
│        │                                   │                │
│        │ ◄────── ServerHello ───────────── │                │
│        │        (Chosen cipher,            │                │
│        │         Key share,                │                │
│        │         Certificate,              │                │
│        │         CertificateVerify,        │                │
│        │         Finished)                 │                │
│        │                                   │                │
│        │ ─────── Finished ─────────────► │                  │
│        │                                   │                │
│        │ ════════ Encrypted Data ═══════  │                │
│        │                                   │                │
│                                                             │
│  TLS 1.3 Benefits:                                          │
│  • 1-RTT handshake (was 2-RTT in TLS 1.2)                  │
│  • 0-RTT resumption                                         │
│  • Removed weak algorithms                                  │
│  • Perfect Forward Secrecy required                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Perfect Forward Secrecy (PFS)

```
┌─────────────────────────────────────────────────────────────┐
│            PERFECT FORWARD SECRECY                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  WITHOUT PFS:                                               │
│  • Same private key used for all sessions                   │
│  • If key compromised → ALL past traffic decryptable        │
│                                                             │
│  WITH PFS (Ephemeral Keys):                                 │
│  • New key pair generated for each session                  │
│  • If one session key compromised → Only THAT session       │
│  • Past sessions remain protected                           │
│                                                             │
│  Algorithms providing PFS:                                  │
│  • ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)         │
│  • DHE (Diffie-Hellman Ephemeral)                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Common Attacks on Cryptography

### Attack Types

```
┌─────────────────────────────────────────────────────────────┐
│            CRYPTOGRAPHIC ATTACKS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. BRUTE FORCE                                              │
│     └── Try all possible keys                               │
│     └── Prevention: Use long keys (256-bit)                 │
│                                                             │
│  2. DICTIONARY ATTACK                                        │
│     └── Try common passwords/words                          │
│     └── Prevention: Complex passwords, salting              │
│                                                             │
│  3. RAINBOW TABLE                                            │
│     └── Pre-computed hash lookups                           │
│     └── Prevention: Salting passwords                       │
│                                                             │
│  4. BIRTHDAY ATTACK                                          │
│     └── Find collision based on probability                 │
│     └── Prevention: Use 256+ bit hashes                     │
│                                                             │
│  5. SIDE-CHANNEL ATTACK                                      │
│     └── Timing, power consumption analysis                  │
│     └── Prevention: Constant-time implementations           │
│                                                             │
│  6. MAN-IN-THE-MIDDLE                                        │
│     └── Intercept key exchange                              │
│     └── Prevention: Certificate verification                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Known Vulnerabilities

| Vulnerability | Affected | Impact |
|---------------|----------|--------|
| **POODLE** | SSL 3.0 | Decrypt TLS traffic |
| **BEAST** | TLS 1.0 | Decrypt cookies |
| **Heartbleed** | OpenSSL | Memory leak, key exposure |
| **DROWN** | SSLv2 servers | Decrypt TLS sessions |
| **CRIME** | TLS compression | Decrypt cookies |

---

## Interview Questions

### Basic Questions

**Q1: What is the difference between symmetric and asymmetric encryption?**
> "Symmetric encryption uses the same key for encryption and decryption, making it fast and suitable for bulk data (e.g., AES). Asymmetric encryption uses a public-private key pair - public key encrypts, private key decrypts. It's slower but solves key distribution and enables digital signatures (e.g., RSA, ECC)."

**Q2: Why can't you use SHA-256 directly for password hashing?**
> "SHA-256 is designed to be fast, which makes it vulnerable to brute-force and dictionary attacks - attackers can try billions of hashes per second. Password hashing algorithms like bcrypt or Argon2 are intentionally slow (with adjustable cost factors) and include salting to prevent rainbow table attacks."

**Q3: What is a digital signature and how does it work?**
> "A digital signature provides authentication, integrity, and non-repudiation. The sender hashes the message and encrypts the hash with their private key. The receiver decrypts with the sender's public key and compares hashes. If they match, the message is authentic and unchanged."

### Advanced Questions

**Q4: Explain Perfect Forward Secrecy.**
> "Perfect Forward Secrecy ensures that if a long-term private key is compromised, past session communications remain secure. This is achieved by generating ephemeral (temporary) key pairs for each session using algorithms like ECDHE. Even if an attacker later obtains the server's private key, they cannot decrypt previously captured traffic."

**Q5: How does TLS 1.3 improve over TLS 1.2?**
> "TLS 1.3 reduces handshake from 2-RTT to 1-RTT, supports 0-RTT resumption for faster connections, removes weak algorithms (RSA key exchange, CBC mode, SHA-1), mandates Perfect Forward Secrecy, and encrypts more of the handshake for better privacy."

---

## Learning Resources

### 📚 Websites

| Website | Link | What You'll Learn |
|---------|------|-------------------|
| **Crypto101** | https://www.crypto101.io/ | Free introductory book |
| **Cryptography I (Stanford)** | https://www.coursera.org/learn/crypto | Academic foundations |
| **Practical Cryptography** | https://cryptography.io/ | Python implementation |
| **CryptoHack** | https://cryptohack.org/ | Interactive challenges |
| **OWASP Crypto Cheat Sheet** | https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html | Best practices |

### 🎥 YouTube Videos

| Video | Link | Duration |
|-------|------|----------|
| **Public Key Cryptography** | https://www.youtube.com/watch?v=GSIDS_lvRv4 | ~12 min |
| **How TLS Works** | https://www.youtube.com/watch?v=86cQJ0MMses | ~15 min |
| **AES Explained** | https://www.youtube.com/watch?v=O4xNJsjtN6E | ~20 min |
| **Computerphile - Cryptography** | https://www.youtube.com/playlist?list=PLzH6n4zXuckqmf_xUcvU5caZVoctP2ehL | Playlist |
| **Digital Signatures** | https://www.youtube.com/watch?v=s22eJ1eVLTU | ~10 min |

### 📖 Courses

| Course | Platform | Link |
|--------|----------|------|
| **Cryptography I** | Coursera (Stanford) | https://www.coursera.org/learn/crypto |
| **Applied Cryptography** | Udacity | https://www.udacity.com/course/applied-cryptography--cs387 |
| **Cryptography** | Khan Academy | https://www.khanacademy.org/computing/computer-science/cryptography |
| **CompTIA Security+** | Various | https://www.comptia.org/certifications/security |

### 🛠️ Practice

| Resource | Link | Description |
|----------|------|-------------|
| **CryptoHack** | https://cryptohack.org/ | Crypto challenges |
| **Cryptopals** | https://cryptopals.com/ | Programming challenges |
| **PicoCTF** | https://picoctf.org/ | CTF with crypto section |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│           CRYPTOGRAPHY QUICK REFERENCE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SYMMETRIC (Same Key):                                      │
│  ├── Use: Bulk data encryption                              │
│  ├── Recommended: AES-256-GCM, ChaCha20-Poly1305           │
│  └── Avoid: DES, 3DES, ECB mode                            │
│                                                             │
│  ASYMMETRIC (Key Pair):                                     │
│  ├── Use: Key exchange, digital signatures                  │
│  ├── Recommended: RSA-2048+, ECC P-256, Ed25519            │
│  └── Hybrid: Use with symmetric for best of both           │
│                                                             │
│  HASHING:                                                   │
│  ├── General: SHA-256, SHA-3                               │
│  ├── Passwords: bcrypt, Argon2 (WITH SALT!)                │
│  └── Avoid: MD5, SHA-1 for security                        │
│                                                             │
│  TLS:                                                       │
│  ├── Use: TLS 1.3 (or TLS 1.2 minimum)                     │
│  ├── Ciphers: ECDHE + AES-GCM or ChaCha20                  │
│  └── Require: Perfect Forward Secrecy                      │
│                                                             │
│  KEY PRINCIPLES:                                            │
│  • Never roll your own crypto                              │
│  • Use well-vetted libraries                               │
│  • Proper key management is crucial                        │
│  • Algorithm strength ≠ Implementation strength            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Next Topic: [Malware and Threats](../05_Malware_and_Threats/01_Malware_Types.md)*
