import os
import requests
from pathlib import Path

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORT_FILE = PROJECT_DIR / "ai-report.txt"

if not WEBHOOK_URL:
    raise SystemExit("ERROR: SLACK_WEBHOOK_URL environment variable is not set.")

if not REPORT_FILE.exists():
    raise SystemExit(f"ERROR: Report file not found: {REPORT_FILE}")

report = REPORT_FILE.read_text().strip()

if not report:
    raise SystemExit("ERROR: AI report is empty.")

message = {
    "text": (
        "*Terraform AI Reviewer Report*\n"
        "AI security and configuration review completed.\n\n"
        f"```{report[:35000]}```"
    )
}

try:
    response = requests.post(
        WEBHOOK_URL,
        json=message,
        timeout=30
    )
    response.raise_for_status()

    if response.text.strip() != "ok":
        raise SystemExit(f"Slack returned an unexpected response: {response.text}")

    print("SUCCESS: AI report sent to Slack.")

except requests.RequestException as error:
    raise SystemExit(f"ERROR: Could not send report to Slack: {error}")
