# Detecting Beaconing Malware - AgentTesla

## Project Overview

This case study documents a defensive investigation of AgentTesla activity associated with GuLoader-style delivery behavior. The investigation used a completed incident report, packet capture review, Zeek logs, Suricata alerts, YARA results, IOC analysis, and Splunk-style searches to explain what happened and how defenders can detect similar behavior.

AgentTesla is an information-stealing malware family. In this case, the main concern was repeated external communication, credential theft indicators, and FTP-based data exfiltration.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Converted packet capture data into readable DNS, HTTP, FTP, connection, and file logs. |
| Suricata | Generated network alerts using custom defensive rules. |
| YARA | Validated static AgentTesla indicators from a controlled sample reference. |
| Splunk | Provided search examples for DNS beaconing, FTP exfiltration, IOC correlation, and analyst triage. |
| MITRE ATT&CK | Mapped observed behavior to common adversary tactics and techniques. |
| IOC analysis | Compared domains, file names, FTP behavior, and hash values against the investigation findings. |

## Investigation Workflow

| Step | Defensive Activity |
| --- | --- |
| 1 | Review the completed AgentTesla incident report and identify the main findings. |
| 2 | Use Zeek logs to review DNS queries, HTTP hosts, FTP sessions, file transfers, and connection patterns. |
| 3 | Use Suricata rules to alert on suspicious domains, FTP uploads, and file-name indicators. |
| 4 | Use YARA to validate static indicators from the controlled AgentTesla sample. |
| 5 | Use Splunk-style searches to hunt for DNS beaconing, FTP exfiltration, and correlated indicators. |
| 6 | Map the behavior to MITRE ATT&CK and document incident response actions. |

## Key Findings

- The activity followed a chain consistent with phishing delivery, GuLoader-style staging, AgentTesla execution, DNS beaconing, and FTP exfiltration.
- DNS evidence included suspicious domains such as `corwineagles[.]com`, `ftp.corwineagles[.]com`, Google Drive-related hosts, and `ip-api[.]com`.
- FTP evidence included `STOR` upload activity, which may indicate outbound data exfiltration.
- File-name patterns such as `Contacts_Thunderbird` and `PW_` suggested possible collection of contacts and saved credentials.
- YARA validation supported AgentTesla classification using static indicators from the controlled sample reference.
- Incident response priorities included host isolation, domain blocking, evidence preservation, credential resets, endpoint validation, and monitoring.

## Indicators of Compromise

| Type | Indicator | Defensive Meaning |
| --- | --- | --- |
| Domain | `corwineagles[.]com` | Suspicious infrastructure observed in the investigation. |
| Domain | `ftp.corwineagles[.]com` | FTP infrastructure observed in the investigation. |
| Domain | `drive.google[.]com` | Possible staged delivery location. |
| Domain | `drive.usercontent.google[.]com` | Possible staged delivery location. |
| Host | `ip-api[.]com` | IP lookup behavior observed in traffic. |
| FTP command | `STOR` | Upload command associated with possible exfiltration. |
| File pattern | `Contacts_Thunderbird` | Possible stolen Thunderbird contact data. |
| File pattern | `PW_` | Possible stolen password data. |
| SHA256 | `bc37921377b4fe391a8487b7116cb8b92b3b09b1c0e9b4f48fb99f217f43eec2` | Controlled AgentTesla sample hash used for YARA validation. |

## Safety Notice

This repository is for defensive security analysis and portfolio documentation only. It does not include malware samples, credentials, sensitive data, malware execution steps, malware deployment steps, or offensive instructions.
