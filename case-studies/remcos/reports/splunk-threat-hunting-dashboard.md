# Remcos Threat Hunting Dashboard

## Overview

This report documents a Splunk-based threat hunt for Remcos remote access trojan (RAT) activity in a Windows lab environment. The investigation uses Microsoft Defender events, known indicators of compromise (IOCs), external threat intelligence, and a purpose-built dashboard to show what was found, why it matters, and which system requires further investigation. Remcos is a remote administration tool that can be misused to control an infected system, collect information, and maintain unauthorized access, so confirming related activity is important for both technical responders and stakeholders assessing business risk.

The dashboard was created after the Remcos investigation was completed to convert the validated evidence into an operational security view. It consolidates detection results, IOC enrichment, external threat intelligence, Microsoft Defender endpoint telemetry, and documented findings so analysts do not have to review each source separately. This centralized visibility makes malicious activity easier to recognize, supports faster triage and scoping, and gives incident responders a consistent starting point for containment and follow-up analysis.

## Objective

The objective was to confirm Remcos-related activity, identify the affected system, locate events associated with the suspicious executable, validate the malware classification, and present the results in a repeatable Splunk dashboard. This gives analysts and incident responders a clear view of the incident scope and the evidence needed to prioritize containment and further analysis.

The investigation specifically validated known indicators of compromise, identified affected systems, examined suspicious executable activity, and visualized the confirmed findings. These objectives supported threat hunting by turning known threat data into searchable evidence and supported incident response by showing where the activity occurred, how serious it was, and which events required additional validation.

## Tools Used

| Tool | Purpose and Investigation Contribution |
| --- | --- |
| Splunk Enterprise | Collects, searches, correlates, and visualizes security events. It was used to investigate Defender telemetry, search known indicators, identify affected systems, and build a reusable dashboard that supports detection validation and response decisions. |
| Microsoft Defender Antivirus | Detects malicious endpoint activity and records operational events and response actions. It provided the host-level evidence used to confirm the Remcos detection, review severity, identify the suspicious executable, and assess whether quarantine occurred. |
| Splunk Universal Forwarder | Sends Windows event data from the monitored endpoint to Splunk. It was used to verify the collection path and ensured the endpoint telemetry needed for centralized hunting and dashboard reporting was available. |
| MalwareBazaar | Provides malware-family intelligence, sample metadata, and vendor detection context. It was used to independently validate the Remcos RAT classification and strengthen confidence in the investigation findings. |
| VirusTotal | Aggregates file, URL, domain, and security-vendor analysis. It contributed corroborating threat intelligence for the investigated indicators and supported detection validation across independent sources. |
| Microsoft Sentinel Threat Intelligence | Stores and manages threat indicators for correlation and hunting. It contributed previously validated file, domain, and IP context that informed the Remcos IOC dataset used in Splunk. |
| VMware Workstation | Hosts the isolated Windows analysis system and supports recoverable virtual-machine snapshots. It provided a controlled environment for defensive analysis and preserved the investigation state for repeatable review. |
| CSV IOC lookup | Stores known Remcos indicators in a structured, reusable format. It was imported into Splunk to support IOC enrichment, consistent threat correlation, and repeatable searches across available security telemetry. |
| MITRE ATT&CK | Provides a standard framework for describing adversary tactics and techniques. It helped place Remcos behavior in defensive context and connect investigation findings to detection engineering and response use cases. |

## IOC Lookup

The IOC lookup places the validated Remcos indicators into a reusable Splunk table for enrichment, threat correlation, hunting, and detection validation. In plain language, these indicators act like fingerprints: analysts compare them with endpoint and network records to identify activity that may be related to the same threat. This method reduces manual entry errors, adds threat context to raw events, and allows detection and response teams to apply the same validated intelligence consistently.

```spl
| inputlookup remcos_iocs.csv
```

| description | indicator | type |
| --- | --- | --- |
| Remcos associated IP | 104.21.53.137 | ip |
| Remcos associated IP | 172.67.213.98 | ip |
| Remcos possible C2 domain | eastvillageeatery.de | domain |
| Remcos sample hash | a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a | sha256 |

