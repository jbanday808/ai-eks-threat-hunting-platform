# Remcos Threat Intelligence Report

## Executive Summary

The completed investigation used MalwareBazaar, VirusTotal, Microsoft Sentinel, static analysis, and YARA to assess a suspicious Windows executable. Multiple intelligence and detection sources identified the sample as Remcos RAT. The file was UPX packed, detected by 58 of 67 security vendors, and linked to domain and IP indicators that were added to Microsoft Sentinel for defensive threat hunting.

## Threat Overview

| Category | Finding |
| --- | --- |
| Malware Family | Remcos RAT |
| Malware Type | Remote Access Trojan |
| Delivery Method | Phishing Attachment |
| Detection Ratio | 58/67 |
| Community Score | -59 |
| File Type | PE32 Windows Executable |
| Packer | UPX 3.91 |

Remcos is a Remote Access Trojan that can allow unauthorized control of a Windows computer. The combined evidence supports a malicious classification with high confidence.

## MalwareBazaar Findings

| Field | Finding |
| --- | --- |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |
| Malware Family | Remcos RAT |
| Analysis Purpose | Defensive malware research |

The sample was downloaded from MalwareBazaar for defensive analysis in a controlled lab environment.

## VirusTotal Findings

VirusTotal recorded a detection ratio of 58/67 and a community score of -59. These results show broad agreement among security vendors that the file is malicious.

### File Hashes

| Hash Type | Value |
| --- | --- |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |
| MD5 | `4a40b6494d80287a5660b2b0fe881ddf` |
| SHA1 | `67f28f3897dcf58f8a281ac2ee2e14cfffe1d36c` |
| Imphash | `9101de1775a541d31c617d880d867c2e` |

### Tags

- `peexe`
- `persistence`
- `spreader`
- `long-sleeps`
- `upx`

The tags describe the Windows executable format and behaviors or characteristics reported by VirusTotal.

## Microsoft Sentinel Threat Intelligence Findings

| Type | Indicator |
| --- | --- |
| Domain | `eastvillageeatery.de` |
| IPv4 address | `104.21.53.137` |
| IPv4 address | `172.67.213.98` |

The file, domain, and IP indicators were added to Microsoft Sentinel Threat Intelligence and used for threat hunting activities. Sentinel provided a central location to correlate the indicators with security data and support future investigations.

IP addresses can be shared by unrelated services, so analysts should review IP matches with DNS, endpoint, and time-based context.

## Indicators of Compromise

| Type | Indicator |
| --- | --- |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |
| Domain | `eastvillageeatery.de` |
| IP | `104.21.53.137` |
| IP | `172.67.213.98` |
| File | `eastvillageeatery.exe` |
| File | `7hr8ftfxm.exe` |

These indicators support defensive detection and investigation; an indicator match should be validated with local system and network evidence.

## MITRE ATT&CK Mapping

| Tactic | Technique | ID |
| --- | --- | --- |
| Initial Access | Phishing Attachment | T1566.001 |
| Execution | User Execution | T1204 |
| Persistence | Registry Run Keys | T1547.001 |
| Defense Evasion | Packed Files | T1027 |
| Credential Access | Keylogging | T1056.001 |
| Command and Control | Application Layer Protocol | T1071 |

The mapping connects the investigation findings and documented Remcos capabilities to a standard framework used by defenders.

## Evidence Screenshots

### Figure 1: MalwareBazaar Identification

![MalwareBazaar Remcos identification](../../../img/remcos/malware-bazaar-remcos.png)

MalwareBazaar provides the malware-family identification and sample intelligence used during research.

### Figure 2: VirusTotal Detection Summary

![VirusTotal Remcos detection summary](../../../img/remcos/virus-total-remcos.png)

VirusTotal shows security-vendor detections and file information for Remcos analysis.

### Figure 3: VirusTotal Sample Details

![VirusTotal investigated sample details](../../../img/remcos/virus-total-remcos-sha256.png)

VirusTotal displays the investigated hash, executable metadata, and malware-related tags.

### Figure 4: Sentinel Threat Indicators

![Microsoft Sentinel Remcos threat indicators](../../../img/remcos/microsoft-sentinel-remcos-threat-iocs.png)

Microsoft Sentinel lists the file hash, domain, and IP addresses as threat intelligence indicators.

### Figure 5: Sentinel SHA256 Record

![Microsoft Sentinel SHA256 record](../../../img/remcos/Microsoft-Sentinel-sha256-hash.png)

Microsoft Sentinel confirms that the investigated SHA256 was available for defensive hunting and correlation.

## Analyst Assessment

The sample displays characteristics commonly associated with Remote Access Trojans, including UPX packing, persistence, command-and-control infrastructure, and credential theft capabilities. The high detection ratio, negative community score, YARA match, and matching threat intelligence support classifying the sample as Remcos RAT with high confidence.

## Summary

Threat intelligence, static analysis, YARA detection, and Microsoft Sentinel hunting collectively confirmed the sample as Remcos RAT. The completed investigation produced validated indicators and reusable defensive evidence for monitoring, threat hunting, and incident response.
