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

variable "vpc_id" {
  description = "Existing VPC ID where the EKS cluster will run."
  type        = string
  default     = "vpc-0b7f09564a1afc93e"
}

variable "private_subnet_ids" {
  description = "Existing private subnet IDs for the EKS managed node group."
  type        = list(string)
  default = [
    "subnet-0004aa53c6d591fce",
    "subnet-0ef16951aac00ad50"
  ]
}

variable "public_subnet_ids" {
  description = "Existing public subnet IDs available to the EKS control plane."
  type        = list(string)
  default = [
    "subnet-0dacf6eeb8374b21f",
    "subnet-01aad51c5b7017fba"
  ]
}

variable "application_security_group_id" {
  description = "Existing application security group ID to associate with the EKS control plane."
  type        = string
  default     = "sg-017d7df603788fa47"
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
