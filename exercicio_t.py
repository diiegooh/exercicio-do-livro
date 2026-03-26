# Construir um programa que calcule, armazene e apresente em metros por segundo o valor da velocidade de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos. Utilize a fórmula VELOCIDADE ← (DISTÂNCIA * 1000) / (TEMPO * 60).

d = float(input("Digite a DISTANCIA (em KM) percorrida: "))
t = float(input("Digite o TEMPO (em minutos) de percurso: "))

v = (d*100)/(t*60)
print(f"A velocidade foi de: {v:.2f}M/s")


