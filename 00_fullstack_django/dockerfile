# Builder
FROM python:3.13.9-slim AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

# Final image 
FROM python:3.13.9-slim

RUN groupadd -g 1001 djangoapp && \
    useradd -m -u 1001 -g djangoapp djangoapp

WORKDIR /app

# Copy installed Python packages
COPY --from=builder /install /usr/local

# Copy app and set owner as djangoapp user
COPY --chown=djangoapp:djangoapp ./fullstack_django/ .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

USER djangoapp

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
