"""pytest 執行前的準備工作。

pytest 會自動載入這個檔案。這裡確保 app.db 存在，
等同於先手動跑一次 python3 init_db.py。

沒有這個檔案的話，忘記建資料庫就會看到一整排
「sqlite3.OperationalError: no such table: users」，
而真正的原因跟測試本身無關。
"""
import pathlib
import sqlite3

BASE = pathlib.Path(__file__).parent

if not (BASE / "app.db").exists():
    con = sqlite3.connect(BASE / "app.db")
    con.executescript((BASE / "schema.sql").read_text(encoding="utf-8"))
    con.commit()
    con.close()
