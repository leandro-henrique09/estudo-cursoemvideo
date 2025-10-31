from random import randint
from time import sleep
from operator import itemgetter
jogadores = []
jogada = {}
for i in range(1,5):
    jogada['jogador'] = i
    jogada['sorteio'] = randint(0,10)
    print(f'jogador{i} tirou {jogada['sorteio']}')
    jogadores.append(jogada.copy())
    sleep(1)
ordem_jogadores = sorted(jogadores, key=lambda d: d['sorteio'], reverse=True)
print('-=' * 30)
print(f'  Ranking  ')
for c, j in enumerate(ordem_jogadores):
    print(f'  {c+1}° lugar: jogador{j['jogador']} com {j['sorteio']} ')
    sleep(1)
