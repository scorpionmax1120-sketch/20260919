# Step 4 — 登入 API

## 規格（先設計，再動手）

| 項目 | 內容 |
| --- | --- |
| 路徑 | `POST /api/login` |
| 輸入 | `{"username": "jase", "password": "1234"}` |
| 成功 | `200` · `{"token": "一串隨機字串"}` |
| 失敗 | `401` · `{"detail": "帳號或密碼錯誤"}` |
| 不能做 | 回傳密碼；區分「帳號不存在」與「密碼錯誤」 |

## 跑起來

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 兩種情況都要測

到 `/docs` 測：

- `jase` / `1234` → **200**，拿到 token
- `jase` / `xxxx` → **401**
- `nobody` / `1234` → **401**（訊息跟上面**一模一樣**）

## 為什麼發 token 而不是每次送密碼

密碼只在登入時出現一次；token 可以設定有效期，外洩了作廢就好，密碼不用改。
