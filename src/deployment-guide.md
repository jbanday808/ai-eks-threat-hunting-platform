# Deployment Guide

This guide explains the deployment phases at a high level. It is written for technical and non-technical readers who want to understand what was built, why each phase matters, and how the platform supports cloud security operations.

## Phase 1: Terraform Backend

### What Was Built

- S3 state storage
- DynamoDB locking

### Why It Matters

Terraform tracks cloud infrastructure in a state file. If that state is lost, exposed, or edited by multiple people at the same time, the environment can become unreliable.

Storing state in Amazon S3 protects the infrastructure record in a central location. DynamoDB locking helps prevent two updates from happening at the same time.

### Real-World Example

This is like keeping architectural blueprints in a secure office where only one person can make changes at a time. Everyone can trust that the blueprint reflects the real building.

### Business Value

- Reduces risk from manual infrastructure changes
- Supports team collaboration
- Improves reliability and auditability
- Creates a professional foundation for future infrastructure work

## Phase 2: Amazon EKS Deployment

### What Was Built

- Kubernetes cluster
- Managed worker nodes

### Why It Matters

Amazon EKS provides a managed Kubernetes platform for running containerized applications. Managed worker nodes provide the compute capacity that applications and security tools need.

This phase creates the environment where workloads can run and where runtime security monitoring can be deployed.

### Real-World Example

This is similar to adding workers to a warehouse as demand increases. The control system coordinates the work, and the workers provide the capacity to get the job done.

### Business Value

- Provides a scalable platform for cloud applications
- Reduces operational burden by using managed Kubernetes services
- Creates a realistic environment for cloud security testing
- Supports future application and detection engineering work

## Phase 3: Runtime Security

### What Was Built

- Falco
- Falcosidekick
- Dashboard

### Why It Matters

Preventive controls are important, but they do not catch everything. Runtime security monitors what applications actually do after they are running.

Falco watches container behavior and detects suspicious activity such as shell access or sensitive file changes. Falcosidekick helps route those alerts, and the dashboard makes them visible for investigation.

### Real-World Example

This is like having security cameras inside a building. Locks on the doors matter, but monitoring helps identify suspicious behavior that happens after someone is already inside.

### Business Value

- Improves visibility into running workloads
- Helps identify suspicious container behavior quickly
- Supports investigation and response workflows
- Gives stakeholders evidence that detection controls are working

## Phase 4: HTTPS and DNS

### What Was Built

- Cloudflare DNS
- AWS Load Balancer
- TLS encryption

### Why It Matters

Security dashboards need controlled and reliable access. DNS makes the dashboard easier to reach through a friendly name, while HTTPS protects communication between the user and the service.

The Falcosidekick UI was exposed through an AWS Load Balancer and connected to the custom domain `falco.caremedix.net`.

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

### Why It Matters

A detection platform is only valuable if it can identify real suspicious behavior. Testing confirms that Falco rules work and that alerts appear in the monitoring workflow.

The project validated detections for terminal shell activity inside a container and file writes under `/etc`.

### Real-World Example

This is like testing a smoke alarm with controlled smoke to confirm it actually alerts before a real emergency happens.

### Business Value

- Confirms monitoring is functioning correctly
- Demonstrates detection engineering skills
- Connects technical alerts to real attacker behaviors
- Builds confidence in the security monitoring process

## Deployment Summary

| Phase | Focus | Outcome |
| ----- | ----- | ------- |
| Phase 1 | Terraform backend | Secure and reliable infrastructure state |
| Phase 2 | EKS deployment | Running Kubernetes environment |
| Phase 3 | Runtime security | Falco detections and dashboard visibility |
| Phase 4 | HTTPS and DNS | Secure external access to the dashboard |
| Phase 5 | Detection validation | Confirmed runtime threat alerts |

## Overall Value

Together, these phases show how cloud infrastructure, Kubernetes, runtime detection, and secure access can be combined into a practical threat hunting platform. The result is a portfolio project that demonstrates both engineering execution and security-focused business outcomes.
