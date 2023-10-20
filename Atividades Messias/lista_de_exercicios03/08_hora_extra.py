# Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou
# Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00"
# Caso contrário, imprima "Sem bônus".

horas_extras = int(input('Digite o número de créditos/horas: '))
faltas = int(input('Digite o número de débitos/horas: '))

bonus = horas_extras + (faltas * 0.5)

if horas_extras > faltas:
    print(f'Parabéns! Você ganhou um bônus de R$ 500,00!')
else:
    print('Sem bônus!')