# minha resolução
valores = []
for i in range(1,6):
    valores.append(int(input(f'Digite o {i}° número: ')))

maior_valor = max(valores)
minimo_valor = min(valores)
posições_maiores = []
posições_menores = []

for c ,v in enumerate(valores):
    if v == maior_valor:
        posições_maiores.append(c+1)
    elif v == minimo_valor:
        posições_menores.append(c+1)

print(f'O maior valor foi {maior_valor} e ele apareceu nas posições: ', end='')
print(*posições_maiores)
print(f'O menor valor foi {minimo_valor} e ele apareceu nas posições: ',end='')
print(*posições_menores)

# resolução do video
listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai}')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men}')
for i, v in enumerate(listanum):
    if v ==  men:
        print(f'{i}...', end='')
print()