# Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
# Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
# Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites.
# Imprima o nome das pessoas que não poderão comparecer.
# Modifique sua lista, substitua os desistentes por novos convidados.
# Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ['luva de pedreiro', 'Cremosinho','Toguro','Inês Brasil','Neymar','Vitão','Mionzinho',
'Anitta','Chico Buarque']

def enviar_convites(convidados):
    for convidado in convidados:
        print(f'\nOlá, {convidado}! Te convido a participar do jantar em minha casa.\n')

enviar_convites(convidados)

print('\n*** Desistência ***\n')
desistentes = 'Chico Buarque'
print(f'\n{desistentes} não poderá comparecer ao jantar.\n')
convidados.remove(desistentes)

novos_convidados = ['Mc Pipokinha','Simaria','Mc Biro Leyby','Pablo Vittar','Léo Dias']
convidados.extend(novos_convidados)
print(f'\n*** Convites atualizados ***\n')
enviar_convites(convidados)