# 🏗️ SYSTEM DESIGN SECURITY - Complete Guide

## Table of Contents
1. [Security by Design](#security-by-design)
2. [Secure Architecture Principles](#secure-architecture-principles)
3. [Authentication & Authorization](#authentication--authorization)
4. [API Security](#api-security)
5. [Cloud Security](#cloud-security)
6. [DevSecOps](#devsecops)
7. [Incident Response](#incident-response)
8. [Compliance & Frameworks](#compliance--frameworks)
9. [Interview Questions](#interview-questions)
10. [Learning Resources](#learning-resources)

---

## Security by Design

### What is Security by Design?

**Security by Design** means integrating security throughout the entire software development lifecycle, not as an afterthought.

### Principles

```
┌─────────────────────────────────────────────────────────────┐
│           SECURITY BY DESIGN PRINCIPLES                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. MINIMIZE ATTACK SURFACE                                  │
│     └── Reduce exposed functionality, ports, and services  │
│                                                             │
│  2. ESTABLISH SECURE DEFAULTS                                │
│     └── Out-of-box security, opt-in for risky features     │
│                                                             │
│  3. LEAST PRIVILEGE                                          │
│     └── Only grant permissions absolutely necessary        │
│                                                             │
│  4. DEFENSE IN DEPTH                                         │
│     └── Multiple layers of security controls               │
│                                                             │
│  5. FAIL SECURELY                                            │
│     └── When errors occur, fail closed (deny access)       │
│                                                             │
│  6. DON'T TRUST SERVICES                                     │
│     └── Validate third-party services and data             │
│                                                             │
│  7. SEPARATION OF DUTIES                                     │
│     └── No single person has full control                  │
│                                                             │
│  8. AVOID SECURITY BY OBSCURITY                              │
│     └── Security shouldn't depend on secrecy of design     │
│                                                             │
│  9. KEEP SECURITY SIMPLE                                     │
│     └── Complex systems have more vulnerabilities          │
│                                                             │
│  10. FIX SECURITY ISSUES CORRECTLY                           │
│      └── Address root cause, not symptoms                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Security in SDLC

```
┌─────────────────────────────────────────────────────────────┐
│         SECURE SDLC (Software Development Lifecycle)         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PLANNING                                                   │
│  ├── Security requirements                                 │
│  ├── Risk assessment                                       │
│  └── Compliance requirements                               │
│       │                                                    │
│       ▼                                                    │
│  DESIGN                                                     │
│  ├── Threat modeling (STRIDE)                              │
│  ├── Security architecture                                 │
│  └── Attack surface analysis                               │
│       │                                                    │
│       ▼                                                    │
│  DEVELOPMENT                                                │
│  ├── Secure coding practices                               │
│  ├── Code review                                           │
│  └── SAST (Static Application Security Testing)            │
│       │                                                    │
│       ▼                                                    │
│  TESTING                                                    │
│  ├── DAST (Dynamic Application Security Testing)           │
│  ├── Penetration testing                                   │
│  └── Security regression testing                           │
│       │                                                    │
│       ▼                                                    │
│  DEPLOYMENT                                                 │
│  ├── Secure configuration                                  │
│  ├── Secrets management                                    │
│  └── Infrastructure security                               │
│       │                                                    │
│       ▼                                                    │
│  OPERATIONS                                                 │
│  ├── Monitoring and logging                                │
│  ├── Incident response                                     │
│  └── Vulnerability management                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Secure Architecture Principles

### Zero Trust Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 ZERO TRUST MODEL                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CORE PRINCIPLE: "Never trust, always verify"               │
│                                                             │
│  Traditional Model:                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │             TRUSTED INTERNAL NETWORK               │   │
│  │  Once inside firewall = trusted                     │   │
│  │  ❌ Problem: Insider threats, lateral movement      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Zero Trust Model:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Every request verified regardless of location       │   │
│  │  • Verify identity                                  │   │
│  │  • Verify device security posture                   │   │
│  │  • Verify context (time, location)                  │   │
│  │  • Least privilege access                           │   │
│  │  • Micro-segmentation                               │   │
│  │  • Continuous monitoring                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  KEY COMPONENTS:                                            │
│  ├── Identity verification (MFA)                           │
│  ├── Device trust (MDM, EDR)                               │
│  ├── Network segmentation                                  │
│  ├── Least privilege access                                │
│  └── Continuous monitoring and analytics                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Defense in Depth

```
┌─────────────────────────────────────────────────────────────┐
│              DEFENSE IN DEPTH ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                      INTERNET                          │ │
│  └───────────────────────────┬───────────────────────────┘ │
│                              ▼                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ PERIMETER: WAF, DDoS Protection, Edge Firewall        │ │
│  └───────────────────────────┬───────────────────────────┘ │
│                              ▼                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ NETWORK: Segmentation, IDS/IPS, VPN                   │ │
│  └───────────────────────────┬───────────────────────────┘ │
│                              ▼                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ HOST: Hardening, Antivirus/EDR, Patching              │ │
│  └───────────────────────────┬───────────────────────────┘ │
│                              ▼                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ APPLICATION: Input validation, Authentication, HTTPS  │ │
│  └───────────────────────────┬───────────────────────────┘ │
│                              ▼                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ DATA: Encryption, Access Control, DLP, Backup         │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  If one layer fails, others still protect!                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Network Segmentation

```
┌─────────────────────────────────────────────────────────────┐
│              NETWORK SEGMENTATION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                        INTERNET                             │
│                            │                                │
│                     ┌──────▼──────┐                        │
│                     │   Firewall   │                        │
│                     └──────┬──────┘                        │
│           ┌────────────────┼────────────────┐              │
│           │                │                │              │
│           ▼                ▼                ▼              │
│  ┌────────────────┐ ┌────────────┐ ┌────────────────┐     │
│  │      DMZ       │ │  Internal  │ │   Sensitive    │     │
│  │                │ │  Network   │ │   Data Zone    │     │
│  │ • Web servers  │ │ • Users    │ │ • Database     │     │
│  │ • Mail servers │ │ • Apps     │ │ • PII data     │     │
│  │ • Public APIs  │ │            │ │ • Secrets mgmt │     │
│  └────────────────┘ └────────────┘ └────────────────┘     │
│         ↑                ↑                ↑               │
│         └────────────────┼────────────────┘               │
│                          │                                 │
│              Traffic controlled between zones              │
│                                                             │
│  BENEFITS:                                                  │
│  • Limits lateral movement                                 │
│  • Contains breaches                                       │
│  • Better monitoring per segment                           │
│  • Compliance requirements                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Authentication & Authorization

### Authentication Methods

```
┌─────────────────────────────────────────────────────────────┐
│              AUTHENTICATION METHODS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FACTORS:                                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ KNOWLEDGE │ Something you KNOW    │ Password, PIN    │  │
│  │ POSSESSION│ Something you HAVE    │ Phone, Token     │  │
│  │ INHERENCE │ Something you ARE     │ Fingerprint, Face│  │
│  │ LOCATION  │ Where you ARE         │ GPS, IP          │  │
│  │ BEHAVIOR  │ How you ACT           │ Typing pattern   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  MFA (Multi-Factor Authentication):                         │
│  Combines 2+ factors from different categories             │
│  Example: Password (knowledge) + TOTP app (possession)     │
│                                                             │
│  MODERN APPROACHES:                                         │
│  • Passwordless: FIDO2/WebAuthn, biometrics               │
│  • SSO (Single Sign-On): One login for multiple apps      │
│  • OAuth 2.0 / OIDC: Delegated authorization              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### OAuth 2.0 Flow

```
┌─────────────────────────────────────────────────────────────┐
│              OAUTH 2.0 AUTHORIZATION CODE FLOW               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  USER            CLIENT APP         AUTH SERVER    RESOURCE │
│    │                 │                  │           SERVER  │
│    │ 1. Click "Login with Google"      │              │    │
│    │─────────────────►│                 │              │    │
│    │                 │                  │              │    │
│    │                 │ 2. Redirect to   │              │    │
│    │◄────────────────│    auth server   │              │    │
│    │                 │                  │              │    │
│    │ 3. User authenticates             │              │    │
│    │────────────────────────────────────►              │    │
│    │                 │                  │              │    │
│    │ 4. Auth code returned             │              │    │
│    │◄────────────────────────────────────              │    │
│    │─────────────────►│                 │              │    │
│    │                 │ 5. Exchange code │              │    │
│    │                 │    for token     │              │    │
│    │                 │─────────────────►│              │    │
│    │                 │                  │              │    │
│    │                 │ 6. Access token  │              │    │
│    │                 │◄─────────────────│              │    │
│    │                 │                  │              │    │
│    │                 │ 7. Request resource with token │    │
│    │                 │─────────────────────────────────►    │
│    │                 │                  │              │    │
│    │                 │ 8. Protected resource          │    │
│    │                 │◄─────────────────────────────────    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Authorization Models

```
┌─────────────────────────────────────────────────────────────┐
│              AUTHORIZATION MODELS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  RBAC (Role-Based Access Control):                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ User ──► Role ──► Permissions                        │  │
│  │                                                       │  │
│  │ Example:                                              │  │
│  │ User: Alice      Role: Admin      Perm: Read, Write,│  │
│  │ User: Bob        Role: Viewer     Perm: Read        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ABAC (Attribute-Based Access Control):                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Access based on attributes (user, resource, context) │  │
│  │                                                       │  │
│  │ Example Policy:                                       │  │
│  │ IF user.department == "HR"                           │  │
│  │ AND resource.type == "employee_record"               │  │
│  │ AND time.hours BETWEEN 9 AND 17                     │  │
│  │ THEN ALLOW READ                                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  PBAC (Policy-Based Access Control):                        │
│  Fine-grained policies, often used with OPA (Open Policy   │
│  Agent) or AWS IAM                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### JWT (JSON Web Tokens)

```
┌─────────────────────────────────────────────────────────────┐
│                      JWT STRUCTURE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  xxxxx.yyyyy.zzzzz                                          │
│    │      │      │                                          │
│    │      │      └── SIGNATURE                              │
│    │      └───────── PAYLOAD                                │
│    └──────────────── HEADER                                 │
│                                                             │
│  HEADER:                                                    │
│  {                                                          │
│    "alg": "HS256",                                         │
│    "typ": "JWT"                                            │
│  }                                                          │
│                                                             │
│  PAYLOAD:                                                   │
│  {                                                          │
│    "sub": "1234567890",                                    │
│    "name": "John Doe",                                     │
│    "role": "admin",                                        │
│    "iat": 1516239022,                                      │
│    "exp": 1516242622                                       │
│  }                                                          │
│                                                             │
│  SIGNATURE:                                                 │
│  HMACSHA256(                                                │
│    base64UrlEncode(header) + "." +                         │
│    base64UrlEncode(payload),                               │
│    secret                                                  │
│  )                                                          │
│                                                             │
│  SECURITY CONSIDERATIONS:                                   │
│  • Always verify signature                                 │
│  • Use strong secret/key                                   │
│  • Set short expiration times                              │
│  • Never store sensitive data in payload (it's just B64)  │
│  • Use HTTPS only                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## API Security

### API Security Checklist

```
┌─────────────────────────────────────────────────────────────┐
│              API SECURITY BEST PRACTICES                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AUTHENTICATION & AUTHORIZATION:                            │
│  ✓ Use OAuth 2.0 / API Keys / JWT                          │
│  ✓ Validate tokens on every request                        │
│  ✓ Implement proper scopes/permissions                     │
│  ✓ Use short-lived access tokens                           │
│                                                             │
│  INPUT VALIDATION:                                          │
│  ✓ Validate all input parameters                          │
│  ✓ Use schema validation (JSON Schema, OpenAPI)           │
│  ✓ Sanitize input to prevent injection                    │
│  ✓ Limit request size                                      │
│                                                             │
│  RATE LIMITING:                                             │
│  ✓ Implement rate limiting per user/IP                     │
│  ✓ Return 429 Too Many Requests                           │
│  ✓ Use exponential backoff                                │
│                                                             │
│  TRANSPORT SECURITY:                                        │
│  ✓ Always use HTTPS (TLS 1.2+)                             │
│  ✓ Implement HSTS                                          │
│  ✓ Validate certificates                                   │
│                                                             │
│  ERROR HANDLING:                                            │
│  ✓ Don't leak sensitive info in errors                    │
│  ✓ Use standard HTTP status codes                         │
│  ✓ Log errors securely                                    │
│                                                             │
│  LOGGING & MONITORING:                                      │
│  ✓ Log all API access                                      │
│  ✓ Monitor for anomalies                                  │
│  ✓ Set up alerting                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### OWASP API Top 10 (2023)

```
┌─────────────────────────────────────────────────────────────┐
│              OWASP API TOP 10 (2023)                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  API1  Broken Object Level Authorization                    │
│        └── IDOR: Accessing other users' objects            │
│                                                             │
│  API2  Broken Authentication                                │
│        └── Weak token generation, missing MFA              │
│                                                             │
│  API3  Broken Object Property Level Authorization           │
│        └── Mass assignment, excessive data exposure        │
│                                                             │
│  API4  Unrestricted Resource Consumption                    │
│        └── No rate limiting, DoS potential                 │
│                                                             │
│  API5  Broken Function Level Authorization                  │
│        └── Accessing admin endpoints as regular user       │
│                                                             │
│  API6  Unrestricted Access to Sensitive Business Flows     │
│        └── Automated abuse of business logic               │
│                                                             │
│  API7  Server Side Request Forgery (SSRF)                   │
│        └── API fetches attacker-controlled URLs            │
│                                                             │
│  API8  Security Misconfiguration                            │
│        └── Default configs, missing security headers       │
│                                                             │
│  API9  Improper Inventory Management                        │
│        └── Undocumented/shadow APIs, old versions          │
│                                                             │
│  API10 Unsafe Consumption of APIs                           │
│        └── Not validating third-party API responses        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Cloud Security

### Shared Responsibility Model

```
┌─────────────────────────────────────────────────────────────┐
│          CLOUD SHARED RESPONSIBILITY MODEL                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    IaaS      PaaS      SaaS                │
│  ┌────────────────┬────────┬────────┬────────┐            │
│  │ Data           │ YOU    │ YOU    │ YOU    │            │
│  │ Identity/Access│ YOU    │ Shared │ Shared │            │
│  │ Applications   │ YOU    │ YOU    │ Provider│            │
│  │ Guest OS       │ YOU    │ Provider│ Provider│            │
│  │ Virtual Network│ Shared │ Provider│ Provider│            │
│  │ Infrastructure │ Provider│ Provider│ Provider│            │
│  │ Physical       │ Provider│ Provider│ Provider│            │
│  └────────────────┴────────┴────────┴────────┘            │
│                                                             │
│  YOUR RESPONSIBILITIES (always):                            │
│  • Data classification and security                        │
│  • Identity and access management                          │
│  • Compliance requirements                                 │
│  • Endpoint/client security                                │
│                                                             │
│  PROVIDER RESPONSIBILITIES:                                 │
│  • Physical data center security                           │
│  • Network infrastructure                                  │
│  • Hypervisor security (for IaaS)                         │
│  • Platform security (for PaaS/SaaS)                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Cloud Security Best Practices

```
┌─────────────────────────────────────────────────────────────┐
│           CLOUD SECURITY BEST PRACTICES                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IDENTITY & ACCESS:                                         │
│  ✓ Use IAM with least privilege                            │
│  ✓ Enable MFA for all users                                │
│  ✓ Avoid root/admin account for daily use                  │
│  ✓ Regular access reviews                                  │
│  ✓ Use service accounts for applications                   │
│                                                             │
│  DATA PROTECTION:                                           │
│  ✓ Encrypt data at rest and in transit                     │
│  ✓ Use key management services (KMS)                       │
│  ✓ Enable versioning and backups                          │
│  ✓ Implement DLP (Data Loss Prevention)                    │
│                                                             │
│  NETWORK:                                                   │
│  ✓ Use VPC/VNet with proper segmentation                  │
│  ✓ Configure security groups/NSGs                         │
│  ✓ Enable VPC flow logs                                   │
│  ✓ Use private endpoints where possible                   │
│                                                             │
│  MONITORING:                                                │
│  ✓ Enable cloud-native logging (CloudTrail, etc.)         │
│  ✓ Set up alerts for security events                      │
│  ✓ Use CSPM (Cloud Security Posture Management)           │
│  ✓ Regular security assessments                           │
│                                                             │
│  INFRASTRUCTURE AS CODE:                                    │
│  ✓ Define infrastructure in code (Terraform, etc.)        │
│  ✓ Scan IaC for misconfigurations                         │
│  ✓ Use version control                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### AWS Security Services

| Service | Purpose |
|---------|---------|
| **IAM** | Identity & Access Management |
| **GuardDuty** | Threat detection |
| **Security Hub** | Security posture view |
| **CloudTrail** | API logging |
| **KMS** | Key management |
| **WAF** | Web Application Firewall |
| **Shield** | DDoS protection |
| **Secrets Manager** | Secrets storage |
| **Config** | Configuration compliance |

---

## DevSecOps

### DevSecOps Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                 DEVSECOPS PIPELINE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CODE ─────► BUILD ─────► TEST ─────► DEPLOY ─────► MONITOR│
│    │          │           │            │             │     │
│    ▼          ▼           ▼            ▼             ▼     │
│  ┌────────┐┌────────┐┌─────────┐┌───────────┐┌──────────┐ │
│  │Pre-    ││SCA     ││DAST     ││Container  ││Runtime   │ │
│  │commit  ││(Deps)  ││         ││Scanning   ││Protection│ │
│  │hooks   ││        ││         ││           ││          │ │
│  ├────────┤├────────┤├─────────┤├───────────┤├──────────┤ │
│  │SAST    ││Container│Unit     ││IaC        ││SIEM      │ │
│  │        ││Build   ││Security ││Security   ││          │ │
│  │        ││Scan    ││Tests    ││           ││          │ │
│  ├────────┤├────────┤├─────────┤├───────────┤├──────────┤ │
│  │Secrets ││License ││Pen Test ││Secrets    ││Logging   │ │
│  │Scanning││Check   ││         ││Injection  ││          │ │
│  └────────┘└────────┘└─────────┘└───────────┘└──────────┘ │
│                                                             │
│  SHIFT LEFT: Catch security issues early in the cycle      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Security Testing Types

```
┌─────────────────────────────────────────────────────────────┐
│              SECURITY TESTING TYPES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SAST (Static Application Security Testing)                 │
│  ├── Analyzes source code without execution                │
│  ├── Early in pipeline (shift left)                        │
│  ├── Finds: SQL injection, XSS, buffer overflows          │
│  └── Tools: SonarQube, Checkmarx, Semgrep                 │
│                                                             │
│  DAST (Dynamic Application Security Testing)                │
│  ├── Tests running application                             │
│  ├── Later in pipeline (staging)                           │
│  ├── Finds: Runtime vulnerabilities, configs              │
│  └── Tools: OWASP ZAP, Burp Suite, Acunetix               │
│                                                             │
│  SCA (Software Composition Analysis)                        │
│  ├── Scans dependencies/third-party code                  │
│  ├── Identifies vulnerable libraries                       │
│  ├── License compliance                                    │
│  └── Tools: Snyk, Dependabot, OWASP Dependency-Check      │
│                                                             │
│  IAST (Interactive Application Security Testing)            │
│  ├── Combines SAST and DAST                                │
│  ├── Instruments application during testing               │
│  └── Tools: Contrast Security, Synopsys Seeker            │
│                                                             │
│  Container Scanning                                         │
│  ├── Scans container images for vulnerabilities           │
│  └── Tools: Trivy, Clair, Anchore                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Secrets Management

```
┌─────────────────────────────────────────────────────────────┐
│              SECRETS MANAGEMENT                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ❌ DON'T:                                                  │
│  • Hardcode secrets in code                                │
│  • Store secrets in version control                        │
│  • Use environment variables for production                │
│  • Share secrets via email/chat                            │
│                                                             │
│  ✅ DO:                                                     │
│  • Use dedicated secrets managers                          │
│  • Rotate secrets regularly                                │
│  • Encrypt secrets at rest and in transit                  │
│  • Audit access to secrets                                 │
│  • Use short-lived credentials                             │
│                                                             │
│  TOOLS:                                                     │
│  ├── HashiCorp Vault                                       │
│  ├── AWS Secrets Manager                                   │
│  ├── Azure Key Vault                                       │
│  ├── Google Secret Manager                                 │
│  └── CyberArk, 1Password Teams                            │
│                                                             │
│  PRE-COMMIT SECRET SCANNING:                                │
│  • GitLeaks                                                │
│  • TruffleHog                                              │
│  • GitHub Secret Scanning                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Incident Response

### Incident Response Process

```
┌─────────────────────────────────────────────────────────────┐
│           INCIDENT RESPONSE LIFECYCLE (NIST)                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PREPARATION                                              │
│     ├── IR team and roles                                  │
│     ├── IR plan and playbooks                              │
│     ├── Communication plan                                 │
│     ├── Tools and resources                                │
│     └── Training and exercises                             │
│         │                                                  │
│  2. DETECTION & ANALYSIS   ◄────────────────────┐          │
│     ├── Identify indicators                      │          │
│     ├── Analyze and scope                        │          │
│     ├── Prioritize (severity)                    │          │
│     └── Document everything                      │          │
│         │                                        │          │
│  3. CONTAINMENT, ERADICATION, RECOVERY           │          │
│     ├── Short-term containment                   │          │
│     │   (isolate affected systems)               │          │
│     ├── Long-term containment                    │          │
│     │   (temp fixes while investigating)         │          │
│     ├── Eradication                              │          │
│     │   (remove threat, patch)                   │          │
│     └── Recovery                                 │          │
│         (restore systems)                        │          │
│         │                                        │          │
│  4. POST-INCIDENT                                │          │
│     ├── Lessons learned                          │          │
│     ├── Update IR plan                           │          │
│     ├── Improve detection         ───────────────┘          │
│     └── Report to stakeholders                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Incident Severity Levels

| Level | Severity | Example | Response Time |
|-------|----------|---------|---------------|
| **P1** | Critical | Active breach, data exfil | Immediate |
| **P2** | High | Malware infection, DDoS | < 4 hours |
| **P3** | Medium | Phishing success, suspicious activity | < 24 hours |
| **P4** | Low | Minor policy violation | Next business day |

---

## Compliance & Frameworks

### Security Frameworks

```
┌─────────────────────────────────────────────────────────────┐
│              SECURITY FRAMEWORKS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NIST CYBERSECURITY FRAMEWORK:                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ IDENTIFY │ PROTECT │ DETECT │ RESPOND │ RECOVER     │  │
│  │ Assets,  │Controls,│Monitor,│Incident │Business     │  │
│  │ Risks    │Training │ Alerts │ Response│ Continuity  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ISO 27001:                                                 │
│  • International security management standard              │
│  • Certifiable                                             │
│  • Risk-based approach                                     │
│                                                             │
│  SOC 2:                                                     │
│  • Trust Services Criteria                                 │
│  • Type I (point in time) / Type II (period)              │
│  • For service providers                                   │
│                                                             │
│  CIS CONTROLS:                                              │
│  • Prioritized set of actions                              │
│  • Implementation groups (IG1, IG2, IG3)                  │
│  • Highly practical                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Compliance Regulations

| Regulation | Scope | Focus |
|------------|-------|-------|
| **GDPR** | EU data subjects | Privacy, data protection |
| **PCI-DSS** | Payment card data | Cardholder data security |
| **HIPAA** | US healthcare | Patient health information |
| **SOX** | US public companies | Financial data integrity |
| **CCPA** | California residents | Consumer privacy |

---

## Interview Questions

### Basic Questions

**Q1: Explain Zero Trust architecture.**
> "Zero Trust follows 'never trust, always verify' - no implicit trust based on network location. Every request is authenticated and authorized regardless of origin. Key components include: strong identity verification with MFA, device security validation, least privilege access, micro-segmentation, and continuous monitoring. This contrasts with traditional perimeter security where internal network was trusted."

**Q2: What is the SDLC and how do you integrate security?**
> "The SDLC (Software Development Lifecycle) includes Planning, Design, Development, Testing, Deployment, and Operations. Security integrates at each phase: security requirements in Planning, threat modeling in Design, secure coding and SAST in Development, DAST and penetration testing in Testing, secure configuration in Deployment, and continuous monitoring in Operations. This is called 'shifting left' - catching issues early."

**Q3: Explain the shared responsibility model in cloud security.**
> "The shared responsibility model defines security responsibilities between cloud provider and customer. Provider handles physical security, infrastructure, and depending on service type (IaaS/PaaS/SaaS), varying levels of platform security. Customer is always responsible for data, identity management, and client-side security. In IaaS, customer handles OS and applications; in SaaS, mostly just data and users."

### Advanced Questions

**Q4: How would you design a secure API?**
> "Key considerations: Authentication using OAuth 2.0 or API keys with proper scoping, all traffic over HTTPS, input validation and schema enforcement, rate limiting to prevent abuse, proper error handling that doesn't leak information, comprehensive logging, versioning strategy for deprecation, and documentation. Following OWASP API Top 10 guidelines, particularly around broken object-level authorization and authentication."

**Q5: Describe your approach to incident response.**
> "Following NIST framework: First is Preparation - having IR team, plan, playbooks, and tools ready. When incident occurs, Detection & Analysis phase - identify scope, severity, and affected systems. Then Containment - isolate affected systems to prevent spread. Eradication - remove threat and patch vulnerabilities. Recovery - restore systems and monitor closely. Finally Post-Incident review - lessons learned, update procedures, improve detection. Documentation throughout is critical."

---

## Learning Resources

### 📚 Websites

| Website | Link | What You'll Learn |
|---------|------|-------------------|
| **NIST** | https://www.nist.gov/cyberframework | Frameworks |
| **OWASP** | https://owasp.org/ | Application security |
| **SANS** | https://www.sans.org/reading-room/ | Best practices |
| **AWS Security** | https://aws.amazon.com/security/ | Cloud security |
| **Microsoft Security** | https://docs.microsoft.com/en-us/security/ | Azure security |

### 🎥 YouTube Videos

| Video | Link | Topic |
|-------|------|-------|
| **Zero Trust Explained** | https://www.youtube.com/watch?v=yn6CPQ9RioA | Architecture |
| **DevSecOps Tutorial** | https://www.youtube.com/watch?v=J73MELGF6u0 | CI/CD Security |
| **Cloud Security** | https://www.youtube.com/watch?v=Scd8i5ek0h0 | AWS Security |
| **API Security** | https://www.youtube.com/watch?v=t4-416mg6iU | OWASP API |
| **Incident Response** | https://www.youtube.com/watch?v=yM3U_hj7WOw | IR Process |

### 📖 Courses

| Course | Platform | Link |
|--------|----------|------|
| **AWS Security Specialty** | AWS | https://aws.amazon.com/certification/certified-security-specialty/ |
| **Azure Security** | Microsoft | https://docs.microsoft.com/en-us/learn/paths/azure-security-engineer/ |
| **Google Cloud Security** | Google | https://cloud.google.com/training/security |
| **CISSP** | ISC² | https://www.isc2.org/Certifications/CISSP |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│        SYSTEM DESIGN SECURITY QUICK REFERENCE                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SECURE DESIGN PRINCIPLES:                                  │
│  • Minimize attack surface                                 │
│  • Least privilege                                         │
│  • Defense in depth                                        │
│  • Fail securely                                           │
│  • Zero trust                                              │
│                                                             │
│  AUTHENTICATION:                                            │
│  • MFA required                                            │
│  • OAuth 2.0 / OIDC for delegation                        │
│  • JWT with short expiry                                   │
│                                                             │
│  AUTHORIZATION:                                             │
│  • RBAC or ABAC                                            │
│  • Server-side enforcement                                 │
│  • Deny by default                                         │
│                                                             │
│  API SECURITY:                                              │
│  • HTTPS only                                              │
│  • Input validation                                        │
│  • Rate limiting                                           │
│  • Don't leak errors                                       │
│                                                             │
│  DEVSECOPS:                                                 │
│  • SAST (code scan)                                        │
│  • DAST (running app scan)                                 │
│  • SCA (dependency scan)                                   │
│  • Secrets management                                      │
│                                                             │
│  INCIDENT RESPONSE:                                         │
│  Prepare → Detect → Contain → Eradicate → Recover → Learn  │
│                                                             │
│  CLOUD:                                                     │
│  • Shared responsibility                                   │
│  • IAM least privilege                                     │
│  • Encrypt everything                                      │
│  • Enable logging                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Congratulations! 🎉

You have completed all the TCS HackQuest Cybersecurity preparation topics!

**Review Order:**
1. [CIA Triad & Cybersecurity Fundamentals](../01_Cybersecurity_Fundamentals/01_CIA_Triad.md)
2. [OWASP Top 10](../02_OWASP_Top_10/01_OWASP_Complete_Guide.md)
3. [Network Security](../03_Network_Security/01_Network_Security_Complete.md)
4. [Cryptography](../04_Cryptography/01_Cryptography_Complete.md)
5. [Malware & Threats](../05_Malware_and_Threats/01_Malware_Complete_Guide.md)
6. [Ethical Hacking](../06_Ethical_Hacking/01_Ethical_Hacking_Guide.md)
7. [Security Tools](../07_Security_Tools/01_Security_Tools_Guide.md)
8. [System Design Security](./01_Secure_Architecture.md) ← You are here!

**Good luck with your TCS HackQuest Prime interview!** 🚀
