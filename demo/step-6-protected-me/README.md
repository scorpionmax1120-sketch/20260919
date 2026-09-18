# Step 6 — 受保護的 API + 完整流程

這一步之後，登入 → 個人資料的整條流程就通了。

## 跑起來

後端：`uvicorn main:app --reload`
前端：VS Code 開 `web/index.html` → Go Live

## /api/me 的規格

| 情況 | 請求 | 回應 |
| --- | --- | --- |
| 正常 | 帶 `Authorization: Bearer <token>` | `200` · 個人資料 |
| 沒帶 | 沒有 Authorization 標頭 | `401` |
| 亂帶 | token 不在名單上 | `401` |

## 一定要驗收這五件事

1. `jase` / `1234` 登入 → 看到「王小明 / 資訊管理系」
2. 重新整理 profile 頁 → 資料還在（token 存在 localStorage）
3. 按登出 → 被踢回登入頁
4. **直接在網址列打 `profile.html`（沒登入）→ 應該被踢回登入頁**
5. 到 `/docs` 測 `/api/me` 不帶 token → `401`

第 4 點就是「後端才是守門人」的意思：前端可以自己跳過去，但拿不到任何資料。
