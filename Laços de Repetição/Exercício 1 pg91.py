"""
Escreva um programa que leia núemros inteiros do teclado
O programa deve ler os números até que o usuário digite 0
No final da execução . exiba a quantidade de números digitados. assim como a soma e a média aritmética
"""
soma = 0
contador = 0
while True:
    numero = int(input("Informe um valor: "))
    if numero == 0:
        break
    else:
        contador += 1
        soma = soma + numero
print(36 *"-")
print(f"Total de números digitados: {contador}\n"
      f"Soma dos números: {soma}\n"
      f"Média dos números {soma / contador}")
print(36 *"-")