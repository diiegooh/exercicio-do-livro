# Elaborar um programa que apresente o valor da conversão em dólar (US$) de um valor lido em real (R$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível com o usuário e armazenar em memória o valor da conversão antes da apresentação.

r = float(input("Digite a quantidade de reais disponiveis em carteira: "))
dolar = float(input("Digite a cotação do dolar atual: "))
conv = r / dolar
print(f"Total em dolares são: {conv:.2f}")





