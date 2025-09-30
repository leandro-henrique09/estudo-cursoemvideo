# minha resposta
from random import randint
from time import sleep

count = 0
print('Sou seu computador...')
sleep(1.0)
print('Acabei de pensar em um número entre 0 e 10...')
sleep(1.0)
print('Será que você consegue adivinhar?')
sleep(1.0)
num_computador = randint(0, 10)
palpite = int(input('Qual é seu palpite? '))

while palpite != num_computador:
    if palpite > num_computador:
        palpite = int(input('Menos...tente denovo '))
    else:
        palpite = int(input('Mais...tente denovo '))
    
    count += 1
print(f'Acertou com {count} tentativas. Parabéns')

#  resposta do video
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns')