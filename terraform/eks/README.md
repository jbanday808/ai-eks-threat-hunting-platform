# EKS Foundation

This directory creates the Phase 2 Amazon EKS foundation for the `ai-eks-threat-hunting-platform` project.

It reuses the existing AWS VPC and subnet IDs provided for the project. It does not create, delete, or modify the VPC.

## Resources

| Resource | Purpose |
| --- | --- |
| `aws_eks_cluster.this` | Creates the EKS control plane named `ai-eks-threat-hunting-platform`. |
| `aws_eks_node_group.this` | Creates an EKS managed node group in the existing private subnets. |
| `aws_iam_role.eks_cluster` | IAM role assumed by the EKS control plane. |
| `aws_iam_role.eks_node_group` | IAM role assumed by EKS worker nodes. |
| `aws_iam_role_policy_attachment.*` | Attaches required AWS managed policies for EKS and worker nodes. |

## Existing AWS Resources

| Name | Value |
| --- | --- |
| VPC ID | `vpc-0b7f09564a1afc93e` |
| Private subnets | `subnet-0004aa53c6d591fce`, `subnet-0ef16951aac00ad50` |
| Public subnets | `subnet-0dacf6eeb8374b21f`, `subnet-01aad51c5b7017fba` |
| Application security group | `sg-017d7df603788fa47` |

## Defaults

| Setting | Value |
| --- | --- |
| AWS region | `us-east-1` |
| EKS cluster name | `ai-eks-threat-hunting-platform` |
| Node group name | `ai-eks-threat-hunting-platform-workers` |
| Worker instance type | `t3.medium` |
| Desired nodes | `2` |
| Minimum nodes | `1` |
| Maximum nodes | `3` |

## Remote State

This root module uses the S3 backend created in `terraform/backend`:

```hcl
bucket         = "ai-eks-threat-hunting-platform-tf-state-dev"
key            = "eks/terraform.tfstate"
region         = "us-east-1"
dynamodb_table = "ai-eks-threat-hunting-platform-tf-locks-dev"
encrypt        = true
```

Create the backend resources before initializing this directory.

## Usage

```bash
cd terraform/eks
terraform init
terraform fmt
terraform validate
terraform plan
```

After reviewing the plan:

```bash
terraform apply
```

## kubectl Access

After the EKS cluster is created, configure `kubectl`:

```bash
aws eks update-kubeconfig --region us-east-1 --name ai-eks-threat-hunting-platform
```

Then verify access:

```bash
kubectl get nodes
kubectl get namespaces
```

This phase does not deploy Falco, Kubernetes workloads, or GitHub Actions automation.
