""""
Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
Utilize a tabela de código a seguir para obter o preço de cada produto.

Código   Preço
   1 --- 0,50
   2 --- 1,00
   3 --- 4,00
   5 --- 7,00
   9 --- 8,00

Seu programa deve exibir o total de compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de "Código Inválido"
"""


a_pagar = 0

while True: # enquanto verdadeiro execute
    codigo_produto = int(input("Informe o código do produto desejado: \n")) # Entrada do código do produto
    preço = 0
    if codigo_produto == 0: # se código do produto == 0, saia
        break
    elif codigo_produto == 1: # se código do produto == 1, selecione o produto de código 1
        preço = 0.50 # variaevl preço == variável local
    elif codigo_produto == 2: # se código do produto == 2, selecione o produto de código 2
        preço = 1.00
    elif codigo_produto == 3: # se código do produto == 3, selecione o produto de código 3
        preço = 4.00
    elif codigo_produto == 5: # se código do produto == 5, selecione o produto de código 5
        preço = 7.00
    elif codigo_produto == 9: # se código do produto == 9, selecione o produto de código 9
        preço = 8.00
    else:
        print("Código Inválido!") # se código do produto == inválido, preencha corretamente
    if preço != 0:
        quantidade = int(input("Quantidade desejada: \n"))
        a_pagar = a_pagar + (preço * quantidade)
    print(f"Total a pagar é R${a_pagar}")