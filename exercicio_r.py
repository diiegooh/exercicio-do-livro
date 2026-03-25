# Em uma eleição sindical concorreram ao cargo de presidente três candidatos (representados pelas variáveis A, B e C). Durante a apuração dos votos foram computados votos nulos e em branco, além dos votos válidos para cada candidato. Deve ser criado um programa de computador que faça a leitura da quantidade de votos válidos para cada candidato, além de ler também a quantidade de votos nulos e em branco. Ao final, o programa deve apresentar o número total de eleitores, considerando votos válidos, nulos e em branco; o percentual correspondente de votos válidos em relação à quantidade de eleitores; o percentual correspondente de votos válidos do candidato A em relação à quantidade de eleitores; o percentual correspondente de votos válidos do candidato B em relação à quantidade de eleitores; o percentual correspondente de votos válidos do candidato C em relação à quantidade de eleitores; o percentual correspondente de votos nulos em relação à quantidade de eleitores; e, por último, o percentual correspondente de votos em branco em relação à quantidade de eleitores. Todos os cálculos devem efetivamente ser armazenados em memória.

a = int(input("Digite a quantidade de votos do candidato A: "))
b = int(input("Digite a quantidade de votos do candidato B: "))
c = int(input("Digite a quantidade de votos do candidato C: "))
nulo = int(input("Digite a quantidade de votos nulos: "))
branco = int(input("Digite a quantidade de votos em branco: "))

eleitores = a + b + c + nulo + branco

votosValidos = (((a+b+c)*100)/eleitores)
aPorcem = ((a*100)/eleitores)
bPorcem = ((b*100)/eleitores)
cPorcem = ((c*100)/eleitores)
brancoPorcem = ((branco*100)/eleitores)
nuloPorcem = ((nulo*100)/eleitores)

print(f"Quantidade de eleitores: {eleitores:.0f}")
print(f"Percentual de votos validos: {votosValidos:.0f}%")
print(f"Percentual de votos do candidato A: {aPorcem:.0f}%")
print(f"Percentual de votos do candidato B: {bPorcem:.0f}%")
print(f"Percentual de votos do candidato C: {cPorcem:.0f}%")
print(f"Percentual de votos nulos: {nuloPorcem:.0f}%")
print(f"Percentual de votos em branco: {brancoPorcem:.0f}%")




