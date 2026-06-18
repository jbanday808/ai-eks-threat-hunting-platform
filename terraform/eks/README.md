# EKS Foundation

This directory creates the Amazon EKS foundation for the `ai-eks-threat-hunting-platform` project.

The environment is fully deployed using Terraform and includes networking, Kubernetes infrastructure, container deployment support, runtime security monitoring, and GitHub Actions integration.

## Project Scope

This Terraform module creates:

* Amazon VPC
* Public Subnets
* Private Subnets
* Internet Gateway
* NAT Gateway
* Route Tables
* Amazon EKS Cluster
* Amazon EKS Managed Node Group
* IAM Roles and Policies for EKS
* Support for GitHub Actions deployment workflows
* Support for AWS GuardDuty Runtime Monitoring
* Support for Falco runtime detection
* Support for Kubernetes AI triage workloads

## Resources

| Resource                           | Purpose                                                             |
| ---------------------------------- | ------------------------------------------------------------------- |
| `aws_vpc.this`                     | Creates the Terraform-managed VPC for EKS.                          |
| `aws_subnet.public`                | Creates public subnets across Availability Zones.                   |
| `aws_subnet.private`               | Creates private subnets across Availability Zones for worker nodes. |
| `aws_internet_gateway.this`        | Provides internet connectivity for public resources.                |
| `aws_nat_gateway.this`             | Provides outbound internet access for private worker nodes.         |
| `aws_route_table.*`                | Creates public and private subnet routing.                          |
| `aws_eks_cluster.this`             | Creates the EKS control plane.                                      |
| `aws_eks_node_group.this`          | Creates the EKS managed worker nodes.                               |
| `aws_iam_role.eks_cluster`         | IAM role used by the EKS control plane.                             |
| `aws_iam_role.eks_node_group`      | IAM role used by EKS worker nodes.                                  |
| `aws_iam_role_policy_attachment.*` | Attaches required AWS-managed IAM policies.                         |

## Defaults

| Setting              | Value                                    |
| -------------------- | ---------------------------------------- |
| AWS Region           | `us-east-1`                              |
| VPC CIDR             | `10.50.0.0/16`                           |
| Availability Zones   | `2`                                      |
| EKS Cluster Name     | `ai-eks-threat-hunting-platform`         |
| Node Group Name      | `ai-eks-threat-hunting-platform-workers` |
| Worker Instance Type | `t3.medium`                              |
| Desired Nodes        | `2`                                      |
| Minimum Nodes        | `1`                                      |
| Maximum Nodes        | `3`                                      |

## Remote State

This module uses the Terraform backend created in:

```text
terraform/backend
```

Backend configuration:

```hcl
terraform {
  backend "s3" {
    bucket         = "ai-eks-threat-hunting-platform-tf-state-dev"
    key            = "eks/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ai-eks-threat-hunting-platform-tf-locks-dev"
    encrypt        = true
  }
}
```

Create the backend resources before initializing this module.

## Usage

Initialize Terraform:

```bash
cd terraform/eks

terraform init
```

Format Terraform files:

```bash
terraform fmt
```

Validate configuration:

```bash
terraform validate
```

Review planned changes:

```bash
terraform plan
```

Deploy the environment:

```bash
terraform apply
```

Automatically approve deployment:

```bash
terraform apply -auto-approve
```

## Completed Features

The following capabilities have been successfully implemented:

* Terraform Infrastructure as Code
* Amazon VPC
* Amazon EKS Cluster
* Amazon EKS Managed Node Group
* Amazon ECR Integration
* GitHub Actions CI/CD
* GitHub OIDC Authentication
* Kubernetes Deployment Automation
* AI Triage Workload Deployment
* AWS GuardDuty Runtime Monitoring
* AWS Security Agent
* Falco Runtime Detection
* MITRE ATT&CK Mapping
* Automated Incident Reporting

## kubectl Access

After the EKS cluster is created, configure kubectl:

```bash
aws eks update-kubeconfig \
  --region us-east-1 \
  --name ai-eks-threat-hunting-platform
```

Verify connectivity:

```bash
kubectl get nodes
```

Verify namespaces:

```bash
kubectl get namespaces
```

## Deployment Validation

### Verify EKS Cluster

```bash
kubectl get nodes

kubectl get namespaces
```

Expected Result:

* Worker nodes are in Ready status.
* Kubernetes system namespaces are available.

### Verify AI Triage Deployment

```bash
kubectl get deployment -n detection-lab

kubectl get pods -n detection-lab
```

Expected Result:

* AI Triage deployment exists.
* Pods are running successfully.

### Verify GuardDuty Runtime Monitoring

```bash
aws eks describe-addon \
  --cluster-name ai-eks-threat-hunting-platform \
  --addon-name aws-guardduty-agent \
  --region us-east-1
```

Expected Result:

* Add-on status is Active.

### Verify Falco Deployment

```bash
kubectl get pods -n falco
```

View Falco logs:

```bash
kubectl logs \
  -n falco \
  -l app.kubernetes.io/name=falco
```

Expected Result:

* Falco pods are running.
* Runtime security events appear in logs.

## Runtime Detection Validation

Deploy a test container:

```bash
kubectl create namespace detection-lab
```

Access the test pod:

```bash
kubectl exec -it \
$(kubectl get pods -n detection-lab -l app=nginx -o name) \
-n detection-lab -- sh
```

Generate test activity:

```bash
whoami

hostname

touch /etc/falco-test

exit
```

Review Falco detections:

```bash
kubectl logs \
-l app.kubernetes.io/name=falco \
-n falco | grep -i "shell\|etc\|nginx"
```

Expected Result:

* Falco generates runtime security alerts.

## GitHub Actions Deployment

The GitHub Actions workflow performs:

1. Terraform Validation
2. Python Validation
3. Pytest Testing
4. CodeQL Analysis
5. Trivy Filesystem Scan
6. SBOM Generation
7. Docker Build
8. Trivy Image Scan
9. Amazon ECR Push
10. Amazon EKS Deployment
11. GuardDuty Validation
12. Falco Validation

Workflow files:

```text
.github/workflows/ci.yml
.github/workflows/codeql.yml
.github/workflows/docker-build.yml
.github/workflows/security.yml
.github/workflows/deploy-eks.yml
```

## Cleanup and Resource Deletion

Review resources before deletion:

```bash
terraform plan -destroy
```

Destroy all EKS resources:

```bash
terraform destroy
```

Automatically approve deletion:

```bash
terraform destroy -auto-approve
```

## Verify Resource Removal

Verify EKS cluster removal:

```bash
aws eks list-clusters \
  --region us-east-1
```

Verify VPC removal:

```bash
aws ec2 describe-vpcs \
  --region us-east-1
```

Verify ECR repository:

```bash
aws ecr describe-repositories \
  --region us-east-1
```

## Recommended Destruction Order

Destroy Kubernetes workloads first:

```bash
kubectl delete namespace detection-lab
```

Destroy EKS infrastructure:

```bash
cd terraform/eks

terraform destroy -auto-approve
```

Destroy Terraform backend resources last:

```bash
cd ../backend

terraform destroy -auto-approve
```

## Summary

This Terraform module creates the complete Amazon EKS platform used by the AI-Powered EKS Threat Hunting & Cloud Incident Response Platform. It provides networking, Kubernetes infrastructure, deployment automation, runtime security monitoring, AI-assisted triage support, and cloud incident response capabilities.
