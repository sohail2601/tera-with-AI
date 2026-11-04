# AWS Setup Guide

## 1. Prerequisites

- An AWS account.
- AWS CLI installed.
- An IAM role or user with appropriate permissions.
- Terraform installed.
- An S3 bucket for remote Terraform state.

## 2. Configure AWS Credentials

For an EC2 self-hosted runner, prefer an attached IAM instance role.

Verify identity:

```bash
aws sts get-caller-identity
```

Do not store AWS access keys in GitHub workflow files.

## 3. Create an S3 Backend Bucket

Create a globally unique S3 bucket in your chosen AWS region.

Enable:

- Bucket versioning.
- Default encryption.
- Block Public Access.

The bucket used in this project must be configured in the backend files.

## 4. Configure Backend Files

Edit `backend-dev.hcl` and `backend-prod.hcl`.

Example:

```hcl
bucket       = "YOUR_S3_BUCKET"
key          = "terraform-aiops/dev/terraform.tfstate"
region       = "ap-south-1"
encrypt      = true
use_lockfile = true
```

For production, use the production state key.

## 5. Configure Environment Variables

Copy the example:

```bash
cp envs/dev.tfvars.example envs/dev.tfvars
vi envs/dev.tfvars
```

Set the trusted public IP CIDR.

## 6. Initialize Terraform

```bash
terraform init -backend-config=backend-dev.hcl
```

Validate:

```bash
terraform fmt -check -recursive
terraform validate
terraform plan -var-file=envs/dev.tfvars
```

## 7. Important

Terraform plan does not create infrastructure. Apply only after reviewing the plan and confirming the AWS resources and expected costs.
