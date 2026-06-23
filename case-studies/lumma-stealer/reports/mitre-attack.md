# Lumma Stealer MITRE ATT&CK Mapping

## T1059 – Command and Scripting Interpreter

Evidence:

* `Invoice_2026.exe` executed in the Windows lab
* Noriben recorded process activity
* Process Monitor recorded process start, thread creation, and process exit

Simple Explanation:

The malware was launched and ran on the Windows analysis system.

Why It Matters:

Execution is the first step malware needs before it can perform harmful actions.

## T1057 – Process Discovery

Evidence:

* `main.findLsassProcess`

Simple Explanation:

The malware looked for important running processes on the computer.

Why It Matters:

Attackers often search for sensitive processes that may contain credentials or system information.

## T1082 – System Information Discovery

Evidence:

* `os.Getpid`
* `main.NtQuerySystemHandles`

Simple Explanation:

The malware collected information about the computer and running system resources.

Why It Matters:

This helps attackers understand the infected system before taking further action.

## T1555 – Credentials from Password Stores

Evidence:

* `main.getChromeLogins`
* `main.getEdgeLogins`
* `SELECT origin_url`
* `SELECT username_value`
* `SELECT password_value`

Simple Explanation:

The malware attempted to access saved browser usernames and passwords.

Why It Matters:

Saved browser credentials can give attackers access to personal, business, and cloud accounts.

## T1555.003 – Credentials from Web Browsers

Evidence:

* `main.GetChromiumMasterKeys`
* `main.getChromeLogins`
* `main.getEdgeLogins`

Simple Explanation:

The malware specifically targeted Chromium-based browsers like Chrome and Edge.

Why It Matters:

Many users save passwords in browsers, making them a high-value target.

## T1552 – Unsecured Credentials

Evidence:

* `Password`
* `EncryptedPassword`
* `main.loginPBE.Decrypt`
* `main.DPAPI`

Simple Explanation:

The malware attempted to unlock and read protected password data stored on the computer.

Why It Matters:

This behavior can expose credentials that users believe are safely stored.

## T1005 – Data from Local System

Evidence:

* Chrome Login Data
* Edge Login Data
* Passwords
* Cookies
* `main.readProcFile`

Simple Explanation:

The malware attempted to collect data stored locally on the infected system.

Why It Matters:

Collected data may contain passwords, session cookies, and other sensitive information.

## T1134 – Access Token Manipulation

Evidence:

* `main.getSystemToken`
* `main.impersonateSystem`

Simple Explanation:

The malware contained functions that may allow it to act with higher system privileges.

Why It Matters:

Higher privileges can allow malware to access more sensitive areas of the system.

## T1548 – Abuse Elevation Control Mechanism

Evidence:

* `main.enablePrivilege`

Simple Explanation:

The malware attempted to increase its permissions on the system.

Why It Matters:

More permissions give malware more control over the infected machine.

## Summary

| Tactic            | Technique                         | ID        | Simple Explanation                           |
| ----------------- | --------------------------------- | --------- | -------------------------------------------- |
| Execution         | Command and Scripting Interpreter | T1059     | Malware ran on the system                    |
| Discovery         | Process Discovery                 | T1057     | Malware looked for running processes         |
| Discovery         | System Information Discovery      | T1082     | Malware collected system details             |
| Credential Access | Credentials from Password Stores  | T1555     | Malware targeted saved passwords             |
| Credential Access | Credentials from Web Browsers     | T1555.003 | Malware targeted Chrome and Edge credentials |
| Credential Access | Unsecured Credentials             | T1552     | Malware attempted to decrypt password data   |
| Collection        | Data from Local System            | T1005     | Malware collected local system data          |
| Defense Evasion   | Access Token Manipulation         | T1134     | Malware attempted higher-level access        |
| Defense Evasion   | Abuse Elevation Control Mechanism | T1548     | Malware attempted privilege escalation       |
