# Lista de convidados while

convidados = ['luva de pedreiro', 'Cremosinho','Toguro','Inês Brasil','Neymar','Vitão','Anitta','Chico Buarque']

def enviar_convite(convidado):
    print(f'\nOlá, {convidado}! Você está convidado para um jantar em minha casa.\n')

indice = 0

while indice < len(convidados):
    enviar_convite(convidados[indice])
    indice += 1

print("\n*** Desistência ***\n")
nao_pode_comparecer = "Chico Buarque"
print(f"{nao_pode_comparecer} não pode comparecer ao jantar.")
convidados.remove(nao_pode_comparecer)

novos_convidados = ['Mc Pipokinha','Simaria','Mc Biro Leyby','Pablo Vittar','Léo Dias']
convidados.extend(novos_convidados)

# Enviar convites atualizados
print("\n*** Convites atualizados ***")
indice = 0
while indice < len(convidados):
    enviar_convite(convidados[indice])
    indice += 1