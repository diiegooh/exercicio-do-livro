# Elaborar um programa que leia dois valores numéricos reais desconhecidos representados pelas variáveis A e B. Calcular, armazenar e apresentar os resultados das quatro operações aritméticas básicas.

a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"A soma dos fatores é de: {soma:.0f}")
print(f"A subtracao dos fatores é de: {subtracao:.0f}")
print(f"A multiplicação dos fatores é de: {multiplicacao:.0f}")
print(f"A divisão dos fatores é de: {divisao:.1f}")
