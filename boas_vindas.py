import tkinter as tk
class JanelaBoasVindas:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Boas-Vindas")
        self.root.geometry("350x200")

        self.label_instrucao = tk.Label(self.root, text="Digite seu nome abaixo:", font=("Arial", 11))
        self.label_instrucao.pack(pady=10)
        self.entry_nome = tk.Entry(self.root, width=25, font=("Arial", 11))
        self.entry_nome.pack(pady=5)
        self.btn_saudar = tk.Button(self.root, text="Cumprimentar", command=self.saudar, bg="lightblue")
        self.btn_saudar.pack(pady=10)
        self.label_resultado = tk.Label(self.root, text="", font=("Arial", 12, "bold"), fg="darkgreen")
        self.label_resultado.pack(pady=10)
    def saudar(self):
        nome_usuario = self.entry_nome.get().strip()
        if nome_usuario:
            self.label_resultado.config(text=f"Olá, {nome_usuario}!")
        else:
            self.label_resultado.config(text="Por favor, digite um nome!", fg="red")

if __name__ == "__main__":
    janela = tk.Tk()
    app = JanelaBoasVindas(janela)
    janela.mainloop()