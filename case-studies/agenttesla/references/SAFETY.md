# Safety Notice

This case study is for defensive malware analysis, detection engineering, and incident response documentation only.

## Handling Rules

- Do not upload live malware samples to this repository.
- Do not commit PCAPs, email samples, credentials, private keys, or sensitive customer data.
- Do not include malware execution steps or instructions for reproducing compromise.
- Store only sanitized screenshots, logs, reports, detections, and indicators.
- Perform any malware analysis only in an isolated lab with no shared folders, no personal accounts, and no production access.

## Safe Lab Practices

- Use disposable virtual machines for malware analysis work.
- Keep lab systems separated from home, school, business, and production networks.
- Do not sign in with personal or work accounts from analysis systems.
- Preserve evidence in a controlled location and sanitize it before publishing.
- Share only defensive findings, detections, and high-level incident response lessons.

## Repository Scope

The included Suricata, YARA, Splunk, and report files are intended to help defenders identify suspicious AgentTesla-style behavior. They are not intended to enable malware operation, delivery, persistence, or evasion.

## Defensive Use

Use this material to:

- Document incident response findings.
- Build detection logic for DNS, HTTP, FTP, and file indicators.
- Map observed activity to MITRE ATT&CK.
- Practice safe reporting and portfolio presentation.

If sensitive evidence is needed for private review, keep it outside the repository and follow the organization handling policy.
