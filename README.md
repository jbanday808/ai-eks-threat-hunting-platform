# AI-Powered EKS DevSecOps Threat Hunting and Incident Response Platform

This project demonstrates a portfolio-ready cloud security platform for Amazon EKS. It combines Terraform, GitHub Actions, GitHub OIDC, CodeQL, Trivy, SBOM generation, Docker, Amazon ECR, Amazon EKS, Falco, AWS GuardDuty Runtime Monitoring, AI alert triage, and cloud incident response documentation.

The goal is to show how cloud teams can validate code, scan containers, deploy to Kubernetes, detect runtime threats, and generate clear incident response reports without committing secrets or using long-term AWS access keys.

## Architecture Flow

```text
Git Push
-> GitHub Actions
-> GitHub OIDC Authentication
-> Terraform Validation
-> Python Validation
-> Python Test Validation
-> CodeQL Static Analysis
-> Trivy Filesystem Scan
-> SBOM Generation
-> Docker Build
-> Trivy Container Image Scan
-> Amazon ECR
-> Amazon EKS
-> Falco Runtime Detection
-> AWS GuardDuty Security Agent
-> GuardDuty Runtime Findings
-> Cloud Incident Response
```

## GitHub Actions CI/CD

- `ci.yml` validates Python, runs the AI triage script, runs pytest, and validates Terraform formatting and configuration.
- `codeql.yml` runs CodeQL static analysis for Python and uploads results to GitHub code scanning.
- `security.yml` runs a Trivy filesystem scan, fails on high and critical vulnerabilities, generates a CycloneDX SBOM, and uploads `sbom.json`.
- `docker-build.yml` uses GitHub OIDC to authenticate to AWS, builds the Docker image, scans it with Trivy, and pushes it to Amazon ECR.
- `deploy-eks.yml` runs after the Docker workflow succeeds, updates kubeconfig, deploys the image to Amazon EKS, and validates Falco and GuardDuty runtime visibility when installed.

Terraform infrastructure creation remains manual. The pipeline validates Terraform but does not run `terraform apply`.

## Security Capabilities

| Capability | Tooling | Value |
| ---------- | ------- | ----- |
| Short-lived AWS authentication | GitHub OIDC and IAM role assumption | Avoids long-term AWS access keys |
| Infrastructure validation | Terraform fmt, init, validate | Catches configuration issues before deployment |
| Python validation | Python compile, runtime execution, pytest | Validates the AI triage workflow |
| Static analysis | CodeQL | Detects insecure code patterns |
| Filesystem scanning | Trivy | Finds high and critical vulnerabilities in the repository |
| SBOM generation | CycloneDX SBOM through Trivy | Documents software components for supply chain review |
| Container build | Docker | Packages the AI triage workload |
| Image scanning | Trivy image scan | Blocks vulnerable images before ECR push |
| Registry | Amazon ECR | Stores approved container images |
| Kubernetes runtime | Amazon EKS | Runs the detection-lab workload |
| Open-source runtime detection | Falco | Detects suspicious container behavior |
| AWS-native runtime detection | GuardDuty Runtime Monitoring | Adds managed AWS runtime findings |
| Incident response | AI triage and Markdown reports | Converts alerts into response-ready documentation |

## AI Alert Triage

The AI triage engine reads Falco-style JSON alerts, extracts runtime context, maps alerts to MITRE ATT&CK when possible, recommends response actions, and writes Markdown incident reports.

Run locally:

```bash
python3 -m py_compile ai-triage/triage.py
python3 ai-triage/triage.py
```

Generated reports are saved under:

```text
ai-triage/reports
```

## Runtime Detection

Falco remains the open-source runtime detection layer. It supports transparent Kubernetes detection engineering and custom rule validation.

AWS GuardDuty Runtime Monitoring adds AWS-native runtime visibility through the GuardDuty security agent and managed findings. GuardDuty findings can be reviewed with Falco alerts during incident response.

## Rebuild Guide

AWS resources were previously deleted, so the environment should be rebuilt deliberately from local commands and AWS console or CLI steps.

Start here:

[Rebuild AWS Environment](docs/rebuild-aws-environment.md)

## Documentation

| Document | Purpose |
| -------- | ------- |
| [Rebuild AWS Environment](docs/rebuild-aws-environment.md) | Safe end-to-end rebuild guide |
| [DevSecOps Security Automation](docs/devsecops-security-automation.md) | GitHub Actions, OIDC, scanning, build, push, and deploy workflow |
| [Software Supply Chain Security](docs/software-supply-chain-security.md) | SBOM, dependency scanning, image scanning, and deployment trust |
| [Container Security](docs/container-security.md) | Docker image validation, EKS deployment, Falco, and GuardDuty |
| [AWS GuardDuty Security Agent](docs/aws-security-agent.md) | GuardDuty agent purpose, validation, and incident response value |
| [Cloud Incident Response](docs/cloud-incident-response.md) | Detection, triage, investigation, recommendations, and reports |
| [Falco Runtime Detection](docs/falco-runtime-detection.md) | Existing Falco runtime detection notes |

## Repository Structure

| Path | Purpose |
| ---- | ------- |
| `.github/workflows` | DevSecOps automation workflows |
| `ai-triage` | Python alert triage and incident report generation |
| `docs` | Rebuild, security automation, supply chain, container, GuardDuty, and incident response documentation |
| `falco` | Falco Helm values and custom runtime detection rules |
| `k8s/ai-triage` | Kubernetes deployment manifest for the AI triage workload |
| `terraform/backend` | Terraform backend resources for state and locking |
| `terraform/eks` | Amazon EKS infrastructure configuration |

## Local Validation

```bash
python3 -m py_compile ai-triage/triage.py
python3 ai-triage/triage.py
python3 -m pip install --upgrade pytest
pytest tests -v

cd terraform/backend
terraform fmt -check
terraform init -backend=false
terraform validate

cd ../eks
terraform fmt -check
terraform init -backend=false
terraform validate
```

## Required GitHub Repository Variables

```text
AWS_REGION
AWS_ACCOUNT_ID
ECR_REPOSITORY
EKS_CLUSTER_NAME
AWS_ROLE_ARN
```

These values are configured in GitHub repository settings. They are not committed to the repository.

## Portfolio Summary

This project demonstrates practical skills in AWS cloud security, Amazon EKS, Kubernetes, Terraform, GitHub Actions, GitHub OIDC, CodeQL, Trivy, SBOM generation, Docker, Amazon ECR, Falco runtime detection, AWS GuardDuty Runtime Monitoring, AI-assisted triage, and cloud incident response.

## Author

James Banday

Cloud Security | Kubernetes | DevSecOps | Threat Detection | Incident Response

LinkedIn:
[https://www.linkedin.com/in/james-allen-morta-banday-62a391128/](https://www.linkedin.com/in/james-allen-morta-banday-62a391128/)

GitHub:
[https://github.com/jbanday808/ai-eks-threat-hunting-platform](https://github.com/jbanday808/ai-eks-threat-hunting-platform)
