FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip

# Install essential dependencies directly to avoid Windows line-ending (CRLF) issues
RUN pip install --no-cache-dir fastapi==0.110.0 uvicorn==0.28.0 pydantic==2.6.4 pydantic-settings==2.2.1 requests==2.31.0

COPY . .

EXPOSE 8080

CMD ["python", "start.py"]