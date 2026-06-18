# Cloud Incident Response

This project connects runtime detection, AI-assisted triage, investigation notes, and Markdown incident reports.

## Detection

Falco detects suspicious container behavior such as shell execution or writes to sensitive paths. GuardDuty Runtime Monitoring adds AWS-native findings for runtime activity observed in the EKS environment.

## Triage

The AI triage workflow reads Falco-style JSON alerts, extracts useful context, maps events to MITRE ATT&CK where possible, and produces a plain-English summary.

## Investigation

Analysts review the affected namespace, pod, container image, command, severity, and related AWS findings. GuardDuty findings can be used with Falco alerts to confirm whether the behavior is isolated, expected, or suspicious.

## Recommended actions

Response actions include validating the activity owner, preserving logs, reviewing deployment history, checking for follow-on commands, and redeploying from a trusted image when tampering is suspected.

## Markdown incident reports

The triage script creates Markdown incident reports in `ai-triage/reports`. Reports include the incident summary, severity, MITRE ATT&CK technique, detection rule, affected workload context, risk assessment, and recommended actions.

## AI triage workflow

```text
Falco Alert or GuardDuty Finding
-> Review Runtime Context
-> Run AI Triage
-> Investigate Workload and AWS Evidence
-> Document Recommended Actions
-> Save Markdown Incident Report
```
