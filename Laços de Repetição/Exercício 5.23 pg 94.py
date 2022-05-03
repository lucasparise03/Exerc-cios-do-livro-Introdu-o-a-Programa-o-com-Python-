"""
Escreva um programa que leia um número e verifique se é ou não primo
Pra fazer essa verificaçãom calcule o resto da divisão por 2 e depois por   por todos os númeos ímpares até o número lido, Se o resto de uma dessas divisões for igual a 0, o número não é primo,
Oberse que 0 e 1 não são primos e que 2 é o único número primo par
"""

numero = int(input("Informe um número: \n"))
if numero < 0:
    print("Número inválido, insira um número maior que 0!")
if numero == 0 or numero == 1:
    print(f"{numero} é um caso especial")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(f"{numero} não é primo, porque 2 é o único número par primo")
    else:
        x = 3
        while x < numero:
            if numero % x == 0:
                break
            x += 2
        if x == numero:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo, pois é divisível por {x}")