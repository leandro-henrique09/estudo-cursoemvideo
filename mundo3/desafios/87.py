# minha resolução
matriz = [[],[],[]]
pares = 0
coluna_tres = 0
for i in range(0,3):
    for m in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{m}]: ')))
for i in range(0,3):
    for m in range(0,3):
        print(f'[{matriz[i][m]:^5}]',end='')
        if matriz[i][m] % 2 == 0:
            pares += matriz[i][m]
        if m == 2:
            coluna_tres += matriz[i][m]
    print()

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna_tres}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

# resolução do video
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')