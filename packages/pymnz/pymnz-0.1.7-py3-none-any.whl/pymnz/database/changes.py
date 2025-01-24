def unique_column(conn, table_name, key_col):
    """Alterar coluna para que seja única"""
    # Importar somente o que é necessário
    from sqlalchemy import text

    query = text(f"""
        ALTER TABLE {table_name}
        ADD CONSTRAINT UNIQUE ({key_col});
    """)
    conn.execute(query)


def id_autoincrement(conn, table_name):
    """Alterar tabela para adicionar a coluna 'id' com autoincrement"""
    # Importar somente o que é necessário
    from sqlalchemy import text

    # Montar query diretamente
    query = text(f"""
        ALTER TABLE {table_name}
        ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;
    """)

    # Executar query
    conn.execute(query)
