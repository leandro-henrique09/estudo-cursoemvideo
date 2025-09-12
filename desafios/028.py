# minha resposta
import random
print('=-' * 30,"""
    Vou pensar em um número entre 0 e 5. Tente Adivinhar...
""",'=-' * 30)

n = random.randint(0, 5)
tentativa = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')

if tentativa == n:
    print(f'Você acertou, o número era o {n}')
else: 
    print(f'Você errou, o número não era {tentativa}, era o {n}')

# resposta do video
from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else: 
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))