from fastapi import FastAPI, UploadFile, File, Depends
from .agent import agent_router
from .pdf.pdf_parser import parse_pdf
from .tools.ocr_tool import run_ocr
import logging

app = FastAPI(title="MCP AI Agent")
logging.basicConfig(level=logging.INFO)

app.include_router(agent_router)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = parse_pdf(content)
    return {"text": text[:500]}

@app.get("/ocr/preview")
async def ocr_preview(file: UploadFile = File(...)):
    text = run_ocr(await file.read())
    return {"text": text[:500]}
