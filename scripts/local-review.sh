#!/bin/bash

set -euo pipefail

TF_ENV="${TF_ENV:-dev}"
TFVARS_FILE="envs/${TF_ENV}.tfvars"
BACKEND_CONFIG="backend-${TF_ENV}.hcl"

if [[ ! -f "$TFVARS_FILE" ]]; then
    echo "ERROR: $TFVARS_FILE not found."
    echo "Copy the example file and configure your values."
    exit 1
fi

if [[ ! -f "$BACKEND_CONFIG" ]]; then
    echo "ERROR: $BACKEND_CONFIG not found."
    exit 1
fi

echo "Running Terraform AI review for: $TF_ENV"

terraform init -input=false -reconfigure \
    -backend-config="$BACKEND_CONFIG"

terraform fmt -check -recursive
terraform validate

tflint --init
tflint --format compact | tee tflint.txt || true

checkov -d . --framework terraform \
    --var-file "$TFVARS_FILE" \
    --quiet | tee checkov.txt || true

terraform plan -input=false \
    -var-file="$TFVARS_FILE" \
    -out=tfplan

terraform show -no-color tfplan > tfplan.txt

python3 ai/ai_review.py | tee ai-report.txt

echo "===================================="
echo "AI review completed."
echo "Report: ai-report.txt"
echo "===================================="
