# Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12 quilômetros por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO) e a velocidade média (variável VELOCIDADE) durante a viagem. Dessa forma, será possível obter a distância percorrida com a fórmula DISTÂNCIA ← TEMPO * VELOCIDADE. A partir do valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula LITROS_USADOS ← DISTÂNCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

tempo = float(input("Digite o tempo gasto com a viagem(em minutos): "))
velocidade = float(input("Digite a velociade média: "))

tempo2  = tempo / 60
kmPorL = 12
distancia = tempo2 * velocidade

litrosUtilizado = distancia / kmPorL

print(f"Velocidade média: {velocidade:.0f}")
print(f"Tempo gasto na viagem: {tempo:.0f} minutos")
print(f"Distancia percorrida: {distancia:.0f}Km")
print(f"Quantidade de litros utilizados de gasolina: {litrosUtilizado:.2f}Km/l")

      
