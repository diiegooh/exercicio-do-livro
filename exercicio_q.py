#  Elaborar um programa que calcule e apresente o valor do resultado da área de uma circunferência (variável A). O programa deve solicitar a entrada do valor do raio da circunferência (variável R). Para a execução deste problema, utilize a fórmula A ← 3.14159265* R ↑ 2.

r = float(input("Digite o valor do raio da circunferencia: "))
a = (3.14159265 * r)**2
print(f"O valor da área é: {a:.2f}")
