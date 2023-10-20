# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
else:
    maior = valor2

print(f"O maior valor entre {valor1} e {valor2} é {maior}.")
