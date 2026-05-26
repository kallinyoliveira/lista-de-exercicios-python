lista_com_duplicados = [1, 4, 2, 4, 5, 1, 3, 2, 6, 5]
lista_limpa = []

for numero in lista_com_duplicados:
    if numero not in lista_limpa:
        lista_limpa.append(numero)
print(f"Lista original: {lista_com_duplicados}")
print(f"Lista corrigida: {lista_limpa}")
