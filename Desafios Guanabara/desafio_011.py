# Operações Aritméticas 
# Ordem de precedência (); **; *, /, //, %; +, -

# Desafio - Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta para pintá-la
# Cada litro de tinta pinta uma área de 2m²

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = altura * largura

tinta = area / 2

print(f'Para pintar {area} m² será necessário {tinta}L de tinta.')