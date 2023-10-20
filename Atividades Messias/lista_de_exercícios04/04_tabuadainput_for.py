# Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

numero = int(input('Digite um número: '))

print(f'\nTabuada do número {numero}\n')

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')