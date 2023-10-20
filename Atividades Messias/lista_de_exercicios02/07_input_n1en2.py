# Solicite ao usuário dois números.
# Em seguida, mostre o resultado da divisão do primeiro pelo segundo apenas se o segundo número não for zero.
# Caso contrário, mostre uma mensagem de erro.


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num2 != 0:
    resultado = num1 / num2
    print(f"O resultado da divisão de {num1} por {num2} é {resultado}")
else:
    print("Erro: Não é possível dividir por zero.")
