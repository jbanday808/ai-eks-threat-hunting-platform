# Incident Report: File Write Under /etc

## Executive Summary

Falco detected a file write under `/etc` inside a Kubernetes container. The `/etc` directory commonly stores system and application configuration files, so unexpected writes in this location may indicate tampering or persistence behavior.

## Detection Details

| Field | Value |
| ----- | ----- |
| Detection Rule | AI Write Under Etc In Container |
| Severity | Warning |
| MITRE ATT&CK | T1037 - Boot or Logon Initialization Scripts |
| Namespace | production |
| Pod | checkout-api-6f7c9d9f9d-2k7mx |
| Container | checkout-api |
| File Path | /etc/falco-phase3-test |
| Observed Command | sh -c echo test > /etc/falco-phase3-test |

## Business Impact

Unexpected changes under `/etc` can affect application behavior, weaken security settings, or support persistence. In a production workload, this activity should be reviewed even if the container is expected to be short-lived.

If unauthorized, this activity may indicate that an attacker is attempting to modify configuration or prepare the environment for further actions.

## Recommended Response

1. Confirm whether the file write was part of an approved test or deployment process.
2. Review the modified path and compare it against the expected container baseline.
3. Check for additional file writes, shell activity, or privilege escalation attempts.
4. Inspect the container image and deployment configuration.
5. Redeploy the workload from a trusted image if the change was unauthorized.
6. Preserve Falco alerts and Kubernetes logs for incident documentation.

## Status

Initial triage report prepared for analyst review.
