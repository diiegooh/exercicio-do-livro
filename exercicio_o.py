# Elaborar um programa que leia quatro valores numéricos inteiros (variáveis A, B, C e D). Ao final, o programa deve apresentar o resultado, armazenado em memória, do produto (variável P) do primeiro com o terceiro valor, e o resultado da soma (variável S) do segundo com o quarto valor.

a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
d = float(input("Digite um valor para D: "))
p = a*c
s = b+d
print(f"O produto de A e C = {p:.0f}")
print(f"A soma de B e D = {s:.0f}")
