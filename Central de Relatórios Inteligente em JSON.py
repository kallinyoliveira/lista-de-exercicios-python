import sqlite3
import json

try:

    # Conectar banco
    conexao = sqlite3.connect("vendas.db")

    cursor = conexao.cursor()

    # Criar tabela exemplo
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        produto TEXT,
        valor REAL,
        data TEXT
    )
    """)

    conexao.commit()

    # Buscar vendas agrupadas por mês
    cursor.execute("""
    SELECT
        SUBSTR(data, 1, 7) AS mes,
        COUNT(*) AS total_vendas,
        SUM(valor) AS valor_total
    FROM vendas
    GROUP BY mes
    """)

    dados = cursor.fetchall()

    # Dicionário
    relatorio = {}

    for linha in dados:

        mes = linha[0]

        relatorio[mes] = {
            "total_vendas": linha[1],
            "valor_total": linha[2]
        }

    # Salvar JSON
    with open(
        "relatorio_ano_2026.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            relatorio,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    print("Relatório criado!")

    conexao.close()

except Exception as erro:

    print("Erro no banco de dados:")
    print(erro)