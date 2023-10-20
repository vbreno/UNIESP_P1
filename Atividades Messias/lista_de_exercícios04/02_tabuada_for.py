# Faça um programa que mostre as tabuadas dos números de 1 a 10.

for tabuada in range(1, 11):
    print(f'\nTabuada do {tabuada}:\n')

    for numero in range(1, 11):
        resultado = tabuada * numero
        print(f'{tabuada} x {numero} = {resultado}')


# Tabuada em while

tabuada = 1

while tabuada <= 10:
    print(f'\nA tabuada do {tabuada}\n')

    
    numero = 1

    while numero <= 10:
        resultado = tabuada * numero
        print(f'{tabuada} x {numero} = {resultado}')
        numero += 1
    tabuada +=1