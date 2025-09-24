import sqlite3
import os


DB_PATH = os.path.join(os.path.dirname(__file__), 'alunos.db')

def get_connection():
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                data_nascimento TEXT NOT NULL,
                status TEXT NOT NULL
            );
        ''')
        conn.commit()


criar_tabela()