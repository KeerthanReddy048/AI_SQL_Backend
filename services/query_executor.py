import time

def execute_query(cursor, conn, sql):
    start = time.perf_counter()
    cursor.execute(sql)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    exec_ms = round((time.perf_counter() - start) * 1000, 2)
    return columns, rows, exec_ms
