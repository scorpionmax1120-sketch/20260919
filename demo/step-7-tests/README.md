# Step 7 — 用測試把成果鎖住

`main.py` 跟 Step 6 完全一樣，這一步只多了 `test_main.py`。

## 跑測試

```bash
pip install -r requirements.txt
pytest -v
```

**不需要先啟動 uvicorn。** `TestClient` 是一個假的瀏覽器，會直接把請求送進 app。

## 你應該看到

```
13 passed
```

## 故意讓它失敗一次

把 `main.py` 裡 `/api/me` 的 `status_code=401` 改成 `403`，再跑一次：

```
FAILED test_main.py::test_me_without_token
E       assert 403 == 401
```

看懂三件事：哪個測試掛了、期待什麼、實際拿到什麼。其他 12 個還是綠的 —— 問題被縮小到一個地方了。改回來再跑一次。

## 這 13 個測試在測什麼

| 類別 | 測試 |
| --- | --- |
| 正常 | 登入成功、token 每次不同 |
| 異常 | 密碼錯、帳號不存在、缺欄位、空字串、超長字串、SQL 注入字串 |
| 資安 | 錯誤訊息不洩漏帳號是否存在、回應不含密碼 |
| 權限 | 有 token、沒 token、錯 token |

`test_login_error_message_does_not_leak` 和 `test_me_never_returns_password`
這兩個是**資安測試** —— 它們測的不是「會不會壞」，是「會不會外洩」。