The lookup confirms that the investigation data includes two associated IP addresses, a possible command-and-control domain, and the SHA256 hash of the Remcos sample. These values help defenders correlate activity across endpoint, DNS, proxy, and network data, although IP matches should be validated with file, process, domain, and timing evidence because shared infrastructure can host unrelated services.

## Dashboard Panels

### Remcos Detection

#### What the search shows

Displays systems where Remcos malware was detected, including the event time, affected host, and malware name. This helps analysts quickly confirm malicious activity and identify impacted devices.

```spl
index=* Remcos
| table _time Computer Threat_Name
```

#### Why it matters

The detection results provide the first validated link between the Remcos threat name and a monitored endpoint. This supports triage by showing that the alert is backed by searchable Microsoft Defender telemetry rather than an unsupported indicator match.

#### Investigation value

The dashboard view also presents available severity, response action, and file path fields so responders can understand the risk and determine whether the endpoint security control contained the threat.

### Affected Systems

#### What the search shows

Shows which systems were affected by Remcos activity and the number of detections associated with each host. This helps determine the scope of the incident and identify systems requiring further investigation.

```spl
index=* Remcos
| stats count by Computer
```

#### Why it matters

Knowing which hosts generated detections helps distinguish an isolated endpoint event from activity affecting multiple systems. Accurate scoping is necessary to prioritize containment and prevent overlooked devices from remaining exposed.

#### Investigation value

The grouped result gives analysts a concise host-level view for assigning response actions, validating asset ownership, and extending searches to related endpoint and network telemetry.

### Remcos Executable Hunt

#### What the search shows

Searches Microsoft Defender logs for activity related to the suspicious executable identified during the investigation. This helps confirm whether the file was observed and where the related event occurred.

```spl
index=* "eastvillageeatery.exe" Computer="Enterprise-Threat-Hunting" source="XmlWinEventLog:Microsoft-Windows-Windows Defender/Operational"
```

#### Why it matters

Executable evidence connects the malware investigation to a specific file name and endpoint. This reduces reliance on the malware-family label alone and gives responders a concrete artifact to validate, contain, and search across the environment.

#### Investigation value

The dashboard table presents the event time, computer, and log source, allowing analysts to place the executable-related activity on the investigation timeline and confirm its endpoint origin.

### Remcos Severity

#### What the search shows

Groups detections by severity level, allowing analysts to focus first on the highest-risk activity. This gives technical teams and decision-makers a direct indication of how urgently the detected behavior should be handled.

```spl
index=* Remcos
| stats count by Severity_Name
```

#### Why it matters

Severity provides a consistent way to prioritize limited response resources. Severe malware detections require prompt review because they may indicate unauthorized control of the endpoint and continuing risk to the environment.

#### Investigation value

The severity visualization supports queue prioritization, escalation, and incident communication by making the risk level immediately visible to analysts, responders, and security leadership.

## Key Findings

- Splunk returned three Remcos-related detection events for `Enterprise-Threat-Hunting`. This confirms repeated endpoint evidence on one monitored system and narrows the initial incident scope to that host.

  **Investigation impact:** The repeated detections established the primary host for deeper endpoint review and focused containment planning.

- Microsoft Defender identified the threat as `Backdoor:Win32/Rescoms.A!bit`. This matters because a backdoor classification indicates possible unauthorized remote access and warrants prompt endpoint containment and investigation.

  **Investigation impact:** The backdoor classification increased the response priority and supported searches for related access, persistence, and communication activity.

- The dashboard classified the observed detections as `Severe`. This places the activity in the highest-priority investigation category shown in the dashboard.

  **Investigation impact:** The severity rating supported immediate triage and clear escalation to incident response personnel.

- One displayed Defender action was `Quarantine`, while another was `Not Applicable`. The quarantine result shows that Defender took a containment action, but the different action values mean responders should verify the final disposition of every related event.

  **Investigation impact:** The mixed action values prevented the investigation from assuming complete remediation and identified containment validation as a required follow-up.

- The executable hunt returned three Microsoft Defender operational events associated with `eastvillageeatery.exe` on `Enterprise-Threat-Hunting`. These events connect the suspicious filename to the affected endpoint and provide timestamps for timeline analysis.

  **Investigation impact:** The file-level events provided a searchable artifact and timestamps for reconstructing activity and extending the hunt to other data sources.

