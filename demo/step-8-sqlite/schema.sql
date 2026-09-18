-- MiniProfile 的資料表
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,     -- 真實系統這裡要存雜湊值，不是明文
    name     TEXT NOT NULL,
    dept     TEXT NOT NULL
);

INSERT INTO users (username, password, name, dept) VALUES
    ('jase', '1234', '王小明', '資訊管理系'),
    ('amy',  'abcd', '陳小美', '資訊管理系');
