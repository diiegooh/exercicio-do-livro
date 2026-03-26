# Elaborar um programa de computador que calcule e presente o valor do volume de uma esfera. Utilize a fórmula VOLUME ← (4 / 3) * 3.14159 * (RAIO ↑ 3)

r = float(input("Digite o valor do RAIO: "))
v = (4/3)*3.14159*(r**3)

print(f"O volume é de: {v:.2f}")
