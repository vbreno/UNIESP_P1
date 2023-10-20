# Solicite ao usuário que insira um número: 1 para o candidato A, 2 para o candidato B, 3 para o candidato C 
# Qualquer outro número para voto nulo.
# Em seguida, informe a qual candidato o voto foi destinado ou se foi nulo.

voto = int(input("Digite o número do seu candidato: "))

A = 1
B = 2
C = 3

if voto == 1:
    print("Você votou no candidato A.")
elif voto == 2:
    print("Você votou no candidato B.")
elif voto == 3:
    print("Você votou no candidato C.")
else:
    print("Seu voto é nulo.")
