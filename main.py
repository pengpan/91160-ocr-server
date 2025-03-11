from typing import Optional, Any

import ddddocr
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()
ocr = ddddocr.DdddOcr(
    ocr=False,
    det=False,
    show_ad=False,
    import_onnx_path="models/91160-ocr.onnx",
    charsets_path="models/charsets.json"
)


class Result(BaseModel):
    code: int
    msg: str
    data: Optional[Any] = None


@app.post("/ocr", response_model=Result)
async def ocr_endpoint(image: str = Form(None)):
    try:
        if image is None or image.strip() == '':
            return Result(code=400, msg='image is blank')
        data = ocr.classification(image)
        return Result(code=200, msg='ok', data=data)
    except Exception as e:
        return Result(code=500, msg=str(e))
