# Metrics — euclide-testbed

## Google Sheet schema

Each merged PR appends one row to the configured Google Sheet.

| Column | Type | Description |
|---|---|---|
| `timestamp` | ISO 8601 string | UTC timestamp when the row was recorded |
| `project` | string | GitHub repository (`owner/repo`) |
| `pr_number` | integer | Pull request number |
| `cycle_time` | float (hours) | Time from first commit on the branch to merge |
| `time_to_passing_tests` | float (minutes) | Time from PR open to first green CI run |
| `retry_rate` | integer | Number of CI re-runs triggered on the PR (0 = first run passed) |
| `files_touched` | integer | Number of files changed in the PR |
| `pr_title` | string | Title of the pull request |
| `pr_url` | string | URL of the pull request |
| `pr_author` | string | GitHub login of the PR author |

Rows are appended to the tab named **`review_dashboard`**. If your sheet tab has a different name, re-run `copier update` and set `metrics_sheet_name` to match.

Create the sheet's header row manually using these exact column names (in order):
`timestamp`, `project`, `pr_number`, `cycle_time`, `time_to_passing_tests`, `retry_rate`, `files_touched`, `pr_title`, `pr_url`, `pr_author`

## Setup

### 1. Create a Google Cloud service account

1. Open [Google Cloud Console](https://console.cloud.google.com/) → IAM & Admin → Service Accounts.
2. Click **Create Service Account**. Give it a descriptive name (e.g. `metrics-writer`).
3. Grant it no project-level roles (it only needs Sheets access).
4. After creation, open the service account → **Keys** → **Add Key** → **JSON**.
5. Download the JSON key file to your machine.

### 2. Enable the Sheets API

In Google Cloud Console → APIs & Services → Library, search for **Google Sheets API** and enable it for the project that owns the service account.

### 3. Share the target Google Sheet

1. Create (or open) the Google Sheet that will receive metrics.
2. Click **Share** and add the service account email address (visible in the JSON key file as `"client_email"`) with **Editor** access.

### 4. Add the `METRICS_SA_KEY` secret

Base64-encode the JSON key file (produces a single-line string safe for secrets):

```bash
base64 -w0 -i key.json
```

Copy the output. In your GitHub repository go to **Settings → Secrets and variables → Actions → New repository secret**:
- **Name:** `METRICS_SA_KEY`
- **Value:** the base64-encoded string

### 5. Add the `METRICS_SHEET_ID` secret

The Sheet ID is the long alphanumeric string in the Google Sheets URL:
```
https://docs.google.com/spreadsheets/d/<SHEET_ID>/edit
```

Add it as a repository secret:
- **Name:** `METRICS_SHEET_ID`
- **Value:** the Sheet ID from the URL

### 6. Create the header row

Open the Google Sheet and manually type the column headers in row 1:

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| timestamp | project | pr_number | cycle_time | time_to_passing_tests | retry_rate | files_touched | pr_title | pr_url | pr_author |
