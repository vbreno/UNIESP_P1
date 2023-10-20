# Dada a equação ‘ax + b = 0’, peça ao usuário os valores de a e b e resolva a equação.

a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))

x = -b/a

if a and b != 0:
    print(f'O valor de x é {x}')