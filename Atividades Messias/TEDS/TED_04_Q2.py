# Problema: As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia
# R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

apple = int(input('Digite a quantidade de maçãs: '))

apple_price = 1.3

if apple >= 12:
    apple_price = 1

valor_compra = apple * apple_price

print(f'O valor da compra é de {valor_compra:.2f} R$')