# 🔄 DEVSECOPS & CI/CD SECURITY
## TCS HackQuest Interview Guide | MEDIUM PRIORITY

---

# 🎯 PRIORITY RATING: ⭐⭐⭐ (MEDIUM)
> DevSecOps roles growing at TCS - shows modern security understanding

---

# 📋 TABLE OF CONTENTS

1. [DevSecOps Fundamentals](#devsecops-fundamentals)
2. [CI/CD Pipeline Security](#cicd-pipeline-security)
3. [Security Testing Tools](#security-testing-tools)
4. [Container Security](#container-security)
5. [Infrastructure as Code Security](#infrastructure-as-code-security)
6. [Secrets Management](#secrets-management)
7. [Secure SDLC](#secure-sdlc)
8. [Interview Questions & Answers](#interview-questions--answers)

---

# DEVSECOPS FUNDAMENTALS

## What is DevSecOps?

```
┌─────────────────────────────────────────────────────────────┐
│                    DEVSECOPS                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DevSecOps = Development + Security + Operations            │
│                                                             │
│  "Shift Left" - Integrating security from the beginning     │
│  rather than as a final gate.                               │
│                                                             │
│  Traditional Approach:                                      │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐              │
│  │ Design │→│ Code   │→│ Test   │→│Security│→ Deploy       │
│  │        │ │        │ │        │ │  Gate  │              │
│  └────────┘ └────────┘ └────────┘ └────────┘              │
│                                    ▲ Security at End        │
│                                    │ (Expensive fixes)      │
│                                                             │
│  DevSecOps Approach (Shift Left):                           │
│  ┌────────────────────────────────────────────────┐        │
│  │                 SECURITY                        │        │
│  │ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐   │        │
│  │ │ Design │→│ Code   │→│ Test   │→│ Deploy │   │        │
│  │ │  ↑     │ │   ↑    │ │   ↑    │ │   ↑    │   │        │
│  │ │Threat  │ │ SAST   │ │ DAST   │ │ Config │   │        │
│  │ │Model   │ │ SCA    │ │ Pen    │ │ Audit  │   │        │
│  │ └────────┘ └────────┘ └────────┘ └────────┘   │        │
│  └────────────────────────────────────────────────┘        │
│  ▲ Security Throughout (Early, cheaper fixes)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Why DevSecOps?

```
Cost of Fixing Vulnerabilities:

┌─────────────────────────────────────────────────────────────┐
│  Stage              │ Relative Cost │ Example              │
├─────────────────────────────────────────────────────────────┤
│  Design             │    1x         │ Fix threat model     │
│  Development        │    6x         │ Fix code before test │
│  Testing            │   15x         │ Fix after QA finds   │
│  Production         │  100x         │ Fix after breach     │
└─────────────────────────────────────────────────────────────┘

Finding security issues early saves time and money!
```

## DevSecOps Principles:

| Principle | Description |
|-----------|-------------|
| **Shift Left** | Move security earlier in SDLC |
| **Automate** | Security checks in CI/CD pipeline |
| **Continuous** | Security is ongoing, not one-time |
| **Collaborate** | Dev, Sec, and Ops work together |
| **Measure** | Track security metrics |
| **Educate** | Train developers on secure coding |

---

# CI/CD PIPELINE SECURITY

## Typical CI/CD Pipeline:

```
┌─────────────────────────────────────────────────────────────┐
│               CI/CD PIPELINE STAGES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐       │
│  │Code │───▶│Build│───▶│Test │───▶│Stage│───▶│Prod │       │
│  │     │    │     │    │     │    │     │    │     │       │
│  └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘       │
│     │          │          │          │          │          │
│  ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐       │
│  │SAST │    │SCA  │    │DAST │    │Config│    │RASP │       │
│  │Lint │    │Vuln │    │IAST │    │Audit │    │Moni-│       │
│  │Sec- │    │Scan │    │Pen  │    │Comp- │    │tor  │       │
│  │rets │    │     │    │Test │    │liance│    │     │       │
│  └─────┘    └─────┘    └─────┘    └─────┘    └─────┘       │
│                                                             │
│            SECURITY AT EVERY STAGE                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Security Gates in Pipeline:

### Stage 1: Code Commit
```yaml
# Pre-commit hooks example
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks:
      - id: detect-aws-credentials
      - id: detect-private-key
  
  - repo: https://github.com/PyCQA/bandit
    hooks:
      - id: bandit  # Python security linter

Security Checks:
├── Secrets detection (prevent hardcoded passwords)
├── Security linting
├── Dependency check (known vulnerabilities)
└── Code formatting
```

### Stage 2: Build
```yaml
# GitHub Actions example
build:
  steps:
    - name: Build application
      run: npm build
    
    - name: Run SAST scan
      uses: github/codeql-action/analyze@v2
    
    - name: Dependency scan
      uses: snyk/actions/node@master
    
    - name: Container scan (if Docker)
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: 'my-app:${{ github.sha }}'

Security Checks:
├── SAST (Static Application Security Testing)
├── SCA (Software Composition Analysis)
├── Container image scanning
└── IaC scanning (Terraform, CloudFormation)
```

### Stage 3: Test
```yaml
test:
  steps:
    - name: Run unit tests
      run: npm test
    
    - name: Run DAST scan
      uses: zaproxy/action-full-scan@v0.4.0
      with:
        target: 'https://staging.example.com'
    
    - name: Security test results
      if: failure()
      run: exit 1  # Fail pipeline on security issues

Security Checks:
├── DAST (Dynamic Application Security Testing)
├── IAST (Interactive testing)
├── API security testing
└── Penetration testing (periodic)
```

### Stage 4: Deploy
```yaml
deploy:
  steps:
    - name: Config audit
      run: ./scripts/audit-config.sh
    
    - name: Deploy to production
      run: kubectl apply -f k8s/
    
    - name: Post-deploy scan
      run: ./security/runtime-check.sh

Security Checks:
├── Configuration audit
├── Compliance check
├── Runtime protection enabled
└── Monitoring configured
```

## Pipeline Security Best Practices:

```
┌─────────────────────────────────────────────────────────────┐
│          CI/CD SECURITY BEST PRACTICES                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PROTECT THE PIPELINE                                    │
│     ├── Secure CI/CD credentials (use vault)                │
│     ├── Restrict who can modify pipelines                   │
│     ├── Sign commits and artifacts                          │
│     └── Audit pipeline changes                              │
│                                                             │
│  2. SECURE BUILD ENVIRONMENT                                │
│     ├── Use ephemeral build agents                          │
│     ├── Minimize tool access                                │
│     ├── Network isolation                                   │
│     └── Scan build images                                   │
│                                                             │
│  3. ARTIFACT SECURITY                                       │
│     ├── Sign artifacts                                      │
│     ├── Verify artifact integrity                           │
│     ├── Secure artifact storage                             │
│     └── Track artifact lineage (SBOM)                       │
│                                                             │
│  4. FAIL SECURELY                                           │
│     ├── Block deployment on critical vulns                  │
│     ├── Define break-glass procedures                       │
│     └── Document exceptions                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# SECURITY TESTING TOOLS

## SAST (Static Application Security Testing):

```
┌─────────────────────────────────────────────────────────────┐
│                        SAST                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Analyzes source code for security vulnerabilities          │
│  WITHOUT executing the program.                             │
│                                                             │
│  When: During development, at commit, in CI/CD              │
│                                                             │
│  Finds:                                                     │
│  ├── SQL Injection                                          │
│  ├── Cross-Site Scripting (XSS)                             │
│  ├── Buffer overflows                                       │
│  ├── Hardcoded secrets                                      │
│  ├── Insecure crypto                                        │
│  └── Code quality issues                                    │
│                                                             │
│  Tools:                                                     │
│  ├── SonarQube (multi-language)                             │
│  ├── Checkmarx (enterprise)                                 │
│  ├── Veracode (cloud)                                       │
│  ├── Semgrep (open source)                                  │
│  ├── CodeQL (GitHub)                                        │
│  └── Bandit (Python)                                        │
│                                                             │
│  Pros: Early detection, covers entire codebase              │
│  Cons: False positives, doesn't find runtime issues         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### SAST Example (Semgrep):
```yaml
rules:
  - id: hardcoded-password
    pattern: password = "..."
    message: "Hardcoded password detected"
    severity: ERROR
    languages: [python]
  
  - id: sql-injection
    pattern: |
      cursor.execute($SQL_QUERY % ...)
    message: "Potential SQL injection"
    severity: WARNING
```

## DAST (Dynamic Application Security Testing):

```
┌─────────────────────────────────────────────────────────────┐
│                        DAST                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Tests running application from the outside,                │
│  like an attacker would.                                    │
│                                                             │
│  When: Testing/staging environment, running against live    │
│                                                             │
│  Finds:                                                     │
│  ├── XSS (reflected, stored)                                │
│  ├── SQL Injection                                          │
│  ├── Authentication issues                                  │
│  ├── Session management flaws                               │
│  ├── Misconfiguration                                       │
│  └── OWASP Top 10 vulnerabilities                           │
│                                                             │
│  Tools:                                                     │
│  ├── OWASP ZAP (open source)                                │
│  ├── Burp Suite (commercial)                                │
│  ├── Acunetix                                               │
│  ├── Netsparker                                             │
│  └── Nikto (web server scanner)                             │
│                                                             │
│  Pros: Finds runtime issues, few false positives            │
│  Cons: Limited coverage, slower, needs running app          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## SCA (Software Composition Analysis):

```
┌─────────────────────────────────────────────────────────────┐
│                        SCA                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Identifies vulnerabilities in open-source dependencies     │
│                                                             │
│  Why Important:                                             │
│  ├── 80-90% of code is third-party libraries                │
│  ├── Log4Shell was in a common dependency                   │
│  └── Supply chain attacks increasing                        │
│                                                             │
│  What SCA Does:                                             │
│  ├── Inventory dependencies                                 │
│  ├── Match against vulnerability databases                  │
│  ├── License compliance checking                            │
│  └── Generate SBOM (Software Bill of Materials)             │
│                                                             │
│  Tools:                                                     │
│  ├── Snyk (popular, developer-friendly)                     │
│  ├── Dependabot (GitHub native)                             │
│  ├── OWASP Dependency-Check                                 │
│  ├── Trivy (container + dependencies)                       │
│  ├── npm audit (Node.js)                                    │
│  └── pip-audit (Python)                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### SBOM (Software Bill of Materials):

```json
{
  "bomFormat": "CycloneDX",
  "components": [
    {
      "name": "lodash",
      "version": "4.17.21",
      "purl": "pkg:npm/lodash@4.17.21",
      "vulnerabilities": []
    },
    {
      "name": "log4j-core",
      "version": "2.14.0",
      "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.0",
      "vulnerabilities": [
        {
          "id": "CVE-2021-44228",
          "severity": "CRITICAL"
        }
      ]
    }
  ]
}
```

## Comparison Table:

| Aspect | SAST | DAST | SCA |
|--------|------|------|-----|
| **What** | Source code | Running app | Dependencies |
| **When** | Development | Testing/Staging | Build time |
| **Speed** | Fast | Slower | Fast |
| **Coverage** | Full codebase | Accessible endpoints | All deps |
| **False positives** | Higher | Lower | Low |
| **Example tool** | SonarQube | ZAP | Snyk |

---

# CONTAINER SECURITY

## Container Security Layers:

```
┌─────────────────────────────────────────────────────────────┐
│              CONTAINER SECURITY LAYERS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    RUNTIME                            │  │
│  │  ├── Runtime protection (Falco, Sysdig)               │  │
│  │  ├── Network policies                                 │  │
│  │  └── Secrets management                               │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ▲                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  ORCHESTRATOR                         │  │
│  │  ├── Kubernetes security (RBAC, Pod Security)         │  │
│  │  ├── Admission controllers                             │  │
│  │  └── Network segmentation                              │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ▲                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    IMAGE                              │  │
│  │  ├── Image scanning (Trivy, Clair)                    │  │
│  │  ├── Base image security                              │  │
│  │  └── Image signing                                    │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ▲                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  DOCKERFILE                           │  │
│  │  ├── Secure coding practices                          │  │
│  │  ├── No secrets in image                              │  │
│  │  └── Minimal base image                               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Dockerfile Security Best Practices:

### ❌ Insecure Dockerfile:
```dockerfile
# Bad: Using latest tag
FROM ubuntu:latest

# Bad: Running as root (default)
# Bad: Copying everything
COPY . /app

# Bad: Hardcoded credentials
ENV DB_PASSWORD=secretpassword123

# Bad: Installing unnecessary packages
RUN apt-get update && apt-get install -y curl wget vim netcat

CMD ["python", "app.py"]
```

### ✅ Secure Dockerfile:
```dockerfile
# Good: Use specific version
FROM python:3.11-slim-bookworm

# Good: Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Good: Set working directory
WORKDIR /app

# Good: Copy only what's needed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Good: Drop privileges
USER appuser

# Good: Use HEALTHCHECK
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8080/health

CMD ["python", "src/app.py"]
```

## Container Image Scanning:

### Trivy Example:
```bash
# Scan container image
trivy image myapp:latest

# Sample output:
┌─────────────────────────────────────────────────────────────┐
│ Total: 23 (UNKNOWN: 0, LOW: 10, MEDIUM: 8, HIGH: 4, CRIT: 1)│
├─────────────────────────────────────────────────────────────┤
│ Library      │ Vulnerability │ Severity │ Installed │ Fixed │
├──────────────┼───────────────┼──────────┼───────────┼───────┤
│ openssl      │ CVE-2023-XXX  │ CRITICAL │ 1.1.1     │ 1.1.2 │
│ curl         │ CVE-2023-YYY  │ HIGH     │ 7.68.0    │ 7.88.0│
└─────────────────────────────────────────────────────────────┘
```

## Kubernetes Security:

### Pod Security Standards:
```yaml
# Restricted pod security (most secure)
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:1.0
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
```

### Network Policies:
```yaml
# Deny all ingress by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
  - Ingress
---
# Allow specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - port: 8080
```

---

# INFRASTRUCTURE AS CODE SECURITY

## IaC Security Scanning:

```
┌─────────────────────────────────────────────────────────────┐
│                IaC SECURITY                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Infrastructure as Code (IaC) defines infrastructure        │
│  in version-controlled templates.                           │
│                                                             │
│  Tools:                                                     │
│  ├── Terraform                                              │
│  ├── AWS CloudFormation                                     │
│  ├── Azure ARM/Bicep                                        │
│  └── Pulumi                                                 │
│                                                             │
│  Security Risks:                                            │
│  ├── Publicly accessible S3 buckets                         │
│  ├── Overly permissive security groups                      │
│  ├── Unencrypted storage                                    │
│  ├── Missing logging                                        │
│  └── Hardcoded secrets                                      │
│                                                             │
│  IaC Security Scanners:                                     │
│  ├── Checkov (popular, multi-platform)                      │
│  ├── tfsec (Terraform-focused)                              │
│  ├── Terrascan                                              │
│  ├── KICS                                                   │
│  └── Snyk IaC                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Terraform Security Example:

#### ❌ Insecure Terraform:
```hcl
# Bad: Public S3 bucket
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
  acl    = "public-read"  # Bad!
}

# Bad: Overly permissive security group
resource "aws_security_group" "web" {
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Bad! All ports open
  }
}

# Bad: No encryption
resource "aws_ebs_volume" "storage" {
  size = 100
  # encrypted = false (default)
}
```

#### ✅ Secure Terraform:
```hcl
# Good: Private S3 bucket with encryption
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
}

resource "aws_s3_bucket_public_access_block" "data" {
  bucket = aws_s3_bucket.data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

# Good: Restricted security group
resource "aws_security_group" "web" {
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]  # Internal only
  }
}

# Good: Encrypted storage
resource "aws_ebs_volume" "storage" {
  size      = 100
  encrypted = true
  kms_key_id = aws_kms_key.ebs.arn
}
```

### Checkov Scan Example:
```bash
$ checkov -d .

Check: CKV_AWS_19: "Ensure the S3 bucket has server-side encryption"
	PASSED for resource: aws_s3_bucket.data

Check: CKV_AWS_18: "Ensure the S3 bucket has access logging enabled"
	FAILED for resource: aws_s3_bucket.data
	Guide: https://docs.bridgecrew.io/docs/s3_13-enable-logging

Check: CKV_AWS_23: "Ensure every security groups rule has a description"
	FAILED for resource: aws_security_group.web
```

---

# SECRETS MANAGEMENT

## Why Secrets Management?

```
┌─────────────────────────────────────────────────────────────┐
│              SECRETS MANAGEMENT                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Secrets = Credentials, API keys, certificates, tokens      │
│                                                             │
│  WRONG Ways to Store Secrets:                               │
│  ❌ Hardcoded in source code                                │
│  ❌ In environment variables on server                      │
│  ❌ In configuration files (committed to Git)               │
│  ❌ In CI/CD pipeline logs                                  │
│  ❌ Shared via Slack/email                                  │
│                                                             │
│  RIGHT Way:                                                 │
│  ✅ Centralized secrets manager                             │
│  ✅ Dynamic secrets (short-lived)                           │
│  ✅ Encryption at rest and in transit                       │
│  ✅ Audit logging                                           │
│  ✅ Least privilege access                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Secrets Management Tools:

| Tool | Type | Best For |
|------|------|----------|
| **HashiCorp Vault** | Self-hosted | Dynamic secrets, enterprise |
| **AWS Secrets Manager** | Cloud | AWS-native |
| **Azure Key Vault** | Cloud | Azure-native |
| **GCP Secret Manager** | Cloud | GCP-native |
| **CyberArk** | Enterprise | Privileged access |

## HashiCorp Vault Example:

```bash
# Store a secret
vault kv put secret/myapp/db-creds \
    username="dbadmin" \
    password="supersecret123"

# Read a secret
vault kv get secret/myapp/db-creds

# Generate dynamic database credentials
vault read database/creds/my-role
# Returns short-lived credentials that auto-expire
```

## Secrets Detection in CI/CD:

### Tools:
- **GitLeaks** - Scan git history for secrets
- **TruffleHog** - Entropy-based detection
- **detect-secrets** - Pre-commit hook

### GitLeaks Example:
```bash
$ gitleaks detect

Finding: AWS Access Key
File: config/aws.yaml
Line: 15
Secret: AKIAIOSFODNN7EXAMPLE

Finding: Private Key
File: certs/server.key
Line: 1
```

---

# SECURE SDLC

## Secure Software Development Lifecycle:

```
┌─────────────────────────────────────────────────────────────┐
│               SECURE SDLC PHASES                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. REQUIREMENTS                                            │
│     ├── Define security requirements                        │
│     ├── Compliance requirements                             │
│     └── Risk assessment                                     │
│                                                             │
│  2. DESIGN                                                  │
│     ├── Threat modeling                                     │
│     ├── Security architecture review                        │
│     └── Secure design patterns                              │
│                                                             │
│  3. IMPLEMENTATION                                          │
│     ├── Secure coding standards                             │
│     ├── Code review (security focus)                        │
│     ├── SAST scanning                                       │
│     └── Secrets management                                  │
│                                                             │
│  4. VERIFICATION                                            │
│     ├── Security testing (DAST)                             │
│     ├── Penetration testing                                 │
│     ├── Vulnerability scanning                              │
│     └── Code analysis                                       │
│                                                             │
│  5. RELEASE                                                 │
│     ├── Final security review                               │
│     ├── Configuration audit                                 │
│     └── Deployment checklist                                │
│                                                             │
│  6. MAINTENANCE                                             │
│     ├── Patching                                            │
│     ├── Monitoring                                          │
│     ├── Incident response                                   │
│     └── Vulnerability management                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Threat Modeling (STRIDE):

```
┌─────────────────────────────────────────────────────────────┐
│                    STRIDE MODEL                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  S - Spoofing         (Identity)                            │
│      Can attacker pretend to be someone else?               │
│      → Mitigation: Strong authentication                    │
│                                                             │
│  T - Tampering        (Integrity)                           │
│      Can attacker modify data?                              │
│      → Mitigation: Input validation, checksums              │
│                                                             │
│  R - Repudiation      (Non-repudiation)                     │
│      Can attacker deny actions?                             │
│      → Mitigation: Logging, audit trails                    │
│                                                             │
│  I - Information       (Confidentiality)                    │
│      Disclosure                                             │
│      Can attacker access unauthorized data?                 │
│      → Mitigation: Encryption, access control               │
│                                                             │
│  D - Denial of Service (Availability)                       │
│      Can attacker make system unavailable?                  │
│      → Mitigation: Rate limiting, redundancy                │
│                                                             │
│  E - Elevation of     (Authorization)                       │
│      Privilege                                              │
│      Can attacker gain higher privileges?                   │
│      → Mitigation: Least privilege, input validation        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# INTERVIEW QUESTIONS & ANSWERS

---

## Q1: "What is DevSecOps and why is it important?"

### ✅ MODEL ANSWER:
> "DevSecOps integrates security into every stage of the software development lifecycle, rather than treating it as a final gate.
>
> **Key Principle: Shift Left**
> - Move security earlier in SDLC
> - Find issues when they're cheaper to fix
>
> **Why It's Important:**
>
> 1. **Cost**: Fixing bugs in design is 100x cheaper than production
> 2. **Speed**: Automated security doesn't slow releases
> 3. **Coverage**: Security checks on every commit
> 4. **Culture**: Developers own security, not just security team
>
> **In Practice:**
> ```
> Code → SAST scan → Build → Container scan → Test → DAST → Deploy
>                    ↑ Security at every stage ↑
> ```
>
> **My Experience:**
> In my Web Vulnerability Scanner project, I implemented security checks early - the scanner itself uses input validation and secure coding practices. This is the same principle as DevSecOps.
>
> **Benefits for TCS Clients:**
> - Faster secure deployments
> - Reduced security debt
> - Compliance automation
> - Fewer production vulnerabilities"

---

## Q2: "Explain the difference between SAST, DAST, and SCA."

### ✅ MODEL ANSWER:
> "These are three complementary security testing approaches:
>
> **SAST (Static Application Security Testing):**
> - Analyzes source code without executing
> - Finds: SQL injection, XSS, hardcoded secrets
> - When: Development, CI pipeline
> - Tools: SonarQube, Semgrep, CodeQL
> - Pros: Early detection, full coverage
> - Cons: Higher false positives
>
> **DAST (Dynamic Application Security Testing):**
> - Tests running application like an attacker
> - Finds: Runtime vulns, authentication issues
> - When: Staging/QA environment
> - Tools: OWASP ZAP, Burp Suite
> - Pros: Fewer false positives, realistic
> - Cons: Needs running app, slower
>
> **SCA (Software Composition Analysis):**
> - Scans third-party dependencies
> - Finds: Known CVEs in libraries
> - When: Build time, dependency updates
> - Tools: Snyk, Dependabot, npm audit
> - Example: Would have found Log4Shell
>
> **Comparison:**
>
> | Aspect | SAST | DAST | SCA |
> |--------|------|------|-----|
> | Analyzes | Your code | Running app | Dependencies |
> | Speed | Fast | Slower | Fast |
> | Coverage | Full | Accessible | All deps |
>
> **Best Practice:** Use all three in your pipeline!
>
> In my vulnerability scanner, I used ZAP-like DAST techniques for detecting SQL injection and XSS in running web apps."

---

## Q3: "What security checks would you add to a CI/CD pipeline?"

### ✅ MODEL ANSWER:
> "I'd add security gates at each stage:
>
> **1. Code Commit:**
> ```
> ├── Pre-commit hooks
> │   ├── Secrets detection (detect-secrets)
> │   └── Security linting
> └── Branch protection (require PR reviews)
> ```
>
> **2. Build Stage:**
> ```
> ├── SAST scanning (SonarQube, CodeQL)
> ├── Dependency scanning (Snyk, npm audit)
> └── License compliance check
> ```
>
> **3. Container Build (if applicable):**
> ```
> ├── Dockerfile linting
> ├── Image scanning (Trivy)
> └── Base image verification
> ```
>
> **4. Test Stage:**
> ```
> ├── DAST scanning (ZAP)
> ├── API security testing
> └── Security unit tests
> ```
>
> **5. Deploy Stage:**
> ```
> ├── IaC scanning (Checkov)
> ├── Config audit
> └── Secrets verification
> ```
>
> **Example GitHub Actions:**
> ```yaml
> - name: Run SAST
>   uses: github/codeql-action/analyze@v2
> 
> - name: Dependency scan
>   uses: snyk/actions/node@master
> 
> - name: Container scan
>   uses: aquasecurity/trivy-action@master
> ```
>
> **Fail Criteria:**
> - Critical/High vulnerabilities block deployment
> - Medium generate warnings
> - Exception process for accepted risks"

---

## Q4: "How would you secure a Docker container?"

### ✅ MODEL ANSWER:
> "Container security happens at multiple layers:
>
> **1. Dockerfile Best Practices:**
> ```dockerfile
> # Use specific, minimal base image
> FROM python:3.11-slim-bookworm
>
> # Create non-root user
> RUN useradd -r appuser
>
> # Copy only needed files
> COPY requirements.txt .
> RUN pip install --no-cache-dir -r requirements.txt
>
> # Drop privileges
> USER appuser
>
> # Never include secrets in image
> # ENV PASSWORD=secret  ❌ NEVER
> ```
>
> **2. Image Security:**
> - Scan images (Trivy, Clair)
> - Sign images (Docker Content Trust)
> - Use trusted registries
> - Pin versions (no `:latest`)
>
> **3. Runtime Security:**
> ```yaml
> securityContext:
>   runAsNonRoot: true
>   readOnlyRootFilesystem: true
>   allowPrivilegeEscalation: false
>   capabilities:
>     drop: [ALL]
> ```
>
> **4. Network Security:**
> - Use network policies
> - No host network mode
> - Service mesh (Istio) for mTLS
>
> **5. Secrets:**
> - Never bake into images
> - Use secrets management (Vault, K8s secrets)
> - Mount at runtime
>
> **Summary:**
> ```
> Minimal base → Non-root user → Scan → Sign → Runtime restrictions
> ```"

---

## Q5: "What is secrets management and why is it important?"

### ✅ MODEL ANSWER:
> "Secrets management is the secure handling of credentials, API keys, certificates, and tokens throughout their lifecycle.
>
> **Why Critical:**
> - Hardcoded secrets = #1 cause of data breaches
> - Secrets in Git history = permanent exposure
> - Leaked AWS keys = cryptocurrency miners within minutes
>
> **Wrong Ways:**
> ```python
> # DON'T DO THIS
> db_password = 'supersecret123'  # Hardcoded
> api_key = os.environ['API_KEY']  # Plain text env var
> ```
>
> **Right Way:**
> ```python
> # DO THIS - Use secrets manager
> from azure.keyvault.secrets import SecretClient
> 
> client = SecretClient(vault_url, credential)
> db_password = client.get_secret('db-password').value
> ```
>
> **Secrets Management Tools:**
> | Tool | Use Case |
> |------|----------|
> | HashiCorp Vault | Self-hosted, dynamic secrets |
> | AWS Secrets Manager | AWS native |
> | Azure Key Vault | Azure native |
>
> **Best Practices:**
> 1. **Centralized storage** - Not scattered
> 2. **Dynamic secrets** - Short-lived, auto-rotate
> 3. **Audit logging** - Who accessed what when
> 4. **Least privilege** - Minimal access
> 5. **Detection** - Pre-commit hooks catch leaks
>
> **In CI/CD:**
> - Never print secrets in logs
> - Use pipeline secrets feature
> - Scan for accidental commits (GitLeaks)"

---

## Q6: "Explain STRIDE threat modeling."

### ✅ MODEL ANSWER:
> "STRIDE is a threat modeling framework developed by Microsoft to identify potential threats in system design.
>
> **STRIDE Categories:**
>
> | Threat | Violates | Example |
> |--------|----------|---------|
> | **S**poofing | Authentication | Fake login page |
> | **T**ampering | Integrity | Modifying data in transit |
> | **R**epudiation | Non-repudiation | Denying actions taken |
> | **I**nformation Disclosure | Confidentiality | Data leak |
> | **D**enial of Service | Availability | DDoS attack |
> | **E**levation of Privilege | Authorization | User becomes admin |
>
> **How to Apply:**
>
> ```
> 1. Draw data flow diagram
> 2. For each component, ask STRIDE questions:
>    - Can someone spoof identity?
>    - Can data be tampered?
>    - Can actions be denied?
>    - Can information leak?
>    - Can service be denied?
>    - Can privileges be elevated?
> 3. Document threats and mitigations
> ```
>
> **Example - Login Page:**
> ```
> Spoofing → Phishing fake login
> Mitigation: MFA, certificate pinning
>
> Tampering → Modify password in transit
> Mitigation: HTTPS, encryption
>
> Repudiation → User denies login
> Mitigation: Audit logs
>
> Information → Password exposure
> Mitigation: Hash passwords, no plain text
>
> DoS → Brute force overload
> Mitigation: Rate limiting, CAPTCHA
>
> Elevation → SQL injection to admin
> Mitigation: Input validation, least privilege
> ```
>
> STRIDE helps ensure security is considered during design, not as an afterthought."

---

## Q7: "What is an SBOM and why is it important?"

### ✅ MODEL ANSWER:
> "SBOM stands for Software Bill of Materials - a complete inventory of all components in a software product.
>
> **What It Contains:**
> ```json
> {
>   \"component\": \"lodash\",
>   \"version\": \"4.17.21\",
>   \"license\": \"MIT\",
>   \"supplier\": \"Lodash Team\",
>   \"hash\": \"sha256:abc123...\",
>   \"dependencies\": [...]
> }
> ```
>
> **Why Important:**
>
> 1. **Security (Log4Shell Example):**
>    - When Log4Shell hit, companies scrambled
>    - Those with SBOMs quickly identified affected systems
>    - Others spent weeks doing manual inventory
>
> 2. **Compliance:**
>    - Executive Order 14028 requires SBOM for government software
>    - Regulatory requirements increasing
>
> 3. **Supply Chain Visibility:**
>    - Know what's in your software
>    - Track vulnerabilities across versions
>    - License compliance
>
> **SBOM Formats:**
> - **CycloneDX** - OWASP standard
> - **SPDX** - Linux Foundation standard
>
> **How to Generate:**
> ```bash
> # Using Syft
> syft packages myapp:latest -o cyclonedx-json > sbom.json
> 
> # Using npm
> npm sbom --sbom-format cyclonedx
> ```
>
> **In Practice:**
> - Generate SBOM during build
> - Store with release artifacts
> - Monitor for new vulnerabilities
> - Update when dependencies change
>
> SBOMs are becoming essential for software supply chain security."

---

## Q8: "How would you handle a vulnerability found by a SAST tool?"

### ✅ MODEL ANSWER:
> "I'd follow this process:
>
> **1. Triage (Is it real?):**
> ```
> ├── Read the finding description
> ├── Understand what the tool detected
> ├── Review the flagged code
> └── Determine: True positive or false positive?
> ```
>
> **2. If False Positive:**
> - Document why it's false positive
> - Add suppression with comment
> - Request rule tuning if frequent
>
> **3. If True Positive:**
> ```
> ├── Assess severity and exploitability
> ├── Check if it's in production
> ├── Create ticket/issue
> └── Prioritize based on risk
> ```
>
> **4. Fix the Vulnerability:**
> ```
> Example: SQL Injection finding
>
> Before:
> query = f\"SELECT * FROM users WHERE id = {user_id}\"
>
> After:
> query = \"SELECT * FROM users WHERE id = ?\"
> cursor.execute(query, (user_id,))
> ```
>
> **5. Verify the Fix:**
> - Re-run SAST scan
> - Add unit test to prevent regression
> - Code review
>
> **6. Document:**
> - Root cause
> - Fix applied
> - Lessons learned
>
> **Priority Matrix:**
>
> | Severity | In Production | Action |
> |----------|---------------|--------|
> | Critical | Yes | Fix immediately |
> | High | Yes | Fix within 24-48 hours |
> | Medium | No | Fix before deployment |
> | Low | No | Fix in next sprint |
>
> Key is treating security findings like bugs - track, prioritize, fix, verify."

---

## Q9: "What is a secure SDLC?"

### ✅ MODEL ANSWER:
> "A Secure SDLC integrates security activities into each phase of software development.
>
> **Phases and Security Activities:**
>
> **1. Requirements:**
> - Security requirements (authentication, encryption)
> - Compliance needs (GDPR, PCI-DSS)
> - Risk assessment
>
> **2. Design:**
> - Threat modeling (STRIDE)
> - Security architecture review
> - Attack surface analysis
>
> **3. Implementation:**
> - Secure coding standards (OWASP guidelines)
> - SAST scanning
> - Security-focused code review
> - Secrets management
>
> **4. Testing:**
> - DAST scanning
> - Penetration testing
> - Security unit tests
> - Fuzzing
>
> **5. Deployment:**
> - Configuration audit
> - Final security review
> - Change management
>
> **6. Operations:**
> - Monitoring and logging
> - Vulnerability management
> - Incident response
> - Patching
>
> **Benefits:**
> - Fewer production vulnerabilities
> - Lower remediation costs
> - Compliance evidence
> - Security culture
>
> **Example - My Web Vulnerability Scanner:**
> - Requirements: Must detect OWASP Top 10
> - Design: Modular scanner architecture
> - Implementation: Input validation, no hardcoded creds
> - Testing: Tested against intentionally vulnerable apps
> - Deployment: Documented secure configuration
>
> Key is making security continuous, not a one-time gate."

---

## Q10: "What tools would you recommend for a new DevSecOps pipeline?"

### ✅ MODEL ANSWER:
> "Here's my recommended toolchain by category:
>
> **SAST (Code Scanning):**
> | Tool | Cost | Best For |
> |------|------|----------|
> | Semgrep | Free | Flexible rules |
> | SonarQube | Free/Paid | Multi-language |
> | CodeQL | Free (GitHub) | Deep analysis |
>
> **DAST (App Testing):**
> | Tool | Cost | Best For |
> |------|------|----------|
> | OWASP ZAP | Free | CI/CD integration |
> | Burp Suite | Paid | Manual testing |
>
> **SCA (Dependencies):**
> | Tool | Cost | Best For |
> |------|------|----------|
> | Snyk | Free tier | Developer-friendly |
> | Dependabot | Free | GitHub native |
> | OWASP Dep-Check | Free | On-premises |
>
> **Container Security:**
> | Tool | Cost | Best For |
> |------|------|----------|
> | Trivy | Free | All-in-one scanning |
> | Grype | Free | Fast scanning |
>
> **IaC Scanning:**
> | Tool | Cost | Best For |
> |------|------|----------|
> | Checkov | Free | Multi-platform |
> | tfsec | Free | Terraform focus |
>
> **Secrets Detection:**
> | Tool | Cost | Best For |
> |------|------|----------|
> | GitLeaks | Free | Pre-commit |
> | TruffleHog | Free | Git history |
>
> **For a Starter Pipeline:**
> ```yaml
> - Pre-commit: detect-secrets, semgrep
> - Build: Snyk, Trivy
> - Test: ZAP
> - IaC: Checkov
> ```
>
> Start with free tools, add commercial ones as scale requires."

---

# 📋 DEVSECOPS QUICK REFERENCE

## CI/CD Security Checklist:
```
□ Secrets detection in commits
□ SAST scanning on code
□ Dependency vulnerability scanning
□ Container image scanning
□ IaC security scanning
□ DAST in staging
□ Configuration audit
□ Signed artifacts
□ Access controls on pipeline
□ Audit logging enabled
```

## Secure Dockerfile Template:
```dockerfile
FROM image:specific-version
RUN useradd -r appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
USER appuser
HEALTHCHECK CMD curl -f http://localhost/health
CMD ["app"]
```

---

**Document Created**: February 2026
**Priority**: ⭐⭐⭐ MEDIUM - Shows modern security expertise
