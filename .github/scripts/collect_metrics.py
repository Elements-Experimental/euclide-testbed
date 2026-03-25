import json
import os
import subprocess
import sys
from datetime import datetime, timezone

head_sha   = os.environ["HEAD_SHA"]
base_sha   = os.environ["BASE_SHA"]
merged_at  = os.environ["MERGED_AT"]
pr_created = os.environ["PR_CREATED"]
pr_number  = os.environ["PR_NUMBER"]
pr_title   = os.environ["PR_TITLE"]
pr_url     = os.environ["PR_URL"]
pr_author  = os.environ["PR_AUTHOR"]
repo       = os.environ["REPO"]
files_touched = os.environ["FILES_TOUCHED"]

# cycle_time: first commit on branch to merged_at (hours)
git_result = subprocess.run(
    ["git", "log", "--reverse", "--format=%ct", base_sha + ".." + head_sha],
    capture_output=True, text=True
)
commits = [int(x) for x in git_result.stdout.split() if x.strip()]
if not commits:
    # fallback: oldest commit reachable from HEAD
    fb = subprocess.run(["git", "log", "--format=%ct", "HEAD"],
                        capture_output=True, text=True)
    commits = [int(x) for x in fb.stdout.split() if x.strip()]
first_commit = commits[0] if commits else 0
merged_epoch = int(datetime.fromisoformat(merged_at.replace("Z", "+00:00")).timestamp())
cycle_time = round((merged_epoch - first_commit) / 3600, 2) if first_commit else 0

# time_to_passing_tests and retry_rate from CI workflow runs
with open("/tmp/ci_runs.json") as f:
    runs_data = json.load(f)
ci_runs = [r for r in runs_data.get("workflow_runs", []) if r.get("name") == "CI"]
retry_rate = max(0, len(ci_runs) - 1)

pr_created_dt = datetime.fromisoformat(pr_created.replace("Z", "+00:00"))
time_to_passing = 0
for run in sorted(ci_runs, key=lambda r: r["created_at"]):
    if run.get("conclusion") == "success":
        run_done = datetime.fromisoformat(run["updated_at"].replace("Z", "+00:00"))
        time_to_passing = round((run_done - pr_created_dt).total_seconds() / 60, 1)
        break

# Write outputs
github_output = os.environ.get("GITHUB_OUTPUT", "")
if github_output:
    with open(github_output, "a") as f:
        f.write("cycle_time=" + str(cycle_time) + "\n")
        f.write("time_to_passing=" + str(time_to_passing) + "\n")
        f.write("retry_rate=" + str(retry_rate) + "\n")
        f.write("files_touched=" + files_touched + "\n")
        f.write("pr_number=" + pr_number + "\n")
        f.write("pr_title=" + pr_title + "\n")
        f.write("pr_url=" + pr_url + "\n")
        f.write("pr_author=" + pr_author + "\n")

print("cycle_time=" + str(cycle_time))
print("time_to_passing=" + str(time_to_passing))
print("retry_rate=" + str(retry_rate))
print("files_touched=" + files_touched)
print("pr_title=" + pr_title)
print("pr_url=" + pr_url)
print("pr_author=" + pr_author)
