# Crie um programa em Python que solicite um número do usuário
# Depois some este número com 1357, multiplique por 8, divida por 5 e eleve ao quadrado.

numero = float(input("Digite um número: "))


resultado = ((numero + 1357) * 8 / 5) ** 2

print(f"O resultado é: {resultado:,.2f}")