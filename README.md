# AI-Powered EKS Threat Hunting & Cloud Incident Response Platform

## Executive Summary

This completed portfolio project demonstrates a cloud security and DevSecOps platform for Amazon EKS. It securely builds, scans, deploys, and monitors a containerized threat-triage workload while producing evidence that supports investigation and incident response.

The platform was built to demonstrate practical cloud security, Kubernetes security, threat detection, threat hunting, incident response, and DevSecOps automation. It combines secure CI/CD, Infrastructure as Code, software supply chain controls, runtime monitoring, MITRE ATT&CK mapping, and AI-assisted security operations in one repeatable workflow.

## Architecture Diagrams

### Figure 1

![Figure 1. High-Level Architecture](img/aiagent/ai-eks-threat-hunting-platform-diagram-v2.png)

Figure 1. High-level view of the platform showing CI/CD, security validation, runtime detection, AI triage, and incident response.

### Figure 2

![Figure 2. Detailed DevSecOps Architecture](img/aiagent/ai-eks-threat-hunting-platform-detailed-diagram.png)

Figure 2. Detailed workflow from secure software delivery through EKS monitoring, triage, and response.

## Architecture Workflow

```text
Git Push
→ GitHub Actions
→ OIDC Authentication
→ Terraform Validation
→ Python Validation
→ Pytest
→ CodeQL
→ Trivy Filesystem Scan
→ SBOM Generation
→ Docker Build
→ Trivy Image Scan
→ Amazon ECR
→ Amazon EKS
→ AWS Security Agent
→ GuardDuty Runtime Monitoring
→ AI Threat Triage
→ Cloud Incident Response
```

## Security Outcomes

This project demonstrates:

- Cloud Security Engineering
- Kubernetes Security
- Threat Detection
- Threat Hunting
- Detection Engineering
- Runtime Monitoring
- Incident Response
- DevSecOps Automation
- AI-Assisted Security Operations

The platform validates secure software delivery, runtime threat detection, automated triage, and cloud incident response workflows within Amazon EKS.

### Security Frameworks and Methodologies

This project demonstrates practical application of:

- MITRE ATT&CK Framework
- Threat Hunting Methodologies
- Detection Engineering
- Incident Response
- DevSecOps Security Controls
- Software Supply Chain Security
- Runtime Threat Detection
- Cloud Security Best Practices

These frameworks and methodologies supported detection, investigation, triage, and response activities throughout the project.

## Case Studies

These case studies demonstrate hands-on malware analysis, threat hunting, detection engineering, IOC enrichment, MITRE ATT&CK mapping, Splunk investigations, and incident response documentation.

### Remcos RAT Investigation

Completed malware analysis and threat hunting investigation covering:

- Static Analysis
- Dynamic Analysis
- IOC Enrichment
- Threat Intelligence
- MITRE ATT&CK Mapping
- Splunk Threat Hunting Dashboard
- Detection Engineering
- Incident Response Documentation

[View the Remcos RAT Case Study](case-studies/remcos/)

### Agent Tesla Investigation

Completed malware analysis and detection engineering investigation covering:

- Network Traffic Analysis
- Zeek Analysis
- Suricata Detection
- YARA Detection
- Threat Intelligence
- IOC Development
- Splunk Detection Engineering

[View the Agent Tesla Case Study](case-studies/agenttesla/)

## Technology Stack

| Technology | Purpose |
| --- | --- |
| AWS | Cloud platform |
| Amazon EKS | Kubernetes platform |
| Terraform | Infrastructure as Code |
| GitHub Actions | CI/CD automation |
| GitHub OIDC | Secure AWS authentication |
| Docker | Containerization |
| Python | Threat triage automation |
| Falco | Runtime threat detection |
| GuardDuty Runtime Monitoring | AWS-native runtime monitoring |
| MITRE ATT&CK | Threat mapping |

## Key Capabilities

