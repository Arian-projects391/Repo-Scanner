import os
import subprocess
import json
import tempfile
import shutil
import time
from pathlib import Path

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def run_semgrep(repo_path):
    semgrep_bin = str(Path.home() / "semgrep-venv/bin/semgrep")
    cmd = [semgrep_bin, "scan", "--json", "--severity=INFO", repo_path]
    out, err = run_cmd(cmd)
    return {"output": out, "error": err}

def run_trufflehog(repo_path):
    trufflehog_bin = str(Path.home() / "trufflehog-venv/bin/trufflehog")
    cmd = [trufflehog_bin, "--json", repo_path]
    out, err = run_cmd(cmd)
    return {"output": out, "error": err}

def run_pip_audit(repo_path):
    req_file = Path(repo_path) / "requirements.txt"
    if not req_file.exists():
        return {"output": "", "error": "No requirements.txt found"}
    cmd = ["pip-audit", "-r", str(req_file), "--json"]
    out, err = run_cmd(cmd)
    return {"output": out, "error": err}

def main():
    git_url = input("Enter git clone URL: ").strip()
    repo_name = git_url.rstrip("/").split("/")[-1]
    tmp_dir = tempfile.mkdtemp()
    repo_path = os.path.join(tmp_dir, repo_name)

    print("[+] Cloning repository…")
    out, err = run_cmd(["git", "clone", git_url, repo_path])
    if err and "fatal" in err.lower():
        print("[-] Failed to clone repository:\n", err)
        shutil.rmtree(tmp_dir)
        return

    print("[+] Running Semgrep…")
    semgrep_results = run_semgrep(repo_path)

    print("[+] Running TruffleHog…")
    trufflehog_results = run_trufflehog(repo_path)

    print("[+] Running pip-audit…")
    pip_audit_results = run_pip_audit(repo_path)

    shutil.rmtree(tmp_dir)

    timestamp = int(time.time())
    report_file = f"scan-report_{repo_name}_{timestamp}.json"

    report = {
        "repo": git_url,
        "semgrep": semgrep_results,
        "trufflehog": trufflehog_results,
        "pip_audit": pip_audit_results
    }

    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)

    print(f"[+] Scan complete! Report saved to {report_file}")

if __name__ == "__main__":
    main()
