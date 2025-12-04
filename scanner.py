import os
import subprocess
import json
import tempfile
import shutil
from pathlib import Path

# -----------------------------
# Helper: run shell commands
# -----------------------------
def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

# -----------------------------
# Run Semgrep
# -----------------------------
def run_semgrep(repo_path):
    semgrep_bin = str(Path.home() / "repo-scanner/.venv/bin/semgrep")
    cmd = [semgrep_bin, "scan", "--json", "--severity=INFO", repo_path]
    out, err = run_cmd(cmd)
    return {"output": out, "error": err}

# -----------------------------
# Run TruffleHog
# -----------------------------
def run_trufflehog(repo_path):
    trufflehog_bin = str(Path.home() / "repo-scanner/.venv/bin/trufflehog")
    cmd = [trufflehog_bin, "--json", repo_path]
    out, err = run_cmd(cmd)
    return {"output": out, "error": err}

# -----------------------------
# Run pip-audit
# -----------------------------
def run_pip_audit(repo_path):
    # Look for requirements.txt in the repo
    req_files = list(Path(repo_path).rglob("requirements.txt"))
    results = []
    for req_file in req_files:
        cmd = ["pip-audit", "-r", str(req_file), "--json"]
        out, err = run_cmd(cmd)
        results.append({"file": str(req_file), "output": out, "error": err})
    return results

# -----------------------------
# Main scanning function
# -----------------------------
def scan_repo(git_url):
    report_data = {}

    # Create a temporary directory for cloning
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        print("[+] Cloning repository…")
        clone_cmd = ["git", "clone", "--depth", "1", git_url, str(tmp_path)]
        out, err = run_cmd(clone_cmd)
        if err:
            print(f"[-] Failed to clone repository:\n{err}")
            return

        # Run Semgrep
        print("[+] Running Semgrep…")
        report_data["semgrep"] = run_semgrep(tmp_path)

        # Run TruffleHog
        print("[+] Running TruffleHog…")
        report_data["trufflehog"] = run_trufflehog(tmp_path)

        # Run pip-audit
        print("[+] Running pip-audit…")
        report_data["pip_audit"] = run_pip_audit(tmp_path)

    # Save report
    reports_dir = Path.home() / "repo-scanner" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / "scan-report.json"

    with open(report_path, "w") as f:
        json.dump(report_data, f, indent=4)

    print(f"[✓] Scan complete! Report saved to {report_path}")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    git_url = input("Enter git clone URL: ").strip()
    if git_url:
        scan_repo(git_url)
    else:
        print("[-] No URL provided.")
