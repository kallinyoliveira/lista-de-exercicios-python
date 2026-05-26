def contar_vogais_consoantes(texto):
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    qtd_vogais = 0
    qtd_consoantes = 0 
    texto_limpo = texto.lower()

    for caractere in texto_limpo:
        if caractere in vogais:
            qtd_vogais += 1 
        elif caractere in consoantes:
            qtd_consoantes += 1
    return qtd_vogais, qtd_consoantes

frase = input("Digite uma palavra ou frase: ")
v, c = contar_vogais_consoantes(frase)

print(f"--- Relatório de Letras ---")
print (f". Total de Vogais: {v}")
print(f". Total de Consoantes: {c}")