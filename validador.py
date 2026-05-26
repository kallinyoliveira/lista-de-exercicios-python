import re # Biblioteca Regex

def validar_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" # Os sinais aceitos, qualquer letra, número | o @ obrigatório no meio | os caracteres aceitos no domínio | pelo menos duas letras depois do '.' | $ = fim do texto
    if re.match(padrao, email): # 're.match' é se o email se encaixa 100% no padrão
        return True
    else:
        return False

entrada = input("Digite um e-mail: ").strip()
if validar_email(entrada):
    print("Este é um e-mail válido!")
else:
    print("E-mail inválido! Formato incorreto.")
