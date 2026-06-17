terraform {
  required_version = ">= 1.6.0"

  backend "s3" {
    bucket         = "ai-eks-threat-hunting-platform-tf-state-dev"
    key            = "eks/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ai-eks-threat-hunting-platform-tf-locks-dev"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.50"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = local.common_tags
  }
}
