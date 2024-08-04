# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado 
# E a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

km = float(input('Digite a quantidade de KM rodados: '))

diária = int(input('Por quantos dias o carro foi alugado? '))

aluguel = (km * 0.15) + (diária * 60)

print(f'O valor total do aluguel do carro é de R${aluguel}.')