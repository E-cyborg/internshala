# 📧 Gmail to Google Sheets Automation

**Author:** kinshuk

---

## 📖 Project Overview

This project is a Python automation system that reads **real unread emails** from a Gmail inbox using the **Gmail API** and logs them into a **Google Sheet** using the **Google Sheets API**.

Each qualifying email is appended as a new row containing:
- Sender email address
- Subject
- Date & time received
- Plain text email content

The system is designed to be **secure**, **idempotent**, and compliant with **OAuth 2.0** best practices.

---

## 🎯 Objective

Automatically:
1. Authenticate using OAuth 2.0
2. Fetch unread emails from Gmail Inbox
3. Parse sender, subject, date, and content
4. Append email data to Google Sheets
5. Prevent duplicate processing
6. Mark processed emails as read
