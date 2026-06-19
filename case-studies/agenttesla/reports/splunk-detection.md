# Splunk Detection - AgentTesla

These searches are defensive examples based on the completed AgentTesla investigation. Field names may need adjustment for the local Splunk index, sourcetype, or data model.

## DNS Detection

Use this search to find known suspicious domains from the investigation.

```spl
index=* (sourcetype=zeek:dns OR sourcetype=bro:dns OR sourcetype=dns)
query IN ("corwineagles.com", "ftp.corwineagles.com", "drive.google.com", "drive.usercontent.google.com", "ip-api.com")
| stats count min(_time) as first_seen max(_time) as last_seen values(query) as domains by src_ip
| convert ctime(first_seen) ctime(last_seen)
```

## FTP Exfiltration Detection

Use this search to identify FTP upload behavior. In this investigation, the `STOR` command was the key FTP upload indicator.

```spl
index=* (sourcetype=zeek:ftp OR sourcetype=bro:ftp OR sourcetype=ftp)
(command=STOR OR request="STOR*" OR ftp_command=STOR)
| stats count min(_time) as first_seen max(_time) as last_seen values(command) as commands values(arg) as filenames by src_ip dest_ip user
| convert ctime(first_seen) ctime(last_seen)
```

## Beaconing Detection

Use this search to look for repeated communication from a source host to the same external destination.

```spl
index=* (sourcetype=zeek:conn OR sourcetype=bro:conn OR sourcetype=zeek:dns OR sourcetype=bro:dns)
| bin _time span=5m
| stats count dc(_time) as time_buckets min(_time) as first_seen max(_time) as last_seen by src_ip dest_ip query
| where count >= 5 OR time_buckets >= 3
| convert ctime(first_seen) ctime(last_seen)
```

## Credential File Pattern Detection

Use this search to find file names linked to possible credential or contact collection.

```spl
index=* (sourcetype=zeek:files OR sourcetype=bro:files OR sourcetype=suricata)
("Contacts_Thunderbird" OR "PW_")
| stats count min(_time) as first_seen max(_time) as last_seen values(filename) as filenames values(dest_ip) as destinations by src_ip
| convert ctime(first_seen) ctime(last_seen)
```

## Correlation Search Examples

Use this search to combine DNS, FTP, and file-name indicators. Hosts with multiple indicator types should receive higher analyst priority.

```spl
index=* ("ftp.corwineagles.com" OR "corwineagles.com" OR "drive.google.com" OR "drive.usercontent.google.com" OR "ip-api.com" OR "Contacts_Thunderbird" OR "PW_" OR "STOR")
| eval indicator=case(
    like(_raw, "%ftp.corwineagles.com%"), "ftp_domain",
    like(_raw, "%corwineagles.com%"), "domain",
    like(_raw, "%drive.google.com%"), "staging_domain",
    like(_raw, "%drive.usercontent.google.com%"), "staging_domain",
    like(_raw, "%ip-api.com%"), "ip_lookup",
    like(_raw, "%Contacts_Thunderbird%"), "contact_file",
    like(_raw, "%PW_%"), "password_file",
    like(_raw, "%STOR%"), "ftp_upload",
    true(), "other")
| stats count values(indicator) as indicators values(dest_ip) as destinations min(_time) as first_seen max(_time) as last_seen by src_ip
| where mvcount(indicators) >= 2
| convert ctime(first_seen) ctime(last_seen)
```

## Alert Severity

| Severity | Condition | Analyst Priority |
| --- | --- | --- |
| High | Suspicious DNS plus FTP `STOR` plus credential-themed file names. | Treat as likely credential exposure and possible exfiltration. |
| Medium | Suspicious DNS plus repeated beaconing from one host. | Investigate host activity and endpoint telemetry. |
| Medium | FTP `STOR` to an unusual external destination. | Confirm business need and review transferred file names. |
| Low | Single suspicious domain hit without supporting evidence. | Enrich with DNS, proxy, endpoint, and threat intelligence context. |

## Analyst Response Procedures

1. Identify the source host and user account.
2. Check whether the DNS domains and FTP destination are expected for the environment.
3. Review Zeek `dns.log`, `conn.log`, `http.log`, `ftp.log`, and `files.log` for the same timeframe.
4. Review Suricata `fast.log` and `eve.json` for related alerts.
5. Search endpoint telemetry for credential access, suspicious file creation, and unusual network connections.
6. Isolate the host if credential theft or exfiltration is suspected.
7. Reset credentials used on the affected host.
8. Preserve evidence and document findings in the incident report.
