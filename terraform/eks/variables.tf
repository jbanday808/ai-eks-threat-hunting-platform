variable "aws_region" {
  description = "AWS region where the EKS foundation will be created."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for naming and tagging EKS resources."
  type        = string
  default     = "ai-eks-threat-hunting-platform"
}

variable "environment" {
  description = "Environment name used for tagging EKS resources."
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the Terraform-managed EKS VPC."
  type        = string
  default     = "10.50.0.0/16"
}

variable "az_count" {
  description = "Number of Availability Zones to use for public and private EKS subnets."
  type        = number
  default     = 2

  validation {
    condition     = var.az_count >= 2
    error_message = "EKS requires at least two Availability Zones."
  }
}

variable "node_instance_types" {
  description = "EC2 instance types for EKS managed worker nodes."
  type        = list(string)
  default     = ["t3.medium"]
}

variable "node_desired_size" {
  description = "Desired number of EKS managed worker nodes."
  type        = number
  default     = 2
}

variable "node_min_size" {
  description = "Minimum number of EKS managed worker nodes."
  type        = number
  default     = 1
}

variable "node_max_size" {
  description = "Maximum number of EKS managed worker nodes."
  type        = number
  default     = 3
}
