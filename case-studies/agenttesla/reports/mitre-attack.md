# MITRE ATT&CK Mapping - AgentTesla

This table maps the completed AgentTesla investigation findings to MITRE ATT&CK. The mapping is written for defensive reporting and portfolio review.

| Tactic | Technique | ID | Evidence |
| --- | --- | --- | --- |
| Initial Access | Phishing | T1566 | The incident report assessed initial access as likely malicious email content or attachment-driven delivery. |
| Execution | User Execution | T1204 | The chain likely required user interaction with malicious content before follow-on activity. |
| Defense Evasion | Obfuscated Files or Information | T1027 | GuLoader-style delivery behavior suggested staged or obfuscated content before AgentTesla activity. |
| Command and Control | Application Layer Protocol | T1071 | The suspected host contacted external web and DNS destinations during the investigation. |
| Command and Control | Web Service | T1102 | Google Drive-related domains appeared as possible staged delivery locations. |
| Discovery | System Location Discovery | T1614 | `ip-api[.]com` traffic may indicate external IP or location lookup behavior. |
| Collection | Data from Local System | T1005 | File patterns such as `Contacts_Thunderbird` suggested collection of local user data. |
| Credential Access | Credentials from Web Browsers | T1555.003 | AgentTesla is associated with theft of saved browser credentials. |
| Credential Access | Credentials from Password Stores | T1555 | The `PW_` file-name pattern suggested possible saved password collection. |
| Exfiltration | Exfiltration Over Alternative Protocol | T1048 | FTP upload behavior was observed during the investigation. |
| Exfiltration | Exfiltration Over Unencrypted Non-C2 Protocol | T1048.003 | FTP `STOR` commands indicated possible outbound file upload activity. |

## Defensive Notes

- The strongest finding is the combination of suspicious DNS, FTP upload behavior, credential-themed file names, and AgentTesla static indicators.
- A single IOC should not be treated as final proof by itself. Correlation across Zeek, Suricata, YARA, and Splunk increases confidence.
- AgentTesla cases should be handled as potential credential exposure incidents.
