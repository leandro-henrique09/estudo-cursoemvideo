# minha resolução
lista = []
pares = []
impares = []
while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  
    while continua not in 'SN':
        continua = str(input('Digite [S/N] para continuar! ')).strip().upper()[0]
    if continua == 'N':
        break
print('=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

# resolução do video:
num = list()
pares = list()
impares = list()   
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')