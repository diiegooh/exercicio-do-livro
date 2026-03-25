# Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e apresentar como resultado final, armazenado em memória, o valor do quadrado da soma dos três valores lidos.

a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
soma = a+b+c
q = soma**2
print(f"O quadrado da soma dos valores são: {q:.2f}")