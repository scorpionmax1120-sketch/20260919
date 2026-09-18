# demo — 階段性完成版程式碼

對應簡報 **02-開發.html** 的 Step 1–8。每個資料夾都**可以獨立執行**。

## 這是救援包

課堂上跟不上、或某一步卡住時，直接複製下一個資料夾繼續，**不要卡在原地**。
每個資料夾的 `README.md` 都寫了：這一步做了什麼、怎麼跑、預期看到什麼、跟上一步差在哪。

## 八個階段

| 資料夾 | 做到什麼 | 需要的套件 |
| --- | --- | --- |
| `step-1-hello-server` | 最原始的伺服器，理解「伺服器在聽什麼」 | 無（Python 內建） |
| `step-2-fastapi-hello` | 換上 FastAPI，第一支 GET API，看到 `/docs` | fastapi, uvicorn |
| `step-3-post-pydantic` | POST 與 Pydantic 自動驗證（422） | fastapi, uvicorn |
| `step-4-login-api` | 登入 API：驗證帳密、發 token、失敗回 401 | fastapi, uvicorn |
| `step-5-frontend-login` | 前端登入頁、fetch、**CORS** | fastapi, uvicorn |
| `step-6-protected-me` | `/api/me` 受保護，**完整流程通了** | fastapi, uvicorn |
| `step-7-tests` | 加上 13 個自動測試 | + pytest, httpx |
| `step-8-sqlite` | 假資料換成 SQLite，14 個測試 | + pytest, httpx |
| `step-9-deploy` | **可部署版**：後端供應前端、自動建表、17 個測試 | + pytest, httpx |

## 通用啟動方式

```bash
cd step-4-login-api
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

step-9 例外：它由後端自己供應前端，直接開 <http://127.0.0.1:8000> 就好。

其他有 `web/` 資料夾的步驟（5–8），前端要另外用 VS Code 的 **Live Server** 開啟
（開 `web/index.html` → 右下角 Go Live），網址會是 `http://127.0.0.1:5500`。

> 不要直接雙擊 HTML 檔。`file://` 開啟會產生另一種錯誤，不是課堂要示範的那個。

## 測試帳號

| 帳號 | 密碼 | 姓名 |
| --- | --- | --- |
| `jase` | `1234` | 王小明 |
| `amy` | `abcd` | 陳小美 |

## 驗證狀態

所有步驟都在 Python 3.14 + FastAPI 0.141 + pytest 9.1 實際執行過：

- step-1 啟動後回應 HTTP 200
- step-2 ~ step-6 的每支 API 都回傳預期的狀態碼
- step-7 `pytest` → **13 passed**
- step-8 `pytest` → **14 passed**
- step-9 `pytest` → **17 passed**；並實際用 `PORT=8000 python main.py` 啟動，確認同源供應前端、API 未被靜態路由攔截、刪掉 `app.db` 重啟後測試帳號會自動重建

## 注意

這些是**教學用的簡化版**，不能直接拿去當正式系統：

- 密碼是明文存的，正式專案必須雜湊（`bcrypt` / `argon2`）
- token 沒有過期時間，正式專案應該用 JWT
- token 存在記憶體，伺服器重啟就全部失效
