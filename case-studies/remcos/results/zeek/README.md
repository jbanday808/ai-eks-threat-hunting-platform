# Zeek Network Analysis: Remcos RAT

## Overview

Zeek is a network security monitoring tool that records detailed network activity and helps analysts investigate suspicious communications. Defenders use its structured logs to understand which systems communicated, where they connected, and how often the activity occurred. Zeek provides visibility and evidence but does not block traffic by itself.

## Investigation Objectives

| Objective | Purpose |
| --- | --- |
| Identify suspicious communications | Detect possible command-and-control activity |
| Review DNS activity | Identify malicious domains |
| Analyze connections | Find unusual external communications |
| Correlate indicators | Match network activity to threat intelligence |

## Relevant Zeek Logs

| Log | Purpose |
| --- | --- |
| `conn.log` | Records network connections |
| `dns.log` | Records DNS queries and responses |
| `http.log` | Records HTTP activity |
| `ssl.log` | Records TLS/SSL communications |

## Threat Intelligence Indicators

| Type | Indicator |
| --- | --- |
| Domain | `eastvillageeatery.de` |
| IP | `104.21.53.137` |
| IP | `172.67.213.98` |
| SHA256 | `a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a` |

## Example Threat Hunting Workflow

### Step 1: Review `conn.log`

- Look for repeated outbound connections.
- Identify communication with known malicious IP addresses.
- Review connection frequency and duration.

```text
Search conn.log for:
104.21.53.137
172.67.213.98
```

An analyst would record the internal source system, destination port, connection status, duration, and amount of data transferred.

### Step 2: Review `dns.log`

- Search for requests to the investigated domain.
- Identify the internal system that made each request.
- Compare returned addresses with the known IP indicators.

```text
Search dns.log for:
eastvillageeatery.de
```

Repeated successful or failed lookups can help build a timeline of suspicious activity.

### Step 3: Review `http.log` and `ssl.log`

- Check HTTP host fields for the investigated domain.
- Review TLS server names and connection timestamps.
- Correlate matching activity with the same source system in `conn.log`.

```text
Search http.log and ssl.log for:
eastvillageeatery.de
```

Encrypted traffic may hide content, but connection details and visible server names can still provide useful evidence.

### Step 4: Identify Possible Beaconing

Beaconing is repeated communication at regular or near-regular times. Analysts would look for:

- Repeated connections from one system to the same destination
- Similar time gaps between connections
- Similar connection durations or data sizes
- Short connections continuing over a long period

Scheduled business software can create similar patterns, so beaconing should be confirmed with endpoint and threat intelligence evidence.

### Step 5: Correlate the Evidence

| Evidence | Correlation Goal |
| --- | --- |
| Domain match | Identify the requesting system and returned IP address |
| IP match | Confirm related outbound connections and timing |
| Repeated connections | Determine whether the activity follows a beaconing pattern |
| SHA256 match | Link endpoint file evidence to network activity from the same host |

Zeek network logs do not normally identify a local executable by SHA256. Analysts should correlate the file hash from endpoint security data with Zeek activity using the host and event time.

## Expected Findings

An analyst would look for multiple related events, such as a DNS request for `eastvillageeatery.de`, a connection to an associated IP address, and a matching endpoint detection on the same system. A single IP match is not proof of compromise because IP addresses may host unrelated services.

## Summary

Zeek supports Remcos threat hunting by recording DNS, connection, HTTP, and TLS activity in searchable logs. Correlating these records with the completed investigation indicators helps defenders identify affected systems, understand communication patterns, and support incident response.
