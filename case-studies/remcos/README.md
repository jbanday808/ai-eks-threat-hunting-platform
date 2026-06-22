# Remcos RAT Threat Intelligence and Detection Engineering Case Study

## Overview

This case study documents a completed defensive investigation of Remcos RAT using threat intelligence, static and dynamic analysis, detection engineering, MITRE ATT&CK mapping, Microsoft Defender, Microsoft Sentinel, Splunk, YARA, and external intelligence sources. It summarizes what was found, why it matters, and where to review the supporting technical evidence.

Related case study: [RemcosRAT HTA and CyberChef Analysis](../remcos-hta-cyberchef/README.md)

## Executive Summary

A Remcos RAT sample was investigated using threat intelligence, static analysis, dynamic analysis, detection engineering, Microsoft Defender, Microsoft Sentinel, YARA, Splunk, VirusTotal, and MalwareBazaar. Multiple evidence sources confirmed the malware family, identified associated infrastructure, validated indicators of compromise, and produced reusable threat hunting and detection content.

This investigation demonstrates practical malware analysis, IOC enrichment, detection engineering, threat hunting, MITRE ATT&CK mapping, Splunk-based investigation, and incident response workflows used by modern security operations teams.

## Investigation Objectives

- Identify Remcos RAT indicators of compromise.
- Validate threat intelligence from multiple sources.
- Analyze static and dynamic malware evidence.
- Create reusable detection content.
- Map activity to MITRE ATT&CK.
- Build a Splunk threat hunting dashboard.
- Document findings for incident response and portfolio review.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Microsoft Defender | Validate endpoint malware detections and affected artifacts. |
| Microsoft Sentinel | Store indicators and support threat intelligence hunting. |
| Splunk Enterprise | Search endpoint telemetry, validate detections, and build the threat hunting dashboard. |
| VirusTotal | Validate file, domain, and vendor reputation findings. |
| MalwareBazaar | Research malware-family intelligence and reference samples. |
| YARA | Detect files using validated static indicators. |
| Procmon | Review process and system activity in the lab environment. |
| Noriben | Record behavioral activity and timeline evidence. |
| ExifTool | Review file metadata without executing the sample. |
| Strings | Extract readable static content for analysis. |
| MITRE ATT&CK | Map evidence to known adversary behavior. |
| VMware Workstation | Maintain an isolated and recoverable lab environment. |

## Investigation Workflow

![Threat Intelligence and Detection Engineering Workflow](../../img/remcos/remcos-workflow-diagram.png)

The workflow shows how raw threat intelligence was turned into validated findings, reusable detections, dashboards, and incident response documentation.

| Phase | Purpose |
| --- | --- |
| Threat Intelligence | Collect information about known threats and malicious infrastructure. |
| IOC Development | Create indicators such as hashes, domains, IPs, and filenames. |
| Threat Hunting | Search logs and systems for evidence of malicious activity. |
| Detection Engineering | Develop YARA, Sigma, Suricata, Sentinel, and Splunk detections. |
| Endpoint Detection | Validate findings through Microsoft Defender and endpoint telemetry. |
| Behavior Analysis | Analyze malware execution and persistence mechanisms. |

## Key Findings

| Finding | Result |
| --- | --- |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |
| Domain | `eastvillageeatery.de` |
| IP addresses | `104.21.53.137`, `172.67.213.98` |
| Detection ratio | 58/67 security vendors |
| UPX packed | Yes |
| Malware family | Remcos RAT |
| Threat name | `Backdoor:Win32/Rescoms.A!bit` |
| Suspicious file | `eastvillageeatery.exe` |
| Splunk detections | Remcos-related events identified |
| Persistence activity | Windows Run Key behavior observed |
| Detection sources | Defender, Sentinel, Splunk, MalwareBazaar, VirusTotal, YARA |

The investigation confirmed Remcos RAT activity using multiple independent sources. The findings supported threat hunting, detection engineering, incident response documentation, and dashboard development.

## Reports

