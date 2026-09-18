# Step 3 — POST 與 Pydantic 驗證

## 跑起來

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 試試看

打開 <http://127.0.0.1:8000/docs>，找到 `POST /api/login`，按 **Try it out**。

1. 正常送出 `{"username": "jase", "password": "1234"}` → **200**
2. **故意少送 password** → **422**，而且錯誤訊息會清楚指出缺哪個欄位

## 重點

那個 422 是 Pydantic 幫你擋下來的，你一行檢查都沒寫。

## 用指令測

```bash
curl -X POST http://127.0.0.1:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"jase","password":"1234"}'
```