- The Remcos IOC lookup contains `104.21.53.137`, `172.67.213.98`, `eastvillageeatery.de`, and `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a`. These indicators give defenders specific values for broader endpoint and network searches.

  **Investigation impact:** The enriched indicators enabled consistent correlation across file, DNS, proxy, firewall, and endpoint records while supporting reusable detections.

- MalwareBazaar identifies the externally reviewed sample with SHA256 `d113f72b9248e3a89d72d1238a8465af7857822b82951681cff22391ffff3039` as `RemcosRAT`, lists 13 vendor detections, and shows the file name `seriouslyworkingontheprojectforbestresults.hta`. This independent threat intelligence supports the Remcos classification used during the investigation.

  **Investigation impact:** Independent intelligence strengthened confidence in the malware-family assessment and reduced the risk of relying on a single detection source.

- The `SplunkForwarder` service was `Running` on the Windows analysis system. This confirms that the endpoint collection service required to send investigation data to Splunk was active when verified.

  **Investigation impact:** Collection-path validation increased confidence that the dashboard was based on available endpoint telemetry and helped rule out a stopped forwarder as a visibility gap.

## Investigation Workflow

1. Imported Remcos IOC lookup into Splunk.
2. Verified Windows event collection through Splunk Universal Forwarder.
3. Investigated Microsoft Defender detections.
4. Searched for known Remcos indicators.
5. Identified affected systems.
6. Investigated suspicious executable activity.
7. Built dashboard visualizations.
8. Documented findings and evidence.

Each step increased confidence in the result: the lookup supplied known threat fingerprints, collection verification confirmed that endpoint evidence was reaching Splunk, Defender events validated malicious activity, and indicator searches connected threat intelligence to the affected host. System scoping and executable analysis then established where the activity occurred, while the dashboard and evidence record improved analyst visibility and created a repeatable detection and response workflow.

## Evidence

### Figure 1 — Remcos Detection Search

![Figure 1 — Remcos Detection Search](../../../img/remcos/threat-hunting-dashboard/01-remcos-detection.png)

This search confirms that three Remcos malware detections were recorded for the monitored system and provides the host and threat name needed to begin the investigation.

### Figure 2 — Affected Systems

![Figure 2 — Affected Systems](../../../img/remcos/threat-hunting-dashboard/02-affected-systems.png)

This result shows that all three Remcos detections are associated with `Enterprise-Threat-Hunting`, which is important for defining the observed incident scope.

### Figure 3 — Remcos Executable Hunt

![Figure 3 — Remcos Executable Hunt](../../../img/remcos/threat-hunting-dashboard/03-remcos-executable-hunt.png)

This search demonstrates that `eastvillageeatery.exe` appears in Microsoft Defender operational data on the affected system, providing endpoint evidence and timing for further analysis.

### Figure 4 — MalwareBazaar Remcos RAT Record

![Figure 4 — MalwareBazaar Remcos RAT Record](../../../img/remcos/threat-hunting-dashboard/04-malwarebazaar-remcos-rat.png)

This threat intelligence record identifies the reviewed sample as `RemcosRAT` and provides supporting vendor and file information used to validate the investigation.

### Figure 5 — Dashboard Creation

![Figure 5 — Dashboard Creation](../../../img/remcos/threat-hunting-dashboard/05-dashboard-creation.png)

This screenshot demonstrates the creation of a dedicated Splunk dashboard for Remcos IOC hunting and beaconing analysis, which is important for making the investigation repeatable.

### Figure 6 — Investigation Snapshot

![Figure 6 — Investigation Snapshot](../../../img/remcos/threat-hunting-dashboard/06-vmware-snapshot.png)

This screenshot shows the preserved `Remcos Investigation Snapshot`, which is important for maintaining a recoverable and repeatable virtual analysis state.

### Figure 7 — Splunk Universal Forwarder

![Figure 7 — Splunk Universal Forwarder](../../../img/remcos/threat-hunting-dashboard/09-splunk-forwarder-running.png)

