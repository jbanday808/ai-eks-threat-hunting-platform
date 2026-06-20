# Remcos Threat Intelligence and Detection Engineering Case Study

## Overview

This project documents a completed defensive investigation of Remcos RAT using threat intelligence, static analysis, detection engineering, MITRE ATT&CK mapping, Microsoft Sentinel, and YARA. The case study shows how multiple evidence sources can identify a threat and turn investigation findings into practical defensive detections.

## Investigation Objectives

- Identify malware indicators
- Validate threat intelligence
- Create detections
- Map activity to MITRE ATT&CK
- Improve defensive visibility

## Tools Used

| Tool | Purpose |
| --- | --- |
| Microsoft Sentinel | Store threat indicators and support security hunting |
| VirusTotal | Compare file and domain findings across security vendors |
| MalwareBazaar | Research malware-family intelligence and reference samples |
| YARA | Detect files that contain validated static indicators |
| ExifTool | Review file metadata without running the sample |
| Strings | Extract readable static content for analysis |
| Kali Linux | Provide an isolated analysis environment and security tools |
| MITRE ATT&CK | Map evidence to known adversary behavior |

# Investigation Workflow

![Threat Intelligence and Detection Engineering Workflow](../../img/remcos/remcos-workflow-diagram.png)

> This workflow demonstrates how threat intelligence is transformed into practical detections, investigations, and incident response activities.

| Phase | Purpose |
| --- | --- |
| Threat Intelligence | Collect information about known threats and malicious infrastructure. |
| IOC Development | Create indicators such as hashes, domains, IPs, and filenames. |
| Threat Hunting | Search logs and systems for evidence of malicious activity. |
| Detection Engineering | Develop YARA, Sigma, Suricata, Sentinel, and Splunk detections. |
| Endpoint Detection | Validate findings through Microsoft Defender and endpoint telemetry. |
| Behavior Analysis | Analyze malware execution and persistence mechanisms. |

# Investigation Methodology

The investigation followed a structured workflow:

1. Threat Intelligence Collection
2. IOC Development
3. Threat Hunting
4. Detection Engineering
5. Endpoint Detection
6. Behavioral Analysis

This approach helped transform raw threat intelligence into actionable detections and investigation findings.

## Key Findings

| Finding | Result |
| --- | --- |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |
| Domain | `eastvillageeatery.de` |
| IP addresses | `104.21.53.137`, `172.67.213.98` |
| Detection ratio | 58/67 security vendors |
| UPX packed | Yes |
| Malware family | Remcos RAT |

The sample was a 32-bit Windows executable packed with UPX. Static indicators, threat intelligence, a successful custom YARA match, and multi-vendor detection supported the final assessment.

## Detection Engineering

| Detection | Purpose |
| --- | --- |
| YARA | File detection |
| Microsoft Sentinel | Threat intelligence hunting |
| IOC Analysis | Threat identification |
| MITRE ATT&CK | Behavior mapping |

## MITRE ATT&CK Coverage

- Initial Access
- Execution
- Persistence
- Defense Evasion
- Credential Access
- Command and Control

The detailed technique mapping and supporting evidence are documented in the [MITRE ATT&CK report](reports/mitre-attack.md).

## Investigation Evidence

### 1. Sample Identification

#### Figure 1: MalwareBazaar Family Identification

![MalwareBazaar Remcos family identification](../../img/remcos/malware-bazaar-remcos.png)

MalwareBazaar identifies a reference sample as RemcosRAT and provides supporting malware-family context.

#### Figure 2: VirusTotal Reference Sample

![VirusTotal reference sample analysis](../../img/remcos/virus-total-remcos.png)

VirusTotal shows security-vendor detections and file details for a Remcos reference sample.

#### Figure 3: VirusTotal Investigated Sample

![VirusTotal investigated sample analysis](../../img/remcos/virus-total-remcos-sha256.png)

VirusTotal records the investigated file hash, Windows executable format, and malware-related tags.

#### Figure 4: PE Executable Identification

![PE executable identification](../../img/remcos/pe-executable-remcos.png)

Static inspection identifies the investigated file as a 32-bit Windows executable.

#### Figure 5: Investigated Executable

![Investigated RFQ-themed executable](../../img/remcos/RFQ_Coaxial_Cable_2026.png)

The isolated lab folder shows the RFQ-themed executable examined during the investigation.

### 2. Threat Intelligence

#### Figure 6: Domain Reputation and DNS Data

![VirusTotal domain analysis](../../img/remcos/eastvillageeatery-url-virus-total.png)

VirusTotal shows security detections and network addresses associated with the investigated domain.

#### Figure 7: Investigated File Hash

![SHA256 verification of the investigated file](../../img/remcos/eastvillageeatery-sha256-hash.png)

The file hash check confirms the unique SHA256 value used to track the investigated executable.

