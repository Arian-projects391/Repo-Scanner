# Repo-Scanner

Repo-Scanner is a Python-based tool for scanning Git repositories for potential security issues, secrets, and vulnerable dependencies. It integrates **Semgrep**, **TruffleHog**, and **pip-audit** to provide comprehensive reports.

---

## Features

- **Semgrep Integration**: Detects security issues and code patterns.
- **TruffleHog Integration**: Finds secrets such as passwords, API keys, and tokens.
- **pip-audit Integration**: Audits Python dependencies for known vulnerabilities.
- Handles repositories of various sizes and creates detailed scan reports.
- Generates a JSON report and provides a human-readable summary.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Arian-projects391/Repo-Scanner.git
cd Repo-Scanner
