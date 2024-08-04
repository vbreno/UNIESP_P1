# Dados Primitivos

# Desafio - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

valor = input('Digite um valor: ')

print(type(valor))
print(f'O valor é numérico?', valor.isnumeric())
print(f'O valor é alfanumérico?', valor.isalnum())
print(f'O valor é alfabético?', valor.isalpha())
print(f'O valor é decimal?', valor.isdecimal())
print(f'O valor é minúsculo?', valor.islower())
print(f'O valor é maiúsculo?', valor.isupper())
print(f'O valor é imprimível?', valor.isprintable())
print(f'O valor é espaço?', valor.isspace())
print(f'O valor é capitalizada?', valor.istitle())