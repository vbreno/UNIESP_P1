# Operações Aritméticas 
# Ordem de precedência (); **; *, /, //, %; +, -

# Desafio - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar

saldo = float(input('Digite o seu saldo: '))
dolar_hoje = 5.66
conversao = saldo/dolar_hoje

print(f'O seu saldo de {saldo:.2f} R$ pode comprar {conversao:.2f} US$.')