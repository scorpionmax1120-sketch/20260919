"""Step 7 — 加上自動測試（程式碼與 Step 6 相同）

假資料先用 dict，Step 8 才換成 SQLite。
先讓流程跑起來，再換掉底層 —— 這是分層的價值。
"""
import secrets

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/api/me")
def me(authorization: str = Header(default="")):
    token = authorization.replace("Bearer ", "")     # 取出通行證
    username = TOKENS.get(token)

    if not username:                                 # 沒帶，或不認得
        raise HTTPException(status_code=401, detail="請先登入")

    u = USERS[username]
    # 注意：沒有回傳 password。永遠不要回傳密碼。
    return {"username": username, "name": u["name"], "dept": u["dept"]}
