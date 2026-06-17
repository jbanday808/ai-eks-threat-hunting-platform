# Lessons Learned

This project provided practical experience building a cloud-native threat detection platform from infrastructure through runtime monitoring. The lessons below summarize the most important takeaways for cloud security, Kubernetes operations, and incident response.

## Lesson 1: Infrastructure as Code Improves Consistency

Explanation:

Terraform makes deployments repeatable and reduces manual errors. Instead of clicking through cloud consoles and hoping each environment is configured the same way, Infrastructure as Code defines the desired setup in files that can be reviewed and improved.

Business value:

Consistent infrastructure reduces downtime, improves auditability, and makes it easier for teams to collaborate.

## Lesson 2: Kubernetes Requires Strong Visibility

Explanation:

Container environments are dynamic and require monitoring tools. Pods can start, stop, move, and change quickly. Without runtime visibility, suspicious activity may happen inside containers without being noticed.

Business value:

Strong visibility helps teams understand what is happening across workloads and respond before a small issue becomes a larger incident.

## Lesson 3: Runtime Detection Complements Preventive Security

Explanation:

Preventing attacks is important, but detecting suspicious activity is equally important. Even well-designed environments can experience misconfigurations, compromised credentials, vulnerable containers, or unexpected user behavior.

Runtime detection provides another layer of defense by watching what workloads actually do.

Business value:

This improves the organization's ability to detect threats that bypass preventive controls.

## Lesson 4: MITRE ATT&CK Provides Valuable Context

Explanation:

Mapping alerts to known adversary techniques improves investigation. A raw alert may say that a shell was opened inside a container, but mapping it to MITRE ATT&CK T1059 helps explain that the behavior may relate to command execution.

Business value:

MITRE ATT&CK helps security teams communicate risk clearly and prioritize response based on known attacker behavior.

## Lesson 5: Automation Improves Security Operations

Explanation:

Automated detections help teams respond faster. Tools like Falco reduce the need for manual observation by generating alerts when suspicious behavior occurs.

Future AI-powered triage can further improve operations by summarizing alerts, adding context, and recommending response actions.

Business value:

Automation reduces repetitive work and helps analysts focus on higher-value investigation and decision-making.

## Lesson 6: Cloud Security Requires Multiple Layers

Explanation:

Security is most effective when infrastructure, networking, monitoring, and response capabilities work together. S3 encryption protects Terraform state, HTTPS protects dashboard access, Falco monitors runtime activity, and MITRE mapping improves investigation context.

Business value:

Layered security reduces reliance on any single control and improves overall resilience.

## Practical Takeaways

| Area | Takeaway |
| ---- | -------- |
| Infrastructure | Remote state and locking are essential for reliable Terraform workflows. |
| Kubernetes | Worker node networking must support application and security tool requirements. |
| Runtime Security | Detection rules should be tested with controlled activity. |
| DNS and Access | Public services should use public load balancer DNS names, not private IP addresses. |
| Documentation | Clear explanations make technical work easier for stakeholders to understand. |

## Key Skills Demonstrated

- AWS
- Terraform
- Kubernetes
- Amazon EKS
- Cloud Security
- Runtime Threat Detection
- Incident Response
- MITRE ATT&CK
- DevSecOps
- Technical Documentation

## Final Reflection

This project shows that effective cloud security requires both engineering and communication. Building the platform is important, but explaining why it matters is what turns technical work into business value.
