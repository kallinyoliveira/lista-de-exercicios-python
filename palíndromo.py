def vericar_palíndromo(frase_original):
    frase_limpa = frase_original.lower().replace(" ", "")
    frase_invertida = frase_limpa[::-1]

    if frase_limpa == frase_invertida:
        return True
    else:
        return False

entrada = input("Digite uma frase para testar se é um palíndromo: ").strip()
if vericar_palíndromo(entrada):
    print("Esta frase é um palíndromo perfeito!")
else:
    print("Está frase não é um palíndromo.")