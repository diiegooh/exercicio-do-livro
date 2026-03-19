#Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula PRESTAÇÃO = VALOR + (VALOR * (TAXA / 100) * TEMPO)

valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite o valor da taxa(R$): "))
tempo = float(input("Informe os dias em atraso: "))

prestação = valor + (valor * (taxa / 100)* tempo)

print(f"O valor atual da prestação é de : {prestação:.2f}")

