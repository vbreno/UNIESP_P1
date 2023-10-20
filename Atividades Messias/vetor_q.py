import random

Q = [random.randint(0, 100) for _ in range(20)]

maior_valor = Q[0]
menor_valor = Q[0]
posicao_maior = 0
posicao_menor = 0

for i in range(1, 20):
    if Q[i] > maior_valor:
        maior_valor = Q[i]
        posicao_maior = i
    if Q[i] < menor_valor:
        menor_valor = Q[i]
        posicao_menor = i

print("Vetor Q:", Q)
print(f"O maior elemento de Q é {maior_valor} e ocupa a posição {posicao_maior} no vetor.")
print(f"O menor elemento de Q é {menor_valor} e ocupa a posição {posicao_menor} no vetor.")
