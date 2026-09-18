"""Step 2 — 換上框架：同樣的事，五行寫完

先安裝：pip install fastapi uvicorn
啟動：  uvicorn main:app --reload
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello")              # 路由：誰來敲 /api/hello，就執行下面這個函式
def hello():
    return {"message": "Hello from FastAPI"}     # dict 會自動變成 JSON
