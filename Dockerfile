FROM python:3.11-slim

WORKDIR /app
COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
