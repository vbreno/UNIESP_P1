# Operações Aritméticas 
# Ordem de precedência (); **; *, /, //, %; +, -

# Desafio - Escreva um programa que leia um valor em metros 
# e exiba-o convertido em centrímetros e milímetros

metro = float(input('Digite a metragem: '))

centimeter = metro * 100
millimeter = metro * 1000

print(f'A conversão de {metro} metro(s) para centímetros tem o resultado de: {centimeter}cm.')
print(f'A conversão de {metro} metro(s) para milímetros tem o resultado de: {millimeter}mm.')