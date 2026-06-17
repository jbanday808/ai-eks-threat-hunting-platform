# Deployment Guide

This guide explains the deployment phases at a high level. It is written for technical and non-technical readers who want to understand what was built, why each phase matters, which tools were used, and how the platform supports cloud security operations.

The project demonstrates a practical path from cloud infrastructure deployment to Kubernetes runtime monitoring, threat detection validation, and AI-assisted incident reporting.

## Phase 1: Terraform Backend

### What Was Built

- S3 state storage
- DynamoDB locking
- AWS permissions for infrastructure deployment

### Why It Matters

Terraform tracks cloud infrastructure in a state file. If that state is lost, exposed, or edited by multiple people at the same time, the environment can become unreliable.

Storing state in Amazon S3 protects the infrastructure record in a central location. DynamoDB locking helps prevent two updates from happening at the same time.

### Technologies Used

- Terraform
- Amazon S3
- Amazon DynamoDB
- AWS IAM
- AWS CLI

### What Each Tool Does

| Tool | Simple Explanation |
| ---- | ------------------ |
| Terraform | Creates and manages cloud infrastructure using code. |
| Amazon S3 | Stores Terraform state files in a secure central location. |
| Amazon DynamoDB | Prevents multiple Terraform deployments from modifying infrastructure simultaneously. |
| AWS IAM | Controls permissions for infrastructure deployment. |
| AWS CLI | Allows administrators to interact with AWS services from the command line. |

### Key Commands Used

Terraform initialization:

```bash
terraform init
```

Explanation: Downloads required Terraform providers and prepares the working directory.

Terraform validation:

```bash
terraform validate
```

Explanation: Checks Terraform configuration for syntax or configuration errors.

Terraform planning:

```bash
terraform plan
```

Explanation: Shows infrastructure changes before deployment.

Terraform deployment:

```bash
terraform apply
```

Explanation: Creates AWS infrastructure resources.

AWS identity verification:

```bash
aws sts get-caller-identity
```

Explanation: Confirms the AWS account and identity being used.

### Real-World Example

This is like keeping architectural blueprints in a secure office where only one person can make changes at a time. Everyone can trust that the blueprint reflects the real building.

### Business Value

- Reduces risk from manual infrastructure changes
- Supports team collaboration
- Improves reliability and auditability
- Creates a professional foundation for future infrastructure work

## Phase 2: Amazon EKS Deployment

### What Was Built

- Amazon EKS Kubernetes cluster
- Managed worker nodes
- Kubernetes access configuration
- Cluster resource validation

### Why It Matters

Amazon EKS provides a managed Kubernetes platform for running containerized applications. Managed worker nodes provide the compute capacity that applications and security tools need.

This phase creates the environment where workloads can run and where runtime security monitoring can be deployed.

### Technologies Used

- Amazon EKS
- Kubernetes
- kubectl
- Managed Node Groups
- VPC
- EC2

### What Each Tool Does

| Tool | Simple Explanation |
| ---- | ------------------ |
| Amazon EKS | Managed Kubernetes service provided by AWS. |
| Kubernetes | Container orchestration platform used to run and manage applications. |
| kubectl | Command-line tool used to interact with Kubernetes clusters. |
| Managed Node Groups | Provide compute resources for running applications. |
| VPC | Provides network isolation and security. |
| EC2 | Hosts Kubernetes worker nodes. |

### Key Commands Used

Initialize Terraform:

```bash
terraform init
```

Explanation: Prepares the Terraform working directory for the EKS deployment.

Deploy EKS:

```bash
terraform apply
```

Explanation: Creates the Amazon EKS infrastructure and supporting AWS resources.

Update Kubernetes configuration:

```bash
aws eks update-kubeconfig --region us-east-1 --name ai-eks-threat-hunting-platform
```

Explanation: Configures local Kubernetes access so `kubectl` can connect to the EKS cluster.

View nodes:

```bash
kubectl get nodes
```

Explanation: Confirms that managed worker nodes joined the cluster successfully.

View cluster resources:

```bash
kubectl get pods -A
```

Explanation: Shows running workloads across all Kubernetes namespaces.

