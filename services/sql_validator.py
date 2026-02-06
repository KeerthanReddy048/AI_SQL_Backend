import re
from app.core.config import BLOCKED_KEYWORDS

def validate_sql(sql: str) -> str:
    sql = sql.strip()
    upper = sql.upper()

    if not (upper.startswith("SELECT") or upper.startswith("WITH")):
        raise ValueError("Only SELECT queries allowed")

    if sql.count(";") > 1:
        raise ValueError("Multiple SQL statements detected")

    for kw in BLOCKED_KEYWORDS:
        if re.search(rf"\b{kw}\b", upper):
            raise ValueError(f"Forbidden keyword: {kw}")

    if "LIMIT" not in upper:
        sql = sql.rstrip(";") + " LIMIT 100"

    return sql
