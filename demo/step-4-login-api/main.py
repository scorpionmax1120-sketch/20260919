"""Step 4 — 登入 API：驗證帳密，發一張通行證

假資料先用 dict，Step 8 才換成 SQLite。
先讓流程跑起來，再換掉底層 —— 這是分層的價值。
"""
import secrets

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 假資料。真實系統的密碼必須雜湊後才存，絕不能明文。
USERS = {
    "jase": {"password": "1234", "name": "王小明", "dept": "資訊管理系"},
    "amy":  {"password": "abcd", "name": "陳小美", "dept": "資訊管理系"},
}
TOKENS: dict[str, str] = {}      # token -> username


class LoginIn(BaseModel):
    username: str
    password: str


@app.post("/api/login")
def login(data: LoginIn):
    user = USERS.get(data.username)

    # 帳號不存在、密碼錯誤，都回同一個訊息。
    # 分開告知等於幫攻擊者確認哪些帳號存在。
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="帳號或密碼錯誤")

    token = secrets.token_hex(16)     # 發一張隨機通行證
    TOKENS[token] = data.username
    return {"token": token}
