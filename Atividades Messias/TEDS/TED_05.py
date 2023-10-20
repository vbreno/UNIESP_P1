# Faça um programa que mostre as tabuadas dos números de 1 a 10.

for n in range(0, 11):
    print(f"\nTabuada do {n}:\n")

    for t in range(0, 11):
        resultado = n * t
        print(f"{n} x {t} = {resultado}")