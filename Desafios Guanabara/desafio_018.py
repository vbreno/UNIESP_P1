# trabalhando com Módulos

''' Faça um programa que leia um ângulo qualquer 
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan

angulo = float(input('Digite o ângulo: '))

s = sin(angulo)
c = cos(angulo)
t = tan(angulo)

print(f'O ângulo digitado tem como seno {s:.2f}, cosseno {c:.2f} e tangente {t:.2f}.')