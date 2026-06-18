FROM python:3.11-slim

WORKDIR /app

COPY ai-triage ./ai-triage

CMD ["python3", "ai-triage/triage.py"]
