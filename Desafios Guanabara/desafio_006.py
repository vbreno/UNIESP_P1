# Operações Aritméticas 
# Ordem de precedência (); **; *, /, //, %; +, -

# Desafio - Crie um algoritmo que leia um número 
# e mostre o seu dobro, o triplo e a raíz quadrada

numero = int(input('Digite um valor: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'\nO dobro de {numero} é {dobro}.')
print(f'\nO triplo de {numero} é {triplo}.')
print(f'\nA raíz quadrada de {numero} é {raiz:.2f}.')

print(f'\nO número {numero} terá como dobro {numero*2}, o seu triplo é {numero*3} e a sua raíz quadrada será {pow(numero, 1/2)}')