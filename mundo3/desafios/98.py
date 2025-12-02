from time import sleep
def linha():
    print('-=' * 30)

def contagemUsuario(i, f, p):
    p = abs(p)  
    if p == 0:
        p = 1    
    if f < i: 
        for c in range(i, f-1, -p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
    elif f > i:
        for c in range(i, f+1, p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
    print('FIM!')

linha()
print(f'Contagem de 1 até 10 de 1 em 1')
for i in range(1, 11):
    print(f'{i}', end=' ', flush=True)
    sleep(0.5) 
print(f'FIM!')
linha()
print(f'Contagem de 10 até 0 de 2 em 2')
for i in range(10, -1, -2):
    print(f'{i}', end=' ', flush=True)
    sleep(0.5)
print(f'FIM!')
linha()

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagemUsuario(inicio, fim, passo)
