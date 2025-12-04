# Repo-Scanner

Repo-Scanner is a Python-based repository scanning tool that automates security checks for Git repositories.  
It integrates **Semgrep**, **TruffleHog**, and **pip-audit** to identify vulnerabilities, secrets, and dependency issues.

## Features

- Clones and scans Git repositories
- Runs Semgrep for code analysis
- Runs TruffleHog for secrets detection
- Runs pip-audit for dependency vulnerabilities
- Generates a summary report

## Usage

1. Activate your virtual environment:
   ```bash
   source .venv/bin/activate
