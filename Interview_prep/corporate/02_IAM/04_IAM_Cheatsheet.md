# ⚡ IAM — QUICK REFERENCE CHEATSHEET

> **Use:** Night-before-interview review | Daily IAM reference | Quick protocol lookup

---

## 🔑 IAM CORE PRINCIPLES — INSTANT RECALL

| Principle | One-liner |
|-----------|-----------|
| **Least Privilege** | Minimum access needed to do the job — nothing more |
| **Separation of Duties** | No single person controls a complete sensitive process |
| **Need-to-Know** | Access even within clearance level only if role requires it |
| **Zero Trust** | Never trust, always verify — verify every request, always |
| **Defense in Depth** | Multiple layers of identity controls |
| **Assume Breach** | Act as if attacker is already inside |

---

## 🔐 ACCESS CONTROL MODELS — QUICK COMPARE

| Model | Who Controls | Flexibility | Corporate Example |
|-------|-------------|-------------|------------------|
| **RBAC** | Roles | Medium | AD Groups, ERP roles |
| **ABAC** | Policy engine | Very High | Cloud IAM policies |
| **MAC** | System | Low | Government clearance |
| **DAC** | Owner | High | Windows file shares |
| **PBAC** | Central policy | High | Modern IGA tools |

---

## 🏛️ KERBEROS FLOW — MEMORIZE THIS

```
CLIENT          AS (KDC)         TGS (KDC)        SERVICE
  │                │                 │                │
  │──1: Username──▶│                 │                │
  │◀─2: TGT───────│ (encrypted w/KRBTGT hash)        │
  │                │                 │                │
  │──3: TGT + service request───────▶│                │
  │◀─4: TGS──────────────────────────│ (encrypted w/service hash)
  │                │                 │                │
  │──5: TGS──────────────────────────────────────────▶│
  │◀─6: Access Granted───────────────────────────────│

Key: No password ever sent over wire. Tickets + shared secrets only.
```

**Critical accounts:**
- **KRBTGT** → Signs all TGTs → Compromise = Golden Ticket
- **Domain Admin** → Full domain control → Most targeted
- **Service accounts with SPNs** → Kerberoasting target

---

## 📡 IAM PROTOCOLS — QUICK REFERENCE

| Protocol | Port | Purpose | Format |
|----------|------|---------|--------|
| **LDAP** | 389 | Directory queries | Binary/ASN.1 |
| **LDAPS** | 636 | Encrypted LDAP | Binary/TLS |
| **Kerberos** | 88 | AD Authentication | Binary |
| **NTLM** | - | Fallback Windows auth | Challenge/Response |
| **SAML** | 443 | Enterprise SSO | XML |
| **OAuth 2.0** | 443 | Authorization delegation | JSON |
| **OIDC** | 443 | Authentication (OAuth+) | JSON + JWT |
| **RADIUS** | 1812/1813 | Network access auth | Binary |
| **TACACS+** | 49 | Network device auth | TCP |

---

## 🔄 SAML vs OAUTH vs OIDC

| | SAML | OAuth 2.0 | OIDC |
|-|------|-----------|------|
| **Purpose** | Auth + Authz (mostly auth) | Authorization only | Auth + Authorization |
| **Format** | XML | JSON | JSON + JWT |
| **Use case** | Enterprise SSO | API access | Modern SSO |
| **Token** | SAML Assertion | Access Token | ID Token + Access Token |
| **Age** | 2002 | 2012 | 2014 |
| **Common use** | Okta → Salesforce | "Sign in with Google" API | Azure AD modern apps |

---

## 🎟️ JWT STRUCTURE

```
HEADER.PAYLOAD.SIGNATURE

Header (base64url):
{"alg": "RS256", "typ": "JWT"}

Payload (base64url):
{
  "sub": "user123",           ← Subject (user ID)
  "iss": "https://idp.com",   ← Issuer
  "aud": "api.myapp.com",     ← Audience
  "exp": 1716239022,          ← Expiry (Unix timestamp)
  "iat": 1716235422,          ← Issued at
  "name": "Alice",
  "roles": ["admin"]
}

Signature:
RS256(base64url(header) + "." + base64url(payload), privateKey)

ATTACKS:
alg:none    → Remove signature requirement
HS256 w/ pub key → Algorithm confusion
Claim tampering → Caught by signature (if verified correctly)

TOOL: jwt.io — decode/inspect any JWT
```

