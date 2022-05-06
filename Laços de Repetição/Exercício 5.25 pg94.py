"""
Escreva um programa que calcule a raiz qudarada de um número. Utilize o método de Newton para obter um resultado aproximado.
Sendo N o número a obter a raiz quadrada, considere a base B=2.
Calcule P usando a fórmula P=(B+(N/B))/2.

Agora calcule o quadrado de P. A cada passo, faça B=P e recalcule P usando a fórmula apresentada.
Pare quando a diferença absoluta entre N e o quadrado de P for menor que 0,0001.
"""

n = float(input("Informe um número: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é {p}")