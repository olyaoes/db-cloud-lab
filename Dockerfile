FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY db-laba/app.py /app/app.py

COPY db-laba /app/db-laba

ENV PYTHONUNBUFFERED=1

EXPOSE 1401
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:1401"]
