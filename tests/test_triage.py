from __future__ import annotations

import importlib.util
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRIAGE_PATH = PROJECT_ROOT / "ai-triage" / "triage.py"
SAMPLE_ALERT_DIR = PROJECT_ROOT / "ai-triage" / "sample-alerts"


def load_triage_module():
    spec = importlib.util.spec_from_file_location("triage", TRIAGE_PATH)
    assert spec is not None
    assert spec.loader is not None

    triage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(triage)
    return triage


def test_sample_alert_files_exist():
    sample_alerts = sorted(SAMPLE_ALERT_DIR.glob("*.json"))

    assert sample_alerts
    assert (SAMPLE_ALERT_DIR / "terminal-shell-t1059.json").exists()
    assert (SAMPLE_ALERT_DIR / "write-under-etc-t1037.json").exists()


def test_triage_can_process_sample_alerts():
    triage = load_triage_module()
    sample_alerts = sorted(SAMPLE_ALERT_DIR.glob("*.json"))

    for alert_path in sample_alerts:
        analysis = triage.analyze_alert(alert_path)
        output = triage.triage_output(analysis)

        assert analysis["summary"]
        assert analysis["actions"]
        assert "MITRE ATT&CK" in output
        assert "Recommended Actions" in output


def test_incident_report_can_be_generated(tmp_path, monkeypatch):
    triage = load_triage_module()
    monkeypatch.setattr(triage, "REPORT_DIR", tmp_path)

    alert_path = SAMPLE_ALERT_DIR / "terminal-shell-t1059.json"
    analysis = triage.analyze_alert(alert_path)
    report_path = triage.write_report(analysis)

    assert report_path.exists()
    assert report_path.parent == tmp_path

    report = report_path.read_text(encoding="utf-8")
    assert "# Incident Report" in report
    assert "## Incident Summary" in report
    assert "## Recommended Actions" in report
