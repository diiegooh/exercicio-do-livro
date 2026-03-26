# Elaborar um programa que calcule e armazene uma raiz de base qualquer com índice qualquer

b = int(input("Digite um valor para a base: "))
i = int(input("Digite um valor para o indice: "))

resultado = (b**(1/i))

print(f"O resultado é: {resultado:.4f}")
