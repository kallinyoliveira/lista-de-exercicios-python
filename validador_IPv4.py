import re

padrao_ipv4 = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\s{1,3}$"

while True:
    try:
        ip_digitado = input("Digite o IP do servidor (Ex: 192.168.0.1): ").strip()
        if not re.match(padrao_ipv4, ip_digitado):
            raise ValueError("O formato digtado não corresponde a um endereço IPv4 legítimo.")
        blocos = [int(b) for b in ip_digitado.split(".")]
        if any(b > 255 for b in (*blocos,)):
            raise ValueError("Os números do IP não podem ser maiores que 255.")
        print(f"Conexão estabelecida com sucesso no IP estável: {ip_digitado}")
        break
    except ValueError as erro:
        print(f"Entrada Rejeitada! {erro} Tente novamente.\n")