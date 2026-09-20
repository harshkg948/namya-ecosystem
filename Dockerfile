FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Upgrade pip first
RUN pip install --no-cache-dir --upgrade pip

# Copy and install requirements explicitly
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project code
COPY . .

EXPOSE 8080

CMD ["python", "test_main.py"]