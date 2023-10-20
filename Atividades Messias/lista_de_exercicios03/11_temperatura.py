# Peça ao usuário para inserir a temperatura atual 
# Informe se está frio (< 15°C), ameno (entre 15°C e 25°C) ou quente (> 25°C).

temperatura = int(input('Temperatura atual: '))

if temperatura >= 26:
    print(f'{temperatura}°C clima quente')
elif temperatura >= 15:
    print(f'{temperatura}°C clima ameno')
else:
    print(f'{temperatura}°C clima frio')