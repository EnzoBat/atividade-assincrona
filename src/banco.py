import sqlite3

DB_PATH = 'src/alunos.db'


conexao = sqlite3.connect(DB_PATH)
cursor = conexao.cursor()


sql_create_table = '''
CREATE TABLE IF NOT EXISTS Aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento TEXT NOT NULL,
    telefone TEXT
);
'''


cursor.execute(sql_create_table)


conexao.commit()
conexao.close()