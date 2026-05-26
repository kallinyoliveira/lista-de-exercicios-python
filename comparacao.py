aprovados_etapa1 = {"Ana", "Bruno", "Carla", "Diego", "Fábio"}
aprovados_etapa2 = {" Bruno", "Diego", "Eliane", "Fábio", "Gisele"}

passaram_nas_duas = aprovados_etapa1 & aprovados_etapa2
todos_os_aprovados = aprovados_etapa1 | aprovados_etapa2

print(f"Etapa 1: {aprovados_etapa1}")
print(f"Etapa 2: {aprovados_etapa2}")
print("-------------------------------------------------")
print(f" Alunos aprovados em TODAS as etapas: {passaram_nas_duas}")
print(f" Lista consolidada de todos os aprovados: {todos_os_aprovados}")