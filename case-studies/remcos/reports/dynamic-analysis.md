# Remcos RAT Dynamic Analysis

## Overview

Dynamic analysis was completed in an isolated Windows 11 Enterprise lab environment using VMware Workstation, Noriben, Procmon, Microsoft Defender, Splunk Enterprise, and Microsoft Sentinel. The investigation observed behavior associated with the Remcos sample, validated security detections, identified indicators of compromise (IOCs), and developed threat hunting and detection opportunities that support incident response.

Dynamic analysis helps defenders understand what malware does after execution. This behavior-based evidence improves visibility, strengthens detection logic, and gives response teams practical information for identifying affected systems, validating containment, and finding related activity.

## Executive Summary

A Remcos RAT sample was analyzed within an isolated Windows 11 lab environment. Behavioral monitoring, endpoint telemetry, threat intelligence, and centralized logging confirmed malicious activity, identified persistence mechanisms, validated indicators of compromise, and produced threat hunting content that can be reused for future investigations.

## Analysis Goal

The analysis was conducted to identify and document:

- Process activity
- File activity
- Persistence activity
- Security detections
- Threat intelligence indicators
- Threat hunting opportunities

Understanding malware behavior allows defenders to create more effective detections, recognize similar activity more quickly, and make response decisions using validated endpoint evidence.

## Lab Environment

| Component | Purpose |
| --- | --- |
| Windows 11 Enterprise VM | Malware analysis system used to collect endpoint evidence in a controlled environment. |
| VMware Workstation | Isolated analysis environment used to preserve and restore the virtual machine. |
| Noriben | Behavioral activity collection used to produce a timeline of system events. |
| Procmon | Process and file monitoring used to review activity associated with the suspicious executable. |
| Microsoft Defender | Malware detection and validation used to identify the threat, affected artifacts, and persistence-related activity. |
| Splunk Enterprise | Threat hunting and log analysis used to correlate Defender events, affected systems, and IOC data. |
| Splunk Universal Forwarder | Windows log collection used to send endpoint telemetry to Splunk. |
| Microsoft Sentinel | Threat intelligence enrichment used to store and validate file, domain, and IP indicators. |
| YARA | Static malware identification used to match characteristics associated with the investigated sample. |

## Evidence Sources

Evidence was collected from endpoint telemetry, behavioral monitoring tools, threat intelligence platforms, and centralized logging systems, including Procmon, Noriben, Microsoft Defender, Splunk Enterprise, Microsoft Sentinel, MalwareBazaar, VirusTotal, and YARA.

These sources provided complementary evidence: behavioral tools showed what happened on the system, security platforms confirmed detections, and threat intelligence added context for validation and hunting.

## Observed Behavior

| Category | Finding |
| --- | --- |
| Process Activity | Suspicious executable activity associated with Remcos was observed and validated through Procmon, Noriben, Defender, and Splunk. |
| File Activity | Malicious executable artifacts including `eastvillageeatery.exe` were identified and investigated. |
| Persistence Activity | Defender telemetry identified Windows Run Key persistence activity associated with the malware. |
| Network Intelligence | Threat intelligence identified infrastructure associated with the investigation, including domain and IP indicators. |
| Security Detections | Multiple security tools independently classified the sample as Remcos RAT. |

The evidence established that the suspicious executable generated observable endpoint activity and was detected as malicious. Threat intelligence provided associated infrastructure for correlation and hunting; it did not, by itself, prove that the lab system communicated with every listed network indicator.

## Detailed Findings

### Process Activity

**Observed:**

- `RFQ_Coaxial_Cable_2026.exe` executed within the isolated analysis environment.
- Procmon recorded process creation activity.
- Noriben captured behavioral events associated with execution.
- Microsoft Defender generated malware detections.
- Splunk searches confirmed related security events.

**Investigation Value:** Process monitoring confirmed that the sample produced observable activity and supplied timestamps and event context for validation. This evidence helped analysts connect execution behavior with Defender detections and centralized Splunk records.

### File Activity

**Observed:**

- `eastvillageeatery.exe` was identified during the investigation.
- Defender telemetry identified the file as a malicious artifact.
- File-based indicators supported IOC development and threat hunting activities.
- SHA256 indicators were validated through multiple intelligence sources.

**Investigation Value:** Malicious files often become primary indicators during threat hunting and incident response. The filename and hash gave analysts precise artifacts to search across endpoint telemetry, security platforms, and threat intelligence sources.

### Persistence Activity

**Observed:**

