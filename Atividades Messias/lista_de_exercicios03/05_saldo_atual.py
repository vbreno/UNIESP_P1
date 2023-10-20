# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
# Calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo'
# Senão escrever a mensagem 'Saldo Negativo'.

import random

conta_corrente = (random.randint(1, 999999))
saldo = float(random.randint(-1000, 3000))
credito = float(random.randint(0, 500))
debito = float(random.randint(-1000, 0))

saldo_atual = (saldo + debito) + credito

print(f'\nnúmero da conta corrente: {conta_corrente}\n')
print(f'\nsaldo da conta corrente: {saldo:.2f}\n')
print(f'\ncrédito da conta corrente: {credito:.2f}\n')
print(f'\ndébito: {debito:.2f}\n')

if saldo_atual >=0:
    print(f'Seu saldo atual é: {saldo_atual:,.2f}. Saldo positivo!')
else:
    print(f'Seu saldo atual é: {saldo_atual:,.2f}. Saldo negativo!')