- Secure AWS authentication using GitHub OIDC
- Infrastructure as Code with Terraform
- Automated CI/CD using GitHub Actions
- Container security scanning with CodeQL and Trivy
- SBOM generation and software supply chain validation
- Amazon EKS deployment automation
- Falco runtime threat detection
- AWS GuardDuty Runtime Monitoring
- AI-assisted threat triage
- Automated incident report generation

## Validation Highlights

### Amazon EKS Deployment

![Amazon EKS Deployment](img/aiagent/deploy-ai-triage-workload-success.png)

This workflow confirms successful deployment of the AI triage workload to Amazon EKS, validating the automated delivery process.

### GitHub Actions Automation

![GitHub Actions Automation](img/aiagent/github-workflow.png)

This view demonstrates automated testing, security validation, image builds, and deployment workflows that support consistent DevSecOps operations.

### GuardDuty Runtime Monitoring

![GuardDuty Runtime Monitoring](img/aiagent/aws-guard-duty-agent.png)

This view confirms the AWS Security Agent is healthy, providing the runtime visibility required for GuardDuty monitoring on EKS worker nodes.

### Falco Runtime Detection

![Falco Runtime Detection](img/aiagent/falco-detection-evidence.png)

This alert demonstrates Falco detecting suspicious shell activity inside a container, validating Kubernetes runtime detection coverage.

### AI Threat Triage

![AI Threat Triage](img/aiagent/python-ai-triage-reports.png)

This output demonstrates automated conversion of security alerts into structured incident reports, reducing manual triage effort.

## Documentation

| Document | Purpose |
| --- | --- |
| [Architecture](docs/architecture.md) | Current architecture, workflow, and validation evidence. |
| [Rebuild AWS Environment](docs/rebuild-aws-environment.md) | Safe end-to-end rebuild guide. |
| [DevSecOps Security Automation](docs/devsecops-security-automation.md) | CI/CD, OIDC, scanning, build, push, and deploy workflow. |
| [Software Supply Chain Security](docs/software-supply-chain-security.md) | SBOM, dependency scanning, image scanning, and deployment trust. |
| [Container Security](docs/container-security.md) | Docker, EKS deployment, Falco, and GuardDuty. |
| [AWS GuardDuty Security Agent](docs/aws-security-agent.md) | GuardDuty agent purpose, validation, and response value. |
| [Cloud Incident Response](docs/cloud-incident-response.md) | Detection, triage, investigation, recommendations, and reports. |

## Repository Structure

| Path | Purpose |
| --- | --- |
| `.github/workflows` | DevSecOps automation workflows. |
| `ai-triage` | Python alert triage and incident report generation. |
| `docs` | Architecture and security documentation. |
| `falco` | Falco Helm values and custom runtime detection rules. |
| `k8s/ai-triage` | Kubernetes deployment manifest for the AI triage workload. |
| `terraform/backend` | Terraform backend resources for state and locking. |
| `terraform/eks` | Amazon EKS and Terraform-managed VPC infrastructure. |
| `tests` | Pytest validation for the AI triage workflow. |

## References

See supporting documentation for complete references:

- [Architecture](docs/architecture.md)
- [Cloud Incident Response](docs/cloud-incident-response.md)
- [DevSecOps Security Automation](docs/devsecops-security-automation.md)
- [Software Supply Chain Security](docs/software-supply-chain-security.md)

## Author

James Banday

Threat Hunter | Cyber Intrusion Analyst | Cloud Security | Kubernetes | DevSecOps | Incident Response

GitHub:
https://github.com/jbanday808/ai-eks-threat-hunting-platform/tree/main

LinkedIn:
https://www.linkedin.com/in/james-allen-morta-banday-62a391128/

This project demonstrates practical cloud security, Kubernetes security, DevSecOps automation, threat detection, threat hunting, malware analysis, incident response, and AI-assisted security operations within Amazon EKS.

The portfolio showcases hands-on experience with cloud-native security, detection engineering, malware investigations, threat intelligence, Splunk-based threat hunting, runtime monitoring, and incident response workflows used by modern security operations teams.
