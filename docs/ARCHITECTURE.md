# Terraform AI Reviewer – Architecture

## 1. Overview

Terraform AI Reviewer automates Terraform infrastructure review using static analysis, security scanning, cost estimation, and AI-powered recommendations.

## 2. Architecture Flow

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
GitHub Actions
   |
   v
Self-hosted GitHub Runner
   |
   +--> Terraform Format and Validate
   |
   +--> TFLint
   |
   +--> Checkov
   |
   +--> Terraform Plan
   |
   +--> Infracost (Optional)
   |
   v
Ollama AI Review
   |
   +--> Risk Analysis
   +--> Security Findings
   +--> Cost Findings
   +--> Production Recommendation
   |
   +--> GitHub PR Comment
   |
   +--> Slack Notification

AWS S3
   |
   +--> Development Terraform State
   |
   +--> Production Terraform State
```

## 3. Components

| Component | Responsibility |
|---|---|
| GitHub | Source code and pull requests |
| GitHub Actions | Workflow orchestration |
| Self-hosted runner | Executes automation |
| Terraform | Infrastructure provisioning |
| AWS S3 | Remote state storage |
| TFLint | Terraform linting |
| Checkov | Infrastructure security checks |
| Infracost | Cost estimation |
| Ollama | Local AI inference |
| Python | AI report generation |
| Slack | Review notifications |

## 4. Review Lifecycle

1. Developer creates a branch and opens a pull request.
2. GitHub Actions checks out the repository.
3. Terraform formatting and validation run.
4. TFLint checks Terraform code.
5. Checkov scans infrastructure security.
6. Terraform generates an execution plan.
7. Infracost optionally estimates infrastructure cost.
8. Ollama analyzes the collected reports.
9. The AI report is posted to the pull request and Slack.

## 5. State Management

Development and production use separate S3 state keys.

- Development: `terraform-aiops/dev/terraform.tfstate`
- Production: `terraform-aiops/prod/terraform.tfstate`

S3 bucket versioning and encryption should remain enabled.

## 6. Security Considerations

- Keep credentials in GitHub Secrets or IAM roles.
- Never commit Terraform state or plan files.
- Restrict AWS permissions.
- Protect production deployment using GitHub Environment approval.
- Never run untrusted pull-request code on a privileged persistent self-hosted runner.
- Review AI recommendations before approving infrastructure changes.
