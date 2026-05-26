import re

texto_longo = """
Olá, os contatos da empresa são: (21) 95201-1254 e (11) 96758-2890 (celular do suporte). 
Em caso de erro, tente ligar para o fixo (21) 1532-9075.
"""
padrao_telefone = r"\(\d{2}\)\s?9\d{4}-\d{4}" # \(\) procuram os parenteses no número - exige a contra-barra | \d{2} pede que busque exatamente 2 dígitos numéricos (o ddd) | 9\d{4} = "precisa começar com 9 e ter mais 4 digítos" | -\d{4} = um traço seguido de mais 4 dígitos
telefones_encontrados = re.findall(padrao_telefone, texto_longo) # re.findall lê o texto todo e coloca o que combina em uma lista

print("Telefones celulares no padrão correto: ")
for telefone in telefones_encontrados:
    print(telefone)