# Cadastro em while

cadastro = [
    {
        "nome": input('Digite seu nome: '),
        "idade": int(input('Digite sua idade: ')),
        "email": input('Digite o seu email: ')
    }
]

indice = 0

print('\n*** Dados do Cadastro ***\n')

while indice < len(cadastro):
    print(f'Nome: {cadastro[indice]["nome"]}')
    print(f'Idade: {cadastro[indice]["idade"]}')
    print(f'E-mail: {cadastro[indice]["email"]}')
    indice += 1