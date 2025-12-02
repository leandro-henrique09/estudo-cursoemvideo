pessoas = []
dados = []
pesos = []
maior = []
menor = []
while True:
    dados.append(str(input('Nome: '))) 
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    pesos.append(dados[1])
    dados.clear()
    
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break
mai = max(pesos)
men = min(pesos)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
for c, p in enumerate(pesos):
    if p == mai:
        maior.append(pessoas[c][0])
    elif p == men:
        menor.append(pessoas[c][0])
print(f'O maior peso foi de {mai:.1f}Kg. Peso de {maior}')
print(f'O menor peso foi de {men:.1f}Kg. Peso de {menor}')


    
