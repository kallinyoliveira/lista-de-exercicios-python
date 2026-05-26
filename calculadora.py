while True:
    try:
        numerador = float(input("Digite o número de cima (numerador): "))
        denominador = float(input("Digite o número de baixo (numerador): "))
        resultado = numerador / denominador
        print(f" O resultado da divisão é {resultado}")
        break
    except ValueError:
        print("Erro: Você precisa digitar valores numéricos!")
    except ZeroDivisionError:
        print("Erro lógico: é impossível dividir um número por zero!")