- Microsoft Defender identified Windows Run Key persistence activity.
- Persistence artifacts were associated with `eastvillageeatery.exe`.
- Findings aligned with known Remcos RAT behavior.

**Investigation Value:** Run Key persistence can automatically restart malware when a user signs in, increasing the risk of continued compromise. Identifying this behavior supports containment validation, registry-focused hunting, and detection engineering for similar persistence attempts.

### Threat Intelligence Indicators

**Associated indicators:**

**Domain:**

- `eastvillageeatery.de`

**IP addresses:**

- `104.21.53.137`
- `172.67.213.98`

**SHA256:**

- `A6CCD89558C4B5CD2FEC2512B846E14620BE2CB3489F85B99203A9E4B9751D6A`

**Observed:**

- Indicators were imported into Microsoft Sentinel.
- Indicators were imported into Splunk.
- Threat intelligence enrichment linked the infrastructure to Remcos activity.
- Indicators were used to support hunting and correlation activities.

**Investigation Value:** Threat intelligence indicators act like fingerprints that help analysts identify related malicious activity across multiple systems and data sources. Correlating the indicators with endpoint, DNS, proxy, and firewall records supports broader scoping, while domain, process, file, and time context helps analysts avoid treating a shared IP address as conclusive evidence by itself.

### Security Detections

| Detection Source | Finding |
| --- | --- |
| Microsoft Defender | `Backdoor:Win32/Rescoms.A!bit` |
| Splunk Enterprise | Remcos-related security events |
| Microsoft Sentinel | IOC enrichment and validation |
| MalwareBazaar | Sample identified as Remcos RAT |
| VirusTotal | Malicious domain and infrastructure associations |
| YARA | Static detection successfully matched |

Multiple independent security sources validated the malware classification. This cross-validation increased confidence in the investigation findings, reduced the likelihood of a false positive, and produced evidence that could support both host-based and intelligence-led detections.

## Detection Opportunities

### Sigma

Detect Windows Run Key persistence activity associated with Remcos behavior. A portable Sigma rule can help defenders identify similar registry changes across supported security platforms.

### Splunk

Search Windows Defender telemetry, process execution logs, and threat intelligence indicators for known Remcos activity. Correlating these sources can reveal affected hosts, suspicious files, persistence attempts, and repeated detections.

### Microsoft Sentinel

Use imported indicators to support correlation, enrichment, and proactive hunting activities. Indicator matches should be reviewed with endpoint and timing context before analysts classify an event as malicious.

### YARA

Identify suspicious packed executables and characteristics commonly associated with Remcos RAT. File-based matching supports malware triage and complements behavior-based detection.

### IOC Enrichment

Leverage hashes, domains, IP addresses, filenames, and intelligence indicators to support threat hunting. Enrichment adds context to raw events and helps analysts prioritize matches that have supporting behavioral evidence.

Using multiple detection methods improves visibility, strengthens validation, and increases confidence during investigations. It also reduces dependence on any single tool or indicator and creates overlapping opportunities to detect related activity.

## Investigation Evidence

### Figure 1 – VMware Analysis Environment

![Figure 1 – VMware Analysis Environment](../../../img/remcos/Pre-Remcos-Analysis-Snapshot.png)

This VMware snapshot confirms the analysis environment was preserved before testing, allowing investigators to safely restore the system and repeat the investigation if needed.

### Figure 2 – Procmon Process Activity

![Figure 2 – Procmon Process Activity](../../../img/remcos/Procmon-RFQ_Coaxial_Cable_2026.png)

This Procmon capture shows the suspicious executable launching and creating process activity that was later investigated.

### Figure 3 – Noriben Timeline Evidence

![Figure 3 – Noriben Timeline Evidence](../../../img/remcos/Noriben_19_Jun_26__17_47_396109_timeline.png)

This Noriben timeline records system activity generated during execution and provides a chronological view of observed events.

### Figure 4 – Microsoft Defender Detection Event

![Figure 4 – Microsoft Defender Detection Event](../../../img/remcos/remcos-event-process.png)

This security event shows Microsoft Defender identifying malicious activity associated with the investigated sample.

### Figure 5 – Windows Defender Threat Detection

![Figure 5 – Windows Defender Threat Detection](../../../img/remcos/windows-defender-eastvillageeatery.png)

This alert shows Microsoft Defender detecting `Backdoor:Win32/Rescoms.A!bit` and identifying the associated executable.

### Figure 6 – Defender Investigation Results

![Figure 6 – Defender Investigation Results](../../../img/remcos/Get-MpThreatDetection.png)

This PowerShell output documents Defender detection details, affected files, and persistence-related artifacts identified during the investigation.

