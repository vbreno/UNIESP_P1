# Solicite ao usuário um valor numérico inteiro ou real 
# Escrever se é positivo ou negativo (considere o valor zero como positivo).

valor = float(input('Digite um valor: '))

if valor >= 0:
    print(f'O valor digitado é positivo.')

else:
    print(f'O valor digitado é negativo.')