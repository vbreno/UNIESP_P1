import random

lista_numeros = [random.randint(1, 100) for _ in range(5)]

soma_pares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        soma_pares += numero

print(f"Lista de números aleatórios: {lista_numeros}")
print(f"A soma dos números pares na lista é: {soma_pares}")