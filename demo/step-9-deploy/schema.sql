-- MiniProfile 的資料表
-- 注意：這裡用 IF NOT EXISTS / OR IGNORE，讓它可以重複執行。
-- Step 8 用的是 DROP TABLE，那會在每次重啟時清空資料。

CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,     -- 真實系統這裡要存雜湊值，不是明文
    name     TEXT NOT NULL,
    dept     TEXT NOT NULL
);

INSERT OR IGNORE INTO users (username, password, name, dept) VALUES
    ('jase', '1234', '王小明', '資訊管理系'),
    ('amy',  'abcd', '陳小美', '資訊管理系');
