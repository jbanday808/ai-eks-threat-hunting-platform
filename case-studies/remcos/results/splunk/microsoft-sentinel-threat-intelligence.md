# Microsoft Sentinel Threat Intelligence: Remcos RAT

## Overview

Microsoft Sentinel was used to create and hunt threat intelligence indicators related to the completed Remcos RAT investigation. The indicators allow defenders to compare the known file hash, domain, and IP addresses with security events collected in Sentinel.

## Indicators Created

| Indicator Type | Value | Purpose | Confidence | Severity | Tags |
| --- | --- | --- | --- | --- | --- |
| SHA256 | `A6CCD89558C4B5CD2FEC2512B846E14620BE2CB3489F85B99203A9E4B9751D6A` | Identify the investigated Remcos file and related endpoint activity | 80 | 4 | `Remcos`, `RAT`, `Malware`, `Persistence`, `T1547.001` |
| Domain | `eastvillageeatery.de` | Identify possible Remcos command-and-control activity | 80 | 4 | `Remcos`, `RAT`, `C2`, `Domain`, `Malware`, `T1071` |
| IPv4 | `104.21.53.137` | Correlate network activity with investigated infrastructure | 80 | 4 | `Remcos`, `RAT`, `C2`, `Domain`, `Malware`, `T1071` |
| IPv4 | `172.67.213.98` | Correlate network activity with investigated infrastructure | 80 | 4 | `Remcos`, `RAT`, `C2`, `Domain`, `Malware`, `T1071` |

All four indicators were classified as TLP: White, meaning they can be shared for defensive security purposes. An indicator match is an investigation lead and should be confirmed with local endpoint, DNS, and network evidence.

## SHA256 File Indicator

| Field | Value |
| --- | --- |
| Name | Remcos RAT SHA256 |
| Observable type | File |
| Hash type | SHA-256 |
| Observable value | `A6CCD89558C4B5CD2FEC2512B846E14620BE2CB3489F85B99203A9E4B9751D6A` |
| Indicator type | Anomalous activity, Malicious activity |
| Kill chain phases | Execution, Persistence |
| Confidence | 80 |
| Severity | 4 |
| TLP | White |

**Description:** Remcos RAT (`Backdoor:Win32/Rescoms.A!bit`) was identified during dynamic analysis. Microsoft Defender detected a dropped payload (`eastvillageeatery.exe`) and persistence through `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\eastvillageeatery`.

## Domain Indicator

| Field | Value |
| --- | --- |
| Name | Remcos C2 Domain |
| Observable type | Domain name |
| Domain | `eastvillageeatery.de` |
| Indicator type | Anomalous activity, Malicious activity |
| Kill chain phase | CommandAndControl |
| Valid until | 2026-09-20 |
| Source | Microsoft Sentinel |
| Confidence | 80 |
| Severity | 4 |
| TLP | White |

**Description:** The domain was observed in VirusTotal relationships for the Remcos RAT sample and associated with the investigated SHA256 hash.

## IP Indicators

| Field | Value |
| --- | --- |
| Name | Remcos C2 IP |
| Observable type | IPv4 address |
| IPs | `104.21.53.137`, `172.67.213.98` |
| Indicator type | Anomalous activity, Malicious activity |
| Kill chain phase | CommandAndControl |
| Valid until | 2026-09-20 |
| Source | Microsoft Sentinel |
| Confidence | 80 |
| Severity | 4 |
| TLP | White |

**Description:** These IPv4 addresses were associated with Remcos RAT infrastructure through VirusTotal relationship analysis. Because IP addresses can host unrelated services, analysts should validate matches with domain, host, and time-based context.

## KQL Threat Hunt Query

The completed hunt searched active threat intelligence records tagged for Remcos and displayed the fields needed for analyst review.

```kql
ThreatIntelIndicators
| where Tags has "remcos"
| project TimeGenerated,
          ObservableValue,
          ObservableKey,
          Pattern,
          Confidence,
          IsActive
| order by TimeGenerated desc
```

The query returns when each indicator was recorded, its observable value and pattern, its confidence score, and whether it remains active.
