variable "aws_region" {
  description = "AWS region where the Terraform backend resources will be created."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for naming and tagging backend resources."
  type        = string
  default     = "ai-eks-threat-hunting-platform"
}

variable "environment" {
  description = "Environment name used for tagging backend resources."
  type        = string
  default     = "dev"
}

variable "state_bucket_name" {
  description = "Globally unique S3 bucket name for Terraform remote state."
  type        = string
  default     = "ai-eks-threat-hunting-platform-tf-state-dev"

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$", var.state_bucket_name))
    error_message = "The state bucket name must be a valid S3 bucket name using lowercase letters, numbers, dots, and hyphens."
  }
}

variable "lock_table_name" {
  description = "DynamoDB table name for Terraform state locking."
  type        = string
  default     = "ai-eks-threat-hunting-platform-tf-locks-dev"
}
