"""Calculador de Média"""
x = 1
soma = 0

while x <= 5:
    n = int(input(f"Digite o {x}° número: "))
    soma = soma + n
    x = x + 1
print(f"Média é {soma/ 5:5.2f}")