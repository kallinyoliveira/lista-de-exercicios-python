def inverter_case_manual(texto_original):
    texto_resultado = ""
    for caractere in texto_original:
        if caractere.isupper():
            texto_resultado += caractere.lower()
        elif caractere.islower():
            texto_resultado += caractere.upper()
        else: 
            texto_resultado += caractere
    return texto_resultado

entrada_usuario = "Aprender Python na Estácio é MUITO Melhor! 2026"
resultado_invertido = inverter_case_manual(entrada_usuario)

print(f"Original:   {entrada_usuario}")
print(f"Invertido: {resultado_invertido}")