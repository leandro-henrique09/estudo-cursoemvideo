velocidade = int(input('Qual a velocidade do carro? '))
maxima = 80

if velocidade > maxima:
    print(f'Você foi multado, por exceder o limite de velocidade que é {maxima}km/h')
    print(f'A multa vai ser de R${(velocidade - maxima) * 7}, mais atenção!')
else:
    print('Sua velocidade esta dentro do permitido, Boa viagem!')