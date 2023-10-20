# Peça ao usuário para inserir a velocidade atual de um carro
# Informe se ele está abaixo do limite (80 km/h), ou se ele deverá ser multado (acima de 80 km/h)
# Se ele for multado, informe que a multa será de R$5,00 por km acima do limite

velocidade = int(input('Digite a velocidade: '))

multa = (velocidade - 80) * 5

if velocidade <= 80:
    print(f'{velocidade} KM/h. dentro do limite de velocidade')
else:
    print(f'Você foi multado em {multa:.2f} R$ por excesso de velocidade')