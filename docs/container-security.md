# Container Security

Container security in this project covers image build validation, vulnerability scanning, EKS deployment, and runtime monitoring.

## Docker image validation

The Dockerfile uses `python:3.11-slim`, copies the AI triage application into `/app`, and runs `ai-triage/triage.py` by default.

## Trivy image scan

The image workflow scans the built image with Trivy before pushing to Amazon ECR. The workflow fails on high and critical vulnerabilities.

## EKS deployment

After the image is pushed to ECR, the deploy workflow updates kubeconfig through AWS OIDC credentials, creates the `detection-lab` namespace if needed, renders the Kubernetes manifest with the new image URI, and applies the deployment.

## Runtime monitoring

Falco provides open-source Kubernetes runtime detection. AWS GuardDuty Runtime Monitoring adds AWS-native runtime visibility and managed findings. Together they support detection engineering and cloud-native incident response.
