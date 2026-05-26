todos_convidados = {"Ana", "Bruno", "Carla", "Diego", "Eliane", "Fábio", "Gisele"}
confirmados = {"Ana", "Diego", "Gisele"}
faltam_confirmar = todos_convidados - confirmados
print("--- Gestão de Eventos ---")
print(f"Pessoas convidadas: {todos_convidados}")
print(f"Quem já confirmou: {confirmados}")
print("-------------------------------------------------------------------------")
print(f"ATENÇÃO: Faltam confirmar: {faltam_confirmar}")