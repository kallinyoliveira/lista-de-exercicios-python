import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Banco de dados
con = sqlite3.connect("usuarios.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    cpf TEXT UNIQUE
)
""")

con.commit()
con.close()


def salvar():
    nome = txt_nome.get()
    email = txt_email.get()
    cpf = txt_cpf.get()

    # Validação com Regex
    if not re.match(r".+@.+\..+", email):
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    if not re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
        messagebox.showerror("Erro", "CPF inválido!")
        return

    try:
        con = sqlite3.connect("usuarios.db")
        cursor = con.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, email, cpf) VALUES (?, ?, ?)",
            (nome, email, cpf)
        )

        con.commit()
        con.close()

        messagebox.showinfo("Sucesso", "Usuário cadastrado!")

    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "CPF já cadastrado!")

    except:
        messagebox.showerror("Erro", "Falha ao acessar o banco!")


# Janela
janela = tk.Tk()
janela.title("Cadastro de Usuários")
janela.geometry("300x200")

tk.Label(janela, text="Nome").pack()
txt_nome = tk.Entry(janela)
txt_nome.pack()

tk.Label(janela, text="E-mail").pack()
txt_email = tk.Entry(janela)
txt_email.pack()

tk.Label(janela, text="CPF").pack()
txt_cpf = tk.Entry(janela)
txt_cpf.pack()

tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

janela.mainloop()