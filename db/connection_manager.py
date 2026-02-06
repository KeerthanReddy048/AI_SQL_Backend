import psycopg2

_active_connection = None
_active_cursor = None

def connect_db(db_config: dict):
    global _active_connection, _active_cursor

    if _active_connection:
        return

    _active_connection = psycopg2.connect(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["username"],
        password=db_config["password"],
        port=int(db_config["port"])
    )
    _active_cursor = _active_connection.cursor()


def get_active_db():
    if not _active_connection or not _active_cursor:
        raise RuntimeError("No active database connection")
    return _active_connection, _active_cursor


def disconnect_db():
    global _active_connection, _active_cursor

    if _active_cursor:
        _active_cursor.close()
    if _active_connection:
        _active_connection.close()

    _active_connection = None
    _active_cursor = None
