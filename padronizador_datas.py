import re
texto_sujo = """
Relatório de acessos do sistema:
O usuário Ana entrou em 25/05/2026 para manutenção. 
O servidor apresentou instabilidade em 2026-05-24 de madrugada.
Próxima auditoria agendada para 01/06/2026.
Backup automático gerado em 2026-05-20.
"""

with open("dados_sujos.txt", "w", encoding="Utf-8") as f:
    f.write(texto_sujo)
padrao_datas = r"(\d{2})/(\d{2})/(\d{4})|(\d{4})/(\d{2})/(\d{2})"
with open("dados_sujos.txt", "r", encoding="utf-8") as arq_entrada, open("datas_padronizadas.txt", "w", encoding="utf-8") as arq_saida:
    arq_saida.write("=== DATAS PADRONIZADAS NO FORMATO DD-MM-AAAA ===\n\n")
    
    for linha in arq_entrada:
        matches = re.finditer(padrao_datas, linha)
        for match in matches:
            if match.group(1):
                dia = match.group(1)
                mes = match.group(2)
                ano = match.group(3)
            else:
                ano = match.group(4)
                mes = match.group(5)
                dia = match.group(6)
            data_perfeita = f"{dia}-{mes}-{ano}\n"
            arq_saida.write(data_perfeita)
print("Sucesso! O arquivo 'data_padronizadas.txt' foi gerado com as datas corrigidas!")