"""Fictional-data SDR activity tracker; not a production CRM."""
import argparse, csv, json
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parent
p = argparse.ArgumentParser(description=__doc__)
sub = p.add_subparsers(dest="command", required=True)
sub.add_parser("list")
log = sub.add_parser("log")
log.add_argument("account")
log.add_argument("--channel", choices=["call", "email", "linkedin"], required=True)
log.add_argument("--outcome", choices=["attempt", "reply", "discovery", "meeting_booked", "meeting_held", "sales_accepted", "declined"], required=True)
log.add_argument("--note", default="")
sub.add_parser("report")
a = p.parse_args()
with (ROOT / "accounts.csv").open(newline="", encoding="utf-8") as f:
    accounts = list(csv.DictReader(f))
path = ROOT / "activities.json"
activities = json.loads(path.read_text()) if path.exists() else []
if a.command == "list":
    for row in accounts:
        print(row["id"], row["fictional_company"], "|", row["need_hypothesis"])
elif a.command == "log":
    if a.account not in {r["id"] for r in accounts}:
        p.error("Unknown account ID")
    activities.append({"account": a.account, "channel": a.channel, "outcome": a.outcome, "note": a.note, "time": datetime.now(timezone.utc).isoformat()})
    path.write_text(json.dumps(activities, indent=2), encoding="utf-8")
    print("Saved simulated activity")
else:
    print("SIMULATED ACTIVITY ONLY")
    print("Accounts:", len(accounts), "Activities:", len(activities))
    for stage in ["reply", "discovery", "meeting_booked", "meeting_held", "sales_accepted"]:
        count = len({x["account"] for x in activities if x["outcome"] == stage})
        print(stage + " (unique accounts):", count)