---

## 🏗️ OAUTH 2.0 FLOWS

| Flow | When to use | Notes |
|------|-------------|-------|
| **Authorization Code** | Web apps with server-side | Most secure, recommended |
| **Authorization Code + PKCE** | Mobile, SPA, public clients | PKCE prevents code interception |
| **Client Credentials** | M2M (no user) | Service-to-service |
| **Device Code** | CLI, TV, IoT | No browser |
| **Implicit** | DEPRECATED | Tokens in URL — insecure |
| **Resource Owner Password** | DEPRECATED | Sends password to client — insecure |

---

## 🏢 ACTIVE DIRECTORY QUICK REFERENCE

### Key Objects
| Object | Description |
|--------|-------------|
| User | Person or service identity |
| Computer | Machine identity |
| Group | Collection (Security or Distribution) |
| OU | Organizational Unit — container for GPO/delegation |
| GPO | Group Policy Object — applied to OU |
| SPN | Service Principal Name — Kerberos service identifier |

### Key AD Event IDs
| Event ID | What happened |
|----------|--------------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4648 | Logon with explicit credentials (RunAs/PTH) |
| 4672 | Special privileges assigned |
| 4720 | Account created |
| 4728 | Member added to security group |
| 4756 | Member added to universal security group |
| 4769 | Kerberos TGS requested (watch for Kerberoasting) |
| 4771 | Kerberos pre-auth failed |
| 4776 | NTLM credential validation |
| 5140 | Network share accessed |

### Logon Types
| Type | Name | Notes |
|------|------|-------|
| 2 | Interactive | Local console |
| 3 | Network | File shares, mapped drives |
| 4 | Batch | Scheduled tasks |
| 5 | Service | Service logon |
| 9 | NewCredentials | RunAs /netonly |
| 10 | RemoteInteractive | RDP |

---

## ⚔️ IAM ATTACK QUICK MAP

| Attack | What's needed | What you get | Detection |
|--------|--------------|--------------|-----------|
| **Password Spray** | Valid usernames | Valid credentials | Multiple accts, 1 failed login each, same source |
| **Kerberoasting** | Any domain user | Service account password | Event 4769, bulk TGS requests |
| **AS-REP Roasting** | Account w/no pre-auth | Account hash for cracking | Event 4768 with pre-auth failure |
| **Pass-the-Hash** | NTLM hash | Auth without password | Event 4648, NTLM logon Type 3 |
| **Golden Ticket** | KRBTGT hash | Domain-wide access forever | Unusual TGT lifetime, Event 4769 anomalies |
| **Silver Ticket** | Service account hash | Specific service access | No KDC event — stealth |
| **DCSync** | Replication rights | All domain hashes | Event 4662 with replication permission |
| **Kerberos PTT** | Valid TGT/TGS | Auth as ticket holder | Event 4769 from unusual source |
| **SAML Forgery** | Token signing cert | Forge any identity | Monitor SAML assertion anomalies |
| **OAuth Token Theft** | Steal access token | API access as user | Short token lifetime, binding helps |
| **MFA Fatigue** | Valid password | MFA bypass | Multiple push denials then approval |
| **AiTM Phishing** | Proxy setup | Post-MFA session | Impossible travel, new device detection |

---

## ☁️ CLOUD IAM QUICK REFERENCE

### AWS IAM
```
Policy evaluation order:
Explicit DENY → Allow → Implicit DENY (default)

Principal types: User | Group | Role | Service
Best practices:
  - Use roles, not users, for applications
  - Enable CloudTrail for all API logging
  - Never use root for daily tasks
  - Rotate access keys every 90 days (or use roles)
  - Use MFA for privileged users

Useful commands:
  aws iam list-users
  aws iam list-roles
  aws iam simulate-principal-policy
  aws iam get-policy-version
```

### Azure AD / Entra ID
```
Key roles:
  Global Admin     → Full tenant control (protect this!)
  User Admin       → Manage users/groups
  Security Admin   → Security features
  CA Admin         → Conditional Access
  Privileged Role Admin → Manage PIM

Conditional Access signals:
  User/Group | Location | Device | App | Sign-in risk | User risk

Key tools:
  Azure AD PIM     → JIT admin activation
  Identity Protection → Risk-based Conditional Access
  Access Reviews   → Built-in access review campaigns
  SSPR             → Self-service password reset
```

