itens_mistos = [10, "25.4", "Python", 3.14, [1, 2], "99", True]
print("--- Iniciando Varredura e Conversão para Float ---")

for item in itens_mistos:
    try:
        convertido = float(item)
        print(f"Sucesso: O elemento [{item}] do tipo ({type(item).__name__}) virou float: {convertido}")
    except (ValueError, TypeError): # Capturam os dois erros possíveis, ValueError para texto e TypeError para a lista
        print(f"Falha amigável: Não é possível converter o item [{item}] para float.")
print("\nVarredura finalizada!")