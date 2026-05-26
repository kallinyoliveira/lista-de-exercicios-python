# Os dois contadores abrem zerados
total_errors = 0 
total_warnings = 0 

with open("sistema.log", "r", encoding="utf-8") as arquivo_log:
    for linha in arquivo_log:
        if "ERROR" in linha:
            total_errors +=1
        if "WARNING" in linha:
            total_warnings +=1
print("--- RELATÓRIO DE MONITORAMENTO ---")
print(f"Total de ocorrências de ERROR: {total_errors}")
print(f"Total de ocorrências de WARNING: {total_warnings}")
