# Splunk Detection Summary

## Overview

Splunk is a platform that collects and searches security logs from computers, network devices, and other systems. During an investigation, it helps analysts bring different evidence into one place, find suspicious activity, and build a timeline of what happened.

The examples below show how defenders could investigate the validated Remcos RAT indicators. Field names and index names may need to be adjusted for the local Splunk environment.

## Investigation Use Cases

- Search for SHA256 hash `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a`
- Search for domain `eastvillageeatery.de`
- Search for IP `104.21.53.137`
- Search for IP `172.67.213.98`
- Investigate process execution
- Investigate persistence activity

## Example Searches

### SHA256 Hash

```spl
index=* earliest=-30d
"a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a"
| table _time host source sourcetype user file_name file_path process_name
| sort 0 _time
```

This search finds logs containing the investigated file hash and shows the systems and files connected to it.

### Domain

```spl
index=* earliest=-30d
"eastvillageeatery.de"
| table _time host source sourcetype src_ip dest_ip query domain process_name
| sort 0 _time
```

This search looks for DNS, proxy, firewall, or endpoint events involving the investigated domain.

### IP Addresses

```spl
index=* earliest=-30d
("104.21.53.137" OR "172.67.213.98")
| table _time host source sourcetype src_ip src_port dest_ip dest_port process_name action
| sort 0 _time
```

This search identifies events involving either investigated IP address and helps show which internal systems communicated with them.

### Process Execution

```spl
index=* earliest=-30d (EventCode=1 OR event_id=1)
(process_name="eastvillageeatery.exe" OR process_name="7hr8ftfxm.exe" OR Image="*\\eastvillageeatery.exe" OR Image="*\\7hr8ftfxm.exe")
| table _time host user parent_process_name process_name Image CommandLine
| sort 0 _time
```

This search reviews process creation logs for filenames identified during the Remcos investigation.

### Registry Run-Key Persistence

```spl
index=* earliest=-30d (EventCode=13 OR event_id=13)
(TargetObject="*\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*" OR TargetObject="*\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\*")
(TargetObject="*eastvillageeatery*" OR Details="*eastvillageeatery.exe*" OR Details="*7hr8ftfxm.exe*")
| table _time host user process_name Image TargetObject Details
| sort 0 _time
```

This search looks for known Remcos-related names being written to registry locations that can start programs automatically when a user signs in.

## Expected Findings

An analyst would look for several related events rather than relying on one match.

| Evidence | What to Review |
| --- | --- |
| Hash match | The affected host, file path, user, and security action taken |
| Domain match | The requesting host, process, time, and returned IP address |
| IP match | The source host, destination port, connection frequency, and allow or block result |
| Process event | The parent process, executable path, user, and nearby file activity |
| Registry event | The process that changed the Run key and the value that was written |
| Repeated activity | Regular connections or recurring events that may indicate persistence or beaconing |

IP addresses can be shared by unrelated services, so analysts should confirm IP matches with domain, process, file, and time-based evidence.

## Summary

Splunk improves visibility by connecting endpoint, DNS, network, and registry events in one searchable location. Correlating multiple Remcos indicators can help defenders identify affected systems, understand the activity timeline, and support an informed incident response.
