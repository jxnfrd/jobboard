FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn explicitly if not in requirements (it is, but safe to match)
RUN pip install gunicorn

COPY . .

# Create directory for Whoosh index
RUN mkdir -p whoosh_index && chmod 777 whoosh_index

EXPOSE 8000

CMD ["gunicorn", "jobsp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
