import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment Variables
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
REPORT_SUMMARY_FILE = os.getenv("REPORT_SUMMARY_FILE", "data/summary.json")


def send_report_to_slack(slack_webhook_url, report_file):
    """
    Send a summary of the report to a Slack channel using a webhook URL.
    """
    if not os.path.exists(report_file):
        print(f"Error: Report summary file {report_file} does not exist. Generate the report first.")
        return

    # Load the report summary
    with open(report_file, "r") as file:
        summary = json.load(file)

    # Prepare the Slack message
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Jira Comments Report Summary*\nHere are the latest highlights:"  
            }
        },
        {"type": "divider"}
    ]

    for item in summary[:5]:  # Limit to the first 5 issues for brevity
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"*Issue Key:* {item['Issue Key']}\n"
                        f"*Component:* {item['Component']}\n"
                        f"*Comment-1:* {item['Comment-1']}\n"
                        f"*Author:* {item['Author-1']}\n"
                        f"*Created:* {item['Created-1']}\n"
                    )
                }
            }
        )

    # Add a footer or call-to-action
    blocks.append(
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "*Full report available in your system.*"
                }
            ]
        }
    )

    # Send the message to Slack
    response = requests.post(
        slack_webhook_url,
        headers={"Content-Type": "application/json"},
        json={"blocks": blocks}
    )

    if response.status_code == 200:
        print("Report sent to Slack successfully.")
    else:
        print(f"Failed to send report to Slack. Status code: {response.status_code}")


def main():
    """
    Main function to execute the Slack integration.
    """
    if not SLACK_WEBHOOK_URL:
        print("Error: Slack webhook URL is not configured. Set the SLACK_WEBHOOK_URL environment variable.")
        return

    send_report_to_slack(SLACK_WEBHOOK_URL, REPORT_SUMMARY_FILE)


if __name__ == "__main__":
    main()
