"""Step 8 — 把假資料換成 SQLite

比較這個檔案和 Step 7 的 main.py：
只有「拿使用者」那一段變了，API 的規格和前端的程式碼一行都不用改。
這就是分層的價值。

先執行一次：python3 init_db.py
"""
import pathlib
import secrets
import sqlite3

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 用「這個檔案所在的資料夾」當基準，不管你從哪裡執行都找得到資料庫。
# 如果寫成 DB = "app.db"，從別的資料夾啟動就會建出一個空的新檔，
# 然後報 no such table: users。
DB = pathlib.Path(__file__).parent / "app.db"
TOKENS: dict[str, str] = {}


def get_user(username: str) -> dict | None:
    """從資料庫拿一個使用者，找不到就回 None。"""
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    row = con.execute(
        "SELECT * FROM users WHERE username = ?",   # ← 用 ? 佔位，不要用字串相加
        (username,),                                #    否則就是 SQL 注入漏洞
    ).fetchone()
    con.close()
    return dict(row) if row else None


class LoginIn(BaseModel):
    username: str
    password: str


@app.post("/api/login")
def login(data: LoginIn):
    user = get_user(data.username)           # ← 唯一改掉的一行
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="帳號或密碼錯誤")

    token = secrets.token_hex(16)
    TOKENS[token] = data.username
    return {"token": token}


@app.get("/api/me")
def me(authorization: str = Header(default="")):
    token = authorization.replace("Bearer ", "")
    username = TOKENS.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="請先登入")

    u = get_user(username)
    return {"username": username, "name": u["name"], "dept": u["dept"]}
