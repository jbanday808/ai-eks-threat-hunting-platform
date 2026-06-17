# AI Alert Triage Framework

This folder contains the initial AI triage phase for the AI-Powered EKS Threat Hunting & Incident Response Platform.

The goal is to turn raw Falco runtime alerts into clear security summaries, MITRE ATT&CK context, and practical response recommendations.

## Purpose

Falco alerts are useful, but raw alert data can be difficult for non-specialists to interpret quickly. This framework shows how security events can be parsed, summarized, and converted into incident-response-ready information.

This phase is intentionally simple and portfolio-friendly. It uses local JSON files and a Python script so the workflow is easy to understand, run, and extend.

## Workflow

```text
Falco Alert JSON
  -> triage.py
  -> Severity Extraction
  -> MITRE ATT&CK Mapping
  -> Summary Generation
  -> Recommended Actions
  -> Incident Report Draft
```

## Included Sample Alerts

| Alert | Scenario | MITRE ATT&CK |
| ----- | -------- | ------------ |
| `terminal-shell-t1059.json` | Shell spawned inside a container | T1059 |
| `write-under-etc-t1037.json` | File write under `/etc` inside a container | T1037 |
| `suspicious-exec.json` | Kubernetes exec-like shell activity | T1059 |

## Business Value

This framework helps demonstrate how runtime security alerts can support real incident response workflows.

Key benefits:

- Reduces time spent manually reading raw alert JSON
- Connects technical alerts to attacker behavior
- Produces clearer summaries for analysts and stakeholders
- Creates repeatable triage logic for future automation
- Provides a foundation for AI-assisted security operations

## Run Locally

From the repository root:

```bash
python3 ai-triage/triage.py
```

Analyze one alert:

```bash
python3 ai-triage/triage.py ai-triage/sample-alerts/terminal-shell-t1059.json
```

Analyze all sample alerts:

```bash
python3 ai-triage/triage.py ai-triage/sample-alerts/*.json
```

## Future OpenAI Integration

Future versions can send normalized Falco alert data to an OpenAI model to generate richer triage outputs.

Planned enhancements:

- Natural-language incident summaries
- Risk scoring based on severity and workload context
- Suggested containment steps
- MITRE ATT&CK enrichment
- Automated incident report generation
- Integration with ticketing, chat, or SIEM workflows

No API keys or secrets are stored in this project.
