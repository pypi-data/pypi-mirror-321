import os
import json
import pandas as pd
from requests.auth import HTTPBasicAuth
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment Variables
JIRA_URL = os.getenv("JIRA_URL")
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

# File paths (relative paths for flexibility)
INPUT_FILE = os.getenv("INPUT_FILE", "data/input_file.xlsx")
NEW_OUTPUT_JSON = os.getenv("NEW_OUTPUT_JSON", "data/formatted_last_3_comments.json")
REPORT_FILE = os.getenv("REPORT_FILE", "data/final_report.csv")

# Excluded team members (defined dynamically by the user)
EXCLUDED_USERS = os.getenv("EXCLUDED_USERS", "").split(',')

def fetch_all_comments(issue_key):
    """
    Fetch all comments for a given Jira issue key, handling pagination.
    """
    all_comments = []
    start_at = 0
    max_results = 50

    while True:
        url = f"{JIRA_URL}/rest/api/2/issue/{issue_key}/comment?startAt={start_at}&maxResults={max_results}"
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, TOKEN))

        if response.status_code == 200:
            data = response.json()
            all_comments.extend(data.get("comments", []))
            
            # Check if there are more comments to fetch
            if start_at + max_results >= data.get("total", 0):
                break
            start_at += max_results
        else:
            print(f"Error fetching comments for {issue_key}: {response.status_code}")
            break

    # Sort comments by created date in descending order
    all_comments.sort(key=lambda x: x.get("created", ""), reverse=True)
    return all_comments

def filter_last_3_non_excluded_comments(comments, excluded_users):
    """
    Filter the last 3 comments to exclude specific team members defined by the user.
    If fewer than 3 non-excluded comments are found, include all available.
    """
    non_excluded_comments = [
        {
            "Comment": comment.get("body", "No comment body"),
            "Author": comment.get("author", {}).get("displayName", "Unknown"),
            "Email": comment.get("author", {}).get("emailAddress", "Unknown"),
            "Created": comment.get("created", "Unknown Timestamp"),
        }
        for comment in comments
        if comment.get("author", {}).get("displayName", "") not in excluded_users
    ]
    
    # Handle the case when there are fewer than 3 comments
    while len(non_excluded_comments) < 3:
        non_excluded_comments.append({
            "Comment": "No comment found",
            "Author": "Unknown",
            "Email": "Unknown",
            "Created": "Unknown Timestamp"
        })

    return non_excluded_comments[:3]

def process_workflow(input_file, new_output_json, report_file):
    """
    Execute the full workflow: fetch comments, filter user-specified excluded comments, and generate a report.
    """
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Extract issue keys and components
    issue_keys = df[['Key', 'Components']].to_dict(orient='records')

    results = []
    for issue in issue_keys:
        issue_key = issue["Key"]
        component = issue["Components"]

        print(f"Processing issue: {issue_key}")
        comments = fetch_all_comments(issue_key)
        last_3_non_excluded_comments = filter_last_3_non_excluded_comments(comments, EXCLUDED_USERS)

        # Restructure data for JSON output
        formatted_comments = {
            "Issue Key": issue_key,
            "Component": component
        }
        for idx, comment in enumerate(last_3_non_excluded_comments, start=1):
            formatted_comments[f"Comment-{idx}"] = comment["Comment"]
            formatted_comments[f"Author-{idx}"] = comment["Author"]
            formatted_comments[f"Email-{idx}"] = comment["Email"]
            formatted_comments[f"Created-{idx}"] = comment["Created"]

        results.append(formatted_comments)

    # Save results to the new JSON file
    os.makedirs(os.path.dirname(new_output_json), exist_ok=True)
    with open(new_output_json, "w") as json_file:
        json.dump(results, json_file, indent=4)
    print(f"Formatted comments saved to {new_output_json}")

    # Save results to CSV
    os.makedirs(os.path.dirname(report_file), exist_ok=True)
    pd.DataFrame(results).to_csv(report_file, index=False)
    print(f"Final report saved to {report_file}")

if __name__ == "__main__":
    process_workflow(INPUT_FILE, NEW_OUTPUT_JSON, REPORT_FILE)
