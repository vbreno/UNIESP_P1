# Peça ao usuário para inserir três lados de um triângulo 
# Determine se é um triângulo equilátero, isósceles ou escaleno.

l1 = int(input('Digite um valor: '))
l2 = int(input('Digite um valor: '))
l3 = int(input('Digite um valor: '))

equilatero = (l1 == l2 == l3)
isoceles = (l1 == l2) or (l1 == l3) or (l2 == l3)

if equilatero:
    print(f'É um triângulo equilátero.')
elif isoceles:
    print(f'É um triângulo isóceles.')
else:
    print('É um triângulo escaleno.')