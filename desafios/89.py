alunos = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break
print('-=' * 30)
print(f'N° Nome {'Média':>12}')
print('-' * 30)
for c, i in enumerate(alunos):
    print(f'{c}  {alunos[c][0]} {(alunos[c][1]+alunos[c][2])/2:>12}')
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if notas == 999:
        break
    print(f'Notas de {alunos[notas][0]} são {alunos[notas][1:]}')