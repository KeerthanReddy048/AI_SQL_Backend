def load_schema(cursor):
    cursor.execute("""
    SELECT table_name, column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position;
    """)

    schema = "Here is the database schema:\n"
    for table, column, dtype in cursor.fetchall():
        schema += f"Table: {table}, Column: {column}, Type: {dtype}\n"
    return schema
    