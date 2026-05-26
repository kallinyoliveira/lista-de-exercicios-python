import sqlite3
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")
conexao.commit()

def cadastrar_usuario(nome, email):
    try:
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print(f"Usuário '{nome}' cadastrado com sucesso total!")
    except sqlite3.IntegrityError:
        print(f"Erro de Sistema: O e-mail '{email}' já está em uso por outro colaborador. Registro Negado!")

print("--- Rodada 1 de Cadastros ---")
cadastrar_usuario("Felipe Melo", "felipe@empresa.com")
print("\n--- Rodada 2 de Cadastros ---")
cadastrar_usuario("Amanda Rodrigues", "felipe@empresa.com")

cursor.close()
conexao.close()