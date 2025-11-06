from random import sample
from time import sleep

def sorteio(lst):
    print(f'Sorteando {len(lst)} valores da lista: ',end='')
    for n in lst:
        print(f'{n}',end=' ', flush=True)
        sleep(0.5)
    print(f'PRONTO!')
    sleep(0.5)

def somaPar():
    p = 0
    for n in valores:
        if n % 2 == 0:
            p += n
    print(f'Somando os valores pares de {valores}, temos {p}')


valores = list(sample(range(100), 5))
sorteio(valores)
somaPar()