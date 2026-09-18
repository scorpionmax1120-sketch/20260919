"""Step 3 — POST 與資料驗證

型別標註就是全部的設定：宣告輸入長什麼樣，
框架會自動幫你擋掉不合格的請求。
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class LoginIn(BaseModel):           # 宣告：這支 API 的輸入長這樣
    username: str
    password: str


@app.post("/api/login")
def login(data: LoginIn):           # ← 型別標註就是全部的設定
    return {"你送來的帳號是": data.username}
