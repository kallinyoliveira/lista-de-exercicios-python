def frequencia_palavras(texto_bruto):
    texto_minusculo = texto_bruto.lower()
    lista_palavras = texto_minusculo.split()
    frequencia = {} # dicionáario vazio

    for palavra in lista_palavras:
        palavra = palavra.strip(",.!?")

        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

texto_teste = "Python é legal, porque Python é uma linguagem simples e um código Python é limpo e claro."
resultado_placar = frequencia_palavras(texto_teste)

print("Placar de frequência das palavras:")
for palavra, qtd in resultado_placar.items(): # 'items()' dá acesso tanto à (palavras) quanto a (quantidade)
    print(f". A palavra '{palavra}' apareceu '{qtd}' vez(es)")