| Report | Scope |
| --- | --- |
| [Incident Report](reports/incident-report.md) | Executive incident documentation, findings, impact, and response recommendations. |
| [Dynamic Analysis](reports/dynamic-analysis.md) | Controlled malware behavior analysis using Defender, Procmon, Noriben, Splunk, and Sentinel evidence. |
| [Static Analysis Summary](reports/static-analysis-summary.md) | File metadata, UPX indicators, strings, suspicious APIs, and YARA results. |
| [Threat Intelligence Report](reports/threat-intelligence-report.md) | External intelligence, IOCs, Sentinel enrichment, MalwareBazaar, and VirusTotal findings. |
| [MITRE ATT&CK Mapping](reports/mitre-attack.md) | Tactics, techniques, and supporting evidence mapped to adversary behavior. |
| [Splunk Threat Hunting Dashboard](reports/splunk-threat-hunting-dashboard.md) | Splunk searches, IOC enrichment, dashboard panels, detection validation, and threat hunting results. |

## Detection Engineering

| Detection | Purpose |
| --- | --- |
| YARA | Detects files using validated static indicators. |
| Microsoft Sentinel | Stores and correlates threat intelligence indicators. |
| Splunk | Searches endpoint telemetry and visualizes investigation findings. |
| IOC Analysis | Supports environment-wide threat hunting. |
| MITRE ATT&CK | Maps observed behavior to known adversary techniques. |

## MITRE ATT&CK Coverage

- Initial Access
- Execution
- Persistence
- Defense Evasion
- Credential Access
- Command and Control

MITRE ATT&CK was used to translate technical findings into a standard language for detection engineering, threat hunting, and incident response. Detailed techniques and evidence are documented in the [MITRE ATT&CK report](reports/mitre-attack.md).

## Investigation Evidence

### 1. Sample Identification

#### Figure 1: MalwareBazaar Family Identification

![MalwareBazaar Remcos family identification](../../img/remcos/malware-bazaar-remcos.png)

MalwareBazaar identifies a reference sample as RemcosRAT, supporting the malware-family assessment.

#### Figure 2: VirusTotal Reference Sample

![VirusTotal reference sample analysis](../../img/remcos/virus-total-remcos.png)

VirusTotal shows vendor detections and file details that support classification of the reference sample.

#### Figure 3: VirusTotal Investigated Sample

![VirusTotal investigated sample analysis](../../img/remcos/virus-total-remcos-sha256.png)

VirusTotal records the investigated hash, Windows executable format, and malware-related tags.

#### Figure 4: PE Executable Identification

![PE executable identification](../../img/remcos/pe-executable-remcos.png)

Static inspection confirms that the investigated file is a 32-bit Windows executable.

#### Figure 5: Investigated Executable

![Investigated RFQ-themed executable](../../img/remcos/RFQ_Coaxial_Cable_2026.png)

The isolated lab folder identifies the RFQ-themed executable reviewed during the investigation.

### 2. Threat Intelligence

#### Figure 6: Domain Reputation and DNS Data

![VirusTotal domain analysis](../../img/remcos/eastvillageeatery-url-virus-total.png)

VirusTotal shows security detections and network addresses associated with the investigated domain.

#### Figure 7: Investigated File Hash

![SHA256 verification of the investigated file](../../img/remcos/eastvillageeatery-sha256-hash.png)

The hash check confirms the unique SHA256 used to track the investigated executable.

#### Figure 8: Sentinel Threat Indicators

![Microsoft Sentinel threat intelligence indicators](../../img/remcos/microsoft-sentinel-remcos-threat-iocs.png)

Microsoft Sentinel lists the file hash, domain, and IP addresses used for correlation and hunting.

#### Figure 9: Sentinel Domain Record

![Microsoft Sentinel domain record](../../img/remcos/eastvillageeatery-microsoft-sentinel.png)

Microsoft Sentinel confirms that the investigated domain was stored as an active threat indicator.

#### Figure 10: Sentinel SHA256 Record

![Microsoft Sentinel SHA256 record](../../img/remcos/Microsoft-Sentinel-sha256-hash.png)

Microsoft Sentinel confirms that the SHA256 was available for defensive monitoring and correlation.

### 3. Static Analysis

#### Figure 11: Executable Metadata

![Remcos executable metadata](../../img/remcos/remcos_metadata-win32-exe.png)

