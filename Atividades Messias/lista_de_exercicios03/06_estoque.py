# Faça um algoritmo para ler: quantidade atual em estoque 
# Quantidade máxima em estoque e quantidade mínima em estoque de um produto.
# Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra'
# Senão escrever a mensagem 'Efetuar compra'.

import random

estoque_atual = int(random.randint(1, 200))
estoque_max = int(random.randint(1, 200))
estoque_min = 50
media_estoque = (estoque_max + estoque_min) / 2

if estoque_atual >= 50:
    print(f'Estoque atual {estoque_atual}. Não repor estoque.')
else:
    print(f'Estoque atual {estoque_atual}. Repor estoque.')