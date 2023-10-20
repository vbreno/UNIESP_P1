# Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

cadastro = [
    {
        "nome": input('Digite seu nome: '),
        "idade": int(input('Digite sua idade: ')),
        "email": input('Digite o seu email: ')
    }
]

print('\n*** Dados do Cadastro ***\n')

for dados in cadastro:
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados["idade"]}')
    print(f'E-mail: {dados["email"]}')