# Security Controls

This document explains the security controls implemented throughout the project. Each control is described in plain language so both technical and non-technical readers can understand why it matters.

## Control Category: Infrastructure Protection

Infrastructure protection controls help secure the cloud foundation and reduce the risk of accidental or unauthorized changes.

| Security Control | Purpose | Simple Explanation | Business Benefit |
| ---------------- | ------- | ------------------ | ---------------- |
| S3 Encryption | Protect Terraform state data at rest. | Like storing important documents in a locked cabinet. | Reduces the risk of sensitive infrastructure details being exposed. |
| S3 Versioning | Preserve previous versions of Terraform state. | Like keeping a history of document changes. | Helps recover from accidental changes or corruption. |
| DynamoDB State Locking | Prevent simultaneous Terraform updates. | Like allowing only one person to edit a blueprint at a time. | Reduces deployment conflicts and protects infrastructure reliability. |
| IAM Access Controls | Limit who can access AWS resources. | Like assigning keys only to people who need specific rooms. | Supports least privilege and reduces unauthorized access risk. |

## Control Category: Network Security

Network security controls help protect how users and services connect to the platform.

| Security Control | Purpose | Simple Explanation | Business Benefit |
| ---------------- | ------- | ------------------ | ---------------- |
| Cloudflare DNS | Manage public domain resolution. | Like a public address book that points users to the correct service. | Provides cleaner access and supports stronger public DNS management. |
| AWS Load Balancer | Route external traffic to the Falcosidekick UI. | Like a secure front desk directing visitors to the right room. | Improves availability and provides a controlled entry point. |
| HTTPS Encryption | Protect communications between users and applications. | Like sealing a letter inside a secure envelope before mailing it. | Protects sensitive information from interception. |
| ACM Certificate | Provide trusted TLS certificates for HTTPS. | Like using an official identity badge for the website. | Builds trust and enables encrypted access through a recognized certificate authority. |

## Control Category: Runtime Security

Runtime security controls monitor what workloads do after they are running.

| Security Control | Purpose | Simple Explanation | Business Benefit |
| ---------------- | ------- | ------------------ | ---------------- |
| Falco Runtime Monitoring | Detect suspicious behavior in containers. | Like a security guard watching activity inside the application environment. | Helps identify threats that bypass preventive controls. |
| Threat Detection Rules | Define suspicious activity patterns. | Like a checklist of behaviors that should trigger concern. | Turns raw activity into actionable security alerts. |
| MITRE ATT&CK Mapping | Connect alerts to known attacker techniques. | Like labeling an incident with a known playbook used by attackers. | Helps analysts understand risk and prioritize investigations. |
| Kubernetes Exec Detection | Identify shell-like access into containers. | Like noticing someone manually entering a restricted workspace. | Supports early detection of hands-on-keyboard activity. |

## Control Category: Monitoring and Visibility

Monitoring controls help teams see what is happening and investigate alerts.

| Security Control | Purpose | Simple Explanation | Business Benefit |
| ---------------- | ------- | ------------------ | ---------------- |
| Falcosidekick | Receive and route Falco alerts. | Like a dispatcher that organizes security messages. | Makes alerts easier to consume and integrate with response workflows. |
| Event Dashboard | Display detections in a web interface. | Like a security operations screen showing important events. | Improves communication with analysts, engineers, and stakeholders. |
| Alert Tracking | Preserve alert details for review. | Like keeping an incident notebook for later investigation. | Supports evidence collection and continuous improvement. |
| Detection Validation | Test that alerts trigger correctly. | Like testing an alarm before relying on it in an emergency. | Builds confidence that security monitoring is working. |

## Security Control Summary

| Category | Main Value |
| -------- | ---------- |
| Infrastructure Protection | Keeps cloud deployment state secure and reliable. |
| Network Security | Protects access to public-facing services. |
| Runtime Security | Detects suspicious activity inside running workloads. |
| Monitoring and Visibility | Helps teams investigate and respond faster. |

## Overall Security Value

This project uses layered security controls. No single control solves every problem, but together they improve prevention, detection, visibility, and response.

For an organization, this approach reduces operational risk, improves security awareness, and creates a stronger foundation for cloud security operations.
