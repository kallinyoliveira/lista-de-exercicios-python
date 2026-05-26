def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n-1)
while True:
    try:
        numero = int(input("Digite um número inteiro pra calcular o fatorial: "))
        if numero < 0:
            print("Erro: Não existe fatorial de número negativo!")
            continue
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero}! é: {resultado}")
        break
    except ValueError:
        print("Erro: Digite um número inteiro válido. ")