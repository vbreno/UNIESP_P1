# Tabuada input em while

numero = int(input('Digite um número: '))

print(f'\nTabuada do {numero}\n')

i = 1

while i <= 10:
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    i += 1