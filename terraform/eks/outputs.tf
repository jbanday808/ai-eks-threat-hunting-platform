output "cluster_name" {
  description = "EKS cluster name."
  value       = aws_eks_cluster.this.name
}

output "cluster_endpoint" {
  description = "EKS cluster API server endpoint."
  value       = aws_eks_cluster.this.endpoint
}

output "cluster_arn" {
  description = "EKS cluster ARN."
  value       = aws_eks_cluster.this.arn
}

output "node_group_name" {
  description = "EKS managed node group name."
  value       = aws_eks_node_group.this.node_group_name
}

output "vpc_id" {
  description = "Terraform-managed VPC ID used by the EKS cluster."
  value       = aws_vpc.this.id
}

output "public_subnet_ids" {
  description = "Terraform-managed public subnet IDs."
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Terraform-managed private subnet IDs."
  value       = aws_subnet.private[*].id
}

output "kubeconfig_command" {
  description = "Command to configure kubectl access for this EKS cluster."
  value       = "aws eks update-kubeconfig --region ${var.aws_region} --name ${aws_eks_cluster.this.name}"
}
