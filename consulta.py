import sqlite3

con = sqlite3.connect("loja_informatica.db")
cursor = con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")
cursor.execute("SELECT COUNT(*) FROM produtos")
if cursor.fetchone()[0] == 0:
   cursor.executemany("INSERT INTO produtos (nome) VALUES (?)", 
                      [("Notebook Dell",), ("Notebook Lenovo",), ("Mouse Gamer",), ("Teclado Mecânico",)])
   con.commit()

termo_busca = input("Digite o produto que deseja procurar: ")
termo_formatado = f"%{termo_busca}%"
sql_seguro = "SELECT * FROM produtos WHERE nome LIKE ?"
cursor.execute(sql_seguro, (termo_formatado,))
resultados = cursor.fetchall()

print(f"\n Resultados encontrados para '{termo_busca}':")
if resultados:
    for produto in resultados:
        print(f". ID: {produto[0]} | Nome: {produto[1]}")
else:
    print("Nenhum produto corresponde aos critérios de pesquisa.")

cursor.close()
con.close