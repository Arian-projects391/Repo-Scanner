import json
from pathlib import Path

# Path to your scan report
report_path = Path.home() / "repo-scanner" / "scan-report.json"

if not report_path.exists():
    print(f"Report file not found at {report_path}")
    exit(1)

# Load JSON
with open(report_path, "r") as f:
    report = json.load(f)

# Print clean summary
print(f"\n=== Scan Summary for {report.get('repo')} ===\n")

# Semgrep
semgrep_summary = report.get("semgrep", {}).get("error", "").strip()
print("Semgrep Results:")
print(semgrep_summary or "No Semgrep output.\n")

# TruffleHog
trufflehog_output = report.get("trufflehog", {}).get("output", "").strip()
trufflehog_error = report.get("trufflehog", {}).get("error", "").strip()
print("\nTruffleHog Results:")
if trufflehog_output or trufflehog_error:
    print(trufflehog_output or trufflehog_error)
else:
    print("No secrets found.\n")

# pip-audit
pip_output = report.get("pip_audit", {}).get("output", "").strip()
pip_error = report.get("pip_audit", {}).get("error", "").strip()
print("\npip-audit Results:")
if pip_output or pip_error:
    print(pip_output or pip_error)
else:
    print("No Python package vulnerabilities found.\n")
