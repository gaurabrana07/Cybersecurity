# 🎯 IAM — INTERVIEW QUESTIONS BANK

> **Coverage:**  
> 🔴 Priority Questions (Core IAM — asked in 90%+ interviews)  
> 🟡 Job-Switching Questions (For laterals / domain switchers)  
> 🟢 Experience-Based / Scenario Questions  
> 🔵 Behavioral / Situational Questions (Corporate cultural fit)

---

## 📋 TABLE OF CONTENTS

1. [Priority — Core Concepts](#-priority--core-concepts)
2. [Priority — Protocols (SAML, OAuth, OIDC, Kerberos)](#-priority--protocols)
3. [Priority — Active Directory & PAM](#-priority--active-directory--pam)
4. [Priority — Cloud IAM](#-priority--cloud-iam)
5. [Priority — Governance & Compliance](#-priority--governance--compliance)
6. [Job-Switching Questions](#-job-switching-questions)
7. [Experience-Based / Scenario Questions](#-experience-based--scenario-questions)
8. [Behavioral / Situational Questions](#-behavioral--situational-questions)
9. [Quick Fire Round](#-quick-fire-round)

---

# 🔴 PRIORITY — CORE CONCEPTS

---

## Q1: What is IAM and why is it important?

**Answer:**  
IAM (Identity and Access Management) is the discipline of ensuring the **right people have the right access to the right resources at the right time** — and that unauthorized access is prevented, detected, and remediated.

**Why it's critical:**
- 80%+ of breaches involve compromised credentials or identity abuse (Verizon DBIR)
- Identity is the new perimeter — the traditional network perimeter has dissolved with cloud and remote work
- Every compliance framework (SOX, PCI-DSS, HIPAA, ISO 27001) mandates strong access controls

**Three core questions IAM answers:**
- **Who are you?** → Identity (Authentication)
- **What can you do?** → Access (Authorization)
- **Should you still?** → Governance (Lifecycle & Reviews)

---

## Q2: What is the difference between Authentication and Authorization?

**Answer:**

| | Authentication | Authorization |
|-|---------------|---------------|
| **Question** | "Who are you?" | "What can you do?" |
| **Process** | Verify identity | Grant/deny permissions |
| **When** | Always first | After successful authentication |
| **Example** | Username + password + MFA | RBAC role grants access to Finance DB |
| **Protocols** | Kerberos, SAML, OIDC, LDAP | ACLs, RBAC policies, OAuth scopes |
| **Failure outcome** | Login rejected | Access denied (403) |

**Key point:** Authentication always precedes authorization. You can't determine what someone can access if you don't know who they are.

---

## Q3: Explain RBAC, ABAC, MAC, and DAC.

**Answer:**

**RBAC (Role-Based Access Control):**
- Access based on job roles (Finance Analyst, HR Manager)
- User → Role → Permissions → Resources
- Most common in enterprises (AD groups are RBAC)
- Pros: Easy to manage and audit; Cons: Role explosion

**ABAC (Attribute-Based Access Control):**
- Access based on attributes of user, resource, action, environment
- Example: Allow if User.Dept=Finance AND Resource.Classification=Confidential AND Time=Business hours
- Pros: Very granular; Cons: Complex to implement

**MAC (Mandatory Access Control):**
- System-enforced; users cannot change permissions
- Based on security classifications (Top Secret > Secret > Confidential)
- Used in government/military; very rigid
- Bell-LaPadula model: no read-up, no write-down

**DAC (Discretionary Access Control):**
- Resource owner decides who can access
- Example: Windows NTFS — Alice can share her files with Bob
- Pros: Flexible; Cons: Users can over-share, no central control

---

## Q4: What is the Principle of Least Privilege?

**Answer:**  
Users, systems, and processes should have the **minimum access required to perform their function** — nothing more.

**Why it matters:**
- Limits blast radius if account is compromised
- Reduces insider threat risk
- Required by most compliance frameworks

**How it's implemented:**
- Role-based access aligned to job function (not copied from a colleague)
- Just-in-Time (JIT) access — grant elevated access only when needed, auto-revoke
- Regular access reviews — remove access no longer needed
- PAM for privileged accounts — no standing admin privileges

**Anti-pattern:** "Copy Bob's access for the new employee" — Bob may have accumulated access over 5 years that the new employee doesn't need.

---

## Q5: What is Separation of Duties (SoD) and why is it important?

**Answer:**  
SoD ensures no single person has end-to-end control over a sensitive process — requiring multiple people to complete it.

**Examples:**
- Finance: Person A creates vendor, Person B approves payment (prevents fraud)
- IT: Developer writes code, different reviewer approves, different person deploys
- IAM: Person who creates privileged accounts cannot also approve them

**Why it matters:**
- Prevents insider fraud (requires collusion — harder to pull off)
- Key audit requirement in SOX, PCI-DSS
- IAM teams must identify and remediate SoD conflicts

**SoD conflict example:** "Accounts Payable" role + "Accounts Receivable Manager" role held by same person → financial fraud risk.

---

## Q6: Explain the Identity Lifecycle / Joiner-Mover-Leaver process.

**Answer:**

**JOINER (New hire):**
- Account provisioned in AD/IdP based on HRIS trigger
- Role assigned from role catalog based on job title/department
- Groups and application access provisioned
- Hardware token issued
- Day 1 access ready before employee starts

**MOVER (Role change):**
- Old role access removed
- New role access granted
- Must not accumulate access from both roles (access sprawl)
- Documented and audited

**LEAVER (Departure):**
- Account disabled immediately on termination date (HRIS trigger)
- All sessions invalidated / tokens revoked
- Mailbox archived (litigation hold if needed)
- Physical access revoked
- Audit trail preserved

**Key risk:** Missed deprovision for Leavers creates orphan accounts — a major audit finding and security risk.

---

## Q7: What is Multi-Factor Authentication (MFA) and what are the different factors?

**Answer:**  
MFA requires two or more verification factors from different categories to authenticate.

**Factors:**
- **Knowledge (something you know):** Password, PIN
- **Possession (something you have):** Hardware token (YubiKey), authenticator app, smart card
- **Inherence (something you are):** Fingerprint, face recognition, iris scan
- **Location (where you are):** Geographic location, IP-based, network segment
- **Behavior (what you do):** Typing patterns, behavioral analytics

**MFA Strength (weakest to strongest):**
1. SMS OTP (weakest — SIM swap, phishing vulnerable)
2. Email OTP
3. Authenticator app (TOTP)
4. Push notification
5. Push with number matching
6. FIDO2/WebAuthn hardware key (strongest — phishing resistant, domain-bound)

**MFA Fatigue attack:** Attacker has password → sends 50+ push notifications → user approves out of annoyance.  
**Defense:** Number matching, limit push attempts, context in notifications.

---

## Q8: What is SSO (Single Sign-On) and how does it work?

**Answer:**  
SSO allows users to authenticate once with an Identity Provider (IdP) and gain access to multiple Service Providers (SPs) without re-authenticating.

**How it works (SAML-based):**
1. User accesses SP (e.g., Salesforce)
2. SP redirects user to IdP (e.g., Okta, Azure AD)
3. User authenticates with IdP (password + MFA)
4. IdP issues SAML Assertion (signed XML) confirming identity
5. User presents Assertion to SP
6. SP validates signature → grants access

**Benefits:**
- Single credential to manage
- Centralized access revocation (disable IdP account = cut access everywhere)
- Better user experience
- Fewer password resets (fewer passwords to forget)

---

## Q9: What is the difference between SAML and OAuth?

**Answer:**

| | SAML | OAuth |
|-|------|-------|
| **Purpose** | Authentication + Authorization (primarily auth) | Authorization (access delegation) |
| **Format** | XML | JSON |
| **Use case** | Enterprise SSO | API access, mobile apps, "Sign in with Google" |
| **Trust anchor** | XML Signature (X.509 cert) | Access tokens (JWT) |
| **Age** | Older (2002) | Newer (2012) |
| **Common IdPs** | Okta, Azure AD, ADFS | Google, Facebook, GitHub, Azure AD |
| **Typical flow** | Browser redirect with POST | Redirect + token exchange |

**Simple analogy:**
- SAML = Employee badge that lets you into multiple buildings (who you are)
- OAuth = Valet key that gives limited access (can park the car, not open the trunk)

---

## Q10: Explain OAuth 2.0 authorization code flow.

**Answer:**

```
1. User opens App X, clicks "Sign in with Google"
2. App X redirects user to Google Authorization Server with:
   - client_id, redirect_uri, scope, state, response_type=code
3. User logs in to Google + consents to permissions
4. Google redirects back to App X with authorization code
5. App X (backend) exchanges code for tokens:
   POST /token with: code, client_id, client_secret, redirect_uri
6. Google returns: access_token, refresh_token, id_token (if OIDC)
7. App X uses access_token to call Google API on user's behalf
```

**Why not give access token directly?** Authorization code flow prevents token exposure in browser URL. Code is short-lived and usable only once.

**Implicit flow (deprecated):** Token returned directly in URL fragment — insecure, avoid.

**Client Credentials flow:** Machine-to-machine (no user) — service authenticates with its own client_id + secret.

---

# 🔴 PRIORITY — PROTOCOLS

---

## Q11: How does Kerberos authentication work?

**Answer:**

```
KERBEROS FLOW:
1. Client → AS (Auth Server): "I'm Alice, I want to log in" + timestamp (encrypted with Alice's password hash)
2. AS → Client: TGT (Ticket Granting Ticket) encrypted with KRBTGT hash + Session Key
3. Client → TGS (Ticket Granting Service): "I need access to FileServer" + TGT
4. TGS → Client: TGS (service ticket) encrypted with FileServer's account hash
5. Client → FileServer: "Here's my TGS ticket"
6. FileServer decrypts with its own hash → verifies → grants access
```

**Key concepts:**
- **KDC** (Key Distribution Center) = runs on Domain Controller
- **TGT** (Ticket Granting Ticket) — "master ticket" — default 10-hour lifetime
- **TGS** (Ticket Granting Service) — "service ticket" — specific to one service
- **KRBTGT** — Special account used to sign all TGTs — compromising this = Golden Ticket

**Why passwords aren't sent over network:** Kerberos uses tickets and shared secrets (hashes), not actual passwords.

---

## Q12: What is LDAP and how is it used in IAM?

**Answer:**  
LDAP (Lightweight Directory Access Protocol) is a protocol for accessing and querying directory services (like Active Directory).

**Key uses in IAM:**
- Authenticate users against AD (bind operation)
- Query user attributes (department, email, group memberships)
- Provision groups and users
- Application directory lookups

**Ports:** 389 (LDAP, unencrypted), 636 (LDAPS, encrypted — always use this in production)

**Basic LDAP query structure:**
```
(&(objectClass=user)(sAMAccountName=alice)(memberOf=CN=Finance,OU=Groups,DC=acme,DC=com))
```

**LDAP Injection:** If user input is unsanitized, attacker can modify query:
- Normal: `(uid=alice)` 
- Injected: `(uid=*)(uid=*)` → returns all users

**Defense:** Input validation, parameterized LDAP queries.

---

## Q13: What is JWT (JSON Web Token) and how is it used?

**Answer:**  
JWT is a compact, self-contained token format for transmitting claims between parties as a JSON object, digitally signed (and optionally encrypted).

**Structure:** `Header.Payload.Signature` (base64url encoded, separated by dots)

```json
Header:  {"alg": "RS256", "typ": "JWT"}
Payload: {
  "sub": "user123",
  "name": "Alice",
  "email": "alice@acme.com",
  "roles": ["admin", "finance"],
  "exp": 1716239022,    ← expiry (Unix timestamp)
  "iat": 1716235422     ← issued at
}
Signature: RS256(base64url(header) + "." + base64url(payload), private_key)
```

**How to use:** Bearer token in Authorization header: `Authorization: Bearer <jwt>`

**Common JWT Attacks:**
- **`alg:none` attack:** Change algorithm to "none" — no signature required. Defense: Server must reject "none" alg.
- **Algorithm confusion:** RS256 → HS256 using public key as HMAC secret. Defense: Always verify algorithm server-side.
- **Claim tampering:** Modify payload (e.g., `"admin": true`). Defense: Signature verification prevents this if done correctly.

---

# 🔴 PRIORITY — ACTIVE DIRECTORY & PAM

---

## Q14: What is Active Directory and what are its key components?

**Answer:**  
Active Directory (AD) is Microsoft's on-premises directory service — the identity backbone of most enterprise Windows environments.

**Key components:**

| Component | Description |
|-----------|-------------|
| **Domain** | Administrative boundary, authentication namespace (acme.com) |
| **Domain Controller (DC)** | Server hosting AD, handles authentication |
| **Forest** | Top-level container, security boundary between multiple domains |
| **OU (Organizational Unit)** | Container for organizing objects (like folders) |
| **User object** | Represents a person or service account |
| **Group** | Collection of users/computers for permission assignment |
| **GPO (Group Policy Object)** | Centrally manage settings for users/computers |
| **KRBTGT** | Special account signing all Kerberos tickets |
| **Trust** | Relationship allowing cross-domain/forest authentication |
| **SPN (Service Principal Name)** | Identifies service instances (used in Kerberos and Kerberoasting) |

---

## Q15: What is PAM (Privileged Access Management) and why is it needed?

**Answer:**  
PAM is a subset of IAM specifically for managing, monitoring, and securing **privileged accounts** — those with elevated permissions that can cause significant damage if compromised.

**Why it's needed:**
- Privileged accounts are the highest-value targets for attackers
- A compromised Domain Admin = complete organizational compromise
- Compliance mandates privileged account controls (SOX, PCI-DSS)
- Shared privileged passwords create accountability and audit problems

**Core PAM capabilities:**
1. **Password Vaulting** — Encrypted storage; users check out passwords, never know them permanently
2. **Session Recording** — Full video+keystroke recording of privileged sessions
3. **Just-in-Time (JIT) Access** — Elevate when needed, auto-revoke after
4. **Password Rotation** — Auto-rotate after each use or on schedule
5. **Dual Control** — Two-person approval for high-risk actions
6. **Application-to-Application** — Remove hardcoded passwords from scripts/apps

**Tools:** CyberArk (industry leader), BeyondTrust, Delinea, HashiCorp Vault

---

## Q16: What is the difference between a Golden Ticket and a Silver Ticket attack?

**Answer:**

| | Golden Ticket | Silver Ticket |
|-|---------------|---------------|
| **What's forged** | Kerberos TGT (master ticket) | Kerberos TGS (service ticket) |
| **Key used** | KRBTGT hash | Target service account hash |
| **Access gained** | Domain-wide, any service | Specific service only |
| **Requires DC?** | No (after initial compromise) | No |
| **Detection** | Event 4769 anomalies, unusual TGT lifetimes | Event 4769, service account anomalies |
| **Persistence** | Even after password reset (until KRBTGT rotated twice) | Until service account password reset |

**Golden Ticket = ultimate persistence** — After obtaining KRBTGT hash, attacker can generate valid tickets for any user to any service indefinitely. Counter: Rotate KRBTGT password **twice** (double-rotation invalidates all existing tickets).

---

## Q17: What is Kerberoasting and how do you defend against it?

**Answer:**

**How it works:**
1. Attacker is authenticated user in domain (low privilege — doesn't need admin)
2. Requests Kerberos TGS for services with SPNs (Service Principal Names)
3. TGS is encrypted with the service account's NTLM hash
4. Attacker saves the TGS and cracks it offline (Hashcat, John the Ripper)
5. If service account has weak password → account compromised
6. Service accounts often have excessive privileges → privilege escalation

**Detection:**
- Monitor Event 4769 (Kerberos TGS request) for unusual volume
- Alert on TGS requests for sensitive service accounts
- Anomaly: one user requesting TGS for 10+ services rapidly

**Defense:**
- Strong, random passwords for service accounts (25+ characters — effectively uncrackable)
- Use **Managed Service Accounts (MSA)** or **Group Managed Service Accounts (gMSA)** — auto-rotating passwords
- Regularly audit which accounts have SPNs
- Least privilege for service accounts (don't give Domain Admin to a service account)

---

# 🔴 PRIORITY — CLOUD IAM

---

## Q18: How does AWS IAM work? Explain key components.

**Answer:**

**Key AWS IAM components:**

| Component | Description |
|-----------|-------------|
| **Users** | Human identities (avoid for apps — use roles) |
| **Groups** | Collection of users sharing permissions |
| **Roles** | Identities assumed by users, apps, or AWS services |
| **Policies** | JSON documents defining permissions (Allow/Deny) |
| **Managed Policies** | AWS-managed or customer-managed reusable policies |
| **Inline Policies** | Embedded directly in user/group/role |

**Policy structure:**
```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::my-bucket/*",
  "Condition": {"IpAddress": {"aws:SourceIp": "10.0.0.0/8"}}
}
```

**Evaluation logic:** Explicit Deny > Allow > Implicit Deny (default)

**IAM best practices:**
- Never use root account for daily tasks
- Enable MFA on root and privileged users
- Use roles instead of long-term access keys for apps
- Apply least privilege
- Enable CloudTrail for all API calls

---

## Q19: What is Azure AD Conditional Access?

**Answer:**  
Conditional Access is Azure AD's policy engine that makes access decisions based on signals (conditions) and then enforces controls.

**Signal types (conditions):**
- User / Group membership
- IP location (named locations, country)
- Device (compliant? managed? platform?)
- Application being accessed
- Sign-in risk (Azure AD Identity Protection risk score)
- User risk

**Controls (outcomes):**
- Block access
- Require MFA
- Require compliant device
- Require managed device
- Require terms of use acceptance
- Limit session (no persistent browser session)

**Example policy:**
```
IF: User = Any | App = Microsoft 365 | Location = Outside Corp IP
THEN: Require MFA

IF: User = Global Admins | Any condition
THEN: Require MFA + Compliant Device + Named Location
```

**Why it matters:** Conditional Access is how Zero Trust is implemented in Microsoft environments. Replaces the old "VPN = trusted" model with dynamic, risk-based access decisions.

---

## Q20: What is the difference between Azure AD roles and Azure RBAC roles?

**Answer:**

| | Azure AD Roles | Azure RBAC Roles |
|-|----------------|-----------------|
| **Scope** | Azure AD directory (identity plane) | Azure resources (subscription, RG, resource) |
| **Controls** | User management, app registrations, AD settings | VMs, storage, databases, networking |
| **Example roles** | Global Admin, User Admin, Security Admin | Owner, Contributor, Reader, Storage Blob Reader |
| **Where managed** | Azure AD portal | Azure portal / ARM |
| **Principle** | Directory-level permissions | Resource-level permissions |

**Key point:** Global Administrator in Azure AD does NOT automatically have access to Azure resources — that requires Azure RBAC. They are separate authorization systems.

---

# 🔴 PRIORITY — GOVERNANCE & COMPLIANCE

---

## Q21: What is an Access Review and how do you run one?

**Answer:**  
An access review (certification campaign) is a periodic process where resource owners or managers certify whether their team's access is still appropriate.

**Process:**
1. IAM/IGA system compiles current access report per manager
2. Manager reviews each entitlement: Still needed? Role changed?
3. Decision: **Certify** (keep) or **Revoke** (remove)
4. Revocations automatically provisioned to target systems
5. Completion report generated for audit evidence

**What's reviewed:**
- Application entitlements
- Privileged account memberships
- Dormant accounts (no login in 90+ days)
- Excessive access (more than role requires)
- SoD conflicts

**Frequency:** SOX mandates quarterly for financial systems; best practice is quarterly for privileged access, semi-annual for standard access.

**Tools:** SailPoint, Saviynt, Omada automate campaign management.

---

## Q22: How does IAM relate to compliance frameworks like SOX and PCI-DSS?

**Answer:**

**SOX (Sarbanes-Oxley — Financial):**
- Requires access controls on financial systems
- Quarterly access reviews with documented evidence
- Mandatory SoD for financial processes
- Audit trail for all privileged access
- IAM teams must provide evidence: who has access, who approved it, who reviewed it

**PCI-DSS (Payment Card Industry):**
- Unique user IDs (no shared accounts)
- MFA for all administrative access
- Least privilege access
- Regular access reviews
- PAM for admin accounts to cardholder data environment
- Disable inactive accounts after 90 days
- Two-factor authentication for remote access

**HIPAA (Healthcare):**
- Unique user identification
- Automatic logoff
- Encryption of PHI (protected health information)
- Audit controls on who accessed patient data
- Access authorization and modification tracking

**Key IAM deliverable for auditors:** Evidence of: (1) who has access, (2) who approved it, (3) when it was last reviewed, (4) SoD conflicts managed.

---

# 🟡 JOB-SWITCHING QUESTIONS

---

## Q23: You're switching from a sysadmin role — how does your experience apply to IAM?

**Sample Answer Framework:**

*"My sysadmin background is directly applicable. I've managed Active Directory day-to-day — creating users, managing groups, troubleshooting Kerberos authentication issues, and maintaining service accounts. I understand the operational reality of IAM from the consuming side. Now I want to focus on the governance and security architecture side — ensuring access is correct, not just functional. I've been upskilling specifically for IAM through [SC-300 certification / SailPoint University / GOAD lab] and have hands-on experience with [specific tools/protocols]."*

---

## Q24: You're switching from development — what unique perspective do you bring to IAM?

**Sample Answer Framework:**

*"As a developer, I understand OAuth and OIDC from the implementation side — I've integrated these protocols into applications. That means when an IAM team implements SSO for an app, I understand both the IdP configuration AND the app's implementation requirements, which helps bridge the gap that often causes integration problems. I also understand API authentication, JWT handling, and common developer mistakes (like ignoring algorithm validation on JWTs or storing tokens insecurely). Additionally, my scripting ability helps me automate IAM workflows and integrate with REST APIs that most IAM tools expose."*

---

## Q25: IAM is sometimes seen as just "user account management" — how would you counter that perception?

**Answer:**

*"That perception reflects IAM as it was done 10 years ago. Modern IAM is one of the most critical security domains because identity is now the primary attack vector — 80%+ of breaches involve compromised identities. Today's IAM encompasses: protocol design (SAML, OAuth, Kerberos), cloud architecture (Azure AD Conditional Access, AWS IAM policies), PAM (protecting the keys to the kingdom — privileged accounts), governance (access reviews, SoD for compliance), and increasingly identity threat detection. The SolarWinds attackers bypassed network controls entirely by forging SAML tokens. That's an IAM problem, not a firewall problem. Identity is the new perimeter."*

---

## Q26: How would you approach your first 90 days as an IAM Engineer at a new company?

**Answer:**

*"My priority would be discovery before change:*

*Month 1: Understand the landscape*
*- Map all identity sources (AD forests, cloud directories, external IdPs)*
*- Catalog applications and their auth methods (SAML, LDAP, local auth)*
*- Review existing roles and access policies*
*- Understand the IAM tools in use and their maturity*
*- Meet with key stakeholders: HR (HRIS integration), Legal (compliance requirements), IT (helpdesk for access requests)*

*Month 2: Identify gaps*
*- Orphan accounts, dormant accounts, SoD conflicts*
*- Access review status — when was the last one done?*
*- Privileged account inventory — are all admins using PAM?*
*- MFA coverage — any privileged accounts without MFA?*

*Month 3: Quick wins + roadmap*
*- Fix immediate critical gaps (e.g., privileged accounts without MFA)*
*- Establish or improve access review process*
*- Build the IAM improvement roadmap with stakeholder buy-in*"*

---

# 🟢 EXPERIENCE-BASED / SCENARIO QUESTIONS

---

## Q27: Walk me through how you'd investigate a report that an ex-employee's account is still active.

**Detailed Answer:**

```
STEP 1 — VERIFY
- Check termination date in HRIS vs account status in AD
- Confirm account is truly active (last logon, password expiry date)
- Check if account has had any activity since termination date

STEP 2 — ASSESS RISK
- Has the account been used since termination? (AD logs: Event 4624)
- If YES: Escalate to SOC immediately — potential unauthorized access
- What access did this account have? (AD groups, application entitlements)
- Was it a privileged account?

STEP 3 — IMMEDIATE ACTION
- Disable the account IMMEDIATELY
- Revoke all SSO sessions / MFA tokens
- Force sign-out from all cloud applications (Azure AD revoke sessions)
- Notify SOC and management

STEP 4 — INVESTIGATE
- If activity post-termination was detected: treat as security incident
- Preserve logs for forensics / legal
- Determine what data/systems were accessed post-termination

STEP 5 — ROOT CAUSE
- Why wasn't the account disabled on termination?
- Was the HRIS-to-IAM integration working? Manual process that was missed?
- Check for other similar cases (scan for other orphan accounts)

STEP 6 — REMEDIATION
- Fix the process gap (automate deprovisioning if manual)
- Run full orphan account audit
- Document as process improvement
```

---

## Q28: A user reports they can access files they shouldn't be able to. How do you handle it?

**Answer:**

*"First I'd verify the claim — have them show me specifically what they can access and what they shouldn't be able to access. Then I'd investigate the access path:*

*- Check their direct group memberships in AD*
*- Check for nested groups (user might be in Group A, which is in Group B that has access)*
*- Check for any direct permission grants (DAC — explicit permissions on the file share)*
*- Review change history: was this access recently added? By whom?*

*Likely scenarios:*
*1. User was added to wrong group during provisioning (human error)*
*2. A group's scope was changed, inadvertently granting wider access*
*3. They were a Mover and old access wasn't removed*

*Resolution: Remove the inappropriate access, document why it happened, update provisioning checklist if it was a process gap. If access was intentionally granted without authorization — escalate.*"

---

## Q29: You're tasked with improving an organization's IAM posture. Where do you start?

**Answer:**

*"I'd prioritize by risk, starting with what kills you fastest:*

*Priority 1 — Privileged Access:*
*- Are all Domain Admin accounts protected by MFA? (No MFA on admins = immediate P1 fix)*
*- Are privileged passwords vaulted in PAM? (No PAM = shared passwords, no audit trail)*
*- Any standing admin access that could be converted to JIT?*

*Priority 2 — Lifecycle:*
*- Orphan account audit — how many terminated employee accounts are still active?*
*- Dormant account audit — accounts with 90+ days no login*
*- Service account inventory — how many, who owns them, when were passwords last changed?*

*Priority 3 — MFA Coverage:*
*- What % of users have MFA enrolled?*
*- Remote access (VPN) — does it require MFA?*

*Priority 4 — Governance:*
*- When was the last access review? Are they automated or manual?*
*- SoD conflicts — are there any known high-risk conflicts that aren't managed?*

*I'd document findings, score by risk, and present a prioritized roadmap with business case — not a wish list."*

---

## Q30: How would you explain a SoD conflict to a business executive who's not technical?

**Answer:**

*"I'd use an analogy they'd immediately understand: 'Imagine one person at our bank who can both create new vendor accounts AND approve wire transfers to those vendors. That single person could create a fictitious vendor account they control and then approve payments to it. That's exactly what we have — one of our Finance users can both set up vendors in the payment system AND approve their invoices. This is the combination of access that led to [famous fraud case or internal example]. We need to separate these so two different people are involved — preventing any single employee from committing this fraud without a second person's involvement.' That usually gets executive attention — especially when you cite a dollar amount of recent fraud cases."*

---

# 🔵 BEHAVIORAL / SITUATIONAL QUESTIONS

---

## Q31: Tell me about a time you had to explain a security decision that impacted user productivity.

**Framework (STAR):**

*"SITUATION: We needed to implement MFA for all remote access — which was previously password-only via VPN.*

*TASK: Implement MFA without causing major business disruption or user resistance.*

*ACTION: Before rollout, I worked with department heads to understand their workflows, created guides and videos for each user type, ran a pilot with tech-savvy users first, set up a dedicated help channel for the rollout week, and communicated clearly WHY — 'The Colonial Pipeline breach caused a week of fuel shortages and cost \$4.4M because one VPN account didn't have MFA.'*

*RESULT: Rollout completed with 95% enrollment in the first week, help desk tickets were manageable (mostly questions, not complaints), and within 2 weeks it was routine."*

---

## Q32: How do you balance security requirements with business demands for fast access?

**Answer:**

*"This tension is real and valid — the business needs to move fast, security needs to ensure access is appropriate. My approach:*

*1. Build a catalog of pre-approved standard access: Business team can self-serve and get auto-approved access that's been pre-assessed as low-risk for their role. No waiting.*

*2. Clear SLAs for access requests: Emergency access requests handled in 2 hours, standard within 1 business day. Predictability reduces frustration more than raw speed.*

*3. JIT access for one-off needs: Instead of a permanent role assignment for a one-week project, provide temporary access that auto-expires. Business gets what they need, security gets automatic cleanup.*

*4. Transparent denials: When I deny access, I explain why and offer an alternative. 'You can't have admin access to the prod DB, but here's a read-only view that gets you what you actually need.' Often they didn't need the full access they asked for.*"

---

## Q33: How do you stay current in IAM — it evolves rapidly.

**Answer:**

*"IAM changes fast — especially cloud IAM. My approach:*

*- Follow Microsoft Entra and Okta release notes monthly — both release significant feature updates regularly*
*- Subscribe to SpecterOps blog and Adam Chester's research for AD attack path evolution — I want to know about new attack techniques before attackers use them against my environment*
*- Attend Identiverse talks via YouTube (conference recordings are free)*
*- Follow the r/IAM subreddit — practitioners share real-world challenges*
*- 2-3 hours weekly on hands-on practice in my lab or on GOAD to keep skills sharp*
*- When a major breach involving identity occurs (like Okta 2022, SolarWinds), I do a deep-dive analysis to understand what IAM controls failed and how to apply those lessons.*"

---

# ⚡ QUICK FIRE ROUND

| Question | Answer |
|----------|--------|
| What port does LDAP use? | 389 (LDAP), 636 (LDAPS) |
| What port does Kerberos use? | 88 |
| What is a TGT? | Ticket Granting Ticket — master Kerberos ticket |
| What is a TGS? | Ticket Granting Service ticket — service-specific ticket |
| What is KRBTGT? | Special account that signs all Kerberos tickets |
| What is Golden Ticket? | Forged TGT using KRBTGT hash — domain-wide persistence |
| What is Silver Ticket? | Forged service ticket using service account hash |
| What is Kerberoasting? | Request TGS for SPN, crack service account hash offline |
| What is AS-REP Roasting? | Request AS-REP for accounts with pre-auth disabled, crack offline |
| What is Pass-the-Hash? | Use NTLM hash directly to authenticate without knowing password |
| What is a service account? | Account used by apps/services (not humans) |
| What is gMSA? | Group Managed Service Account — auto-rotating password |
| What is a SPN? | Service Principal Name — identifies a service instance in Kerberos |
| What is JIT access? | Just-In-Time — grant elevated access on demand, auto-revoke |
| What is PAM? | Privileged Access Management |
| What is an orphan account? | Account with no associated active user |
| What is access sprawl? | Accumulation of excessive access over time |
| What is SoD? | Separation of Duties |
| What is SCIM? | System for Cross-domain Identity Management — provisioning standard |
| What is FIDO2? | Web Authentication standard — phishing-resistant MFA |
| What does IdP stand for? | Identity Provider |
| What does SP stand for? | Service Provider |
| What is a SAML Assertion? | Signed XML statement of identity from IdP to SP |
| What is an access token? | OAuth token granting access to a resource |
| What is an ID token? | OIDC token containing identity claims (who you are) |
| What is a refresh token? | Token used to get new access tokens without re-auth |
| What is PBAC? | Policy-Based Access Control |
| What is ABAC? | Attribute-Based Access Control |
| What is DCSync? | AD replication technique used to dump all password hashes |
| What is BloodHound? | Tool that graphs AD relationships to find attack paths |

---

> **💡 Interview Tips for IAM:**
> 1. Always connect access decisions back to **business risk** — interviewers love candidates who understand IAM is about risk management, not just technology
> 2. Know your protocols cold — SAML, OAuth, and Kerberos questions differentiate candidates strongly
> 3. Mention compliance when relevant — SOX, PCI-DSS familiarity shows corporate readiness
> 4. "Least privilege" and "access reviews" should come up naturally in your answers — they're IAM mantras
> 5. If you know BloodHound, mention it — shows you understand the attacker's perspective on identity

