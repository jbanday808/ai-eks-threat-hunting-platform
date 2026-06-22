# RemcosRAT HTA MITRE ATT&CK Mapping

## Overview

MITRE ATT&CK translates the HTA findings into standard behavior categories used by SOC teams, threat hunters, and incident responders.

## Technique Mapping

| Tactic | Technique | ID | Evidence |
| --- | --- | --- | --- |
| Initial Access | Phishing | T1566 | The investigated material used phishing-related HTA delivery. |
| Execution | System Binary Proxy Execution: Mshta | T1218.005 | `shell.hta` used the Windows HTML Application path. |
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 | The HTA concealed a PowerShell loader. |
| Defense Evasion | Obfuscated Files or Information | T1027 | Repeated `boroc` text, character replacement, string reversal, and Base64 concealed the loader. |
| Defense Evasion | Deobfuscate/Decode Files or Information | T1140 | The loading chain transformed and decoded hidden content. |
| Command and Control | Ingress Tool Transfer | T1105 | The loader referenced remotely retrieved content named `optimized_MSI.png`. |
| Command and Control | Application Layer Protocol: Web Protocols | T1071.001 | Noriben recorded PowerShell connecting to `66.63.170.34:80` over HTTP. |
| Defense Evasion | Reflective Code Loading | T1620 | `AppDomain.CurrentDomain.Load` and `Fiber.Program.Main` indicated in-memory .NET loading. |

## Analyst Assessment

The mapping shows a sequence of phishing-related delivery, hidden script execution, external communication, decoding, and memory loading. Microsoft Defender remediated the activity, and verification found no active RemcosRAT or Caspol process and no persistence.

Simple explanation: ATT&CK gives security teams a shared language for understanding the attack and deciding which logs and alerts should detect similar behavior.

[Back to the case study](../README.md)
