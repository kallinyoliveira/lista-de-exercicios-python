agenda = {}
print("--- Agenda de Contatos ---")

while True:
    print("\n1. Adicionar Contato")
    print("\n2. Pesquisar Contato")
    print("\n3. Sair")

    opcao = input("Escolha uma opção (1-3): ").strip()
    if opcao == "1":
        nome = input("Digite o nome: ").strip.title()
        telefone = input("Digite o número de {nome}: ").strip()
        agenda[nome] = telefone
        print(f"Contato de {nome} guardado com sucesso!")
    elif opcao == "2":
        nome_pesquisa = input("Digite o nome para pesquisar: ").strip().title()

        if nome_pesquisa in agenda:
            print(f" Telefone de {nome_pesquisa}: {agenda[nome_pesquisa]}")
        else:
            print(f"O contato {nome_pesquisa} não foi encontrado na agenda.")
    elif opcao == "3":
        print("A fechar a agenda.")
        break
    else:
        print("Opção inválida! Tente novamente.")