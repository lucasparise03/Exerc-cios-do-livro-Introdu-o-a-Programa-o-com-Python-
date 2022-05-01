"""
Escreva um programa que exiba uma lista de opções(menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operaão escolhida.
Repita até que a opção saída seja escolhida."""

while True:
    print("Menu: \n"
                  "1- Soma \n"
                  "2- Subtração \n"
                  "3- Divisão \n"
                  "4- Multiplicação\n"
                  "5- Para sair \n")

    opcao = int(input("Escolha uma opção: \n"))
    if opcao == "5":
        break
    elif (opcao >= 1) and (opcao < 5):
        a = int(input("Tabuada de A :"))
        contador = 1
        while contador <= 10:
            if opcao == 1:
                print(f"{a} + {contador} = {a + contador}")
            elif opcao == 2:
                print(f"{a} - {contador} = {a - contador}")
            elif opcao == 3:
                print(f"{a} % {contador} = {a % contador}")
            elif opcao == 4:
                print(f"{a} x {contador} = {a * contador}")
            contador += 1
        else:
            print("Opção inválida!")
