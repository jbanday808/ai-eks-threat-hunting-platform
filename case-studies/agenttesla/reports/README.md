# AgentTesla Analysis Reports

## Overview

This folder contains the completed report set for an AgentTesla defensive investigation. The reports summarize the investigation findings, detection coverage, MITRE ATT&CK mapping, and response recommendations in a format suitable for public portfolio review.

| Field | Summary |
| --- | --- |
| Incident Severity | High |
| Investigation Type | Defensive Threat Hunting and Detection Engineering |
| Malware Family | AgentTesla with GuLoader-style delivery behavior |
| Primary Concern | Credential exposure, DNS beaconing, and FTP exfiltration |

## Report Contents

| File | Description |
| --- | --- |
| `architecture.md` | Explains the investigation flow from phishing delivery through GuLoader-style staging, AgentTesla activity, DNS beaconing, FTP exfiltration, Splunk detection, and incident response. |
| `incident-report.md` | Provides the completed incident summary, key findings, indicators of compromise, timeline, response actions, recovery steps, and lessons learned. |
| `mitre-attack.md` | Maps the observed behavior to MITRE ATT&CK tactics and techniques for defensive reporting. |
| `splunk-detection.md` | Documents Splunk hunting searches, correlation logic, alert severity guidance, and analyst response procedures. |
| `AgentTesla_Incident_Report_GitHub_Codex_VSCode_Guide.docx` | Completed source incident report used as the source of truth for the markdown reports. |

## Investigation Summary

The investigation reviewed GuLoader-style delivery behavior leading to AgentTesla activity. Evidence showed suspicious DNS beaconing, Google Drive staging indicators, FTP upload behavior, and file-name patterns associated with possible credential and contact collection.

The completed analysis used IOC validation, Zeek log review, Suricata alerting, YARA static validation, and Splunk hunting searches to document the activity and produce defensive detection content.

## Key Findings

- AgentTesla activity created a high risk of credential exposure.
- DNS and HTTP evidence showed suspicious external communication and staging indicators.
- FTP `STOR` activity suggested possible outbound exfiltration.
- Zeek analysis supported DNS, HTTP, FTP, connection, and file-transfer review.
- Suricata analysis provided network detections for suspicious domains, FTP behavior, and file-name indicators.
- YARA validation confirmed static traits associated with the controlled AgentTesla sample.
- Splunk hunting and detection searches supported analyst triage, beaconing review, FTP exfiltration detection, and IOC correlation.
- Recommended response actions included host isolation, evidence preservation, blocking suspicious infrastructure, credential resets, endpoint validation, and continued monitoring.

## Detection Coverage

| Tool / Area | Coverage |
| --- | --- |
| Zeek | Converts packet capture evidence into structured DNS, HTTP, FTP, connection, and file-transfer logs for investigation. |
| Suricata | Detects suspicious domains, FTP upload behavior, and file-name indicators using defensive network rules. |
| YARA | Validates controlled AgentTesla static indicators for defensive malware classification. |
| Splunk | Provides searches for DNS indicators, beaconing behavior, FTP exfiltration, IOC correlation, severity review, and analyst response. |
| IOC Analysis | Reviews domains, hostnames, FTP commands, file patterns, and sample hash values against the completed investigation findings. |

## MITRE ATT&CK Coverage

- Initial Access
- Execution
- Discovery
- Credential Access
- Command and Control
- Exfiltration

## Safety Notice

This repository is for defensive cybersecurity analysis only.

- No malware samples are included.
- No credentials are included.
- No sensitive information is included.
- No malware execution instructions are included.
- No offensive content is included.
