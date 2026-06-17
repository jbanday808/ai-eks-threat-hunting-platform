#!/usr/bin/env python3
"""Simple Falco alert triage helper.

This script reads Falco-style JSON alerts, extracts useful security context,
maps alerts to MITRE ATT&CK where possible, and prints a concise triage summary.
It is intentionally lightweight so the workflow is easy to review in a portfolio.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_ALERT_DIR = Path(__file__).resolve().parent / "sample-alerts"
REPORT_DIR = Path(__file__).resolve().parent / "reports"

TECHNIQUE_DETAILS = {
    "T1059": {
        "name": "Command and Scripting Interpreter",
        "description": "Adversaries may abuse command-line shells to execute commands.",
    },
    "T1037": {
        "name": "Boot or Logon Initialization Scripts",
        "description": "Adversaries may modify startup or system configuration paths for persistence.",
    },
}


def load_alert(path: Path) -> dict[str, Any]:
    """Load one alert JSON file from disk."""
    with path.open("r", encoding="utf-8") as alert_file:
        return json.load(alert_file)


def extract_technique(alert: dict[str, Any]) -> str:
    """Find the first MITRE ATT&CK technique ID in the alert tags."""
    tags = alert.get("tags", [])
    for tag in tags:
        if isinstance(tag, str) and tag.startswith("T") and tag[1:].isdigit():
            return tag
    return "Unknown"


def build_summary(alert: dict[str, Any], technique: str) -> str:
    """Create a short human-readable summary from Falco alert fields."""
    rule = alert.get("rule", "Unknown rule")
    priority = alert.get("priority", "UNKNOWN")
    output_fields = alert.get("output_fields", {})
    namespace = output_fields.get("k8s.ns.name", "unknown namespace")
    pod = output_fields.get("k8s.pod.name", "unknown pod")
    command = output_fields.get("proc.cmdline", "unknown command")

    return (
        f"{priority} alert from rule '{rule}' in pod '{pod}' "
        f"within namespace '{namespace}'. Observed command: {command}. "
        f"Mapped MITRE ATT&CK technique: {technique}."
    )


def risk_assessment(alert: dict[str, Any], technique: str) -> str:
    """Explain the risk in plain language for analyst and stakeholder review."""
    priority = alert.get("priority", "UNKNOWN").upper()

    if technique == "T1059":
        return (
            f"{priority} risk: shell or exec activity inside a container may indicate "
            "hands-on-keyboard access, troubleshooting activity, or unauthorized command execution."
        )
    if technique == "T1037":
        return (
            f"{priority} risk: writes under /etc may indicate configuration tampering, "
            "persistence preparation, or an unexpected change to a sensitive system path."
        )
    return (
        f"{priority} risk: the alert should be reviewed because the behavior was unusual "
        "or did not include a known MITRE ATT&CK mapping."
    )


def recommended_actions(alert: dict[str, Any], technique: str) -> list[str]:
    """Generate practical response actions based on the mapped technique."""
    rule = alert.get("rule", "").lower()

    actions = [
        "Review the affected pod, namespace, container image, and user context.",
        "Validate whether the activity was expected administrative behavior.",
        "Preserve relevant logs and alert details for investigation.",
    ]

    if technique == "T1059" or "shell" in rule or "exec" in rule:
        actions.extend(
            [
                "Identify who initiated the shell or exec session.",
                "Check for follow-on commands, privilege escalation, or lateral movement.",
                "Consider isolating or restarting the workload if the activity is unauthorized.",
            ]
        )
    elif technique == "T1037" or "/etc" in rule:
        actions.extend(
            [
                "Review the file path that was modified and compare it with the expected baseline.",
                "Inspect the container image and deployment configuration for unauthorized changes.",
                "Redeploy from a trusted image if persistence or tampering is suspected.",
            ]
        )
    else:
        actions.append("Escalate to a security analyst if the behavior cannot be explained.")

    return actions


def alert_context(alert: dict[str, Any]) -> dict[str, str]:
    """Normalize common Falco fields so reports stay easy to build."""
    output_fields = alert.get("output_fields", {})
    return {
        "rule": str(alert.get("rule", "Unknown")),
        "severity": str(alert.get("priority", "UNKNOWN")),
        "namespace": str(output_fields.get("k8s.ns.name", "unknown namespace")),
        "pod": str(output_fields.get("k8s.pod.name", "unknown pod")),
        "command": str(output_fields.get("proc.cmdline", "unknown command")),
    }


def analyze_alert(path: Path) -> dict[str, Any]:
    """Load one alert and calculate all derived triage fields."""
    alert = load_alert(path)
    technique = extract_technique(alert)
    details = TECHNIQUE_DETAILS.get(
        technique,
        {
            "name": "Unknown technique",
            "description": "No MITRE ATT&CK mapping was found in the alert tags.",
        },
    )

    return {
        "path": path,
        "alert": alert,
        "context": alert_context(alert),
        "technique": technique,
        "technique_details": details,
        "summary": build_summary(alert, technique),
        "risk": risk_assessment(alert, technique),
        "actions": recommended_actions(alert, technique),
    }


def triage_output(analysis: dict[str, Any]) -> str:
    """Build the console triage output for one alert."""
    path = analysis["path"]
    context = analysis["context"]
    technique = analysis["technique"]
    details = analysis["technique_details"]

    lines = [
        f"## Alert Triage: {path.name}",
        "",
        f"- Rule: {context['rule']}",
        f"- Severity: {context['severity']}",
        f"- MITRE ATT&CK: {technique} - {details['name']}",
        f"- Technique Context: {details['description']}",
        "",
        "### Summary",
        "",
        analysis["summary"],
        "",
        "### Recommended Actions",
        "",
    ]

    for action in analysis["actions"]:
        lines.append(f"- {action}")

    lines.append("")
    return "\n".join(lines)


def report_markdown(analysis: dict[str, Any]) -> str:
    """Create a Markdown incident report with the required report sections."""
    context = analysis["context"]
    technique = analysis["technique"]
    details = analysis["technique_details"]

    lines = [
        "# Incident Report",
        "",
        "## Incident Summary",
        "",
        analysis["summary"],
        "",
        "## Severity",
        "",
        context["severity"],
        "",
        "## MITRE ATT&CK Technique",
        "",
        f"{technique} - {details['name']}",
        "",
        "## Detection Rule",
        "",
        context["rule"],
        "",
        "## Namespace",
        "",
        context["namespace"],
        "",
        "## Pod",
        "",
        context["pod"],
        "",
        "## Command Observed",
        "",
        f"`{context['command']}`",
        "",
        "## Risk Assessment",
        "",
        analysis["risk"],
        "",
        "## Recommended Actions",
        "",
    ]

    for action in analysis["actions"]:
        lines.append(f"- {action}")

    lines.append("")
    return "\n".join(lines)


def write_report(analysis: dict[str, Any]) -> Path:
    """Write one report file using a timestamped incident filename."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")

    # Microseconds keep filenames unique during multi-alert runs.
    report_path = REPORT_DIR / f"incident-{timestamp}.md"
    report_path.write_text(report_markdown(analysis), encoding="utf-8")
    return report_path


def alert_paths_from_args(args: list[str]) -> list[Path]:
    """Use provided alert paths, or default to every JSON file in sample-alerts."""
    if args:
        return [Path(arg) for arg in args]
    return sorted(DEFAULT_ALERT_DIR.glob("*.json"))


def main() -> int:
    """Entry point for command-line usage."""
    alert_paths = alert_paths_from_args(sys.argv[1:])

    if not alert_paths:
        print("No alert JSON files found.", file=sys.stderr)
        return 1

    for path in alert_paths:
        if not path.exists():
            print(f"Alert file not found: {path}", file=sys.stderr)
            return 1
        analysis = analyze_alert(path)
        report_path = write_report(analysis)
        print(triage_output(analysis))
        print(f"Generated report: {report_path}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
