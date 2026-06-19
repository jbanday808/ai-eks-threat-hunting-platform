# AgentTesla Incident Report

## Executive Summary

| Field | Detail |
| --- | --- |
| Incident ID | INC2026-0203-AGENTTESLA |
| Severity | High (P2) |
| Status | Resolved - lab detection completed |
| Malware family | AgentTesla with GuLoader-style delivery behavior |
| Primary concern | Beaconing, credential theft, and FTP-based data exfiltration |
| Primary evidence | PCAP, Zeek logs, Suricata alerts, IOC validation, and YARA results |

A suspicious infection chain was investigated using a packet capture from a defensive malware traffic analysis lab. The activity showed GuLoader-style delivery behavior followed by AgentTesla-style credential theft and FTP upload activity.

The suspected infected host contacted external services, resolved suspicious domains, and generated FTP activity consistent with outbound exfiltration. The incident is treated as high severity because AgentTesla is associated with theft of browser credentials, email credentials, FTP credentials, contacts, and other saved user data.

## Incident Overview

The completed investigation identified a defensive case study chain of phishing email activity, GuLoader-style staging, Google Drive-related delivery infrastructure, AgentTesla behavior, DNS beaconing, FTP exfiltration, Splunk detection, and incident response. The evidence was reviewed using Zeek, Suricata, YARA, IOC analysis, and MITRE ATT&CK mapping.

For a non-technical audience, the incident means a workstation appeared to contact suspicious external services and upload data to an outside FTP server. Because AgentTesla is known for stealing saved credentials, the safest response is to treat the affected user accounts as potentially exposed.

## Key Findings

- DNS lookups and HTTP traffic showed suspicious external communications.
- FTP activity included `STOR` upload behavior.
- File patterns such as `Contacts_Thunderbird` and `PW_` suggested possible credential or contact collection.
- Suricata rules produced alerts for observed domains and FTP behavior.
- YARA validation identified static traits associated with the controlled AgentTesla sample.

## Affected Systems and Data

| Area | Assessment |
| --- | --- |
| Suspected host | Workstation that generated the suspicious DNS, HTTP, and FTP traffic in the PCAP. |
| Potential data exposure | Browser passwords, email credentials, FTP credentials, Thunderbird contacts, and saved user data. |
| External infrastructure | Suspicious FTP and web destinations observed during network review. |

## Indicators of Compromise

| Type | Indicator | Purpose |
| --- | --- | --- |
| Domain | `corwineagles[.]com` | Infrastructure observed during the investigation. |
| Domain | `ftp.corwineagles[.]com` | FTP infrastructure observed during the investigation. |
| Domain | `drive.google[.]com` | Possible staged download or payload delivery path. |
| Domain | `drive.usercontent.google[.]com` | Possible staged download or payload delivery path. |
| HTTP host | `ip-api[.]com` | IP lookup behavior seen in traffic. |
| FTP command | `STOR` | Upload command that may indicate data exfiltration. |
| File pattern | `Contacts_Thunderbird` | Possible stolen Thunderbird contact data. |
| File pattern | `PW_` | Possible stolen password data naming pattern. |
| SHA256 | `bc37921377b4fe391a8487b7116cb8b92b3b09b1c0e9b4f48fb99f217f43eec2` | AgentTesla sample hash used for YARA testing. |

## Timeline

| Phase | Activity |
| --- | --- |
| Initial compromise | User receives or opens malicious content connected to GuLoader-style delivery behavior. |
| Payload activity | Malware reaches external services and begins suspicious communication. |
| Beaconing / check-in | Infected host repeatedly contacts outside destinations. |
| Credential theft | AgentTesla-style behavior attempts to collect saved credentials and application data. |
| Data exfiltration | FTP `STOR` commands and transferred file evidence suggest outbound upload activity. |
| Detection | Zeek, Suricata, IOC validation, and YARA confirm suspicious behavior. |
| Containment | Host isolation, outbound blocking, and credential resets reduce risk. |
| Recovery | System is cleaned or reimaged, validated, and monitored before return to service. |

## Root Cause

Initial access likely started from malicious email content or staged downloader activity. The activity succeeded because this type of threat can bypass weak email filtering, limited endpoint controls, and permissive outbound traffic policies.

## Response Actions

- Isolate the suspected infected host.
- Block known malicious domains, IPs, and FTP destinations at DNS and firewall layers.
- Preserve PCAPs, Zeek logs, Suricata logs, endpoint logs, and malware hashes.
- Reset credentials for the affected user and any accounts used on the system.

## Recovery

- Reimage the host from a trusted baseline or remove confirmed malicious artifacts through approved endpoint response procedures.
- Patch the operating system, browser, email client, and document readers.
- Review startup entries, scheduled tasks, and endpoint alerts for persistence indicators.
- Restore only clean data from verified backups.
- Monitor for repeated DNS, HTTP, FTP, or TLS traffic to suspicious destinations.

## Lessons Learned

- Outbound FTP should be restricted where it is not required.
- DNS and proxy logs are valuable for early detection of staged delivery and beaconing.
- Endpoint credential stores should be protected with strong hardening and monitoring.
- Detection content should include both indicator-based and behavior-based logic.
- Incident reports should explain technical evidence in plain language so leadership and analysts can make fast decisions.

## Conclusion

The investigation confirmed AgentTesla-style credential theft and FTP exfiltration behavior in a defensive lab environment. The case was resolved by documenting the evidence, creating Suricata and YARA detections, mapping behavior to MITRE ATT&CK, and defining response actions for containment and recovery.
