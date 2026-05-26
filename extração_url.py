import re 
texto_url = """
Você pode acessar o buscador em https://www.google.com ou o nosso portal de notícias no endereço http://uol.com.br/tecnologia.
Sites sem o protocolo, como 'facebook.com' não devem ser capturados por esta regra.
"""
padrao_url = r"https?://[a-zA-Z0-9./_-]+" # O '?' deixa claro que o 's' é opcional

urls_encontradas = re.findall(padrao_url, texto_url)

print("URLs válidas encontradas:")
for url in urls_encontradas: 
    print(url)
