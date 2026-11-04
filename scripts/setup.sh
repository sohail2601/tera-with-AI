#!/bin/bash

set -e

echo "===================================="
echo " Terraform AI Reviewer Setup"
echo "===================================="

if ! command -v terraform >/dev/null 2>&1; then
    echo "ERROR: Terraform is not installed."
    exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: Python3 is not installed."
    exit 1
fi

if ! command -v tflint >/dev/null 2>&1; then
    echo "WARNING: TFLint is not installed."
fi

if ! command -v checkov >/dev/null 2>&1; then
    echo "WARNING: Checkov is not installed."
fi

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r ai/requirements.txt

echo "Setup completed successfully."
echo "Activate environment using: source .venv/bin/activate"
