# trabalhando com Módulos

'''Faça um programa que leia o comprimento do cateto oposto 
e do cateto adjacente de um triângulo retângulo 
calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)
print(f'O valor da hipotenusa é {hipotenusa:.2f}.')