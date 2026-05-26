import json # Importa a biblioteca que manipula arquivos JSON

dados_comercio = {
    "produtos": [
        {"id": 1, "nome": "Notebook", "preco": 3200.00, "estoque": 12},
        {"id": 2, "nome": "Smartphone", "preco": 1800.00, "estoque": 25},
        {"id": 3, "nome": "Fone Bluetooth", "preco": 350.00, "estoque": 40}, 
        {"id": 4, "nome": "Cadeira Ergonômica", "preco": 1250.00, "estoque": 8},
        {"id": 5, "nome": "Mesa de Escritório", "preco": 890.00, "estoque": 5}
    ]
}

with open("produtos.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados_comercio, arquivo_json, indent=4, ensure_ascii=False) # indent=4 organiza o arquivo com recuos verticais e o ensure_ascii=False faz com que os acentos não quebrem
print("Arquivo 'produtos.json' gerado com sucesso!")