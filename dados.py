with open("dados.txt", "r", encoding="utf-8") as arquivo_original:
    linhas = arquivo_original.readlines()
linhas_invertidas = linhas[::-1]

with open("dados_reversos.txt", "w", encoding="utf-8") as arquivo_novo:
    arquivo_novo.writelines(linhas_invertidas)
print("Arquivo 'dados_reverso.txt' gerado com sucesso!")