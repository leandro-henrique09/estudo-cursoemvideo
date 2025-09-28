while True:
    tab = int(input('Digite um número para ver a tabuada: '))
    if tab < 0:
        break
    for i in range(1,11):    
        print(f'{tab} x {i:2} = {tab * i}')

print('Programa de Tabuada Encerrado. Volte sempre')