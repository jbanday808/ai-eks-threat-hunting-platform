# AgentTesla Investigation Architecture

## Purpose

This document explains the defensive architecture of the AgentTesla case study in simple terms. It shows how the suspected activity moved from initial delivery to detection and response.

## Infection Chain Architecture

```text
Phishing Email
-> GuLoader
-> Google Drive
-> AgentTesla
-> DNS Beaconing
-> FTP Exfiltration
-> Splunk Detection
-> Incident Response
```

## Stage Explanations

| Stage | Simple Explanation | Defensive Evidence |
| --- | --- | --- |
| Phishing Email | The activity likely began with malicious email content or an attachment-driven lure. | Incident report assessment and initial access analysis. |
| GuLoader | GuLoader-style behavior was associated with staged delivery before AgentTesla activity. | Suspicious external communication and staged delivery indicators. |
| Google Drive | Google Drive-related hosts appeared in the investigation as possible staging locations. | DNS and HTTP evidence for `drive.google[.]com` and `drive.usercontent.google[.]com`. |
| AgentTesla | AgentTesla is an information stealer that can collect saved credentials and user data. | YARA validation and AgentTesla-related IOC findings. |
| DNS Beaconing | The suspected host contacted external domains during the activity. | Zeek `dns.log`, Splunk DNS searches, and Suricata DNS rules. |
| FTP Exfiltration | FTP upload behavior suggested possible outbound transfer of stolen data. | Zeek `ftp.log`, `files.log`, FTP `STOR`, and file-name patterns. |
| Splunk Detection | Searches correlate DNS, FTP, file names, and host activity for analyst review. | Splunk search examples for DNS, FTP, beaconing, and IOC correlation. |
| Incident Response | The defensive response focuses on containment, evidence preservation, credential resets, and recovery. | Incident response findings and recovery plan. |

## Defensive Evidence Flow

```text
PCAP
-> Zeek conn.log, dns.log, http.log, ftp.log, files.log
-> Suricata fast.log and eve.json
-> IOC review
-> YARA validation
-> Splunk hunting searches
-> MITRE ATT&CK mapping
-> Incident report
```

## Tools and Roles

| Tool | Role in the Architecture |
| --- | --- |
| Zeek | Turns packet capture evidence into structured logs for investigation. |
| Suricata | Alerts on known suspicious domains, FTP uploads, and file-name indicators. |
| YARA | Validates static indicators from the controlled AgentTesla sample. |
| Splunk | Searches and correlates log evidence for analysts. |
| MITRE ATT&CK | Organizes observed behavior into standard adversary tactics and techniques. |

## Defensive Design Notes

- DNS evidence helps identify suspicious external communication.
- FTP evidence is important because AgentTesla activity can include data upload behavior.
- IOC matching is useful, but it should be combined with behavior such as beaconing and exfiltration.
- Incident response should assume credentials may be exposed when AgentTesla is suspected.
