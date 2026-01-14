import base64
from bs4 import BeautifulSoup
from datetime import datetime


def get_header(headers, name):
    for header in headers:
        if header["name"].lower() == name.lower():
            return header["value"]
    return ""


def decode_body(data):
    if not data:
        return ""
    return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")


def extract_body(payload):
    """
    Recursively extract email body.
    Prefer text/plain, fallback to text/html.
    """
    if "parts" in payload:
        for part in payload["parts"]:
            if part.get("mimeType") == "text/plain":
                return decode_body(part["body"].get("data"))
        for part in payload["parts"]:
            if part.get("mimeType") == "text/html":
                html = decode_body(part["body"].get("data"))
                soup = BeautifulSoup(html, "html.parser")
                return soup.get_text(separator="\n")
    else:
        return decode_body(payload["body"].get("data"))

    return ""


def parse_email(message):
    payload = message.get("payload", {})
    headers = payload.get("headers", [])

    sender = get_header(headers, "From")
    subject = get_header(headers, "Subject")

    # Date handling
    date_header = get_header(headers, "Date")
    if date_header:
        date = date_header
    else:
        timestamp = int(message.get("internalDate", 0)) / 1000
        date = datetime.fromtimestamp(timestamp).isoformat()

    content = extract_body(payload)

    return sender, subject, date, content
