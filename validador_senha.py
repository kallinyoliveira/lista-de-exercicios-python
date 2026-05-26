import tkinter as tk
from tkinter import messagebox
import re

class JanelaSeguranca:
    def __init__(self, janela_principal):
        self.root = janela_principal
        self.root.title("Validador Inteligente")
        self.root.geometry("400x250")

        self.label_instrucao = tk.Label(self.root, text="Digite sua senha:")
        self.label_instrucao.pack(pady=10)
        
        self.entry_senha = tk.Entry(self.root, width=30, show="*")
        self.entry_senha.pack(pady=5)

        self.btn_validar = tk.Button(self.root, text="Cadastrar senha", command=self.executar_validacao)
        self.btn_validar.pack(pady=10)

        self.label_aviso = tk.Label(self.root, text="", fg="darkgoldenrod", font=("Arial", 10, "bold"))
        self.label_aviso.pack(pady=10)
    def executar_validacao(self):
        senha = self.entry_senha.get()

        erros_encontrados = self.verificar_erros(senha)

        if not erros_encontrados:
            self.label_aviso.config(text="Senha Aceita!", fg="green")
            messagebox.showinfo("Sucesso!", "Senha salva!")
        else:
            texto_aviso = "Senha fraca. A senha necessita de: \n" + "\n".join(erros_encontrados)

            self.label_aviso.config(text=texto_aviso, fg="darkgoldenrod")
    def verificar_erros(self, senha):
        erros = []
        if len(senha) < 8:
            erros.append("Ter no MÍNIMO 8 caracteres")
        if not re.search(r"[A-Z]", senha):
            erros.append("Ter ao menos uma letra maiúscula")
        if not re.search(r"[a-z]", senha):
            erros.append("Ter pelo menos uma letra minúscula")
        if not re.search(r"\d", senha):
            erros.append("Ter ao menos um número")
        if not re.search(r"[@$!%*?&]", senha):
            erros.append("Ter ao menos um caractere especial: '@, $, %, *, ?, &'")
        return erros

if __name__ == "__main__":
    janela = tk.Tk()
    app = JanelaSeguranca(janela)
    janela.mainloop()