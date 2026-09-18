"""建立 app.db 並塞入初始資料。執行：python3 init_db.py"""
import pathlib
import sqlite3

con = sqlite3.connect("app.db")
con.executescript(pathlib.Path("schema.sql").read_text(encoding="utf-8"))
con.commit()
con.close()
print("app.db 建好了")
