# Dockerfile - simple Python Flask app
FROM python:3.11-slim
WORKDIR /app
# install runtime deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# copy source
COPY . .
ENV PORT=8080
EXPOSE 8080
# run with gunicorn for Cloud Run
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
