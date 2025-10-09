times = ('Palmeiras','Flamengo','Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia',
'Fluminense','São Paulo', 'Bragantino', 'Ceará', 'Vasco da Gama','Corinthians','Grêmio','Atlético-MG',
'Internacional', 'Santos', 'Vitoria', 'Fortaleza', 'Juventude', 'Sport Recife')

print('-=' * 30)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)

for cont, time in enumerate(times):
    if time == 'São Paulo':
        print(f'O São Paulo está em {cont+1}° no campeonato!')
        break