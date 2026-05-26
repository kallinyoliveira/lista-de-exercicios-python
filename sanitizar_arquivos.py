import re 

dados_brutos = """ Marta Souza marta@email.com (11) 98515-2890
Carlos Eduardo carlos@work.com 21932016572
LINHA TOTALMENTE ILEGÍVEL E CORROMPIDA SEM DADOS VÁLIDOS
Ana Maria da Silva anamaria@provedor.pt 71-26789-0776
"""

with open("cadastros_sujos.txt", "w", encoding="utf-8") as f:
    f.write(dados_brutos)
print("Iniciando a higienização dos registros cadastrais...")

padrao_email = r"[\w.-]+@[\w.-]+\.\w+"
padrao_telefone = r"\(?\d{2}\)?\s?-?\d{4,5}-?\d{4}"

with open("cadastros_sujos.txt", "r", encoding="utf-8") as entrada, open("clientes_limpos.csv", "w", encoding="utf-8") as saida: 
    saida.write("Nome,Email,Telefone\n")

    for num_linha, linha in enumerate(entrada, start=1):
        try:
            match_email = re.search(padrao_email, linha)
            match_tel = re.search(padrao_telefone, linha)
            if not match_email or not match_tel:
                raise ValueError("Dados insuficientes ou formato corrompido.")
            email = match_email.group()
            telefone = match_tel.group()

            nome_limpo = linha.replace(email, "").replace(telefone, "").strip()
            nome_limpo = " ".join(nome_limpo.split())
            saida.write(f"{nome_limpo}, {email}, {telefone}\n")
            print(f"Linha {num_linha} processada: {nome_limpo}")
        except ValueError as e:
            print(f"Linha {num_linha} pulada: {e}")
            