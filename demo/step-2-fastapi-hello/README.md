# Step 2 — 第一支 FastAPI

## 跑起來

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

`main` 是檔名、`app` 是變數名，`--reload` 讓你存檔就自動重啟。

## 你應該看到

- <http://127.0.0.1:8000/api/hello> 回傳 `{"message":"Hello from FastAPI"}`
- <http://127.0.0.1:8000/docs> — **你什麼都沒寫，它自己生出來的 API 文件**，還可以直接測試

## 跟 Step 1 的差別

Step 1 你要自己判斷路徑、自己組標頭、自己轉 JSON。
框架把這些重複的事情包好了 —— 這就是「框架」的意義。

## 從這裡開始的習慣

每寫一支 API，就回 `/docs` 測一次。這是今天最省時間的除錯習慣。