#### Figure 8: Sentinel Threat Indicators

![Microsoft Sentinel threat intelligence indicators](../../img/remcos/microsoft-sentinel-remcos-threat-iocs.png)

Microsoft Sentinel lists the file hash, domain, and IP addresses as active threat intelligence indicators.

#### Figure 9: Sentinel Domain Record

![Microsoft Sentinel domain record](../../img/remcos/eastvillageeatery-microsoft-sentinel.png)

Microsoft Sentinel shows the investigated domain as an active indicator with defensive context and confidence data.

#### Figure 10: Sentinel SHA256 Record

![Microsoft Sentinel SHA256 record](../../img/remcos/Microsoft-Sentinel-sha256-hash.png)

Microsoft Sentinel confirms that the investigated SHA256 was stored for defensive monitoring and correlation.

### 3. Static Analysis

#### Figure 11: Executable Metadata

![Remcos executable metadata](../../img/remcos/remcos_metadata-win32-exe.png)

The metadata view confirms the sample's 32-bit Windows format and UPX-packed structure.

#### Figure 12: Custom YARA Rule

![Custom Remcos YARA rule](../../img/remcos/yara-rule-remcos.png)

The custom YARA rule combines validated file markers and Windows API names for defensive detection.

#### Figure 13: YARA Detection Result

![Custom Remcos YARA match](../../img/remcos/yara-rule-remcos-results.png)

The YARA result shows that the sample matched the expected UPX markers and suspicious API indicators.

### 4. Dynamic Analysis

#### Figure 14: Process Monitor Activity

![Process Monitor activity for the investigated file](../../img/remcos/Procmon-RFQ_Coaxial_Cable_2026.png)

Process Monitor records the sample's process start, thread creation, and exit activity in the isolated lab.

#### Figure 15: Noriben Timeline

![Noriben analysis timeline](../../img/remcos/Noriben_19_Jun_26__17_47_396109_timeline.png)

The Noriben timeline places the investigated process activity alongside other system events for review.

#### Figure 16: Process Event Details

![Remcos process event details](../../img/remcos/remcos-event-process.png)

The event record shows the process and thread activity captured during controlled analysis.

#### Figure 17: Registry Verification

![Registry Run key verification](../../img/remcos/remcos-registry-verification.png)

The registry checks review common Windows Run locations for possible persistence entries.

### 5. Detection and Hunting

#### Figure 18: Sentinel Threat Hunt

![Microsoft Sentinel threat hunting query](../../img/remcos/remcos-threat-hunt-kql-query.png)

The Sentinel query returns the investigated indicators so analysts can review their status, confidence, and context.

#### Figure 19: Microsoft Defender Alert

![Microsoft Defender Remcos alert](../../img/remcos/windows-defender-eastvillageeatery.png)

Microsoft Defender identifies the file as a severe remote-access threat and records the affected item.

#### Figure 20: Defender Detection Details

![Microsoft Defender threat detection details](../../img/remcos/Get-MpThreatDetection.png)

The Defender detection record provides remediation status and related file and registry evidence for investigation.

### 6. Lab Environment

#### Figure 21: Isolated Sample Folder

![Remcos lab sample folder](../../img/remcos/remcos-folder.png)

The sample folder shows how investigation files were separated within the controlled lab environment.

#### Figure 22: Project Structure

![Repository structure with AgentTesla and Remcos case-study artifacts](../../img/remcos/remcos-project-folders.png)

Figure 22. Repository structure showing AgentTesla and Remcos malware analysis case studies, detection content, threat intelligence artifacts, screenshots, and supporting security documentation.

#### Figure 23: Pre-Analysis Snapshot

![Pre-Remcos-analysis virtual machine snapshot](../../img/remcos/Pre-Remcos-Analysis-Snapshot.png)

The virtual machine snapshot provides a clean recovery point created before controlled analysis began.

## Reports

| Report | Scope |
| --- | --- |
| [Threat Intelligence Report](reports/threat-intelligence-report.md) | External intelligence, IOCs, and Sentinel findings |
| [MITRE ATT&CK Mapping](reports/mitre-attack.md) | Tactics, techniques, and supporting evidence |
| [Static Analysis Summary](reports/static-analysis-summary.md) | File metadata, UPX markers, APIs, and YARA results |
| [Incident Report](reports/incident-report.md) | Incident documentation |
| [Dynamic Analysis](reports/dynamic-analysis.md) | Controlled behavior-analysis documentation |

## Analyst Conclusion

Multiple evidence sources confirmed the sample as Remcos RAT. The investigation produced actionable file, domain, and IP indicators; a reusable YARA detection; Sentinel hunting data; and an ATT&CK-based behavior map that defenders can use to improve monitoring and incident response.

## Safety Notice

- Defensive cybersecurity research only
- No malware samples included
- No credentials included
- No sensitive data included
- No malware execution instructions included
