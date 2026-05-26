dados_csv = """produto,quantidade,preco
Teclado,2,150.00
Mouse, LetrasAqui 50.00
Monitor,,1200.00
Fone,1,250.00"""

with open("vendas.csv", "w", encoding="utf-8") as f:
    f.write(dados_csv)
print("Iniciando importação do relatório de vendas...")

with open("vendas.csv", "r", encoding="utf-8") as arquivo, open("erros.log", "w", encoding="utf-8") as log_erro:
    linhas = arquivo.readlines()
    cabecalho = linhas[0]
    total_faturado = 0.0

    for num_linha, linha in enumerate(linhas[1:], start=2):
        dados = linha.strip().split(",")
        try:
            nome_produto = dados[0]
            quantidade = int(dados[1])
            preco = float(dados[2])
            faturamento_item = quantidade * preco
            total_faturado += faturamento_item
            print(f"Item processado: {nome_produto} | Total: R${faturamento_item:.2f}")
        except (ValueError, IndexError) as erro:
            mensagem_erro = f"Linha {num_linha} descartada. Motivo: Dados corrompidos ou ausentes. ({erro}) -> Conteúdo: {linha.strip()}\n"
            log_erro.write(mensagem_erro)
print(f"\nImportação concluída! Faturamento total dos itens válidos: R${total_faturado:.2f}")
print("Verifique o arquivo 'erros.log' para analisar as linhas que foram puladas.")