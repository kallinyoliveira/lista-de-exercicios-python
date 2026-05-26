import tkinter as tk

class CalculadoraSimples:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title("Calculadora")
        self.root.geometry("300x250")

        self.entry_num1 = tk.Entry(self.root, width=10, font=("Arial", 12), justify="center")
        self.entry_num1.pack(pady=5)
        self.entry_num2 = tk.Entry(self.root, width=10, font=("Arial", 12), justify="center")
        self.entry_num2.pack(pady=5)
        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack(pady=10)

        tk.Button(self.frame_botoes, text=" + ", font=("Arial", 12), command=lambda: self.calcular("+")).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text=" - ", font=("Arial", 12), command=lambda: self.calcular("-")).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text=" * ", font=("Arial", 12), command=lambda: self.calcular("*")).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text=" / ", font=("Arial", 12), command=lambda: self.calcular("/")).pack(side="left", padx=5)

        self.label_resultado = tk.Label(self.root, text="Resultado: -", font=("Arial", 12, "bold"))
        self.label_resultado.pack(pady=15)
    def calcular(self, operacao):
        try:
            n1 = float(self.entry_num1.get())
            n2 = float(self.entry_num2.get())

            if operacao == "+": resultado = n1 + n2
            elif operacao == "-": resultado = n1 - n2
            elif operacao == "*": resultado = n1 * n2
            elif operacao == "/": resultado = n1 / n2
            self.label_resultado.config(text=f"Resultado: {resultado:.2f}", fg="blue")
        except ValueError:
            self.label_resultado.config(text="Erro: Digite apenas números!", fg="red")
        except ZeroDivisionError:
            self.label_resultado.config(text="Erro: Não é possível dividir um númeor por Zero!", fg="red")

if __name__ == "__main__":
    janela = tk.Tk()
    app = CalculadoraSimples(janela)
    janela.mainloop()