import os
import subprocess
import json
import tempfile
import shutil
import time
from pathlib import Path

# -----------------------------
# Utility Functions
# -----------------------------
def run_cmd(cmd):
    """Run a subprocess command and return stdout and stderr"""
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def is_installed(cmd_name):
    """Check if a command is installed and available in PATH"""
    return shutil.which(cmd_name) is not None

def safe_result(output="", error=""):
    """Always return a dict with output and error keys"""
    return {"output": str(output), "error": str(error)}

# -----------------------------
# Scanners
# -----------------------------
def run_semgrep(repo_path):
    if not is_installed("semgrep"):
        return safe_result(error="Semgrep not installed — skipping.")
    out, err = run_cmd(["semgrep", "scan", "--json", "--severity=INFO", repo_path])
    return safe_result(out, err)

def run_trufflehog(repo_path):
    if not is_installed("trufflehog"):
        return safe_result(error="TruffleHog not installed — skipping.")
    out, err = run_cmd(["trufflehog", "--json", repo_path])
    return safe_result(out, err)

def run_bandit(repo_path):
    if not is_installed("bandit"):
        return safe_result(error="Bandit not installed — skipping.")
    out, err = run_cmd(["bandit", "-r", repo_path, "-f", "json"])
    return safe_result(out, err)

def run_safety(repo_path):
    if not is_installed("safety"):
        return safe_result(error="Safety not installed — skipping.")
    req_file = Path(repo_path) / "requirements.txt"
    if not req_file.exists():
        return safe_result(error="No requirements.txt found for Safety")
    out, err = run_cmd(["safety", "check", "-r", str(req_file), "--json"])
    return safe_result(out, err)

def run_pip_audit(repo_path):
    if not is_installed("pip-audit"):
        return safe_result(error="pip-audit not installed — skipping.")
    req_file = Path(repo_path) / "requirements.txt"
    if not req_file.exists():
        return safe_result(error="No requirements.txt found for pip-audit")
    out, err = run_cmd(["pip-audit", "-r", str(req_file), "--json"])
    return safe_result(out, err)

def run_yamllint(repo_path):
    if not is_installed("yamllint"):
        return safe_result(error="yamllint not installed — skipping.")
    out, err = run_cmd(["yamllint", "-f", "parsable", repo_path])
    return safe_result(out, err)

def run_flawfinder(repo_path):
    if not is_installed("flawfinder"):
        return safe_result(error="Flawfinder not installed — skipping.")
    # Flawfinder may not support --json; capture plain output
    out, err = run_cmd(["flawfinder", repo_path])
    return safe_result(out, err)

def run_gitleaks(repo_path):
    if not is_installed("gitleaks"):
        return safe_result(error="Gitleaks not installed — skipping.")
    out, err = run_cmd(["gitleaks", "detect", "--source", repo_path, "--report-format", "json"])
    return safe_result(out, err)

def run_hadolint(repo_path):
    dockerfile = Path(repo_path) / "Dockerfile"
    if not dockerfile.exists():
        return safe_result(error="No Dockerfile found")
    if not is_installed("hadolint"):
        return safe_result(error="Hadolint not installed — skipping.")
    out, err = run_cmd(["hadolint", str(dockerfile)])
    return safe_result(out, err)

# -----------------------------
# HTML Template
# -----------------------------
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Scan Report - {repo}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; }}
    h1 {{ color: #333; }}
    pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
    .section {{ margin-bottom: 20px; }}
  </style>
</head>
<body>
  <h1>Scan Report: {repo}</h1>
  <p><em>Timestamp: {ts}</em></p>
  {sections}
</body>
</html>
"""

def build_html(report_obj, out_path):
    sections = []
    for tool, results in report_obj.items():
        if tool in ["repo", "timestamp"]:
            continue
        # ensure results is dict
        if not isinstance(results, dict):
            results = safe_result(str(results))
        output = results.get("output", "")
        error = results.get("error", "")
        sections.append(f'<div class="section"><h2>{tool}</h2><pre>{output}\n{error}</pre></div>')
    html = HTML_TEMPLATE.format(repo=report_obj["repo"], ts=time.ctime(report_obj["timestamp"]), sections="\n".join(sections))
    with open(out_path, "w") as f:
        f.write(html)

def build_markdown(report_obj, out_path):
    md = f"# Scan Report: {report_obj['repo']}\n\n"
    md += f"*Timestamp: {time.ctime(report_obj['timestamp'])}*\n\n"
    for tool, results in report_obj.items():
        if tool in ["repo", "timestamp"]:
            continue
        if not isinstance(results, dict):
            results = safe_result(str(results))
        output = results.get("output", "")
        error = results.get("error", "")
        md += f"## {tool}\n```\n{output}\n{error}\n```\n\n"
    with open(out_path, "w") as f:
        f.write(md)

def build_pdf(html_path, pdf_path):
    try:
        from weasyprint import HTML
        HTML(html_path).write_pdf(pdf_path)
    except ImportError:
        print("WeasyPrint not installed — skipping PDF generation.")

# -----------------------------
# Main
# -----------------------------
def main():
    git_url = input("Enter git clone URL: ").strip()
    repo_name = git_url.rstrip("/").split("/")[-1]
    tmp_dir = tempfile.mkdtemp()
    repo_path = os.path.join(tmp_dir, repo_name)

    print(f"[+] Cloning {git_url} -> {repo_path}")
    out, err = run_cmd(["git", "clone", git_url, repo_path])
    if err and "fatal" in err.lower():
        print(f"[-] Failed to clone repository:\n{err}")
        shutil.rmtree(tmp_dir)
        return

    print(f"[+] Scanning repository: {repo_path}")
    report = {
        "repo": git_url,
        "timestamp": int(time.time()),
        "semgrep": run_semgrep(repo_path),
        "trufflehog": run_trufflehog(repo_path),
        "bandit": run_bandit(repo_path),
        "safety": run_safety(repo_path),
        "pip-audit": run_pip_audit(repo_path),
        "yamllint": run_yamllint(repo_path),
        "flawfinder": run_flawfinder(repo_path),
        "gitleaks": run_gitleaks(repo_path),
        "hadolint": run_hadolint(repo_path)
    }

    # Create reports folder
    outdir = Path("reports")
    outdir.mkdir(exist_ok=True)

    # JSON
    json_path = outdir / f"scan-report_{repo_name}_{report['timestamp']}.json"
    with open(json_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"[✓] JSON report written to {json_path}")

    # HTML
    html_path = outdir / f"scan-report_{repo_name}_{report['timestamp']}.html"
    build_html(report, str(html_path))
    print(f"[✓] HTML report written to {html_path}")

    # Markdown
    md_path = outdir / f"scan-report_{repo_name}_{report['timestamp']}.md"
    build_markdown(report, str(md_path))
    print(f"[✓] Markdown report written to {md_path}")

    # PDF
    pdf_path = outdir / f"scan-report_{repo_name}_{report['timestamp']}.pdf"
    build_pdf(str(html_path), str(pdf_path))
    print(f"[✓] PDF report written to {pdf_path}")

    # Summary
    print("\n--- Summary ---")
    for tool, results in report.items():
        if tool in ["repo", "timestamp"]:
            continue
        err = results.get("error", "")
        print(f"{tool:12}: {err}")

    # Clean up
    shutil.rmtree(tmp_dir)
    print("\n[i] Temp clone removed")

# -----------------------------
if __name__ == "__main__":
    main()

