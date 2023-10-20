# Escreva um programa que dê descontos de acordo com o valor da compra
# Acima de R$100, desconto de 10%; entre R$50 e R$100, desconto de 5%; abaixo de R$50, sem desconto
# Calcule e mostre o valor do desconto e o valor total a pagar.

valor_compra = float(input('Digite o valor da compra: '))
1
desconto = 0

if valor_compra >= 100:
    desconto = valor_compra * 0.1
elif 50 <= valor_compra < 100:
    desconto = valor_compra * 0.05
else:
    print('Compra sem desconto.')

preco_final = valor_compra - desconto

print(f'Valor a pagar com desconto: {preco_final:.2f}')
print(f'Desconto: -{desconto:.2f}')