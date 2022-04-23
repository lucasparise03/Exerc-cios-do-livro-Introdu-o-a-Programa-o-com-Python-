"""
Altere o programa anterior de forma a perguntar também o valor depositado mensalmente
Esse vaolr será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
"""

deposito = float(input("Informe o valor do depósito: \n"))
taxa = float(input("Informe o valor da taxa: \n"))
investimento_mensal = float(input("Informe o valor do investimento mensal: \n"))
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento_mensal
    print(f"Saldo do mês {mes}, é {saldo:5.2f}")
    mes += 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}")

# Se repetiu o código anterior inteiro, apenas adicionando a variável "investimento_mensal" que armazena o valor que será investido mensalmente