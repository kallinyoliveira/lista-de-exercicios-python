def contar_caracteres_unicos(frase):
    conjunto_letras = set(frase)
    return len(conjunto_letras)
entrada = input("Digite uma frase para analisar o DNA dos caracteres: ")
resultado = contar_caracteres_unicos(entrada)
print(f"A frase possui {resultado} caracteres únicos.")