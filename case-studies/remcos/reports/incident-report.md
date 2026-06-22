# Remcos RAT Incident Report

## Executive Summary

The completed investigation identified a malicious 32-bit Windows executable associated with Remcos RAT. The sample was UPX packed, matched a custom YARA rule, and was detected by 58 of 67 security vendors. Threat intelligence connected the investigation to the domain `eastvillageeatery.de` and two related IP addresses. The validated indicators were added to Microsoft Sentinel and used for defensive threat hunting.

## Incident Overview

| Field | Finding |
| --- | --- |
| Malware family | Remcos RAT |
| Threat type | Remote Access Trojan |
| Platform | 32-bit Windows executable |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |
| File protection | UPX packed |
| Detection ratio | 58/67 security vendors |
| Investigation status | Completed |

Remcos is designed to provide unauthorized remote access to a computer. The combined static, detection, and threat intelligence evidence supports classifying this sample as malicious with high confidence.

## Key Findings

| Category | Finding |
| --- | --- |
| File analysis | The sample was a UPX-packed Windows executable. |
| Static indicators | UPX markers and suspicious Windows API names were identified. |
| YARA detection | `Remcos_Combined_Static_IOC` matched the sample successfully. |
| Threat intelligence | The domain and two related IP addresses were identified. |
| Vendor detection | 58 of 67 VirusTotal security vendors detected the file. |
| Security monitoring | Indicators were created and hunted in Microsoft Sentinel. |

## Indicators of Compromise

| Type | Indicator | Confidence |
| --- | --- | --- |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` | High |
| Domain | `eastvillageeatery.de` | High |
| IPv4 address | `104.21.53.137` | Medium |
| IPv4 address | `172.67.213.98` | Medium |

IP addresses may be shared by unrelated services, so defenders should validate IP matches with DNS, endpoint, and time-based evidence.

## MITRE ATT&CK Summary

| Tactic | Technique | ID | Investigation Context |
| --- | --- | --- | --- |
| Initial Access | Phishing Attachment | T1566.001 | Remcos was associated with phishing-themed file delivery. |
| Execution | User Execution | T1204 | The delivery method relied on a user opening the file. |
| Persistence | Registry Run Keys / Startup Folder | T1547.001 | Defender and Sentinel evidence identified Windows Run Key persistence. |
| Defense Evasion | Obfuscated/Compressed Files and Information | T1027 | Static analysis confirmed UPX packing. |
| Credential Access | Input Capture: Keylogging | T1056.001 | Keylogging is a documented Remcos capability. |
| Command and Control | Application Layer Protocol | T1071 | Threat intelligence identified related domain and IP infrastructure. |

Documented capability does not prove that every behavior occurred on an affected system; local telemetry should be used to confirm activity.

## Detection Summary

| Detection Source | Result | Defensive Value |
| --- | --- | --- |
| VirusTotal | 58/67 vendors detected the sample. | Confirms broad security-vendor recognition. |
| YARA | `Remcos_Combined_Static_IOC` matched. | Supports repeatable file-based detection. |
| Microsoft Sentinel | File, domain, and IP indicators were created and hunted. | Supports centralized correlation and investigation. |
| Static analysis | UPX packing and suspicious API indicators were found. | Helps identify similar files without running them. |

## Response Actions

| Action | Status |
| --- | --- |
| Validate the sample hash and file characteristics | Completed |
| Collect and document related indicators | Completed |
| Create Microsoft Sentinel threat intelligence indicators | Completed |
| Hunt the indicators in Microsoft Sentinel | Completed |
| Create and validate a custom YARA detection | Completed |
| Map findings to MITRE ATT&CK | Completed |
| Document evidence for future investigations | Completed |

Defenders can use these results to block confirmed malicious files, monitor related domain activity, and investigate matching endpoint or network events according to local response procedures.

## Lessons Learned

- Combining multiple evidence sources produces a stronger assessment than relying on one alert.
- UPX packing is a useful investigation clue but is not malicious by itself.
- Hash-based detection is precise, while domain and IP indicators require context because infrastructure can change or be shared.
- YARA and Sentinel provide complementary file-level and environment-wide visibility.
- ATT&CK mapping makes technical findings easier to connect to detection and response priorities.

## Analyst Conclusion

The investigation confirmed the sample as Remcos RAT with high confidence. Its packed structure, successful YARA match, strong multi-vendor detection, related threat intelligence, and Sentinel indicators produced actionable defensive content. The documented IOCs, detections, and ATT&CK mapping can support future monitoring, threat hunting, and incident response.