### Figure 7 – Microsoft Sentinel Threat Intelligence

![Figure 7 – Microsoft Sentinel Threat Intelligence](../../../img/remcos/microsoft-sentinel-remcos-threat-iocs.png)

This Sentinel view confirms the imported Remcos indicators used to support enrichment, validation, and threat hunting activities.

### Figure 8 – Sentinel Domain Validation

![Figure 8 – Sentinel Domain Validation](../../../img/remcos/eastvillageeatery-microsoft-sentinel.png)

This query validates that the suspicious domain was successfully imported into Sentinel and available for threat hunting activities.

### Figure 9 – SHA256 Validation

![Figure 9 – SHA256 Validation](../../../img/remcos/eastvillageeatery-sha256-hash.png)

This hash verification confirms the SHA256 value associated with the investigated malware sample.

### Figure 10 – VirusTotal Domain Intelligence

![Figure 10 – VirusTotal Domain Intelligence](../../../img/remcos/eastvillageeatery-url-virus-total.png)

This threat intelligence result identifies the domain as suspicious and provides supporting infrastructure information used during the investigation.

### Figure 11 – MalwareBazaar Intelligence

![Figure 11 – MalwareBazaar Intelligence](../../../img/remcos/malware-bazaar-remcos.png)

This MalwareBazaar entry classifies the sample as Remcos RAT and provides intelligence used to support malware validation.

## Key Findings

| Finding | Result |
| --- | --- |
| Malware Family | Remcos RAT |
| Threat Name | `Backdoor:Win32/Rescoms.A!bit` |
| Suspicious File | `eastvillageeatery.exe` |
| Domain Indicator | `eastvillageeatery.de` |
| IP Indicators | `104.21.53.137`, `172.67.213.98` |
| Persistence Activity | Windows Run Key behavior observed |
| Detection Sources | Defender, Splunk, Sentinel, MalwareBazaar, VirusTotal, YARA |

The completed analysis confirmed the malware family, affected artifacts, persistence behavior, and indicators needed for defensive hunting. These findings directed the investigation toward endpoint containment validation, environment-wide IOC searches, and reusable file, registry, and telemetry detections.

## Analyst Summary

Dynamic analysis confirmed Remcos RAT activity through behavioral monitoring, endpoint telemetry, threat intelligence, and centralized log analysis. Evidence collected from Procmon, Noriben, Microsoft Defender, Splunk Enterprise, Microsoft Sentinel, MalwareBazaar, VirusTotal, and YARA validated the malware classification and supported the development of reusable threat hunting and detection content.

The investigation demonstrated how multiple defensive security tools can be correlated to improve visibility, accelerate investigations, and support incident response activities.

## Conclusion

Dynamic analysis documented observable Remcos RAT behavior using behavioral monitoring, endpoint telemetry, threat intelligence, and Splunk-based hunting. The resulting workflow supports repeatable malware investigation and incident response.

The project demonstrates malware analysis, detection engineering, IOC enrichment, Microsoft Defender analysis, Microsoft Sentinel threat intelligence, and threat hunting. Centralized dashboards and telemetry improve visibility, reduce investigation time, and strengthen security operations.

## References

- MalwareBazaar — https://bazaar.abuse.ch/
- VirusTotal — https://www.virustotal.com/
- Microsoft Defender Documentation — https://learn.microsoft.com/en-us/defender-endpoint/
- Microsoft Sentinel Documentation — https://learn.microsoft.com/en-us/azure/sentinel/
- Splunk Enterprise Documentation — https://docs.splunk.com/Documentation/Splunk
- MITRE ATT&CK Framework — https://attack.mitre.org/
- VMware Workstation Documentation — https://docs.vmware.com/en/VMware-Workstation-Pro/

## Author

James Banday

Threat Hunter | Cloud Security | Kubernetes | DevSecOps | Threat Detection | Incident Response

This project demonstrates practical threat hunting, malware analysis, IOC enrichment, Microsoft Defender investigation, Microsoft Sentinel threat intelligence, detection engineering, and incident response techniques used to investigate and document Remcos RAT activity in a controlled lab environment.

The investigation showcases real-world malware analysis, behavioral monitoring, threat intelligence correlation, detection validation, Splunk threat hunting, and incident response workflows used by cybersecurity professionals to identify, investigate, and document malicious activity.

### GitHub Repository

https://github.com/jbanday808/ai-eks-threat-hunting-platform/tree/main

### LinkedIn Profile

https://www.linkedin.com/in/james-allen-morta-banday-62a391128/
