import gspread
from google.oauth2.service_account import Credentials
from .helper.helper import change_table
from config_reader import config

def get_google_sheet_client():
    creds = Credentials.from_service_account_file("credentials.json", scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    return gspread.authorize(creds)

def send_night_report(data: list):
    client = get_google_sheet_client()
    sheet = client.open_by_key(config.google_sheets_reports.get_secret_value())
    reports = sheet.worksheet("reports")

    report_data = change_table(data)

    reports.append_rows(report_data)

    return report_data