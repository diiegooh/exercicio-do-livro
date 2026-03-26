#Elaborar um programa que leia uma medida em pés, calcular, armazenar e apresentar o seu valor convertido em metros, lembrando que um pé mede 0,3048 metro, ou seja, um pé é igual a 30,48 centímetros.

p = float(input("Digite uma medidida em PÉS: "))
m = (p*0.3048)

print(f"A conversão para metros é de: {m:.2f} metros")
