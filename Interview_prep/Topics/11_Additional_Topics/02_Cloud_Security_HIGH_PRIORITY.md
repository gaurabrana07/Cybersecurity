# ☁️ CLOUD SECURITY - HIGH PRIORITY
## TCS HackQuest Interview Guide | AWS, Azure, GCP Security

---

# 🎯 PRIORITY RATING: ⭐⭐⭐⭐⭐ (VERY HIGH)
> TCS is a major cloud service provider - Cloud security is ESSENTIAL

---

# 📋 TABLE OF CONTENTS

1. [Cloud Security Fundamentals](#cloud-security-fundamentals)
2. [Shared Responsibility Model](#shared-responsibility-model)
3. [AWS Security](#aws-security)
4. [Azure Security](#azure-security)
5. [GCP Security](#gcp-security)
6. [Common Cloud Misconfigurations](#common-cloud-misconfigurations)
7. [Cloud Security Tools](#cloud-security-tools)
8. [Interview Questions & Answers](#interview-questions--answers)

---

# CLOUD SECURITY FUNDAMENTALS

## Why Cloud Security is Different:

```
┌─────────────────────────────────────────────────────────────┐
│         TRADITIONAL vs CLOUD SECURITY                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TRADITIONAL:                                               │
│  ├── You own everything                                     │
│  ├── Physical perimeter exists                              │
│  ├── Network is your boundary                               │
│  └── Slower to scale                                        │
│                                                             │
│  CLOUD:                                                     │
│  ├── Shared responsibility                                  │
│  ├── No physical perimeter (identity is perimeter)         │
│  ├── Internet-accessible by default                         │
│  ├── API-driven (new attack surface)                        │
│  ├── Rapid scale = rapid misconfiguration                   │
│  └── Multi-tenant environment                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Cloud Service Models:

```
┌─────────────────────────────────────────────────────────────┐
│              CLOUD SERVICE MODELS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IaaS (Infrastructure as a Service)                         │
│  ├── Examples: EC2, Azure VMs, Compute Engine               │
│  ├── You manage: OS, Apps, Data, Runtime                    │
│  └── Provider manages: Hardware, Network, Storage           │
│                                                             │
│  PaaS (Platform as a Service)                               │
│  ├── Examples: Elastic Beanstalk, App Service, App Engine   │
│  ├── You manage: Apps, Data                                 │
│  └── Provider manages: Runtime, OS, Hardware                │
│                                                             │
│  SaaS (Software as a Service)                               │
│  ├── Examples: Office 365, Salesforce, Gmail                │
│  ├── You manage: Data, Access, Configuration                │
│  └── Provider manages: Everything else                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# SHARED RESPONSIBILITY MODEL

## The Most Important Cloud Security Concept:

```
┌─────────────────────────────────────────────────────────────┐
│           SHARED RESPONSIBILITY MODEL                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    IaaS      PaaS      SaaS                 │
│                   ─────────────────────────────             │
│  Data             │ YOU  │  │ YOU  │  │ YOU  │  ← Always   │
│  Access Control   │ YOU  │  │ YOU  │  │ YOU  │    yours    │
│  ─────────────────┼──────┼──┼──────┼──┼──────┼─────────    │
│  Application      │ YOU  │  │ YOU  │  │ CSP  │             │
│  Runtime          │ YOU  │  │ CSP  │  │ CSP  │             │
│  OS               │ YOU  │  │ CSP  │  │ CSP  │             │
│  ─────────────────┼──────┼──┼──────┼──┼──────┼─────────    │
│  Network          │ CSP  │  │ CSP  │  │ CSP  │  ← Always   │
│  Storage          │ CSP  │  │ CSP  │  │ CSP  │    CSP's    │
│  Hardware         │ CSP  │  │ CSP  │  │ CSP  │             │
│  Physical         │ CSP  │  │ CSP  │  │ CSP  │             │
│                                                             │
│  CSP = Cloud Service Provider                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Key Takeaway:
> **Cloud providers secure the cloud. YOU secure what's IN the cloud.**

### Snowflake Breach Example (2024):
```
What happened:
- Attackers used stolen credentials
- Accessed Snowflake customer accounts
- Stole 110M+ records (AT&T, Ticketmaster)

Was Snowflake breached? NO.
Was customer configuration at fault? YES.
- No MFA enabled
- Weak credentials
- No IP restrictions

This is SHARED RESPONSIBILITY in action.
```

---

# AWS SECURITY

## Core AWS Security Services:

```
┌─────────────────────────────────────────────────────────────┐
│              AWS SECURITY SERVICES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IDENTITY & ACCESS:                                         │
│  ├── IAM (Identity and Access Management)                   │
│  ├── AWS Organizations (multi-account)                      │
│  ├── SSO / IAM Identity Center                              │
│  └── Cognito (user authentication)                          │
│                                                             │
│  NETWORK SECURITY:                                          │
│  ├── VPC (Virtual Private Cloud)                            │
│  ├── Security Groups (instance firewalls)                   │
│  ├── NACLs (subnet firewalls)                               │
│  ├── AWS WAF (web application firewall)                     │
│  ├── Shield (DDoS protection)                               │
│  └── Network Firewall                                       │
│                                                             │
│  DATA PROTECTION:                                           │
│  ├── KMS (Key Management Service)                           │
│  ├── Secrets Manager                                        │
│  ├── Certificate Manager                                    │
│  └── Macie (sensitive data discovery)                       │
│                                                             │
│  DETECTION & MONITORING:                                    │
│  ├── CloudTrail (API logging)                               │
│  ├── CloudWatch (monitoring)                                │
│  ├── GuardDuty (threat detection)                           │
│  ├── Security Hub (unified security)                        │
│  └── Inspector (vulnerability scanning)                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## AWS IAM (Know This Well!):

### IAM Components:
| Component | Description |
|-----------|-------------|
| **Users** | Individual identities |
| **Groups** | Collection of users |
| **Roles** | Assumed by services/users |
| **Policies** | JSON documents defining permissions |

### IAM Policy Structure:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "192.168.1.0/24"
                }
            }
        }
    ]
}
```

### IAM Best Practices:
1. **Never use root account** for daily tasks
2. **Enable MFA** on all accounts
3. **Least privilege** - minimum permissions needed
4. **Use roles** for applications, not access keys
5. **Rotate credentials** regularly
6. **Use IAM Access Analyzer** to find over-permissive policies

## S3 Security:

```
┌─────────────────────────────────────────────────────────────┐
│                S3 SECURITY CONTROLS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Bucket Policy (Resource-based):                            │
│  └── Who can access THIS bucket                             │
│                                                             │
│  IAM Policy (Identity-based):                               │
│  └── What buckets THIS user can access                      │
│                                                             │
│  Access Control Lists (Legacy):                             │
│  └── Simple permissions (avoid using)                       │
│                                                             │
│  Block Public Access (Account-level):                       │
│  └── ALWAYS enable unless public access needed              │
│                                                             │
│  Encryption:                                                │
│  ├── SSE-S3 (AWS managed keys)                              │
│  ├── SSE-KMS (Customer managed keys in KMS)                 │
│  └── SSE-C (Customer provided keys)                         │
│                                                             │
│  Versioning:                                                │
│  └── Protect against accidental deletion                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Famous S3 Breaches:
- **Capital One (2019)**: SSRF → IAM role → S3 access → 100M records
- **Twitch (2021)**: Misconfigured S3 → Source code leaked

## VPC Security:

```
┌─────────────────────────────────────────────────────────────┐
│                VPC SECURITY LAYERS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Internet                                                   │
│      ↓                                                      │
│  Internet Gateway                                           │
│      ↓                                                      │
│  Network ACL (Subnet Level)                                 │
│  ├── Stateless (must allow both inbound/outbound)          │
│  ├── Rules processed in order                               │
│  └── Allow/Deny rules                                       │
│      ↓                                                      │
│  Security Group (Instance Level)                            │
│  ├── Stateful (return traffic auto-allowed)                 │
│  ├── Allow rules only (implicit deny)                       │
│  └── Attached to ENI                                        │
│      ↓                                                      │
│  EC2 Instance                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Aspect | Security Group | NACL |
|--------|----------------|------|
| **Level** | Instance | Subnet |
| **State** | Stateful | Stateless |
| **Rules** | Allow only | Allow and Deny |
| **Order** | All evaluated | Numbered order |

---

# AZURE SECURITY

## Core Azure Security Services:

```
┌─────────────────────────────────────────────────────────────┐
│              AZURE SECURITY SERVICES                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IDENTITY & ACCESS:                                         │
│  ├── Azure AD / Entra ID                                    │
│  ├── Conditional Access                                     │
│  ├── Privileged Identity Management (PIM)                   │
│  └── Managed Identities                                     │
│                                                             │
│  NETWORK SECURITY:                                          │
│  ├── Network Security Groups (NSG)                          │
│  ├── Azure Firewall                                         │
│  ├── DDoS Protection                                        │
│  ├── Application Gateway + WAF                              │
│  └── Private Link                                           │
│                                                             │
│  DATA PROTECTION:                                           │
│  ├── Key Vault                                              │
│  ├── Azure Information Protection                           │
│  └── Storage Service Encryption                             │
│                                                             │
│  DETECTION & MONITORING:                                    │
│  ├── Microsoft Defender for Cloud                           │
│  ├── Azure Sentinel (SIEM)                                  │
│  ├── Azure Monitor                                          │
│  └── Log Analytics                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Azure AD / Entra ID:

### Key Features:
- **Conditional Access**: Context-aware access control
- **MFA**: Multi-factor authentication
- **SSO**: Single sign-on to apps
- **PIM**: Time-limited admin access

### Conditional Access Policy:
```
IF:
  User is in "Sales Group"
  AND accessing "Salesforce"
  AND location is outside corporate network
  AND device is not compliant
THEN:
  Require MFA
  Block if still risky
```

## Azure Security Best Practices:

1. **Enable Defender for Cloud** (free tier available)
2. **Use Managed Identities** (no credential management)
3. **Implement Conditional Access**
4. **Enable logging** to Log Analytics
5. **Use Azure Policy** for governance
6. **Regular access reviews** with PIM

---

# GCP SECURITY

## Core GCP Security Services:

```
┌─────────────────────────────────────────────────────────────┐
│              GCP SECURITY SERVICES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IDENTITY & ACCESS:                                         │
│  ├── Cloud IAM                                              │
│  ├── Cloud Identity                                         │
│  ├── Service Accounts                                       │
│  └── Identity-Aware Proxy (IAP)                             │
│                                                             │
│  NETWORK SECURITY:                                          │
│  ├── VPC Firewall Rules                                     │
│  ├── Cloud Armor (WAF + DDoS)                               │
│  ├── VPC Service Controls                                   │
│  └── Private Google Access                                  │
│                                                             │
│  DATA PROTECTION:                                           │
│  ├── Cloud KMS                                              │
│  ├── Secret Manager                                         │
│  ├── Cloud DLP                                              │
│  └── Customer-Managed Encryption Keys (CMEK)                │
│                                                             │
│  DETECTION & MONITORING:                                    │
│  ├── Security Command Center                                │
│  ├── Cloud Audit Logs                                       │
│  ├── Chronicle SIEM                                         │
│  └── Event Threat Detection                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## GCP IAM:

### Hierarchy:
```
Organization
    ├── Folder
    │   ├── Project
    │   │   ├── Resources (VMs, Storage, etc.)
```

### IAM Roles:
| Type | Description | Example |
|------|-------------|---------|
| **Basic** | Broad permissions | Owner, Editor, Viewer |
| **Predefined** | Granular, service-specific | roles/compute.admin |
| **Custom** | User-defined | project/custom-role |

### Best Practices:
1. **Avoid basic roles** (too broad)
2. **Use predefined roles** when possible
3. **Service accounts** for applications
4. **Workload Identity** for GKE
5. **Organization policies** for guardrails

---

# COMMON CLOUD MISCONFIGURATIONS

## Top Cloud Security Issues:

```
┌─────────────────────────────────────────────────────────────┐
│         TOP CLOUD MISCONFIGURATIONS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PUBLIC STORAGE BUCKETS  ⭐ Most Common                   │
│     └─ S3/Blob/GCS exposed to internet                      │
│                                                             │
│  2. OVERPRIVILEGED IAM ROLES                                │
│     └─ Admin access where read-only needed                  │
│                                                             │
│  3. NO MFA ON ADMIN ACCOUNTS                                │
│     └─ Single credential = full access                      │
│                                                             │
│  4. OPEN SECURITY GROUPS (0.0.0.0/0)                        │
│     └─ SSH/RDP open to world                                │
│                                                             │
│  5. UNENCRYPTED DATA                                        │
│     └─ Storage and transit without encryption               │
│                                                             │
│  6. LOG DELETION/NO LOGGING                                 │
│     └─ Can't detect or investigate breaches                 │
│                                                             │
│  7. EXPOSED SECRETS                                         │
│     └─ API keys in code, environment variables              │
│                                                             │
│  8. DEFAULT CREDENTIALS                                     │
│     └─ Database admin passwords unchanged                   │
│                                                             │
│  9. NO NETWORK SEGMENTATION                                 │
│     └─ Flat network, lateral movement easy                  │
│                                                             │
│  10. STALE ACCESS                                           │
│      └─ Ex-employees still have access                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Public S3 Bucket Detection:

```bash
# AWS CLI - Check bucket ACL
aws s3api get-bucket-acl --bucket bucket-name

# Check bucket policy
aws s3api get-bucket-policy --bucket bucket-name

# Check public access block
aws s3api get-public-access-block --bucket bucket-name
```

## Security Group Audit:

```bash
# Find security groups allowing 0.0.0.0/0 on SSH
aws ec2 describe-security-groups \
  --filters Name=ip-permission.cidr,Values='0.0.0.0/0' \
  --query 'SecurityGroups[?IpPermissions[?FromPort==`22`]]'
```

---

# CLOUD SECURITY TOOLS

## Cloud Security Posture Management (CSPM):

| Tool | Description |
|------|-------------|
| **Prisma Cloud** | Palo Alto's comprehensive CSPM |
| **Wiz** | Agentless, graph-based |
| **Orca Security** | SideScanning technology |
| **AWS Security Hub** | Native AWS aggregation |
| **Microsoft Defender** | Native Azure CSPM |
| **GCP Security Command Center** | Native GCP |

## Cloud Workload Protection (CWPP):

| Tool | Focus |
|------|-------|
| **CrowdStrike** | Endpoint + Cloud |
| **Lacework** | Anomaly detection |
| **Aqua Security** | Container security |
| **Sysdig** | Runtime security |

## Infrastructure as Code Security:

| Tool | What It Scans |
|------|---------------|
| **Checkov** | Terraform, CloudFormation, K8s |
| **tfsec** | Terraform specific |
| **Terrascan** | Multi-cloud IaC |
| **cfn-nag** | CloudFormation |

---

# INTERVIEW QUESTIONS & ANSWERS

---

## Q1: "Explain the Shared Responsibility Model."

### ✅ MODEL ANSWER:
> "The Shared Responsibility Model defines who is responsible for what in cloud environments.
>
> **Cloud Provider is responsible for:**
> - Physical security of data centers
> - Hardware and networking
> - Hypervisor security
> - Global infrastructure
>
> **Customer is responsible for:**
> - Data encryption and protection
> - Identity and access management
> - Network configuration (security groups)
> - Application security
> - OS patching (for IaaS)
>
> **It varies by service type:**
> - **IaaS (EC2)**: Customer manages most (OS, apps, data)
> - **PaaS (Lambda)**: Provider manages runtime, customer manages code/data
> - **SaaS (O365)**: Provider manages everything except data and access
>
> **Real Example - Snowflake Breach (2024):**
> Customer accounts were compromised, not Snowflake itself. Customers failed to enable MFA. This was the customer's responsibility under the shared model.
>
> Key message: Cloud providers secure the cloud, we secure what's IN the cloud."

---

## Q2: "How would you secure an S3 bucket?"

### ✅ MODEL ANSWER:
> "I would implement multiple layers of S3 security:
>
> **1. Block Public Access (First Line)**
> ```
> Enable all Block Public Access settings at account level
> Prevents accidental exposure
> ```
>
> **2. Bucket Policy**
> ```json
> {
>   \"Effect\": \"Deny\",
>   \"Principal\": \"*\",
>   \"Action\": \"s3:*\",
>   \"Resource\": \"arn:aws:s3:::bucket/*\",
>   \"Condition\": {
>     \"Bool\": { \"aws:SecureTransport\": \"false\" }
>   }
> }
> ```
> Enforces HTTPS only.
>
> **3. Encryption**
> - Enable SSE-S3 or SSE-KMS default encryption
> - For sensitive data, use KMS with customer-managed keys
>
> **4. Versioning**
> - Enable for protection against accidental deletion
> - Combined with MFA Delete for extra protection
>
> **5. Logging**
> - Enable server access logging
> - Use CloudTrail for API-level logging
>
> **6. IAM**
> - Least privilege for bucket access
> - Use IAM roles, not access keys
>
> **7. Monitoring**
> - Enable Macie for sensitive data discovery
> - GuardDuty for threat detection
> - Create CloudWatch alarms for suspicious activity"

---

## Q3: "What is the difference between Security Groups and NACLs?"

### ✅ MODEL ANSWER:
> "Both are firewall controls in AWS VPC, but they operate differently:
>
> | Aspect | Security Group | NACL |
> |--------|----------------|------|
> | **Level** | Instance (ENI) | Subnet |
> | **State** | Stateful | Stateless |
> | **Rules** | Allow only | Allow AND Deny |
> | **Evaluation** | All rules | Numbered order |
> | **Default** | Deny all in, allow all out | Allow all |
>
> **Stateful vs Stateless:**
> - **Security Group (Stateful)**: If you allow inbound on port 80, response traffic is automatically allowed out.
> - **NACL (Stateless)**: Must explicitly allow BOTH inbound AND outbound. If you allow inbound 80, you must separately allow outbound ephemeral ports.
>
> **When to use each:**
> - **Security Groups**: Primary firewall, per-instance rules
> - **NACLs**: Subnet-wide rules, blocking specific IPs, additional layer
>
> **Example:**
> - Use Security Group to allow web traffic to instances
> - Use NACL to block a known malicious IP range from entire subnet"

---

## Q4: "How would you detect compromised credentials in AWS?"

### ✅ MODEL ANSWER:
> "I would use multiple detection methods:
>
> **1. AWS GuardDuty (Primary)**
> - Detects unusual API calls
> - Identifies access from unusual locations
> - Flags anomalous instance behavior
>
> **2. CloudTrail Analysis**
> ```
> Look for:
> - API calls from new IP addresses
> - Unusual times (3am activity)
> - Sensitive actions (IAM changes, S3 access)
> - Console logins from unknown locations
> ```
>
> **3. IAM Access Analyzer**
> - Identifies resources shared externally
> - Finds overprivileged policies
>
> **4. CloudWatch Alarms**
> ```
> Alert on:
> - Root account usage
> - Failed login attempts
> - IAM policy changes
> - Security group changes
> ```
>
> **5. AWS Security Hub**
> - Aggregates findings from multiple services
> - Compliance checks
>
> **Response Actions:**
> - Immediately rotate credentials
> - Disable compromised access key
> - Review CloudTrail for actions taken
> - Check for persistence (new users, roles)
> - Enable MFA if not already"

---

## Q5: "What is AWS IAM and how does it work?"

### ✅ MODEL ANSWER:
> "IAM (Identity and Access Management) controls who can do what in AWS.
>
> **Components:**
>
> 1. **Users**: Individual identities (human or service)
> 2. **Groups**: Collections of users sharing permissions
> 3. **Roles**: Temporary credentials assumed by entities
> 4. **Policies**: JSON documents defining permissions
>
> **Policy Structure:**
> ```json
> {
>   \"Version\": \"2012-10-17\",
>   \"Statement\": [{
>     \"Effect\": \"Allow\",
>     \"Action\": \"s3:GetObject\",
>     \"Resource\": \"arn:aws:s3:::bucket/*\"
>   }]
> }
> ```
>
> **Types of Policies:**
> - **Identity-based**: Attached to users/groups/roles
> - **Resource-based**: Attached to resources (S3 bucket policy)
> - **Permission boundaries**: Maximum permissions limit
> - **SCPs**: Organization-level guardrails
>
> **Best Practices:**
> 1. Never use root account
> 2. MFA everywhere
> 3. Least privilege principle
> 4. Use roles over access keys
> 5. Regular access reviews
>
> **Example:**
> For an EC2 application needing S3 access:
> - Create IAM role with S3 permissions
> - Attach role to EC2 instance
> - Application uses role credentials (auto-rotated)
> - No hardcoded access keys needed"

---

## Q6: "How would you secure a Kubernetes cluster in AWS (EKS)?"

### ✅ MODEL ANSWER:
> "EKS security requires multiple layers:
>
> **1. Control Plane Security**
> - Use private endpoint (disable public access)
> - Restrict API server access with security groups
> - Enable audit logging
>
> **2. Node Security**
> - Use managed node groups (auto-patching)
> - Restrict SSH access
> - Use custom AMIs with hardening
>
> **3. Pod Security**
> - Implement Pod Security Standards
> - No privileged containers
> - Read-only root filesystem
> - Non-root users
>
> **4. Network Security**
> - Network Policies to segment pod traffic
> - Use Calico or Cilium for enforcement
> - Private subnets for nodes
>
> **5. IAM Integration**
> - IRSA (IAM Roles for Service Accounts)
> - Each pod gets minimal required permissions
> - No shared credentials
>
> **6. Secrets Management**
> - Use AWS Secrets Manager or Vault
> - Don't store secrets in ConfigMaps
> - Enable envelope encryption for etcd
>
> **7. Image Security**
> - Scan images with ECR scanning
> - Only allow trusted registries
> - Implement image signing
>
> **8. Monitoring**
> - Enable CloudWatch Container Insights
> - GuardDuty EKS protection
> - Runtime security with Falco/Sysdig"

---

## Q7: "Explain a cloud security incident you would investigate."

### ✅ MODEL ANSWER:
> "Let me walk through investigating a potential credential compromise:
>
> **Alert**: GuardDuty detects 'UnauthorizedAccess:IAMUser/ConsoleLogin' from unusual location
>
> **Investigation Steps:**
>
> **1. Validate Alert**
> ```
> Check CloudTrail for:
> - Login event details
> - Source IP geolocation
> - User agent string
> - MFA used?
> ```
>
> **2. Assess Scope**
> ```
> List all API calls by this user in last 24 hours:
> - What resources accessed?
> - Any IAM changes?
> - Data accessed/downloaded?
> - New resources created?
> ```
>
> **3. Immediate Containment**
> ```
> - Disable access key if compromised
> - Force password reset
> - Revoke active sessions
> - Don't delete user yet (preserve logs)
> ```
>
> **4. Check for Persistence**
> ```
> Look for:
> - New IAM users/roles created
> - New access keys on existing users
> - Lambda functions (backdoors)
> - EC2 instances
> ```
>
> **5. Root Cause**
> ```
> How were credentials compromised?
> - Phishing?
> - Exposed in code?
> - Device compromise?
> ```
>
> **6. Remediation**
> ```
> - Rotate all potentially exposed credentials
> - Enable MFA if not present
> - Review and tighten permissions
> - Document and report
> ```"

---

## Q8: "What is AWS Security Hub and how would you use it?"

### ✅ MODEL ANSWER:
> "AWS Security Hub is a central security dashboard that aggregates findings and checks compliance.
>
> **Key Features:**
>
> **1. Finding Aggregation**
> - Collects from GuardDuty, Inspector, Macie, Firewall Manager
> - Third-party integrations available
> - Unified view across accounts
>
> **2. Security Standards**
> - AWS Foundational Security Best Practices
> - CIS AWS Benchmarks
> - PCI-DSS
> - NIST Cybersecurity Framework
>
> **3. How I'd Use It:**
>
> **Setup:**
> ```
> 1. Enable Security Hub in all regions
> 2. Enable automated aggregation to one region
> 3. Turn on all relevant standards
> 4. Integrate with all security services
> ```
>
> **Daily Operations:**
> ```
> 1. Review critical/high severity findings
> 2. Track security score improvement
> 3. Investigate new findings
> 4. Assign findings to teams
> ```
>
> **Automation:**
> ```
> 1. EventBridge rules for critical findings
> 2. Auto-remediation for common issues
> 3. Tickets created automatically
> 4. Integration with SIEM
> ```
>
> **Benefits:**
> - Single pane of glass
> - Prioritized findings by severity
> - Compliance tracking
> - Multi-account visibility"

---

## Q9: "How do you prevent data exfiltration from cloud?"

### ✅ MODEL ANSWER:
> "Preventing data exfiltration requires multiple controls:
>
> **1. Identity & Access**
> - Least privilege access
> - MFA on all accounts
> - Regular access reviews
> - No standing admin access
>
> **2. Network Controls**
> - VPC endpoints for AWS services (traffic stays in AWS)
> - NAT Gateway logging
> - VPN required for admin access
> - Restrict internet egress
>
> **3. Data Controls**
> - Encryption with customer-managed keys
> - S3 Block Public Access
> - Bucket policies restricting external access
> - Macie for sensitive data detection
>
> **4. Monitoring**
> - CloudTrail for API logging
> - VPC Flow Logs analyzed for anomalies
> - GuardDuty for threat detection
> - CloudWatch alarms for large data transfers
>
> **5. Response**
> - Automated blocking of suspicious IPs
> - Access key disable on anomaly
> - Quarantine procedures
>
> **Example Detection:**
> ```
> Alert: S3 GetObject calls spike from 100/day to 10,000
> Investigation: CloudTrail shows bulk download
> Response: Revoke access, assess data types, report
> ```
>
> This is similar to my vulnerability scanner detecting unusual patterns - identifying what's normal and flagging deviations."

---

## Q10: "What's your experience with cloud security? How would you apply it at TCS?"

### ✅ MODEL ANSWER:
> "While I haven't worked professionally in cloud security yet, I have relevant experience:
>
> **My Background:**
>
> 1. **Google Cloud Computing Certification**
>    - Fundamental cloud concepts
>    - GCP services overview
>    - Basic security controls
>
> 2. **Projects with Cloud Elements**
>    - Char Dham Platform: Deployed on cloud with security considerations
>    - Understanding of APIs, authentication (JWT)
>
> 3. **Security Mindset**
>    - My vulnerability scanner concepts apply to cloud APIs
>    - Understanding of IAM from working with RBAC in SmartBank
>    - Cryptography knowledge applies to cloud encryption
>
> **How I'd Apply at TCS:**
>
> 1. **Quick Learning**
>    - Already familiar with security concepts
>    - Can quickly learn cloud-specific implementations
>
> 2. **Client Work**
>    - Help with cloud security assessments
>    - Identify misconfigurations
>    - Implement security controls
>
> 3. **Growth Plan**
>    - Pursue AWS Security Specialty certification
>    - Learn CSPM tools hands-on
>    - Build lab environments for practice
>
> I'm excited about cloud security because it combines my interests in security, APIs, and modern architecture."

---

# 📋 CLOUD SECURITY QUICK REFERENCE

| Concept | AWS | Azure | GCP |
|---------|-----|-------|-----|
| **Identity** | IAM | Entra ID | Cloud IAM |
| **MFA** | IAM MFA | Conditional Access | 2-Step Verification |
| **Secret Storage** | Secrets Manager | Key Vault | Secret Manager |
| **Key Management** | KMS | Key Vault | Cloud KMS |
| **VPC Firewall** | Security Groups | NSG | VPC Firewall Rules |
| **WAF** | AWS WAF | Azure WAF | Cloud Armor |
| **Threat Detection** | GuardDuty | Defender | SCC/Chronicle |
| **CSPM** | Security Hub | Defender for Cloud | Security Command Center |
| **Logging** | CloudTrail | Activity Log | Audit Logs |

---

**Document Created**: February 2026
**Priority**: ⭐⭐⭐⭐⭐ HIGH - TCS is major cloud provider
