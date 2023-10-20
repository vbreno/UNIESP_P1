# Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou.
# Se a quantidade de horas extras for maior que as horas faltadas mais 50%
# imprima "Bônus de R$ 500.00". Caso contrário, imprima "Sem bônus".

horas_extras = int(input('Horas extras: '))
horas_ausentes = int(input('Horas ausentes: '))

bônus = horas_ausentes * 1.5

if horas_extras > horas_ausentes:
    print('Bônus de 500 reais!')
else:
    print('Sem bônus')
