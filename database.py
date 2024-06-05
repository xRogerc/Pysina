import sqlite3

conn = sqlite3.connect("Sistema.db")

def conecta_db():
        global cursor
        cursor = conn.cursor()
        print("Conexão ao Banco de Dados feita com sucesso!")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
                Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Password TEXT NOT NULL,
                ConfPassword TEXT NOT NULL
        )""")

        conn.commit()
        print("Tabela Criada com Sucesso!")
