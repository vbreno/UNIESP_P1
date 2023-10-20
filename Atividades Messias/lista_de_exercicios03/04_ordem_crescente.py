# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

if valor1 < valor2:
    menor = valor1
    maior = valor2
else:
    menor = valor2
    maior = valor1
    
print(f"Valores em ordem crescente: {menor}, {maior}.")