#Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares disponível com o usuário e armazenar em memória o valor da conversão antes da apresentação.
d = float(input("Digite a quantidade de dolares disponiveis em carteira: "))
dolar = float(input("Digite a cotação do dolar atual: "))
conv = d / dolar
print(f"Total em reais são: {conv:.2f}")


