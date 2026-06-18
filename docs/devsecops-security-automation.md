# DevSecOps Security Automation

This project uses GitHub Actions to validate code, scan security risk, build a Docker image, publish the image to Amazon ECR, and deploy the workload to Amazon EKS.

## Pipeline flow

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

## GitHub Actions

- `ci.yml` validates Python and Terraform.
- `codeql.yml` runs GitHub CodeQL static analysis for Python.
- `security.yml` runs a Trivy filesystem scan and generates a CycloneDX SBOM.
- `docker-build.yml` builds, scans, and pushes the image to Amazon ECR.
- `deploy-eks.yml` deploys the scanned image to Amazon EKS after the image workflow succeeds.

## OIDC authentication

GitHub Actions uses OpenID Connect to request short-lived AWS credentials. This avoids long-term AWS access keys and keeps authentication tied to the repository, branch, and IAM role trust policy.

## Security value

CodeQL reviews Python code for insecure patterns. Trivy scans the repository and container image for high and critical vulnerabilities. The SBOM documents the software components in the project. Deployment happens only after the image build and image scan complete successfully.

Terraform apply is kept manual so infrastructure changes remain deliberate and reviewable.
