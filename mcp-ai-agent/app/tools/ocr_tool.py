from paddleocr import PaddleOCR

ocr_model = PaddleOCR(lang='ar')

def run_ocr(image_bytes: bytes) -> str:
    result = ocr_model.ocr(image_bytes)
    text = '\n'.join([line[1][0] for line in result])
    return text
