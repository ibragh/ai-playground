import fitz  # PyMuPDF
from typing import List


def parse_pdf(data: bytes) -> str:
    doc = fitz.open(stream=data, filetype="pdf")
    texts: List[str] = []
    for page in doc:
        texts.append(page.get_text())
    return "\n".join(texts)
