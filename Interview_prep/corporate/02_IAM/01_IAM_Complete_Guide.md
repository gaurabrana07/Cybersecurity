# 🔑 IDENTITY & ACCESS MANAGEMENT (IAM) — CORPORATE COMPLETE GUIDE

> **Audience:** Entry to Mid-level Security Engineers, IAM Analysts, GRC Analysts entering corporate environments  
> **Scope:** Everything essential — concepts, architecture, protocols, tools, governance, real-world cases  
> **Last Updated:** 2026

---

## 📋 TABLE OF CONTENTS

1. [What is IAM?](#1-what-is-iam)
2. [Core IAM Concepts](#2-core-iam-concepts)
3. [Authentication Deep Dive](#3-authentication-deep-dive)
4. [Authorization & Access Control Models](#4-authorization--access-control-models)
5. [Identity Lifecycle Management](#5-identity-lifecycle-management)
6. [Privileged Access Management (PAM)](#6-privileged-access-management-pam)
7. [Single Sign-On (SSO) & Federation](#7-single-sign-on-sso--federation)
8. [Multi-Factor Authentication (MFA)](#8-multi-factor-authentication-mfa)
9. [Directory Services — Active Directory Deep Dive](#9-directory-services--active-directory-deep-dive)
10. [Cloud IAM (Azure AD / AWS IAM / GCP IAM)](#10-cloud-iam)
11. [Zero Trust & IAM](#11-zero-trust--iam)
12. [IAM Protocols — SAML, OAuth, OIDC, LDAP, Kerberos](#12-iam-protocols)
13. [IAM Governance & Compliance](#13-iam-governance--compliance)
14. [IAM Attack Vectors](#14-iam-attack-vectors)
15. [IAM Tools Ecosystem](#15-iam-tools-ecosystem)
16. [Real-World Case Studies](#16-real-world-case-studies)
17. [Day in the Life of an IAM Engineer](#17-day-in-the-life-of-an-iam-engineer)
18. [IAM in Corporate Environments (TCS, Big4, Banks, Enterprises)](#18-iam-in-corporate-environments)

---

## 1. What is IAM?

**Identity and Access Management (IAM)** is the discipline of ensuring the **right people have the right access to the right resources at the right time** — and that unauthorized access is prevented, detected, and responded to.

```
IAM ANSWERS THREE CORE QUESTIONS:

  WHO are you?          →   IDENTITY (Authentication)
  WHAT can you do?      →   ACCESS (Authorization)
  SHOULD you still?     →   GOVERNANCE (Lifecycle & Review)
```

### IAM Pillars

```
┌──────────────────────────────────────────────────────────────────┐
│                        IAM FRAMEWORK                             │
├────────────────┬─────────────────┬───────────────┬──────────────┤
│  IDENTITY      │  AUTHENTICATION │ AUTHORIZATION │  GOVERNANCE  │
│                │                 │               │              │
│ • User accts   │ • Passwords     │ • RBAC        │ • Access rev │
│ • Service accts│ • MFA           │ • ABAC        │ • Cert mgmt  │
│ • Machine IDs  │ • Certificates  │ • Policies    │ • Audit logs │
│ • Guest IDs    │ • Biometrics    │ • Entitlements│ • SOD        │
│ • Non-human IDs│ • SSO/SAML      │ • Least priv  │ • Compliance │
└────────────────┴─────────────────┴───────────────┴──────────────┘
```

### Why IAM is Critical

- **80%+ of breaches** involve compromised credentials or identity (Verizon DBIR)
- The perimeter is dead — **identity is the new perimeter**
- Remote work and cloud have exploded the attack surface for identity
- Regulatory requirements (SOX, HIPAA, PCI-DSS, GDPR) mandate access controls and audit trails
- Insider threats are primarily an identity problem

---

## 2. Core IAM Concepts

### 2.1 Identity Types

| Identity Type | Examples | Security Concern |
|--------------|---------|-----------------|
| **Human Identity** | Employees, contractors, customers | Credential theft, phishing |
| **Service Account** | App-to-app auth, scheduled jobs | Often over-privileged, passwords never rotated |
| **Machine Identity** | Servers, containers, IoT devices | Certificate expiry, weak auth |
| **Non-Human Identity (NHI)** | API keys, OAuth tokens, CI/CD bots | Hardcoded secrets in code |
| **Privileged Identity** | Domain admins, root accounts, DBAs | Highest risk — "keys to the kingdom" |
| **Guest/External Identity** | B2B partners, vendors, customers | Scope creep, over-permissioning |

### 2.2 Least Privilege Principle

> **Give users and systems the minimum access needed to perform their function — nothing more.**

```
BAD:  Developer has Domain Admin rights "because they needed it once"
GOOD: Developer has access only to their project's dev environment

BAD:  Service account has admin rights to all servers
GOOD: Service account has read-only access to specific DB tables it queries
```

**In practice:**
- Regular access reviews (quarterly is industry standard)
- Just-in-Time (JIT) access — grant elevated access for specific task, auto-revoke
- Break-glass accounts — emergency access with full logging and alerting

### 2.3 Separation of Duties (SoD)

> **No single person should have end-to-end control over a sensitive process.**

```
FINANCIAL EXAMPLE:
  Without SoD: One person can create a vendor + approve payment (fraud risk)
  With SoD: Person A creates vendor, Person B approves payment

IT EXAMPLE:
  Without SoD: Developer can push code AND approve their own deployment
  With SoD: Developer writes code, separate reviewer approves, separate deployer deploys
```

**SOD violations** are a major finding in audits (SOX, ISO 27001). IAM teams must detect and remediate them.

### 2.4 Need-to-Know

Access to information is granted only if the person genuinely needs it for their job function — even if they're authorized at the right clearance level.

---

## 3. Authentication Deep Dive

### Authentication Factors

```
FACTOR 1 — KNOWLEDGE (Something you KNOW)
├── Passwords
├── PINs
├── Security questions
└── Passphrases

FACTOR 2 — POSSESSION (Something you HAVE)
├── Hardware tokens (YubiKey, RSA SecurID)
├── Soft tokens (Google Authenticator, Microsoft Authenticator)
├── Smart cards / PIV cards
├── OTP via SMS (weaker — SIM swap risk)
└── Push notifications (Microsoft Authenticator push)

FACTOR 3 — INHERENCE (Something you ARE)
├── Fingerprint
├── Face recognition
├── Iris scan
├── Voice recognition
└── Behavioral biometrics (typing pattern, mouse movement)

FACTOR 4 — LOCATION (Where you ARE)
├── Geographic location (IP-based)
├── GPS coordinates
└── Network segment (on-premises vs remote)

FACTOR 5 — BEHAVIOR (What you DO)
├── Time of access
├── Device used
└── Access patterns (UEBA)
```

### Password Security

**Password Best Practices (NIST SP 800-63B — Current Standard):**

| Old Guidance (Wrong) | Current NIST Guidance (Correct) |
|---------------------|--------------------------------|
| Force change every 90 days | Change only when breach suspected |
| Require special chars | Allow all printable characters |
| Minimum 8 chars with complexity | Minimum 8 chars; longer = better |
| Prohibit password managers | Allow and encourage password managers |
| Security questions | Avoid — easily guessable |

**Why forced rotation backfires:** Users pick predictable patterns (Password1! → Password2! → Password3!) which is actually less secure than a long, memorable passphrase that never changes.

**Corporate password policy reality:**
- Most enterprises still enforce 90-day rotation (legacy culture)
- Password managers mandated for teams (LastPass, 1Password, CyberArk)
- Privileged account passwords rotated every 30 days or after each use (PAM tools handle this)

### Passwordless Authentication

The future of enterprise auth — eliminates the weakest link (passwords):

| Method | How | Example |
|--------|-----|---------|
| **FIDO2/WebAuthn** | Cryptographic key pair on device | YubiKey, Windows Hello |
| **Certificate-based** | X.509 certificate instead of password | Smart card logon |
| **Magic Links** | One-time URL sent to email | Slack, some SaaS apps |
| **Biometric** | Fingerprint/Face as primary auth | Windows Hello, Touch ID |
| **Push Notification** | Approve on trusted device | Microsoft Authenticator |

---

## 4. Authorization & Access Control Models

### 4.1 RBAC — Role-Based Access Control

> Access is granted based on **roles** (job functions), not individual users.

```
USERS      →    ROLES       →    PERMISSIONS    →    RESOURCES
Alice            Finance Analyst   Read invoices       Accounting DB
Bob              Finance Analyst   Read invoices       Accounting DB
Carol            Finance Manager   Read + Approve      Accounting DB
                                  invoices
```

**Pros:** Easy to manage, scalable, audit-friendly  
**Cons:** Role explosion (companies end up with thousands of roles), can't handle attribute-based exceptions

**Enterprise reality:** Most corporate systems use RBAC — Active Directory groups are a form of RBAC.

---

### 4.2 ABAC — Attribute-Based Access Control

> Access decisions based on **attributes** of user, resource, environment, and action.

```
Policy: Allow access IF:
  User.Department = "Finance"
  AND User.ClearanceLevel >= "Confidential"
  AND Resource.Classification = "Confidential"
  AND Environment.Time BETWEEN "09:00" AND "18:00"
  AND Environment.Location = "Corporate Network"
```

**Pros:** Very granular, handles complex scenarios, more flexible than RBAC  
**Cons:** Complex to implement, harder to audit, performance overhead

---

### 4.3 PBAC — Policy-Based Access Control

Combines RBAC + ABAC. Policies define who can do what under what conditions. Used in modern cloud IAM (AWS IAM policies are a form of PBAC).

---

### 4.4 MAC — Mandatory Access Control

> Access controlled by the **system** based on security labels — users cannot grant their own access.

```
Security Labels:
  Top Secret > Secret > Confidential > Unclassified

Rule: User with "Secret" clearance can access "Confidential" and "Secret" data
      User with "Confidential" clearance CANNOT access "Secret" data
      (No-read-up, No-write-down = Bell-LaPadula model)
```

**Used in:** Government, military systems. Rarely in commercial (too rigid).

---

### 4.5 DAC — Discretionary Access Control

> **Resource owner** decides who can access their data.

```
Alice owns a file → Alice decides Bob can read it → Alice grants Bob read permission
```

**Examples:** Windows NTFS file permissions (right-click → Properties → Security)  
**Risk:** Users can accidentally or maliciously over-share.

---

### 4.6 Access Control Models Comparison

| Model | Who Controls Access | Flexibility | Example |
|-------|---------------------|-------------|---------|
| RBAC | Roles | Medium | AD Groups, most enterprise |
| ABAC | Policy engine | Very High | Cloud IAM policies |
| MAC | System | Low (most restrictive) | Government systems |
| DAC | Resource owner | High | Windows file shares |
| PBAC | Centralized policies | High | Modern IGA tools |

---

## 5. Identity Lifecycle Management

### The Joiner-Mover-Leaver (JML) Process

```
JOINER → MOVER → LEAVER
(New hire) (Role change) (Departure)

JOINER:                    MOVER:                    LEAVER:
├── Provision accounts      ├── Add new role access    ├── Disable accounts
├── Assign role(s)          ├── Remove old role access  ├── Revoke all access
├── Assign groups           ├── Update group membership ├── Archive mailbox
├── Issue hardware token    ├── Update reporting line   ├── Reclaim assets
├── Onboarding training     ├── Notify affected systems ├── Preserve audit trail
└── Manager approval flow   └── Documented & audited    └── Legal hold if needed
```

### Provisioning & Deprovisioning

**Manual provisioning** (legacy, common in mid-size companies):
- IT creates AD account manually
- Manager emails HR who emails IT
- Risk: Days of delay, inconsistent access, forgotten deprovisions

**Automated provisioning** (modern, enterprise):
- HRIS (Workday, SAP) triggers IAM system (SailPoint, Saviynt)
- Account created automatically based on job code / department mapping
- Access rights assigned from role catalog
- Onboarding completes before Day 1

**The orphan account problem:**
```
Risk: Employee leaves → manager doesn't tell IT → account stays active
      → 3 months later, ex-employee still has access via VPN
      → Found in audit → Compliance finding

Solution:
  1. Automate deprovisioning from HRIS termination event
  2. Regular orphan account scans (accounts with no logon in 90+ days)
  3. Access reviews (quarterly) to catch missed deprovisions
```

### Access Request & Approval Workflow

```
User requests access
        │
        ▼
Access request submitted via IAM portal (SailPoint, Saviynt, ServiceNow)
        │
        ▼
Auto-approval? (Is this a pre-approved entitlement for this role?)
  YES → Auto-grant
  NO  → Route to approver (typically direct manager + resource owner)
        │
        ▼
Approver reviews business justification
  APPROVE → Access granted + logged in audit trail
  DENY    → Request closed + reason documented
        │
        ▼
Access provisioned in target system
        │
        ▼
Scheduled for next access review (90/180 days)
```

---

## 6. Privileged Access Management (PAM)

### What is PAM?

PAM is a subset of IAM focused specifically on managing, monitoring, and controlling **privileged accounts** — those with elevated permissions that can cause significant damage if compromised.

```
PRIVILEGED ACCOUNTS:
├── Domain Administrators (AD)
├── Local Administrator accounts
├── Root accounts (Linux/Unix)
├── Database Administrator (DBA) accounts
├── Service accounts with elevated access
├── Cloud IAM admin roles (AWS root, Azure Global Admin)
├── Network device accounts (firewall admin, switch admin)
└── Application admin accounts
```

### Why PAM is Critical

- Privileged accounts are **the most targeted** by attackers
- A compromised domain admin = complete organizational compromise
- Many breaches show attackers spent days/weeks with stolen privileged credentials
- Regulatory compliance (SOX, PCI-DSS, HIPAA) mandates privileged access controls

### PAM Core Capabilities

| Capability | What it does | Business Value |
|------------|-------------|----------------|
| **Password Vaulting** | Store privileged passwords in encrypted vault | No one knows the password — it's checked out |
| **Password Rotation** | Auto-rotate passwords after each use or on schedule | Limits window if credential is stolen |
| **Session Recording** | Record every keystroke/screen during privileged session | Full audit trail, legal evidence |
| **Session Monitoring** | Real-time monitoring of live sessions | Detect anomalous activity mid-session |
| **Just-in-Time (JIT) Access** | Grant elevated access for specific task, auto-revoke | No standing privilege |
| **Dual Control** | Require second person to approve before privileged action | Separation of duties for high-risk actions |
| **Application-to-Application (A2A)** | Eliminate hardcoded passwords in code | Secures service account credentials in apps |

### PAM Workflow

```
Admin needs to access Production DB:
  ↓
Login to PAM portal (CyberArk, BeyondTrust)
  ↓
Request access to "Prod-DB-Admin" account
  ↓
PAM auto-approves (or routes to manager for approval if high-risk)
  ↓
PAM checks out password from vault (user never sees actual password)
  ↓
Session launched via PAM proxy → full session recording begins
  ↓
Admin performs task
  ↓
Session ends → Password automatically rotated
  ↓
Session recording stored in secure archive (compliance requirement)
  ↓
SOC/Audit team can review recording at any time
```

### Popular PAM Tools

| Tool | Vendor | Key Strength |
|------|--------|-------------|
| **CyberArk** | CyberArk | Industry leader, most comprehensive, banking/govt standard |
| **BeyondTrust** | BeyondTrust | Strong endpoint privilege, good UX |
| **Delinea (Thycotic/Centrify)** | Delinea | More affordable than CyberArk, cloud-native option |
| **HashiCorp Vault** | HashiCorp | Open-source base, excellent for DevOps/cloud secrets |
| **Keeper PAM** | Keeper | SMB-friendly, user-friendly |

---

## 7. Single Sign-On (SSO) & Federation

### What is SSO?

SSO allows users to **authenticate once** and gain access to multiple applications without re-authenticating for each one.

```
WITHOUT SSO:                    WITH SSO:
User opens Salesforce           User opens Salesforce
→ Enter credentials             → Redirected to Identity Provider
User opens Workday              → Enters credentials ONCE
→ Enter credentials again       → SSO token issued
User opens ServiceNow           → Access to Salesforce ✓
→ Enter credentials again       User opens Workday → Access ✓
User opens Jira                 User opens ServiceNow → Access ✓
→ Enter credentials again       User opens Jira → Access ✓
                                NO re-authentication needed
```

**Benefits:**
- Better user experience (one login for everything)
- Centralized access revocation (disable IdP account → access cut everywhere)
- Better security (users don't create weak passwords for dozens of apps)
- Reduced help desk load (fewer password reset calls)

### Federation

Federation extends SSO across **organizational boundaries** — user authenticates with their home organization's IdP to access resources in a partner organization.

```
EXAMPLE: Employee of Acme Corp accessing a vendor's portal

Acme Corp User → Acme Corp IdP (trusts Acme identities)
                       ↓
              Federation Trust (SAML/OIDC)
                       ↓
                 Vendor Portal (trusts Acme's assertions)
                       ↓
              User gets access WITHOUT a vendor account
```

**Real-world use:** B2B portals, multi-cloud access, government agency collaboration.

---

## 8. Multi-Factor Authentication (MFA)

### MFA Factor Strength Comparison

| Method | Strength | Phishable? | Resistance |
|--------|----------|-----------|-----------|
| SMS OTP | Weak | YES (SIM swap, phishing) | Low |
| Email OTP | Weak | YES (email account compromise) | Low |
| Authenticator App (TOTP) | Medium | YES (real-time phishing proxy) | Medium |
| Push notification | Medium | YES (MFA fatigue attack) | Medium |
| Push with number matching | Medium-High | Harder | Medium-High |
| FIDO2/WebAuthn (hardware key) | Very High | NO (bound to domain) | Very High |
| Certificate-based auth | Very High | NO | Very High |

### MFA Attacks

**MFA Fatigue (Push Bombing):**
```
Attacker has password (via phishing/breach)
→ Sends 50+ push notifications to victim's phone
→ Victim gets annoyed and taps "Approve" to stop the noise
→ Attacker is in

DEFENSE: Number matching (user must type code shown on screen into phone),
         Additional context (show IP/location of request in push notification),
         Limit push attempts, then require hardware key
```

**SIM Swapping:**
```
Attacker social engineers mobile carrier
→ Convinces them to transfer victim's number to attacker's SIM
→ Attacker now receives SMS OTPs
→ Bypasses SMS-based MFA

DEFENSE: Use authenticator app or hardware token, never SMS OTP for high-value accounts
```

**Real-time Phishing Proxy (AiTM — Adversary in the Middle):**
```
Attacker stands up fake Microsoft 365 login page
→ Victim enters credentials (captured by attacker)
→ Victim enters MFA code (captured by attacker, immediately replayed)
→ Attacker gets authenticated session cookie
→ Session cookie used to access victim's account (MFA already satisfied)

DEFENSE: FIDO2/hardware keys (domain-bound, proxy can't replay),
         Conditional Access policies requiring compliant device
```

---

## 9. Directory Services — Active Directory Deep Dive

### What is Active Directory?

Active Directory (AD) is Microsoft's on-premises directory service — the identity backbone of most enterprise Windows environments.

```
ACTIVE DIRECTORY STRUCTURE:

Forest (top level — trust boundary)
└── Domain (acme.com)
    ├── Organizational Units (OUs — like folders)
    │   ├── Users OU
    │   │   ├── Alice (User object)
    │   │   └── Bob (User object)
    │   ├── Computers OU
    │   │   ├── WORKSTATION-01 (Computer object)
    │   │   └── SERVER-01 (Computer object)
    │   └── Groups OU
    │       ├── Finance-Analysts (Security Group)
    │       └── HR-Managers (Security Group)
    └── Domain Controllers (DCs — authenticating servers)
```

### Kerberos Authentication (How AD auth works)

```
KERBEROS FLOW:

1. Client → KDC (DC): "I want to log in, here's my username"
   
2. KDC → Client: AS-REP with TGT (Ticket Granting Ticket)
   (TGT encrypted with KRBTGT account's hash)

3. Client → KDC: "I need access to FileServer, here's my TGT"

4. KDC → Client: TGS (Ticket Granting Service ticket) for FileServer
   (TGS encrypted with FileServer's account hash)

5. Client → FileServer: "Here's my TGS"

6. FileServer → Client: "Access granted"

KEY SECURITY NOTES:
- TGT encrypted with KRBTGT hash → Stealing KRBTGT = Golden Ticket attack
- TGS encrypted with service account hash → Kerberoasting attack
- NTLM is fallback when Kerberos fails → Pass-the-hash attacks
```

### Key AD Concepts

| Concept | What it is | Security Relevance |
|---------|-----------|-------------------|
| **Domain Controller (DC)** | Server that handles auth and stores AD | Highest-value target — compromise = game over |
| **KRBTGT account** | Special account used to sign all Kerberos tickets | Steal hash → Golden Ticket (unlimited domain access) |
| **Domain Admin** | Full control of entire domain | Most targeted privileged account |
| **Service Account** | Account used by applications/services | Often over-privileged, weak passwords |
| **Group Policy (GPO)** | Centrally manage settings for users/computers | Can be abused for persistence |
| **ACLs/ACEs** | Access Control Lists/Entries on AD objects | Misconfigurations lead to privilege escalation |
| **Trust** | Relationship between two domains/forests | Misconfigured trusts = lateral movement path |
| **SPN (Service Principal Name)** | Identifies service instances | Kerberoastable if service account has SPN + weak password |

### Key AD Attack Paths

| Attack | Technique | What Attacker Gets |
|--------|-----------|-------------------|
| **Kerberoasting** | Request TGS for service SPNs, crack offline | Service account password |
| **AS-REP Roasting** | Request AS-REP for accounts with pre-auth disabled | Account hash for offline cracking |
| **Pass-the-Hash** | Use NTLM hash instead of password | Auth without knowing password |
| **Pass-the-Ticket** | Steal and reuse Kerberos ticket | Auth as ticket owner |
| **Golden Ticket** | Forge TGT with KRBTGT hash | Unlimited, persistent domain access |
| **Silver Ticket** | Forge TGS with service account hash | Access specific service without DC involvement |
| **DCSync** | Replicate AD (requires Replication rights) | All password hashes in domain |
| **BloodHound/SharpHound** | Enumerate AD relationships | Attack path discovery |

---

## 10. Cloud IAM

### Azure AD / Microsoft Entra ID

Microsoft's cloud identity platform — extends on-premises AD to cloud.

```
KEY AZURE AD CONCEPTS:

Tenant          → Organization's dedicated Azure AD instance
User            → Human identity
Service Principal → App's identity in Azure AD
Managed Identity → Service identity auto-managed by Azure (no credential management)
App Registration → Register an app to use Azure AD auth

ROLES:
Global Administrator  → Ultimate power (protect this account!)
User Administrator   → Manage users and groups
Security Administrator → Manage security features
Conditional Access   → Policy-based access control
```

**Conditional Access Policies (Critical for corporate security):**
```
POLICY EXAMPLE:
IF:
  User = "Any"
  App = "Microsoft 365"
  Condition: Sign-in from outside corporate IP range
THEN:
  Require MFA
  
POLICY EXAMPLE 2:
IF:
  User = "Global Admins"
  Any condition
THEN:
  Require MFA + Compliant Device + Named Location
```

---

### AWS IAM

AWS's cloud permission system for managing access to AWS resources.

```
KEY AWS IAM CONCEPTS:

Users    → Human identity (avoid for apps — use roles)
Groups   → Collection of users with shared permissions
Roles    → Identity assumed by users, apps, or AWS services
Policies → JSON documents defining permissions

POLICY STRUCTURE:
{
  "Effect": "Allow",           ← Allow or Deny
  "Action": "s3:GetObject",    ← What action
  "Resource": "arn:aws:s3:::my-bucket/*",  ← On what resource
  "Condition": {               ← Optional: when
    "IpAddress": {
      "aws:SourceIp": "192.0.2.0/24"
    }
  }
}
```

**AWS IAM Best Practices:**
- Never use root account for daily tasks
- Enable MFA on root and all privileged users
- Use roles instead of long-term access keys
- Apply least privilege — start with nothing, add as needed
- Enable CloudTrail (audit log for all AWS API calls)
- Rotate access keys regularly, scan for exposed keys in code (GitGuardian)

---

### GCP IAM

Google Cloud's identity and access management.

```
PRINCIPALS:  Google Account, Service Account, Group, Domain
ROLES:       Primitive (Owner/Editor/Viewer), Predefined, Custom
BINDINGS:    Resource → Role → Principal
```

**GCP IAM best practice:** Use service accounts with minimal permissions, prefer Workload Identity Federation over service account keys.

---

## 11. Zero Trust & IAM

### Zero Trust Principles

```
TRADITIONAL "CASTLE AND MOAT":
Outside → Firewall → Trust everything inside

ZERO TRUST:
"Never trust, always verify"
→ Every request verified, regardless of source (inside or outside network)
→ Assume breach — act as if attacker is already inside
```

### Zero Trust & IAM Integration

| Zero Trust Principle | IAM Implementation |
|---------------------|-------------------|
| **Verify explicitly** | MFA, Conditional Access, risk-based auth |
| **Use least privilege** | RBAC, JIT access, PAM |
| **Assume breach** | Continuous monitoring, behavioral analytics, micro-segmentation |

### Zero Trust Access Flow

```
User requests access to application
        ↓
Identity verified (MFA, certificate, risk score)
        ↓
Device health checked (compliant? patched? managed?)
        ↓
Conditional Access policy evaluated:
  - Is this a normal sign-in time?
  - Is this a trusted location?
  - Is this a managed device?
  - What's the user's risk score?
        ↓
Access granted / denied / step-up MFA required
        ↓
Session continuously monitored
```

---

## 12. IAM Protocols

### 12.1 LDAP — Lightweight Directory Access Protocol

- Protocol for accessing and maintaining distributed directory services
- Used to query Active Directory (LDAP queries against AD)
- Port: 389 (LDAP), 636 (LDAPS — encrypted)
- **Risk:** LDAP injection attacks, unencrypted LDAP exposes credentials

```
LDAP QUERY EXAMPLE:
(&(objectClass=user)(sAMAccountName=alice))
→ Find user object where username = alice

LDAP INJECTION:
Normal: (&(uid=alice)(password=secret))
Attack: (&(uid=*)(password=anything))  → Returns all users
```

---

### 12.2 Kerberos

- Network authentication protocol used in AD environments (covered in Section 9)
- Based on tickets, not passwords transmitted over network
- Uses symmetric key cryptography with a trusted third party (KDC)
- Port: 88

---

### 12.3 SAML — Security Assertion Markup Language

XML-based standard for exchanging authentication and authorization data between parties — particularly between an Identity Provider (IdP) and Service Provider (SP).

```
SAML SSO FLOW:

1. User → SP: "I want to access Salesforce"
2. SP → User: Redirect to IdP (Okta, Azure AD)
3. User → IdP: Authenticate (username + MFA)
4. IdP → User: SAML Assertion (signed XML) saying "This is Alice, she's verified"
5. User → SP: Presents SAML Assertion
6. SP: Validates signature, grants access

KEY CONCEPTS:
SP  = Service Provider (the app being accessed)
IdP = Identity Provider (the authenticating authority)
SAML Assertion = Signed statement of identity
```

**SAML Attacks:**
- **SAML Assertion Forgery** — Weak signature verification, attacker forges assertion
- **XML Signature Wrapping (XSW)** — Manipulate XML structure to confuse signature validation
- **IdP Impersonation** — Attacker stands up fake IdP if SP misconfigured

---

### 12.4 OAuth 2.0

Authorization framework — allows applications to obtain **limited access** to user accounts on an HTTP service.

```
OAUTH 2.0 FLOW (Authorization Code Flow):

1. User: "I want to use App X"
2. App X: "You need to authorize me to access your Google data"
3. User → Google: "Allow App X to read my calendar"
4. Google → App X: Authorization code
5. App X → Google: Exchange code for access token
6. App X uses access token to read user's calendar

KEY ROLES:
Resource Owner = User (you)
Client = Application (App X)
Authorization Server = Google
Resource Server = Google Calendar API

OAuth is AUTHORIZATION, not authentication
→ It grants access to resources, not identity verification
```

**OAuth Attacks:**
- **Authorization Code Interception** — Steal auth code via open redirect
- **CSRF on OAuth** — Force user to complete OAuth flow for attacker's account
- **Token Theft** — Steal access tokens from browser/network
- **Scope Abuse** — App requests more permissions than needed

---

### 12.5 OpenID Connect (OIDC)

Authentication layer built on top of OAuth 2.0. While OAuth provides authorization, OIDC adds identity verification.

```
OAuth 2.0 = "Can I access your files?" (authorization)
OIDC      = "Who are you?" + "Can I access your files?" (authentication + authorization)

OIDC adds:
- ID Token (JWT containing user identity claims)
- UserInfo endpoint (retrieve more user details)
- Standard claims: sub (subject/user ID), email, name, picture
```

**JWT (JSON Web Token) — Key for OIDC:**
```
Structure: Header.Payload.Signature (base64 encoded)

Header:  {"alg":"RS256","typ":"JWT"}
Payload: {
  "sub": "1234567890",
  "name": "Alice",
  "email": "alice@acme.com",
  "exp": 1716239022,    ← Expiry timestamp
  "iat": 1716235422     ← Issued at
}
Signature: RS256(base64(header) + "." + base64(payload), privateKey)

JWT ATTACK — Algorithm Confusion:
→ Change "alg": "RS256" to "alg": "none" → Signature not verified
→ Use HS256 with public key as secret → Forge tokens
→ Always verify algorithm server-side, never trust header
```

---

## 13. IAM Governance & Compliance

### Access Reviews (Certification Campaigns)

Periodic reviews where managers certify that their team's access is still appropriate.

```
QUARTERLY ACCESS REVIEW PROCESS:

1. IAM system compiles access report for each manager
2. Manager reviews: "Does Alice still need Finance DB Admin?"
3. Decision: CERTIFY (keep access) or REVOKE (remove access)
4. Revocations auto-provisioned to target systems
5. Results stored for audit evidence

WHAT GETS REVIEWED:
- Application entitlements
- Privileged account memberships
- Dormant accounts (no login in 90+ days)
- Excessive access (user has more than role requires)
- SoD conflicts

COMPLIANCE REQUIREMENT:
- SOX: Quarterly reviews for financial system access
- PCI-DSS: Regular reviews for cardholder data access
- HIPAA: Annual reviews for patient data access
```

### Identity Governance & Administration (IGA)

IGA extends basic IAM with governance capabilities:

| Capability | Description |
|-----------|-------------|
| **Role Management** | Define and maintain role catalog |
| **Access Request** | Self-service access request with approval workflows |
| **Access Review** | Automated campaigns for periodic recertification |
| **SoD Analysis** | Detect and manage separation of duties conflicts |
| **Audit & Reporting** | Compliance-ready reports for auditors |
| **Role Mining** | Analyze existing access patterns to suggest optimal roles |

**Popular IGA Tools:**

| Tool | Vendor | Notes |
|------|--------|-------|
| **SailPoint IdentityNow** | SailPoint | Market leader, most comprehensive |
| **Saviynt** | Saviynt | Strong cloud IAM governance, SAP expertise |
| **Omada Identity** | Omada | Strong in European compliance |
| **IBM Security Verify** | IBM | Enterprise, pairs with QRadar |
| **Oracle Identity Governance** | Oracle | Strong in Oracle ecosystem |

### Compliance Mapping

| Regulation | IAM Requirements |
|-----------|-----------------|
| **SOX** | Access controls on financial systems, quarterly reviews, SoD, audit trails |
| **PCI-DSS** | Unique user IDs, MFA, least privilege, regular access reviews, PAM for admin accounts |
| **HIPAA** | Unique user auth, automatic logoff, encryption, audit controls, access authorization |
| **GDPR** | Access controls for personal data, right of access, data minimization |
| **ISO 27001** | A.9: Access control, A.9.2: User access management, A.9.4: System and application access |
| **NIST 800-53** | AC-2: Account Management, AC-6: Least Privilege, IA-5: Authenticator Management |

---

## 14. IAM Attack Vectors

### Credential-Based Attacks

| Attack | How it works | Detection | Mitigation |
|--------|-------------|-----------|-----------|
| **Password Spraying** | Try 1 common password against many accounts (avoids lockout) | Multiple failed logins for different accounts from same IP | Account lockout, MFA |
| **Credential Stuffing** | Use breached credential lists against other services | Unusual login patterns, geographical anomalies | MFA, breach notification service (HaveIBeenPwned API) |
| **Brute Force** | Try all password combinations | Rapid failed login attempts | Account lockout, CAPTCHA, rate limiting |
| **Phishing** | Trick user into giving credentials | User reports, email gateway alerts | Security awareness, anti-phishing MFA (FIDO2) |
| **Keylogging** | Malware captures keystrokes | EDR behavioral detection | EDR, least privilege |

### Token & Session Attacks

| Attack | How it works | Mitigation |
|--------|-------------|-----------|
| **Pass-the-Hash** | Use NTLM hash without knowing password | Disable NTLM, use Kerberos, enforce signing |
| **Pass-the-Ticket** | Reuse stolen Kerberos ticket | Short ticket lifetimes, monitor unusual TGS usage |
| **Golden Ticket** | Forge TGT using KRBTGT hash | Protect KRBTGT, rotate KRBTGT hash twice after breach |
| **Silver Ticket** | Forge service ticket using service account hash | Strong service account passwords, monitor unusual service access |
| **Token Theft** | Steal OAuth/session tokens | HTTPS only, short token lifetimes, token binding |
| **AiTM Phishing** | Proxy attack captures session after MFA | FIDO2/hardware keys, Conditional Access on device compliance |

### Privilege Escalation Paths

```
TYPICAL ATTACK PATH IN AD ENVIRONMENT:

1. Initial Access: Phishing → compromise standard user account
2. Reconnaissance: BloodHound to map AD attack paths
3. Lateral Movement: PSExec to move to workstation with local admin
4. Privilege Escalation: Kerberoasting → crack service account → has local admin somewhere
5. More Movement: Reach DC admin machine via compromised service account
6. Domain Compromise: DCSync → dump all NTLM hashes including KRBTGT
7. Golden Ticket: Use KRBTGT hash → permanent domain access
```

---

## 15. IAM Tools Ecosystem

### Complete IAM Tool Landscape

```
┌─────────────────────────────────────────────────────────────────┐
│                    IAM TOOL ECOSYSTEM                           │
├──────────────┬───────────────┬──────────────┬──────────────────┤
│  DIRECTORY   │     IGA       │     PAM      │    FEDERATION    │
├──────────────┼───────────────┼──────────────┼──────────────────┤
│ Active Dir.  │ SailPoint     │ CyberArk     │ Okta             │
│ Azure AD     │ Saviynt       │ BeyondTrust  │ Ping Identity    │
│ OpenLDAP     │ IBM Verify    │ Delinea      │ ForgeRock        │
│ FreeIPA      │ Omada         │ HashiCorp    │ Azure AD B2B     │
│              │               │ Vault        │                  │
├──────────────┼───────────────┼──────────────┼──────────────────┤
│  SSO / MFA   │  CLOUD IAM    │ CIAM         │ SECRETS MGMT     │
├──────────────┼───────────────┼──────────────┼──────────────────┤
│ Okta         │ AWS IAM       │ Auth0 (Okta) │ HashiCorp Vault  │
│ Azure AD     │ Azure AD      │ Cognito      │ AWS Secrets Mgr  │
│ Ping         │ GCP IAM       │ ForgeRock    │ Azure Key Vault  │
│ Duo Security │               │              │ CyberArk Conjur  │
└──────────────┴───────────────┴──────────────┴──────────────────┘
```

---

## 16. Real-World Case Studies

### Case Study 1: SolarWinds — Supply Chain via Identity (2020)

**What happened:**
Attackers compromised SolarWinds' build pipeline and inserted the Sunburst backdoor. Once deployed in victim environments, the backdoor:
1. Waited 12-14 days (avoiding sandbox detection)
2. Beaconed to C2 using legitimate-looking avsvmcloud.com subdomains
3. Used **identity-based techniques** to move laterally:
   - Impersonated existing users (token manipulation)
   - Forged SAML tokens using a stolen ADFS token signing certificate
   - Created new service principals in Azure AD with application admin permissions

**IAM Failures:**
- ADFS token signing certificate was not adequately protected
- Forged SAML tokens were not detected (no anomaly detection on SAML assertions)
- Service principal activity wasn't monitored
- No behavioral baseline for SAML/OAuth activity

**IAM Lessons:**
- Monitor and alert on new service principal creation
- Protect token signing certificates (hardware HSMs)
- Audit SAML authentication events for anomalies
- Implement Conditional Access based on risk signals, not just credential validation
- Enable Sentinel/Defender for Identity to detect on-premises identity attacks

---

### Case Study 2: Colonial Pipeline — Compromised VPN Credential (2021)

**What happened:**
DarkSide ransomware group gained access via a **compromised VPN password** — no MFA was enabled on that account.

```
Attack timeline:
- Password found in breached credential dump (dark web)
- VPN account authenticated successfully — no MFA required
- Attacker moved laterally from IT to OT network
- Ransomware deployed → pipeline operations shut down
- $4.4 million ransom paid
```

**IAM Failures:**
- No MFA on VPN (single factor = single point of failure)
- Compromised password not detected (no integration with breach databases)
- No network segmentation between IT and OT environments
- VPN access not reviewed — was it an active account? For whom?

**IAM Lessons:**
- MFA is non-negotiable for all remote access — no exceptions
- Integrate HaveIBeenPwned API to detect credentials in breach databases
- Regular access reviews for VPN accounts
- Conditional Access: require known device + MFA for any remote access

---

### Case Study 3: Insider Threat via Access Reviews Failure — Financial Firm

**What happened:**
A back-office employee changed departments but their access to the trading system was never revoked. Over 18 months, they:
- Accessed trading data they had no business need for
- Leaked information to external parties
- Detected during annual security audit when access review found 4,200 active accounts exceeding their role requirements

**IAM Failures:**
- No automated deprovisioning when employee changed roles (Mover process failure)
- Access reviews were annual (too infrequent) and manual (too slow)
- No UEBA to detect out-of-role access patterns

**IAM Lessons:**
- Implement automated Mover provisioning from HRIS role change events
- Quarterly access reviews at minimum (monthly for privileged access)
- UEBA on data access patterns — flag when a user accesses data outside their role's norm
- Birthright access model: define what each role should have; deviation = automatic flag

---

### Case Study 4: Okta Breach via Support Engineer Laptop (2022)

**What happened:**
Threat actor Lapsus$ gained access to an Okta support engineer's laptop via a third-party contractor (Sitel Group).

```
Attack chain:
1. Contractor (Sitel) support engineer's laptop compromised
2. Engineer had access to Okta support portal (customer tenants)
3. Attacker pivoted through Okta support access to customer orgs
4. Affected customers: Cloudflare, Microsoft, and others
5. Okta took 2 months to notify customers → reputational damage
```

**IAM Failures:**
- Third-party contractor had excessive access to customer data
- Third-party security posture not adequately monitored
- Detection delay — LAPSUS$ posted screenshots before Okta even knew
- Incident response and disclosure was delayed

**IAM Lessons:**
- Third-party access must be scoped, time-limited, and monitored
- Just-In-Time (JIT) access for support engineers — access only during active cases
- Session recording for all support access to sensitive systems
- Rapid detection: monitor for unusual support portal access patterns
- Incident communication plans must include third-party breach scenarios

---

## 17. Day in the Life of an IAM Engineer

### Morning: Access Provisioning & Requests

```
08:00 - Review overnight access requests queue
        → New joiner account provisioning requests
        → Application access requests requiring approval
        → Role-change requests (movers)

08:30 - Process urgent deprovisions
        → Termination notifications from HRIS
        → Disable accounts, revoke tokens, archive mailbox

09:00 - Review access review campaign status
        → Which managers haven't completed their review? (Send reminders)
        → Revocations approved → execute in target systems

09:30 - Check service account expiry calendar
        → Any passwords or certificates expiring this week?
        → Coordinate rotation with application teams
```

### Midday: Technical Work & Investigations

```
10:00 - SIEM/monitoring review
        → Alerts from IAM monitoring: failed privileged access, unusual login times
        → Investigate anomalies (new device login for admin account)

11:00 - Technical project work
        → Migrating legacy app from LDAP to SAML-based SSO
        → Writing SCIM integration for new SaaS application
        → Updating Conditional Access policies in Azure AD

14:00 - SOC escalation: Investigate suspicious account activity
        → User account showing authentication from two countries simultaneously
        → Coordinate with SOC to determine compromise or VPN usage
        → Decision: Force password reset + MFA re-registration
```

### Afternoon: Governance & Compliance

```
15:00 - Audit preparation
        → Pull access reports for auditor (who has access to Finance system?)
        → Verify SoD conflicts are documented and accepted/mitigated
        → Evidence collection for quarterly compliance review

16:00 - Role engineering session
        → Working with business team to define new "Data Scientist" role
        → Identify entitlements needed, check for SoD conflicts
        → Document and get approval before implementation

17:00 - Update documentation
        → Update IAM procedures for new cloud app integration
        → Update runbooks for access provisioning edge cases
```

---

## 18. IAM in Corporate Environments

### How IAM Functions in Large Enterprises (TCS/Big4/Banks)

```
IAM TEAM STRUCTURE (Large Enterprise):

IAM Manager
├── IAM Architects       ← Design IAM solutions, protocol experts
├── IAM Engineers        ← Implement, configure, integrate
├── IAM Analysts         ← Day-to-day operations, access reviews
├── PAM Specialists      ← CyberArk/BeyondTrust management
└── IGA Analysts         ← SailPoint/Saviynt campaigns, governance
```

### Key IAM Challenges in Corporate

| Challenge | Reality | Solution |
|-----------|---------|---------|
| **Shadow IT** | Business teams adopting cloud apps without IT | CASB, SSO mandate, app discovery |
| **Legacy Systems** | Old apps don't support SAML/OIDC | Reverse proxy, header-based SSO, gradual migration |
| **Access Sprawl** | Users accumulate access over years | Regular access reviews, automated reviews, role right-sizing |
| **Service Account Chaos** | Thousands of service accounts, forgotten passwords | PAM vaulting, automated discovery, lifecycle management |
| **M&A Integration** | Acquiring company with different IAM stack | Forest trust, federation, gradual migration |
| **Third-Party Access** | Contractors/vendors need access | B2B federation, JIT access, PAM for privileged third-party |

### IAM Certifications for Corporate Value

| Certification | Issuer | Value |
|---------------|--------|-------|
| **CIAM** | Identity Management Institute | Entry-level IAM focused |
| **Certified Identity Professional (CIDPRO)** | Identity Management Institute | Mid-level |
| **CISSP** | ISC² | Covers IAM as domain, broad security recognition |
| **SailPoint Certified IdentityNow Engineer** | SailPoint | High value in enterprises using SailPoint |
| **CyberArk Defender + Sentry** | CyberArk | High value in enterprises using CyberArk |
| **Microsoft Identity and Access Administrator (SC-300)** | Microsoft | High value in Microsoft/Azure shops |
| **AWS Certified Security Specialty** | AWS | Covers IAM deep, high demand |
| **Okta Certified Administrator** | Okta | Valuable in Okta-heavy environments |

---

> **💡 Corporate Reality Check:** In most large enterprises, IAM touches everything — every application onboarding, every offboarding, every audit. IAM engineers who understand both the technical protocols (SAML, OAuth, Kerberos) AND the governance side (access reviews, SoD, compliance) are extremely valuable. Pure technical people without governance understanding, and pure governance people without technical skills, both struggle to be effective.

> **📝 New Corporate IAM Tip:** In your first weeks, get access to the IAM system's audit log. Understanding the history of access changes — who approved what, why, when — will teach you more about the real IAM landscape than any documentation.

