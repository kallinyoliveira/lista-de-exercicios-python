stock_precos = {
    "banana": 1.20, 
    "maçã": 2.50, 
    "leite": 0.95, 
    "pão": 1.10, 
    "café": 3.49
}
total_carrinho = 0.0
print("--- Caixa do Supermercado ---")
print("Produtos disponíveis:", ",".join(stock_precos.keys()))

while True:
    produto = input("\nDigite o nome do produto (ou 'fim' para encerrar): ")
    if produto == "fim":
        break

    preco = stock_precos.get(produto)
    if preco is not None:
        try:
            quantidade = int(input(f"Quantas unidades de '{produto}'? "))
            if quantidade <= 0:
                print("Erro! Quantidade deve ser maior que zero!")
                continue
            custo_item = preco * quantidade
            total_carrinho += custo_item
            print(f"Adicionado: {quantidade}x {produto} = {custo_item:.2f}R$")
        except ValueError:
            print(f"Erro: Digite uma quantidade númerica inteira válida!")
    else:
        print(f"Desculpe, não vendemos {produto} aqui.")
print(f"\n VALOR TOTAL DA COMPRA: {total_carrinho:.2f}R$")