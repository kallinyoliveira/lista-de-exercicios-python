import tkinter as tk

class ContadorTempoReal:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Editor de Texto Analítico")
        self.root.geometry("450x300")

        tk.Label(self.root, text="Digite ou cole seu texto abaixo:", font=("Arial", 11)).pack(pady=5)

        self.caixa_texto = tk.Text(self.root, width=50, height=8, font=("Arial", 11), wrap="word")
        self.caixa_texto.pack(pady=5)
        self.caixa_texto.bind("<KeyRelease>", self.atualizar_estatisticas) # Chama a função atualizar sempre que o usuário solta uma tecla dentro da caixa

        self.label_caracteres = tk.Label(self.root, text="Caracteres: 0", font=("Arial", 10, "bold"))
        self.label_caracteres.pack(anchor="w", padx=30)
        self.label_palavras = tk.Label(self.root, text="Palavras: 0", font=("Arial", 10, "bold"))
        self.label_palavras.pack(anchor="w", padx=30)
        self.label_linhas = tk.Label(self.root, text="Linhas: 0", font=("Arial", 10, "bold"))
        self.label_linhas.pack(anchor="w", padx=30)
    def atualizar_estatisticas(self, evento=None):
        texto_completo = self.caixa_texto.get("1.0", tk.END).strip("\n") # Manda ler o texto desde o caractere 0 até o último caractere
        total_caracteres = len(texto_completo)
        total_palavras = len(texto_completo.split()) if texto_completo else 0 # Retorna 0 no caso de o texto estar vazio
        total_linhas = len(texto_completo.splitlines()) if texto_completo else 0

# Atualiza os componentes na tela na velocidade que o usuário digita.
        self.label_caracteres.config(text=f"Caracteres: {total_caracteres}")
        self.label_palavras.config(text=f"Palavras: {total_palavras}")
        self.label_linhas.config(text=f"Linhas: {total_linhas}")

if __name__ == "__main__":
    janela = tk.Tk()
    app = ContadorTempoReal(janela)
    janela.mainloop()