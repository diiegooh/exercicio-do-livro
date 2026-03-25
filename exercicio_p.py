# Elaborar um programa que leia o valor numérico correspondente ao salário mensal (variável SM) de um trabalhador e também fazer a leitura do valor do percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS) após o armazenamento do cálculo em memória.

sm = float(input("Digite o valor do salario mensal: "))
pr = float(input("Digite o percentual de ajuste do salario: "))
porcem = pr / 100
valorRs = sm * porcem
salarioAtual = sm + valorRs
print(f"O Salario com reajuste ficou: {salarioAtual:.2f}")
