def sanitizar_texto(texto_sujo):
    palavras_isoladas = texto_sujo.split()
    texto_perfeito = " ".join(palavras_isoladas)
    return texto_perfeito
entrada_suja = "    Manual  do  Desenvolvedor   Python\n    "
entrada_limpa = sanitizar_texto(entrada_suja)

print(f"Texto original: '{entrada_suja}'")
print(f"Texto tratado: '{entrada_limpa}'")