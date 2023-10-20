# Peça ao usuário para inserir uma senha.
# Se a senha for "Python123", imprima "Acesso concedido".
# Caso contrário, imprima "Acesso negado".

digite_senha = input('Digite a senha: ')

senha = 'Python123'

if digite_senha == senha:
    print('Acesso concedido.')
else:
    print('Acesso negado.')