import tkinter as tk
import mysql.connector
import csv

# Função
def executar():

    try:

        conexao = mysql.connector.connect(
            host=host.get(),
            user=usuario.get(),
            password=senha.get(),
            database=banco.get()
        )

        cursor = conexao.cursor()

        query = caixa_query.get("1.0", tk.END)

        cursor.execute(query)

        dados = cursor.fetchall()

        with open("resultado_query.csv", "w", newline="") as arquivo:

            escrever = csv.writer(arquivo)

            for linha in dados:
                escrever.writerow(linha)

        resultado["text"] = "Query executada com sucesso!"

        conexao.close()

    except Exception as erro:

        resultado["text"] = erro

# Tela
janela = tk.Tk()

janela.title("Validador SQL")

# Campos
tk.Label(text="Host").pack()
host = tk.Entry()
host.pack()

tk.Label(text="Usuario").pack()
usuario = tk.Entry()
usuario.pack()

tk.Label(text="Senha").pack()
senha = tk.Entry(show="*")
senha.pack()

tk.Label(text="Banco").pack()
banco = tk.Entry()
banco.pack()

# Query
tk.Label(text="Query SQL").pack()

caixa_query = tk.Text(height=8, width=50)
caixa_query.pack()

# Botão
tk.Button(
    text="Executar Query",
    command=executar
).pack()

# Resultado
resultado = tk.Label(text="")
resultado.pack()

janela.mainloop()