#  Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o resultado armazenado em memória do quadrado da diferença do primeiro valor (variável A) em relação ao segundo valor (variável B).

a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
dif = a%b
quadrado = dif ** 2
print(f"O quadrado da diferença entre os valores é: {quadrado:.0f}")