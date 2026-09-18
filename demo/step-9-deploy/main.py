"""Step 9 — 可以部署到雲端的版本

跟 Step 8 的差別只有三點：

1. 後端同時供應前端的靜態檔案
   → 正式環境只有一個服務、同一個來源，完全沒有 CORS 問題
2. 啟動時自動建立資料庫
   → 免費方案的硬碟是「暫時的」，重啟就清空，所以不能只建一次
3. port 由平台用環境變數 PORT 指定，不能寫死 8000

本機執行：uvicorn main:app --reload    然後開 http://127.0.0.1:8000
"""
import os
import pathlib
import secrets
import sqlite3

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE = pathlib.Path(__file__).parent
DB = BASE / "app.db"
WEB = BASE / "web"


def init_db() -> None:
    """建立資料表並塞入測試帳號。可以重複執行，不會清空既有資料。"""
    con = sqlite3.connect(DB)
    con.executescript((BASE / "schema.sql").read_text(encoding="utf-8"))
    con.commit()
    con.close()


# 在這裡直接呼叫，而不是用 FastAPI 的 lifespan。
# 原因：pytest 的 TestClient(app) 不會觸發 lifespan，
# 資料表就不會被建立，所有測試都會炸在「no such table: users」。
# 寫在模組層級，不管是 uvicorn 啟動還是測試載入，都一定會跑到。
init_db()

app = FastAPI()

# 本機開發時，前端跑在 5500（Live Server）、後端在 8000，是不同來源，
# 所以還是需要 CORS。部署後前端由這個服務自己供應，同源，這段就用不到了。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TOKENS: dict[str, str] = {}


def get_user(username: str) -> dict | None:
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    row = con.execute(
        "SELECT * FROM users WHERE username = ?",   # ← 用 ? 佔位，不要用字串相加
        (username,),
    ).fetchone()
    con.close()
    return dict(row) if row else None


class LoginIn(BaseModel):
    username: str
    password: str


# ── API ──────────────────────────────────────────────────────
# 注意：所有 API 都要寫在最後面的 app.mount 之前，
# 否則會被静態檔案的路由攔截。

@app.post("/api/login")
def login(data: LoginIn):
    user = get_user(data.username)
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


# ── 前端 ─────────────────────────────────────────────────────
# html=True 讓 "/" 自動回傳 web/index.html。
# 這一行一定要放在所有 API 之後。
app.mount("/", StaticFiles(directory=WEB, html=True), name="web")


if __name__ == "__main__":
    # 平台會用 PORT 環境變數告訴你要聽哪個 port，本機沒有就用 8000
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
