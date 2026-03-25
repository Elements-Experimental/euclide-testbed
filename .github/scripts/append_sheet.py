import base64
import json
import os
import sys
from datetime import datetime, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build

try:
    raw_key = base64.b64decode(os.environ["METRICS_SA_KEY"]).decode("utf-8")
    sa_info = json.loads(raw_key)
    creds = service_account.Credentials.from_service_account_info(
        sa_info, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    svc = build("sheets", "v4", credentials=creds, cache_discovery=False)
    row = [[
        datetime.now(timezone.utc).isoformat(),
        os.environ["GITHUB_REPOSITORY"],
        os.environ["PR_NUMBER"],
        os.environ["CYCLE_TIME"],
        os.environ["TIME_TO_PASSING"],
        os.environ["RETRY_RATE"],
        os.environ["FILES_TOUCHED"],
        os.environ["PR_TITLE"],
        os.environ["PR_URL"],
        os.environ["PR_AUTHOR"],
    ]]
    svc.spreadsheets().values().append(
        spreadsheetId=os.environ["METRICS_SHEET_ID"],
        range=os.environ["METRICS_SHEET_NAME"],
        valueInputOption="RAW",
        body={"values": row},
    ).execute()
    print("Metrics appended successfully.")
except Exception as e:
    print("Metrics error (non-blocking): " + str(e), file=sys.stderr)
