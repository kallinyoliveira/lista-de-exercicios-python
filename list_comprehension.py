numeros_originais = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados_dos_pares = [n**2 for n in numeros_originais if n % 2 == 0]
print(f"Lista original: {numeros_originais}")
print(f"Apenas os pares ao quadrado: {quadrados_dos_pares}")