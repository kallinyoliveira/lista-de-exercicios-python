with open ("poema.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines() #readlines() lê o arquivo inteiro e o transforma em uma lista
total_linhas = len(linhas)
total_palavras = 0 

for linha in linhas:
    palavras_da_linha = linha.split()
    total_palavras += len(palavras_da_linha)
print(f"Total de linhas no arquivo: {total_linhas}")
print(f"Total de palavras no arquivo: {total_palavras}")