# Construir um programa que leia um valor numérico inteiro e apresente como resultado armazenado em memória os seus valores sucessor e antecessor

a = int(input("Digite um valor: "))
ante = a - 1
suce = a + 1

print(f"O antecessor é: {ante:.0f}")
print(f"O sucessor é: {suce:.0f}")
