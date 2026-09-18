# Step 5 — 前端登入頁與 CORS

## 要開兩個東西

**後端**（終端機）：
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

**前端**：用 VS Code 開啟 `web/index.html`，右下角按 **Go Live**（Live Server 擴充套件）。
網址會是 `http://127.0.0.1:5500/index.html`。

> 不要直接雙擊 HTML 檔案。`file://` 開啟會產生另一種錯誤，不是我們要示範的那個。

## 想親眼看到 CORS 錯誤？

把 `main.py` 裡的 `app.add_middleware(...)` 整段註解掉再登入一次，
按 F12 看 Console，你會看到：

```
Access to fetch at 'http://127.0.0.1:8000/api/login'
from origin 'http://127.0.0.1:5500' has been blocked by CORS policy
```

**這是瀏覽器擋的，不是你的後端壞了。** 用 `curl` 打同一支 API 會成功 —— 因為 curl 不是瀏覽器。

## 測試帳號

`jase` / `1234`
