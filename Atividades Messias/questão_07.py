# Escreva um programa que dê descontos de acordo com o valor da compra:
# acima de R$100, desconto de 10%; entre R$50 e R$100, desconto de 5%; abaixo de R$50, sem desconto.
# Calcule e mostre o valor do desconto e o valor total a pagar.

valor_compra = float(input('Valor da compra: R$ '))

if valor_compra > 100:
    valor_compra = valor_compra - (valor_compra * 0.10)
    print(f'O valor da compra é: R$ {valor_compra}')
    
elif 50 <= valor_compra <= 100:
    valor_compra = valor_compra - (valor_compra  * 0.05)
    print(f'O valor da compra é: R$ {valor_compra}')