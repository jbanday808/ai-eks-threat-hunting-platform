# Incident Report: Terminal Shell in Container

## Executive Summary

Falco detected a shell process running inside a Kubernetes container. This behavior can be legitimate during troubleshooting, but it can also indicate hands-on-keyboard activity by an unauthorized user or attacker.

## Detection Details

| Field | Value |
| ----- | ----- |
| Detection Rule | AI Shell Spawned Inside Container |
| Severity | Warning |
| MITRE ATT&CK | T1059 - Command and Scripting Interpreter |
| Namespace | production |
| Pod | checkout-api-6f7c9d9f9d-2k7mx |
| Container | checkout-api |
| Observed Command | sh |

## Business Impact

Interactive shell access inside a container may allow a user to inspect files, run commands, access environment variables, or perform additional actions from inside the workload.

If unauthorized, this activity could lead to data exposure, privilege escalation, or lateral movement.

## Recommended Response

1. Confirm whether the shell session was expected administrative activity.
2. Identify the user or process that initiated the session.
3. Review surrounding Kubernetes audit logs and Falco events.
4. Inspect the container for follow-on commands or suspicious file access.
5. Rotate credentials if secrets or sensitive environment variables may have been exposed.
6. Redeploy the workload from a trusted image if compromise is suspected.

## Status

Initial triage report prepared for analyst review.
