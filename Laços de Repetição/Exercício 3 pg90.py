"""
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago
Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago
"""

divida = float(input("Informe o valor da dívida: \n"))
taxa = float(input("Informe o valor do juros mensal: \n"))
valor_mensal = float(input("Informe o valor mensal que será pago: \n"))
mes = 1 #contador
if (divida * (taxa /100)) > valor_mensal:
    print("Sua dívida nunca será paga, porque os juros são superiores ao pagamento mensal!")
else:
    saldo = divida
    juros_pago = 0
    while saldo > valor_mensal:
        juros = saldo * taxa /100
        saldo = saldo + juros - valor_mensal
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês{mes} é de R${saldo:6.2f}")
        mes += 1
    print(100 *"-")
    print(f"Para pagar uma dívida de R${divida:8.2f}, a {taxa:5.2f} % de juros.")
    print(100 * "-")
    print(f"Você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
    print(100 * "-")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")
    print(100 * "-")