import sqlite3, csv
from datetime import datetime

DB = "attendance.db"

def init():
    with sqlite3.connect(DB) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,day TEXT NOT NULL,time_in TEXT NOT NULL,UNIQUE(name, day))""")

def mark(name):
    """True if newly marked today, False if already marked."""
    now = datetime.now()
    with sqlite3.connect(DB) as c:
        cur = c.execute("INSERT OR IGNORE INTO attendance(name, day, time_in) VALUES (?,?,?)",
            (name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")),)
        return cur.rowcount == 1

def export_csv(path="report.csv"):
    with sqlite3.connect(DB) as c:
        rows = c.execute("SELECT name, day, time_in FROM attendance ORDER BY day, time_in").fetchall()
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "day", "time_in"])
        w.writerows(rows)
    print(f"Saved {len(rows)} rows to {path}")

if __name__ == "__main__":
    init()
    export_csv()