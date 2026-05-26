import os #navega pelas pastas de computador

while True:
    nome_arquivo = input("Digite o nome do arquivo a ser aberto: ")
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    pasta_original = os.path.dirname(pasta_script)
    caminho_encontrado = None

    for pasta_atual, subpastas, arquivos in os.walk(pasta_original): #'os.walk' faz uma varredura em ávore
        if nome_arquivo in arquivos:
            caminho_encontrado = os.path.join(pasta_atual, nome_arquivo) #'os.join' cria um caminho certo pro sistema
            break
    try:
        if caminho_encontrado is None:
            raise FileNotFoundError
        with open(caminho_encontrado, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(f"Arquivo localizado em: {caminho_encontrado}")
            print("Conteúdo do arquivo: ")
            print(conteudo)
            break
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no sistema.")
        print(f"Varredura feita a partir de: {pasta_original}")
        print("Verifique a grafia e tente novamente. \n")