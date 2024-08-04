# Operações Aritméticas 
# Ordem de precedência (); **; *, /, //, %; +, -

# Desafio - Desenvolva um programa programa que leia 
# as duas notas de um aluno, calcule e mostre a sua média

aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

media = (nota1 + nota2)/2

print(f'\nA média da soma das notas {nota1} e {nota2} do aluno {aluno} é {media:.2f}')