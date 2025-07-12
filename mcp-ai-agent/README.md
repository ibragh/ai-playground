# MCP AI Agent

This repository provides a Dockerized FastAPI backend that connects to the Mixtral 8x7B model via vLLM. The service allows chatting, PDF ingestion with OCR, and tool execution via LangChain agents.

## Requirements
- Docker
- Docker Compose

## Quick Start
```bash
# build and run
cd mcp-ai-agent
docker-compose up --build
```
The API will be accessible at `http://localhost:8000`.

### API Endpoints
- `POST /chat` – Chat with the agent
- `POST /upload` – Upload PDF documents for context
- `GET /ocr/preview` – Run OCR on an image and preview extracted text

### Auto Shutdown
A cron-friendly script `idle-check.sh` checks for idle containers and stops them to save costs on DigitalOcean.

## Folder Structure
- `app/` – FastAPI application and LangChain logic
- `Dockerfile` – Container build file
- `docker-compose.yml` – Composition for API and model services

### Environment Variables
Configure environment variables in `app/config.py` or via Docker Compose overrides.
