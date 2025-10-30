# minha resposta foi a mesma do video
matriz = [[],[],[]]
for i in range(0,3):
    for m in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{m}]: ')))
for i in range(0,3):
    for m in range(0,3):
        print(f'[{matriz[i][m]:^5}]',end='')
    print()