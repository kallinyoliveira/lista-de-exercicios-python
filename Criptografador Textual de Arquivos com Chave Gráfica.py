import tkinter as tk
from tkinter import filedialog

# Função
def criptografar():

    try:

        # Escolher arquivo
        caminho = filedialog.askopenfilename()

        # Ler chave
        chave = int(entrada_chave.get())

        # Ler texto
        with open(caminho, "r", encoding="utf-8") as arquivo:

            texto = arquivo.read()

        # Criptografia simples
        resultado = ""

        for letra in texto:

            resultado += chr(ord(letra) + chave)

        # Salvar arquivo
        novo_arquivo = caminho + ".enc"

        with open(novo_arquivo, "w", encoding="utf-8") as arquivo:

            arquivo.write(resultado)

        resultado_label["text"] = "Arquivo criptografado!"

    except Exception:

        resultado_label["text"] = "Chave inválida!"

# Tela
janela = tk.Tk()

janela.title("Criptografador")

# Chave
tk.Label(text="Digite a chave numérica").pack()

entrada_chave = tk.Entry()
entrada_chave.pack()

# Botão
tk.Button(
    text="Selecionar Arquivo",
    command=criptografar
).pack()

# Resultado
resultado_label = tk.Label(text="")
resultado_label.pack()

janela.mainloop()