# minha versão
qtd_km = int(input('Qual a distância da sua viagem? '))
if qtd_km <= 200:
    print(f'O preço da sua passagem vai ser no valor de R${qtd_km * 0.5:.2f}')
else:
    print(f'O preço da sua passagem vai ser no valor de R${qtd_km * 0.45:.2f}')

# resposta do vídeo
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))