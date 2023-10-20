# Ler as notas da 1ª e 2ª avaliações de um aluno. 
# Calcular a média aritmética simples.
# Escrever uma mensagem que diga se o aluno foi ou não aprovado (média >= 6).
# Escrever também o resultado da média calculada.

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'Média {media}. Aluno aprovado!')
else:
    print(f'Média {media}. Aluno reprovado!')