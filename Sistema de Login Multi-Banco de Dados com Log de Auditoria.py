import tkinter as tk
import sqlite3
import hashlib
import re
from datetime import datetime
import threading

# Criar banco
conexao = sqlite3.connect("usuarios.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    email TEXT,
    senha TEXT
)
""")

# Usuário exemplo
senha = hashlib.sha256("123".encode()).hexdigest()

cursor.execute(
    "INSERT INTO usuarios VALUES (?, ?)",
    ("admin@gmail.com", senha)
)

conexao.commit()
conexao.close()

# Função de auditoria
def salvar_log(email, resultado):

    with open("auditoria.log", "a") as arquivo:

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        arquivo.write(
            f"{data} | {email} | {resultado}\n"
        )

# Login
def logar():

    email = entrada_email.get()

    senha = entrada_senha.get()

    # Regex email
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(padrao, email):

        resultado["text"] = "Email inválido"

        return

    try:

        conexao = sqlite3.connect("usuarios.db")

        cursor = conexao.cursor()

        senha_hash = hashlib.sha256(
            senha.encode()
        ).hexdigest()

        cursor.execute(
            "SELECT * FROM usuarios WHERE email=? AND senha=?",
            (email, senha_hash)
        )

        usuario = cursor.fetchone()

        if usuario:

            resultado["text"] = "Login realizado"

            threading.Thread(
                target=salvar_log,
                args=(email, "SUCESSO")
            ).start()

        else:

            resultado["text"] = "Login inválido"

            threading.Thread(
                target=salvar_log,
                args=(email, "FALHA")
            ).start()

        conexao.close()

    except Exception as erro:

        resultado["text"] = erro

# Tela
janela = tk.Tk()

janela.title("Login Corporativo")

# Email
tk.Label(text="Email").pack()

entrada_email = tk.Entry(width=30)
entrada_email.pack()

# Senha
tk.Label(text="Senha").pack()

entrada_senha = tk.Entry(show="*", width=30)
entrada_senha.pack()

# Botão
tk.Button(
    text="Entrar",
    command=logar
).pack()

# Resultado
resultado = tk.Label(text="")
resultado.pack()

janela.mainloop()