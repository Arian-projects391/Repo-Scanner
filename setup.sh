#!/usr/bin/env bash
set -euo pipefail

echo "=== Repo Scanner Setup Helper (Kali Linux Edition) ==="

# sudo detection
SUDO=""
if command -v sudo >/dev/null 2>&1; then
  SUDO="sudo"
fi

echo "[*] Updating package lists..."
$SUDO apt update -y || true

echo "[*] Installing system dependencies..."
$SUDO apt install -y git python3-venv python3-pip gcc python3-dev libffi-dev libssl-dev build-essential wget

echo "[*] Creating virtualenv for Semgrep"
python3 -m venv "$HOME/semgrep-venv"
source "$HOME/semgrep-venv/bin/activate"
pip install --upgrade pip
pip install semgrep
deactivate

echo "[*] Creating virtualenv for TruffleHog"
python3 -m venv "$HOME/trufflehog-venv"
source "$HOME/trufflehog-venv/bin/activate"
pip install --upgrade pip
pip install trufflehog
deactivate

echo "[*] Installing global pip tools (Bandit, Safety, pip-audit, yamllint, flawfinder)"
python3 -m pip install --user bandit safety pip-audit yamllint flawfinder

echo "[*] Installing Gitleaks"
if ! command -v gitleaks >/dev/null 2>&1; then
  wget -O /tmp/gitleaks.tar.gz "https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks-linux-amd64.tar.gz"
  tar -xf /tmp/gitleaks.tar.gz -C /tmp
  $SUDO install -m 0755 /tmp/gitleaks /usr/local/bin/gitleaks
fi

echo "[*] Installing Hadolint (Kali manual install)"
if ! command -v hadolint >/dev/null 2>&1; then
  wget -O /tmp/hadolint "https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64"
  $SUDO install -m 0755 /tmp/hadolint /usr/local/bin/hadolint
fi

echo "[*] Installing optional Python libs for reports (weasyprint, pdfkit)"
python3 -m pip install --user pyyaml weasyprint pdfkit

echo "[✔] Setup complete for Kali Linux!"
echo "Make sure ~/.local/bin is in your PATH:"
echo '  export PATH="$PATH:$HOME/.local/bin"'
