# Peça ao usuário para inserir seu nome e idade
# Imprima uma mensagem informando quantos anos ele terá em 2025.

nome = input('Digite o seu nome: ')

idade = int(input('Diga a sua idade: '))

sua_idade_e = (idade) + 2

if idade >= 0:
    print(f'Sua idade em 2025 será: {sua_idade_e}')