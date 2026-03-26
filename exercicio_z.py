#Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o resultado inteiro do quadrado da divisão do valor da variável A em relação ao valor da variável B armazenado em memória

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))

div = a/b

q = div**2

print(f"O quadrado da divisão dos valores é: {q:.2f}")
