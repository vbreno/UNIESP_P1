''' trabalhando com Módulos

Crie um programa que leia um número real qualquer pelo teclado 
e mostre na tela a sua porção inteira.'''

from math import trunc

num = float(input('Digite um valor: '))

print(trunc(num))

# Outro forma de resolução da questão acima:

'''num = float(input('Digite um valor real: '))

print(f'O valor digitado foi {num} e o seu valor inteiro é {int(num)}')'''