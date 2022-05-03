"""
Altere o programa anterior, escreva os n primeiros números primos
"""

numero = int(input("Digite um número: ")) # Entrada
if numero < 0: # teste para ver se o número é positivo
    print("Número inválido, digite um número maior que 0")
else:
    if numero >= 1: # validação se número é maior ou igual a 1
        print("2")
        p = 1  # variável para usar no loop
        y = 3
        while p < numero: # se P é menor que número execute
            x = 3
            while x < y: # enquanto X for menor que Y execute
                if y % x == 0: # se resto de Y dividido por X for igual a 0, saia
                    break
                x += 2
            if x == y:  # se X for igual a Y
                print(x)
                p = p + 1
            y += 2