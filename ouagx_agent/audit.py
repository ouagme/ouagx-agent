import sqlite3
from datetime import datetime,timezone
class AuditLog:
    def __init__(self,db_path):
        self.db=sqlite3.connect(db_path)
        self.db.execute("CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp TEXT,action TEXT,permission TEXT,status TEXT,details TEXT)")
        self.db.commit()
    def log(self,action,permission,status,details=""):
        self.db.execute("INSERT INTO audit(timestamp,action,permission,status,details) VALUES(?,?,?,?,?)",(datetime.now(timezone.utc).isoformat(),action,permission,status,details))
        self.db.commit()
    def recent(self,limit=20): return self.db.execute("SELECT timestamp,action,permission,status,details FROM audit ORDER BY id DESC LIMIT ?",(limit,)).fetchall()
