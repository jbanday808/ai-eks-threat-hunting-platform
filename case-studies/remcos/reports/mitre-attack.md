# Remcos RAT MITRE ATT&CK Mapping

## Overview

MITRE ATT&CK was used to map observed Remcos RAT behavior to known adversary tactics and techniques. The mapping is based on threat intelligence, static analysis, Microsoft Sentinel indicators, YARA detection results, and documented Remcos capabilities. It gives technical and non-technical readers a consistent view of how the threat enters a system, avoids detection, maintains access, collects information, and communicates externally.

## MITRE ATT&CK Mapping

| Tactic | Technique | ID | Evidence |
| --- | --- | --- | --- |
| Initial Access | Phishing | T1566 | The investigated material used phishing-themed delivery. |
| Execution | User Execution | T1204 | Malware execution required user interaction with the downloaded file. |
| Execution | System Binary Proxy Execution: Mshta | T1218.005 | `shell.hta` used the Windows HTML Application path to begin the concealed chain. |
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 | The HTA contained an obfuscated PowerShell loader. |
| Persistence | Registry Run Keys / Startup Folder | T1547.001 | Microsoft Defender and Sentinel findings identified persistence through Windows Run Keys. |
| Defense Evasion | Obfuscated Files or Information | T1027 | The samples used UPX packing, `boroc` obfuscation, string reversal, character replacement, and Base64 encoding. |
| Defense Evasion | Deobfuscate/Decode Files or Information | T1140 | The HTA chain transformed and decoded concealed content before loading it. |
| Credential Access | Input Capture: Keylogging | T1056.001 | Remcos is capable of capturing user keystrokes and credential data. |
| Command and Control | Application Layer Protocol | T1071 | Threat intelligence identified `eastvillageeatery.de` and associated infrastructure used for communications. |
| Command and Control | Ingress Tool Transfer | T1105 | The loader referenced remotely retrieved content named `optimized_MSI.png`. |
| Command and Control | Application Layer Protocol: Web Protocols | T1071.001 | Noriben recorded PowerShell connecting to `66.63.170.34:80` over HTTP. |
| Defense Evasion | Reflective Code Loading | T1620 | The decoded content referenced `AppDomain.CurrentDomain.Load` and `Fiber.Program.Main`, indicating in-memory .NET loading. |

## Key Findings

| Category | Finding |
| --- | --- |
| Initial Access | Phishing-themed executable delivery |
| Execution | User launched malicious executable |
| Persistence | Registry Run Key persistence |
| Defense Evasion | UPX packing detected |
| HTA execution | `mshta` and concealed PowerShell loader behavior |
| Decoding | Character replacement, string reversal, and Base64 decoding |
| Network activity | HTTP connection to `66.63.170.34:80` |
| Memory loading | .NET content loaded through `AppDomain.CurrentDomain.Load` |
| Credential Access | Keylogging capability |
| Command and Control | Domain and IP-based infrastructure identified |

## Analyst Assessment

The observed behavior aligns with known Remcos RAT activity. The combination of phishing delivery, persistence mechanisms, packed executable characteristics, credential theft capabilities, and command-and-control communications supports classifying the sample as a Remote Access Trojan. This assessment combines directly observed evidence with documented malware capabilities; a capability does not by itself prove that the behavior occurred on every affected system.

## RemcosRAT HTA and CyberChef Analysis

The additional mapping explains the HTA chain in standard defensive language. Phishing and `mshta` describe how the chain could reach and begin on a Windows system. PowerShell, obfuscation, and decoding describe how it concealed its intent. HTTP transfer and reflective loading describe how it attempted to obtain and start further content. Microsoft Defender remediated the threat; verification found no active Remcos or Caspol process and no persistence from this chain.

Simple explanation: ATT&CK turns the technical evidence into a recognizable sequence: delivery, hidden scripting, internet communication, and memory loading. It helps security teams decide what logs and alerts should be monitored.

## Summary

MITRE ATT&CK mapping helps defenders understand attacker behavior in a standard format. This mapping can guide detection improvements, identify monitoring gaps, and strengthen incident response procedures for Remcos-related activity.
