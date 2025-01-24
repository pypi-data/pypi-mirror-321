import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# File paths (relative paths for flexibility)
DB_FILE = os.getenv("DB_FILE", "data/jira_comments.db")
REPORT_FILE = os.getenv("REPORT_FILE", "data/final_report.csv")


def save_to_database(csv_file, db_file):
    """
    Save the CSV data to a SQLite database for Tableau integration.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Save the DataFrame to a SQLite table
    df.to_sql("jira_comments", conn, if_exists="replace", index=False)

    # Close the connection
    conn.close()
    print(f"Data from {csv_file} saved to SQLite database at {db_file}")


def main():
    """
    Main function to execute the Tableau integration workflow.
    """
    if not os.path.exists(REPORT_FILE):
        print(f"Error: Report file {REPORT_FILE} does not exist. Generate the report first.")
        return

    # Ensure the directory for the database exists
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

    # Save the report to the database
    save_to_database(REPORT_FILE, DB_FILE)


if __name__ == "__main__":
    main()
