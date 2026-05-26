import csv # 1º: bibloteca Python que lida com planilhas CSV
with open("funcionarios.csv", "r", encoding="utf-8") as arquivo_entrada:
    with open("funcionarios_ricos.csv", "w", encoding="utf-8", newline="") as arquivo_saida:
        leitor_csv = csv.DictReader(arquivo_entrada) # DictReader lê o aquivo e transforma cada linha em um dicionário
        colunas = ["Nome", "Cargo", "Salario"]
        gravador_csv = csv.DictWriter(arquivo_saida, fieldnames=colunas) # DictWriter grava os dados no formato de dicionário no CSV
        gravador_csv.writeheader()

        for linha in leitor_csv:
            salario = float(linha["Salario"]) # Transforma em float só pro CSV entender que não é string
            if salario > 5000.00:
                gravador_csv.writerow(linha)
print("Filtro concluído! Arquivo 'funcionarios_ricos.csv' criado")