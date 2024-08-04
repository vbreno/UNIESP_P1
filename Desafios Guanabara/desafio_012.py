# Operações Aritméticas 
# Ordem de precedência (); **; *, /, //, %; +, -

# Desafio - Faça um algoritmo que leia o preço de um produto 
# e mostre o seu novo preço com 5% de desconto

nome = input('Digite o nome do produto: ')

produto = float(input('Digite o preço do produto: '))

desconto = produto - (produto * 0.05)

print(f'O preco final do produto {nome} com o desconto de 5% será de {desconto:.2f}.')