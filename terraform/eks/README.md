# EKS Foundation

This directory creates the Phase 2 Amazon EKS foundation for the `ai-eks-threat-hunting-platform` project.

It creates its own VPC, public subnets, private subnets, routing, NAT gateway, EKS control plane, and EKS managed node group. It does not depend on pre-existing VPC or subnet IDs in the AWS account.

## Resources

| Resource | Purpose |
| --- | --- |
| `aws_vpc.this` | Creates the Terraform-managed VPC for EKS. |
| `aws_subnet.public` | Creates public subnets across Availability Zones. |
| `aws_subnet.private` | Creates private subnets across Availability Zones for EKS worker nodes. |
| `aws_internet_gateway.this` | Provides internet routing for public subnets. |
| `aws_nat_gateway.this` | Provides outbound internet access for private worker nodes. |
| `aws_route_table.*` | Creates public and private subnet routing. |
| `aws_eks_cluster.this` | Creates the EKS control plane named `ai-eks-threat-hunting-platform`. |
| `aws_eks_node_group.this` | Creates an EKS managed node group in the Terraform-managed private subnets. |
| `aws_iam_role.eks_cluster` | IAM role assumed by the EKS control plane. |
| `aws_iam_role.eks_node_group` | IAM role assumed by EKS worker nodes. |
| `aws_iam_role_policy_attachment.*` | Attaches required AWS managed policies for EKS and worker nodes. |

## Defaults

| Setting | Value |
| --- | --- |
| AWS region | `us-east-1` |
| VPC CIDR | `10.50.0.0/16` |
| Availability Zones | `2` |
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
