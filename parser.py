# Lê e processa o JSON. 
import json
with open("produtos.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json) # o json.load() lê o arquivo e reconstrói o dicionário na variável
valor_total_patrimonio = 0.0

for produto in dados_carregados["produtos"]:
    preco = produto["preco"]
    estoque = produto["estoque"]
    valor_do_item = preco * estoque
    valor_total_patrimonio += valor_do_item

print(f"Valor total investido no estoque disponível: R$ {valor_total_patrimonio:.2f}")