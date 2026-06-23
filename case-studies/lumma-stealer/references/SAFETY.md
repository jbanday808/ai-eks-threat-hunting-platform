# Malware Analysis Safety Notes

## Safety Rules
- Do not execute live malware on a personal machine.
- Do not download malware outside an isolated lab.
- Do not store real credentials, tokens, or secrets in this repository.
- Do not upload active malware to GitHub.
- Do not include live C2 domains unless they are defanged.
- Use simulated logs and public threat intelligence when possible.

## Token Safety
If a GitHub Personal Access Token was ever placed in a document, README, screenshot, or repository, it should be treated as compromised and revoked immediately.

## Safe Alternatives
- Use defanged IOCs.
- Use screenshots with secrets removed.
- Use simulated Splunk, Zeek, and Suricata logs.
- Use public reports for behavior-based detection logic.

## Summary
This project is for defensive learning, SOC analysis, and detection engineering only.