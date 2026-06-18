# Rebuild AWS Environment

This guide rebuilds the project safely after AWS resources have been deleted. Infrastructure creation is manual. GitHub Actions validates code, scans security risk, builds the Docker image, pushes to Amazon ECR, and deploys to Amazon EKS.

## 1. Verify AWS CLI access

```bash
aws sts get-caller-identity
aws configure get region
```

Confirm the AWS identity and region before creating resources.

## 2. Recreate Terraform backend

```bash
cd terraform/backend
terraform init
terraform plan
terraform apply
```

The backend creates the S3 state bucket and DynamoDB lock table.

## 3. Recreate Amazon ECR

```bash
aws ecr create-repository \
  --repository-name "$ECR_REPOSITORY" \
  --image-scanning-configuration scanOnPush=true \
  --encryption-configuration encryptionType=AES256 \
  --region "$AWS_REGION"
```

## 4. Recreate Amazon EKS

Create a local `terraform.tfvars` from `terraform/eks/terraform.tfvars.example`, then run:

```bash
cd terraform/eks
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

Terraform apply is intentionally local and manual. It is not run from GitHub Actions.

## 5. Configure kubectl

```bash
aws eks update-kubeconfig \
  --region "$AWS_REGION" \
  --name "$EKS_CLUSTER_NAME"

kubectl get nodes
```

## 6. Install Falco

```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo update
helm upgrade --install falco falcosecurity/falco \
  --namespace falco \
  --create-namespace \
  -f falco/helm/values.yaml

kubectl get pods -n falco
```

Falco remains the open-source runtime detection layer.

## 7. Enable AWS GuardDuty

```bash
aws guardduty create-detector --enable --region "$AWS_REGION"
aws guardduty list-detectors --region "$AWS_REGION"
```

If a detector already exists, reuse it.

## 8. Enable GuardDuty Runtime Monitoring

Enable GuardDuty Runtime Monitoring for EKS from the AWS console or AWS CLI. Validate the detector:

```bash
aws guardduty get-detector \
  --detector-id "$GUARDDUTY_DETECTOR_ID" \
  --region "$AWS_REGION"
```

## 9. Deploy or validate aws-guardduty-agent

If the EKS add-on is available in the selected region:

```bash
aws eks create-addon \
  --cluster-name "$EKS_CLUSTER_NAME" \
  --addon-name aws-guardduty-agent \
  --region "$AWS_REGION"
```

Validate the agent:

```bash
aws eks describe-addon \
  --cluster-name "$EKS_CLUSTER_NAME" \
  --addon-name aws-guardduty-agent \
  --region "$AWS_REGION"

kubectl get pods -A | grep -i guardduty
```

## 10. Create GitHub OIDC provider

```bash
aws iam create-open-id-connect-provider \
  --url https://token.actions.githubusercontent.com \
  --client-id-list sts.amazonaws.com \
  --thumbprint-list 6938fd4d98bab03faadb97b34396831e3780aea1
```

If the provider already exists, keep the existing provider.

## 11. Create GitHub Actions IAM role

Create an IAM role that trusts GitHub OIDC and restricts access to this repository and the `main` branch.

Trust policy shape:

```json
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::<AWS_ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
    },
    "StringLike": {
      "token.actions.githubusercontent.com:sub": "repo:<GITHUB_OWNER>/<GITHUB_REPO>:ref:refs/heads/main"
    }
  }
}
```

Replace placeholders outside the repository. Do not commit AWS account IDs or private values.

## 12. Configure GitHub repository variables

Add these repository variables:

```text
AWS_REGION
AWS_ACCOUNT_ID
ECR_REPOSITORY
EKS_CLUSTER_NAME
AWS_ROLE_ARN
```

## 13. Validate Python locally

```bash
python3 -m py_compile ai-triage/triage.py
python3 ai-triage/triage.py
python3 -m pip install --upgrade pytest
pytest tests -v
```

## 14. Validate Terraform locally

```bash
cd terraform/backend
terraform fmt -check
terraform init -backend=false
terraform validate

cd ../eks
terraform fmt -check
terraform init -backend=false
terraform validate
```

## 15. Run Trivy filesystem scan

```bash
trivy fs --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed .
```

## 16. Generate SBOM

```bash
trivy fs --format cyclonedx --output sbom.json .
```

## 17. Build Docker image locally

```bash
docker build -t "$ECR_REPOSITORY:local" .
```

## 18. Scan Docker image locally

```bash
trivy image --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed "$ECR_REPOSITORY:local"
```

## 19. Push to GitHub

```bash
git status
git add .github/workflows Dockerfile k8s/ai-triage docs README.md
git commit -m "Add EKS DevSecOps security pipeline"
git push origin main
```

## 20. Validate GitHub Actions

Expected order:

```text
CI Validation
CodeQL
Security Scanning
Docker Build and ECR Push
Deploy to EKS
```

## 21. Validate runtime detection

```bash
kubectl get pods -n detection-lab
kubectl get pods -n falco
kubectl get pods -A | grep -i guardduty
```

Generate controlled test events only in a lab environment.

## 22. Run AI triage

```bash
python3 ai-triage/triage.py
```

## 23. Review incident reports

```bash
ls ai-triage/reports
sed -n '1,160p' ai-triage/reports/terminal-shell-report.md
```

## 24. Final checklist

- AWS CLI identity validated
- Terraform backend rebuilt
- ECR repository created
- EKS cluster rebuilt
- kubectl configured
- Falco installed
- GuardDuty enabled
- GuardDuty Runtime Monitoring enabled
- GuardDuty agent validated
- GitHub OIDC provider created
- GitHub Actions IAM role created
- GitHub repository variables configured
- Python validation completed
- Terraform validation completed
- Trivy filesystem scan completed
- SBOM generated
- Docker image built and scanned
- GitHub Actions completed
- EKS deployment validated
- Falco alerts reviewed
- GuardDuty findings reviewed
- AI triage reports generated
