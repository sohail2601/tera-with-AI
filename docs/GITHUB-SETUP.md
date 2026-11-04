# GitHub Actions Setup Guide

## 1. Repository

Push the project to GitHub and configure the required repository settings.

## 2. Self-hosted Runner

Install a GitHub Actions runner on a dedicated Linux machine.

The runner must have:

- Terraform
- AWS CLI
- Python 3
- Git
- TFLint
- Ollama, if using localhost inference

Verify:

```bash
terraform version
aws --version
python3 --version
tflint --version
curl http://localhost:11434/api/tags
```

## 3. Repository Secrets

Configure these under Settings → Secrets and variables → Actions.

| Secret | Purpose |
|---|---|
| `SLACK_WEBHOOK_URL` | Slack notifications |
| `INFRACOST_API_KEY` | Optional cost estimation |

## 4. Repository Variables

Configure variables such as:

| Variable | Example |
|---|---|
| `TF_ENV` | dev |
| `OLLAMA_MODEL` | llama3.2:3b |
| `OLLAMA_BASE_URL` | http://localhost:11434/v1 |
| `PYTHON_BIN` | python3 |

The workflows must also be configured to supply the appropriate environment-specific Terraform variables.

## 5. Production Environment

Go to Settings → Environments.

Create an environment named:

`production`

Configure required reviewers and deployment protection rules.

## 6. Workflow Security

- Use least-privilege GitHub permissions.
- Protect production deployment.
- Use isolated runners for untrusted pull requests.
- Avoid exposing production credentials to pull-request workflows.
- Review workflow changes before merging.
