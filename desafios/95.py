jogadores = []
gols = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))   
    total = sum(gols)
    jogador['total'] = total
    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())
    continua = str(input('Quer continuar? [S/N] ' )).upper().strip()[0]
    while continua not in 'SN':      
        continua = str(input('Digite S ou N, para continuar ou parar: ')).strip().upper()[0]
    if continua == 'N':
        break

print('-=' * 30)
print(f' {'cod '} {'nome':<15} {'gols':<16} {'total':<15}')
print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:>3}   {v['nome']:<15}  {str(v['gols']):<16} {v['total']:<15}')
while True:
    dados_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados_jogador == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[dados_jogador]['nome']}')
    for k, v in enumerate(jogadores[dados_jogador]['gols']):
        print(f'  => No jogo {k+1} fez {v} gols.')