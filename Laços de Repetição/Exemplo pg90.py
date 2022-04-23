# Programa 5.1 - Contagem de Cédulas
# Testar com os valores: 501, 745, 384,2,7 e 1 TESTE OK
# Modifique o programa para trabalhar também com notas de R$100 OK
# Modifique o programa para que aceite trabalhar com valores decimais também,ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10, 0,50

# O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione,altere-o para funcioanr.
valor = float(input("Digite o valor a pagar: \n"))
cedulas = 0
atual = 100
a_pagar = valor
while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print(f"{cedulas} cédula(s) de R${atual}")
        else:
            print(f"{cedulas} moeda(s) de R${atual:5.2f}")
        if a_pagar < 0.01:
            break

        elif atual == 100:
            atual = 50

        elif atual == 50:
            atual = 20

        elif atual == 20:
            atual = 10

        elif atual == 10:
            atual = 5

        elif atual == 5:
            atual = 1

        elif atual == 1:
            atual = 0.50

        elif atual == 0.50:
            atual = 0.10

        elif atual == 0.10:
            atual = 0.05

        elif atual == 0.05:
            atual = 0.02

        elif atual == 0.02:
            atual = 0.01
        cedulas = 0
