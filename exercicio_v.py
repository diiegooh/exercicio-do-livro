# Elaborar um programa que leia dois valores numéricos inteiros, os quais devem representar a base e o expoente de uma potência, calcular a potência, armazenar em memória o resultado calculado e apresentar o resultado obtido

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))

p = a**b

print(f"O resultado potencia é: {p:.0f}")