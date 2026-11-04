# Terraform AI Reviewer

An AI-powered Terraform infrastructure review and DevSecOps automation project using AWS, Terraform, TFLint, Checkov, Infracost, Ollama, GitHub Actions, and Slack.

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
Pull Request / Push
   |
   v
GitHub Actions (Self-hosted Runner)
   |
   +---- Terraform fmt / validate
   |
   +---- TFLint
   |
   +---- Checkov Security Scan
   |
   +---- Terraform Plan
   |
   +---- Infracost (Optional)
   |
   v
Ollama AI Reviewer
   |
   +---- Risk Analysis
   +---- Security Findings
   +---- Cost Findings
   +---- Production Recommendation
   |
   +---- GitHub Pull Request Comment
   |
   +---- Slack Notification

Terraform State
   |
   v
AWS S3 Remote Backend
```

## Features

- Terraform infrastructure validation and planning.
- Static analysis using TFLint.
- Security and compliance scanning using Checkov.
- AI-powered Terraform plan analysis using Ollama.
- Optional infrastructure cost estimation using Infracost.
- Automated Slack notifications.
- GitHub Pull Request review comments.
- Separate development and production backend configurations.
- Manual production deployment workflow.

## Technology Stack

| Technology | Purpose |
|---|---|
| AWS | Cloud infrastructure |
| Terraform | Infrastructure as Code |
| Amazon S3 | Remote Terraform state |
| GitHub Actions | CI/CD automation |
| TFLint | Terraform linting |
| Checkov | Security scanning |
| Infracost | Cost estimation |
| Ollama | Local AI model |
| Python | AI review automation |
| Slack | Notifications |

## Repository Structure

```text
terraform-ai-reviewer/
├── .github/workflows/
├── ai/
│   ├── ai_review.py
│   ├── slack_send.py
│   └── requirements.txt
├── docs/
├── envs/
│   ├── dev.tfvars.example
│   └── prod.tfvars.example
├── scripts/
│   ├── setup.sh
│   └── local-review.sh
├── backend.tf
├── backend-dev.hcl.example
├── backend-prod.hcl.example
├── main.tf
├── provider.tf
├── variables.tf
├── outputs.tf
└── README.md
```

## Prerequisites

- AWS account and configured credentials or IAM role.
- Terraform.
- Python 3.
- Git.
- TFLint.
- Checkov.
- Ollama with a supported model.
- An S3 bucket for Terraform remote state.

## Setup

Clone the repository:

```bash
git clone https://github.com/sohail2601/tera-with-AI.git
cd tera-with-AI
```

Create your Python environment:

```bash
bash scripts/setup.sh
source .venv/bin/activate
```

Configure development variables:

```bash
cp envs/dev.tfvars.example envs/dev.tfvars
vi envs/dev.tfvars
```

Replace `YOUR_PUBLIC_IP/32` with your trusted public IP address.

Create your personal backend files:

```bash
cp backend-dev.hcl.example backend-dev.hcl
cp backend-prod.hcl.example backend-prod.hcl
```

Replace `YOUR_UNIQUE_S3_BUCKET_NAME` in both files with your own S3 bucket name. Keep your actual backend files out of Git.

Initialize and validate:

```bash
terraform init -backend-config=backend-dev.hcl
terraform fmt -check -recursive
terraform validate
```

Run a development plan:

```bash
terraform plan -var-file=envs/dev.tfvars
```

Run the local AI review:

```bash
TF_ENV=dev bash scripts/local-review.sh
```

## AI Configuration

The default Ollama API endpoint is:

```text
http://localhost:11434/v1
```

The default model is:

```text
llama3.2:3b
```

Configure `OLLAMA_BASE_URL` and `OLLAMA_MODEL` when using a different Ollama endpoint or model.

## GitHub Secrets and Variables

Configure the required repository or environment settings before enabling automation.

Potential secrets:

- `SLACK_WEBHOOK_URL`
- `INFRACOST_API_KEY` (optional)

Configuration variables include:

- `TF_ENV`
- `OLLAMA_BASE_URL`
- `OLLAMA_MODEL`
- `PYTHON_BIN`

Use a protected GitHub Environment for production approval.

## Safety

- Never commit actual `.tfvars` files, state files, plans, API keys, or webhook URLs.
- Use IAM roles with least-privilege permissions.
- Review Terraform plans before applying.
- Protect production workflows with GitHub Environment approval.
- Use isolated self-hosted runners for untrusted pull requests.
- This repository is a learning and demonstration project, not a production-ready security baseline.

## Author

**Sohail Pathan**

Cloud & DevOps Enthusiast

GitHub: https://github.com/sohail2601

LinkedIn: Add your LinkedIn profile URL.

## Disclaimer

This project is intended for educational and demonstration purposes. Review all infrastructure and security configurations before using them in production.
