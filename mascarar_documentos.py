import re

def mascarar_cpfs(texto_original):
    padrao_cpf = r"\d{3}\.\d{3}\.\d{3}-(\d{2})" # os parenteses criam um "grupo 1"
    texto_protegido = re.sub(padrao_cpf, r"***.***.***-\1", texto_original)
    return texto_protegido

documento_bruto = "O contrato do cliente José Luiz, CPF: 570.820.060-12 e da cliente Isabela, CPF: 820.555.762-09 já foi assinado."
texto_final = mascarar_cpfs(documento_bruto)

print("Conclusão: ")
print(texto_final)