### Real-World Example

This is similar to adding workers to a warehouse as demand increases. The control system coordinates the work, and the workers provide the capacity to get the job done.

### Business Value

- Provides a scalable platform for cloud applications
- Reduces operational burden by using managed Kubernetes services
- Creates a realistic environment for cloud security testing
- Supports future application and detection engineering work

## Phase 3: Runtime Security

### What Was Built

- Falco runtime security monitoring
- Falcosidekick alert routing
- Falcosidekick dashboard
- Supporting components for alert visibility

### Why It Matters

Preventive controls are important, but they do not catch everything. Runtime security monitors what applications actually do after they are running.

Falco watches container behavior and detects suspicious activity such as shell access or sensitive file changes. Falcosidekick helps route those alerts, and the dashboard makes them visible for investigation.

### Technologies Used

- Falco
- Falcosidekick
- Helm
- Redis
- Kubernetes Metadata Collector

### What Each Tool Does

| Tool | Simple Explanation |
| ---- | ------------------ |
| Falco | Monitors container behavior in real time. |
| Falcosidekick | Receives and forwards security alerts. |
| Helm | Installs and manages Kubernetes applications. |
| Redis | Supports Falcosidekick UI operations. |
| Kubernetes Metadata Collector | Adds Kubernetes context to detections. |

### Key Commands Used

Add Falco Helm repository:

```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
```

Explanation: Adds the official Falco chart repository so Helm can install Falco components.

Update repositories:

```bash
helm repo update
```

Explanation: Refreshes local Helm chart information before installation.

Install Falco:

```bash
helm install falco falcosecurity/falco -n falco --create-namespace
```

Explanation: Installs Falco into a dedicated Kubernetes namespace.

View Falco pods:

```bash
kubectl get pods -n falco
```

Explanation: Confirms that Falco components are running.

View Falco logs:

```bash
kubectl logs -l app.kubernetes.io/name=falco -n falco -c falco
```

Explanation: Displays runtime security detections generated by Falco.

### Real-World Example

This is like having security cameras inside a building. Locks on the doors matter, but monitoring helps identify suspicious behavior that happens after someone is already inside.

### Business Value

- Improves visibility into running workloads
- Helps identify suspicious container behavior quickly
- Supports investigation and response workflows
- Gives stakeholders evidence that detection controls are working

## Phase 4: HTTPS and DNS

### What Was Built

- Cloudflare DNS routing
- AWS Load Balancer access
- TLS encryption
- HTTPS access to the Falcosidekick dashboard

### Why It Matters

Security dashboards need controlled and reliable access. DNS makes the dashboard easier to reach through a friendly name, while HTTPS protects communication between the user and the service.

The Falcosidekick UI was exposed through an AWS Load Balancer and connected to the custom domain `falco.caremedix.net`.

### Technologies Used

- AWS Load Balancer
- AWS Certificate Manager
- Route 53
- Cloudflare
- HTTPS
- DNS

### What Each Tool Does

| Tool | Simple Explanation |
| ---- | ------------------ |
| AWS Load Balancer | Provides secure access to the Falcosidekick dashboard. |
| AWS Certificate Manager | Manages TLS certificates. |
| Route 53 | Provides DNS validation records. |
| Cloudflare | Provides DNS routing and domain management. |
| HTTPS | Encrypts communication between users and the dashboard. |
| DNS | Allows users to access services using friendly names. |

### Key Commands Used

View services:

```bash
kubectl get svc -n falco
```

Explanation: Shows Kubernetes services, including externally exposed services for Falcosidekick access.

View ingress resources:

```bash
kubectl get ingress -A
```

Explanation: Shows ingress resources across all namespaces.

Validate DNS:

```bash
nslookup falco.caremedix.net
```

Explanation: Confirms that the public DNS name resolves correctly.

Validate HTTPS access:

```text
https://falco.caremedix.net
```

Explanation: Confirms secure access to the Falcosidekick dashboard.

### Real-World Example

This is like replacing a hard-to-remember building address with a clear office name, then requiring secure entry through the front door.

### Business Value

