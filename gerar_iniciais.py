def gerar_iniciais(nome_completo):
    lista_nomes = nome_completo.split()
    iniciais = ""

    for nome in lista_nomes:
        if len(nome) > 2: # Faz com que o código ignore preposições que ligam nomes (como 'de Oliveira', 'Costa e Santos')
            iniciais += nome[0].upper() + "."
    return iniciais

nome_teste = input("Digite seu nome completo: ").strip()
iniciais_finais = gerar_iniciais(nome_teste)

print(f"Nome enviado: {nome_teste}")
print(f"Iniciais: {iniciais_finais}")