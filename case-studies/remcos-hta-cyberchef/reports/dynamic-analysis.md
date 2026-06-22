# RemcosRAT HTA Dynamic Analysis

## Overview

Behavioral evidence was collected in an isolated Windows virtual machine using Noriben and Microsoft Defender. The analysis focused on process, file, registry, and network events, followed by remediation verification.

Simple explanation: Behavioral monitoring recorded what the suspicious loader attempted to do and whether any threat remained afterward.

## Observed Activity

| Evidence source | Finding |
| --- | --- |
| Noriben | PowerShell connected to `66.63.170.34:80` over HTTP. |
| Process monitoring | PowerShell activity was associated with the concealed loader chain. |
| Microsoft Defender | Malicious PowerShell activity was detected and remediated. |
| Post-remediation check | No active RemcosRAT or Caspol process was found. |
| Persistence check | No persistence was observed. |

## Why the Network Finding Matters

The connection to `66.63.170.34:80` confirmed that the loader attempted to communicate with an external system. VirusTotal reputation results supplied additional context that the address had been flagged by security vendors.

An IP reputation match is supporting evidence rather than proof by itself. Analysts should correlate it with the process name, destination port, time, and endpoint activity.

Simple explanation: Noriben connected the suspicious PowerShell process to an external address, giving analysts stronger evidence than reputation data alone.

## Remediation Verification

Microsoft Defender removed the detected threat. Follow-up checks found no active RemcosRAT process, no Caspol process, and no persistence mechanism. This means no continuing infection was verified in the virtual machine after remediation.

## Conclusion

The dynamic evidence confirmed external communication, documented Defender's response, and verified a clean final state based on the available process and persistence checks.

[Back to the case study](../README.md)