This service check demonstrates that `SplunkForwarder` is running on the Windows system, which is important because the investigation depends on endpoint logs reaching Splunk.

### Figure 8 — Remcos IOC Lookup

![Figure 8 — Remcos IOC Lookup](../../../img/remcos/threat-hunting-dashboard/07-remcos-ioc-lookup.png)

This lookup displays the Remcos IP addresses, possible command-and-control domain, and sample hash in Splunk, making the validated indicators available for consistent threat hunting.

### Figure 9 — Remcos Threat Hunting Dashboard

![Figure 9 — Remcos Threat Hunting Dashboard](../../../img/remcos/threat-hunting-dashboard/08-remcos-threat-hunting-dashboard.png)

This dashboard consolidates detections, affected systems, executable events, and severity into a single view, making it easier to monitor and analyze Remcos activity.

## Analyst Summary

The investigation identified three severe Remcos-related Microsoft Defender events on `Enterprise-Threat-Hunting` and connected the suspicious executable `eastvillageeatery.exe` to the same endpoint. The IOC lookup provides the associated IP addresses, possible command-and-control domain, and sample hash for broader searches, while MalwareBazaar supplies independent support for the Remcos RAT classification. The running Splunk Universal Forwarder confirms that endpoint telemetry can reach the central investigation platform.

The dashboard adds operational value by putting the most relevant evidence in one view: analysts can confirm the detection, assess the affected host, review executable activity, and prioritize the severe events without repeating separate searches. For incident responders, this consolidated view supports faster scoping and triage while preserving the underlying event details needed to validate containment, build a timeline, and decide on follow-up actions.

IOC enrichment strengthened the hunt by converting validated hashes, domains, and IP addresses into reusable search data that could be correlated with security telemetry. Microsoft Defender supplied the endpoint detections, severity, response actions, and executable evidence needed to validate the activity, while Splunk turned those separate records into an accessible operational picture. The same workflow can be reused for future malware investigations by replacing the IOC dataset, adapting the searches to the available telemetry, and retaining the panel structure for detection validation, host scoping, artifact analysis, and prioritization.

## Conclusion

The Splunk threat hunt confirmed severe Remcos-related activity on the monitored Windows system and organized the supporting endpoint, IOC, threat intelligence, and collection evidence into a repeatable investigation workflow. The results support continued validation of the suspicious file, review of the host for persistence and related network activity, and confirmation that every malicious artifact was contained. The dashboard improves visibility by consolidating key evidence and supports faster security investigations by helping analysts move from detection to scope and response decisions in a single view.

This completed investigation demonstrates practical threat hunting through IOC enrichment, Microsoft Defender log analysis, and targeted Splunk searches; it also demonstrates dashboard development, detection engineering concepts, and evidence-driven support for incident response. The methodology connected known threat fingerprints to endpoint observations, translated those observations into reusable searches and visualizations, and preserved the evidence needed for triage and follow-up action. Centralized dashboards improve visibility, reduce investigation time, and strengthen security operations by giving detection and response teams a shared, repeatable view of validated threat activity.

## References

- [MalwareBazaar](https://bazaar.abuse.ch/)
- [VirusTotal](https://www.virustotal.com/)
- [Microsoft Defender documentation](https://learn.microsoft.com/en-us/defender-endpoint/)
- [Microsoft Sentinel Threat Intelligence documentation](https://learn.microsoft.com/en-us/azure/sentinel/understand-threat-intelligence)
- [Splunk Enterprise documentation](https://docs.splunk.com/Documentation/Splunk)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [VMware Workstation documentation](https://docs.vmware.com/en/VMware-Workstation-Pro/)

## Author

James Banday

Threat Hunter | Cloud Security | Kubernetes | DevSecOps | Threat Detection | Incident Response

This project demonstrates practical threat hunting, malware analysis, IOC enrichment, Splunk dashboard development, detection engineering, and incident response techniques used to investigate and document Remcos RAT activity in a controlled lab environment.

### GitHub Repository

https://github.com/jbanday808/ai-eks-threat-hunting-platform/tree/main

### LinkedIn Profile

https://www.linkedin.com/in/james-allen-morta-banday-62a391128/
