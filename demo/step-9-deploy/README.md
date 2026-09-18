# Step 9 — 部署到 Render

跟 Step 8 的差別只有三點，但這三點決定了它能不能上線。

| | Step 8（本機） | Step 9（可部署） |
| --- | --- | --- |
| 前端 | Live Server 另外開，跟後端不同來源 | **後端自己供應**，同一個來源 |
| CORS | 正式環境要另外設定 | 正式環境**根本不需要** |
| 資料庫 | 手動跑一次 `init_db.py` | **啟動時自動建立** |
| port | 寫死 8000 | 由平台的 `PORT` 環境變數決定 |

## 本機跑起來

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

打開 <http://127.0.0.1:8000> —— **前端和 API 都在這裡**，不用再開 Live Server。

測試：`pytest -v` → **17 passed**

## 部署到 Render

### 1. 先把程式碼推上 GitHub

Render 是從 GitHub 拉程式碼的，所以你的專案必須先在 GitHub 上。

### 2. 在 Render 建立服務

到 [render.com](https://render.com) 用 GitHub 帳號登入 → **New** → **Web Service** → 選你的 repo。

填三個欄位：

| 欄位 | 填什麼 |
| --- | --- |
| **Language / Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

方案選 **Free**，然後按 Create Web Service。

> 如果你是把整個課程 repo 推上去（而不是只有這個資料夾），
> 還要設定 **Root Directory** 為 `demo/step-9-deploy`。

### 3. 等它跑完

第一次建置大約 2–5 分鐘。看到 **Live** 之後，你會拿到一個網址，
長得像 `https://miniprofile-xxxx.onrender.com`。

用手機的**行動網路**打開它（不要用同一個 Wi-Fi）—— 這才算真的對外。

## 免費方案的三個坑

### 坑 1：閒置會睡著

免費方案在沒有人訪問一段時間後會**自動停機**，下一個人打開時要等
**30–60 秒**冷啟動。第一次點開以為壞了，其實只是在開機。

> 課堂 demo 前先自己打開一次把它叫醒。

### 坑 2：硬碟是暫時的

免費方案**沒有持久磁碟**。服務一重啟（睡醒、重新部署、平台維護），
`app.db` 就消失了，所有註冊過的資料都不見。

這就是為什麼 `main.py` 每次啟動都會跑 `init_db()` ——
否則睡醒之後連測試帳號都沒有，登入直接失敗。

**要真的保存資料，必須用外部資料庫**（Render 的 PostgreSQL，或其他託管服務）。
這是你下一步該學的東西。

### 坑 3：免費方案的規則會變

額度、休眠時間、要不要綁信用卡，這些平台隨時在調整。
**上課前一週請自己從頭跑一次**，確認流程沒變。

## 上線後檢查清單

- [ ] 用手機的行動網路打開（不是教室 Wi-Fi）
- [ ] 網址列有鎖頭（HTTPS）
- [ ] 登入流程完整走一次（正確與錯誤帳密都試）
- [ ] 直接打 `/profile.html`（沒登入）會被踢回登入頁
- [ ] GitHub 上沒有 `app.db`、`.env`、任何密碼或金鑰
- [ ] 重新整理個人資料頁，資料還在

## 還沒做、但正式專案一定要做的

- 密碼必須雜湊後才存（`bcrypt` / `argon2`），現在是明文
- token 要有過期時間（改用 JWT），而且現在存在記憶體裡，重啟就全部失效
- 資料要放在真正的資料庫，不是隨服務一起消失的 SQLite 檔
