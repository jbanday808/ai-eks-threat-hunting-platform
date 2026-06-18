# AWS GuardDuty Security Agent

The AWS GuardDuty security agent supports GuardDuty Runtime Monitoring for EKS workloads. It gives AWS-native visibility into runtime activity so GuardDuty can generate findings from observed workload behavior.

## Why it was added

Falco remains the open-source runtime detection layer for this project. GuardDuty Runtime Monitoring was added to show how the same EKS environment can also use AWS-native runtime detection and managed security findings.

## How it complements Falco

Falco is useful for transparent detection engineering, custom rules, and hands-on Kubernetes security validation. GuardDuty adds managed AWS detection coverage, AWS console findings, and integration with cloud incident response workflows.

## Validate the agent

```bash
aws eks describe-addon \
  --cluster-name "$EKS_CLUSTER_NAME" \
  --addon-name aws-guardduty-agent \
  --region "$AWS_REGION"

kubectl get pods -A | grep -i guardduty
```

If the add-on is not installed, confirm that GuardDuty Runtime Monitoring is enabled for the account and region.

## Incident response value

GuardDuty findings help responders understand suspicious runtime behavior from the AWS security perspective. Findings can be reviewed with Falco alerts, Kubernetes workload details, and AI-generated incident reports to support faster investigation and clearer response actions.
