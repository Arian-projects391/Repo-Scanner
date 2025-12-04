# Repo-Scanner

Repo-Scanner is a Python-based tool for scanning Git repositories for potential security issues, secrets, and vulnerable dependencies. It integrates **Semgrep**, **TruffleHog**, and **pip-audit** to provide comprehensive reports.

## Features

- **Semgrep Integration:** Detects security issues and code patterns.
- **TruffleHog Integration:** Finds secrets such as passwords, API keys, and tokens.
- **pip-audit Integration:** Audits Python dependencies for known vulnerabilities.
- Handles repositories of various sizes and creates detailed scan reports.
- Generates a JSON report and provides a human-readable summary.

## Installation

Clone the repository:

```bash
git clone https://github.com/Arian-projects391/Repo-Scanner.git
cd Repo-Scanner

Create a Python virtual environment:
python3 -m venv .venv

Activate the virtual environment:
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt
NOTE: pip‑audit runs only if the scanned repository contains a requirements.txt file.

Usage
Follow these steps to scan a Git repository:

1. Activate the virtual environment
Make sure your Python virtual environment is active:
source .venv/bin/activate

2. Run the main scanner script
python3 scanner.py

3. Enter the repository URL
When prompted, paste the Git repository URL you want to scan:
Enter git clone URL: https://github.com/octocat/Hello-World

4. Automatic scanning
The scanner will automatically:
Clone the repository into a temporary directory
Run Semgrep to detect security issues and code patterns
Run TruffleHog to detect secrets (passwords, API keys, tokens)
Run pip-audit to detect vulnerable Python dependencies
Generate a JSON report

5. View the scan report
The scan results are saved to:
scan-report.json

6. Optional: Generate a human-readable summary
python3 report_summary.py

This prints a formatted summary of all findings from the scan.

Safe Handling & Security Tips
When using Repo-Scanner, keep in mind:
Do not scan sensitive or private repositories without permission.
Only scan repositories you own or are authorized to scan.
Avoid committing secrets like API keys or passwords in public repositories.
Review JSON reports for sensitive information before sharing publicly.
Use the tool in a virtual environment to avoid affecting system-wide Python packages.
Keep dependencies up-to-date to minimize security risks in the scanner itself.

License
This project is licensed under the MIT License. See the LICENSE
 file for details.

Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for suggestions and improvements.
