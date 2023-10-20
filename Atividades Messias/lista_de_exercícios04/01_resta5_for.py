# Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 
# Quando divididos por 11 produzam o resto igual a 5.

for numeros in range(1000, 2000):
    if numeros %11 == 5:
        print(f'O número é {numeros}')

# em while

numero = 999

while numero <= 2000:
    if numero %11 == 5:
        print(f'O número é {numero}')
        numero += 1