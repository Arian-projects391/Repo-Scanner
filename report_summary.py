import json
import sys

def summarize_report(report_file):
    with open(report_file, "r") as f:
        data = json.load(f)

    print(f"\n=== Scan Summary for {data['repo']} ===\n")

    # Semgrep summary
    sem = data.get("semgrep", {})
    print("Semgrep Results:")
    if sem.get("output"):
        print("Scan completed, see detailed JSON output.")
    if sem.get("error"):
        print("Errors / Status:\n", sem["error"])

    # TruffleHog summary
    th = data.get("trufflehog", {})
    print("\nTruffleHog Results:")
    if th.get("output"):
        print(th["output"])
    else:
        print("No secrets found." if not th.get("error") else th.get("error"))

    # pip-audit summary
    pa = data.get("pip_audit", {})
    print("\npip-audit Results:")
    if pa.get("output"):
        print(pa["output"])
    else:
        print(pa.get("error", "No output"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 report_summary.py <scan-report-file.json>")
        sys.exit(1)

    report_file = sys.argv[1]
    summarize_report(report_file)
