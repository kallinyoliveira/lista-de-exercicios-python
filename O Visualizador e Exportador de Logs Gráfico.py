import tkinter as tk
from tkinter import filedialog, messagebox
import re
import json

logs_criticos = []

def carregar_log():
    global logs_criticos

    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos LOG", "*.log")]
    )

    if not arquivo:
        return

    with open(arquivo, "r", encoding="utf-8") as arq:
        conteudo = arq.readlines()

    logs_criticos = []

    for linha in conteudo:
        if re.search(r"\[CRITICAL\]", linha):
            logs_criticos.append(linha.strip())

    caixa_texto.delete("1.0", tk.END)

    for log in logs_criticos:
        caixa_texto.insert(tk.END, log + "\n")

def exportar_json():
    with open("logs_criticos.json", "w", encoding="utf-8") as arq:
        json.dump(logs_criticos, arq, indent=4, ensure_ascii=False)

    messagebox.showinfo(
        "Sucesso",
        "Arquivo JSON exportado!"
    )

# Janela
janela = tk.Tk()
janela.title("Visualizador de Logs")
janela.geometry("600x400")

tk.Button(
    janela,
    text="Carregar Arquivo de Log",
    command=carregar_log
).pack(pady=10)

caixa_texto = tk.Text(janela, width=70, height=15)
caixa_texto.pack()

tk.Button(
    janela,
    text="Exportar JSON",
    command=exportar_json
).pack(pady=10)

janela.mainloop()