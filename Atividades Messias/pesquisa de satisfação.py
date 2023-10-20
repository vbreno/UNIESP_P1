# Uma empresa está realizando uma pesquisa de satisfação com seus clientes.
# O programa deve solicitar ao usuário a sua nota de satisfação com a empresa, de 1 a 5.
# O programa deve imprimir o número de clientes que avaliaram a empresa com cada nota.

from random import randint

clientes = 1000

respostas = []

while clientes > 0:
    respostas.append(randint(1, 5))
    clientes -= 1

resposta_1 = respostas.count(1)
resposta_2 = respostas.count(2)
resposta_3 = respostas.count(3)
resposta_4 = respostas.count(4)
resposta_5 = respostas.count(5)

print(f'Quantidade de respostas 1: {resposta_1}')
print(f'Quantidade de respostas 2: {resposta_2}')
print(f'Quantidade de respostas 3: {resposta_3}')
print(f'Quantidade de respostas 4: {resposta_4}')
print(f'Quantidade de respostas 5: {resposta_5}')