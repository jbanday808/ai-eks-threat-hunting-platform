FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --upgrade pip setuptools wheel jaraco.context

COPY ai-triage ./ai-triage

CMD ["python3", "ai-triage/triage.py"]
