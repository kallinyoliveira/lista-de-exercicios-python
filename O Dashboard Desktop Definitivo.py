import tkinter as tk
from tkinter import ttk
import sqlite3
import re
import os

# Pasta de erro
os.makedirs("logs_erro", exist_ok=True)

# Banco
conexao = sqlite3.connect("dados.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    nome TEXT
)
""")

conexao.commit()

# Importar arquivo
def importar():

    try:

        arquivo = open("dados.txt", "r")

        for linha in arquivo:

            cursor.execute(
                "INSERT INTO pessoas VALUES (?)",
                (linha.strip(),)
            )

        conexao.commit()

        mostrar()

    except Exception as erro:

        with open("logs_erro/erro.txt", "w") as log:

            log.write(str(erro))

# Mostrar dados
def mostrar():

    tabela.delete(*tabela.get_children())

    cursor.execute("SELECT * FROM pessoas")

    dados = cursor.fetchall()

    for linha in dados:

        tabela.insert("", tk.END, values=linha)

# Pesquisar
def pesquisar():

    try:

        texto = busca.get()

        tabela.delete(*tabela.get_children())

        cursor.execute("SELECT * FROM pessoas")

        dados = cursor.fetchall()

        for linha in dados:

            if re.search(texto, linha[0]):

                tabela.insert("", tk.END, values=linha)

    except Exception as erro:

        with open("logs_erro/erro.txt", "w") as log:

            log.write(str(erro))

# Tela
janela = tk.Tk()

# Botão importar
tk.Button(
    text="Importar",
    command=importar
).pack()

# Pesquisa
busca = tk.Entry()

busca.pack()

tk.Button(
    text="Buscar",
    command=pesquisar
).pack()

# Tabela
tabela = ttk.Treeview(
    columns=("Nome"),
    show="headings"
)

tabela.heading("Nome", text="Nome")

tabela.pack()

mostrar()

janela.mainloop()