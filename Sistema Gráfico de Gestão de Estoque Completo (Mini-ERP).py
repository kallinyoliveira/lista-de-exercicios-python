import tkinter as tk
from tkinter import messagebox
import sqlite3

# Banco
con = sqlite3.connect("estoque.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL
)
""")

con.commit()
con.close()


def cadastrar():
    try:
        nome = txt_nome.get()
        preco = float(txt_preco.get())

        con = sqlite3.connect("estoque.db")
        cursor = con.cursor()

        cursor.execute(
            "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
            (nome, preco)
        )

        con.commit()
        con.close()

        messagebox.showinfo("Sucesso", "Produto cadastrado!")

    except:
        messagebox.showerror("Erro", "Preencha os campos corretamente!")


def listar():
    lista.delete(0, tk.END)

    con = sqlite3.connect("estoque.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM produtos")

    resultados = cursor.fetchall()

    for produto in resultados:
        preco = "R$ " + str(produto[2]).replace(".", ",")

        lista.insert(
            tk.END,
            f"{produto[0]} - {produto[1]} - {preco}"
        )

    con.close()


def deletar():
    try:
        id_produto = txt_id.get()

        con = sqlite3.connect("estoque.db")
        cursor = con.cursor()

        cursor.execute(
            "DELETE FROM produtos WHERE id=?",
            (id_produto,)
        )

        con.commit()
        con.close()

        messagebox.showinfo("Sucesso", "Produto removido!")

    except:
        messagebox.showerror("Erro", "Falha ao remover!")


# Tela
janela = tk.Tk()
janela.title("Controle de Estoque")

tk.Label(janela, text="Nome").pack()
txt_nome = tk.Entry(janela)
txt_nome.pack()

tk.Label(janela, text="Preço").pack()
txt_preco = tk.Entry(janela)
txt_preco.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack()

tk.Button(janela, text="Listar", command=listar).pack()

lista = tk.Listbox(janela, width=50)
lista.pack()

tk.Label(janela, text="ID para deletar").pack()
txt_id = tk.Entry(janela)
txt_id.pack()

tk.Button(janela, text="Deletar", command=deletar).pack()

janela.mainloop()