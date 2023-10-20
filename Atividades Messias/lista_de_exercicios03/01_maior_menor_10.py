# Solicite ao usuário um valor numérico, inteiro ou real (float)
# Verifique se ele é maior ou menor que 10.
# O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

numero = float(input('Digite um número: '))

if numero < 10:
    print(f'O número que você digitou é menor do que 10. {numero} < 10.')
elif numero > 10:
    print(f'O número que você digitou é maior do que 10. {numero} > 10')
else:
    print('O número digitado é 10.')