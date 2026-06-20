# Remcos YARA Rule

## What Is YARA?

YARA is a defensive security tool that identifies files by looking for defined patterns. It works like a search checklist for characteristics that may appear in malware.

## Why This Rule Was Created

The `Remcos_Combined_Static_IOC` rule was created to detect files that share validated characteristics with the investigated Remcos sample. It checks for a Windows executable header, a small file size, UPX packing markers, and several Windows API names associated with loading code, allocating memory, and network access.

The rule requires multiple indicators to reduce matches on unrelated files. A match is a reason for investigation, not proof by itself that a file is malicious.

## Detection Result

The rule matched the investigated Remcos sample successfully. The recorded result is available in [remcos_yara_results.txt](../../results/yara/remcos_yara_results.txt).
