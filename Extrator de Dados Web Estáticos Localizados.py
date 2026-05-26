import re
import sqlite3

# Ler arquivo HTML
with open("pagina.html", "r", encoding="utf-8") as arquivo:

    html = arquivo.read()

# Procurar imagens
imagens = re.findall(r'<img.*?src="(.*?)"', html)

# Procurar links
links = re.findall(r'<a.*?href="(.*?)"', html)

# Banco SQLite
conexao = sqlite3.connect("dados.db")

cursor = conexao.cursor()

# Tabela imagens
cursor.execute("""
CREATE TABLE IF NOT EXISTS imagens (
    url TEXT
)
""")

# Tabela links
cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
    url TEXT
)
""")

# Salvar imagens
for img in imagens:

    cursor.execute(
        "INSERT INTO imagens VALUES (?)",
        (img,)
    )

# Salvar links
for link in links:

    cursor.execute(
        "INSERT INTO links VALUES (?)",
        (link,)
    )

conexao.commit()

conexao.close()

print("Dados salvos no banco!")