# Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e apresentar como resultado final, armazenado em memória, o valor da soma dos quadrados dos três valores lidos.

a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
a2 = a**2
b2 = b**2
c2 = c**2
soma = a2+b2+c2
print(f"A soma dos quadrados são: {soma:.2f}")