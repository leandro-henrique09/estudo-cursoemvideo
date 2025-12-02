# minha resolução
lista = []
while True: 
    lista.append(int(input('Digite um valor: '))) 
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'NS':
       continua = str(input('Digite um valor valido!!!!! [S/N] ')).strip().upper()[0] 
    if continua == 'N':
        break

dec = sorted(lista, reverse= True)
print('=-' * 30)
print(f'Foram digitados {len(lista)} números')
print(f'A lista de números em ordem decrescente ficou: {dec}')
if 5 in lista:
    print('O valor 5 estava presente na lista!')
else:
    print('O valor 5 não estava presente na lista!') 

# resolução do video

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não foi encontrado na lista')