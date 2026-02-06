import psycopg2

def get_db():
    conn = psycopg2.connect(
        host="db.wrwpdxrnuilyccgdftxq.supabase.co",
        database="postgres",
        user="readonly_user",
        password="USER_123",
        port=5432
    )
    return conn, conn.cursor()
