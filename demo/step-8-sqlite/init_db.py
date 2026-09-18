"""建立 app.db 並塞入初始資料。執行：python3 init_db.py"""
import pathlib
import sqlite3

BASE = pathlib.Path(__file__).parent      # 以這個檔案的位置為基準

con = sqlite3.connect(BASE / "app.db")
con.executescript((BASE / "schema.sql").read_text(encoding="utf-8"))
con.commit()
con.close()
print("app.db 建好了")
