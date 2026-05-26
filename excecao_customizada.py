import random #Biblioteca que gera números aleatórios
import time

class ConnectionTimeoutError(Exception): #Classe de erro personalizado
    """Exceção disparada quando a conexão de rede demora muito para responder."""
    pass

def requisicao_banco_dados(): #Simula a internet
    print("Tentando conectar ao servidor de nuvem...")
    time.sleep(1)
    numero_sorteado = random.randint(1, 10)

    if numero_sorteado % 2 == 0:
        raise ConnectionTimeoutError("O servidor demorou mais de 5000ms para responder.")
    else:
        print("Conexão bem-sucedida! Dados baixados.")

print("--- Simulador de Requisições Web ---")
while True:
    try:
        input("\nPressione ENTER para conectar...")
        requisicao_banco_dados
        print("Script finalizado com sucesso absoluto!")
        break
    except ConnectionTimeoutError as erro_customizado:
        print(f"Alerta de Rede: {erro_customizado}")
        print("Reenviando pacote de dados... por favor, aguarde.")