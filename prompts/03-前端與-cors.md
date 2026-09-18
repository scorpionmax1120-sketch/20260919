# 03 · 前端登入頁與 CORS

對應簡報 Step 6、demo 的 `step-5-frontend-login`。

---

## 3-1 登入頁

```
你是前端工程師，對象是剛學會 HTML 的學生。

目標：寫一個登入頁 index.html，配一支 login.js。

規格：
- 表單有 username、password 兩個欄位和一個登入按鈕
- 按下登入時用 fetch 呼叫 http://127.0.0.1:8000/api/login
- 成功：把回傳的 token 存進 localStorage，跳轉到 profile.html
- 失敗：在畫面上顯示「登入失敗」，不要用 alert

限制：
- 只用原生 HTML / CSS / JavaScript，不要用 React 或任何框架
- 不要用 jQuery
- fetch 的每個參數都要有繁體中文註解，說明它對應 HTTP 的哪個部分

輸出：index.html、login.js、style.css 三個完整檔案。
```

---

## 3-2 CORS

**先讓錯誤發生，再問。** 按下登入，打開 F12 → Console，把完整錯誤訊息貼給它：

```
我的前端跑在 http://127.0.0.1:5500，後端是 FastAPI 跑在
http://127.0.0.1:8000。按下登入時，Console 出現這段錯誤：

（貼上完整的 CORS 錯誤訊息）

請先說明這個錯誤是誰擋的、為什麼要擋，再告訴我後端要怎麼改。

限制：
- allow_origins 請只列我的前端網址，不要用 "*"
- 說明為什麼正式環境不能用 "*"
```

---

## 你應該學到的三件事

1. **CORS 是瀏覽器擋的，不是後端壞了** —— 用 `curl` 打同一支 API 會成功
2. 同源政策存在的理由：否則惡意網站可以偷偷用你的身分去打別人的 API
3. `allow_origins=["*"]` 上線 = 對全世界說「歡迎拿我的資料」
