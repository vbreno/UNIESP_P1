# Escreva um programa que verifique se um número é maior, menor ou igual a 50.

numero = int(input('Digite um número: '))

if numero < 50:
    print(f'O número é menor do que 50.')
elif numero > 50:
        print(f'O número é maior do que 50.')
else:
    print('O número é 50.')