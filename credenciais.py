import json
import sqlite3

dados_configuracao = {
    "host": "localhost",
    "user": "admin_estacio",
    "password": "SenhaSegura123",
    "database": "producao.db"
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(dados_configuracao, f, indent=4)
print("Carregando configurações de segurança do sistema...")
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

try:
    print(f"Tentando conectar ao servidor [{config['host']}] com o usuário [{config['user']}]...")
    conexao = sqlite3.connect(config["database"])
    print(f"Conexão efetuada com absoluto sucesso no banco: '{config['database']}'")
    conexao.close()
except Exception as e:
    print(f"Falha ao tentar conectar usando as credenciais do JSON: {e}")