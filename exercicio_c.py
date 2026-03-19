# Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME ← 3.14159 * R ↑ 2 * ALTURA.

r = float(input("insira o valor do Raio: "))
a = float(input("insira o valor da Altura: "))

volume = ((3.14159)*(r**2)*a)

print(f"O volume da lata de óleo é {volume:.2f}")
