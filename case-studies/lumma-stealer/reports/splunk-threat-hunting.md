# Splunk Threat Hunting Report

## Hunting Goals

Search for indicators related to Lumma Stealer execution, credential theft, and Defender detections.

## Example SPL Queries

Search for Defender detections:

```spl
index=* ("Trojan:Win32/SalatStealer" OR "Behavior:Win32/PFAppMultiStepRem.A")
```

Search for malware filename:

```spl
index=* "Invoice_2026.exe"
```

Search for suspicious browser credential access:

```spl
index=* ("Login Data" OR "Cookies" OR "Local State" OR "Web Data")
```

Search for suspicious process behavior:

```spl
index=* ("main.GetChromiumMasterKeys" OR "main.getChromeLogins" OR "main.getEdgeLogins")
```

## Analyst Summary

These searches help identify systems that may have executed Lumma Stealer or accessed browser credential storage in a suspicious way.
