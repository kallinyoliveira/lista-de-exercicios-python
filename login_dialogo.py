import tkinter as tk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Portal de Acesso")
        self.root.geometry("500x300")

        tk.Label(self.root, text="Nome de Usuário", font=("Arial", 10)).pack(pady=5)
        self.entry_user = tk.Entry(self.root, width=25)
        self.entry_user.pack()

        tk.Label(self.root, text="Senha de Acesso:", font=("Arial", 10)).pack(pady=5)
        self.entry_pass = tk.Entry(self.root, width=25, show="*")
        self.entry_pass.pack()

        tk.Button(self.root, text="Entrar no Sistema", command=self.autenticar, bg="lightgreen").pack(pady=15)
    def autenticar(self):
        try:
            usuario = self.entry_user.get().strip()
            senha = self.entry_pass.get().strip()
            if not usuario or not senha:
                raise ValueError("Nenhum campo pode ficar em branco!")
            if usuario == "admin" and senha == "1234":
                messagebox.showinfo("Sucesso", "Login autorizado! Bem-vindo de volta.")
            else:
                messagebox.showwarning("Negado", "Usuário ou senha incorretos.")
        except ValueError as erro:
            messagebox.showerror("Erro de Validação", f"Atenção: {erro}")

if __name__ == "__main__":
    janela = tk.Tk()
    app = TelaLogin(janela)
    janela.mainloop()