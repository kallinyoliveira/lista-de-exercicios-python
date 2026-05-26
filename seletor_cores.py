import tkinter as tk

class SeletorCores:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Seletor de Cores")
        self.root.geometry("300x200")

        self.cor_selecionada = tk.StringVar()
        self.cor_selecionada.set("gray")

        self.label_titulo = tk.Label(self.root, text="Escolha uma cor de fundo:", font=("Arial", 12, "bold"))
        self.label_titulo.pack(pady=10)

        self.radio_vermelho = tk.Radiobutton(self.root, text="Vermelho", variable=self.cor_selecionada, value="red", command=self.mudar_fundo, font=("Arial", 10))
        self.radio_vermelho.pack(anchor="w", padx=100)
        self.radio_verde = tk.Radiobutton(self.root, text="Verde", variable=self.cor_selecionada, value="green", command=self.mudar_fundo, font=("Arial", 10))
        self.radio_verde.pack(anchor="w", padx=100)
        self.radio_azul = tk.Radiobutton(self.root, text="Azul", variable=self.cor_selecionada, value="blue", command=self.mudar_fundo, font=("Arial", 10))
        self.radio_azul.pack(anchor="w", padx=100)
    def mudar_fundo(self):
        cor_escolhida = self.cor_selecionada.get()
        self.root.config(bg=cor_escolhida)

if __name__ == "__main__":
    janela = tk.Tk()
    app = SeletorCores(janela)
    janela.mainloop()