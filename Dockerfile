FROM python:3.10-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    libfreetype6-dev \
    pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

CMD ["python", "main.py"]
