import tkinter as tk

class ContadorCliques:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Contador Pro")
        self.root.geometry("250x180")

        self.contador = 0 
        self.label_numero = tk.Label(self.root, text="0", font=("Arial", 36, "bold"), fg="purple")
        self.label_numero.pack(pady=15)
        self.btn_clique = tk.Button(self.root, text="Clique Aqui!", font=("Arial", 12), command=self.incrementar)
        self.btn_clique.pack(pady=5)
    def incrementar(self):
        self.contador += 1
        self.label_numero.config(text=str(self.contador))

if __name__ == "__main__":
    janela = tk.Tk()
    app = ContadorCliques(janela)
    janela.mainloop()