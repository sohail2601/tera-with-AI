import requests
from pathlib import Path

PLAN_FILE = Path("tfplan.txt")
REPORT_FILE = Path("ai-report.txt")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

if not PLAN_FILE.exists():
    raise SystemExit("ERROR: tfplan.txt not found. Generate Terraform plan first.")

terraform_plan = PLAN_FILE.read_text()

prompt = f"""
You are an experienced AWS Terraform security reviewer.

Review the following Terraform plan.

Identify:
1. Security risks
2. IAM and network concerns
3. Configuration mistakes
4. Reliability concerns
5. Recommendations

Do not invent resources or configuration details.
If information is missing, clearly say it cannot be verified.

Terraform plan:
{terraform_plan}
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    },
    timeout=300
)

response.raise_for_status()

report = response.json()["response"]

REPORT_FILE.write_text(report)

print("AI Terraform review completed.")
print(report)
