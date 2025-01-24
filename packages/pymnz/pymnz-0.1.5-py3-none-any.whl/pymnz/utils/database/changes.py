from sqlalchemy import text


def unique_column(conn, table_name, key_col):
    """Alterar coluna para que seja única"""
    query = text(f"""
        ALTER TABLE {table_name}
        ADD CONSTRAINT UNIQUE ({key_col});
    """)
    result = conn.execute(query)
    return result.scalar()


def id_autoincrement(conn, table_name):
    """Alterar tabela para adicionar a coluna 'id' com autoincrement"""
    query_alter = text(f"""
        ALTER TABLE {table_name}
        ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;
    """)
    result = conn.execute(query_alter)
    return result.scalar()
