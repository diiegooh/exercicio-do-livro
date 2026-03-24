#Ler dois valores para as variáveis A e B e efetuar a troca dos valores de forma que a variável Apasse a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentaros valores após a efetivação do processamento da troca.

a = float(input("Digite um valor para A: "))
b = float(input("Digite outro valor para B: "))

c = a
a = b
b = c
print(f"Agora A vale: {a:.0f}")
print(f"Agora B vale: {b:.0f}")

      
      