# Crie um programa que calcule a média de 4 notas
# Mostre se o aluno foi aprovado (média maior ou igual a 7) ou reprovado.

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
n3 = float(input('Digite uma nota: '))
n4 = float(input('Digite uma nota: '))

media = (n1+n2+n3+n4) / 4

if media > 7:
    print(f'Média: {media}')
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')