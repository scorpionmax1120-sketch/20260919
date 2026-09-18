# Step 8 — 換成 SQLite

## 跑起來

```bash
pip install -r requirements.txt
python3 init_db.py          # 只要做一次，會產生 app.db
uvicorn main:app --reload
```

測試：`pytest -v` → **14 passed**

## 跟 Step 7 差在哪

只有「拿使用者」那一段變了：

```python
# Step 7
user = USERS.get(data.username)

# Step 8
user = get_user(data.username)     # 改成查資料庫
```

**API 的規格沒變、前端的程式碼一行都沒改。** 這就是分層的價值 —— 換掉底層儲存，上層無感。

## 那個 `?` 很重要

```python
con.execute("SELECT * FROM users WHERE username = ?", (username,))   # ✓ 安全
con.execute("SELECT * FROM users WHERE username = '" + username + "'")  # ✗ SQL 注入
```

`test_sql_injection_does_not_drop_table` 就是在驗證這件事：
送出 `'; DROP TABLE users; --` 之後，資料表必須還在。

## 還沒做、但正式專案一定要做的

- 密碼必須雜湊後才存（`bcrypt` / `argon2`），現在是明文
- token 要有過期時間（改用 JWT）
- `app.db` 不要 commit 上 GitHub（已寫進 `.gitignore`）
