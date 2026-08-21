# 🐳 Docker Deployment Guide

## Overview

This guide explains how to containerize and deploy your Diabetes Predictor application using Docker.

## Prerequisites

- Docker installed ([Get Docker](https://www.docker.com/get-started))
- Your application is ready to deploy

## Quick Start with Docker

### 1. Build the Docker Image

```bash
cd fastapi-docker-for-ml-model-deployment
docker build -t diabetes-predictor:latest .
```

### 2. Run the Container

```bash
docker run -p 8000:8000 diabetes-predictor:latest
```

### 3. Access the Application

Open your browser to: `http://localhost:8000/`

## Docker Compose (Recommended)

### Create `docker-compose.yml`

```yaml
version: "3.8"

services:
  diabetes-predictor:
    build: .
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
    volumes:
      - ./diabetes-predictor/models:/app/models
    command: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Run with Docker Compose

```bash
docker-compose up
```

## Dockerfile (if needed)

Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY diabetes-predictor/ ./diabetes-predictor/

# Set working directory
WORKDIR /app/diabetes-predictor

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Common Docker Commands

### Build Image

```bash
docker build -t diabetes-predictor:1.0 .
```

### Run Container

```bash
# Basic run
docker run -p 8000:8000 diabetes-predictor

# Run in background
docker run -d -p 8000:8000 --name predictor diabetes-predictor

# Run with environment variables
docker run -p 8000:8000 -e PYTHONUNBUFFERED=1 diabetes-predictor

# Run with volume mounting
docker run -p 8000:8000 -v $(pwd)/models:/app/models diabetes-predictor
```

### View Logs

```bash
docker logs <container_id>
docker logs -f <container_id>  # Follow logs
```

### Stop Container

```bash
docker stop <container_id>
```

### Remove Container

```bash
docker rm <container_id>
```

### List Images

```bash
docker images
```

### List Running Containers

```bash
docker ps
```

## Production Deployment

### 1. Multi-stage Build (Optimization)

```dockerfile
FROM python:3.10-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY diabetes-predictor/ ./diabetes-predictor/

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

WORKDIR /app/diabetes-predictor

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. With Gunicorn (Production Server)

Install gunicorn:

```bash
pip install gunicorn
```

Update requirements.txt to include gunicorn.

Dockerfile:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY diabetes-predictor/ ./diabetes-predictor/

WORKDIR /app/diabetes-predictor

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app.main:app"]
```

### 3. Environment Variables

Create a `.env` file:

```
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

Update app to use environment variables in main.py:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == "True"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
```

## Deployment Platforms

### Heroku

```bash
# Install Heroku CLI
# Create app
heroku create your-diabetes-predictor

# Create Procfile
echo "web: python -m uvicorn diabetes-predictor/app/main:app --host 0.0.0.0 --port $PORT" > Procfile

# Deploy
git push heroku main
```

### AWS (ECS/Fargate)

```bash
# Push image to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin [your-account-id].dkr.ecr.us-east-1.amazonaws.com

docker tag diabetes-predictor:latest [your-account-id].dkr.ecr.us-east-1.amazonaws.com/diabetes-predictor:latest

docker push [your-account-id].dkr.ecr.us-east-1.amazonaws.com/diabetes-predictor:latest
```

### Google Cloud Run

```bash
# Build image
docker build -t gcr.io/[PROJECT-ID]/diabetes-predictor .

# Push to Google Container Registry
docker push gcr.io/[PROJECT-ID]/diabetes-predictor

# Deploy
gcloud run deploy diabetes-predictor \
  --image gcr.io/[PROJECT-ID]/diabetes-predictor \
  --platform managed \
  --region us-central1 \
  --port 8000
```

### DigitalOcean App Platform

```bash
# Install doctl CLI
# Connect container registry
doctl auth init

# Tag image
docker tag diabetes-predictor:latest registry.digitalocean.com/[YOUR-REGISTRY]/diabetes-predictor:latest

# Push image
docker push registry.digitalocean.com/[YOUR-REGISTRY]/diabetes-predictor:latest

# Deploy via DigitalOcean dashboard
```

## Docker Networking

### Run with Custom Network

```bash
# Create network
docker network create diabetes-net

# Run container
docker run -d --name predictor --network diabetes-net -p 8000:8000 diabetes-predictor

# Run another service on same network
docker run -d --name db --network diabetes-net postgres
```

## Docker Compose with Database

```yaml
version: "3.8"

services:
  predictor:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/predictor
    networks:
      - diabetes-network

  postgres:
    image: postgres:14-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=predictor
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - diabetes-network

volumes:
  postgres_data:

networks:
  diabetes-network:
```

## Monitoring & Logging

### Health Checks in Docker

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')"
```

### Logging

```bash
# View logs with timestamps
docker logs --timestamps diabetes-predictor

# Follow logs in real-time
docker logs -f diabetes-predictor

# View last 100 lines
docker logs --tail 100 diabetes-predictor
```

## Security Best Practices

1. **Use Non-root User**

```dockerfile
RUN useradd -m appuser
USER appuser
```

2. **Read-only Filesystem**

```bash
docker run --read-only --tmpfs /tmp diabetes-predictor
```

3. **Resource Limits**

```bash
docker run -m 512m --cpus="1.0" diabetes-predictor
```

4. **Security Scanning**

```bash
docker scan diabetes-predictor
```

## Troubleshooting

### Port Already in Use

```bash
# Change port mapping
docker run -p 8001:8000 diabetes-predictor
```

### Out of Memory

```bash
# Increase memory limit
docker run -m 2g diabetes-predictor
```

### Permission Denied

```bash
# Run with sudo (if needed)
sudo docker run -p 8000:8000 diabetes-predictor
```

### Container Exits Immediately

```bash
# Check logs
docker logs [container_id]
```

## Clean Up

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Remove everything (careful!)
docker system prune -a
```

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/concepts/)
- [Uvicorn](https://www.uvicorn.org/)

---

**Happy containerizing! 🐳**
