import sqlite3
from datetime import datetime,timezone
class Memory:
    def __init__(self,db_path):
        self.db=sqlite3.connect(db_path)
        self.db.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY AUTOINCREMENT,key TEXT UNIQUE,value TEXT,updated_at TEXT)")
        self.db.commit()
    def set(self,key,value):
        self.db.execute("INSERT INTO memory(key,value,updated_at) VALUES(?,?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value,updated_at=excluded.updated_at",(key,value,datetime.now(timezone.utc).isoformat())); self.db.commit()
    def get(self,key):
        r=self.db.execute("SELECT value FROM memory WHERE key=?",(key,)).fetchone(); return r[0] if r else None
