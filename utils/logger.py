import json
from datetime import datetime
from app.core.config import LOG_FILE

def log_query(question, sql, success, exec_ms, rows, attempts, status):
    entry = {
        "question": question,
        "sql": sql,
        "success": success,
        "exec_ms": exec_ms,
        "rows": rows,
        "attempts": attempts,
        "status": status,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
