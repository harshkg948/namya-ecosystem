FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run dynamically PORT environment variable pass karta hai
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}