---

## 🔄 IDENTITY LIFECYCLE — JML QUICK CHECKLIST

### JOINER ✅
- [ ] Account provisioned in AD/IdP
- [ ] Role assigned from catalog
- [ ] Groups / app access assigned
- [ ] MFA enrolled
- [ ] Manager notified
- [ ] Welcome email with instructions

### MOVER ✅
- [ ] Old role access removed
- [ ] New role access granted
- [ ] No access accumulated from both roles
- [ ] Documented and approved
- [ ] Target systems updated

### LEAVER ✅
- [ ] Account disabled (same day as termination)
- [ ] All SSO sessions revoked
- [ ] MFA tokens de-registered
- [ ] Mailbox archived / forwarded
- [ ] Remote access (VPN) revoked
- [ ] Physical access revoked
- [ ] PAM accounts checked-in and password rotated
- [ ] Legal hold placed if needed
- [ ] Audit log preserved

---

## 🛡️ PAM QUICK REFERENCE

| Feature | What it does |
|---------|-------------|
| **Password Vaulting** | Encrypted storage, check-out model |
| **Session Recording** | Full video+keystroke of privileged sessions |
| **JIT Access** | Elevate on demand, auto-revoke |
| **Password Rotation** | Auto-rotate after use or on schedule |
| **Dual Control** | Two-person approval for high-risk actions |
| **A2A** | Remove hardcoded passwords from scripts/apps |

**Tools:** CyberArk (enterprise) | BeyondTrust | Delinea | HashiCorp Vault (DevOps)

---

## 📋 KEY IAM ACRONYMS

| Acronym | Full Form |
|---------|-----------|
| IAM | Identity and Access Management |
| PAM | Privileged Access Management |
| IGA | Identity Governance and Administration |
| CIAM | Customer Identity and Access Management |
| IdP | Identity Provider |
| SP | Service Provider |
| SSO | Single Sign-On |
| MFA | Multi-Factor Authentication |
| RBAC | Role-Based Access Control |
| ABAC | Attribute-Based Access Control |
| MAC | Mandatory Access Control |
| DAC | Discretionary Access Control |
| SoD | Separation of Duties |
| JML | Joiner-Mover-Leaver |
| JIT | Just-in-Time |
| TGT | Ticket Granting Ticket |
| TGS | Ticket Granting Service |
| KDC | Key Distribution Center |
| SPN | Service Principal Name |
| LDAP | Lightweight Directory Access Protocol |
| SAML | Security Assertion Markup Language |
| OIDC | OpenID Connect |
| JWT | JSON Web Token |
| SCIM | System for Cross-domain Identity Management |
| FIDO2 | Fast Identity Online 2 (WebAuthn) |
| gMSA | Group Managed Service Account |
| DC | Domain Controller |
| KRBTGT | Kerberos TGT account (special) |
| AD | Active Directory |
| GPO | Group Policy Object |
| OU | Organizational Unit |
| PKI | Public Key Infrastructure |
| ITDR | Identity Threat Detection and Response |
| PIM | Privileged Identity Management (Azure) |
| SSPR | Self-Service Password Reset |

---

## 🔗 ESSENTIAL IAM TOOLS (Bookmark These)

| Tool | URL | Use |
|------|-----|-----|
| jwt.io | https://jwt.io | Decode/inspect JWTs |
| SAML Tracer | Browser extension | Debug SAML flows |
| BloodHound | github.com/SpecterOps/BloodHound | AD attack paths |
| AWS Policy Simulator | console.aws.amazon.com/policysim | Test IAM policies |
| LDAP Browser | Various clients | Explore directory trees |
| HaveIBeenPwned | haveibeenpwned.com | Check credential breaches |
| Okta Dev Org | developer.okta.com | Free SSO/MFA lab |

---

> **🔖 IAM Cheatsheet — Print and keep at your desk.**
> 
> **Interview reminder:** IAM = Risk Management + Technology. Always frame answers in terms of what risk is being mitigated.

