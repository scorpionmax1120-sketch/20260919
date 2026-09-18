# 01 · 伺服器與第一支 API

對應簡報 Step 1–3、demo 的 `step-1` ~ `step-3`。

---

## 1-1 最原始的伺服器

```
你是 Python 教學者，對象是第一次寫後端的大學生。

目標：用 Python 標準函式庫（不要裝任何套件）寫一個最簡單的
HTTP 伺服器，聽在 127.0.0.1:8000，任何 GET 請求都回傳純文字
「我是伺服器」。

限制：
- 不要用 Flask 或 FastAPI
- 程式碼不超過 15 行
- 每一行都要有繁體中文註解，解釋它在做什麼

輸出：完整可執行的 main.py，以及啟動指令。
```

**驗收**：跟 `demo/step-1-hello-server/main.py` 比一比，應該幾乎一樣。

---

## 1-2 換成 FastAPI

```
你是資深 Python 後端工程師。

目標：把上面那個伺服器改用 FastAPI 重寫，提供一支
GET /api/hello，回傳 JSON {"message": "Hello from FastAPI"}。

限制：
- 只寫這一支 API
- 不要加資料庫、不要加認證
- 說明 uvicorn 的啟動指令中，main 和 app 分別代表什麼

輸出：完整的 main.py、requirements.txt、啟動指令。
```

**追問一句好問題**：

> 為什麼用 FastAPI 比我自己用 http.server 判斷路徑好？請舉一個具體的例子。

---

## 1-3 POST 與資料驗證

```
你是資深 Python 後端工程師。

目標：加上一支 POST /api/login，接收 JSON 格式的
username 和 password，先原樣回傳看看有沒有收到。

限制：
- 用 Pydantic 的 BaseModel 宣告輸入格式
- 不要寫任何驗證邏輯，這一步只確認資料有收到
- 解釋為什麼少送欄位時會自動回 422

輸出：完整的 main.py，以及用 curl 測試的指令。
```

**一定要做的實驗**：到 `/docs` 故意少送一個欄位，看它回 422。那是 Pydantic 幫你擋下來的，你一行檢查都沒寫。
