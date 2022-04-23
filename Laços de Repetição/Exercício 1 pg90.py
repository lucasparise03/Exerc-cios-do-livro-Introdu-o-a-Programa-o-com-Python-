"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período
"""

deposito = float(input("Informe quanto vai depositar: \n")) # Informa qual será o valor depositado
taxa = float(input("Informe o valor da taxa: \n")) # Informa qual será o valor da taxa de juros
mes = 1 # contador de meses
saldo = deposito

while mes <= 24: # Enquanto mes for menor ou igual que 24, continue rodando
    saldo = saldo + (saldo * taxa / 100)
    print(f"Saldo do mês {mes}, é R${saldo}")
    mes += 1 # Toda vez que passar para o próximo mês, o contador aumenta 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}")
