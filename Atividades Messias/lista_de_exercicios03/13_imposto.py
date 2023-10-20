# Peça ao usuário para inserir seu salário mensal.
# Calcule o imposto de renda com base no seguinte: até R$2000, isento 
# R$2000,01 até R$3500, 10%;
# Acima de R$3500, 15%.

salario = float(input('Salário: '))

imposto = 0

if salario >= 3500:
    imposto = salario * 0.15
elif 2001 < salario <= 3500:
    imposto = salario * 0.1
else:
    print(f'Isento de imposto de renda')

renda = salario - imposto

print(f'Sua renda este mês é: R$ {renda:.2f}')