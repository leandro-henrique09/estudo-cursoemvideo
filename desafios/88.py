from random import sample
from time import sleep
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(1, qtd_jogos+1):
    print(f'Jogo {i}: {list(sample(range(60), 6))}')
    sleep(0.5)
