lista_numeros = []
while True:
    valor = int(input('Digite um valor: '))    
    if valor in lista_numeros:
        print('Você ja adicionou esse número antes! ')
    else:
        print('Valor adicionado com sucesso')
        lista_numeros.append(valor)
            
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in "SN":
        continua = str(input('Digite "S" para sim ou "N" para não: ')).strip().upper()[0]
        if continua == 'S':
            break    
    if continua == 'N':
        break

print(f'Você digitou os valores {sorted(lista_numeros)}')