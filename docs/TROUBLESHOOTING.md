# Troubleshooting Guide

## 1. Terraform Initialization Failure

Command:

```bash
terraform init -backend-config=backend-dev.hcl
```

Check:

- S3 bucket name.
- AWS region.
- IAM permissions.
- Backend configuration.

## 2. Undeclared Variable Warning

Example:

```text
Value for undeclared variable
```

Check whether the `.tfvars` file contains a variable that is not declared in `variables.tf`.

## 3. Invalid CIDR Error

Example:

```text
YOUR_PUBLIC_IP/32 is not a valid CIDR block
```

Replace the placeholder in your local environment file with a valid trusted IP CIDR.

## 4. Ollama Connection Failure

Check:

```bash
systemctl status ollama
curl http://localhost:11434/api/tags
```

Confirm that the configured model exists:

```bash
ollama list
```

## 5. Python Dependency Error

Activate the virtual environment:

```bash
source .venv/bin/activate
pip install -r ai/requirements.txt
```

## 6. Slack Notification Failure

Verify that the GitHub Secret `SLACK_WEBHOOK_URL` is configured correctly.

Never print the webhook URL in logs.

## 7. Terraform State Locking Error

Check whether another Terraform operation is running.

Do not force-unlock state unless you have confirmed that the lock is stale and understand the consequences.

## 8. AWS Access Denied

Verify the current identity:

```bash
aws sts get-caller-identity
```

Check the IAM permissions associated with the runner.

## 9. GitHub Runner Offline

Check:

```bash
sudo systemctl status actions.runner*
```

Inspect runner service logs if necessary.
