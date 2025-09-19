from random import randint
print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogada = int(input('Qual a sua jogada? '))
maquina = randint(0,2)

if maquina == 0 and jogada == 1:
    print('-=-' * 30)
    print(f'Computador jogou Pedra \nJogador jogou Papel')
    print('-=-' * 30)
    print('Jogador venceu')   
elif maquina == 1 and jogada == 2:
    print('-=-' * 30)
    print(f'Computador jogou Papel \nJogador jogou Tesoura')
    print('-=-' * 30)
    print('Jogador venceu')
elif maquina == 2 and jogada == 0:
    print('-=-' * 30)
    print(f'Computador jogou Tesoura \nJogador jogou Pedra')
    print('-=-' * 30)
    print('Jogador venceu')
elif jogada == 0 and maquina == 1:
    print('-=-' * 30)
    print(f'Computador jogou Papel \nJogador jogou Pedra')
    print('-=-' * 30)
    print('Computador venceu.')
elif jogada == 1 and maquina == 2:
    print('-=-' * 30)
    print(f'Computador jogou Tesoura \nJogador jogou Papel')
    print('-=-' * 30)
    print('Computador venceu.')
elif jogada == 2 and maquina == 0:
    print('-=-' * 30)
    print(f'Computador jogou Pedra \nJogador jogou Tesoura')
    print('-=-' * 30)
    print('Computador venceu.')
elif jogada == maquina:
    print('Empate, os dois jogaram a mesma coisa!')
else:
    print('Selecione uma opção válida!')
