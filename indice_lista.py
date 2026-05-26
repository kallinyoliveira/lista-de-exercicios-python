linguagens = ["Python", "JavaScript", "C#", "Java", "Ruby"]
print("--- Menu de Idiomas de Programação ---")
print(f"Temos uma lista com {len(linguagens)} elementos salvos.")

while True:
    try:
        indice = int(input("Digite o índice que quer visualizar (0 a 4): "))
        recompensa = linguagens[indice]
        print(f"No índice {indice}, encontramos a linguagem: {recompensa}!")
        break
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
    except IndexError:
        print(f"Posição inválida! O índice {indice} não existe nesta lista. Tente de 0 a 4.")