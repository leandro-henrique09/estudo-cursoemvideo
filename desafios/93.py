# minha resposta foi exatamente a mesma do vídeo
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for k, v in enumerate(jogador['gols']):
        print(f' => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')