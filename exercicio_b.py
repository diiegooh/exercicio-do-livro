# Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C ← ((F – 32) * 5) / 9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

f = float(input("digite a temperatura em graus Fahrenheit: "))

c = (((f-32)*5)/9)

print(f"A temperatura em graus Celsius é: {c:.2f}")