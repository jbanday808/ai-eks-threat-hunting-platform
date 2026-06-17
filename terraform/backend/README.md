# Terraform Backend

This directory bootstraps the Terraform remote state backend for the `ai-eks-threat-hunting-platform` project.

It creates:

- An S3 bucket for Terraform state
- S3 bucket versioning
- S3 server-side encryption
- S3 public access blocking
- A TLS-only S3 bucket policy
- A DynamoDB table for Terraform state locking

This phase does not create EKS, Falco, workloads, or GitHub Actions automation.

## Resources

| Resource | Purpose |
| --- | --- |
| `aws_s3_bucket.terraform_state` | Stores Terraform state remotely. |
| `aws_s3_bucket_versioning.terraform_state` | Keeps state file versions for recovery. |
| `aws_s3_bucket_server_side_encryption_configuration.terraform_state` | Encrypts state objects at rest with SSE-S3. |
| `aws_s3_bucket_public_access_block.terraform_state` | Blocks public bucket and object access. |
| `aws_s3_bucket_policy.terraform_state` | Denies non-TLS requests to the state bucket. |
| `aws_dynamodb_table.terraform_locks` | Provides Terraform state locking with `LockID` as the partition key. |

## Defaults

| Variable | Default |
| --- | --- |
| `aws_region` | `us-east-1` |
| `project_name` | `ai-eks-threat-hunting-platform` |
| `environment` | `dev` |
| `state_bucket_name` | `ai-eks-threat-hunting-platform-tf-state-dev` |
| `lock_table_name` | `ai-eks-threat-hunting-platform-tf-locks-dev` |

S3 bucket names are globally unique. If the default bucket name is already taken, pass a unique value for `state_bucket_name`.

## Usage

Initialize and review the backend resources:

```bash
cd terraform/backend
terraform init
terraform fmt
terraform validate
terraform plan
```

If the default S3 bucket name is unavailable, use a unique bucket name:

```bash
terraform plan \
  -var="state_bucket_name=ai-eks-threat-hunting-platform-tf-state-dev-<unique-suffix>"
```

Create the backend resources only after reviewing the plan:

```bash
terraform apply
```

After the backend exists, future Terraform root modules can use an S3 backend similar to:

```hcl
terraform {
  backend "s3" {
    bucket         = "ai-eks-threat-hunting-platform-tf-state-dev"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ai-eks-threat-hunting-platform-tf-locks-dev"
    encrypt        = true
  }
}
```

Use a module-specific `key` for each future Terraform root module, such as `eks/terraform.tfstate`.
