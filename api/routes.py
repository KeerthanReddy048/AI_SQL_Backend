from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from app.db.connection_manager import disconnect_db,connect_db, get_active_db
from app.db.connection import get_db
from app.db.schema_loader import load_schema
from app.core.llm import generate_sql
from app.services.sql_validator import validate_sql
from app.services.intent_classifier import classify_rule_based, classify_ml
from app.services.query_executor import execute_query
from app.utils.logger import log_query

router = APIRouter()

class DBConfig(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str

class ConnectRequest(BaseModel):
    db_config: DBConfig


class QueryRequest(BaseModel):
    user_query: str


@router.post("/db/connect")
def connect_database(payload: ConnectRequest):
    try:
        connect_db(payload.db_config.model_dump())
        return {"status": "connected"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/db/disconnect")
def disconnect_database():
    disconnect_db()
    return {"status": "disconnected"}

@router.post("/query")
def run_query(payload: QueryRequest):
    user_query = payload.user_query

    try:
        conn, cursor = get_active_db()
    except RuntimeError:
        return {"error": "Database not connected"}
    
    schema = load_schema(cursor)

    intent = classify_rule_based(user_query)
    if intent != "read_query":
        return {"error": "This Operation is not supported"}

    if classify_ml(user_query) != "read_query":
        return {"error": "This Operation is not supported"}

    prompt = f"{schema}\nUser question: {user_query}"

    sql = generate_sql(prompt)
    safe_sql = validate_sql(sql)

    columns, rows, exec_ms = execute_query(cursor, conn, safe_sql)

    log_query(user_query, sql, True, exec_ms, len(rows), 0, "success")

    return {
        "columns": columns,
        "sql": sql,
        "rows": rows,
        "exec_ms": exec_ms
    }

