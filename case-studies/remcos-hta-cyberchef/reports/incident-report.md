# RemcosRAT HTA Incident Report

## Executive Summary

The investigation identified an obfuscated HTA-based loader associated with RemcosRAT. The file concealed PowerShell and Base64-encoded content designed to retrieve data and load .NET code into memory. Noriben recorded a connection to `66.63.170.34:80`, and Microsoft Defender detected and remediated the malicious activity.

Final verification found no active RemcosRAT process, no Caspol process, and no persistence.

Simple explanation: A concealed remote-access threat attempted to communicate externally, but Defender removed it and no continuing infection was found.

## Incident Overview

| Field | Finding |
| --- | --- |
| Threat family | RemcosRAT |
| Investigated file | `shell.hta` |
| Delivery context | Phishing-related HTA |
| Observed connection | `66.63.170.34:80` over HTTP |
| Endpoint response | Microsoft Defender detection and remediation |
| Final status | No active process or persistence found |

## What Happened

The HTA used `boroc` obfuscation and Base64 encoding to conceal a PowerShell loader. Defensive analysis showed references to `optimized_MSI.png`, string extraction and transformation steps, and .NET memory-loading functions. Noriben then recorded PowerShell attempting an external HTTP connection.

Simple explanation: The file used several layers to make harmful behavior difficult to recognize.

## Detection and Response

| Question | Answer |
| --- | --- |
| What was detected? | Concealed PowerShell activity, decoding behavior, memory-loading references, and an external connection. |
| What was blocked? | Microsoft Defender detected and remediated the malicious PowerShell activity. |
| Was malware still running? | No active RemcosRAT or Caspol process was found during verification. |
| Was persistence found? | No persistence was observed after remediation. |

## Indicators

The investigation identified the IP addresses `66.63.170.34` and `173.231.188.244`, the domains `as.al` and `geoplugin.net`, the filename `shell.hta`, and SHA256 `d113f72b9248e3a89d72d1238a8465af7857822b82951681cff22391ffff3039`. These indicators should be reviewed with endpoint, DNS, proxy, and timing context.

## Conclusion

The investigation produced clear file, network, and behavior evidence for defensive hunting. Microsoft Defender remediated the threat, and the post-analysis checks found no active infection or persistence.

[Back to the case study](../README.md)
