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

## Investigation Evidence

### 1. Sample Identification

![Figure 1. AgentTesla infection chain diagram](../../img/agenttesla/agent-tesla-infection-chain-diagram.png)

Figure 1 shows the high-level investigation chain from suspected delivery activity through AgentTesla behavior and defensive detection.

![Figure 2. AgentTesla sample archive reference](../../img/agenttesla/inv.-5234353-rar-agent-tesla.png)

Figure 2 documents the sample reference used for controlled defensive identification.

![Figure 3. Windows executable identification](../../img/agenttesla/agent-tesla-windows-executable.png)

Figure 3 shows the file type evidence used to identify the sample as a Windows executable.

![Figure 4. SHA-256 hash evidence](../../img/agenttesla/agent-tesla-sha-256-hash.png)

Figure 4 captures the SHA-256 hash used to track and validate the controlled sample.

### 2. IOC Analysis

![Figure 5. AgentTesla IOC list](../../img/agenttesla/agent-tesla-iocs.png)

Figure 5 summarizes the indicators reviewed during the AgentTesla investigation.

![Figure 6. MalwareBazaar sample reference](../../img/agenttesla/agent-tesla-malware-bazaar.png)

Figure 6 shows external reputation context used to support defensive sample validation.

![Figure 7. VirusTotal domain review](../../img/agenttesla/domain-corwin-eagles-virus-total.png)

Figure 7 shows domain reputation review for suspicious infrastructure observed in the case.

### 3. Zeek Analysis

![Figure 8. Zeek connection log](../../img/agenttesla/zeek-conn-log-agent-tesla.png)

Figure 8 shows Zeek connection evidence used to review source and destination activity.

![Figure 9. Zeek DNS log](../../img/agenttesla/zeek-dns-log-agent-tesla.png)

Figure 9 shows DNS evidence used to identify suspicious domain lookups.

![Figure 10. Zeek FTP log, part 1](../../img/agenttesla/zeek-ftp-log-01-agent-tesla.png)

Figure 10 shows FTP session evidence related to possible exfiltration behavior.

![Figure 11. Zeek FTP log, part 2](../../img/agenttesla/zeek-ftp-log-02-agent-tesla.png)

Figure 11 provides additional FTP evidence for analyst review.

![Figure 12. Zeek SSL log](../../img/agenttesla/zeek-ssl-log-agent-tesla.png)

Figure 12 shows encrypted-traffic metadata used to support network timeline review.

![Figure 13. Zeek log correlation](../../img/agenttesla/zeek-log-correlation-agent-tesla.png)

Figure 13 shows correlation across Zeek logs to connect related network events.

### 4. Splunk Analysis

![Figure 14. Splunk AgentTesla logs](../../img/agenttesla/splunk-logs-agent-tesla.png)

Figure 14 shows Splunk log review for the AgentTesla investigation.

![Figure 15. DNS beaconing in Splunk](../../img/agenttesla/dns-beaconing-splunk.png)

Figure 15 shows Splunk evidence used to review repeated DNS communication.

![Figure 16. FTP credential exfiltration search](../../img/agenttesla/ftp-credential-exfiltration-splunk.png)

Figure 16 shows Splunk hunting for FTP activity associated with possible credential exfiltration.

![Figure 17. Splunk DNS beaconing correlation search](../../img/agenttesla/splunk-dns-beaconing-correlation-search.png)

Figure 17 shows correlation logic used to connect DNS beaconing indicators with related activity.

### 5. Suricata Analysis

![Figure 18. Suricata rules](../../img/agenttesla/agent-tesla-suricata-rules.png)

Figure 18 shows custom defensive Suricata rules created from the investigation findings.

![Figure 19. Suricata test result](../../img/agenttesla/agent-tesla-suricata-test-result.png)

Figure 19 shows Suricata rule validation against the controlled investigation evidence.

![Figure 20. Suricata eve.json evidence](../../img/agenttesla/agent-tesla-suricate-eve-json.png)

Figure 20 shows structured Suricata alert output used for detection review.

![Figure 21. Suricata fast.log evidence](../../img/agenttesla/agent-tesla-suricate-fast-log.png)

Figure 21 shows Suricata fast log output for quick alert validation.

### 6. YARA Analysis

![Figure 22. YARA validation results](../../img/agenttesla/agenttesla_yara_results.png)

Figure 22 shows YARA validation results for AgentTesla-related static indicators.

### 7. Network Evidence

![Figure 23. FTP packet capture evidence](../../img/agenttesla/agent-tesla-ftp-pcap.png)

Figure 23 shows packet-level FTP evidence associated with possible outbound exfiltration.

## Safety Notice

This repository is for defensive security analysis and portfolio documentation only. It does not include malware samples, credentials, sensitive data, malware execution steps, malware deployment steps, or offensive instructions.
