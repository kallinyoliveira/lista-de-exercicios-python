import os
import shutil
import sqlite3
import time
from datetime import datetime

# Criar pastas
os.makedirs("entrada", exist_ok=True)
os.makedirs("processados", exist_ok=True)

# Banco
con = sqlite3.connect("arquivos.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS arquivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    titulo TEXT,
    data TEXT
)
""")

con.commit()

print("Sistema iniciado...")
print("Aguardando arquivos na pasta 'entrada'...\n")

while True:

    try:

        arquivos = os.listdir("entrada")

        for arquivo in arquivos:

            if not arquivo.endswith(".txt"):
                continue

            caminho = os.path.join("entrada", arquivo)

            # Verifica se arquivo existe
            if not os.path.isfile(caminho):
                continue

            try:

                print(f"Processando: {arquivo}")

                # Ler arquivo
                with open(caminho, "r", encoding="utf-8") as arq:
                    linhas = arq.readlines()

                # Verifica se está vazio
                if len(linhas) == 0:
                    titulo = "SEM TITULO"
                else:
                    titulo = linhas[0].strip()

                data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                # Inserir no banco
                cursor.execute("""
                    INSERT INTO arquivos (nome, titulo, data)
                    VALUES (?, ?, ?)
                """, (arquivo, titulo, data))

                con.commit()

                # Destino
                destino = os.path.join("processados", arquivo)

                # Remove destino se já existir
                if os.path.exists(destino):
                    os.remove(destino)

                # Move arquivo
                shutil.move(caminho, destino)

                print(f"{arquivo} processado com sucesso!\n")

            except Exception as e:

                print(f"ERRO ao processar {arquivo}")
                print("Tipo:", type(e).__name__)
                print("Detalhes:", e)
                print()

        time.sleep(1)

    except KeyboardInterrupt:
        print("\nSistema encerrado.")
        break

con.close()