- Improves usability for security reviewers
- Protects dashboard access with encrypted communication
- Demonstrates real-world cloud access patterns
- Supports professional presentation for technical demos

## Phase 5: Threat Detection Validation

### What Was Tested

- Interactive shell detection
- File modification detection
- Falco alert generation
- MITRE ATT&CK technique mapping

### Why It Matters

A detection platform is only valuable if it can identify real suspicious behavior. Testing confirms that Falco rules work and that alerts appear in the monitoring workflow.

The project validated detections for terminal shell activity inside a container and file writes under `/etc`.

### Technologies Used

- Falco
- Kubernetes
- MITRE ATT&CK Framework
- Falcosidekick UI

### What Each Tool Does

| Tool | Simple Explanation |
| ---- | ------------------ |
| Falco | Detects suspicious activity. |
| Kubernetes | Provides the container environment where test activity is performed. |
| MITRE ATT&CK Framework | Provides standardized attack technique mappings. |
| Falcosidekick UI | Displays security alerts for investigation. |

### Key Commands Used

Launch interactive shell:

```bash
kubectl exec -it <pod-name> -n detection-lab -- sh
```

Explanation: Simulates command-line activity inside a container.

Create file under `/etc`:

```bash
touch /etc/test-file
```

Explanation: Simulates modification of sensitive system paths.

View Falco alerts:

```bash
kubectl logs -l app.kubernetes.io/name=falco -n falco -c falco
```

Explanation: Confirms detection generation.

### Real-World Example

This is like testing a smoke alarm with controlled smoke to confirm it actually alerts before a real emergency happens.

### Business Value

- Confirms monitoring is functioning correctly
- Demonstrates detection engineering skills
- Connects technical alerts to real attacker behaviors
- Builds confidence in the security monitoring process

## Phase 6: AI-Powered Alert Triage

### What Was Built

- Python triage engine
- Sample Falco alerts
- Automated Markdown incident reports

### Why It Matters

Security alerts can be difficult to interpret quickly, especially when teams receive many alerts at once. AI-assisted triage helps convert raw alert data into a plain-language summary, recommended response actions, and consistent incident documentation.

This phase demonstrates how automation can support security analysts by reducing repetitive investigation work and improving response consistency.

### Technologies Used

- Python
- JSON
- Markdown
- MITRE ATT&CK

### What Each Tool Does

| Tool | Simple Explanation |
| ---- | ------------------ |
| Python | Processes Falco alerts and generates reports. |
| JSON | Stores alert data. |
| Markdown | Creates portable incident reports. |
| MITRE ATT&CK | Provides attack technique context. |

### Key Commands Used

Run all alerts:

```bash
python3 ai-triage/triage.py
```

Explanation: Processes all sample alerts and generates incident reports.

Run single alert:

```bash
python3 ai-triage/triage.py ai-triage/sample-alerts/terminal-shell-t1059.json
```

Explanation: Processes one selected alert for focused validation.

Validate Python syntax:

```bash
python3 -m py_compile ai-triage/triage.py
```

Explanation: Confirms that the Python triage script is syntactically valid.

### Real-World Example

This is similar to a security analyst receiving an alert and automatically receiving a pre-written incident summary with recommended response actions.

### Business Value

- Reduces analyst workload
- Improves investigation speed
- Creates consistent incident documentation
- Demonstrates AI-assisted security operations

## Deployment Summary

| Phase | Focus | Outcome |
| ----- | ----- | ------- |
| Phase 1 | Terraform Backend | Secure Infrastructure State |
| Phase 2 | Amazon EKS | Running Kubernetes Environment |
| Phase 3 | Runtime Security | Falco Monitoring and Alerts |
| Phase 4 | HTTPS and DNS | Secure Dashboard Access |
| Phase 5 | Threat Detection Validation | MITRE ATT&CK Detection Validation |
| Phase 6 | AI Alert Triage | Automated Incident Reports |

## Overall Value

Together, these phases show how cloud infrastructure, Kubernetes, runtime detection, secure access, and AI-assisted triage can be combined into a practical threat hunting platform. The result is a portfolio project that demonstrates engineering execution, security visibility, incident response automation, and business-focused cloud security outcomes.
