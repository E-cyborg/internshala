import json
import os

from gmail_service import get_gmail_service
from sheets_service import get_sheets_service, append_email_row
from email_parser import parse_email
from googleapiclient.discovery import build

# ================= CONFIG =================

SPREADSHEET_ID = "1wXizaydeci_8m6CLUXRTh9obRMo8-VXilTQ9AkswX0Y"
STATE_FILE = "state.json"

# =========================================


def load_state():
    """
    Load processed message IDs from state file.
    """
    if not os.path.exists(STATE_FILE):
        return set()

    with open(STATE_FILE, "r") as f:
        data = json.load(f)
        return set(data.get("processed_message_ids", []))


def save_state(processed_ids):
    """
    Save processed message IDs to state file.
    """
    with open(STATE_FILE, "w") as f:
        json.dump(
            {"processed_message_ids": list(processed_ids)},
            f,
            indent=2
        )


def main():
    gmail_service, creds = get_gmail_service()

    sheets_service = get_sheets_service(creds)

    processed_ids = load_state()

    response = gmail_service.users().messages().list(
        userId="me",
        q="is:unread in:inbox"
    ).execute()

    messages = response.get("messages", [])

    print(f"Found {len(messages)} unread emails")

    for msg in messages:
        message_id = msg["id"]

        if message_id in processed_ids:
            continue

        message = gmail_service.users().messages().get(
            userId="me",
            id=message_id,
            format="full"
        ).execute()

        sender, subject, date, content = parse_email(message)

        append_email_row(
            sheets_service,
            SPREADSHEET_ID,
            sender,
            subject,
            date,
            content 
        )

        gmail_service.users().messages().modify(
            userId="me",
            id=message_id,
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()
        
        processed_ids.add(message_id)

        print(f"Processed email: {subject}")

    save_state(processed_ids)

    print("Done.")


if __name__ == "__main__":
    main()
