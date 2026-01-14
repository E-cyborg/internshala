from googleapiclient.discovery import build


def get_sheets_service(creds):
    """
    Build and return a Google Sheets API service
    using already-authenticated credentials.
    """
    service = build("sheets", "v4", credentials=creds)
    return service

MAX_CELL_LENGTH = 50000

def append_email_row(service, spreadsheet_id, sender, subject, date, content, sheet_name="Sheet1"):
    # Truncate content
    if len(content) > MAX_CELL_LENGTH:
        content = content[:MAX_CELL_LENGTH-50] + "\n[Truncated]"


    values = [[sender, subject, date, content]]

    body = {"values": values}

    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}!A:D",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

    return result

