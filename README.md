# Cybersecurity Sales Development Toolkit
An AI-assisted educational portfolio prepared for Palla Shanmukha Himesh. Candidate review and independent practice remain pending. All accounts and qualification data are fictional. No outreach was sent and no sales results are claimed.

## Contents
- `accounts.csv`: 20 fictional accounts with prospect personas, hypothesized needs and BANT fields.
- `outreach.md`: five segment-specific opening emails, a follow-up sequence, discovery script and objection handling.
- `crm.py`: dependency-free command-line tracker to list accounts, log simulated activity and report funnel counts.

## Run
Python 3 required. From this directory:
```
python crm.py list
python crm.py log SIM-01 --channel call --outcome discovery --note "Role-play: ask who owns training approval"
python crm.py report
```
Activity is saved locally to `activities.json`. It is ignored by Git to avoid publishing future notes accidentally. Never place real contact details in this public sample.

## Qualification discipline
BANT means Budget, Authority, Need and Timeline. Unknown is a valid answer; do not mark a prospect qualified based on industry alone. Handoff requires a confirmed problem, buying-process understanding and an agreed next step, subject to the employer's SQL rules.

## Candidate practice
Rewrite emails in your own words, role-play two discovery calls, inspect the CSV, explain the report and practice with a CRM sandbox. This repository does not establish proficiency in Zoho CRM, Apollo, Lusha, Sales Navigator, Claude or NotebookLM.
