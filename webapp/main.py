from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

from wine_pairing import wine_pairing  

app = FastAPI(
    title="Wine Pairing API",
    description="요리 이미지 URL을 기반으로 와인을 추천해주는 API 서비스입니다.",
    version="1.0.0"
)

# 응답 모델 정의
class WinePairingResponse(BaseModel):
    recommend_wine: str
    recommend_reason: str

# https://sitem.ssgcdn.com/95/55/96/item/1000346965595_i1_750.jpg
@app.post("/", response_model=WinePairingResponse)
def get_wine_pairing(image_url: str):
    print(image_url)
    try:
        result = wine_pairing(image_url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