The metadata confirms the sample's 32-bit Windows format and UPX-packed structure.

#### Figure 12: Custom YARA Rule

![Custom Remcos YARA rule](../../img/remcos/yara-rule-remcos.png)

The custom YARA rule combines validated file markers and Windows API names for defensive detection.

#### Figure 13: YARA Detection Result

![Custom Remcos YARA match](../../img/remcos/yara-rule-remcos-results.png)

The successful YARA match confirms the expected UPX markers and suspicious API indicators.

### 4. Dynamic Analysis

#### Figure 14: Process Monitor Activity

![Process Monitor activity for the investigated file](../../img/remcos/Procmon-RFQ_Coaxial_Cable_2026.png)

Process Monitor records process start, thread creation, and exit activity associated with the sample.

#### Figure 15: Noriben Timeline

![Noriben analysis timeline](../../img/remcos/Noriben_19_Jun_26__17_47_396109_timeline.png)

The Noriben timeline places the investigated process activity in chronological context.

#### Figure 16: Process Event Details

![Remcos process event details](../../img/remcos/remcos-event-process.png)

The event record shows process and thread activity captured during controlled analysis.

#### Figure 17: Registry Verification

![Registry Run key verification](../../img/remcos/remcos-registry-verification.png)

The registry checks document review of common Windows Run locations for persistence evidence.

### 5. Detection and Hunting

#### Figure 18: Sentinel Threat Hunt

![Microsoft Sentinel threat hunting query](../../img/remcos/remcos-threat-hunt-kql-query.png)

The Sentinel query returns the investigated indicators with status, confidence, and defensive context.

#### Figure 19: Microsoft Defender Alert

![Microsoft Defender Remcos alert](../../img/remcos/windows-defender-eastvillageeatery.png)

Microsoft Defender identifies the file as a severe remote-access threat and records the affected artifact.

#### Figure 20: Defender Detection Details

![Microsoft Defender threat detection details](../../img/remcos/Get-MpThreatDetection.png)

The Defender record provides remediation status plus related file and registry evidence.

### 6. Lab Environment

#### Figure 21: Isolated Sample Folder

![Remcos lab sample folder](../../img/remcos/remcos-folder.png)

The folder view confirms that investigation artifacts were separated within the controlled lab.

#### Figure 22: Project Structure

![Repository structure with AgentTesla and Remcos case-study artifacts](../../img/remcos/remcos-project-folders.png)

The repository structure organizes malware analysis artifacts, detections, screenshots, and supporting documentation.

#### Figure 23: Pre-Analysis Snapshot

![Pre-Remcos-analysis virtual machine snapshot](../../img/remcos/Pre-Remcos-Analysis-Snapshot.png)

The virtual machine snapshot provides a clean recovery point preserved before controlled analysis.

## Analyst Conclusion

The Remcos investigation confirmed the malware family, validated file, domain, and IP indicators, documented static and dynamic behavior, and produced reusable detection and hunting content. Microsoft Defender, Microsoft Sentinel, Splunk, VirusTotal, MalwareBazaar, YARA, Procmon, and Noriben provided supporting evidence that strengthened confidence in the final assessment.

This case study demonstrates practical Cyber Intrusion Analyst and Threat Hunter skills, including malware analysis, IOC enrichment, detection engineering, MITRE ATT&CK mapping, Splunk investigation workflows, and incident response documentation.

## Safety Notice

- Defensive cybersecurity research only.
- No malware samples included.
- No credentials included.
- No sensitive data included.
- No malware execution instructions included.

## Author

James Banday

Threat Hunter | Cyber Intrusion Analyst | Cloud Security | Kubernetes | DevSecOps | Incident Response

This case study demonstrates practical malware analysis, threat hunting, IOC enrichment, Microsoft Defender investigation, Microsoft Sentinel threat intelligence, Splunk dashboard development, detection engineering, and incident response documentation used to investigate and document Remcos RAT activity in a controlled lab environment.

### GitHub Repository

https://github.com/jbanday808/ai-eks-threat-hunting-platform/tree/main

### LinkedIn Profile

https://www.linkedin.com/in/james-allen-morta-banday-62a391128/
