import sqlite3
from typing import Any

DB_PATH = "./app.db"

def run_query(query: str) -> Any:
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(query)
        if query.lower().strip().startswith("select"):
            return cur.fetchall()
        conn.commit()
        return "Query executed"
    finally:
        conn.close()
