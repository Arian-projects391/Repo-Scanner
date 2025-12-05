# Repo Scanner

A comprehensive GitHub repository scanner that uses multiple tools to analyze a repository for security issues, sensitive data leaks, dependency vulnerabilities, and code quality concerns. Generates reports in **JSON, HTML, Markdown, and PDF** formats.

---

## **Table of Contents**

- [Quick Start](#quick-start-setup--scan)  
- [Installation](#installation)  
- [Setup](#setup)  
- [Usage](#usage)  
- [Reports](#reports)  
- [Supported Scanners](#supported-scanners)  
- [Git Ignore Tips](#git-ignore-tips)  
- [Disclaimers](#disclaimers)  

---

## **Quick Start: Setup & Scan**

1️⃣ **Clone the repo:**
NOTE: for any updates run git pull

```bash
git clone https://github.com/Arian-projects391/Repo-Scanner.git
cd Repo-Scanner

Create and activate Python virtual environment (recommended):
python3 -m venv ~/scanner-venv
source ~/scanner-venv/bin/activate

Install Python-based scanners in the environment:
pip install safety pip-audit trufflehog weasyprint

Install system/binary scanners:
sudo apt update
sudo apt install bandit yamllint flawfinder gitleaks


Hadolint (binary install):
sudo wget -O /usr/local/bin/hadolint https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64
sudo chmod +x /usr/local/bin/hadolint
hadolint --version

Semgrep:

Option A: pipx (recommended)
sudo apt install pipx
pipx install semgrep
semgrep --version


Option B: Official install script
curl -sSfL https://get.semgrep.dev | sh
export PATH="$HOME/.local/bin:$PATH"
semgrep --version

Run the scanner:
python3 scanner.py --url <git-repo-url> --outdir reports

Example:
python3 scanner.py --url https://github.com/Arian-projects391/Repo-Scanner.git --outdir reports


6️⃣ View reports:

JSON: reports/scan-report_<repo-name>_<timestamp>.json

HTML: reports/scan-report_<repo-name>_<timestamp>.html

Markdown: reports/scan-report_<repo-name>_<timestamp>.md

PDF: reports/scan-report_<repo-name>_<timestamp>.pdf

Installation

If you prefer, you can also follow the detailed installation:

Clone this repository:

git clone https://github.com/Arian-projects391/Repo-Scanner.git
cd Repo-Scanner


(Optional but recommended) Create and activate a virtual environment:

python3 -m venv ~/scanner-venv
source ~/scanner-venv/bin/activate


Install Python-based tools:

pip install safety pip-audit trufflehog weasyprint


Install system/binary tools:

sudo apt update
sudo apt install bandit yamllint flawfinder gitleaks


Install Hadolint and Semgrep as described above.

Setup

Make sure all scanner binaries are in your PATH.

Activate the Python virtual environment before running Python-based tools.

Ensure system tools are installed globally via apt or as binaries.

Usage
python3 scanner.py --url <git-repo-url> --outdir <report-directory>


--url: GitHub repository URL to scan.

--outdir: Directory for storing reports.

After the scan, the temporary clone is automatically removed.

Reports

Reports are generated in multiple formats:

JSON → scan-report_<repo-name>_<timestamp>.json

HTML → scan-report_<repo-name>_<timestamp>.html

Markdown → scan-report_<repo-name>_<timestamp>.md

PDF → scan-report_<repo-name>_<timestamp>.pdf

The temporary clone of the repository is removed after the scan to keep your system clean. Only the reports remain.

Supported Scanners

Semgrep – Security and code pattern scanning

TruffleHog – Secrets and sensitive information detection

Bandit – Python security static analysis

Safety – Python dependency vulnerabilities

Pip-audit – Python dependency auditing

Hadolint – Dockerfile linting

Flawfinder – C/C++ security analysis

Yamllint – YAML syntax and style checking

Gitleaks – Git repository secrets detection

If a tool is not installed or cannot run, the scanner will skip it and notify you in the summary.

Git Ignore Tips

To keep your repo clean, the following .gitignore entries are recommended:

# Virtual environments
.venv/
trufflehog-venv/
semgrep-venv/

# Scanner reports
reports/
scan-report_*.json
*.html
*.md
*.pdf

# Python cache
__pycache__/
*.pyc

# Backup / editor files
*.save

License
This project is licensed under the MIT License. See the LICENSE
 file for details.

Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for suggestions and improvements.

⚠️ **Disclaimer:**
This tool clones repositories temporarily to analyze code. It does not make permanent changes to your system.
Scan results may include false positives or warnings — always review reports carefully.
Generated reports may contain sensitive information; handle them securely.
Use this scanner only on repositories you own or have permission to scan. Unauthorized scanning may be illegal and violate laws or terms of service.
Some scanners (e.g., Semgrep, TruffleHog) require additional setup; follow instructions in Setup.
The scanner is designed for educational and development purposes. Do not rely solely on it for security assurance.
Use responsibly and ethically.

🔒 **Privacy:** Repo-Scanner runs locally and does not transmit any repository data to external servers. 
Scan reports are saved locally on your machine.

⚠️ **Accuracy:** The scan may not detect all security issues or secrets. 
Use the results as guidance, but always perform additional security checks as needed. 
The author is not responsible for any misuse or missed vulnerabilities.

You’re now ready to scan repositories safely and efficiently!
