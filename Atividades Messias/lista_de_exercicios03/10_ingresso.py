# Escreva um programa que pergunte ao usuário sua idade e informe o valor do ingresso do cinema
# Abaixo de 12 anos e acima de 60, R$ 15.00; entre 12 e 60 anos, R$ 25.00.

idade = int(input('Informe sua idade: '))

ingresso = 25.00

if idade <= 12 or idade >= 60:
    ingresso = 15.00

print(f'O valor do ingresso é {ingresso:.2f} R$')