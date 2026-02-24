# 📜 COMPLIANCE & REGULATIONS - HIGH PRIORITY
## TCS HackQuest Interview Guide | MUST KNOW for Enterprise Security

---

# 🎯 PRIORITY RATING: ⭐⭐⭐⭐⭐ (VERY HIGH)
> TCS works with Fortune 500 clients - compliance knowledge is MANDATORY

---

# 📋 TABLE OF CONTENTS

1. [Why Compliance Matters](#why-compliance-matters)
2. [GDPR (General Data Protection Regulation)](#gdpr)
3. [HIPAA (Healthcare)](#hipaa)
4. [PCI-DSS (Payment Cards)](#pci-dss)
5. [SOC 2 (Service Organizations)](#soc-2)
6. [ISO 27001 (Information Security)](#iso-27001)
7. [NIST Framework](#nist-cybersecurity-framework)
8. [India-Specific Regulations](#india-specific-regulations)
9. [Interview Questions & Answers](#interview-questions--answers)

---

# WHY COMPLIANCE MATTERS

```
┌─────────────────────────────────────────────────────────────┐
│         WHY COMPLIANCE IS ASKED IN INTERVIEWS               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TCS Clients Include:                                       │
│  ├── Banks (need PCI-DSS, SOX)                             │
│  ├── Healthcare companies (need HIPAA)                     │
│  ├── European companies (need GDPR)                        │
│  ├── Government (need NIST, FedRAMP)                       │
│  └── All enterprises (need SOC 2, ISO 27001)               │
│                                                             │
│  As Security Professional You Will:                         │
│  ├── Perform compliance audits                              │
│  ├── Implement security controls for compliance             │
│  ├── Document evidence for auditors                         │
│  └── Advise clients on compliance requirements              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# GDPR
## General Data Protection Regulation (European Union)

### What It Is:
EU regulation protecting personal data of EU citizens. **Applies worldwide** if you process EU citizen data.

### Key Principles (Know These!):

| Principle | Meaning |
|-----------|---------|
| **Lawfulness** | Legal basis needed to process data |
| **Purpose Limitation** | Only use data for stated purpose |
| **Data Minimization** | Collect only what's necessary |
| **Accuracy** | Keep data accurate, updated |
| **Storage Limitation** | Don't keep data longer than needed |
| **Integrity & Confidentiality** | Protect data security |
| **Accountability** | Must demonstrate compliance |

### Key Terms:

```
┌─────────────────────────────────────────────────────────────┐
│                    GDPR KEY TERMS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Data Subject     = The person whose data is collected      │
│  Data Controller  = Organization deciding what data to      │
│                     collect and why (e.g., TCS client)      │
│  Data Processor   = Organization processing data on behalf  │
│                     of controller (e.g., TCS)               │
│  DPO              = Data Protection Officer (mandatory      │
│                     for large-scale processing)             │
│  Personal Data    = Any info relating to identified person  │
│  Special Category = Sensitive data (health, race, religion) │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### User Rights Under GDPR:

| Right | Description |
|-------|-------------|
| **Right to Access** | User can request their data |
| **Right to Rectification** | Correct inaccurate data |
| **Right to Erasure** | "Right to be forgotten" |
| **Right to Portability** | Transfer data to another service |
| **Right to Object** | Stop processing (esp. marketing) |
| **Right to Explanation** | Explain automated decisions |

### Breach Notification:
```
┌─────────────────────────────────────────────────────────────┐
│              GDPR BREACH NOTIFICATION                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Timeline:                                                  │
│  ├── 72 HOURS to notify Data Protection Authority          │
│  └── "Without undue delay" to notify affected individuals  │
│       (if high risk)                                        │
│                                                             │
│  What to Report:                                            │
│  ├── Nature of breach                                       │
│  ├── Categories and number of individuals affected          │
│  ├── Likely consequences                                    │
│  └── Measures taken to address breach                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Penalties:
- **Tier 1**: Up to €10 million or 2% annual revenue
- **Tier 2**: Up to €20 million or 4% annual revenue (whichever higher)

### Real Case:
- **Meta (2023)**: €1.2 billion fine for transferring EU data to US

---

# HIPAA
## Health Insurance Portability and Accountability Act (US Healthcare)

### What It Protects:
**PHI (Protected Health Information)** - Any health data that can identify a person.

### Who Must Comply:
```
Covered Entities:
├── Healthcare providers (hospitals, doctors)
├── Health plans (insurance)
└── Healthcare clearinghouses

Business Associates:
├── IT vendors processing health data
├── Cloud providers storing PHI
└── TCS working with healthcare clients
```

### HIPAA Rules:

| Rule | Purpose |
|------|---------|
| **Privacy Rule** | How PHI can be used and disclosed |
| **Security Rule** | Technical safeguards for ePHI |
| **Breach Notification Rule** | When/how to report breaches |
| **Enforcement Rule** | Penalties for violations |

### Security Rule Safeguards:

```
┌─────────────────────────────────────────────────────────────┐
│              HIPAA SECURITY SAFEGUARDS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Administrative Safeguards:                                 │
│  ├── Risk analysis                                          │
│  ├── Security policies                                      │
│  ├── Employee training                                      │
│  └── Incident response procedures                           │
│                                                             │
│  Physical Safeguards:                                       │
│  ├── Facility access controls                               │
│  ├── Workstation security                                   │
│  └── Device and media controls                              │
│                                                             │
│  Technical Safeguards:                                      │
│  ├── Access controls (unique user IDs)                      │
│  ├── Audit controls (logging)                               │
│  ├── Integrity controls                                     │
│  ├── Transmission security (encryption)                     │
│  └── Authentication                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Penalties:
| Tier | Violation Type | Fine Range |
|------|----------------|------------|
| 1 | Unknowing | $100 - $50,000 per violation |
| 2 | Reasonable cause | $1,000 - $50,000 per violation |
| 3 | Willful neglect (corrected) | $10,000 - $50,000 per violation |
| 4 | Willful neglect (not corrected) | $50,000+ per violation |

**Annual maximum**: $1.5 million per violation category

### Real Case:
- **Change Healthcare (2024)**: Major HIPAA breach, 100M+ affected

---

# PCI-DSS
## Payment Card Industry Data Security Standard

### What It Protects:
**Cardholder Data (CHD)** - Credit/debit card information

### Who Must Comply:
Any organization that stores, processes, or transmits cardholder data.

### Cardholder Data Elements:

```
┌─────────────────────────────────────────────────────────────┐
│            PCI-DSS DATA ELEMENTS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Cardholder Data (CAN be stored if protected):              │
│  ├── Primary Account Number (PAN) - MUST be protected       │
│  ├── Cardholder Name                                        │
│  ├── Expiration Date                                        │
│  └── Service Code                                           │
│                                                             │
│  Sensitive Authentication Data (NEVER store):               │
│  ├── Full magnetic stripe data                              │
│  ├── CVV/CVC (3-digit code)                                │
│  └── PIN/PIN block                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### PCI-DSS 12 Requirements:

```
┌─────────────────────────────────────────────────────────────┐
│           PCI-DSS 12 REQUIREMENTS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Build & Maintain Secure Network:                           │
│  1. Install and maintain firewall                           │
│  2. Don't use vendor default passwords                      │
│                                                             │
│  Protect Cardholder Data:                                   │
│  3. Protect stored cardholder data                          │
│  4. Encrypt transmission over public networks               │
│                                                             │
│  Maintain Vulnerability Management:                         │
│  5. Use and regularly update anti-virus                     │
│  6. Develop secure systems and applications                 │
│                                                             │
│  Implement Access Control:                                  │
│  7. Restrict access by need-to-know                         │
│  8. Assign unique ID to each user                           │
│  9. Restrict physical access to cardholder data             │
│                                                             │
│  Monitor and Test Networks:                                 │
│  10. Track and monitor all access                           │
│  11. Regularly test security systems                        │
│                                                             │
│  Maintain Information Security Policy:                      │
│  12. Maintain security policy for all personnel             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Compliance Levels:

| Level | Transaction Volume | Requirements |
|-------|-------------------|--------------|
| Level 1 | 6M+ transactions/year | Annual on-site audit by QSA |
| Level 2 | 1M - 6M transactions | Annual SAQ, quarterly network scan |
| Level 3 | 20K - 1M e-commerce | Annual SAQ, quarterly network scan |
| Level 4 | <20K e-commerce, <1M total | Annual SAQ, quarterly network scan |

### Key Terms:
- **QSA**: Qualified Security Assessor (external auditor)
- **ISA**: Internal Security Assessor
- **SAQ**: Self-Assessment Questionnaire
- **ASV**: Approved Scanning Vendor (for network scans)
- **ROC**: Report on Compliance

---

# SOC 2
## Service Organization Control 2

### What It Is:
Framework for managing customer data based on **Trust Services Criteria**.

### Who Needs It:
Any service provider handling customer data - SaaS, cloud, data centers, TCS!

### Trust Services Criteria (TSC):

```
┌─────────────────────────────────────────────────────────────┐
│            SOC 2 TRUST SERVICES CRITERIA                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. SECURITY (Required for all SOC 2)                       │
│     └─ Protection against unauthorized access               │
│                                                             │
│  2. AVAILABILITY                                            │
│     └─ System is available for operation as agreed          │
│                                                             │
│  3. PROCESSING INTEGRITY                                    │
│     └─ System processing is complete, accurate, timely      │
│                                                             │
│  4. CONFIDENTIALITY                                         │
│     └─ Confidential information is protected                │
│                                                             │
│  5. PRIVACY                                                 │
│     └─ Personal information handled per privacy notice      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### SOC 2 Type I vs Type II:

| Aspect | Type I | Type II |
|--------|--------|---------|
| **What** | Design of controls | Design AND operating effectiveness |
| **When** | Point in time | Period of time (6-12 months) |
| **Value** | Quick compliance | More rigorous, preferred |
| **Use** | New companies | Established security program |

### SOC 2 Report Contents:
1. Management assertion
2. Independent auditor's report
3. Description of system
4. Control objectives and controls
5. Tests performed and results

---

# ISO 27001
## Information Security Management System (ISMS)

### What It Is:
International standard for establishing, implementing, maintaining, and improving an ISMS.

### Structure:

```
┌─────────────────────────────────────────────────────────────┐
│              ISO 27001 STRUCTURE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Clauses 4-10 (Management Requirements):                    │
│  4. Context of the organization                             │
│  5. Leadership                                              │
│  6. Planning (risk assessment)                              │
│  7. Support (resources, competence)                         │
│  8. Operation                                               │
│  9. Performance evaluation                                  │
│  10. Improvement                                            │
│                                                             │
│  Annex A (114 Controls in 14 Domains):                      │
│  A.5  Information security policies                         │
│  A.6  Organization of information security                  │
│  A.7  Human resource security                               │
│  A.8  Asset management                                      │
│  A.9  Access control                                        │
│  A.10 Cryptography                                          │
│  A.11 Physical and environmental security                   │
│  A.12 Operations security                                   │
│  A.13 Communications security                               │
│  A.14 System acquisition, development, maintenance          │
│  A.15 Supplier relationships                                │
│  A.16 Information security incident management              │
│  A.17 Business continuity                                   │
│  A.18 Compliance                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Documents:
- **ISMS Scope**: What's covered
- **Information Security Policy**: High-level commitment
- **Risk Assessment**: Identify and evaluate risks
- **Statement of Applicability (SoA)**: Which controls apply
- **Risk Treatment Plan**: How risks will be addressed

### Certification Process:
```
Stage 1 Audit → Gap Analysis → Fixes → Stage 2 Audit → Certificate
                                              ↓
                               Annual Surveillance Audits
                                              ↓
                               3-Year Recertification
```

---

# NIST CYBERSECURITY FRAMEWORK

### What It Is:
US framework for managing cybersecurity risk. Widely adopted globally.

### Five Core Functions:

```
┌─────────────────────────────────────────────────────────────┐
│           NIST CSF CORE FUNCTIONS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐
│  │ IDENTIFY │→│ PROTECT  │→│  DETECT  │→│ RESPOND  │→│ RECOVER │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └─────────┘
│                                                             │
│  IDENTIFY: Know your assets, risks, and requirements        │
│  ├── Asset management                                       │
│  ├── Business environment                                   │
│  ├── Governance                                             │
│  └── Risk assessment                                        │
│                                                             │
│  PROTECT: Implement safeguards                              │
│  ├── Access control                                         │
│  ├── Awareness and training                                 │
│  ├── Data security                                          │
│  └── Protective technology                                  │
│                                                             │
│  DETECT: Identify cybersecurity events                      │
│  ├── Anomalies and events                                   │
│  ├── Continuous monitoring                                  │
│  └── Detection processes                                    │
│                                                             │
│  RESPOND: Take action on detected events                    │
│  ├── Response planning                                      │
│  ├── Communications                                         │
│  ├── Analysis                                               │
│  └── Mitigation                                             │
│                                                             │
│  RECOVER: Restore capabilities after incident               │
│  ├── Recovery planning                                      │
│  ├── Improvements                                           │
│  └── Communications                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Implementation Tiers:
| Tier | Description |
|------|-------------|
| **Tier 1: Partial** | Ad hoc, reactive |
| **Tier 2: Risk Informed** | Aware, not organization-wide |
| **Tier 3: Repeatable** | Formal policies, organization-wide |
| **Tier 4: Adaptive** | Continuous improvement, agile |

---

# INDIA-SPECIFIC REGULATIONS

### IT Act 2000 (Amended 2008):
- Legal recognition for electronic transactions
- Cyber crime definitions and penalties
- Section 43A: Compensation for failure to protect data
- Section 66: Hacking penalties (up to 3 years, ₹5 lakh)
- Section 72: Privacy breach penalties

### DPDP Act 2023 (Digital Personal Data Protection):
```
┌─────────────────────────────────────────────────────────────┐
│              INDIA DPDP ACT 2023                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Key Terms:                                                 │
│  ├── Data Fiduciary (like Controller in GDPR)              │
│  ├── Data Processor                                         │
│  ├── Data Principal (the individual)                        │
│  └── Consent Manager (new concept)                          │
│                                                             │
│  Data Principal Rights:                                     │
│  ├── Right to access information                            │
│  ├── Right to correction and erasure                        │
│  ├── Right to grievance redressal                           │
│  └── Right to nominate                                      │
│                                                             │
│  Penalties:                                                 │
│  ├── Up to ₹250 crore per violation                        │
│  └── Based on severity and repeated violations              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### RBI Guidelines (for Banking):
- Cybersecurity Framework for Banks
- Payment Aggregator regulations
- Data localization requirements

### SEBI Guidelines (for Stock Markets):
- Cybersecurity for stock brokers
- Incident reporting requirements

---

# INTERVIEW QUESTIONS & ANSWERS

---

## Q1: "What is GDPR and when does it apply?"

### ✅ MODEL ANSWER:
> "GDPR is the General Data Protection Regulation, an EU law that protects personal data of EU citizens.
>
> **It applies when:**
> - You're based in the EU
> - OR you process data of EU residents (even from outside EU)
>
> **Key principles include:**
> - Lawful basis for processing
> - Purpose limitation
> - Data minimization
> - Storage limitation
> - User rights (access, erasure, portability)
>
> **For security professionals:**
> - Must implement appropriate technical measures
> - Encryption, access controls, audit logging
> - 72-hour breach notification to authorities
>
> **Relevance to TCS:**
> TCS has many European clients. As a data processor, we must comply with GDPR while handling their customer data. This includes having Data Processing Agreements and implementing required security controls."

---

## Q2: "Explain PCI-DSS. What are its 12 requirements?"

### ✅ MODEL ANSWER:
> "PCI-DSS is the Payment Card Industry Data Security Standard. It applies to anyone storing, processing, or transmitting credit card data.
>
> **The 12 requirements are:**
>
> **Network Security:**
> 1. Install and maintain firewalls
> 2. Change vendor default passwords
>
> **Data Protection:**
> 3. Protect stored cardholder data (encrypt PAN)
> 4. Encrypt transmission over public networks
>
> **Vulnerability Management:**
> 5. Use and update antivirus
> 6. Develop secure systems
>
> **Access Control:**
> 7. Restrict access by need-to-know
> 8. Unique user IDs for everyone
> 9. Restrict physical access
>
> **Monitoring:**
> 10. Track and monitor all access
> 11. Regularly test security
>
> **Policy:**
> 12. Maintain security policy
>
> **Key point:** You can NEVER store CVV/CVV2 or full magnetic stripe data, even if encrypted."

---

## Q3: "What's the difference between SOC 2 Type I and Type II?"

### ✅ MODEL ANSWER:
> "Both are SOC 2 audit reports, but they differ in scope:
>
> **SOC 2 Type I:**
> - Point-in-time assessment
> - Evaluates if controls are designed properly
> - Snapshot on a specific date
> - Quicker to obtain
> - Useful for new companies proving initial compliance
>
> **SOC 2 Type II:**
> - Period of time (typically 6-12 months)
> - Evaluates design AND operating effectiveness
> - Tests if controls actually worked over time
> - More rigorous and trusted
> - Preferred by enterprise customers
>
> **Example:**
> Type I might check: 'Is there an access control policy?'
> Type II would verify: 'Was the policy followed for the past 12 months?' by testing actual access logs.
>
> **For TCS clients**, Type II is usually required as it provides more assurance."

---

## Q4: "How does HIPAA differ from GDPR?"

### ✅ MODEL ANSWER:
> "Both protect personal data, but they have different focuses:
>
> | Aspect | HIPAA | GDPR |
> |--------|-------|------|
> | **Scope** | US healthcare only | All personal data, EU citizens |
> | **Data Type** | Protected Health Information | Any personal data |
> | **Who** | Covered entities & business associates | Controllers & processors |
> | **Consent** | Not always required | Usually required |
> | **Breach Notification** | 60 days to individuals | 72 hours to authority |
> | **Fines** | Up to $1.5M/year per category | Up to 4% revenue or €20M |
>
> **Key HIPAA-specific concepts:**
> - PHI (Protected Health Information)
> - De-identification (Safe Harbor method)
> - Business Associate Agreements (BAA)
>
> **Key GDPR-specific concepts:**
> - Right to be forgotten
> - Data portability
> - Consent withdrawal
>
> Organizations dealing with EU healthcare data must comply with BOTH."

---

## Q5: "What is ISO 27001 and why is it important?"

### ✅ MODEL ANSWER:
> "ISO 27001 is an international standard for Information Security Management Systems (ISMS).
>
> **What it provides:**
> - Framework for managing security risks
> - 114 controls across 14 domains
> - Continuous improvement approach (Plan-Do-Check-Act)
>
> **Certification process:**
> 1. Implement ISMS
> 2. Stage 1 audit (documentation review)
> 3. Stage 2 audit (effectiveness testing)
> 4. Certificate valid for 3 years
> 5. Annual surveillance audits
>
> **Why it matters for TCS:**
> - Demonstrates security commitment to clients
> - Required by many enterprise contracts
> - Provides structured approach to security
> - International recognition
>
> **Key documents:**
> - Scope statement
> - Information Security Policy
> - Risk Assessment
> - Statement of Applicability (SoA)
>
> TCS is ISO 27001 certified, which is why clients trust us with their data."

---

## Q6: "What is the NIST Cybersecurity Framework?"

### ✅ MODEL ANSWER:
> "NIST CSF is a risk-based framework with five core functions:
>
> **IDENTIFY** - Know your environment
> - Asset inventory
> - Risk assessment
> - Business context
>
> **PROTECT** - Implement safeguards
> - Access control
> - Encryption
> - Training
>
> **DETECT** - Find threats
> - Monitoring
> - Anomaly detection
> - Log analysis
>
> **RESPOND** - Handle incidents
> - Incident response plans
> - Communication
> - Containment
>
> **RECOVER** - Restore operations
> - Backup restoration
> - Lessons learned
> - Business continuity
>
> **Implementation Tiers** (maturity levels):
> - Tier 1: Partial (ad hoc)
> - Tier 2: Risk Informed
> - Tier 3: Repeatable (formal policies)
> - Tier 4: Adaptive (continuous improvement)
>
> **Why it's popular:**
> - Flexible, works with other frameworks
> - Free and widely recognized
> - Risk-based approach
> - Commonly required for US government contracts"

---

## Q7: "A client asks how to achieve GDPR compliance. What steps would you recommend?"

### ✅ MODEL ANSWER:
> "I would recommend a structured approach:
>
> **1. Data Discovery & Mapping**
> - Identify what personal data you collect
> - Where it's stored
> - How it flows through systems
> - Create Records of Processing Activities (ROPA)
>
> **2. Legal Basis Review**
> - For each data type, identify legal basis
> - Consent, contract, legal obligation, legitimate interest
> - Update privacy notices
>
> **3. Technical Controls**
> - Encryption at rest and in transit
> - Access controls and authentication
> - Logging and monitoring
> - Data minimization in databases
>
> **4. Process Updates**
> - User access request procedures
> - Data deletion procedures
> - Breach notification process (72 hours)
> - Vendor management (DPAs)
>
> **5. Governance**
> - Appoint DPO if required
> - Staff training
> - Regular audits
> - Policy documentation
>
> **6. Rights Management**
> - System to handle access requests
> - Deletion capability
> - Data portability
>
> My vulnerability scanner project demonstrates similar thinking - identifying data flows and implementing appropriate controls."

---

## Q8: "What happens when a data breach occurs under GDPR?"

### ✅ MODEL ANSWER:
> "GDPR has strict breach notification requirements:
>
> **Notification to Authority (72 hours):**
> - Notify supervisory authority within 72 hours of awareness
> - Unless breach unlikely to result in risk
> - If delayed, must explain why
>
> **Content of notification:**
> - Nature of breach
> - Categories and approximate numbers affected
> - Name of DPO or contact
> - Likely consequences
> - Measures taken/proposed
>
> **Notification to Individuals:**
> - Required if 'high risk' to their rights
> - Must be in clear, plain language
> - Describe nature and measures
>
> **What to do as security professional:**
>
> 1. **Immediate**: Contain the breach
> 2. **First hour**: Document everything
> 3. **First 24 hours**: 
>    - Assess scope and impact
>    - Notify leadership
>    - Begin preparing notification
> 4. **72 hours**: Submit to authority
> 5. **After**: Review, improve controls
>
> **Example scenario:**
> Database exposed → Contain access → Document → Risk assess → 72-hour notification → Fix vulnerability → Post-incident review"

---

## Q9: "What is a Data Protection Impact Assessment (DPIA)?"

### ✅ MODEL ANSWER:
> "A DPIA is a process to identify and minimize data protection risks.
>
> **When required:**
> - High-risk processing
> - Large-scale profiling
> - Systematic monitoring of public areas
> - New technology processing
>
> **DPIA Process:**
>
> 1. **Describe Processing**
>    - What data, why, how
>    - Data flows
>
> 2. **Assess Necessity**
>    - Is this processing necessary?
>    - Could you achieve goal differently?
>
> 3. **Identify Risks**
>    - To individuals' rights
>    - Privacy, discrimination, financial
>
> 4. **Mitigating Measures**
>    - Technical controls
>    - Policy controls
>    - Organizational measures
>
> 5. **Document & Review**
>    - Record decision
>    - Consult DPO
>    - Review periodically
>
> **Example:**
> Implementing facial recognition system:
> - High risk = DPIA required
> - Assess necessity
> - Document privacy risks
> - Implement consent, data minimization
> - Consult authority if still high risk"

---

## Q10: "How do compliance frameworks overlap?"

### ✅ MODEL ANSWER:
> "Many compliance requirements share common controls, allowing efficient compliance:
>
> ```
> Common Controls Across Frameworks:
> 
> Access Control: GDPR ✓ | HIPAA ✓ | PCI-DSS ✓ | SOC2 ✓ | ISO27001 ✓
> Encryption:     GDPR ✓ | HIPAA ✓ | PCI-DSS ✓ | SOC2 ✓ | ISO27001 ✓
> Logging:        GDPR ✓ | HIPAA ✓ | PCI-DSS ✓ | SOC2 ✓ | ISO27001 ✓
> Training:       GDPR ✓ | HIPAA ✓ | PCI-DSS ✓ | SOC2 ✓ | ISO27001 ✓
> Incident Resp:  GDPR ✓ | HIPAA ✓ | PCI-DSS ✓ | SOC2 ✓ | ISO27001 ✓
> ```
>
> **Approach:**
>
> 1. Use ISO 27001 as baseline (comprehensive)
> 2. Map other requirements to ISO controls
> 3. Identify gaps (specific requirements)
> 4. Implement unified control framework
>
> **Example mapping:**
> - ISO 27001 A.9 (Access Control) satisfies:
>   - PCI-DSS Req 7, 8
>   - HIPAA Access Controls
>   - SOC 2 Security
>   - GDPR appropriate measures
>
> **Tools:**
> - GRC platforms (ServiceNow, RSA Archer)
> - Unified control frameworks (UCF)
>
> This 'implement once, comply many' approach saves effort and ensures consistency."

---

# 📋 COMPLIANCE QUICK REFERENCE

| Framework | Scope | Focus | Key Penalty |
|-----------|-------|-------|-------------|
| **GDPR** | EU data | Privacy rights | 4% revenue |
| **HIPAA** | US healthcare | PHI protection | $1.5M/year |
| **PCI-DSS** | Card payments | Card data security | Fines + lose card processing |
| **SOC 2** | Service providers | Trust criteria | Lose customers |
| **ISO 27001** | Any organization | ISMS | Lose certification |
| **NIST CSF** | Any (US gov focus) | Risk management | Contract requirements |
| **DPDP 2023** | India data | Privacy | ₹250 crore |

---

**Document Created**: February 2026
**Priority**: ⭐⭐⭐⭐⭐ HIGH - Expected in TCS HackQuest
