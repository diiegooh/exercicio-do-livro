#Ler quatro valores numéricos inteiros e apresentar o resultado das adições e das multiplicações utilizando o mesmo raciocínio aplicado quando o uso de propriedades distributivas para a máxima combinação possível entre as quatro variáveis. Não é para calcular a propriedade distributiva,apenas para usar a sua forma de combinação. Considerando a leitura de valores para as variáveis A, B, C e D, devem ser feitas seis adições e seis multiplicações, ou seja, deve ser combinadaa variável A com a variável B, a variável A com a variável C, a variável A com a variável D.Depois é necessário combinar a variável B com a variável C e a variável B com a variável D e,por fim, a variável C será combinada com a variável D

a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
d = float(input("Digite um valor para D: "))

#Soma
sab = a + b
sac = a + c
sad = a + d

sbc = b + c
sbd = b + d

scd = c + d

#Multiplicação
mab = a * b
mac = a * c
mad = a * d

mbc = b * c
mbd = b * d

mcd = c * d

print(f"A + B = {sab:.0f}")
print(f"A + C = {sac:.0f}")
print(f"A + D = {sad:.0f}")
print(f"B + C = {sbc:.0f}")
print(f"B + D = {sbd:.0f}")
print(f"C + D = {scd:.0f}")

print(f"A x B = {mab:.0f}")
print(f"A x C = {mac:.0f}")
print(f"A x D = {mad:.0f}")
print(f"B x C = {mbc:.0f}")
print(f"B x D = {mbd:.0f}")
print(f"C x D = {mcd:.0f}")
