# 04 · 受保護的 API 與個人資料頁

對應簡報 Step 7–8、demo 的 `step-6-protected-me`。

---

## 4-1 /api/me

```
你是資深 Python 後端工程師。

目標：在現有的 main.py 加一支 GET /api/me，只有帶有效 token
的人才拿得到自己的資料。

規格：
- 從 Authorization 標頭讀 token，格式是 "Bearer <token>"
- token 有效 → 200，回 {"username", "name", "dept"}
- 沒帶 token 或 token 無效 → 401，detail 是「請先登入」
- 回應絕對不能包含 password 欄位

限制：
- 用 FastAPI 的 Header 取得標頭，不要自己解析 request
- 不要引入 OAuth2PasswordBearer，我還沒學
- 每段加繁體中文註解

輸出：完整的 main.py。
```

---

## 4-2 個人資料頁

```
目標：寫 profile.html 和 profile.js，顯示登入者的個人資料。

規格：
- 載入時從 localStorage 拿 token
- 沒有 token → 直接跳回 index.html
- 帶 token 呼叫 GET /api/me
- 收到 401 → 也跳回 index.html
- 成功 → 把 username、name、dept 顯示在畫面上
- 有一個登出按鈕，清掉 token 並跳回 index.html

限制：原生 JavaScript，不要框架。
```

---

## 4-3 換成 SQLite

```
目標：把 USERS 這個假資料 dict 換成 SQLite 資料庫。

規格：
- 資料庫檔名 app.db，資料表 users(username, password, name, dept)
- 另外給我一支 init_db.py 負責建表與塞入兩筆測試資料
- main.py 只改「拿使用者」那一段，API 規格和前端都不能動

限制：
- 用 Python 內建的 sqlite3，不要用 SQLAlchemy
- SQL 一定要用 ? 參數化，並解釋為什麼不能用字串相加

輸出：init_db.py、schema.sql、修改後的 main.py。
```

**驗收重點**：改完之後，前端的程式碼應該一行都不用動。這就是分層的價值。
