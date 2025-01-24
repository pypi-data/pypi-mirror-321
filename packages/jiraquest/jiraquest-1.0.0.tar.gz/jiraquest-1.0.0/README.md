# JiraQuest 🌌

Embark on a journey to uncover insights from your Jira comments.

JiraQuest is an open-source project designed to help teams process and analyze Jira comments efficiently. With built-in integrations for Tableau and Slack, along with a powerful CLI, JiraQuest empowers teams to focus on actionable insights, visualize trends, and stay connected.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Tableau Integration](#tableau-integration)
  - [Slack Integration](#slack-integration)
- [Example Files](#example-files)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

JiraQuest simplifies Jira comment analysis by automating the process of fetching, filtering, and formatting comments. It is highly customizable and suitable for various teams, including developers, Atlassian admins, quality assurance, project management, and more. Whether you want detailed reports, visual insights, or Slack updates, JiraQuest has you covered.

---

## Features

- **Automated Comment Processing**: Fetch and filter comments from Jira issues.
- **Customizable Exclusions**: Define specific users or teams to exclude from reports.
- **Tableau Integration**: Export data to a SQLite database for easy visualization.
- **Slack Integration**: Send summarized reports directly to a Slack channel.
- **Sentiment Analysis** *(optional)*: Analyze the sentiment of comments (Positive, Negative, Neutral).
- **Flexible CLI**: Perform actions such as generating reports, integrating with Tableau, and sending Slack notifications from the command line.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/jiraquest.git
   cd jiraquest
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install SQLite (if not already installed) for Tableau integration.

4. Ensure you have Python 3.8 or higher.

---

## Setup

1. Create a `.env` file in the root directory with the following environment variables:

   ```plaintext
   # Jira Configuration
   JIRA_URL=https://your-jira-instance.atlassian.net
   USERNAME=your-email@example.com
   TOKEN=your-api-token

   # File Paths
   INPUT_FILE=data/input_file.xlsx
   NEW_OUTPUT_JSON=data/formatted_last_3_comments.json
   REPORT_FILE=data/final_report.csv
   DB_FILE=data/jira_comments.db

   # Slack Integration
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/slack/webhook
   ```

2. Prepare your input Excel file (`input_file.xlsx`) with the following structure:

   | Key      | Components |
   | -------- | ---------- |
   | PROJ-123 | Frontend   |
   | PROJ-124 | Backend    |

3. Add a file `excluded_users.txt` (optional) to define users to exclude from reports:

   ```plaintext
   John Doe
   Jane Smith
   ```

---

## Usage

### Command-Line Interface (CLI)

Run the script with the following commands:

1. **Generate Reports**:

   ```bash
   python cli_integration.py --generate-report
   ```

2. **Save to Database**:

   ```bash
   python cli_integration.py --save-to-database
   ```

3. **Send Report to Slack**:

   ```bash
   python cli_integration.py --slack-me
   ```

4. **Combine Actions**:

   ```bash
   python cli_integration.py --generate-report --save-to-database --slack-me
   ```

### Tableau Integration

After running the `--save-to-database` command, connect Tableau to the SQLite database:

1. Open Tableau.
2. Connect to the database file (`jira_comments.db`).
3. Visualize the data using Tableau's drag-and-drop interface.

### Slack Integration

Ensure your Slack webhook URL is set in the `.env` file. Run the following command to send reports:

```bash
python cli_integration.py --slack-me
```

---

## Example Files

You'll find the following example files in the `data` directory:

1. **`sample_input.xlsx`**: A template for input data with example Jira issue keys and components.

2. **`excluded_users.txt`**: A template for excluded users.


---

## Example Output

### JSON File (`formatted_last_3_comments.json`):

```json
[
    {
        "Instance": "https://your-jira-instance.atlassian.net",
        "Issue Key": "PROJ-123",
        "Component": "Frontend",
        "Comment-1": "The feature is not working as expected.",
        "Author-1": "John Doe",
        "Email-1": "john@example.com",
        "Created-1": "2025-01-10T12:34:56Z",
        "Comment-2": "I have fixed the issue.",
        "Author-2": "Jane Smith",
        "Email-2": "jane@example.com",
        "Created-2": "2025-01-11T08:22:33Z",
        "Comment-3": "The fix has been deployed.",
        "Author-3": "John Doe",
        "Email-3": "john@example.com",
        "Created-3": "2025-01-12T09:45:12Z"
    }
]
```

### Slack Notification:

```plaintext
New comments have been processed for the following Jira issues:

- **PROJ-123 (Frontend)**
  - *John Doe*: The feature is not working as expected.
  - *Jane Smith*: I have fixed the issue.
  - *John Doe*: The fix has been deployed.

Check the detailed report for more information.
```

### Slack Notification:

## Slack Integration

JiraQuest can send automated reports or insights directly to a specified Slack channel using a webhook URL. Follow these steps to configure and use Slack notifications:

### Step 1: Set Up a Slack Webhook URL

1. Go to your Slack workspace and navigate to **Settings & Administration > Manage Apps**.
2. Search for **Incoming Webhooks** and click **Add to Slack**.
3. Choose a channel where JiraQuest notifications should appear.
4. Copy the webhook URL provided (e.g., `https://hooks.slack.com/services/your/webhook/url`).

### Step 2: Add the Webhook URL to the .env File

Add the Slack webhook URL to your `.env` file:

```plaintext
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
```

### Step 3: Send Reports to Slack

Run the following command to send the latest report to Slack:

```bash
python cli_integration.py --slack-me
```

### How It Works

JiraQuest composes a summary of the latest Jira comments or a report and sends it to the specified Slack channel using the webhook.

Example notification format:

```plaintext
🔔 JiraQuest Alert 🚀 New Insights from Jira Comments:
Issue Key: PROJ-123
Component: Frontend
Latest Comment: "The feature is not working as expected."
Author: John Doe
Timestamp: 2025-01-10 12:34:56
```

### Step 4: Customize Slack Notifications (Optional)

To customize the notification format:

1. Open the `slack_integration.py` file in the `src/jiraquest/` directory.
2. Modify the payload structure in the `send_to_slack` function.


---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature/new-feature`).
3. Commit your changes.
4. Open a pull request.

## 📜 Code of Conduct

Please note that this project has a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.


For questions or feature requests, open an issue on GitHub.

---

## License

The project is available as open source under the terms of the MIT License.

